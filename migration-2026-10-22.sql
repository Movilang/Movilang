-- MoviLang · 2026-10-22: друзі й дуети, рейтинг тижня, питання викладачу, подарунки, реферали,
-- відгуки, сесії уроків (де кидають), підтримка й повернення, журнал листів.
-- Можна запускати повторно. Supabase → SQL Editor → New query → вставити → Run.

-- ---------- профіль: нік, код друга, реферал, бонуси ----------
alter table public.profiles add column if not exists nick text;
alter table public.profiles add column if not exists friend_code text;
alter table public.profiles add column if not exists referred_by uuid references public.profiles(id) on delete set null;
alter table public.profiles add column if not exists ref_credits int not null default 0;
alter table public.profiles add column if not exists marketing boolean not null default true;
create unique index if not exists profiles_friend_code_uq on public.profiles(friend_code);
create unique index if not exists profiles_nick_uq on public.profiles(lower(nick));

update public.profiles set friend_code = upper(substr(md5(id::text || 'ml'), 1, 6)) where friend_code is null;

create or replace function public.ml_fill_code() returns trigger language plpgsql as $$
begin
  if new.friend_code is null then new.friend_code := upper(substr(md5(new.id::text || 'ml'), 1, 6)); end if;
  return new;
end $$;
drop trigger if exists trg_ml_fill_code on public.profiles;
create trigger trg_ml_fill_code before insert on public.profiles for each row execute function public.ml_fill_code();

create or replace function public.set_my_nick(p_nick text) returns text
language plpgsql security definer set search_path = public as $$
declare n text := btrim(p_nick);
begin
  if auth.uid() is null then raise exception 'not logged in'; end if;
  if n !~ '^[\w .\-]{3,20}$' then raise exception 'Нік: 3–20 символів (літери, цифри, пробіл, . - _)'; end if;
  if exists (select 1 from profiles where lower(nick) = lower(n) and id <> auth.uid()) then raise exception 'Цей нік уже зайнятий'; end if;
  update profiles set nick = n where id = auth.uid();
  return n;
end $$;

create or replace function public.set_marketing(p_on boolean) returns void
language sql security definer set search_path = public as $$ update profiles set marketing = p_on where id = auth.uid(); $$;

-- реферал: учень, що прийшов за посиланням, записує код того, хто запросив (лише один раз і лише в перші 7 днів)
create or replace function public.claim_referral(p_code text) returns boolean
language plpgsql security definer set search_path = public as $$
declare ref uuid; me profiles;
begin
  select * into me from profiles where id = auth.uid();
  if me.id is null or me.referred_by is not null or me.created_at < now() - interval '7 days' then return false; end if;
  select id into ref from profiles where friend_code = upper(btrim(p_code));
  if ref is null or ref = me.id then return false; end if;
  update profiles set referred_by = ref where id = me.id;
  return true;
end $$;

-- ---------- друзі (дует) ----------
create table if not exists public.friendships (
  user_id uuid not null references public.profiles(id) on delete cascade,
  friend_id uuid not null references public.profiles(id) on delete cascade,
  created_at timestamptz not null default now(),
  primary key (user_id, friend_id)
);
alter table public.friendships enable row level security;
drop policy if exists p_fr_sel on public.friendships;
create policy p_fr_sel on public.friendships for select using (user_id = auth.uid() or friend_id = auth.uid() or public.is_admin());
drop policy if exists p_fr_del on public.friendships;
create policy p_fr_del on public.friendships for delete using (user_id = auth.uid() or friend_id = auth.uid());

create or replace function public.add_friend(p_code text) returns text
language plpgsql security definer set search_path = public as $$
declare f profiles;
begin
  if auth.uid() is null then raise exception 'not logged in'; end if;
  select * into f from profiles where friend_code = upper(btrim(p_code));
  if f.id is null then raise exception 'Код не знайдено'; end if;
  if f.id = auth.uid() then raise exception 'Це твій власний код'; end if;
  insert into friendships(user_id, friend_id) values (auth.uid(), f.id) on conflict do nothing;
  insert into friendships(user_id, friend_id) values (f.id, auth.uid()) on conflict do nothing;
  return coalesce(f.nick, split_part(f.email, '@', 1));
end $$;

-- окуляри: 10 за урок + бал/10 (тиждень = останні 7 днів)
create or replace function public.ml_points(p_uid uuid, p_since timestamptz) returns int
language sql stable security definer set search_path = public as $$
  select coalesce(sum(10 + coalesce(score, 0) / 10), 0)::int from (
    select score, completed_at from progress where user_id = p_uid and completed_at >= p_since
    union all select score, completed_at from progress_lang where user_id = p_uid and completed_at >= p_since) x;
$$;

create or replace function public.my_friends() returns table (friend_id uuid, nick text, lessons int, week_points int, last_active date, course text)
language sql stable security definer set search_path = public as $$
  select p.id, coalesce(p.nick, split_part(p.email, '@', 1)),
    ((select count(*) from progress where user_id = p.id) + (select count(*) from progress_lang where user_id = p.id))::int,
    public.ml_points(p.id, now() - interval '7 days'),
    (select max(day) from activity where user_id = p.id),
    (select coalesce(c.title_pl, c.title) from progress pr join lessons l on l.id = pr.lesson_id join courses c on c.id = l.course_id
       where pr.user_id = p.id order by pr.completed_at desc limit 1)
  from friendships f join profiles p on p.id = f.friend_id
  where f.user_id = auth.uid();
$$;

