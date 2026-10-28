// MoviLang · переклад слова з урахуванням контексту речення і переклад цілого речення.
// Секрети (одне з двох): DEEPL_API_KEY (deepl.com → API Free/Pro) або GOOGLE_TRANSLATE_KEY (Google Cloud Translation API).
// DeepL — краще: має параметр context (речення-контекст для одного слова).
// POST {text, context?, src: 'en'|'pl'|'uk', dst: 'en'|'pl'|'uk'} → {text, provider}
import { createClient } from "npm:@supabase/supabase-js@2.45.4";

const CORS = { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type", "Access-Control-Allow-Methods": "POST, OPTIONS" };
const json = (o: unknown, s = 200) => new Response(JSON.stringify(o), { status: s, headers: { ...CORS, "Content-Type": "application/json" } });
const LANG = new Set(["en", "pl", "uk"]);
const DL_TARGET: Record<string, string> = { en: "EN-GB", pl: "PL", uk: "UK" };

async function sha(s: string) { const b = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s)); return [...new Uint8Array(b)].map((x) => x.toString(16).padStart(2, "0")).join("").slice(0, 40); }

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  try {
    const { text, context, src, dst } = await req.json();
    const t = String(text || "").trim(), ctx = String(context || "").trim().slice(0, 600);
    if (!t || t.length > 600 || !LANG.has(src) || !LANG.has(dst) || src === dst) return json({ error: "bad request" }, 400);
    const admin = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
    const key = await sha([src, dst, t, ctx].join("|"));
    const { data: hit } = await admin.from("tr_cache").select("out,provider").eq("key", key).maybeSingle();
    if (hit) return json({ text: hit.out, provider: hit.provider, cached: true });

    let out = "", provider = "";
    const DK = Deno.env.get("DEEPL_API_KEY"), GK = Deno.env.get("GOOGLE_TRANSLATE_KEY");
    if (DK) {
      const host = DK.endsWith(":fx") ? "https://api-free.deepl.com" : "https://api.deepl.com";
      const body: Record<string, unknown> = { text: [t], source_lang: src.toUpperCase(), target_lang: DL_TARGET[dst] };
      if (ctx && ctx !== t) body.context = ctx;
      const r = await fetch(host + "/v2/translate", { method: "POST", headers: { Authorization: "DeepL-Auth-Key " + DK, "Content-Type": "application/json" }, body: JSON.stringify(body) });
      const j = await r.json().catch(() => ({}));
      if (!r.ok) return json({ error: j?.message || "DeepL HTTP " + r.status }, 502);
      out = j?.translations?.[0]?.text || ""; provider = "deepl";
    } else if (GK) {
      // Google не має параметра context: перекладаємо речення, де слово позначене тегом, і витягаємо переклад цього фрагмента.
      const useCtx = ctx && ctx !== t && ctx.toLowerCase().includes(t.toLowerCase());
      const q = useCtx ? ctx.replace(new RegExp(t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "i"), (m) => "<b>" + m + "</b>") : t;
      const r = await fetch("https://translation.googleapis.com/language/translate/v2?key=" + GK, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ q, source: src, target: dst, format: useCtx ? "html" : "text" }) });
      const j = await r.json().catch(() => ({}));
      if (!r.ok) return json({ error: j?.error?.message || "Google HTTP " + r.status }, 502);
      const full = String(j?.data?.translations?.[0]?.translatedText || "");
      const m = useCtx ? full.match(/<b>([\s\S]*?)<\/b>/i) : null;
      out = (m ? m[1] : full).replace(/<[^>]+>/g, "").replace(/&#39;/g, "'").replace(/&quot;/g, '"').replace(/&amp;/g, "&").trim(); provider = "google";
      if (useCtx && !m) { // тег загубився — перекладаємо слово окремо
        const r2 = await fetch("https://translation.googleapis.com/language/translate/v2?key=" + GK, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ q: t, source: src, target: dst, format: "text" }) });
        out = String((await r2.json())?.data?.translations?.[0]?.translatedText || out);
      }
    } else return json({ error: "no translation key (DEEPL_API_KEY / GOOGLE_TRANSLATE_KEY)" }, 503);

    if (out) await admin.from("tr_cache").upsert({ key, src, dst, text: t.slice(0, 600), out, provider });
    return json({ text: out, provider });
  } catch (e) { return json({ error: String((e as Error).message || e) }, 500); }
});
