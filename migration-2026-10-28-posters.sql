-- MoviLang · власні постери курсів (завантаження з адмінки). Запустити один раз.
alter table public.courses add column if not exists poster_url text;
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values ('posters', 'posters', true, 5242880, array['image/jpeg','image/png','image/webp'])
on conflict (id) do update set public = true, file_size_limit = 5242880, allowed_mime_types = array['image/jpeg','image/png','image/webp'];
drop policy if exists posters_read on storage.objects;
create policy posters_read on storage.objects for select using (bucket_id = 'posters');
drop policy if exists posters_admin_ins on storage.objects;
create policy posters_admin_ins on storage.objects for insert with check (bucket_id = 'posters' and public.is_admin());
drop policy if exists posters_admin_upd on storage.objects;
create policy posters_admin_upd on storage.objects for update using (bucket_id = 'posters' and public.is_admin());
drop policy if exists posters_admin_del on storage.objects;
create policy posters_admin_del on storage.objects for delete using (bucket_id = 'posters' and public.is_admin());
select 'ok' as status;
