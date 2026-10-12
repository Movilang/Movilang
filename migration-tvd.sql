-- MovieLang: курс «Щоденники вампіра: Сезон 1» (28 уроків).
-- Можна запускати повторно: курс оновлюється, прогрес учнів зберігається.
-- Supabase → SQL Editor → New query → вставити → Run.

-- 1) Курс може не мати безкоштовного першого уроку
alter table public.courses add column if not exists free_first boolean not null default true;

-- 2) Тимчасово вмикаємо http, щоб завантажити JSON курсу з GitHub
create extension if not exists http with schema extensions;

do $$
declare
  src text := 'https://raw.githubusercontent.com/movielang/movielang/main/content/tvd/tvd1.json';
  j jsonb; cid uuid; l jsonb; lid uuid;
begin
  select content::jsonb into j from extensions.http_get(src);
  if j is null or jsonb_array_length(j) = 0 then raise exception 'Не вдалося завантажити %', src; end if;

  select id into cid from public.courses where slug = 'vampire-diaries-1';
  if cid is null then
    insert into public.courses (slug, title, title_pl, title_en, kind, level, price, poster, published, free_first, description, description_pl, description_en)
    values ('vampire-diaries-1',
      'Щоденники вампіра: Сезон 1 — Ласкаво просимо до Містик Фоллс',
      'Pamiętniki wampirów: Sezon 1 — Witaj w Mystic Falls',
      'The Vampire Diaries: Season 1 — Welcome to Mystic Falls',
      'series', 'B1–B2', '69 zł', 'p5', false, false,
      '22 епізоди першого сезону, 5 арок, квести-«боси» і фінальний іспит. Лексика прямо з серіалу, сарказм Деймона, тести на вербену і щоденник Олени. Пояснення українською, рівень B1 → B2.',
      '22 odcinki pierwszego sezonu, 5 łuków fabularnych, questy-„bossowie” i egzamin końcowy. Słownictwo prosto z serialu. Wyjaśnienia po ukraińsku, poziom B1 → B2.',
      'All 22 episodes of season one in 5 story arcs, branching boss quests and a final exam. Vocabulary straight from the show. Explanations in Ukrainian, level B1 → B2.')
    returning id into cid;
  end if;

  for l in select * from jsonb_array_elements(j) loop
    select id into lid from public.lessons where course_id = cid and num = (l->>'num')::int;
    if lid is null then
      insert into public.lessons (course_id, num, title, grammar, scene, tasks, variants)
      values (cid, (l->>'num')::int, l->>'title', l->>'grammar', l->>'scene', l->'tasks', l->'variants');
    else
      update public.lessons set title = l->>'title', grammar = l->>'grammar', scene = l->>'scene', tasks = l->'tasks', variants = l->'variants'
      where id = lid;
    end if;
  end loop;
end $$;

-- 3) Прибираємо тимчасове розширення
drop extension if exists http;

-- 4) Коли перевірите курс в адмін-режимі — опублікуйте:
-- update public.courses set published = true where slug = 'vampire-diaries-1';
