-- MoviLang: «Щоденники вампіра: Сезон 1» — 36 уроків (було 28) + курс «Гаррі Поттер» B1.
-- Supabase → SQL Editor → New query → вставити → Run. Прогрес учнів зберігається:
-- старі уроки лише отримують нові номери, 8 нових уроків додаються.

create extension if not exists http with schema extensions;

do $$
declare
  j jsonb; cid uuid; l jsonb; lid uuid;
begin
  -- 1) «Щоденники вампіра»
  select content::jsonb into j from extensions.http_get('https://raw.githubusercontent.com/Movilang/movilang/main/content/tvd/tvd1.json');
  if j is null or jsonb_array_length(j) <> 36 then raise exception 'TVD: очікувалось 36 уроків'; end if;
  select id into cid from public.courses where slug = 'vampire-diaries-1';
  if cid is null then raise exception 'Курс vampire-diaries-1 не знайдено'; end if;

  -- перенумерація старих 28 уроків (тільки якщо ще не зроблено)
  if (select count(*) from public.lessons where course_id = cid) = 28 then
    update public.lessons set num = num + 100 where course_id = cid;
    update public.lessons set num = (array[1,2,3,5,6,7,9,10,12,13,14,15,17,18,20,21,22,23,24,25,26,28,29,30,32,34,35,36])[num - 100]
      where course_id = cid and num > 100;
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

  -- 2) «Гаррі Поттер»: словник B1
  select content::jsonb into j from extensions.http_get('https://raw.githubusercontent.com/Movilang/movilang/main/content/hp/hp.json');
  if j is null or jsonb_array_length(j) <> 36 then raise exception 'HP: очікувалось 36 уроків'; end if;
  select id into cid from public.courses where slug = 'harry-potter-1';
  for l in select * from jsonb_array_elements(j) loop
    update public.lessons set tasks = l->'tasks', variants = l->'variants'
    where course_id = cid and num = (l->>'num')::int;
  end loop;
end $$;

drop extension if exists http;

-- перевірка: має бути 36 і 36
select c.slug, count(l.id) from public.courses c join public.lessons l on l.course_id = c.id group by c.slug;
