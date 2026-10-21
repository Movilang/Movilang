// MoviLang · webhook Stripe: po opłaceniu tworzy klucz, odblokowuje kurs (albo przygotowuje prezent),
// nalicza bonus polecającemu i wysyła e-maile (jeśli ustawiono RESEND_API_KEY).
// Секрети: STRIPE_WEBHOOK_SECRET (whsec_…); опційно RESEND_API_KEY, MAIL_FROM, SITE_URL. «Verify JWT» вимкнути.
import { createClient } from "npm:@supabase/supabase-js@2.45.4";

const enc = new TextEncoder();
async function hmac(secret: string, msg: string) {
  const k = await crypto.subtle.importKey("raw", enc.encode(secret), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const sig = await crypto.subtle.sign("HMAC", k, enc.encode(msg));
  return [...new Uint8Array(sig)].map((b) => b.toString(16).padStart(2, "0")).join("");
}
function genCode() { const a = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"; let s = ""; const r = crypto.getRandomValues(new Uint8Array(12)); for (const x of r) s += a[x % a.length]; return s; }
const fmtKey = (c: string) => c.replace(/(.{4})(?=.)/g, "$1-");
const esc = (s: string) => String(s || "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]!));

async function mail(to: string, subject: string, html: string) {
  const key = Deno.env.get("RESEND_API_KEY"); if (!key || !to) return;
  const from = Deno.env.get("MAIL_FROM") || "MoviLang <onboarding@resend.dev>";
  await fetch("https://api.resend.com/emails", { method: "POST", headers: { Authorization: "Bearer " + key, "Content-Type": "application/json" }, body: JSON.stringify({ from, to, subject, html }) }).catch(() => {});
}
const shell = (body: string) => `<div style="font-family:Arial,sans-serif;max-width:520px;margin:auto;padding:24px;border-radius:14px;background:#111;color:#eee"><h2 style="color:#ff4d5a;margin-top:0">MoviLang</h2>${body}<p style="color:#888;font-size:12px;margin-top:28px">MoviLang — angielski, polski i ukraiński z filmów i seriali.</p></div>`;

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

  const site = (Deno.env.get("SITE_URL") || "https://movilang.pages.dev").replace(/\/$/, "");
  const admin = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
  const { data: ord } = await admin.from("orders").select("*").eq("session_id", s.id).maybeSingle();
  if (ord && ord.status === "paid") return new Response("already");
  const uid = s.metadata?.user_id || ord?.user_id, bundle = s.metadata?.bundle === "1", cid = s.metadata?.course_id || null;
  const gift = s.metadata?.gift === "1" || !!ord?.gift;
  const code = genCode(), now = new Date().toISOString();

  // подарунок: ключ НЕ активується — його активує отримувач
  await admin.from("access_keys").insert({ code, course_id: bundle ? null : cid, activated_by: gift ? null : uid || null, activated_at: gift ? null : uid ? now : null });
  if (uid && !gift) {
    if (bundle) {
      const { data: cs } = await admin.from("courses").select("id").eq("published", true);
      if (cs?.length) await admin.from("enrollments").upsert(cs.map((c) => ({ user_id: uid, course_id: c.id })), { onConflict: "user_id,course_id", ignoreDuplicates: true });
    } else if (cid) await admin.from("enrollments").upsert({ user_id: uid, course_id: cid }, { onConflict: "user_id,course_id", ignoreDuplicates: true });
  }

  // реферали: перша оплата запрошеного → +1 бонус тому, хто запросив; використаний бонус — списати
  if (uid) {
    const { data: prof } = await admin.from("profiles").select("referred_by,ref_credits").eq("id", uid).maybeSingle();
    const { count: paidBefore } = await admin.from("orders").select("id", { count: "exact", head: true }).eq("user_id", uid).eq("status", "paid");
    if (prof?.referred_by && !paidBefore) {
      const { data: rp } = await admin.from("profiles").select("ref_credits").eq("id", prof.referred_by).maybeSingle();
      await admin.from("profiles").update({ ref_credits: (rp?.ref_credits || 0) + 1 }).eq("id", prof.referred_by);
    }
    if (ord?.ref_used && (prof?.ref_credits || 0) > 0) await admin.from("profiles").update({ ref_credits: prof!.ref_credits - 1 }).eq("id", uid);
  }

  const row = { status: "paid", paid_at: now, key_code: code, amount: s.amount_total ?? ord?.amount ?? 0, payment_intent: s.payment_intent || null };
  if (ord) await admin.from("orders").update(row).eq("id", ord.id);
  else await admin.from("orders").insert({ ...row, session_id: s.id, user_id: uid, email: s.customer_details?.email, course_id: bundle ? null : cid, bundle, gift });

  // листи
  let what = "wszystkie kursy MoviLang";
  if (!bundle && cid) { const { data: c } = await admin.from("courses").select("title_pl,title").eq("id", cid).maybeSingle(); what = c?.title_pl || c?.title || what; }
  const buyer = s.customer_details?.email || ord?.email;
  if (gift) {
    await mail(buyer, "🎁 Twój prezent MoviLang jest gotowy", shell(`<p>Dziękujemy! Kupiłeś(-aś) prezent: <b>${esc(what)}</b>.</p><p>Kod prezentowy:</p><p style="font-size:22px;letter-spacing:2px;background:#222;padding:12px;border-radius:8px;text-align:center"><b>${fmtKey(code)}</b></p><p>Przekaż go bliskiej osobie albo wydrukuj kartkę prezentową na stronie zamówienia.</p>`));
    if (ord?.gift_to) await mail(ord.gift_to, "🎁 Masz prezent: kurs w MoviLang!", shell(`<p>Ktoś bliski podarował Ci kurs <b>${esc(what)}</b>.</p>${ord.gift_msg ? `<blockquote style="border-left:3px solid #ff4d5a;padding-left:10px;color:#ccc">${esc(ord.gift_msg)}</blockquote>` : ""}<p>Twój kod:</p><p style="font-size:22px;letter-spacing:2px;background:#222;padding:12px;border-radius:8px;text-align:center"><b>${fmtKey(code)}</b></p><p><a style="color:#ff4d5a" href="${site}/#/register">Załóż konto</a> i wpisz kod w swoim kabinecie.</p>`));
  } else {
    await mail(buyer, "✅ Kurs odblokowany — MoviLang", shell(`<p>Płatność przyjęta! Kurs <b>${esc(what)}</b> jest już na Twoim koncie.</p><p>Klucz (na wszelki wypadek): <b>${fmtKey(code)}</b></p><p><a style="color:#ff4d5a" href="${site}/#/cabinet">Przejdź do kabinetu →</a></p>`));
  }
  return new Response("ok");
});
