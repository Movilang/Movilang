// MoviLang — налаштування підключення до бази даних Supabase.
// Поки поля порожні, сайт працює в ДЕМО-режимі (дані лише в браузері).
// Як заповнити — див. README.md, крок 2.
// Адреса сайту. Щоб змінити домен: python3 tools/set-domain.py нова-адреса.pl
window.MOVILANG_SITE = {
  URL: "https://movielang.pages.dev",   // головна адреса сайту
  REDIRECT_FROM: []                     // старі адреси, з яких автоматично перекидати на URL
};
window.MOVILANG_CONFIG = {
  SUPABASE_URL: "https://pybzpbkmdupvtsmxlqvr.supabase.co",       // напр. "https://abcdefgh.supabase.co"
  SUPABASE_ANON_KEY: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InB5YnpwYmttZHVwdnRzbXhscXZyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTE2MjMxMjMsImV4cCI6MjEwNzE5OTEyM30.2pMZ-wHdsCXhLnkSH0t5DluePC4TInsCSeSf8vMz6w8"   // Project Settings → API → anon public key
};
