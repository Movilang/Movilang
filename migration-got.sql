-- MoviLang: курс «Гра престолів. Сезон 1» / „Gra o tron. Sezon 1” / Game of Thrones. Season 1 (B2, 18+) — 36 уроків, 6 арок, EN/PL/UA.
-- Можна запускати повторно: курс оновлюється, прогрес учнів зберігається.
-- Supabase → SQL Editor → New query → вставити все → Run.
-- Уроки мають сталі id (з content/got/got1.json), тому завдання з content/std/game-of-thrones-1 підтягнуться автоматично.

alter table public.courses add column if not exists free_first boolean not null default true;
create extension if not exists http with schema extensions;

do $$
declare
  src text := 'https://raw.githubusercontent.com/Movilang/movilang/main/content/got/got1.json';
  j jsonb; cid uuid; l jsonb;
begin
  select content::jsonb into j from extensions.http_get(src);
  if j is null or jsonb_array_length(j) <> 36 then raise exception 'Очікувалось 36 уроків: %', src; end if;

  select id into cid from public.courses where slug = 'game-of-thrones-1';
  if cid is null then
    insert into public.courses (slug, title, title_pl, title_en, kind, level, price, poster, published, free_first, description, description_pl, description_en)
    values ('game-of-thrones-1',
      'Гра престолів. Сезон 1',
      'Gra o tron. Sezon 1',
      'Game of Thrones. Season 1',
      'series', 'B2', '69 zł', 'p5', false, true,
      'Увесь перший сезон у 36 уроках. Ти — юний писар із Вінтерфелла: їдеш на південь із лордом Недом, ведеш протоколи малої ради, розплутуєш таємницю книги родоводів, тікаєш зі столиці й стаєш писарем короля Робба. Граматика рівня B2: усі часи, умовні речення, пасив, непряма мова, інверсія, дієприслівникові звороти. 6 арок, квести-«боси» і фінальний іспит із сертифікатом. 18+: без сцен насильства, лише сюжет.',
      'Cały pierwszy sezon w 36 lekcjach. Jesteś młodym pisarzem z Winterfell: jedziesz na południe z lordem Nedem, piszesz protokoły małej rady, rozwikłujesz tajemnicę księgi rodów, uciekasz ze stolicy i zostajesz pisarzem króla Robba. Gramatyka na poziomie B2: wszystkie czasy, okresy warunkowe, strona bierna, mowa zależna, inwersja, imiesłowy. 6 łuków, questy-„bossowie” i egzamin końcowy z certyfikatem. 18+: bez scen przemocy, tylko fabuła.',
      'The whole first season in 36 lessons. You are a young scribe from Winterfell: you ride south with Lord Ned, take the minutes of the small council, unravel the secret of the book of lineages, escape from the capital and become King Robb''s scribe. B2 grammar: all tenses, conditionals, the passive, reported speech, inversion, participle clauses. 6 arcs, boss quests and a final exam with a certificate. 18+: no violent scenes, just the story.')
    returning id into cid;
  end if;

  for l in select * from jsonb_array_elements(j) loop
    insert into public.lessons (id, course_id, num, title, title_pl, title_en, grammar, scene, scene_pl, scene_en, tasks, variants)
    values ((l->>'id')::uuid, cid, (l->>'num')::int, l->>'title', l->>'title_pl', l->>'title_en', l->>'grammar', l->>'scene', l->>'scene_pl', l->>'scene_en', l->'tasks', l->'variants')
    on conflict (id) do update set title = excluded.title, title_pl = excluded.title_pl, title_en = excluded.title_en, grammar = excluded.grammar,
      scene = excluded.scene, scene_pl = excluded.scene_pl, scene_en = excluded.scene_en, tasks = excluded.tasks, variants = excluded.variants;
  end loop;
end $$;

drop extension if exists http;

-- перевірка: має бути 36
select count(*) from public.lessons l join public.courses c on c.id = l.course_id where c.slug = 'game-of-thrones-1';

-- публікація:
update public.courses set published = true where slug = 'game-of-thrones-1';
