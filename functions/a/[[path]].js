// Audio clips stored in Cloudflare R2 (binding: AUDIO). GET = public playback, PUT = admin upload.
const SB_URL = "https://pybzpbkmdupvtsmxlqvr.supabase.co";
const SB_ANON = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InB5YnpwYmttZHVwdnRzbXhscXZyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTE2MjMxMjMsImV4cCI6MjEwNzE5OTEyM30.2pMZ-wHdsCXhLnkSH0t5DluePC4TInsCSeSf8vMz6w8";
const OK_PATH = /^g\/(en|pl|uk)\/[0-9a-f]{16}\.wav$/;

async function isAdmin(req) {
  const auth = req.headers.get("Authorization") || "";
  if (!/^Bearer\s+\S+/.test(auth)) return false;
  const u = await fetch(SB_URL + "/auth/v1/user", { headers: { apikey: SB_ANON, Authorization: auth } });
  if (!u.ok) return false;
  const user = await u.json();
  const p = await fetch(SB_URL + "/rest/v1/profiles?select=role&id=eq." + encodeURIComponent(user.id), { headers: { apikey: SB_ANON, Authorization: auth } });
  if (!p.ok) return false;
  const rows = await p.json();
  return rows[0] && rows[0].role === "admin";
}

export async function onRequest({ request, env, params }) {
  const path = [].concat(params.path || []).join("/");
  if (!OK_PATH.test(path)) return new Response("bad path", { status: 400 });
  if (!env.AUDIO) return new Response("R2 binding AUDIO missing", { status: 503 });
  if (request.method === "GET" || request.method === "HEAD") {
    const obj = await env.AUDIO.get(path);
    if (!obj) return new Response("not found", { status: 404 });
    return new Response(request.method === "HEAD" ? null : obj.body, { headers: { "Content-Type": "audio/wav", "Cache-Control": "public, max-age=31536000, immutable", ETag: obj.httpEtag } });
  }
  if (request.method === "PUT") {
    if (!(await isAdmin(request))) return new Response("admin only", { status: 403 });
    const body = await request.arrayBuffer();
    if (body.byteLength < 100 || body.byteLength > 3_000_000) return new Response("size", { status: 400 });
    await env.AUDIO.put(path, body, { httpMetadata: { contentType: "audio/wav", cacheControl: "public, max-age=31536000, immutable" } });
    return Response.json({ ok: true, path });
  }
  return new Response("method", { status: 405 });
}
