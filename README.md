# MovieLang — як запустити сайт

Сайт складається з файлів `index.html`, `styles.css`, `app.js`, `config.js`.
Без налаштувань він працює в **демо-режимі** (дані лише в браузері). Для справжніх акаунтів підключіть безкоштовну базу **Supabase**.

## 1. Публікація (автоматична)
Сайт підключено до Cloudflare Pages через GitHub: кожна зміна в гілці `main` автоматично публікується на https://movielang.info-movielang.workers.dev за ~1 хвилину.

## 1a. Ручна публікація (запасний варіант)
1. Зайдіть на dash.cloudflare.com → **Workers & Pages** → **Create** → вкладка **Pages** → **Upload assets**.
2. Назва проєкту: `movielang` → завантажте папку з файлами (або zip) → **Deploy**.
3. Сайт буде доступний за адресою `https://movielang.info-movielang.workers.dev`. Власний домен: **Custom domains** у налаштуваннях проєкту.

## 2. Підключити базу даних (справжні акаунти)
1. Зареєструйтесь на supabase.com → **New project** (регіон: Central EU / Frankfurt).
2. **SQL Editor** → New query → вставте весь вміст `schema.sql` → **Run**.
3. **Project Settings → API**: скопіюйте `Project URL` і `anon public` key у `config.js`.
4. **Authentication → URL Configuration**: Site URL = адреса вашого сайту (напр. `https://movielang.info-movielang.workers.dev`).
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
