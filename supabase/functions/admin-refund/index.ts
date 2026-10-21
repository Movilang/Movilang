// MoviLang · повернення коштів (тільки адміністратор): Stripe refund + закриття доступу.
// Секрети: STRIPE_SECRET_KEY. «Verify JWT» можна лишити ввімкненим.
import { createClient } from "npm:@supabase/supabase-js@2.45.4";

const CORS = { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type", "Access-Control-Allow-Methods": "POST, OPTIONS" };
const json = (o: unknown, s = 200) => new Response(JSON.stringify(o), { status: s, headers: { ...CORS, "Content-Type": "application/json" } });

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  try {
    const SK = Deno.env.get("STRIPE_SECRET_KEY");
    if (!SK) return json({ error: "STRIPE_SECRET_KEY not set" }, 503);
    const admin = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
    const jwt = (req.headers.get("Authorization") || "").replace("Bearer ", "");
    const { data: ud } = await admin.auth.getUser(jwt);
    const { data: me } = await admin.from("profiles").select("role").eq("id", ud?.user?.id || "").maybeSingle();
    if (me?.role !== "admin") return json({ error: "admin only" }, 403);

    const { order_id, ticket_id, revoke = true } = await req.json();
    const { data: o } = await admin.from("orders").select("*").eq("id", order_id).maybeSingle();
    if (!o) return json({ error: "order not found" }, 404);
    if (o.status === "refunded") return json({ error: "already refunded" }, 400);
    let pi = o.payment_intent;
    if (!pi) {
      const r = await fetch("https://api.stripe.com/v1/checkout/sessions/" + o.session_id, { headers: { Authorization: "Bearer " + SK } });
      pi = (await r.json())?.payment_intent;
    }
    if (!pi) return json({ error: "no payment_intent" }, 400);
    const f = new URLSearchParams(); f.set("payment_intent", pi);
    const r = await fetch("https://api.stripe.com/v1/refunds", { method: "POST", headers: { Authorization: "Bearer " + SK, "Content-Type": "application/x-www-form-urlencoded" }, body: f });
    const j = await r.json();
    if (!r.ok) return json({ error: j?.error?.message || "Stripe error" }, 502);

    if (revoke && o.user_id && !o.gift) {
      if (o.bundle) await admin.from("enrollments").delete().eq("user_id", o.user_id);
      else if (o.course_id) await admin.from("enrollments").delete().eq("user_id", o.user_id).eq("course_id", o.course_id);
    }
    if (o.key_code) await admin.from("access_keys").delete().eq("code", o.key_code);
    await admin.from("orders").update({ status: "refunded", refunded_at: new Date().toISOString() }).eq("id", o.id);
    if (ticket_id) await admin.from("tickets").update({ status: "refunded", updated_at: new Date().toISOString() }).eq("id", ticket_id);
    return json({ ok: true, refund: j.id });
  } catch (e) { return json({ error: String((e as Error).message || e) }, 500); }
});
