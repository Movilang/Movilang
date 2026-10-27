-- MoviLang: курс «Тачки» / „Auta” / Cars (A1, також для дітей) — 36 уроків, 6 арок, EN/PL/UA.
-- Можна запускати повторно: курс оновлюється, прогрес учнів зберігається.
-- Supabase → SQL Editor → New query → вставити → Run.

alter table public.courses add column if not exists free_first boolean not null default true;
create extension if not exists http with schema extensions;

do $$
declare
  src text := 'https://raw.githubusercontent.com/Movilang/movilang/main/content/ca/ca1.json';
  j jsonb; cid uuid; l jsonb; lid uuid;
begin
  select content::jsonb into j from extensions.http_get(src);
  if j is null or jsonb_array_length(j) <> 36 then raise exception 'Очікувалось 36 уроків: %', src; end if;

  select id into cid from public.courses where slug = 'cars';
  if cid is null then
    insert into public.courses (slug, title, title_pl, title_en, kind, level, price, poster, published, free_first, description, description_pl, description_en)
    values ('cars',
      'Тачки',
      'Auta',
      'Cars',
      'film', 'A1', '49 zł', 'p2', false, true,
      'Увесь фільм у 36 уроках: зарозумілий гонщик-новачок губиться на трасі 66, ремонтує дорогу в маленькому містечку, знаходить справжніх друзів і дізнається таємницю Дока. Прості пояснення, багато ігор і нагород — підходить і дітям. 6 арок, квести-«боси» і фінальний іспит із сертифікатом. Рівень A1.',
      'Cały film w 36 lekcjach: zarozumiały debiutant gubi się na drodze 66, naprawia drogę w małym miasteczku, znajduje prawdziwych przyjaciół i poznaje tajemnicę Doca. Proste wyjaśnienia, dużo gier i nagród — także dla dzieci. 6 łuków, questy-„bossowie” i egzamin końcowy z certyfikatem. Poziom A1.',
      'The whole film in 36 lessons: a cocky rookie racer gets lost on Route 66, fixes the road in a tiny town, finds real friends and learns Doc''s secret. Simple explanations, lots of games and rewards — great for kids too. 6 arcs, boss quests and a final exam with a certificate. Level A1.')
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
select count(*) from public.lessons l join public.courses c on c.id = l.course_id where c.slug = 'cars';

-- публікація:
update public.courses set published = true where slug = 'cars';
