-- MoviLang · оновлення 2026-10-18: оплата онлайн, пакет, серія днів, повторення слів.
-- Можна запускати повторно.

-- ===== Замовлення (Stripe) =====
create table if not exists public.orders (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references public.profiles(id) on delete set null,
  email text,
  session_id text unique,
  course_id uuid references public.courses(id) on delete set null,
  bundle boolean not null default false,
  amount int not null default 0,
  currency text not null default 'pln',
  status text not null default 'pending',
  key_code text,
  created_at timestamptz not null default now(),
  paid_at timestamptz
);
alter table public.orders enable row level security;
drop policy if exists p_orders_sel on public.orders;
create policy p_orders_sel on public.orders for select using (user_id = auth.uid() or public.is_admin());

-- ===== Повторення слів (інтервали 1-3-7-14-30 днів) =====
create table if not exists public.word_review (
  user_id uuid references public.profiles(id) on delete cascade,
  target text not null,
  word text not null,
  meaning text,
  step int not null default 0,
  due date not null default current_date,
  updated_at timestamptz not null default now(),
  primary key (user_id, target, word)
);
alter table public.word_review enable row level security;
drop policy if exists p_wr_all on public.word_review;
create policy p_wr_all on public.word_review for all using (user_id = auth.uid()) with check (user_id = auth.uid());

-- ===== Активність по днях (серія 🔥 і денна ціль) =====
create table if not exists public.activity (
  user_id uuid references public.profiles(id) on delete cascade,
  day date not null,
  lessons int not null default 0,
  reviews int not null default 0,
  primary key (user_id, day)
);
alter table public.activity enable row level security;
drop policy if exists p_act_sel on public.activity;
create policy p_act_sel on public.activity for select using (user_id = auth.uid() or public.is_admin());

create or replace function public.bump_activity(p_day date, p_lessons int, p_reviews int) returns void
language plpgsql security definer set search_path = public as $$
begin
  if auth.uid() is null then return; end if;
  insert into public.activity (user_id, day, lessons, reviews) values (auth.uid(), p_day, greatest(p_lessons,0), greatest(p_reviews,0))
  on conflict (user_id, day) do update set lessons = activity.lessons + excluded.lessons, reviews = activity.reviews + excluded.reviews;
end $$;

-- ===== Рівень з тесту =====
alter table public.profiles add column if not exists level text;
create or replace function public.set_my_level(p_level text) returns void
language sql security definer set search_path = public as $$
  update public.profiles set level = left(p_level, 8) where id = auth.uid();
$$;

-- ===== Ціна пакета (можна змінити в «Тексти сайту») =====
insert into public.site_settings (key, value) values ('bundle_price', '149 zł') on conflict (key) do nothing;
