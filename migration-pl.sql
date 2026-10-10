-- MovieLang: польська мова + ціни в злотих. Запустити один раз у Supabase → SQL Editor.
alter table public.courses add column if not exists title_pl text;
alter table public.courses add column if not exists description_pl text;
alter table public.lessons add column if not exists title_pl text;
alter table public.lessons add column if not exists scene_pl text;
update public.courses set price = '49 zł' where price like '%₴%' and price like '299%';
update public.courses set price = '59 zł' where price like '%₴%' and price like '349%';
update public.courses set title_pl = 'Harry Potter i Kamień Filozoficzny',
  description_pl = 'Przechodzisz historię razem z bohaterem: od dziwnego listu do finałowego zwycięstwa. Każda lekcja opiera się na jednej scenie i ćwiczy jeden temat gramatyczny.'
  where slug = 'harry-potter-1' and title_pl is null;
update public.lessons l set title_pl = v.t, scene_pl = v.s
from (values
 (1,'Zwykły dom, niezwykły chłopiec','Chłopiec mieszka z ciotką, wujem i kuzynem; jego pokój jest pod schodami.'),
 (2,'List, którego nie da się zatrzymać','Przychodzą dziesiątki listów, wuj próbuje je ukryć.'),
 (3,'Jesteś czarodziejem','Olbrzym znajduje chłopca na wyspie i wyjawia mu prawdę.'),
 (4,'Zakupy na magicznej ulicy','Kupowanie szaty, książek, różdżki i sowy.'),
 (5,'Peron i pociąg','Szukanie dziwnego peronu, poznanie przyjaciela w pociągu.'),
 (6,'Tiara wybiera dom','Ceremonia przydziału uczniów do domów.'),
 (7,'Pierwsza lekcja latania','Lekcja na miotłach i pierwsza gra w powietrzu.'),
 (8,'Finał: Twoja ulubiona scena','Podziemne próby i finałowe spotkanie.')) as v(n,t,s)
join public.courses c on c.slug = 'harry-potter-1'
where l.course_id = c.id and l.num = v.n and l.title_pl is null;
update public.site_settings set value = '49 zł' where key = 'plan1_price';
update public.site_settings set value = '119 zł' where key = 'plan2_price';
update public.site_settings set value = '59 zł / міс' where key = 'plan3_price';
