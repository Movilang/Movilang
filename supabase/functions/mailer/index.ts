// MoviLang · листи: вітання, нагадування через 3 дні, кинутий кошик, відповідь викладача.
// Секрети: RESEND_API_KEY (resend.com), MAIL_FROM (напр. "MoviLang <hello@movilang.pl>"), SITE_URL, CRON_SECRET (будь-який довгий рядок).
// «Verify JWT» вимкнути. Щоденний запуск — GitHub Actions (.github/workflows/daily.yml) з заголовком x-cron-secret.
// Ручний виклик від адміна: POST {type:"answer", question_id} з токеном адміністратора.
import { createClient } from "npm:@supabase/supabase-js@2.45.4";

const CORS = { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type, x-cron-secret", "Access-Control-Allow-Methods": "POST, OPTIONS" };
const json = (o: unknown, s = 200) => new Response(JSON.stringify(o), { status: s, headers: { ...CORS, "Content-Type": "application/json" } });
const esc = (s: string) => String(s || "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]!));
const shell = (body: string, site: string) => `<div style="font-family:Arial,sans-serif;max-width:520px;margin:auto;padding:24px;border-radius:14px;background:#111;color:#eee"><h2 style="color:#ff4d5a;margin-top:0">MoviLang</h2>${body}<p style="color:#888;font-size:12px;margin-top:28px">MoviLang · <a style="color:#888" href="${site}/#/cabinet">wypisz się z przypomnień w kabinecie</a></p></div>`;

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  const KEY = Deno.env.get("RESEND_API_KEY");
  if (!KEY) return json({ error: "RESEND_API_KEY not set" }, 503);
  const from = Deno.env.get("MAIL_FROM") || "MoviLang <onboarding@resend.dev>";
  const site = (Deno.env.get("SITE_URL") || "https://movilang.pages.dev").replace(/\/$/, "");
  const admin = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
  const send = async (to: string, subject: string, html: string) => {
    const r = await fetch("https://api.resend.com/emails", { method: "POST", headers: { Authorization: "Bearer " + KEY, "Content-Type": "application/json" }, body: JSON.stringify({ from, to, subject, html: shell(html, site) }) });
    return r.ok;
  };
  // запис у журнал → якщо вже було, не надсилаємо
  const once = async (uid: string, kind: string, ref: string) => { const { error } = await admin.from("email_log").insert({ user_id: uid, kind, ref }); return !error; };
  const body = await req.json().catch(() => ({}));

  // ---- відповідь викладача (виклик з адмінки) ----
  if (body.type === "answer") {
    const jwt = (req.headers.get("Authorization") || "").replace("Bearer ", "");
    const { data: ud } = await admin.auth.getUser(jwt);
    const { data: me } = await admin.from("profiles").select("role").eq("id", ud?.user?.id || "").maybeSingle();
    if (me?.role !== "admin") return json({ error: "admin only" }, 403);
    const { data: q } = await admin.from("questions").select("*").eq("id", body.question_id).maybeSingle();
    if (!q || !q.answer || !q.email) return json({ error: "no answer" }, 400);
    const ok = await send(q.email, "💬 Odpowiedź na Twoje pytanie — MoviLang", `<p>Twoje pytanie:</p><blockquote style="border-left:3px solid #555;padding-left:10px;color:#bbb">${esc(q.text)}</blockquote><p>Odpowiedź:</p><blockquote style="border-left:3px solid #ff4d5a;padding-left:10px">${esc(q.answer).replace(/\n/g, "<br>")}</blockquote><p><a style="color:#ff4d5a" href="${site}/#/${q.lesson_id ? "lesson/" + q.lesson_id : "cabinet"}">Wróć do lekcji →</a></p>`);
    return json({ ok });
  }

  // ---- щоденний прогін ----
  if (req.headers.get("x-cron-secret") !== Deno.env.get("CRON_SECRET")) return json({ error: "forbidden" }, 403);
  const now = Date.now(), H = 3600000, out = { welcome: 0, reminder: 0, cart: 0 };
  const { data: users } = await admin.from("profiles").select("id,email,name,nick,created_at,marketing,role").neq("role", "admin");

  for (const u of users || []) {
    if (!u.email) continue;
    const name = esc(u.nick || u.name || "");
    const age = now - new Date(u.created_at).getTime();
    // 1) вітання — у першу добу
    if (age < 48 * H && await once(u.id, "welcome", "")) {
      if (await send(u.email, "👋 Witaj w MoviLang!", `<p>Cześć${name ? " " + name : ""}!</p><p>Cieszymy się, że jesteś. Trzy rzeczy na start:</p><ol><li><a style="color:#ff4d5a" href="${site}/#/test">Zrób test poziomu</a> (3 minuty) — podpowiemy kurs.</li><li><a style="color:#ff4d5a" href="${site}/#/trial">Przejdź darmową lekcję</a>.</li><li>Ustaw dzienny cel w kabinecie — 1 lekcja dziennie wystarczy.</li></ol>`)) out.welcome++;
      continue;
    }
    if (!u.marketing) continue;
    // 2) нагадування — 3+ дні без активності (не частіше ніж раз на 14 днів)
    const { data: last } = await admin.from("activity").select("day").eq("user_id", u.id).order("day", { ascending: false }).limit(1).maybeSingle();
    const lastT = last?.day ? new Date(last.day).getTime() : new Date(u.created_at).getTime();
    if (now - lastT > 3 * 24 * H && now - lastT < 30 * 24 * H) {
      const ref = new Date(Math.floor(now / (14 * 24 * H)) * 14 * 24 * H).toISOString().slice(0, 10);
      if (await once(u.id, "reminder", ref) && await send(u.email, "🎬 Twoja seria czeka — wróć na 10 minut", `<p>Hej${name ? " " + name : ""}!</p><p>Nie było Cię od kilku dni. Jedna krótka lekcja i seria znów rośnie.</p><p><a style="display:inline-block;background:#ff4d5a;color:#fff;padding:10px 18px;border-radius:8px;text-decoration:none" href="${site}/#/cabinet">Kontynuuj naukę →</a></p>`)) out.reminder++;
    }
  }

  // 3) кинутий кошик: pending > 2 год, < 3 днів, без оплачених після нього
  const { data: pend } = await admin.from("orders").select("id,user_id,email,course_id,bundle,created_at").eq("status", "pending").lt("created_at", new Date(now - 2 * H).toISOString()).gt("created_at", new Date(now - 72 * H).toISOString());
  for (const o of pend || []) {
    if (!o.user_id || !o.email) continue;
    const { count } = await admin.from("orders").select("id", { count: "exact", head: true }).eq("user_id", o.user_id).eq("status", "paid").gte("created_at", o.created_at);
    if (count) continue;
    let what = "pakiet wszystkich kursów", link = site + "/#/pricing";
    if (!o.bundle && o.course_id) { const { data: c } = await admin.from("courses").select("title_pl,title").eq("id", o.course_id).maybeSingle(); what = c?.title_pl || c?.title || "kurs"; link = site + "/#/course/" + o.course_id; }
    if (await once(o.user_id, "cart", o.id) && await send(o.email, "🛒 Zostawiłeś coś w koszyku", `<p>Zacząłeś zakup: <b>${esc(what)}</b>, ale płatność się nie zakończyła.</p><p>Jeśli coś poszło nie tak (BLIK, karta) — spróbuj jeszcze raz albo napisz do nas.</p><p><a style="display:inline-block;background:#ff4d5a;color:#fff;padding:10px 18px;border-radius:8px;text-decoration:none" href="${link}">Wróć do zakupu →</a></p>`)) out.cart++;
  }
  return json(out);
});
