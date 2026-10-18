-- MoviLang: курс «Як я познайомився з вашою мамою. Сезон 1» / „Jak poznałem waszą matkę” / How I Met Your Mother S1 (B1–B2) — 36 уроків, 6 арок, EN/PL/UA.
-- Можна запускати повторно: курс оновлюється, прогрес учнів зберігається.
-- Supabase → SQL Editor → New query → вставити → Run.

alter table public.courses add column if not exists free_first boolean not null default true;
create extension if not exists http with schema extensions;

do $$
declare
  src text := 'https://raw.githubusercontent.com/Movilang/movilang/main/content/hm/hm1.json';
  j jsonb; cid uuid; l jsonb; lid uuid;
begin
  select content::jsonb into j from extensions.http_get(src);
  if j is null or jsonb_array_length(j) <> 36 then raise exception 'Очікувалось 36 уроків: %', src; end if;

  select id into cid from public.courses where slug = 'himym-s1';
  if cid is null then
    insert into public.courses (slug, title, title_pl, title_en, kind, level, price, poster, published, free_first, description, description_pl, description_en)
    values ('himym-s1',
      'Як я познайомився з вашою мамою. Сезон 1',
      'Jak poznałem waszą matkę. Sezon 1',
      'How I Met Your Mother. Season 1',
      'series', 'B1–B2', '49 zł', 'p8', false, true,
      'Увесь перший сезон у 36 уроках: синій валторн, ананас, Вікторія, танець дощу, правила Барні і Сан-Франциско. Граматика B1–B2: усі умовні речення, непряма мова, пасив, модальні в минулому, інверсія, cleft-речення та сотні живих фраз і ідіом. 6 арок, квести-«боси» і фінальний іспит із сертифікатом.',
      'Cały pierwszy sezon w 36 lekcjach: niebieski róg, ananas, Victoria, taniec deszczu, zasady Barneya i San Francisco. Gramatyka B1–B2: wszystkie tryby warunkowe, mowa zależna, strona bierna, czasowniki modalne w przeszłości, inwersja, zdania z wyróżnieniem i setki żywych zwrotów i idiomów. 6 łuków, questy-„bossowie” i egzamin końcowy z certyfikatem.',
      'All of season one in 36 lessons: the blue French horn, the pineapple, Victoria, the rain dance, Barney''s rules and San Francisco. B1–B2 grammar: every conditional, reported speech, the passive, past modals, inversion, cleft sentences and hundreds of real phrases and idioms. 6 arcs, boss quests and a final exam with a certificate.')
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
select count(*) from public.lessons l join public.courses c on c.id = l.course_id where c.slug = 'himym-s1';

-- публікація:
update public.courses set published = true where slug = 'himym-s1';
