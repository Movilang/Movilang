-- MoviLang · кеш перекладів (щоб не платити двічі за те саме слово/речення). Запустити один раз.
create table if not exists public.tr_cache (
  key text primary key,
  src text, dst text, text text, out text, provider text,
  created_at timestamptz not null default now()
);
alter table public.tr_cache enable row level security;  -- доступ лише з Edge Function (service role)
select 'ok' as status;
