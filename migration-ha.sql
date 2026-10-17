-- MoviLang: курс «Сам удома» / „Kevin sam w domu” / Home Alone (A2) — 36 уроків, 6 арок, EN/PL/UA.
-- Можна запускати повторно: курс оновлюється, прогрес учнів зберігається.
-- Supabase → SQL Editor → New query → вставити → Run.

alter table public.courses add column if not exists free_first boolean not null default true;
create extension if not exists http with schema extensions;

do $$
declare
  src text := 'https://raw.githubusercontent.com/Movilang/movilang/main/content/ha/ha1.json';
  j jsonb; cid uuid; l jsonb; lid uuid;
begin
  select content::jsonb into j from extensions.http_get(src);
  if j is null or jsonb_array_length(j) <> 36 then raise exception 'Очікувалось 36 уроків: %', src; end if;

  select id into cid from public.courses where slug = 'home-alone';
  if cid is null then
    insert into public.courses (slug, title, title_pl, title_en, kind, level, price, poster, published, free_first, description, description_pl, description_en)
    values ('home-alone',
      'Сам удома',
      'Kevin sam w domu',
      'Home Alone',
      'film', 'A2', '49 zł', 'p6', false, true,
      'Увесь фільм у 36 уроках: велика родина, порожній дім, мокрі бандити, мамина дорога додому і Святвечір. 6 арок, квести-«боси», карта пасток, рація Кевіна і фінальний іспит із сертифікатом. Рівень A2.',
      'Cały film w 36 lekcjach: wielka rodzina, pusty dom, mokrzy bandyci, droga mamy do domu i Wigilia. 6 łuków, questy-„bossowie”, mapa pułapek, krótkofalówka Kevina i egzamin końcowy z certyfikatem. Poziom A2.',
      'The whole film in 36 lessons: a big family, an empty house, the Wet Bandits, Mom''s trip home and Christmas Eve. 6 arcs, boss quests, a trap map, Kevin''s walkie-talkie and a final exam with a certificate. Level A2.')
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
select count(*) from public.lessons l join public.courses c on c.id = l.course_id where c.slug = 'home-alone';

-- Коли перевірите курс в адмін-режимі — опублікуйте:
-- update public.courses set published = true where slug = 'home-alone';
