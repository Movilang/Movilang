-- MovieLang — схема бази даних для Supabase.
-- Запустіть увесь файл один раз: Supabase → SQL Editor → New query → вставити → Run.

-- ========== Таблиці ==========
create table if not exists public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  email text,
  name text,
  role text not null default 'student' check (role in ('student','admin')),
  created_at timestamptz not null default now()
);

create table if not exists public.courses (
  id uuid primary key default gen_random_uuid(),
  slug text,
  title text not null,
  kind text not null default 'film',
  level text default 'A2',
  price text default '299 ₴',
  poster text default 'p1',
  published boolean not null default false,
  description text default '',
  created_at timestamptz not null default now()
);

create table if not exists public.lessons (
  id uuid primary key default gen_random_uuid(),
  course_id uuid not null references public.courses(id) on delete cascade,
  num int not null default 1,
  title text not null,
  grammar text default '',
  scene text default '',
  tasks jsonb not null default '[]'::jsonb
);

create table if not exists public.access_keys (
  code text primary key,
  course_id uuid references public.courses(id) on delete cascade, -- null = усі курси
  created_at timestamptz not null default now(),
  activated_by uuid references public.profiles(id) on delete set null,
  activated_at timestamptz
);

create table if not exists public.enrollments (
  user_id uuid references public.profiles(id) on delete cascade,
  course_id uuid references public.courses(id) on delete cascade,
  created_at timestamptz not null default now(),
  primary key (user_id, course_id)
);

create table if not exists public.progress (
  user_id uuid references public.profiles(id) on delete cascade,
  lesson_id uuid references public.lessons(id) on delete cascade,
  score int not null default 0,
  answer text,
  completed_at timestamptz not null default now(),
  primary key (user_id, lesson_id)
);

create table if not exists public.site_settings (
  key text primary key,
  value text
);

-- ========== Профіль створюється автоматично при реєстрації ==========
create or replace function public.handle_new_user() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  insert into public.profiles (id, email, name)
  values (new.id, new.email, coalesce(new.raw_user_meta_data->>'name', split_part(new.email, '@', 1)));
  return new;
end $$;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created after insert on auth.users
  for each row execute function public.handle_new_user();

-- ========== Хто адмін ==========
create or replace function public.is_admin() returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.profiles where id = auth.uid() and role = 'admin');
$$;

-- ========== Активація ключа (безпечно, на сервері) ==========
create or replace function public.activate_key(p_code text) returns json
language plpgsql security definer set search_path = public as $$
declare k public.access_keys;
begin
  if auth.uid() is null then return json_build_object('ok', false, 'msg', 'Увійдіть в акаунт'); end if;
  select * into k from public.access_keys where code = upper(trim(p_code)) for update;
  if not found then return json_build_object('ok', false, 'msg', 'Такого ключа не знайдено. Перевір літери O та 0, I та 1.'); end if;
  if k.activated_by is not null then return json_build_object('ok', false, 'msg', 'Цей ключ уже активовано.'); end if;
  update public.access_keys set activated_by = auth.uid(), activated_at = now() where code = k.code;
  if k.course_id is null then
    insert into public.enrollments (user_id, course_id) select auth.uid(), id from public.courses on conflict do nothing;
  else
    insert into public.enrollments (user_id, course_id) values (auth.uid(), k.course_id) on conflict do nothing;
  end if;
  return json_build_object('ok', true, 'course_id', k.course_id);
end $$;

-- ========== Права доступу (Row Level Security) ==========
alter table public.profiles enable row level security;
alter table public.courses enable row level security;
alter table public.lessons enable row level security;
alter table public.access_keys enable row level security;
alter table public.enrollments enable row level security;
alter table public.progress enable row level security;
alter table public.site_settings enable row level security;

-- профілі: свій бачить кожен, усі — адмін; роль змінює лише адмін
drop policy if exists p_profiles_sel on public.profiles;
create policy p_profiles_sel on public.profiles for select using (id = auth.uid() or public.is_admin());
drop policy if exists p_profiles_upd on public.profiles;
create policy p_profiles_upd on public.profiles for update using (public.is_admin());

-- курси й уроки: опубліковані бачать усі, змінює адмін
drop policy if exists p_courses_sel on public.courses;
create policy p_courses_sel on public.courses for select using (published or public.is_admin());
drop policy if exists p_courses_all on public.courses;
create policy p_courses_all on public.courses for all using (public.is_admin()) with check (public.is_admin());

drop policy if exists p_lessons_sel on public.lessons;
create policy p_lessons_sel on public.lessons for select using (
  exists (select 1 from public.courses c where c.id = course_id and (c.published or public.is_admin())));
drop policy if exists p_lessons_all on public.lessons;
create policy p_lessons_all on public.lessons for all using (public.is_admin()) with check (public.is_admin());

-- ключі: лише адмін (учні активують через activate_key)
drop policy if exists p_keys_all on public.access_keys;
create policy p_keys_all on public.access_keys for all using (public.is_admin()) with check (public.is_admin());

-- записи на курси: свої або адмін
drop policy if exists p_enr_sel on public.enrollments;
create policy p_enr_sel on public.enrollments for select using (user_id = auth.uid() or public.is_admin());

-- прогрес: учень пише й читає свій, адмін читає всі
drop policy if exists p_prog_sel on public.progress;
create policy p_prog_sel on public.progress for select using (user_id = auth.uid() or public.is_admin());
drop policy if exists p_prog_ins on public.progress;
create policy p_prog_ins on public.progress for insert with check (user_id = auth.uid());
drop policy if exists p_prog_upd on public.progress;
create policy p_prog_upd on public.progress for update using (user_id = auth.uid());

-- тексти сайту: читають усі, змінює адмін
drop policy if exists p_set_sel on public.site_settings;
create policy p_set_sel on public.site_settings for select using (true);
drop policy if exists p_set_all on public.site_settings;
create policy p_set_all on public.site_settings for all using (public.is_admin()) with check (public.is_admin());

-- ========== ПІСЛЯ реєстрації на сайті зробіть себе адміном ==========
-- Замініть пошту на свою і запустіть окремо:
-- update public.profiles set role = 'admin' where email = 'ВАША@ПОШТА.com';

-- ========== Оновлення 2026-10-10: польська мова ==========
alter table public.courses add column if not exists title_pl text;
alter table public.courses add column if not exists description_pl text;
alter table public.lessons add column if not exists title_pl text;
alter table public.lessons add column if not exists scene_pl text;

-- ========== Оновлення 2026-10-12: курс без безкоштовного першого уроку ==========
alter table public.courses add column if not exists free_first boolean not null default true;
