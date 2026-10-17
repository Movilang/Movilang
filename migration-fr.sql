-- MoviLang: курс «Друзі. Сезон 1» / „Przyjaciele. Sezon 1” / Friends S1 (A2–B1) — 36 уроків, 6 арок, EN/PL/UA.
-- Можна запускати повторно: курс оновлюється, прогрес учнів зберігається.
-- Supabase → SQL Editor → New query → вставити → Run.

alter table public.courses add column if not exists free_first boolean not null default true;
create extension if not exists http with schema extensions;

do $$
declare
  src text := 'https://raw.githubusercontent.com/Movilang/movilang/main/content/fr/fr1.json';
  j jsonb; cid uuid; l jsonb; lid uuid;
begin
  select content::jsonb into j from extensions.http_get(src);
  if j is null or jsonb_array_length(j) <> 36 then raise exception 'Очікувалось 36 уроків: %', src; end if;

  select id into cid from public.courses where slug = 'friends-s1';
  if cid is null then
    insert into public.courses (slug, title, title_pl, title_en, kind, level, price, poster, published, free_first, description, description_pl, description_en)
    values ('friends-s1',
      'Друзі. Сезон 1',
      'Przyjaciele. Sezon 1',
      'Friends. Season 1',
      'series', 'A2–B1', '49 zł', 'p2', false, true,
      'Увесь перший сезон у 36 уроках: наречена, що втекла, Central Perk, мавпочка Марсель, малюк Бен, брошка-камея й аеропорт. 6 арок, сарказм Чендлера, ідіоми «як зрозумів Джоуі», пейджер Росса, квести-«боси» і фінальний іспит із сертифікатом. Рівень A2–B1.',
      'Cały pierwszy sezon w 36 lekcjach: uciekająca panna młoda, Central Perk, małpka Marcel, mały Ben, broszka z kameą i lotnisko. 6 łuków, sarkazm Chandlera, idiomy „jak zrozumiał Joey”, pager Rossa, questy-„bossowie” i egzamin końcowy z certyfikatem. Poziom A2–B1.',
      'The whole first season in 36 lessons: a runaway bride, Central Perk, Marcel the monkey, baby Ben, a cameo brooch and the airport. 6 arcs, Chandler''s sarcasm, idioms “as Joey understood them”, Ross''s pager, boss quests and a final exam with a certificate. Level A2–B1.')
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
select count(*) from public.lessons l join public.courses c on c.id = l.course_id where c.slug = 'friends-s1';

-- публікація:
update public.courses set published = true where slug = 'friends-s1';
