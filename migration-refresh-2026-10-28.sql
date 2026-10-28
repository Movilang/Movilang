-- MoviLang: оновлення завдань у всіх 7 курсах (польська й українська версії: репліки з фільму, нові завдання «Сцена з фільму», без повторів).
-- Прогрес учнів зберігається. Supabase → SQL Editor → New query → вставити все → Run.
-- Курс «Тачки» має бути вже завантажений (migration-ca.sql); якщо ні — спершу запусти його.

create extension if not exists http with schema extensions;

do $$
declare
  r record; j jsonb; cid uuid; l jsonb; n int := 0;
begin
  for r in select * from (values
    ('cars', 'content/ca/ca1.json'), ('zootopia', 'content/zt/zt1.json'), ('friends-s1', 'content/fr/fr1.json'),
    ('home-alone', 'content/ha/ha1.json'), ('himym-s1', 'content/hm/hm1.json'),
    ('vampire-diaries-1', 'content/tvd/tvd1.json'), ('harry-potter-1', 'content/hp/hp.json')) as t(slug, path)
  loop
    select id into cid from public.courses where slug = r.slug;
    if cid is null then raise notice 'Курсу % немає — пропускаю', r.slug; continue; end if;
    select content::jsonb into j from extensions.http_get('https://raw.githubusercontent.com/Movilang/movilang/main/' || r.path);
    if j is null or jsonb_array_length(j) <> 36 then raise exception 'Очікувалось 36 уроків: %', r.path; end if;
    for l in select * from jsonb_array_elements(j) loop
      update public.lessons set title = l->>'title', title_pl = l->>'title_pl', title_en = l->>'title_en', grammar = l->>'grammar',
        scene = l->>'scene', scene_pl = l->>'scene_pl', scene_en = l->>'scene_en', tasks = l->'tasks', variants = l->'variants'
      where course_id = cid and num = (l->>'num')::int;
    end loop;
    n := n + 1;
  end loop;
  raise notice 'Оновлено курсів: %', n;
end $$;

drop extension if exists http;

select c.slug, count(l.*) as lessons from public.courses c left join public.lessons l on l.course_id = c.id group by c.slug order by c.slug;
