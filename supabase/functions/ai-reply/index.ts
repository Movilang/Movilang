import "jsr:@supabase/functions-js/edge-runtime.d.ts";

// In-character reply to a learner's letter (and follow-up messages in the same thread).
const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};
const NAME: Record<string, string> = { en: "English", pl: "Polish", uk: "Ukrainian" };
function json(b: unknown, s = 200) { return new Response(JSON.stringify(b), { status: s, headers: { ...CORS, "Content-Type": "application/json" } }); }
const SCHEMA = { type: "OBJECT", properties: { who: { type: "STRING" }, reply: { type: "STRING" } }, required: ["who", "reply"] };
const clip = (v: unknown, n: number) => String(v ?? "").replace(/<[^>]+>/g, "").trim().slice(0, n);

async function tfetch(url: string, init: RequestInit, ms: number) {
  const c = new AbortController(); const t = setTimeout(() => c.abort(), ms);
  try { return await fetch(url, { ...init, signal: c.signal }); } finally { clearTimeout(t); }
}
function models(): string[] {
  const pref = Deno.env.get("GEMINI_MODEL");
  return [...new Set([pref, "gemini-flash-latest", "gemini-flash-lite-latest"].filter(Boolean) as string[])];
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  if (req.method !== "POST") return json({ error: "method" }, 405);
  const t0 = Date.now();
  let b: any = {};
  try { b = await req.json(); } catch { return json({ error: "bad_json" }, 400); }
  const target = NAME[b.target] ? b.target : "en";
  const text = clip(b.text, 3000), task = clip(b.task, 600);
  const course = clip(b.course, 120), lesson = clip(b.lesson, 160), scene = clip(b.scene, 600), who = clip(b.who, 60);
  const history = (Array.isArray(b.history) ? b.history : []).slice(-12).map((m: any) => ({ r: m && m.r === "me" ? "me" : "char", t: clip(m && m.t, 1500) })).filter((m: any) => m.t);
  if (text.length < 3) return json({ error: "empty" }, 400);
  const key = (Deno.env.get("GEMINI_API_KEY") || Deno.env.get("GEMINI_KEY") || Deno.env.get("GOOGLE_API_KEY") || "").trim();
  if (!key) return json({ error: "no_key" }, 503);

  const sys = `You are a character from "${course}" writing back to a language learner, fully in character (voice, personality, catchphrases, what you know at this point of the story).
The learner is studying ${NAME[target]} at about B1 level. In the course lesson "${lesson}" (${scene}) they got this writing task: "${task}".
${who ? `You are ${who}.` : `Work out from the task who the letter is addressed to (the recipient) and become that character. If the task has no clear recipient, choose the most fitting main character of the lesson.`}
Rules:
- Write ONLY in ${NAME[target]}, simple and natural B1 language (short sentences, everyday words; a few words typical for the character are fine).
- React to what the learner actually wrote: quote or mention 1-2 concrete details, show emotion, stay true to the story without spoiling later events.
- 70-140 words. Letter or chat style fitting the situation. Sign with the character's name if it's a letter.
- End with one question that invites the learner to write back.
- Never correct grammar here (another teacher does that). Never mention being an AI. Keep it friendly and safe for teenagers; if the learner writes something inappropriate, gently steer back to the story.
Return JSON: who = the character's name, reply = your message.`;

  const contents: any[] = [{ role: "user", parts: [{ text }] }];
  for (const m of history) contents.push({ role: m.r === "me" ? "user" : "model", parts: [{ text: m.t }] });
  if (history.length && history[history.length - 1].r !== "me") return json({ error: "nothing_to_answer" }, 400);

  let last = "";
  for (const model of models()) {
    const left = 45000 - (Date.now() - t0);
    if (left < 6000) break;
    let r: Response;
    try {
      r = await tfetch(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent`, {
        method: "POST",
        headers: { "Content-Type": "application/json", "x-goog-api-key": key },
        body: JSON.stringify({ systemInstruction: { parts: [{ text: sys }] }, contents, generationConfig: { temperature: 0.8, responseMimeType: "application/json", responseSchema: SCHEMA } }),
      }, Math.min(30000, left - 2000));
    } catch { last = `${model} timeout`; continue; }
    if (!r.ok) { last = `${model} -> ${r.status}: ${(await r.text()).slice(0, 200)}`; console.error("ai-reply:", last); continue; }
    const j = await r.json();
    const out = (j?.candidates?.[0]?.content?.parts || []).filter((p: any) => !p.thought).map((p: any) => p.text || "").join("").replace(/^```json\s*|```\s*$/g, "");
    try {
      const res = JSON.parse(out);
      if (!res.reply) throw 0;
      return json({ who: clip(res.who, 60) || who || "?", reply: clip(res.reply, 2500), model });
    } catch { last = `${model} parse`; }
  }
  return json({ error: "busy", detail: last }, 503);
});
