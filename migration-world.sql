-- MoviLang · Ігровий світ курсу (фракції, очки, рейтинг фракцій).
-- Очки рахуються на сервері з таблиць progress / progress_lang — з клієнта їх записати не можна.
-- Можна запускати повторно. Supabase → SQL Editor → New query → вставити → Run.

create table if not exists public.world_profiles (
  user_id uuid not null references public.profiles(id) on delete cascade,
  course_id uuid not null references public.courses(id) on delete cascade,
  faction text not null check (faction ~ '^[a-z0-9_]{2,24}$'),
  created_at timestamptz not null default now(),
  primary key (user_id, course_id)
);
alter table public.world_profiles enable row level security;
drop policy if exists p_wp_sel on public.world_profiles;
create policy p_wp_sel on public.world_profiles for select using (user_id = auth.uid() or public.is_admin());
-- запис лише через join_faction (security definer), прямих insert/update немає

-- очки за урок: 10 + бал/10; «бос» (урок із завданням quest) ×3
create or replace function public.world_lesson_points(p_score int, p_tasks jsonb) returns int
language sql immutable as $$
  select ((10 + coalesce(p_score, 0) / 10) *
    case when exists (select 1 from jsonb_array_elements(coalesce(p_tasks, '[]'::jsonb)) x where x->>'type' = 'quest') then 3 else 1 end)::int;
$$;

create or replace function public.world_user_points(p_uid uuid, p_course uuid) returns int
language sql stable security definer set search_path = public as $$
  select coalesce(sum(world_lesson_points(s.score, l.tasks)), 0)::int from (
    select lesson_id, score from progress where user_id = p_uid
    union all
    select lesson_id, score from progress_lang where user_id = p_uid
  ) s join lessons l on l.id = s.lesson_id where l.course_id = p_course;
$$;
revoke execute on function public.world_user_points(uuid, uuid) from public, anon, authenticated;

-- вибір фракції: один раз на курс (повторний виклик лише повертає вже обрану)
create or replace function public.join_faction(p_course uuid, p_faction text) returns text
language plpgsql security definer set search_path = public as $$
declare f text;
begin
  if auth.uid() is null then raise exception 'not logged in'; end if;
  if p_faction !~ '^[a-z0-9_]{2,24}$' then raise exception 'bad faction'; end if;
  insert into world_profiles(user_id, course_id, faction) values (auth.uid(), p_course, p_faction) on conflict do nothing;
  select faction into f from world_profiles where user_id = auth.uid() and course_id = p_course;
  return f;
end $$;

-- мій стан у світі курсу
create or replace function public.world_me(p_course uuid) returns table (faction text, points int, rank int)
language sql stable security definer set search_path = public as $$
  with mine as (select faction from world_profiles where user_id = auth.uid() and course_id = p_course),
  pts as (select w.user_id, world_user_points(w.user_id, p_course) p from world_profiles w where w.course_id = p_course)
  select (select faction from mine), world_user_points(auth.uid(), p_course),
    (select count(*)::int + 1 from pts where p > world_user_points(auth.uid(), p_course));
$$;

-- рейтинг фракцій курсу (лише агрегати, без особистих даних)
create or replace function public.world_standings(p_course uuid) returns table (faction text, members int, points int)
language sql stable security definer set search_path = public as $$
  select w.faction, count(*)::int, coalesce(sum(world_user_points(w.user_id, p_course)), 0)::int
  from world_profiles w where w.course_id = p_course group by w.faction;
$$;

-- топ-10 учнів курсу (лише нік)
create or replace function public.world_top(p_course uuid) returns table (nick text, faction text, points int, me boolean)
language sql stable security definer set search_path = public as $$
  select coalesce(nullif(to_jsonb(p)->>'nick', ''), 'Учень ' || upper(substr(md5(p.id::text), 1, 4))), w.faction,
    world_user_points(w.user_id, p_course), w.user_id = auth.uid()
  from world_profiles w join profiles p on p.id = w.user_id
  where w.course_id = p_course order by 3 desc limit 10;
$$;

grant execute on function public.join_faction(uuid, text), public.world_me(uuid), public.world_standings(uuid), public.world_top(uuid) to authenticated;
grant execute on function public.world_standings(uuid) to anon;
