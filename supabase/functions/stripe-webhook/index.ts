// MoviLang · webhook Stripe: po opłaceniu tworzy klucz, aktywuje go i odblokowuje kurs.
// Секрети: STRIPE_WEBHOOK_SECRET (whsec_…). Функцію розгорнути з вимкненим «Verify JWT».
import { createClient } from "npm:@supabase/supabase-js@2.45.4";

const enc = new TextEncoder();
async function hmac(secret: string, msg: string) {
  const k = await crypto.subtle.importKey("raw", enc.encode(secret), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const sig = await crypto.subtle.sign("HMAC", k, enc.encode(msg));
  return [...new Uint8Array(sig)].map((b) => b.toString(16).padStart(2, "0")).join("");
}
function genCode() { const a = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"; let s = ""; const r = crypto.getRandomValues(new Uint8Array(12)); for (const x of r) s += a[x % a.length]; return s; }

Deno.serve(async (req) => {
  const secret = Deno.env.get("STRIPE_WEBHOOK_SECRET");
  const raw = await req.text();
  if (!secret) return new Response("no secret", { status: 503 });
  const head = req.headers.get("stripe-signature") || "";
  const parts = Object.fromEntries(head.split(",").map((p) => { const i = p.indexOf("="); return [p.slice(0, i), p.slice(i + 1)]; }));
  const t = parts["t"], v1s = head.split(",").filter((p) => p.startsWith("v1=")).map((p) => p.slice(3));
  if (!t || !v1s.length) return new Response("bad sig", { status: 400 });
  if (Math.abs(Date.now() / 1000 - Number(t)) > 600) return new Response("old", { status: 400 });
  const expected = await hmac(secret, t + "." + raw);
  if (!v1s.includes(expected)) return new Response("bad sig", { status: 400 });

  const ev = JSON.parse(raw);
  if (!["checkout.session.completed", "checkout.session.async_payment_succeeded"].includes(ev.type)) return new Response("ignored");
  const s = ev.data.object;
  if (s.payment_status !== "paid") return new Response("not paid yet");

  const admin = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
  const { data: ord } = await admin.from("orders").select("*").eq("session_id", s.id).maybeSingle();
  if (ord && ord.status === "paid") return new Response("already");
  const uid = s.metadata?.user_id || ord?.user_id, bundle = s.metadata?.bundle === "1", cid = s.metadata?.course_id || null;
  const code = genCode(), now = new Date().toISOString();
  await admin.from("access_keys").insert({ code, course_id: bundle ? null : cid, activated_by: uid || null, activated_at: uid ? now : null });
  if (uid) {
    if (bundle) {
      const { data: cs } = await admin.from("courses").select("id").eq("published", true);
      if (cs?.length) await admin.from("enrollments").upsert(cs.map((c) => ({ user_id: uid, course_id: c.id })), { onConflict: "user_id,course_id", ignoreDuplicates: true });
    } else if (cid) await admin.from("enrollments").upsert({ user_id: uid, course_id: cid }, { onConflict: "user_id,course_id", ignoreDuplicates: true });
  }
  const row = { status: "paid", paid_at: now, key_code: code, amount: s.amount_total ?? ord?.amount ?? 0 };
  if (ord) await admin.from("orders").update(row).eq("id", ord.id);
  else await admin.from("orders").insert({ ...row, session_id: s.id, user_id: uid, email: s.customer_details?.email, course_id: bundle ? null : cid, bundle });
  return new Response("ok");
});
