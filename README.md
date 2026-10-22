# MoviLang — як запустити сайт

Сайт складається з файлів `index.html`, `styles.css`, `app.js`, `config.js`.
Без налаштувань він працює в **демо-режимі** (дані лише в браузері). Для справжніх акаунтів підключіть безкоштовну базу **Supabase**.

## 1. Публікація (автоматична)
Сайт підключено до Cloudflare Pages через GitHub: кожна зміна в гілці `main` автоматично публікується на https://movilang.pages.dev за ~1 хвилину.

## 1a. Ручна публікація (запасний варіант)
1. Зайдіть на dash.cloudflare.com → **Workers & Pages** → **Create** → вкладка **Pages** → **Upload assets**.
2. Назва проєкту: `movielang` → завантажте папку з файлами (або zip) → **Deploy**.
3. Сайт буде доступний за адресою `https://movilang.pages.dev`. Власний домен: **Custom domains** у налаштуваннях проєкту.

## 2. Підключити базу даних (справжні акаунти)
1. Зареєструйтесь на supabase.com → **New project** (регіон: Central EU / Frankfurt).
2. **SQL Editor** → New query → вставте весь вміст `schema.sql` → **Run**.
3. **Project Settings → API**: скопіюйте `Project URL` і `anon public` key у `config.js`.
4. **Authentication → URL Configuration**: Site URL = адреса вашого сайту (напр. `https://movilang.pages.dev`).
5. (Необов'язково) **Authentication → Providers → Email**: вимкніть «Confirm email», щоб учні входили одразу після реєстрації.
6. Завантажте оновлені файли на Cloudflare Pages ще раз (**Create new deployment**).

## 3. Стати адміністратором
1. Зареєструйтесь на своєму сайті.
2. Supabase → SQL Editor → виконайте:
   `update public.profiles set role = 'admin' where email = 'ВАША@ПОШТА.com';`
3. Вийдіть і увійдіть знову — у меню з'явиться **Адмін**.

## Що вміє адмін-панель
- **Статистика**: учні, нові та активні за 7 днів, ключі, пройдені уроки, середній бал, графік за 14 днів.
- **Користувачі**: список з прогресом, призначення адмінів.
- **Курси й уроки**: створення курсів, уроків і завдань (vocabulary, listening, subtitles, grammar, speaking, quiz, фінал). У порожній базі є кнопка «Додати демо-курс Гаррі Поттер».
- **Ключі доступу**: генерація ключів для курсу чи всіх курсів, статус активації.
- **Тексти сайту**: заголовок, опис, тарифи, текст про покупку, FAQ.

## Що додати пізніше
- Автоматична оплата (WayForPay, LiqPay, Stripe) з видачею ключа після оплати. Зараз адмін генерує ключі і надсилає їх покупцю вручну.
- Запис голосу для speaking-завдань.

## Сюжетні курси (з 2026-10-12)
Плеєр підтримує додаткові поля і типи завдань (усі необов'язкові, старі курси працюють як раніше):
- `cards` — переказ попереднього епізоду і картки персонажів (не оцінюється);
- `glossary` — словник сцени: слово, транскрипція, частина мови, рівень, переклад, хто/кому, коротка репліка, приклад (не оцінюється);
- `quest` — розгалужений квест: кроки з виборами і 2–3 кінцівки;
- `why` — пояснення до кожного варіанта відповіді; `label` — власна назва типу завдання; `ins` — власна інструкція;
- `variants.arc` — заголовок арки на сторінці курсу; `variants.badge` — нагорода уроку; `variants.cert` — сертифікат (≥70%);
- `courses.free_first = false` — перший урок курсу платний.

Курс «Щоденники вампіра»: джерело — `content/tvd/*.py`, збірка й самоперевірка — `python3 content/tvd/build.py` → `content/tvd/tvd1.json`, завантаження в базу — `migration-tvd.sql`.
Не редагуйте уроки цього курсу в адмін-редакторі уроків: він не знає нових полів (картки, словник, квест).

## Оплата онлайн (Stripe: BLIK, Przelewy24, картка) — з 2026-10-18
1. Supabase → SQL Editor → запустити `migration-extras.sql`.
2. stripe.com → акаунт (PL), Settings → Payment methods: увімкнути BLIK і Przelewy24.
3. Supabase → Edge Functions → створити `checkout` (код: `supabase/functions/checkout/index.ts`) і `stripe-webhook` (код: `supabase/functions/stripe-webhook/index.ts`, **Verify JWT вимкнути**).
4. Stripe → Developers → Webhooks → Add endpoint: `https://pybzpbkmdupvtsmxlqvr.supabase.co/functions/v1/stripe-webhook`, події `checkout.session.completed` і `checkout.session.async_payment_succeeded`.
5. Supabase → Edge Functions → Secrets: `STRIPE_SECRET_KEY` (sk_live_…), `STRIPE_WEBHOOK_SECRET` (whsec_…), `SITE_URL` = https://movilang.pages.dev.
Ціна курсу береться з поля «ціна» курсу, ціна пакета — з налаштування `bundle_price`.

## Оновлення 2026-10-22: друзі, рейтинг, подарунки, реферали, відгуки, підтримка, листи, бекап

1. **SQL:** вставити `migration-2026-10-22.sql` у Supabase → SQL Editor → Run.
2. **Edge Functions** (Supabase → Edge Functions → Deploy / Edit, вставити код):
   - `checkout` — оновлений код (подарунки, знижка −20 % для рефералів);
   - `stripe-webhook` — оновлений код (подарунки, бонуси рефералів, листи), **Verify JWT вимкнути**;
   - `mailer` — новий, **Verify JWT вимкнути**;
   - `admin-refund` — новий (повернення коштів з адмінки).
3. **Secrets** (Supabase → Edge Functions → Secrets):
   - `RESEND_API_KEY` — ключ із resend.com (безкоштовно до 3000 листів/міс.);
   - `MAIL_FROM` — напр. `MoviLang <hello@твій-домен>` (до підтвердження домену в Resend можна `MoviLang <onboarding@resend.dev>` — листи йдуть лише на твою пошту);
   - `CRON_SECRET` — будь-який довгий випадковий рядок.
4. **GitHub → Settings → Secrets and variables → Actions:**
   - `CRON_SECRET` — той самий рядок (щоденні листи, `.github/workflows/daily.yml`);
   - `SUPABASE_DB_URL` — Supabase → Connect → Session pooler URI з паролем (щотижневий бекап, `.github/workflows/backup.yml`; файл — у вкладці Actions → backup → Artifacts, зберігається 90 днів).
5. **Правові сторінки:** у `privacy.html` і `terms.html` заповнити `[UZUPEŁNIJ: …]` (ім'я / фірма, адреса, NIP).

Нові сторінки: `#/friends` (дует і реферальне посилання `?ref=КОД`), `#/top` (рейтинг тижня), `#/gift` (подарунок), `#/support` (підтримка й повернення), `/blog/`, `/privacy.html`, `/terms.html`.
Нові вкладки адмінки: Питання, Підтримка (з кнопкою повернення коштів), Відгуки, Де кидають, Звіт за місяць (CSV/PDF), Перевірка курсів (автоперевірка + знайти й замінити).

## Ігровий світ курсу
Файл `world.js` — конфіг світу для кожного курсу (ключ = `slug`). Курс без запису працює як раніше.
- `factions` — 3–5 сторін (`icon`, `color`, назви uk/pl/en, `motto`). Ключі: латиниця, `a-z0-9_`.
- `ritual` — 5 питань англійською; кожна відповідь = `[текст, ключ_фракції]`. Перемагає фракція з найбільшою кількістю відповідей.
- `points` — назва й іконка валюти. Очки: 10 + бал/10 за урок, «бос» (урок із `quest`) ×3. Рахує сервер з `progress`.
- `collection` / `cardIcon` — картки за «босів» і фінал (слова беруться з `glossary` уроку). 100 % = золота рамка.
- `journal` — `open`, `sign`, `lines` (шаблони з `{w1..w3}`, `{t1..t3}`, `{line1..3}`, `{scene_en}`).
База: запустити `migration-world.sql` (таблиця `world_profiles`, RPC `join_faction`, `world_me`, `world_standings`, `world_top`).
Сторінка світу: `#/world/<id курсу>/me|rank|cards|journal`.
