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
-- MoviLang: курс «Зоотрополіс» / „Zwierzogród” / Zootopia (A1–A2, також для дітей) — 36 уроків, 6 арок, EN/PL/UA.
-- Можна запускати повторно: курс оновлюється, прогрес учнів зберігається.
-- Supabase → SQL Editor → New query → вставити → Run.

alter table public.courses add column if not exists free_first boolean not null default true;
create extension if not exists http with schema extensions;

do $$
declare
  src text := 'https://raw.githubusercontent.com/Movilang/movilang/main/content/zt/zt1.json';
  j jsonb; cid uuid; l jsonb; lid uuid;
begin
  select content::jsonb into j from extensions.http_get(src);
  if j is null or jsonb_array_length(j) <> 36 then raise exception 'Очікувалось 36 уроків: %', src; end if;

  select id into cid from public.courses where slug = 'zootopia';
  if cid is null then
    insert into public.courses (slug, title, title_pl, title_en, kind, level, price, poster, published, free_first, description, description_pl, description_en)
    values ('zootopia',
      'Зоотрополіс',
      'Zwierzogród',
      'Zootopia',
      'film', 'A1–A2', '49 zł', 'p3', false, true,
      'Увесь фільм у 36 уроках: мрія маленької кролиці, поліцейська академія, хитрий лис Нік, зникла видра, сині квіти і місто, де всі різні. Прості пояснення, багато ігор і нагород — підходить і дітям. 6 арок, квести-«боси» і фінальний іспит із сертифікатом. Рівень A1–A2.',
      'Cały film w 36 lekcjach: marzenie małej króliczki, akademia policyjna, sprytny lis Nick, zaginiona wydra, niebieskie kwiaty i miasto, gdzie wszyscy są różni. Proste wyjaśnienia, dużo gier i nagród — także dla dzieci. 6 łuków, questy-„bossowie” i egzamin końcowy z certyfikatem. Poziom A1–A2.',
      'The whole film in 36 lessons: a little bunny''s dream, the police academy, Nick the sly fox, a missing otter, blue flowers and a city where everyone is different. Simple explanations, lots of games and rewards — great for kids too. 6 arcs, boss quests and a final exam with a certificate. Level A1–A2.')
    returning id into cid;
  end if;

  for l in select * from jsonb_array_elements(j) loop
    select id into lid from public.lessons where course_id = cid and num = (l->>'num')::int;
    if lid is null then
      insert into public.lessons (course_id, num, title, title_pl, title_en, grammar, scene, scene_pl, scene_en, tasks, variants)
      values (cid, (l->>'num')::int, l->>'title', l->>'title_pl', l->>'title_en', l->>'grammar', l->>'scene', l->>'scene_pl', l->>'scene_en', l->'tasks', l->'variants');
    else
      update public.lessons set title = l->>'title', title_pl = l->>'title_pl', title_en = l->>'title_en', grammar = l->>'grammar',
        scene = l->>'scene', scene_pl = l->>'scene_pl', scene_en = l->>'scene_en', tasks = l->'tasks', variants = l->'variants'
      where id = lid;
    end if;
  end loop;
end $$;

drop extension if exists http;

-- перевірка: має бути 36

-- публікація:
update public.courses set published = true where slug = 'zootopia';
-- MoviLang: курс безкоштовний міні-курс «Крижане серце» / „Kraina Lodu” / Frozen (A1) — 6 уроків, EN/PL/UA.
-- Можна запускати повторно: курс оновлюється, прогрес учнів зберігається.
-- Supabase → SQL Editor → New query → вставити → Run.

alter table public.courses add column if not exists free_first boolean not null default true;
create extension if not exists http with schema extensions;

do $$
declare
  src text := 'https://raw.githubusercontent.com/Movilang/movilang/main/content/fz/fz1.json';
  j jsonb; cid uuid; l jsonb; lid uuid;
begin
  select content::jsonb into j from extensions.http_get(src);
  if j is null or jsonb_array_length(j) <> 6 then raise exception 'Очікувалось 6 уроків: %', src; end if;

  select id into cid from public.courses where slug = 'frozen-mini';
  if cid is null then
    insert into public.courses (slug, title, title_pl, title_en, kind, level, price, poster, published, free_first, description, description_pl, description_en)
    values ('frozen-mini',
      'Крижане серце · міні-курс',
      'Kraina Lodu · mini-kurs',
      'Frozen · mini-course',
      'film', 'A1', '0 zł', 'p4', false, true,
      'Безкоштовний міні-курс на 6 уроків: дві сестри, коронація, крижаний палац, Олаф і справжня любов. Ідеальний старт для дітей і початківців. Наприкінці — сертифікат. Рівень A1.',
      'Darmowy mini-kurs w 6 lekcjach: dwie siostry, koronacja, lodowy pałac, Olaf i prawdziwa miłość. Idealny start dla dzieci i początkujących. Na końcu certyfikat. Poziom A1.',
      'A free 6-lesson mini-course: two sisters, a coronation, an ice palace, Olaf and true love. A perfect start for kids and beginners. Certificate at the end. Level A1.')
    returning id into cid;
  end if;

  for l in select * from jsonb_array_elements(j) loop
    select id into lid from public.lessons where course_id = cid and num = (l->>'num')::int;
    if lid is null then
      insert into public.lessons (course_id, num, title, title_pl, title_en, grammar, scene, scene_pl, scene_en, tasks, variants)
      values (cid, (l->>'num')::int, l->>'title', l->>'title_pl', l->>'title_en', l->>'grammar', l->>'scene', l->>'scene_pl', l->>'scene_en', l->'tasks', l->'variants');
    else
      update public.lessons set title = l->>'title', title_pl = l->>'title_pl', title_en = l->>'title_en', grammar = l->>'grammar',
        scene = l->>'scene', scene_pl = l->>'scene_pl', scene_en = l->>'scene_en', tasks = l->'tasks', variants = l->'variants'
      where id = lid;
    end if;
  end loop;
end $$;

drop extension if exists http;

-- перевірка: має бути 6

-- публікація:
update public.courses set published = true where slug = 'frozen-mini';
