// MoviLang · створення оплати Stripe Checkout (картка, BLIK, Przelewy24).
// Секрети (Supabase → Edge Functions → Secrets): STRIPE_SECRET_KEY, SITE_URL (напр. https://movilang.pages.dev)
import { createClient } from "npm:@supabase/supabase-js@2.45.4";

const CORS = { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type", "Access-Control-Allow-Methods": "POST, OPTIONS" };
const json = (o: unknown, s = 200) => new Response(JSON.stringify(o), { status: s, headers: { ...CORS, "Content-Type": "application/json" } });
const grosze = (p: string | null) => { const m = String(p || "").replace(",", ".").match(/\d+(\.\d+)?/); return m ? Math.round(parseFloat(m[0]) * 100) : 0; };

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  try {
    const SK = Deno.env.get("STRIPE_SECRET_KEY");
    if (!SK) return json({ error: "Płatności nie są jeszcze skonfigurowane (brak STRIPE_SECRET_KEY)." }, 503);
    const url = Deno.env.get("SUPABASE_URL")!, service = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
    const site = (Deno.env.get("SITE_URL") || req.headers.get("origin") || "https://movilang.pages.dev").replace(/\/$/, "");
    const admin = createClient(url, service);
    const jwt = (req.headers.get("Authorization") || "").replace("Bearer ", "");
    const { data: ud } = await admin.auth.getUser(jwt);
    const user = ud?.user;
    if (!user) return json({ error: "Zaloguj się, aby kupić kurs." }, 401);

    const body = await req.json().catch(() => ({}));
    const bundle = !!body.bundle;
    let name = "", amount = 0, courseId: string | null = null;
    if (bundle) {
      const { data: s } = await admin.from("site_settings").select("value").eq("key", "bundle_price").maybeSingle();
      amount = grosze(s?.value || "149 zł") || 14900; name = "MoviLang — wszystkie kursy";
    } else {
      const { data: c } = await admin.from("courses").select("id,title_pl,title,price,published").eq("id", body.course_id).maybeSingle();
      if (!c || !c.published) return json({ error: "Nie znaleziono kursu." }, 404);
      amount = grosze(c.price); courseId = c.id; name = "MoviLang — " + (c.title_pl || c.title);
    }
    if (amount < 200) return json({ error: "Nieprawidłowa cena." }, 400);

    const f = new URLSearchParams();
    f.set("mode", "payment");
    f.set("success_url", site + "/#/paid/{CHECKOUT_SESSION_ID}");
    f.set("cancel_url", site + (courseId ? "/#/course/" + courseId : "/#/pricing"));
    f.set("customer_email", user.email || "");
    f.set("client_reference_id", user.id);
    f.set("locale", "pl");
    f.set("line_items[0][quantity]", "1");
    f.set("line_items[0][price_data][currency]", "pln");
    f.set("line_items[0][price_data][unit_amount]", String(amount));
    f.set("line_items[0][price_data][product_data][name]", name);
    f.set("metadata[user_id]", user.id);
    f.set("metadata[course_id]", courseId || "");
    f.set("metadata[bundle]", bundle ? "1" : "0");
    const r = await fetch("https://api.stripe.com/v1/checkout/sessions", { method: "POST", headers: { Authorization: "Bearer " + SK, "Content-Type": "application/x-www-form-urlencoded" }, body: f });
    const s = await r.json();
    if (!r.ok) return json({ error: s?.error?.message || "Stripe error" }, 502);
    await admin.from("orders").insert({ user_id: user.id, email: user.email, session_id: s.id, course_id: courseId, bundle, amount, currency: "pln", status: "pending" });
    return json({ url: s.url });
  } catch (e) { return json({ error: String((e as Error).message || e) }, 500); }
});
