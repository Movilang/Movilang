-- Bezpieczeństwo (z audytu Supabase Advisors, 2026-11-06)
-- 1) Funkcje dla zalogowanych — goście (anon) nie powinni ich wywoływać
revoke execute on function public.add_friend(text) from anon, public;
revoke execute on function public.bump_activity(date, integer, integer) from anon, public;
revoke execute on function public.claim_referral(text) from anon, public;
revoke execute on function public.join_faction(uuid, text) from anon, public;
revoke execute on function public.my_friends() from anon, public;
revoke execute on function public.set_marketing(boolean) from anon, public;
revoke execute on function public.set_my_level(text) from anon, public;
revoke execute on function public.set_my_nick(text) from anon, public;
revoke execute on function public.world_me(uuid) from anon, public;
grant execute on function public.add_friend(text), public.bump_activity(date, integer, integer), public.claim_referral(text), public.join_faction(uuid, text), public.my_friends(), public.set_marketing(boolean), public.set_my_level(text), public.set_my_nick(text), public.world_me(uuid) to authenticated;
-- 2) Stały search_path
alter function public.ml_fill_code set search_path = public;
alter function public.world_lesson_points set search_path = public;