create or replace function public.leaderboard_week() returns table (nick text, points int, lessons int, me boolean)
language sql stable security definer set search_path = public as $$
  with x as (
    select user_id, score from progress where completed_at >= now() - interval '7 days'
    union all select user_id, score from progress_lang where completed_at >= now() - interval '7 days')
  select coalesce(p.nick, 'Uczeń #' || substr(p.friend_code, 1, 4)), sum(10 + coalesce(x.score, 0) / 10)::int, count(*)::int, p.id = auth.uid()
  from x join profiles p on p.id = x.user_id where p.role <> 'admin'
  group by p.id, p.nick, p.friend_code order by 2 desc limit 50;
$$;

-- ---------- питання викладачу ----------
create table if not exists public.questions (
  id bigint generated always as identity primary key,
  user_id uuid references public.profiles(id) on delete cascade,
  email text,
  lesson_id uuid references public.lessons(id) on delete set null,
  target text,
  task_n int,
  task_q text,
  text text not null,
  answer text,
  status text not null default 'new',
  seen boolean not null default true,
  created_at timestamptz not null default now(),
  answered_at timestamptz
);
alter table public.questions enable row level security;
drop policy if exists p_q_sel on public.questions;
create policy p_q_sel on public.questions for select using (user_id = auth.uid() or public.is_admin());
drop policy if exists p_q_ins on public.questions;
create policy p_q_ins on public.questions for insert with check (user_id = auth.uid());
drop policy if exists p_q_upd on public.questions;
create policy p_q_upd on public.questions for update using (public.is_admin() or user_id = auth.uid());

-- ---------- відгуки ----------
create table if not exists public.reviews (
  id bigint generated always as identity primary key,
  user_id uuid references public.profiles(id) on delete cascade,
  course_id uuid references public.courses(id) on delete cascade,
  stage int not null default 6,
  rating int not null check (rating between 1 and 5),
  text text,
  approved boolean not null default false,
  created_at timestamptz not null default now(),
  unique (user_id, course_id, stage)
);
alter table public.reviews enable row level security;
drop policy if exists p_rv_sel on public.reviews;
create policy p_rv_sel on public.reviews for select using (approved or user_id = auth.uid() or public.is_admin());
drop policy if exists p_rv_ins on public.reviews;
create policy p_rv_ins on public.reviews for insert with check (user_id = auth.uid());
drop policy if exists p_rv_upd on public.reviews;
create policy p_rv_upd on public.reviews for update using (public.is_admin());
drop policy if exists p_rv_del on public.reviews;
create policy p_rv_del on public.reviews for delete using (public.is_admin());

create or replace function public.course_reviews(p_course uuid) returns table (nick text, rating int, text text, created_at timestamptz)
language sql stable security definer set search_path = public as $$
  select coalesce(p.nick, split_part(p.name, ' ', 1), 'Uczeń'), r.rating, r.text, r.created_at
  from reviews r left join profiles p on p.id = r.user_id
  where r.course_id = p_course and r.approved order by r.created_at desc limit 30;
$$;

-- ---------- сесії уроків (де саме кидають) ----------
create table if not exists public.lesson_sessions (
  id bigint generated always as identity primary key,
  user_id uuid references public.profiles(id) on delete cascade,
  lesson_id uuid references public.lessons(id) on delete cascade,
  target text,
  last_task int not null default 0,
  total int not null default 0,
  finished boolean not null default false,
  started_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create index if not exists lesson_sessions_lesson_idx on public.lesson_sessions(lesson_id);
alter table public.lesson_sessions enable row level security;
drop policy if exists p_ls_sel on public.lesson_sessions;
create policy p_ls_sel on public.lesson_sessions for select using (user_id = auth.uid() or public.is_admin());
drop policy if exists p_ls_ins on public.lesson_sessions;
create policy p_ls_ins on public.lesson_sessions for insert with check (user_id = auth.uid());
drop policy if exists p_ls_upd on public.lesson_sessions;
create policy p_ls_upd on public.lesson_sessions for update using (user_id = auth.uid());

-- ---------- підтримка й повернення ----------
create table if not exists public.tickets (
  id bigint generated always as identity primary key,
  user_id uuid references public.profiles(id) on delete set null,
  email text,
  order_id uuid references public.orders(id) on delete set null,
  kind text not null default 'question',
  text text not null,
  status text not null default 'new',
  admin_note text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
alter table public.tickets enable row level security;
drop policy if exists p_t_sel on public.tickets;
create policy p_t_sel on public.tickets for select using (user_id = auth.uid() or public.is_admin());
drop policy if exists p_t_ins on public.tickets;
create policy p_t_ins on public.tickets for insert with check (user_id = auth.uid());
drop policy if exists p_t_upd on public.tickets;
create policy p_t_upd on public.tickets for update using (public.is_admin());

-- ---------- замовлення: подарунки, знижки, повернення ----------
alter table public.orders add column if not exists gift boolean not null default false;
alter table public.orders add column if not exists gift_to text;
alter table public.orders add column if not exists gift_msg text;
alter table public.orders add column if not exists discount int not null default 0;
alter table public.orders add column if not exists payment_intent text;
alter table public.orders add column if not exists refunded_at timestamptz;
alter table public.orders add column if not exists ref_used boolean not null default false;
drop policy if exists p_orders_upd on public.orders;
create policy p_orders_upd on public.orders for update using (public.is_admin());

-- ---------- журнал листів (щоб не надсилати двічі) ----------
create table if not exists public.email_log (
  id bigint generated always as identity primary key,
  user_id uuid references public.profiles(id) on delete cascade,
  kind text not null,
  ref text not null default '',
  sent_at timestamptz not null default now(),
  unique (user_id, kind, ref)
);
alter table public.email_log enable row level security;
drop policy if exists p_el_sel on public.email_log;
create policy p_el_sel on public.email_log for select using (public.is_admin());

-- перевірка
select 'ok' as status, (select count(*) from public.profiles where friend_code is not null) as profiles_with_code;
