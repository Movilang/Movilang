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
select count(*) from public.lessons l join public.courses c on c.id = l.course_id where c.slug = 'frozen-mini';

-- публікація:
update public.courses set published = true where slug = 'frozen-mini';
