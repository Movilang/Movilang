/* MovieLang — клієнтський застосунок.
   Два режими бекенду: Supabase (якщо заповнено config.js) або DEMO (localStorage). */
(function () {
'use strict';

/* ================= helpers ================= */
var $app = document.getElementById('app');
function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]; }); }
function toast(msg, type) { type = type || 'ok'; var t = document.createElement('div'); t.className = 'toast ' + type; t.setAttribute('role', 'status'); t.innerHTML = '<span class="ti">' + (type === 'ok' ? '✓' : type === 'err' ? '!' : 'i') + '</span><span></span>'; t.lastChild.textContent = msg; document.body.appendChild(t); setTimeout(function () { t.remove(); }, 3800); }
function uid() { return 'id' + Math.random().toString(36).slice(2, 10) + Date.now().toString(36); }
function fmtDate(d) { if (!d) return '—'; try { return new Date(d).toLocaleDateString(LANG === 'pl' ? 'pl-PL' : 'uk-UA', {day:'2-digit',month:'2-digit',year:'numeric'}); } catch (e) { return d; } }
function genCode() { var a = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789', s = ''; for (var i = 0; i < 12; i++) { s += a[Math.floor(Math.random() * a.length)]; if (i === 3 || i === 7) s += '-'; } return s; }
function say(t) { try { var u = new SpeechSynthesisUtterance(t); u.lang = 'en-GB'; u.rate = .9; speechSynthesis.cancel(); speechSynthesis.speak(u); } catch (e) { toast(t('Озвучення недоступне в цьому браузері'), 'err'); } }
var TASK_TYPES = { vocabulary:'VOCABULARY', listening:'LISTENING', subtitles:'SUBTITLES', grammar:'GRAMMAR', speaking:'SPEAKING', quiz:'MINI QUIZ', final:'FINAL' };
var POSTER_CLASSES = ['p1','p2','p3','p4','p5','p6','p7','p8'];


/* ================= i18n + theme ================= */
var I18N_PL = {"Логотип і значки":"Logo i ikony","Рамка логотипа ML":"Ramka logo ML","Фон усередині логотипа":"Tło wewnątrz logo","Літери ML":"Litery ML","Кружок з ініціалом":"Kółko z inicjałem","Ініціал у кружку":"Inicjał w kółku","Активна кнопка UA/PL: фон":"Aktywny przycisk UA/PL: tło","Активна кнопка UA/PL: текст":"Aktywny przycisk UA/PL: tekst","Активна кнопка UA/PL: рамка":"Aktywny przycisk UA/PL: ramka","Вибраний елемент":"Wybrany element","Зберегти як стандартний шаблон":"Zapisz jako szablon standardowy","Клікни елемент у перегляді, щоб змінити його колір":"Kliknij element w podglądzie, aby zmienić jego kolor","Вибрати елемент":"Wybierz element","Режим вибору: клікни будь-який елемент у перегляді":"Tryb wyboru: kliknij dowolny element w podglądzie","Режим вибору вимкнено":"Tryb wyboru wyłączony","Збережено як стандартний шаблон. Кнопка «Скинути до стандартних» тепер повертає до нього.":"Zapisano jako szablon standardowy. Przycisk „Przywróć domyślne” wraca teraz do niego.","<a href=\"#/admin\" style=\"color:var(--nav-admin)\">Адмін</a>":"<a href=\"#/admin\" style=\"color:var(--nav-admin)\">Admin</a>","Тло":"Tło","Текст":"Tekst","Головний екран":"Ekran główny","Меню":"Menu","Головна кнопка":"Główny przycisk","Другорядна кнопка":"Przycisk dodatkowy","Лінії та рамки":"Linie i ramki","Акценти":"Akcenty","Повідомлення":"Komunikaty","Фон сторінки":"Tło strony","Фон меню (верхня панель)":"Tło menu (górny pasek)","Фон карток і секцій":"Tło kart i sekcji","Фон елементів у картках":"Tło elementów w kartach","Фон полів вводу":"Tło pól formularza","Основний текст":"Tekst główny","Заголовки":"Nagłówki","Додатковий текст (описи)":"Tekst dodatkowy (opisy)","Приглушений текст (підказки)":"Tekst przygaszony (podpowiedzi)","Посилання":"Linki","Текст у футері":"Tekst w stopce","Надзаголовок":"Nadtytuł","Крапка перед надзаголовком":"Kropka przed nadtytułem","Заголовок: слово 1":"Nagłówek: słowo 1","Заголовок: слово 2":"Nagłówek: słowo 2","Заголовок: слово 3":"Nagłówek: słowo 3","Пункти меню":"Pozycje menu","Пункт меню при наведенні":"Pozycja menu po najechaniu","Пункт «Адмін»":"Pozycja „Admin”","Фон кнопки":"Tło przycisku","Текст кнопки":"Tekst przycisku","Рамка":"Ramka","Колір при наведенні":"Kolor po najechaniu","Рамки карток":"Ramki kart","Лінії-розділювачі":"Linie oddzielające","Рамки полів вводу":"Ramki pól formularza","Виділений тариф і стрічка":"Wyróżniony pakiet i wstążka","Значок рівня (A2–B1)":"Odznaka poziomu (A2–B1)","Прогрес: початок":"Postęp: początek","Прогрес: кінець":"Postęp: koniec","Стовпчики графіка":"Słupki wykresu","Успіх (зелений)":"Sukces (zielony)","Помилка (червоний)":"Błąd (czerwony)","Кожен елемент має власний колір. ↺ повертає стандартний.":"Każdy element ma własny kolor. ↺ przywraca domyślny.","Скинути":"Przywróć","Шаблон":"Szablon","Зберегти сюди":"Zapisz tutaj","Завантажити":"Wczytaj","порожній":"pusty","Опублікувати на сайті":"Opublikuj na stronie","Шаблони":"Szablony","Збережи поточні кольори в один із 3 слотів, щоб потім швидко повернутися до них.":"Zapisz obecne kolory w jednym z 3 slotów, aby szybko do nich wracać.","Курс":"Kurs","Урок":"Lekcja","Вхід":"Logowanie","Кабінет":"Konto","Головна":"Strona główna","Це справжній сайт: клікай і переходь між сторінками. Зміни видно лише тут, поки не натиснеш «Опублікувати».":"To prawdziwa strona: klikaj i przechodź między podstronami. Zmiany widać tylko tutaj, dopóki nie klikniesz „Opublikuj”.","Повернено стандартні значення. Натисни «Опублікувати», щоб застосувати.":"Przywrócono domyślne. Kliknij „Opublikuj”, aby zastosować.","Вигляд сайту опубліковано":"Wygląd strony opublikowany","Перезаписати? Натисни ще раз":"Nadpisać? Kliknij ponownie","Шаблон збережено":"Szablon zapisany","Шаблон завантажено в редактор. Натисни «Опублікувати», щоб застосувати на сайті.":"Szablon wczytany do edytora. Kliknij „Opublikuj”, aby zastosować na stronie.","Реєстрація":"Rejestracja","Пробний урок безкоштовно":"Darmowa lekcja próbna","Мої марафони":"Moje maratony","Пошта":"E-mail","активовано":"aktywowany","Каталог":"Katalog","Тарифи":"Cennik","Створити кабінет":"Załóż konto","Вигляд і кольори":"Wygląd i kolory","Кольори":"Kolory","Темна":"Ciemny","Світла":"Jasny","Окремі кольори для темної та світлої теми. Зміни видно у вікні попереднього перегляду одразу.":"Osobne kolory dla motywu ciemnego i jasnego. Zmiany od razu widać w oknie podglądu.","Шрифти":"Czcionki","Заголовки":"Nagłówki","Основний текст":"Tekst główny","Застосувати до всього сайту під час редагування":"Pokazuj zmiany na całej stronie podczas edycji","Зберегти вигляд":"Zapisz wygląd","Скинути до стандартних":"Przywróć domyślne","Скасувати зміни":"Anuluj zmiany","Попередній перегляд":"Podgląd","Посилання":"Link","Зміни скасовано":"Zmiany anulowane","Точно? Натисни ще раз":"Na pewno? Kliknij ponownie","Повернено стандартні значення. Натисни «Зберегти», щоб застосувати.":"Przywrócono domyślne. Kliknij „Zapisz”, aby zastosować.","Вигляд сайту збережено":"Wygląd strony zapisany","Фон сторінки":"Tło strony","Фон секцій і карток":"Tło sekcji i kart","Фон панелей і полів":"Tło paneli i pól","Рамки й лінії":"Ramki i linie","Додатковий текст":"Tekst dodatkowy","Приглушений текст":"Tekst przygaszony","Головний акцент (кнопки)":"Główny akcent (przyciski)","Текст на кнопках":"Tekst na przyciskach","Фіолетовий акцент":"Akcent fioletowy","Неоновий акцент (посилання, мітки)":"Akcent neonowy (linki, etykiety)","Виділення (рівні, значки)":"Wyróżnienia (poziomy, odznaki)","Успіх (зелений)":"Sukces (zielony)","Пошту підтверджено! Ласкаво просимо до MovieLang.":"E-mail potwierdzony! Witamy w MovieLang.","Пошту підтверджено! Тепер увійди.":"E-mail potwierdzony! Teraz się zaloguj.","Посилання недійсне або застаріле. Увійди або зареєструйся ще раз.":"Link jest nieważny lub wygasł. Zaloguj się lub zarejestruj ponownie.","Світла тема":"Jasny motyw","Темна тема":"Ciemny motyw","Потрібні права адміністратора": "Wymagane uprawnienia administratora", "Користувач з такою поштою вже існує": "Użytkownik z tym adresem e-mail już istnieje", "Невірна пошта або пароль": "Nieprawidłowy e-mail lub hasło", "Увійдіть в акаунт": "Zaloguj się na konto", "Такого ключа не знайдено. Перевір літери O та 0, I та 1.": "Nie znaleziono takiego klucza. Sprawdź litery O i 0, I i 1.", "Цей ключ уже активовано.": "Ten klucz został już aktywowany.", "Акаунт створено! Перевір пошту (і папку «Спам»), натисни посилання з листа, потім увійди.": "Konto utworzone! Sprawdź skrzynkę (i folder „Spam”), kliknij link z wiadomości, a potem się zaloguj.", "Пошту не підтверджено. Відкрий лист від Supabase і натисни посилання, потім увійди.": "E-mail niepotwierdzony. Otwórz wiadomość od Supabase, kliknij link, a potem się zaloguj.", "Невірна пошта або пароль.": "Nieprawidłowy e-mail lub hasło.", "Помилка входу: ": "Błąd logowania: ", "<a href=\"#/\">Головна</a><a href=\"#/catalog\">Каталог</a><a href=\"#/trial\">Пробний урок</a><a href=\"#/pricing\">Тарифи</a>": "<a href=\"#/\">Strona główna</a><a href=\"#/catalog\">Katalog</a><a href=\"#/trial\">Lekcja próbna</a><a href=\"#/pricing\">Cennik</a>", "<a href=\"#/cabinet\">Кабінет</a>": "<a href=\"#/cabinet\">Konto</a>", "<a href=\"#/admin\" style=\"color:var(--red)\">Адмін</a>": "<a href=\"#/admin\" style=\"color:var(--red)\">Admin</a>", "</span></a><button class=\"btn btn-ghost btn-sm\" type=\"button\" id=\"logoutBtn\">Вийти</button>": "</span></a><button class=\"btn btn-ghost btn-sm\" type=\"button\" id=\"logoutBtn\">Wyloguj</button>", "<a class=\"btn btn-ghost btn-sm\" href=\"#/login\">Увійти</a><a class=\"btn btn-red btn-sm\" href=\"#/register\">Реєстрація</a>": "<a class=\"btn btn-ghost btn-sm\" href=\"#/login\">Zaloguj się</a><a class=\"btn btn-red btn-sm\" href=\"#/register\">Rejestracja</a>", "Ви вийшли з акаунта": "Wylogowano", "СЕРІАЛ": "SERIAL", "ФІЛЬМ": "FILM", "<span class=\"tag new\">СКОРО</span>": "<span class=\"tag new\">WKRÓTCE</span>", "<div class=\"empty\">Курсів поки немає. Адміністратор може додати їх в адмін-панелі.</div>": "<div class=\"empty\">Na razie brak kursów. Administrator może je dodać w panelu admina.</div>", " уроків</span><b>": " lekcji</span><b>", "<span class=\"ribbon\">НАЙПОПУЛЯРНІШИЙ</span>": "<span class=\"ribbon\">NAJPOPULARNIEJSZY</span>", "\" href=\"#/buy\">Купити ключ</a></div>": "\" href=\"#/buy\">Kup klucz</a></div>", "Мій кабінет": "Moje konto", "Створити кабінет": "Załóż konto", "</a><a class=\"btn btn-ghost\" href=\"#/trial\">Пробний урок безкоштовно</a></div>": "</a><a class=\"btn btn-ghost\" href=\"#/trial\">Darmowa lekcja próbna</a></div>", "<div class=\"hero-meta\"><div><b>15 хв</b>на день</div><div><b>": "<div class=\"hero-meta\"><div><b>15 min</b>dziennie</div><div><b>", "</b>марафонів</div><div><b>6 типів</b>завдань</div></div></div>": "</b>maratonów</div><div><b>6 typów</b>zadań</div></div></div>", "<section><div class=\"sec-head\"><div class=\"eyebrow\">Як це працює</div><h2>Від квитка до першої розмови</h2></div><div class=\"steps\">": "<section><div class=\"sec-head\"><div class=\"eyebrow\">Jak to działa</div><h2>Od biletu do pierwszej rozmowy</h2></div><div class=\"steps\">", "Купуєш ключ": "Kupujesz klucz", "Обираєш фільм, пакет або підписку.": "Wybierasz film, pakiet lub subskrypcję.", "Активуєш": "Aktywujesz", "Вводиш код у кабінеті.": "Wpisujesz kod na swoim koncie.", "Відкриваєш марафон": "Otwierasz maraton", "Уроки за сценами фільму.": "Lekcje oparte na scenach z filmu.", "Виконуєш завдання": "Wykonujesz zadania", "Слова, аудіо, субтитри, граматика, говоріння.": "Słówka, audio, napisy, gramatyka, mówienie.", "Бачиш прогрес": "Widzisz postępy", "Статистика й бали в кабінеті.": "Statystyki i punkty na koncie.", "<section><div class=\"sec-head\"><div class=\"eyebrow\">Каталог</div><h2>Фільми та серіали</h2></div>": "<section><div class=\"sec-head\"><div class=\"eyebrow\">Katalog</div><h2>Filmy i seriale</h2></div>", "<section id=\"pricing\"><div class=\"sec-head\"><div class=\"eyebrow\">Тарифи</div><h2>Обери свій квиток</h2></div>": "<section id=\"pricing\"><div class=\"sec-head\"><div class=\"eyebrow\">Cennik</div><h2>Wybierz swój bilet</h2></div>", "<section><div class=\"sec-head\"><div class=\"eyebrow\">FAQ</div><h2>Питання та відповіді</h2></div>": "<section><div class=\"sec-head\"><div class=\"eyebrow\">FAQ</div><h2>Pytania i odpowiedzi</h2></div>", "<div class=\"page\"><div class=\"sec-head\"><div class=\"eyebrow\">Каталог</div><h2>Фільми та серіали</h2></div>": "<div class=\"page\"><div class=\"sec-head\"><div class=\"eyebrow\">Katalog</div><h2>Filmy i seriale</h2></div>", "<div class=\"page\"><div class=\"sec-head\"><div class=\"eyebrow\">Тарифи</div><h2>Обери свій квиток</h2></div>": "<div class=\"page\"><div class=\"sec-head\"><div class=\"eyebrow\">Cennik</div><h2>Wybierz swój bilet</h2></div>", "<div class=\"sec-head\" style=\"margin-top:30px\"><h2>Питання та відповіді</h2></div>": "<div class=\"sec-head\" style=\"margin-top:30px\"><h2>Pytania i odpowiedzi</h2></div>", "<div class=\"page\"><div class=\"sec-head\"><div class=\"eyebrow\">Купівля ключа</div><h2>Як отримати ключ доступу</h2><p class=\"lead\">": "<div class=\"page\"><div class=\"sec-head\"><div class=\"eyebrow\">Zakup klucza</div><h2>Jak zdobyć klucz dostępu</h2><p class=\"lead\">", "<div class=\"panel\" style=\"max-width:560px\"><h3>Уже маєш ключ?</h3><p class=\"muted\" style=\"margin-block:8px 14px\">Активуй його в особистому кабінеті.</p><a class=\"btn btn-red\" href=\"": "<div class=\"panel\" style=\"max-width:560px\"><h3>Masz już klucz?</h3><p class=\"muted\" style=\"margin-block:8px 14px\">Aktywuj go na swoim koncie.</p><a class=\"btn btn-red\" href=\"", "Перейти до кабінету": "Przejdź do konta", "Новий кабінет": "Nowe konto", "Вхід": "Logowanie", "Створи свій кабінет": "Załóż swoje konto", "З поверненням!": "Witaj ponownie!", "<label class=\"fl\" for=\"aName\">Ім'я<input class=\"inp-s\" id=\"aName\" autocomplete=\"name\" required></label>": "<label class=\"fl\" for=\"aName\">Imię<input class=\"inp-s\" id=\"aName\" autocomplete=\"name\" required></label>", "<label class=\"fl\" for=\"aEmail\">Пошта<input class=\"inp-s\" id=\"aEmail\" type=\"email\" autocomplete=\"email\" required></label>": "<label class=\"fl\" for=\"aEmail\">E-mail<input class=\"inp-s\" id=\"aEmail\" type=\"email\" autocomplete=\"email\" required></label>", "<label class=\"fl\" for=\"aPass\">Пароль": "<label class=\"fl\" for=\"aPass\">Hasło", " (мінімум 6 символів)": " (minimum 6 znaków)", "Зареєструватися": "Zarejestruj się", "Увійти": "Zaloguj się", "Вже є акаунт? <a href=\"#/login\">Увійти</a>": "Masz już konto? <a href=\"#/login\">Zaloguj się</a>", "Ще немає акаунта? <a href=\"#/register\">Створити кабінет</a>": "Nie masz jeszcze konta? <a href=\"#/register\">Załóż konto</a>", "<p class=\"hint\" style=\"margin-top:10px\">Демо: адмін admin@movielang.demo / admin123, учень olena@example.com / demo123</p>": "<p class=\"hint\" style=\"margin-top:10px\">Demo: admin admin@movielang.demo / admin123, uczeń olena@example.com / demo123</p>", "Введи коректну пошту, напр. name@gmail.com": "Wpisz poprawny e-mail, np. name@gmail.com", "Пароль має містити щонайменше 6 символів.": "Hasło musi mieć co najmniej 6 znaków.", "Вкажи своє ім'я.": "Podaj swoje imię.", "Зачекай…": "Chwileczkę…", "Кабінет створено!": "Konto utworzone!", "Вхід виконано": "Zalogowano", "Спершу увійди в акаунт": "Najpierw zaloguj się na konto", "Урок": "Lekcja", "Перший урок": "Pierwsza lekcja", "П'ять уроків": "Pięć lekcji", "Три дні навчання": "Trzy dni nauki", "Точність 90%+": "Trafność 90%+", "Два марафони": "Dwa maratony", "Марафон пройдено": "Maraton ukończony", "<div class=\"page\"><div class=\"sec-head\"><div class=\"eyebrow\">Особистий кабінет</div><h2>Привіт, ": "<div class=\"page\"><div class=\"sec-head\"><div class=\"eyebrow\">Moje konto</div><h2>Cześć, ", "<form class=\"form\" id=\"keyForm\" novalidate><label class=\"fl\" for=\"keyInput\">Активувати ключ<input class=\"inp\" id=\"keyInput\" placeholder=\"XXXX-XXXX-XXXX\" maxlength=\"14\" autocomplete=\"off\" style=\"font-size:15px;padding:11px 12px\"></label><button class=\"btn btn-red btn-sm\" type=\"submit\" style=\"justify-content:center\">Активувати</button><div class=\"msg small\" id=\"keyMsg\" role=\"status\"></div>": "<form class=\"form\" id=\"keyForm\" novalidate><label class=\"fl\" for=\"keyInput\">Aktywuj klucz<input class=\"inp\" id=\"keyInput\" placeholder=\"XXXX-XXXX-XXXX\" maxlength=\"14\" autocomplete=\"off\" style=\"font-size:15px;padding:11px 12px\"></label><button class=\"btn btn-red btn-sm\" type=\"submit\" style=\"justify-content:center\">Aktywuj</button><div class=\"msg small\" id=\"keyMsg\" role=\"status\"></div>", "<p class=\"hint\">Демо-ключ: HPS1-7KQ4-WZ9M</p>": "<p class=\"hint\">Klucz demo: HPS1-7KQ4-WZ9M</p>", "<a class=\"btn btn-ghost btn-sm\" href=\"#/admin\" style=\"justify-content:center\">Адмін-панель</a>": "<a class=\"btn btn-ghost btn-sm\" href=\"#/admin\" style=\"justify-content:center\">Panel admina</a>", "</b><span>уроків пройдено</span></div><div class=\"stat\"><b>": "</b><span>ukończonych lekcji</span></div><div class=\"stat\"><b>", "%</b><span>середній бал</span></div><div class=\"stat\"><b>": "%</b><span>średni wynik</span></div><div class=\"stat\"><b>", "</b><span>XP набрано</span></div><div class=\"stat\"><b>": "</b><span>zdobytych XP</span></div><div class=\"stat\"><b>", "</b><span>днів навчання</span></div></div>": "</b><span>dni nauki</span></div></div>", "<div class=\"rows\"><div class=\"box\"><h4>Мої марафони</h4>": "<div class=\"rows\"><div class=\"box\"><h4>Moje maratony</h4>", "<div class=\"empty small\">Марафонів ще немає. Активуй ключ або <a href=\"#/trial\">пройди пробний урок</a>.</div>": "<div class=\"empty small\">Nie masz jeszcze maratonów. Aktywuj klucz albo <a href=\"#/trial\">przejdź lekcję próbną</a>.</div>", "<a class=\"btn btn-ghost btn-sm\" href=\"#/catalog\" style=\"justify-self:start\">Каталог курсів</a></div>": "<a class=\"btn btn-ghost btn-sm\" href=\"#/catalog\" style=\"justify-self:start\">Katalog kursów</a></div>", "<div class=\"box\"><h4>Досягнення</h4><div class=\"ach\">": "<div class=\"box\"><h4>Osiągnięcia</h4><div class=\"ach\">", "<h4>Останні уроки</h4><div class=\"done-list\">": "<h4>Ostatnie lekcje</h4><div class=\"done-list\">", "<span class=\"muted\">Ще немає пройдених уроків</span>": "<span class=\"muted\">Brak ukończonych lekcji</span>", "Ключ має містити 12 символів.": "Klucz musi mieć 12 znaków.", "Ключ активовано! Марафон відкрито.": "Klucz aktywowany! Maraton odblokowany.", "<div class=\"page\"><div class=\"empty\">Курс не знайдено. <a href=\"#/catalog\">До каталогу</a></div></div>": "<div class=\"page\"><div class=\"empty\">Nie znaleziono kursu. <a href=\"#/catalog\">Do katalogu</a></div></div>", " уроків</span><span class=\"badge\">": " lekcji</span><span class=\"badge\">", "серіал": "serial", "фільм": "film", "<span class=\"badge\" style=\"color:var(--ok)\">доступ відкрито</span>": "<span class=\"badge\" style=\"color:var(--ok)\">dostęp odblokowany</span>", "<div class=\"row\"><a class=\"btn btn-red\" href=\"#/buy\">Купити ключ · ": "<div class=\"row\"><a class=\"btn btn-red\" href=\"#/buy\">Kup klucz · ", "<a class=\"btn btn-ghost\" href=\"#/cabinet\">Активувати ключ</a>": "<a class=\"btn btn-ghost\" href=\"#/cabinet\">Aktywuj klucz</a>", "<a class=\"btn btn-ghost\" href=\"#/register\">Створити кабінет</a>": "<a class=\"btn btn-ghost\" href=\"#/register\">Załóż konto</a>", " · безкоштовно": " · za darmo", "<div class=\"empty\" style=\"margin-top:20px\">Уроки цього марафону скоро з'являться.</div>": "<div class=\"empty\" style=\"margin-top:20px\">Lekcje tego maratonu pojawią się wkrótce.</div>", "</div><div class=\"panel\"><h3 style=\"margin-bottom:18px\">Типи завдань у курсі</h3><div class=\"task-types\">": "</div><div class=\"panel\"><h3 style=\"margin-bottom:18px\">Typy zadań w kursie</h3><div class=\"task-types\">", "</span><span class=\"tcount\">Завдання ": "</span><span class=\"tcount\">Zadanie ", " з ": " z ", "<div class=\"tscene\"><b>Сцена:</b> ": "<div class=\"tscene\"><b>Scena:</b> ", "<div><button class=\"speak\" type=\"button\" id=\"tsay\"><span class=\"play\"></span>Прослухати</button></div>": "<div><button class=\"speak\" type=\"button\" id=\"tsay\"><span class=\"play\"></span>Odsłuchaj</button></div>", "<textarea class=\"inp-s\" id=\"tfinal\" rows=\"6\" placeholder=\"My favourite scene is…\"></textarea><div class=\"row\"><button class=\"btn btn-red\" type=\"button\" id=\"tsubmit\">Зберегти відповідь</button><span class=\"hint\" id=\"wc\">0 слів</span></div>": "<textarea class=\"inp-s\" id=\"tfinal\" rows=\"6\" placeholder=\"My favourite scene is…\"></textarea><div class=\"row\"><button class=\"btn btn-red\" type=\"button\" id=\"tsubmit\">Zapisz odpowiedź</button><span class=\"hint\" id=\"wc\">0 słów</span></div>", "<div class=\"topts\"><button class=\"topt\" type=\"button\" data-s=\"1\">✓ Я повторив(ла)</button><button class=\"topt\" type=\"button\" data-s=\"0\">Пропустити</button></div>": "<div class=\"topts\"><button class=\"topt\" type=\"button\" data-s=\"1\">✓ Powtórzyłem(-am)</button><button class=\"topt\" type=\"button\" data-s=\"0\">Pomiń</button></div>", "<div class=\"tfb\" id=\"tfb\"></div><div class=\"tnav\"><span class=\"hint\">Підказки українською, завдання англійською</span><button class=\"btn btn-red\" type=\"button\" id=\"tnext\" hidden>Далі</button></div>": "<div class=\"tfb\" id=\"tfb\"></div><div class=\"tnav\"><span class=\"hint\">Wskazówki po polsku, zadania po angielsku</span><button class=\"btn btn-red\" type=\"button\" id=\"tnext\" hidden>Dalej</button></div>", " слів": " słów", "Напиши хоча б 20 слів (зараз ": "Napisz co najmniej 20 słów (teraz ", "Відповідь збережено! ": "Odpowiedź zapisana! ", "Далі": "Dalej", "Показати результат": "Pokaż wynik", "Правильно! ": "Dobrze! ", "Майже. ": "Prawie. ", "<div class=\"tres\"><span class=\"ttag\">РЕЗУЛЬТАТ</span><div class=\"big\">": "<div class=\"tres\"><span class=\"ttag\">WYNIK</span><div class=\"big\">", "</div><p class=\"lead\" style=\"text-align:center\" id=\"tresText\">Бал: ": "</div><p class=\"lead\" style=\"text-align:center\" id=\"tresText\">Wynik: ", "<div class=\"empty\">У цьому уроці ще немає завдань.</div>": "<div class=\"empty\">Ta lekcja nie ma jeszcze zadań.</div>", "<div class=\"page\"><div class=\"empty\">Урок не знайдено.</div></div>": "<div class=\"page\"><div class=\"empty\">Nie znaleziono lekcji.</div></div>", "<div class=\"page\"><div class=\"empty\">Цей урок відкривається після активації ключа. <a href=\"#/course/": "<div class=\"page\"><div class=\"empty\">Ta lekcja odblokuje się po aktywacji klucza. <a href=\"#/course/", "\">До марафону</a></div></div>": "\">Do maratonu</a></div></div>", "Марафон": "Maraton", "</a><div class=\"eyebrow\">Урок ": "</a><div class=\"eyebrow\">Lekcja ", "Бал: ": "Wynik: ", "%. Результат збережено в кабінеті.": "%. Wynik zapisany na Twoim koncie.", "%. Створи кабінет, щоб зберігати прогрес.": "%. Załóż konto, aby zapisywać postępy.", "\">Наступний урок</a>": "\">Następna lekcja</a>", "<a class=\"btn btn-red\" href=\"#/buy\">Отримати ключ доступу</a>": "<a class=\"btn btn-red\" href=\"#/buy\">Zdobądź klucz dostępu</a>", "</a><button class=\"btn btn-ghost\" type=\"button\" id=\"again\">Пройти ще раз</button>": "</a><button class=\"btn btn-ghost\" type=\"button\" id=\"again\">Przejdź jeszcze raz</button>", "<div class=\"page\"><div class=\"empty\">Пробний урок з'явиться, щойно буде створено перший курс.</div></div>": "<div class=\"page\"><div class=\"empty\">Lekcja próbna pojawi się, gdy zostanie utworzony pierwszy kurs.</div></div>", "<div class=\"page\"><div class=\"empty\">Ця сторінка доступна лише адміністратору.</div></div>": "<div class=\"page\"><div class=\"empty\">Ta strona jest dostępna tylko dla administratora.</div></div>", "<div class=\"page\"><div class=\"sec-head\"><div class=\"eyebrow\">Адмін-панель</div><h2>Керування MovieLang</h2></div><div class=\"tabs\" role=\"tablist\">": "<div class=\"page\"><div class=\"sec-head\"><div class=\"eyebrow\">Panel admina</div><h2>Zarządzanie MovieLang</h2></div><div class=\"tabs\" role=\"tablist\">", "Статистика": "Statystyki", "Користувачі": "Użytkownicy", "Курси й уроки": "Kursy i lekcje", "Ключі доступу": "Klucze dostępu", "Тексти сайту": "Teksty strony", "</div><div id=\"adminBody\"><p class=\"muted\">Завантаження…</p></div></div>": "</div><div id=\"adminBody\"><p class=\"muted\">Ładowanie…</p></div></div>", "<div class=\"empty\">Помилка: ": "<div class=\"empty\">Błąd: ", "</b><span>учнів усього</span></div><div class=\"stat\"><b>": "</b><span>uczniów łącznie</span></div><div class=\"stat\"><b>", "</b><span>нових за 7 днів</span></div>": "</b><span>nowych w 7 dni</span></div>", "</b><span>активних за 7 днів</span></div><div class=\"stat\"><b>": "</b><span>aktywnych w 7 dni</span></div><div class=\"stat\"><b>", "</b><span>ключів активовано</span></div></div>": "</b><span>aktywowanych kluczy</span></div></div>", "</b><span>курсів</span></div><div class=\"stat\"><b>": "</b><span>kursów</span></div><div class=\"stat\"><b>", "</b><span>записів на курси</span></div></div>": "</b><span>zapisów na kursy</span></div></div>", "<div class=\"rows\"><div class=\"box\"><h4>Пройдені уроки за 14 днів</h4><div class=\"week\" style=\"grid-template-columns:repeat(14,1fr);height:140px\">": "<div class=\"rows\"><div class=\"box\"><h4>Ukończone lekcje w ciągu 14 dni</h4><div class=\"week\" style=\"grid-template-columns:repeat(14,1fr);height:140px\">", "</div></div><div class=\"box\"><h4>Учні за курсами</h4><div class=\"bars\">": "</div></div><div class=\"box\"><h4>Uczniowie wg kursów</h4><div class=\"bars\">", "<div><button class=\"btn btn-danger btn-sm\" type=\"button\" id=\"resetDemo\">Скинути демо-дані</button></div>": "<div><button class=\"btn btn-danger btn-sm\" type=\"button\" id=\"resetDemo\">Zresetuj dane demo</button></div>", "Демо-дані скинуто": "Dane demo zresetowane", "Точно скинути? Натисни ще раз": "Na pewno? Kliknij ponownie", "<span class=\"muted small\">це ви</span>": "<span class=\"muted small\">to Ty</span>", "Зробити учнем": "Zmień na ucznia", "Зробити адміном": "Nadaj rolę admina", "<p class=\"muted\" style=\"margin-bottom:14px\">Усього: ": "<p class=\"muted\" style=\"margin-bottom:14px\">Łącznie: ", "</p><div class=\"tbl-wrap\"><table class=\"tbl\"><thead><tr><th>Користувач</th><th>Роль</th><th>Реєстрація</th><th>Курсів</th><th>Уроків</th><th>Сер. бал</th><th>Активність</th><th></th></tr></thead><tbody>": "</p><div class=\"tbl-wrap\"><table class=\"tbl\"><thead><tr><th>Użytkownik</th><th>Rola</th><th>Rejestracja</th><th>Kursy</th><th>Lekcje</th><th>Śr. wynik</th><th>Aktywność</th><th></th></tr></thead><tbody>", "Роль змінено": "Rola zmieniona", "<div class=\"row\" style=\"justify-content:space-between;margin-bottom:14px\"><span class=\"muted\">Курсів: ": "<div class=\"row\" style=\"justify-content:space-between;margin-bottom:14px\"><span class=\"muted\">Kursów: ", "</span><button class=\"btn btn-red btn-sm\" type=\"button\" id=\"newCourse\">+ Новий курс</button></div>": "</span><button class=\"btn btn-red btn-sm\" type=\"button\" id=\"newCourse\">+ Nowy kurs</button></div>", "<div class=\"tbl-wrap\"><table class=\"tbl\"><thead><tr><th>Курс</th><th>Тип</th><th>Рівень</th><th>Уроків</th><th>Ціна</th><th>Статус</th><th></th></tr></thead><tbody>": "<div class=\"tbl-wrap\"><table class=\"tbl\"><thead><tr><th>Kurs</th><th>Typ</th><th>Poziom</th><th>Lekcje</th><th>Cena</th><th>Status</th><th></th></tr></thead><tbody>", "Серіал": "Serial", "Фільм": "Film", "опубліковано": "opublikowany", "чернетка": "szkic", "\">Редагувати</button></td></tr>": "\">Edytuj</button></td></tr>", "<div class=\"empty\">Курсів ще немає. <button class=\"btn btn-ghost btn-sm\" type=\"button\" id=\"importSeed\">Додати демо-курс «Гаррі Поттер»</button></div>": "<div class=\"empty\">Nie ma jeszcze kursów. <button class=\"btn btn-ghost btn-sm\" type=\"button\" id=\"importSeed\">Dodaj kurs demo „Harry Potter”</button></div>", "Демо-курс додано": "Kurs demo dodany", "<div style=\"display:grid;gap:18px\"><button class=\"btn btn-ghost btn-sm\" type=\"button\" id=\"back\" style=\"justify-self:start\">← Усі курси</button>": "<div style=\"display:grid;gap:18px\"><button class=\"btn btn-ghost btn-sm\" type=\"button\" id=\"back\" style=\"justify-self:start\">← Wszystkie kursy</button>", "Редагування курсу": "Edycja kursu", "Новий курс": "Nowy kurs", "<label class=\"fl\" for=\"cTitle\">Назва<input class=\"inp-s\" id=\"cTitle\" value=\"": "<label class=\"fl\" for=\"cTitle\">Tytuł<input class=\"inp-s\" id=\"cTitle\" value=\"", "<div class=\"grid3\"><label class=\"fl\" for=\"cKind\">Тип<select class=\"inp-s\" id=\"cKind\"><option value=\"film\"": "<div class=\"grid3\"><label class=\"fl\" for=\"cKind\">Typ<select class=\"inp-s\" id=\"cKind\"><option value=\"film\"", ">Фільм</option><option value=\"series\"": ">Film</option><option value=\"series\"", ">Серіал</option></select></label>": ">Serial</option></select></label>", "<label class=\"fl\" for=\"cLevel\">Рівень<input class=\"inp-s\" id=\"cLevel\" value=\"": "<label class=\"fl\" for=\"cLevel\">Poziom<input class=\"inp-s\" id=\"cLevel\" value=\"", "\"></label><label class=\"fl\" for=\"cPrice\">Ціна<input class=\"inp-s\" id=\"cPrice\" value=\"": "\"></label><label class=\"fl\" for=\"cPrice\">Cena<input class=\"inp-s\" id=\"cPrice\" value=\"", "<div class=\"grid2\"><label class=\"fl\" for=\"cPoster\">Колір постера<select class=\"inp-s\" id=\"cPoster\">": "<div class=\"grid2\"><label class=\"fl\" for=\"cPoster\">Kolor plakatu<select class=\"inp-s\" id=\"cPoster\">", "Фіолетовий": "Fioletowy", "Бордовий": "Bordowy", "Синій": "Niebieski", "Зелений": "Zielony", "Червоний": "Czerwony", "Золотий": "Złoty", "Індиго": "Indygo", "Рожевий": "Różowy", "<label class=\"fl\" for=\"cPub\">Статус<select class=\"inp-s\" id=\"cPub\"><option value=\"1\"": "<label class=\"fl\" for=\"cPub\">Status<select class=\"inp-s\" id=\"cPub\"><option value=\"1\"", ">Опубліковано</option><option value=\"0\"": ">Opublikowany</option><option value=\"0\"", ">Чернетка</option></select></label></div>": ">Szkic</option></select></label></div>", "<label class=\"fl\" for=\"cDesc\">Опис<textarea class=\"inp-s\" id=\"cDesc\">": "<label class=\"fl\" for=\"cDesc\">Opis<textarea class=\"inp-s\" id=\"cDesc\">", "<div class=\"row\"><button class=\"btn btn-red\" type=\"submit\">Зберегти курс</button>": "<div class=\"row\"><button class=\"btn btn-red\" type=\"submit\">Zapisz kurs</button>", "<button class=\"btn btn-danger btn-sm\" type=\"button\" id=\"delC\">Видалити курс</button>": "<button class=\"btn btn-danger btn-sm\" type=\"button\" id=\"delC\">Usuń kurs</button>", "<div class=\"panel\" style=\"display:grid;gap:14px\"><div class=\"row\" style=\"justify-content:space-between\"><h3>Уроки (": "<div class=\"panel\" style=\"display:grid;gap:14px\"><div class=\"row\" style=\"justify-content:space-between\"><h3>Lekcje (", ")</h3><button class=\"btn btn-red btn-sm\" type=\"button\" id=\"newL\">+ Новий урок</button></div>": ")</h3><button class=\"btn btn-red btn-sm\" type=\"button\" id=\"newL\">+ Nowa lekcja</button></div>", " завдань</small></span><button class=\"btn btn-ghost btn-sm\" type=\"button\" data-l=\"": " zadań</small></span><button class=\"btn btn-ghost btn-sm\" type=\"button\" data-l=\"", "\">Редагувати</button></li>": "\">Edytuj</button></li>", "<div class=\"empty\">Додай перший урок.</div>": "<div class=\"empty\">Dodaj pierwszą lekcję.</div>", "<p class=\"muted\">Після збереження курсу можна буде додавати уроки.</p>": "<p class=\"muted\">Po zapisaniu kursu będzie można dodawać lekcje.</p>", "Вкажи назву курсу.": "Podaj tytuł kursu.", "Курс збережено": "Kurs zapisany", "Видалити разом з уроками? Натисни ще раз": "Usunąć razem z lekcjami? Kliknij ponownie", "Курс видалено": "Kurs usunięty", "\"><div class=\"row\" style=\"justify-content:space-between\"><b>Завдання ": "\"><div class=\"row\" style=\"justify-content:space-between\"><b>Zadanie ", "\">Видалити</button></div>": "\">Usuń</button></div>", "<div class=\"grid2\"><label class=\"fl\">Тип<select class=\"inp-s\" data-f=\"type\">": "<div class=\"grid2\"><label class=\"fl\">Typ<select class=\"inp-s\" data-f=\"type\">", "<label class=\"fl\">Опис сцени<input class=\"inp-s\" data-f=\"scene\" value=\"": "<label class=\"fl\">Opis sceny<input class=\"inp-s\" data-f=\"scene\" value=\"", "<label class=\"fl\">Питання / речення (пропуск позначай ____)<input class=\"inp-s\" data-f=\"q\" value=\"": "<label class=\"fl\">Pytanie / zdanie (lukę oznacz ____)<input class=\"inp-s\" data-f=\"q\" value=\"", "<div class=\"grid2\"><label class=\"fl\">Варіанти через « / »<input class=\"inp-s\" data-f=\"options\" value=\"": "<div class=\"grid2\"><label class=\"fl\">Warianty oddzielone « / »<input class=\"inp-s\" data-f=\"options\" value=\"", "<label class=\"fl\">Номер правильного варіанта (1, 2, 3…)<input class=\"inp-s\" data-f=\"answer\" type=\"number\" min=\"1\" value=\"": "<label class=\"fl\">Numer poprawnej odpowiedzi (1, 2, 3…)<input class=\"inp-s\" data-f=\"answer\" type=\"number\" min=\"1\" value=\"", "<div class=\"grid2\"><label class=\"fl\">Фраза для озвучення (необов'язково)<input class=\"inp-s\" data-f=\"say\" value=\"": "<div class=\"grid2\"><label class=\"fl\">Fraza do odsłuchu (opcjonalnie)<input class=\"inp-s\" data-f=\"say\" value=\"", "<label class=\"fl\">Пояснення після відповіді<input class=\"inp-s\" data-f=\"tip\" value=\"": "<label class=\"fl\">Wyjaśnienie po odpowiedzi<input class=\"inp-s\" data-f=\"tip\" value=\"", "<div style=\"display:grid;gap:18px\"><button class=\"btn btn-ghost btn-sm\" type=\"button\" id=\"backC\" style=\"justify-self:start\">← До курсу</button>": "<div style=\"display:grid;gap:18px\"><button class=\"btn btn-ghost btn-sm\" type=\"button\" id=\"backC\" style=\"justify-self:start\">← Do kursu</button>", "Редагування уроку": "Edycja lekcji", "Новий урок": "Nowa lekcja", "<div class=\"grid3\"><label class=\"fl\" for=\"lNum\">Номер<input class=\"inp-s\" id=\"lNum\" type=\"number\" min=\"1\" value=\"": "<div class=\"grid3\"><label class=\"fl\" for=\"lNum\">Numer<input class=\"inp-s\" id=\"lNum\" type=\"number\" min=\"1\" value=\"", "\"></label><label class=\"fl\" for=\"lTitle\" style=\"grid-column:span 2\">Назва уроку<input class=\"inp-s\" id=\"lTitle\" value=\"": "\"></label><label class=\"fl\" for=\"lTitle\" style=\"grid-column:span 2\">Tytuł lekcji<input class=\"inp-s\" id=\"lTitle\" value=\"", "<div class=\"grid2\"><label class=\"fl\" for=\"lGr\">Граматика / тема<input class=\"inp-s\" id=\"lGr\" value=\"": "<div class=\"grid2\"><label class=\"fl\" for=\"lGr\">Gramatyka / temat<input class=\"inp-s\" id=\"lGr\" value=\"", "\"></label><label class=\"fl\" for=\"lScene\">Сцена (опис своїми словами)<input class=\"inp-s\" id=\"lScene\" value=\"": "\"></label><label class=\"fl\" for=\"lScene\">Scena (opis własnymi słowami)<input class=\"inp-s\" id=\"lScene\" value=\"", "<h3 style=\"margin-top:8px\">Завдання (": "<h3 style=\"margin-top:8px\">Zadanie (", "<button class=\"btn btn-ghost btn-sm\" type=\"button\" id=\"addT\" style=\"justify-self:start\">+ Додати завдання</button>": "<button class=\"btn btn-ghost btn-sm\" type=\"button\" id=\"addT\" style=\"justify-self:start\">+ Dodaj zadanie</button>", "<div class=\"row\"><button class=\"btn btn-red\" type=\"submit\">Зберегти урок</button>": "<div class=\"row\"><button class=\"btn btn-red\" type=\"submit\">Zapisz lekcję</button>", "\">Переглянути як учень</a><button class=\"btn btn-danger btn-sm\" type=\"button\" id=\"delL\">Видалити урок</button>": "\">Zobacz jako uczeń</a><button class=\"btn btn-danger btn-sm\" type=\"button\" id=\"delL\">Usuń lekcję</button>", "Вкажи назву уроку.": "Podaj tytuł lekcji.", "У ": "W ", " завданні(ях) порожнє питання.": " zadaniu(-ach) brakuje pytania.", "Урок збережено": "Lekcja zapisana", "Точно видалити? Натисни ще раз": "Na pewno usunąć? Kliknij ponownie", "Урок видалено": "Lekcja usunięta", "<form class=\"panel form\" id=\"kForm\" novalidate style=\"margin-bottom:18px\"><h3>Згенерувати ключі</h3><div class=\"grid3\"><label class=\"fl\" for=\"kCourse\">Курс<select class=\"inp-s\" id=\"kCourse\"><option value=\"\">Усі курси (підписка)</option>": "<form class=\"panel form\" id=\"kForm\" novalidate style=\"margin-bottom:18px\"><h3>Wygeneruj klucze</h3><div class=\"grid3\"><label class=\"fl\" for=\"kCourse\">Kurs<select class=\"inp-s\" id=\"kCourse\"><option value=\"\">Wszystkie kursy (subskrypcja)</option>", "<label class=\"fl\" for=\"kN\">Кількість<input class=\"inp-s\" id=\"kN\" type=\"number\" min=\"1\" max=\"100\" value=\"5\"></label><div style=\"align-self:end\"><button class=\"btn btn-red\" type=\"submit\">Створити</button></div></div><div id=\"kNew\"></div></form>": "<label class=\"fl\" for=\"kN\">Ilość<input class=\"inp-s\" id=\"kN\" type=\"number\" min=\"1\" max=\"100\" value=\"5\"></label><div style=\"align-self:end\"><button class=\"btn btn-red\" type=\"submit\">Utwórz</button></div></div><div id=\"kNew\"></div></form>", "<div class=\"tbl-wrap\"><table class=\"tbl\"><thead><tr><th>Ключ</th><th>Курс</th><th>Створено</th><th>Статус</th><th></th></tr></thead><tbody>": "<div class=\"tbl-wrap\"><table class=\"tbl\"><thead><tr><th>Klucz</th><th>Kurs</th><th>Utworzono</th><th>Status</th><th></th></tr></thead><tbody>", "Усі курси": "Wszystkie kursy", "<span class=\"pill ok\">активовано</span><br><span class=\"muted small\">": "<span class=\"pill ok\">aktywowany</span><br><span class=\"muted small\">", "<span class=\"pill warn\">вільний</span>": "<span class=\"pill warn\">wolny</span>", "\">Копіювати</button> <button class=\"btn btn-danger btn-sm\" type=\"button\" data-kdel=\"": "\">Kopiuj</button> <button class=\"btn btn-danger btn-sm\" type=\"button\" data-kdel=\"", "\">Видалити</button>": "\">Usuń</button>", "Створено ключів: ": "Utworzono kluczy: ", "<p class=\"muted small\" style=\"margin-top:10px\">Нові ключі:</p><pre style=\"font-family:var(--f-mono);color:var(--neon);white-space:pre-wrap;user-select:all\">": "<p class=\"muted small\" style=\"margin-top:10px\">Nowe klucze:</p><pre style=\"font-family:var(--f-mono);color:var(--neon);white-space:pre-wrap;user-select:all\">", "Скопійовано: ": "Skopiowano: ", "Ключ: ": "Klucz: ", "Точно?": "Na pewno?", "Ключ видалено": "Klucz usunięty", "Надзаголовок головної": "Nadtytuł strony głównej", "Заголовок, слово 1": "Nagłówek, słowo 1", "Заголовок, слово 2": "Nagłówek, słowo 2", "Заголовок, слово 3": "Nagłówek, słowo 3", "Опис під заголовком": "Opis pod nagłówkiem", "Тариф 1: назва": "Pakiet 1: nazwa", "Тариф 1: ціна": "Pakiet 1: cena", "Тариф 1: пункти (кожен з нового рядка)": "Pakiet 1: punkty (każdy w nowej linii)", "Тариф 2: назва": "Pakiet 2: nazwa", "Тариф 2: ціна": "Pakiet 2: cena", "Тариф 2: пункти": "Pakiet 2: punkty", "Тариф 3: назва": "Pakiet 3: nazwa", "Тариф 3: ціна": "Pakiet 3: cena", "Тариф 3: пункти": "Pakiet 3: punkty", "Як купити ключ (текст на сторінці покупки)": "Jak kupić klucz (tekst na stronie zakupu)", "FAQ: кожен рядок «Питання|Відповідь»": "FAQ: każda linia „Pytanie|Odpowiedź”", "<form class=\"panel form\" id=\"sForm\" novalidate><h3>Тексти на сайті</h3><p class=\"muted small\">Зміни одразу з'являться на головній, у тарифах і FAQ.</p>": "<form class=\"panel form\" id=\"sForm\" novalidate><h3>Teksty na stronie</h3><p class=\"muted small\">Zmiany od razu pojawią się na stronie głównej, w cenniku i FAQ.</p>", "<div class=\"row\"><button class=\"btn btn-red\" type=\"submit\">Зберегти зміни</button><a class=\"btn btn-ghost btn-sm\" href=\"#/\">Переглянути сайт</a></div></form>": "<div class=\"row\"><button class=\"btn btn-red\" type=\"submit\">Zapisz zmiany</button><a class=\"btn btn-ghost btn-sm\" href=\"#/\">Zobacz stronę</a></div></form>", "Тексти сайту збережено": "Teksty strony zapisane", "<div class=\"page\"><div class=\"empty\">Сторінку не знайдено. <a href=\"#/\">На головну</a></div></div>": "<div class=\"page\"><div class=\"empty\">Nie znaleziono strony. <a href=\"#/\">Na stronę główną</a></div></div>", "<div class=\"page\"><div class=\"empty\">Помилка: ": "<div class=\"page\"><div class=\"empty\">Błąd: ", "<div class=\"page\"><p class=\"muted\">Завантаження…</p></div>": "<div class=\"page\"><p class=\"muted\">Ładowanie…</p></div>", "Озвучення недоступне в цьому браузері": "Odsłuch niedostępny w tej przeglądarce"};
var LANG = 'uk';
try { LANG = localStorage.getItem('ml_lang') || ((navigator.language || '').slice(0, 2) === 'pl' ? 'pl' : 'uk'); } catch (e) {}
function t(s) { return LANG === 'pl' && I18N_PL[s] != null ? I18N_PL[s] : s; }
function setLang(l) { LANG = l; try { localStorage.setItem('ml_lang', l); } catch (e) {} applyStatic(); renderNav(); route(); }
var THEME = 'dark';
try { THEME = localStorage.getItem('ml_theme') || 'dark'; } catch (e) {}
function applyTheme() { document.documentElement.setAttribute('data-theme', THEME); }
function toggleTheme() { THEME = THEME === 'dark' ? 'light' : 'dark'; try { localStorage.setItem('ml_theme', THEME); } catch (e) {} applyTheme(); renderNav(); }
applyTheme();
function applyStatic() {
  document.documentElement.lang = LANG === 'pl' ? 'pl' : 'uk';
  var d = document.getElementById('discl'); if (d) d.textContent = LANG === 'pl' ? 'Tytuły filmów i seriali służą do opisu treści kursów; projekt nie jest powiązany z właścicielami praw.' : "Назви фільмів і серіалів використано для опису змісту курсів; проєкт не пов'язаний із правовласниками.";
  var b = document.getElementById('demoBar'); if (b) b.textContent = LANG === 'pl' ? 'Tryb demo: dane zapisują się tylko w tej przeglądarce. Admin: admin@movielang.demo / admin123' : 'Демо-режим: дані зберігаються лише в цьому браузері. Адмін: admin@movielang.demo / admin123';
}
function tr(o, k) { return o ? (LANG === 'pl' && o[k + '_pl'] ? o[k + '_pl'] : o[k]) : ''; }

/* ================= custom theme (admin) ================= */
var THEME_GROUPS = [
  ['Тло', [['page-bg','Фон сторінки'],['nav-bg','Фон меню (верхня панель)'],['card-bg','Фон карток і секцій'],['panel-bg','Фон елементів у картках'],['input-bg','Фон полів вводу']]],
  ['Текст', [['text','Основний текст'],['heading','Заголовки'],['text-2','Додатковий текст (описи)'],['text-3','Приглушений текст (підказки)'],['link','Посилання'],['footer-text','Текст у футері']]],
  ['Головний екран', [['eyebrow','Надзаголовок'],['eyebrow-dot','Крапка перед надзаголовком'],['hero-1','Заголовок: слово 1'],['hero-2','Заголовок: слово 2'],['hero-3','Заголовок: слово 3']]],
  ['Логотип і значки', [['logo-bg','Рамка логотипа ML'],['logo-inner','Фон усередині логотипа'],['logo-text','Літери ML'],['avatar-bg','Кружок з ініціалом'],['avatar-text','Ініціал у кружку'],['toggle-bg','Активна кнопка UA/PL: фон'],['toggle-text','Активна кнопка UA/PL: текст'],['toggle-border','Активна кнопка UA/PL: рамка']]],
  ['Меню', [['nav-link','Пункти меню'],['nav-link-hover','Пункт меню при наведенні'],['nav-admin','Пункт «Адмін»']]],
  ['Головна кнопка', [['btn-bg','Фон кнопки'],['btn-text','Текст кнопки']]],
  ['Другорядна кнопка', [['btn2-text','Текст'],['btn2-border','Рамка'],['btn2-hover','Колір при наведенні']]],
  ['Лінії та рамки', [['border','Рамки карток'],['divider','Лінії-розділювачі'],['input-border','Рамки полів вводу']]],
  ['Акценти', [['highlight','Виділений тариф і стрічка'],['badge-level','Значок рівня (A2–B1)'],['progress-1','Прогрес: початок'],['progress-2','Прогрес: кінець'],['chart-bar','Стовпчики графіка']]],
  ['Повідомлення', [['success','Успіх (зелений)'],['error','Помилка (червоний)']]]
];
var THEME_TOKENS = [];
THEME_GROUPS.forEach(function (g) { g[1].forEach(function (tk) { THEME_TOKENS.push(tk); }); });
var THEME_DEFAULTS = {
  dark: {bg:'#0b0a12',bg2:'#13111d',panel:'#1a1726',line:'#2c2840',fg:'#f3f0fa',muted:'#a39dba',dim:'#6f6987',red:'#ff3b4e',btnfg:'#ffffff',violet:'#8b5cf6',neon:'#3ee7ff',gold:'#ffd166',ok:'#3ddc97'},
  light:{bg:'#f6f4fb',bg2:'#ffffff',panel:'#efebf8',line:'#dcd6ea',fg:'#17131f',muted:'#555067',dim:'#7d7791',red:'#e11d48',btnfg:'#ffffff',violet:'#7c3aed',neon:'#0e7490',gold:'#b45309',ok:'#15803d'}
};
var FONT_CHOICES = {
  display: ['Dela Gothic One','Unbounded','Russo One','Montserrat Alternates','Rubik Mono One','Playfair Display','Oswald','Comfortaa'],
  body: ['Onest','Inter Tight','Manrope','Rubik','Nunito','Montserrat','PT Sans','Golos Text']
};
function parseCustomTheme(v) { var o = {dark:{}, light:{}, fonts:{}}; try { var p = typeof v === 'string' ? JSON.parse(v || '{}') : (v || {}); o.dark = p.dark || {}; o.light = p.light || {}; o.fonts = p.fonts || {}; } catch (e) {} return o; }
function themeCss(ct) {
  var css = '';
  ['dark','light'].forEach(function (m) {
    var vals = ct[m] || {}, parts = [];
    Object.keys(vals).forEach(function (k) { if (/^#[0-9a-fA-F]{3,8}$/.test(vals[k])) parts.push('--' + k + ':' + vals[k]); });
    if (parts.length) css += ':root[data-theme="' + m + '"]{' + parts.join(';') + '}';
  });
  var f = ct.fonts || {};
  if (f.display && FONT_CHOICES.display.indexOf(f.display) > -1) css += ':root{--f-display:"' + f.display + '","Onest",Impact,sans-serif}';
  if (f.body && FONT_CHOICES.body.indexOf(f.body) > -1) css += ':root{--f-body:"' + f.body + '",system-ui,-apple-system,"Segoe UI",sans-serif}body{font-family:var(--f-body)}';
  return css;
}
function loadFont(name) {
  if (!name || document.querySelector('link[data-font="' + name + '"]')) return;
  var l = document.createElement('link'); l.rel = 'stylesheet'; l.dataset.font = name;
  l.href = 'https://fonts.googleapis.com/css2?family=' + encodeURIComponent(name).replace(/%20/g, '+') + ':wght@400;600;700&display=swap';
  document.head.appendChild(l);
}
function applyCustomTheme(ct) {
  ct = ct || parseCustomTheme(SETTINGS.theme_custom);
  var el = document.getElementById('customTheme');
  if (!el) { el = document.createElement('style'); el.id = 'customTheme'; document.head.appendChild(el); }
  el.textContent = themeCss(ct);
  if (ct.fonts) { loadFont(ct.fonts.display); loadFont(ct.fonts.body); }
}

function LS() { var o = {}; for (var k in DEFAULT_SETTINGS) { if (/_pl$/.test(k)) continue; var v = SETTINGS[k]; if (LANG === 'pl' && SETTINGS[k + '_pl']) v = SETTINGS[k + '_pl']; o[k] = v; } return o; }

/* ================= default content ================= */
var DEFAULT_SETTINGS = {
  theme_custom: '', theme_presets: '', theme_default: '',
  hero_eyebrow: 'Онлайн-марафон англійської · A2–B2',
  hero_w1: 'Дивись.', hero_w2: 'Розумій.', hero_w3: 'Говори.',
  hero_lead: 'Вчи англійську на сценах з улюблених фільмів і серіалів. Купуєш персональний ключ, відкриваєш марафон і щодня проходиш короткі завдання: слова зі сцени, аудіювання, субтитри з пропусками, граматику і говоріння.',
  plan1_name: 'Один фільм', plan1_price: '49 zł', plan1_text: '1 марафон на вибір\n7–10 уроків\nСловник і картки\nСертифікат після фіналу',
  plan2_name: 'Пакет фільмів', plan2_price: '119 zł', plan2_text: '3 марафони на вибір\nПеревірка speaking-завдань\nРозширений словник з аудіо\nКлюч можна подарувати',
  plan3_name: 'Підписка', plan3_price: '59 zł / міс', plan3_text: 'Усі марафони каталогу\nНові марафони щомісяця\nРозмовний клуб онлайн\nСкасування в один клік',
  buy_info: 'Щоб купити ключ, напишіть нам: info.movielang@gmail.com — ключ надійде на пошту протягом години.',
  faq: 'Чи потрібно мати сам фільм?|Ні. Уроки містять опис сцен і навчальні аудіо, а всі завдання ми створюємо самі.\nЯкий рівень англійської потрібен?|Від A2. Кожен марафон має позначку рівня, а пояснення граматики написані українською.\nЩо таке ключ доступу?|Персональний код з 12 символів. Введи його в кабінеті, і марафон відкриється.\nСкільки часу займає урок?|10–15 хвилин. Прогрес зберігається після кожного уроку.\nЧи можна подарувати ключ?|Так. Ключ не прив\'язаний до покупця, доки його не активовано.',
  hero_eyebrow_pl: 'Maraton angielskiego online · A2–B2',
  hero_w1_pl: 'Oglądaj.', hero_w2_pl: 'Rozumiej.', hero_w3_pl: 'Mów.',
  hero_lead_pl: 'Ucz się angielskiego na scenach z ulubionych filmów i seriali. Kupujesz osobisty klucz, otwierasz maraton i codziennie wykonujesz krótkie zadania: słówka ze sceny, słuchanie, napisy z lukami, gramatykę i mówienie.',
  plan1_name_pl: 'Jeden film', plan1_price_pl: '49 zł', plan1_text_pl: '1 maraton do wyboru\n7–10 lekcji\nSłowniczek i fiszki\nCertyfikat po finale',
  plan2_name_pl: 'Pakiet filmów', plan2_price_pl: '119 zł', plan2_text_pl: '3 maratony do wyboru\nSprawdzanie zadań speaking\nRozszerzony słowniczek z audio\nKlucz można podarować',
  plan3_name_pl: 'Subskrypcja', plan3_price_pl: '59 zł / mies.', plan3_text_pl: 'Wszystkie maratony z katalogu\nNowe maratony co miesiąc\nKlub konwersacyjny online\nAnulowanie jednym kliknięciem',
  buy_info_pl: 'Aby kupić klucz, napisz do nas: info.movielang@gmail.com — klucz wyślemy e-mailem w ciągu godziny.',
  faq_pl: 'Czy muszę mieć sam film?|Nie. Lekcje zawierają opisy scen i nagrania edukacyjne, a wszystkie zadania tworzymy sami.\nJaki poziom angielskiego jest potrzebny?|Od A2. Każdy maraton ma oznaczony poziom, a gramatyka jest wyjaśniona po polsku.\nCzym jest klucz dostępu?|To osobisty kod z 12 znaków. Wpisz go na swoim koncie, a maraton się odblokuje.\nIle trwa jedna lekcja?|10–15 minut. Postępy zapisują się po każdej lekcji.\nCzy mogę podarować klucz?|Tak. Klucz nie jest przypisany do kupującego, dopóki nie zostanie aktywowany.'
};

function T(type, scene, q, options, answer, tip, extra) { var t = {type:type, scene:scene, q:q, options:options || [], answer:answer || 0, tip:tip || ''}; if (extra) for (var k in extra) t[k] = extra[k]; return t; }
var SEED_COURSES = [
  {slug:'harry-potter-1', title_pl:'Harry Potter i Kamień Filozoficzny', description_pl:'Przechodzisz historię razem z bohaterem: od dziwnego listu do finałowego zwycięstwa. Każda lekcja opiera się na jednej scenie i ćwiczy jeden temat gramatyczny.', title:'Гаррі Поттер і філософський камінь', kind:'film', level:'A2–B1', price:'49 zł', poster:'p1', published:true, description:'Проходиш історію разом з героєм: від дивного листа до фінальної перемоги. Кожен урок спирається на одну сцену і тренує одну тему граматики.'},
  {slug:'friends-s1', title_pl:'Przyjaciele. Sezon 1', description_pl:'Codzienny angielski, żarty i potoczne zwroty sześciorga przyjaciół z Nowego Jorku.', title:'Друзі. Сезон 1', kind:'series', level:'A2', price:'49 zł', poster:'p2', published:true, description:'Побутова англійська, жарти й розмовні фрази шести друзів у Нью-Йорку.'},
  {slug:'zootopia', title_pl:'Zwierzogród', description_pl:'Miasto zwierząt, historia detektywistyczna i proste, zrozumiałe słownictwo.', title:'Зоотрополіс', kind:'film', level:'A2', price:'49 zł', poster:'p3', published:true, description:'Місто тварин, детективна історія і проста зрозуміла лексика.'},
  {slug:'sherlock-s1', title_pl:'Sherlock. Sezon 1', description_pl:'Szybkie dialogi, dedukcja i brytyjski angielski na poziomie B2.', title:'Шерлок. Сезон 1', kind:'series', level:'B2', price:'59 zł', poster:'p7', published:true, description:'Швидкі діалоги, дедукція і британська англійська для рівня B2.'}
];
var SEED_HP_LESSONS = [
  {num:1, title_pl:'Zwykły dom, niezwykły chłopiec', scene_pl:'Chłopiec mieszka z ciotką, wujem i kuzynem; jego pokój jest pod schodami.', title:'Звичайний будинок, незвичайний хлопчик', grammar:'Present Simple', scene:'Хлопчик живе з тіткою, дядьком і кузеном; його кімната — під сходами.', tasks:[
    T('vocabulary','Кімната під сходами.','What does <b>stairs</b> mean?',['сходи','стіни','двері'],0,'Stairs — сходи.'),
    T('listening','Тітка дає хлопчику доручення.','Listen. What does she want Harry to do?',['clean the kitchen','cook breakfast','go to school'],1,'Cook breakfast — приготувати сніданок.',{say:'Harry, go and cook breakfast. Now!'}),
    T('grammar','Present Simple: he / she / it + -s.','Harry ____ with his aunt and uncle.',['live','lives','living'],1,'Після he/she/it додаємо -s: Harry lives.'),
    T('quiz','Питання за сюжетом.','Where does Harry sleep at the start of the story?',['in a big bedroom','under the stairs','at school'],1,'Under the stairs — під сходами.')]},
  {num:2, title_pl:'List, którego nie da się zatrzymać', scene_pl:'Przychodzą dziesiątki listów, wuj próbuje je ukryć.', title:'Лист, який не можна зупинити', grammar:'Past Simple', scene:'Приходять десятки листів, дядько намагається їх сховати.', tasks:[
    T('vocabulary','Лист з печаткою.','What is an <b>envelope</b>?',['конверт','марка','скриня'],0,'Envelope — конверт.'),
    T('subtitles','Дядько забирає лист.','Uncle Vernon ____ the letter and burned it.',['took','takes','take'],0,'Past Simple від take — took.'),
    T('quiz','Питання за сюжетом.','Where does the family go to escape the letters?',['to a small island','to London','to the zoo'],0,'To a small island — на маленький острів.')]},
  {num:3, title_pl:'Jesteś czarodziejem', scene_pl:'Olbrzym znajduje chłopca na wyspie i wyjawia mu prawdę.', title:'Ти чарівник', grammar:'to be', scene:'Велетень знаходить хлопчика на острові й розповідає правду.', tasks:[
    T('subtitles','Велетень розповідає хлопчику правду про нього.','You are a ____, Harry.',['wizard','teacher','student'],0,'Wizard — чарівник.'),
    T('listening','День народження в хатинці.','Listen. What does Hagrid bring for Harry?',['a book','a cake','a broom'],1,'A cake — торт.',{say:'Happy birthday, Harry! I brought you a cake.'}),
    T('grammar','to be: is / are / was / were.','His parents ____ wizards.',['was','were','is'],1,'Множина в минулому — were.'),
    T('speaking','Опиши героя.','Повтори вголос: <i>“Hagrid is tall and very kind.”</i>',[],0,'У повній версії система оцінює вимову.',{say:'Hagrid is tall and very kind.'})]},
  {num:4, title_pl:'Zakupy na magicznej ulicy', scene_pl:'Kupowanie szaty, książek, różdżki i sowy.', title:'Покупки на чарівній вулиці', grammar:'can / can\'t', scene:'Купівля мантії, книжок, палички та сови.', tasks:[
    T('vocabulary','Магазин паличок.','What is a <b>wand</b>?',['чарівна паличка','мантія','сова'],0,'Wand — чарівна паличка.'),
    T('grammar','can / can\'t.','Muggles ____ see the magic street.',['can','can\'t','are'],1,'Звичайні люди не бачать вулицю — can\'t.'),
    T('speaking','Рольова гра в магазині.','Повтори вголос: <i>“Can I try this one?”</i>',[],0,'Can I…? — ввічливе прохання.',{say:'Can I try this one?'})]},
  {num:5, title_pl:'Peron i pociąg', scene_pl:'Szukanie dziwnego peronu, poznanie przyjaciela w pociągu.', title:'Платформа і потяг', grammar:'Питання', scene:'Пошук дивної платформи, знайомство в потязі.', tasks:[
    T('listening','Знайомство в потязі.','Listen and choose what you hear.',['Is this seat free?','Is this street free?','Is this sweet free?'],0,'Seat — місце.',{say:'Is this seat free?'}),
    T('grammar','Порядок слів у питанні.','____ you like sweets?',['Do','Does','Are'],0,'З you — Do you…?'),
    T('quiz','Питання за сюжетом.','How do they get to the platform?',['through a wall','by car','by plane'],0,'Through a wall — крізь стіну.')]},
  {num:6, title_pl:'Tiara wybiera dom', scene_pl:'Ceremonia przydziału uczniów do domów.', title:'Капелюх обирає дім', grammar:'Прикметники', scene:'Церемонія розподілу учнів по гуртожитках.', tasks:[
    T('vocabulary','Характер.','What does <b>brave</b> mean?',['сміливий','розумний','добрий'],0,'Brave — сміливий.'),
    T('subtitles','Хлопчик хвилюється перед вибором.','Harry is ____ because he doesn\'t want the wrong house.',['nervous','bored','angry'],0,'Nervous — схвильований.'),
    T('grammar','Порівняння.','The Great Hall is ____ than the classroom.',['big','bigger','biggest'],1,'Порівняння: big → bigger.')]},
  {num:7, title_pl:'Pierwsza lekcja latania', scene_pl:'Lekcja na miotłach i pierwsza gra w powietrzu.', title:'Перший урок польотів', grammar:'Present Continuous', scene:'Урок на мітлах і перша гра в повітрі.', tasks:[
    T('grammar','Present Continuous.','Look! Harry ____ very fast.',['flies','is flying','fly'],1,'Дія зараз — is flying.'),
    T('listening','Учитель дає команду.','Listen. What must students say to the broom?',['up','go','fly'],0,'Up — вгору.',{say:'Hold your hand over the broom and say: up!'}),
    T('speaking','Коментатор матчу.','Повтори вголос: <i>“He is flying higher and higher!”</i>',[],0,'Тренуємо інтонацію.',{say:'He is flying higher and higher!'})]},
  {num:8, title_pl:'Finał: Twoja ulubiona scena', scene_pl:'Podziemne próby i finałowe spotkanie.', title:'Фінал: твоя улюблена сцена', grammar:'Повторення', scene:'Підземні випробування й фінальна зустріч.', tasks:[
    T('quiz','Питання за сюжетом.','What animal brings letters?',['an owl','a cat','a rat'],0,'An owl — сова.'),
    T('quiz','Питання за сюжетом.','What game do they play on the way to the stone?',['chess','cards','football'],0,'Chess — шахи.'),
    T('final','Фінальне завдання.','Describe your favourite scene and character in English (80–120 words). Use 3 verbs in Past Simple and can / can\'t.',[],0,'Відповідь збережеться в кабінеті.')]}
];

/* ================= DEMO backend (localStorage) ================= */
function DemoBackend() {
  var KEY = 'movielang_demo_db_v1', SKEY = 'movielang_demo_session';
  var mem = null;
  function load() {
    if (mem) return mem;
    try { mem = JSON.parse(localStorage.getItem(KEY) || 'null'); } catch (e) { mem = null; }
    if (!mem) mem = seed();
    return mem;
  }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(mem)); } catch (e) {} }
  function seed() {
    var db = {users:[], courses:[], lessons:[], keys:[], enrollments:[], progress:[], settings:JSON.parse(JSON.stringify(DEFAULT_SETTINGS))};
    var now = Date.now(), day = 86400000;
    db.users.push({id:'u_admin', email:'admin@movielang.demo', password:'admin123', name:'Адміністратор', role:'admin', created_at:new Date(now - 30*day).toISOString()});
    var students = [['olena@example.com','Олена К.',20],['andrii@example.com','Андрій М.',12],['maria@example.com','Марія С.',5],['ivan@example.com','Іван П.',2]];
    SEED_COURSES.forEach(function (c, i) { var cc = JSON.parse(JSON.stringify(c)); cc.id = 'c' + (i + 1); cc.created_at = new Date(now - 25*day).toISOString(); db.courses.push(cc); });
    SEED_HP_LESSONS.forEach(function (l) { var ll = JSON.parse(JSON.stringify(l)); ll.id = 'l' + l.num; ll.course_id = 'c1'; db.lessons.push(ll); });
    students.forEach(function (s, i) {
      var id = 'u_s' + i; db.users.push({id:id, email:s[0], password:'demo123', name:s[1], role:'student', created_at:new Date(now - s[2]*day).toISOString()});
      var code = genCode(); db.keys.push({code:code, course_id:'c1', created_at:new Date(now - s[2]*day).toISOString(), activated_by:id, activated_at:new Date(now - s[2]*day + 3600000).toISOString()});
      db.enrollments.push({user_id:id, course_id:'c1', created_at:new Date(now - s[2]*day).toISOString()});
      var done = [6,4,2,1][i];
      for (var n = 1; n <= done; n++) db.progress.push({user_id:id, lesson_id:'l' + n, score:[100,88,75,92,67,100][(n + i) % 6], completed_at:new Date(now - (s[2] - n)*day).toISOString()});
    });
    for (var k = 0; k < 3; k++) db.keys.push({code:genCode(), course_id:'c1', created_at:new Date(now - day).toISOString(), activated_by:null, activated_at:null});
    db.keys.push({code:'HPS1-7KQ4-WZ9M', course_id:'c1', created_at:new Date(now).toISOString(), activated_by:null, activated_at:null});
    mem = db; save(); return db;
  }
  function me() { var id; try { id = localStorage.getItem(SKEY); } catch (e) {} var u = load().users.filter(function (x) { return x.id === id; })[0]; return u ? {id:u.id, email:u.email, name:u.name, role:u.role} : null; }
  function setSession(id) { try { if (id) localStorage.setItem(SKEY, id); else localStorage.removeItem(SKEY); } catch (e) {} }
  function needAdmin() { var u = me(); if (!u || u.role !== 'admin') throw new Error(t('Потрібні права адміністратора')); }
  function P(v) { return Promise.resolve(v); }
  return {
    mode:'demo',
    getUser: function () { return P(me()); },
    signUp: function (email, pass, name) {
      var db = load(); email = email.trim().toLowerCase();
      if (db.users.some(function (u) { return u.email === email; })) return Promise.reject(new Error(t('Користувач з такою поштою вже існує')));
      var u = {id:uid(), email:email, password:pass, name:name || email.split('@')[0], role:'student', created_at:new Date().toISOString()};
      db.users.push(u); save(); setSession(u.id); return P(me());
    },
    signIn: function (email, pass) {
      var u = load().users.filter(function (x) { return x.email === email.trim().toLowerCase() && x.password === pass; })[0];
      if (!u) return Promise.reject(new Error(t('Невірна пошта або пароль')));
      setSession(u.id); return P(me());
    },
    signOut: function () { setSession(null); return P(true); },
    getSettings: function () { var s = load().settings; var o = {}; for (var k in DEFAULT_SETTINGS) o[k] = s[k] != null ? s[k] : DEFAULT_SETTINGS[k]; return P(o); },
    saveSettings: function (obj) { needAdmin(); var db = load(); for (var k in obj) db.settings[k] = obj[k]; save(); return P(true); },
    listCourses: function (all) { var db = load(); return P(db.courses.filter(function (c) { return all || c.published; }).map(function (c) { var o = JSON.parse(JSON.stringify(c)); o.lessons_count = db.lessons.filter(function (l) { return l.course_id === c.id; }).length; return o; })); },
    getCourse: function (id) { var c = load().courses.filter(function (x) { return x.id === id; })[0]; return P(c ? JSON.parse(JSON.stringify(c)) : null); },
    saveCourse: function (c) { needAdmin(); var db = load(); if (!c.id) { c.id = uid(); c.created_at = new Date().toISOString(); db.courses.push(c); } else { db.courses = db.courses.map(function (x) { return x.id === c.id ? Object.assign({}, x, c) : x; }); } save(); return P(c); },
    deleteCourse: function (id) { needAdmin(); var db = load(); db.courses = db.courses.filter(function (x) { return x.id !== id; }); db.lessons = db.lessons.filter(function (l) { return l.course_id !== id; }); save(); return P(true); },
    listLessons: function (courseId) { return P(load().lessons.filter(function (l) { return l.course_id === courseId; }).sort(function (a, b) { return a.num - b.num; }).map(function (l) { return JSON.parse(JSON.stringify(l)); })); },
    getLesson: function (id) { var l = load().lessons.filter(function (x) { return x.id === id; })[0]; return P(l ? JSON.parse(JSON.stringify(l)) : null); },
    saveLesson: function (l) { needAdmin(); var db = load(); if (!l.id) { l.id = uid(); db.lessons.push(l); } else { db.lessons = db.lessons.map(function (x) { return x.id === l.id ? l : x; }); } save(); return P(l); },
    deleteLesson: function (id) { needAdmin(); var db = load(); db.lessons = db.lessons.filter(function (x) { return x.id !== id; }); save(); return P(true); },
    myEnrollments: function () { var u = me(); if (!u) return P([]); return P(load().enrollments.filter(function (e) { return e.user_id === u.id; }).map(function (e) { return e.course_id; })); },
    activateKey: function (code) {
      var u = me(); if (!u) return Promise.reject(new Error(t('Увійдіть в акаунт')));
      var db = load(); code = code.trim().toUpperCase();
      var k = db.keys.filter(function (x) { return x.code === code; })[0];
      if (!k) return P({ok:false, msg:t('Такого ключа не знайдено. Перевір літери O та 0, I та 1.')});
      if (k.activated_by) return P({ok:false, msg:t('Цей ключ уже активовано.')});
      k.activated_by = u.id; k.activated_at = new Date().toISOString();
      var ids = k.course_id ? [k.course_id] : db.courses.map(function (c) { return c.id; });
      ids.forEach(function (cid) { if (!db.enrollments.some(function (e) { return e.user_id === u.id && e.course_id === cid; })) db.enrollments.push({user_id:u.id, course_id:cid, created_at:new Date().toISOString()}); });
      save(); return P({ok:true, course_id:k.course_id});
    },
    myProgress: function () { var u = me(); if (!u) return P([]); return P(load().progress.filter(function (p) { return p.user_id === u.id; })); },
    saveProgress: function (lessonId, score, answer) {
      var u = me(); if (!u) return P(false); var db = load();
      db.progress = db.progress.filter(function (p) { return !(p.user_id === u.id && p.lesson_id === lessonId); });
      db.progress.push({user_id:u.id, lesson_id:lessonId, score:score, answer:answer || null, completed_at:new Date().toISOString()}); save(); return P(true);
    },
    adminData: function () { needAdmin(); var db = load(); return P({users:db.users.map(function (u) { return {id:u.id, email:u.email, name:u.name, role:u.role, created_at:u.created_at}; }), keys:db.keys.slice(), enrollments:db.enrollments.slice(), progress:db.progress.slice()}); },
    createKeys: function (courseId, n) { needAdmin(); var db = load(), out = []; for (var i = 0; i < n; i++) { var k = {code:genCode(), course_id:courseId || null, created_at:new Date().toISOString(), activated_by:null, activated_at:null}; db.keys.push(k); out.push(k); } save(); return P(out); },
    deleteKey: function (code) { needAdmin(); var db = load(); db.keys = db.keys.filter(function (k) { return k.code !== code; }); save(); return P(true); },
    setRole: function (userId, role) { needAdmin(); var db = load(); db.users.forEach(function (u) { if (u.id === userId) u.role = role; }); save(); return P(true); },
    resetDemo: function () { try { localStorage.removeItem(KEY); localStorage.removeItem(SKEY); } catch (e) {} mem = null; load(); return P(true); }
  };
}

/* ================= Supabase backend ================= */
function SupabaseBackend(url, key) {
  var sb = window.supabase.createClient(url, key);
  var cachedUser;
  function ok(r) { if (r.error) throw new Error(r.error.message); return r.data; }
  function profile() {
    return sb.auth.getUser().then(function (r) {
      var u = r.data && r.data.user; if (!u) return null;
      return sb.from('profiles').select('*').eq('id', u.id).maybeSingle().then(function (p) {
        var pr = p.data || {};
        return {id:u.id, email:u.email, name:pr.name || (u.user_metadata && u.user_metadata.name) || u.email, role:pr.role || 'student'};
      });
    });
  }
  return {
    mode:'supabase',
    getUser: function () { return profile().then(function (u) { cachedUser = u; return u; }); },
    signUp: function (email, pass, name) {
      return sb.auth.signUp({email:email.trim(), password:pass, options:{data:{name:name, lang:LANG, theme:THEME}, emailRedirectTo: location.origin + '/#/confirmed'}}).then(function (r) {
        if (r.error) throw new Error(r.error.message);
        if (!r.data.session) return {pending:true};
        return profile();
      });
    },
    signIn: function (email, pass) { return sb.auth.signInWithPassword({email:email.trim(), password:pass}).then(function (r) {
      if (r.error) { var m = (r.error.message || '').toLowerCase();
        if (m.indexOf('not confirmed') > -1) throw new Error(t('Пошту не підтверджено. Відкрий лист від Supabase і натисни посилання, потім увійди.'));
        if (m.indexOf('invalid') > -1) throw new Error(t('Невірна пошта або пароль.'));
        throw new Error(t('Помилка входу: ') + r.error.message); }
      return profile(); }); },
    signOut: function () { return sb.auth.signOut(); },
    getSettings: function () { return sb.from('site_settings').select('*').then(function (r) { var o = {}; for (var k in DEFAULT_SETTINGS) o[k] = DEFAULT_SETTINGS[k]; (r.data || []).forEach(function (x) { o[x.key] = x.value; }); return o; }); },
    saveSettings: function (obj) { var rows = Object.keys(obj).map(function (k) { return {key:k, value:obj[k]}; }); return sb.from('site_settings').upsert(rows).then(ok); },
    listCourses: function (all) {
      var q = sb.from('courses').select('*, lessons(count)').order('created_at');
      if (!all) q = q.eq('published', true);
      return q.then(ok).then(function (rows) { return rows.map(function (c) { c.lessons_count = c.lessons && c.lessons[0] ? c.lessons[0].count : 0; delete c.lessons; return c; }); });
    },
    getCourse: function (id) { return sb.from('courses').select('*').eq('id', id).maybeSingle().then(ok); },
    saveCourse: function (c) { var row = {slug:c.slug, title:c.title, title_pl:c.title_pl || null, description_pl:c.description_pl || null, kind:c.kind, level:c.level, price:c.price, poster:c.poster, published:!!c.published, description:c.description}; if (c.id) row.id = c.id; return sb.from('courses').upsert(row).select().single().then(ok); },
    deleteCourse: function (id) { return sb.from('courses').delete().eq('id', id).then(ok); },
    listLessons: function (courseId) { return sb.from('lessons').select('*').eq('course_id', courseId).order('num').then(ok); },
    getLesson: function (id) { return sb.from('lessons').select('*').eq('id', id).maybeSingle().then(ok); },
    saveLesson: function (l) { var row = {course_id:l.course_id, num:l.num, title:l.title, title_pl:l.title_pl || null, scene_pl:l.scene_pl || null, grammar:l.grammar, scene:l.scene, tasks:l.tasks}; if (l.id) row.id = l.id; return sb.from('lessons').upsert(row).select().single().then(ok); },
    deleteLesson: function (id) { return sb.from('lessons').delete().eq('id', id).then(ok); },
    myEnrollments: function () { if (!cachedUser) return Promise.resolve([]); return sb.from('enrollments').select('course_id').eq('user_id', cachedUser.id).then(ok).then(function (r) { return r.map(function (x) { return x.course_id; }); }); },
    activateKey: function (code) { return sb.rpc('activate_key', {p_code:code.trim().toUpperCase()}).then(ok); },
    myProgress: function () { if (!cachedUser) return Promise.resolve([]); return sb.from('progress').select('*').eq('user_id', cachedUser.id).then(ok); },
    saveProgress: function (lessonId, score, answer) { if (!cachedUser) return Promise.resolve(false); return sb.from('progress').upsert({user_id:cachedUser.id, lesson_id:lessonId, score:score, answer:answer || null, completed_at:new Date().toISOString()}).then(ok); },
    adminData: function () {
      return Promise.all([sb.from('profiles').select('*').order('created_at'), sb.from('access_keys').select('*').order('created_at', {ascending:false}), sb.from('enrollments').select('*'), sb.from('progress').select('*')])
        .then(function (r) { r.forEach(ok); return {users:r[0].data, keys:r[1].data, enrollments:r[2].data, progress:r[3].data}; });
    },
    createKeys: function (courseId, n) { var rows = []; for (var i = 0; i < n; i++) rows.push({code:genCode(), course_id:courseId || null}); return sb.from('access_keys').insert(rows).select().then(ok); },
    deleteKey: function (code) { return sb.from('access_keys').delete().eq('code', code).then(ok); },
    setRole: function (userId, role) { return sb.from('profiles').update({role:role}).eq('id', userId).then(ok); }
  };
}

/* ================= init ================= */
var cfg = window.MOVIELANG_CONFIG || {};
var API = (cfg.SUPABASE_URL && cfg.SUPABASE_ANON_KEY && window.supabase) ? SupabaseBackend(cfg.SUPABASE_URL, cfg.SUPABASE_ANON_KEY) : DemoBackend();
if (API.mode === 'demo') document.getElementById('demoBar').hidden = false;
var USER = null, SETTINGS = DEFAULT_SETTINGS;

function renderNav() {
  var links = t('<a href="#/">Головна</a><a href="#/catalog">Каталог</a><a href="#/trial">Пробний урок</a><a href="#/pricing">Тарифи</a>');
  if (USER) links += t('<a href="#/cabinet">Кабінет</a>');
  if (USER && USER.role === 'admin') links += t('<a href="#/admin" style="color:var(--nav-admin)">Адмін</a>');
  document.getElementById('navlinks').innerHTML = links;
  var tg = '<div class="row" style="gap:6px"><button class="tgl' + (LANG === 'uk' ? ' on' : '') + '" type="button" data-lang="uk" aria-label="Українська">UA</button><button class="tgl' + (LANG === 'pl' ? ' on' : '') + '" type="button" data-lang="pl" aria-label="Polski">PL</button><button class="tgl" type="button" id="themeBtn" aria-label="' + (THEME === 'dark' ? t('Світла тема') : t('Темна тема')) + '">' + (THEME === 'dark' ? '☀' : '☾') + '</button></div>';
  document.getElementById('navuser').innerHTML = tg + (USER
    ? '<a class="userchip" href="#/cabinet" style="text-decoration:none"><span class="ava">' + esc((USER.name || '?')[0].toUpperCase()) + '</span><span class="muted" style="max-width:120px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">' + esc(USER.name) + t('</span></a><button class="btn btn-ghost btn-sm" type="button" id="logoutBtn">Вийти</button>')
    : t('<a class="btn btn-ghost btn-sm" href="#/login">Увійти</a><a class="btn btn-red btn-sm" href="#/register">Реєстрація</a>'));
  document.querySelectorAll('[data-lang]').forEach(function (b) { b.onclick = function () { setLang(b.dataset.lang); }; });
  document.getElementById('themeBtn').onclick = toggleTheme;
  var lb = document.getElementById('logoutBtn');
  if (lb) lb.onclick = function () { API.signOut().then(function () { USER = null; toast(t('Ви вийшли з акаунта')); location.hash = '#/'; renderNav(); route(); }); };
}

/* ================= views ================= */
function heroSvg() {
  return '<svg class="scene" viewBox="0 0 800 500" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><defs><radialGradient id="glow" cx="62%" cy="40%" r="45%"><stop offset="0" stop-color="#ffd27a" stop-opacity=".75"/><stop offset=".5" stop-color="#8b5cf6" stop-opacity=".25"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient><linearGradient id="floor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a1230"/><stop offset="1" stop-color="#050409"/></linearGradient></defs><rect width="800" height="500" fill="url(#floor)"/><rect width="800" height="500" fill="url(#glow)"/><rect x="90" y="70" width="150" height="190" rx="75" fill="#0c0a1a" stroke="#3a2f63" stroke-width="4"/><g transform="translate(470 150) rotate(-12)"><rect width="140" height="92" rx="6" fill="#efe2c4"/><path d="M0 6 L70 54 L140 6" fill="none" stroke="#c9b48a" stroke-width="3"/><circle cx="70" cy="56" r="15" fill="#b3202f"/></g><g fill="#ffe7a8"><circle cx="440" cy="120" r="2.5"/><circle cx="640" cy="110" r="2"/><circle cx="610" cy="280" r="2.5"/></g><g fill="#05040a"><circle cx="300" cy="250" r="44"/><path d="M210 500 C210 380 240 310 300 300 C360 310 392 380 392 500 Z"/></g></svg>';
}
function posterHtml(c, small) {
  var cls = POSTER_CLASSES.indexOf(c.poster) > -1 ? c.poster : 'p1';
  return '<div class="poster ' + cls + '"' + (small ? ' style="width:120px;flex:0 0 120px;padding:10px"' : '') + '><span class="perf l"></span><span class="perf r"></span>' +
    (small ? '' : '<span class="tag">' + (c.kind === 'series' ? t('СЕРІАЛ') : t('ФІЛЬМ')) + ' · ' + esc(c.level) + '</span>' + (c.lessons_count ? '' : t('<span class="tag new">СКОРО</span>'))) +
    '<div class="ptitle"' + (small ? ' style="font-size:14px"' : '') + '>' + esc(tr(c, 'title')) + '</div></div>';
}
function catalogGrid(courses) {
  if (!courses.length) return t('<div class="empty">Курсів поки немає. Адміністратор може додати їх в адмін-панелі.</div>');
  return '<div class="grid-films">' + courses.map(function (c) {
    return '<a class="film" href="#/course/' + esc(c.id) + '">' + posterHtml(c) + '<div class="film-meta"><span>' + (c.lessons_count || 0) + t(' уроків</span><b>') + esc(c.price) + '</b></div></a>';
  }).join('') + '</div>';
}
function pricingHtml() {
  var s = LS();
  return '<div class="prices">' + [1,2,3].map(function (i) {
    var best = i === 2;
    return '<div class="price' + (best ? ' best' : '') + '">' + (best ? t('<span class="ribbon">НАЙПОПУЛЯРНІШИЙ</span>') : '') +
      '<span class="eyebrow">' + esc(s['plan' + i + '_name']) + '</span><div class="amount">' + esc(s['plan' + i + '_price']) + '</div><p class="muted">&nbsp;</p><ul>' +
      String(s['plan' + i + '_text'] || '').split('\n').filter(Boolean).map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') +
      '</ul><a class="btn ' + (best ? 'btn-red' : 'btn-ghost') + t('" href="#/buy">Купити ключ</a></div>');
  }).join('') + '</div>';
}
function faqHtml() {
  return '<div class="faq">' + String(LS().faq || '').split('\n').filter(Boolean).map(function (line, i) {
    var p = line.split('|'); return '<details' + (i === 0 ? ' open' : '') + '><summary>' + esc(p[0]) + '</summary><p>' + esc(p.slice(1).join('|')) + '</p></details>';
  }).join('') + '</div>';
}

function viewHome() {
  return API.listCourses(false).then(function (courses) {
    var s = LS();
    $app.innerHTML =
      '<section class="hero"><div><div class="eyebrow">' + esc(s.hero_eyebrow) + '</div>' +
      '<h1 style="margin-top:18px"><span class="w">' + esc(s.hero_w1) + '</span><span class="w">' + esc(s.hero_w2) + '</span><span class="w">' + esc(s.hero_w3) + '</span></h1>' +
      '<div class="hero-sub">WATCH · UNDERSTAND · SPEAK</div><p class="lead">' + esc(s.hero_lead) + '</p>' +
      '<div class="hero-cta"><a class="btn btn-red" href="' + (USER ? '#/cabinet' : '#/register') + '"><span class="play"></span>' + (USER ? t('Мій кабінет') : t('Створити кабінет')) + t('</a><a class="btn btn-ghost" href="#/trial">Пробний урок безкоштовно</a></div>') +
      t('<div class="hero-meta"><div><b>15 хв</b>на день</div><div><b>') + courses.length + t('</b>марафонів</div><div><b>6 типів</b>завдань</div></div></div>') +
      '<div><div class="screen">' + heroSvg() + '<div class="tc"><i></i>REC · 00:14:32</div><div class="lvl">SUBTITLES CHALLENGE · A2</div><div class="sub">You are a <span class="gap">wizard</span>, Harry.</div><div class="progressbar"><i></i></div></div></div></section>' +
      t('<section><div class="sec-head"><div class="eyebrow">Як це працює</div><h2>Від квитка до першої розмови</h2></div><div class="steps">') +
      [[t('Купуєш ключ'),t('Обираєш фільм, пакет або підписку.')],[t('Активуєш'),t('Вводиш код у кабінеті.')],[t('Відкриваєш марафон'),t('Уроки за сценами фільму.')],[t('Виконуєш завдання'),t('Слова, аудіо, субтитри, граматика, говоріння.')],[t('Бачиш прогрес'),t('Статистика й бали в кабінеті.')]].map(function (x) { return '<div class="step"><h3>' + x[0] + '</h3><p>' + x[1] + '</p></div>'; }).join('') +
      '</div></section>' +
      t('<section><div class="sec-head"><div class="eyebrow">Каталог</div><h2>Фільми та серіали</h2></div>') + catalogGrid(courses) + '</section>' +
      t('<section id="pricing"><div class="sec-head"><div class="eyebrow">Тарифи</div><h2>Обери свій квиток</h2></div>') + pricingHtml() + '</section>' +
      t('<section><div class="sec-head"><div class="eyebrow">FAQ</div><h2>Питання та відповіді</h2></div>') + faqHtml() + '</section>';
  });
}
function viewCatalog() { return API.listCourses(false).then(function (c) { $app.innerHTML = t('<div class="page"><div class="sec-head"><div class="eyebrow">Каталог</div><h2>Фільми та серіали</h2></div>') + catalogGrid(c) + '</div>'; }); }
function viewPricing() { $app.innerHTML = t('<div class="page"><div class="sec-head"><div class="eyebrow">Тарифи</div><h2>Обери свій квиток</h2></div>') + pricingHtml() + t('<div class="sec-head" style="margin-top:30px"><h2>Питання та відповіді</h2></div>') + faqHtml() + '</div>'; return Promise.resolve(); }
function viewBuy() {
  $app.innerHTML = t('<div class="page"><div class="sec-head"><div class="eyebrow">Купівля ключа</div><h2>Як отримати ключ доступу</h2><p class="lead">') + esc(LS().buy_info) + '</p></div>' + pricingHtml() +
    t('<div class="panel" style="max-width:560px"><h3>Уже маєш ключ?</h3><p class="muted" style="margin-block:8px 14px">Активуй його в особистому кабінеті.</p><a class="btn btn-red" href="') + (USER ? '#/cabinet' : '#/register') + '">' + (USER ? t('Перейти до кабінету') : t('Створити кабінет')) + '</a></div></div>';
  return Promise.resolve();
}

function viewAuth(mode) {
  if (USER) { location.hash = '#/cabinet'; return Promise.resolve(); }
  var reg = mode === 'register';
  $app.innerHTML = '<div class="page"><div class="authbox panel"><div class="eyebrow">' + (reg ? t('Новий кабінет') : t('Вхід')) + '</div><h2 style="font-size:32px;margin-block:10px 20px">' + (reg ? t('Створи свій кабінет') : t('З поверненням!')) + '</h2>' +
    '<form class="form" id="authForm" novalidate>' +
    (reg ? t('<label class="fl" for="aName">Ім\'я<input class="inp-s" id="aName" autocomplete="name" required></label>') : '') +
    t('<label class="fl" for="aEmail">Пошта<input class="inp-s" id="aEmail" type="email" autocomplete="email" required></label>') +
    t('<label class="fl" for="aPass">Пароль') + (reg ? t(' (мінімум 6 символів)') : '') + '<input class="inp-s" id="aPass" type="password" autocomplete="' + (reg ? 'new-password' : 'current-password') + '" required></label>' +
    '<button class="btn btn-red" type="submit" style="justify-content:center">' + (reg ? t('Зареєструватися') : t('Увійти')) + '</button><div class="msg" id="aMsg" role="status"></div></form>' +
    '<p class="muted small" style="margin-top:14px">' + (reg ? t('Вже є акаунт? <a href="#/login">Увійти</a>') : t('Ще немає акаунта? <a href="#/register">Створити кабінет</a>')) + '</p>' +
    (API.mode === 'demo' && !reg ? t('<p class="hint" style="margin-top:10px">Демо: адмін admin@movielang.demo / admin123, учень olena@example.com / demo123</p>') : '') + '</div></div>';
  document.getElementById('authForm').onsubmit = function (e) {
    e.preventDefault();
    var email = document.getElementById('aEmail').value, pass = document.getElementById('aPass').value, msg = document.getElementById('aMsg');
    var name = reg ? document.getElementById('aName').value.trim() : '';
    if (!/^\S+@\S+\.\S+$/.test(email)) { msg.className = 'msg err'; msg.textContent = t('Введи коректну пошту, напр. name@gmail.com'); return; }
    if (pass.length < 6) { msg.className = 'msg err'; msg.textContent = t('Пароль має містити щонайменше 6 символів.'); return; }
    if (reg && !name) { msg.className = 'msg err'; msg.textContent = t('Вкажи своє ім\'я.'); return; }
    msg.className = 'msg'; msg.textContent = t('Зачекай…');
    (reg ? API.signUp(email, pass, name) : API.signIn(email, pass)).then(function (u) {
      if (u && u.pending) { msg.className = 'msg ok'; msg.textContent = t('Акаунт створено! Перевір пошту (і папку «Спам»), натисни посилання з листа, потім увійди.'); document.getElementById('authForm').querySelector('button[type=submit]').disabled = true; return; }
      USER = u; renderNav(); toast(reg ? t('Кабінет створено!') : t('Вхід виконано')); location.hash = u && u.role === 'admin' ? '#/admin' : '#/cabinet';
    }).catch(function (err) { msg.className = 'msg err'; msg.textContent = err.message; });
  };
  return Promise.resolve();
}

function requireUser() { if (!USER) { location.hash = '#/login'; toast(t('Спершу увійди в акаунт'), 'info'); return false; } return true; }

function viewCabinet() {
  if (!requireUser()) return Promise.resolve();
  return Promise.all([API.listCourses(true), API.myEnrollments(), API.myProgress()]).then(function (r) {
    var courses = r[0], enr = r[1], prog = r[2];
    var lessonPromises = enr.map(function (cid) { return API.listLessons(cid); });
    return Promise.all(lessonPromises).then(function (lessonLists) {
      var doneIds = {}; prog.forEach(function (p) { doneIds[p.lesson_id] = p; });
      var avg = prog.length ? Math.round(prog.reduce(function (a, p) { return a + (+p.score || 0); }, 0) / prog.length) : 0;
      var xp = prog.reduce(function (a, p) { return a + Math.round((+p.score || 0) / 10) * 10; }, 0);
      var days = {}; prog.forEach(function (p) { days[(p.completed_at || '').slice(0, 10)] = 1; });
      var allLessons = {}; lessonLists.forEach(function (ls) { ls.forEach(function (l) { allLessons[l.id] = l; }); });
      var my = enr.map(function (cid, i) { var c = courses.filter(function (x) { return x.id === cid; })[0]; if (!c) return ''; var ls = lessonLists[i], d = ls.filter(function (l) { return doneIds[l.id]; }).length, pct = ls.length ? Math.round(d / ls.length * 100) : 0;
        return '<a href="#/course/' + esc(c.id) + '" style="text-decoration:none" class="prog"><div class="top"><span>' + esc(tr(c, 'title')) + '</span><b>' + d + ' / ' + ls.length + '</b></div><div class="bar"><i style="width:' + pct + '%;background:' + (pct === 100 ? 'var(--ok)' : 'linear-gradient(90deg,var(--progress-1),var(--progress-2))') + '"></i></div></a>'; }).join('');
      var recent = prog.slice().sort(function (a, b) { return (b.completed_at || '').localeCompare(a.completed_at || ''); }).slice(0, 6).map(function (p) { var l = allLessons[p.lesson_id]; return '<div><span>' + esc(l ? l.num + '. ' + tr(l, 'title') : t('Урок')) + '</span><b class="score">' + esc(p.score) + '%</b></div>'; }).join('');
      var medals = [[prog.length >= 1, '1', t('Перший урок')], [prog.length >= 5, '5', t('П\'ять уроків')], [Object.keys(days).length >= 3, '3🔥', t('Три дні навчання')], [avg >= 90 && prog.length > 0, '★', t('Точність 90%+')], [enr.length >= 2, '2', t('Два марафони')], [lessonLists.some(function (ls) { return ls.length && ls.every(function (l) { return doneIds[l.id]; }); }), '🏁', t('Марафон пройдено')]];
      $app.innerHTML = t('<div class="page"><div class="sec-head"><div class="eyebrow">Особистий кабінет</div><h2>Привіт, ') + esc(USER.name) + '!</h2></div>' +
        '<div class="dash"><aside class="dside"><div class="user"><div class="ava">' + esc(USER.name[0].toUpperCase()) + '</div><div><b>' + esc(USER.name) + '</b><small>' + esc(USER.email) + '</small></div></div>' +
        t('<form class="form" id="keyForm" novalidate><label class="fl" for="keyInput">Активувати ключ<input class="inp" id="keyInput" placeholder="XXXX-XXXX-XXXX" maxlength="14" autocomplete="off" style="font-size:15px;padding:11px 12px"></label><button class="btn btn-red btn-sm" type="submit" style="justify-content:center">Активувати</button><div class="msg small" id="keyMsg" role="status"></div>') +
        (API.mode === 'demo' ? t('<p class="hint">Демо-ключ: HPS1-7KQ4-WZ9M</p>') : '') + '</form>' +
        (USER.role === 'admin' ? t('<a class="btn btn-ghost btn-sm" href="#/admin" style="justify-content:center">Адмін-панель</a>') : '') + '</aside>' +
        '<div class="dmain"><div class="stats"><div class="stat"><b>' + prog.length + t('</b><span>уроків пройдено</span></div><div class="stat"><b>') + avg + t('%</b><span>середній бал</span></div><div class="stat"><b>') + xp + t('</b><span>XP набрано</span></div><div class="stat"><b>') + Object.keys(days).length + t('</b><span>днів навчання</span></div></div>') +
        t('<div class="rows"><div class="box"><h4>Мої марафони</h4>') + (my || t('<div class="empty small">Марафонів ще немає. Активуй ключ або <a href="#/trial">пройди пробний урок</a>.</div>')) + t('<a class="btn btn-ghost btn-sm" href="#/catalog" style="justify-self:start">Каталог курсів</a></div>') +
        t('<div class="box"><h4>Досягнення</h4><div class="ach">') + medals.map(function (m) { return '<div class="medal' + (m[0] ? '' : ' off') + '"><span class="m" style="border-color:' + (m[0] ? 'var(--gold)' : 'var(--dim)') + ';color:' + (m[0] ? 'var(--gold)' : 'var(--dim)') + '">' + m[1] + '</span>' + m[2] + '</div>'; }).join('') + '</div>' +
        t('<h4>Останні уроки</h4><div class="done-list">') + (recent || t('<span class="muted">Ще немає пройдених уроків</span>')) + '</div></div></div></div></div></div>';
      var inp = document.getElementById('keyInput'), msg = document.getElementById('keyMsg');
      inp.oninput = function () { var v = inp.value.toUpperCase().replace(/[^A-Z0-9]/g, '').slice(0, 12); inp.value = v.replace(/(.{4})(?=.)/g, '$1-'); };
      document.getElementById('keyForm').onsubmit = function (e) {
        e.preventDefault();
        if (inp.value.replace(/-/g, '').length !== 12) { msg.className = 'msg small err'; msg.textContent = t('Ключ має містити 12 символів.'); return; }
        API.activateKey(inp.value).then(function (res) {
          if (res.ok) { toast(t('Ключ активовано! Марафон відкрито.')); route(); } else { msg.className = 'msg small err'; msg.textContent = res.msg; }
        }).catch(function (err) { msg.className = 'msg small err'; msg.textContent = err.message; });
      };
    });
  });
}

function viewCourse(id) {
  return Promise.all([API.getCourse(id), API.listLessons(id), API.myEnrollments(), API.myProgress()]).then(function (r) {
    var c = r[0], ls = r[1], enrolled = r[2].indexOf(id) > -1 || (USER && USER.role === 'admin'), done = {};
    if (!c) { $app.innerHTML = t('<div class="page"><div class="empty">Курс не знайдено. <a href="#/catalog">До каталогу</a></div></div>'); return; }
    r[3].forEach(function (p) { done[p.lesson_id] = p; });
    var types = {}; ls.forEach(function (l) { (l.tasks || []).forEach(function (t) { types[t.type] = 1; }); });
    $app.innerHTML = '<div class="page"><div class="mcard"><div class="panel"><div class="mhead">' + posterHtml(c, true) + '<div class="mhead-info"><div class="badges"><span class="badge hot">' + esc(c.level) + '</span><span class="badge">' + ls.length + t(' уроків</span><span class="badge">') + (c.kind === 'series' ? t('серіал') : t('фільм')) + '</span>' + (enrolled ? t('<span class="badge" style="color:var(--ok)">доступ відкрито</span>') : '') + '</div>' +
      '<h2 style="font-size:clamp(24px,3.4vw,36px)">' + esc(tr(c, 'title')) + '</h2><p class="muted">' + esc(tr(c, 'description')) + '</p>' +
      (enrolled ? '' : t('<div class="row"><a class="btn btn-red" href="#/buy">Купити ключ · ') + esc(c.price) + '</a>' + (USER ? t('<a class="btn btn-ghost" href="#/cabinet">Активувати ключ</a>') : t('<a class="btn btn-ghost" href="#/register">Створити кабінет</a>')) + '</div>') + '</div></div>' +
      (ls.length ? '<ul class="lessons">' + ls.map(function (l, i) {
        var open = enrolled || i === 0, isDone = done[l.id];
        var inner = '<li class="' + (isDone ? 'done' : '') + '"><span class="lnum">' + (isDone ? '✓ ' : '') + String(l.num).padStart(2, '0') + '</span><span class="ltitle">' + esc(tr(l, 'title')) + '<small>' + esc(l.grammar) + (i === 0 && !enrolled ? t(' · безкоштовно') : '') + '</small></span>' + (open ? (isDone ? '<b class="score">' + isDone.score + '%</b>' : '<span class="lock" style="color:var(--neon)">▶</span>') : '<span class="lock">🔒</span>') + '</li>';
        return open ? '<a class="lesson-link" href="#/lesson/' + esc(l.id) + '">' + inner + '</a>' : inner;
      }).join('') + '</ul>' : t('<div class="empty" style="margin-top:20px">Уроки цього марафону скоро з\'являться.</div>')) +
      t('</div><div class="panel"><h3 style="margin-bottom:18px">Типи завдань у курсі</h3><div class="task-types">') + Object.keys(types).map(function (t) { return '<div class="ttype"><span class="k q">' + esc(t.slice(0, 2).toUpperCase()) + '</span><div><b>' + esc(TASK_TYPES[t] || t) + '</b></div></div>'; }).join('') + '</div></div></div></div>';
  });
}

/* ---------- lesson player ---------- */
function runPlayer(container, lesson, onFinish) {
  var tasks = lesson.tasks || [], cur = 0, res = [], finalText = '';
  container.innerHTML = '<div class="trial"><div class="tcard" id="tcard" aria-live="polite"></div><div class="tside" id="tside"></div></div>';
  var card = container.querySelector('#tcard'), side = container.querySelector('#tside');
  function renderSide() { side.innerHTML = tasks.map(function (t, i) { var c = i === cur ? 'on' : ''; if (res[i] === true) c += ' ok'; if (res[i] === false) c += ' bad'; return '<div class="tstep ' + c + '"><i>' + (i + 1) + '</i>' + esc(TASK_TYPES[t.type] || t.type) + '</div>'; }).join(''); }
  function qHtml(t) { return esc(t.q).replace(/&lt;(\/?)(b|i)&gt;/g, '<$1$2>').replace(/_{3,}/g, '<span class="gap">____</span>'); }
  function render() {
    var t = tasks[cur]; renderSide();
    var h = '<div class="ttop"><span class="ttag">' + esc(TASK_TYPES[t.type] || t.type) + t('</span><span class="tcount">Завдання ') + (cur + 1) + t(' з ') + tasks.length + '</span></div>' + (t.scene ? t('<div class="tscene"><b>Сцена:</b> ') + esc(t.scene) + '</div>' : '') + '<div class="tq">' + qHtml(t) + '</div>';
    if (t.say) h += t('<div><button class="speak" type="button" id="tsay"><span class="play"></span>Прослухати</button></div>');
    if (t.type === 'final') h += t('<textarea class="inp-s" id="tfinal" rows="6" placeholder="My favourite scene is…"></textarea><div class="row"><button class="btn btn-red" type="button" id="tsubmit">Зберегти відповідь</button><span class="hint" id="wc">0 слів</span></div>');
    else if (t.type === 'speaking' || !(t.options && t.options.length)) h += t('<div class="topts"><button class="topt" type="button" data-s="1">✓ Я повторив(ла)</button><button class="topt" type="button" data-s="0">Пропустити</button></div>');
    else h += '<div class="topts">' + t.options.map(function (o, i) { return '<button class="topt" type="button" data-i="' + i + '">' + esc(o) + '</button>'; }).join('') + '</div>';
    h += t('<div class="tfb" id="tfb"></div><div class="tnav"><span class="hint">Підказки українською, завдання англійською</span><button class="btn btn-red" type="button" id="tnext" hidden>Далі</button></div>');
    card.innerHTML = h;
    var sb = card.querySelector('#tsay'); if (sb) sb.onclick = function () { say(t.say); };
    card.querySelectorAll('.topt').forEach(function (b) { b.onclick = function () { answer(b); }; });
    var ta = card.querySelector('#tfinal');
    if (ta) { ta.oninput = function () { card.querySelector('#wc').textContent = (ta.value.trim().split(/\s+/).filter(Boolean).length) + t(' слів'); };
      card.querySelector('#tsubmit').onclick = function () { var n = ta.value.trim().split(/\s+/).filter(Boolean).length; if (n < 20) { var fb = card.querySelector('#tfb'); fb.className = 'tfb err'; fb.textContent = t('Напиши хоча б 20 слів (зараз ') + n + ').'; return; } finalText = ta.value.trim(); done(true, t('Відповідь збережено! ') + (t.tip || '')); }; }
  }
  function done(ok, text) {
    res[cur] = ok; var fb = card.querySelector('#tfb'); fb.className = 'tfb ' + (ok ? 'ok' : 'err'); fb.textContent = text;
    card.querySelectorAll('.topt,#tsubmit').forEach(function (x) { x.disabled = true; });
    renderSide(); var n = card.querySelector('#tnext'); n.hidden = false; n.textContent = cur < tasks.length - 1 ? t('Далі') : t('Показати результат'); n.onclick = next; n.focus();
  }
  function answer(b) {
    var t = tasks[cur], ok;
    if (b.dataset.s != null) ok = b.dataset.s === '1';
    else { ok = +b.dataset.i === +t.answer; card.querySelectorAll('.topt').forEach(function (x) { if (+x.dataset.i === +t.answer) x.classList.add('right'); }); if (!ok) b.classList.add('wrong'); var g = card.querySelector('.gap'); if (g) g.textContent = t.options[t.answer]; }
    done(ok, (ok ? t('Правильно! ') : t('Майже. ')) + (t.tip || ''));
  }
  function next() { if (cur < tasks.length - 1) { cur++; render(); } else finish(); }
  function finish() {
    var sc = res.filter(Boolean).length, pct = tasks.length ? Math.round(sc / tasks.length * 100) : 0; cur = tasks.length; renderSide();
    card.innerHTML = t('<div class="tres"><span class="ttag">РЕЗУЛЬТАТ</span><div class="big">') + sc + ' / ' + tasks.length + t('</div><p class="lead" style="text-align:center" id="tresText">Бал: ') + pct + '%</p><div class="row" style="justify-content:center" id="tresBtns"></div></div>';
    onFinish(pct, finalText, card.querySelector('#tresText'), card.querySelector('#tresBtns'), function () { cur = 0; res = []; render(); });
  }
  if (!tasks.length) { card.innerHTML = t('<div class="empty">У цьому уроці ще немає завдань.</div>'); return; }
  render();
}

function viewLesson(id) {
  return API.getLesson(id).then(function (l) {
    if (!l) { $app.innerHTML = t('<div class="page"><div class="empty">Урок не знайдено.</div></div>'); return; }
    return Promise.all([API.getCourse(l.course_id), API.listLessons(l.course_id), API.myEnrollments()]).then(function (r) {
      var c = r[0], ls = r[1], enrolled = r[2].indexOf(l.course_id) > -1 || (USER && USER.role === 'admin');
      var isFirst = ls.length && ls[0].id === l.id, idx = ls.map(function (x) { return x.id; }).indexOf(l.id), nextL = ls[idx + 1];
      if (!enrolled && !isFirst) { $app.innerHTML = t('<div class="page"><div class="empty">Цей урок відкривається після активації ключа. <a href="#/course/') + esc(l.course_id) + t('">До марафону</a></div></div>'); return; }
      $app.innerHTML = '<div class="page"><div class="sec-head"><a href="#/course/' + esc(l.course_id) + '" class="muted small">← ' + esc(c ? tr(c, 'title') : t('Марафон')) + t('</a><div class="eyebrow">Урок ') + l.num + ' · ' + esc(l.grammar) + '</div><h2>' + esc(tr(l, 'title')) + '</h2><p class="lead">' + esc(tr(l, 'scene')) + '</p></div><div id="player"></div></div>';
      runPlayer(document.getElementById('player'), l, function (pct, finalText, textEl, btns, again) {
        if (USER) { API.saveProgress(l.id, pct, finalText).then(function () { textEl.textContent = t('Бал: ') + pct + t('%. Результат збережено в кабінеті.'); }); }
        else textEl.textContent = t('Бал: ') + pct + t('%. Створи кабінет, щоб зберігати прогрес.');
        btns.innerHTML = (nextL && enrolled ? '<a class="btn btn-red" href="#/lesson/' + esc(nextL.id) + t('">Наступний урок</a>') : (!enrolled ? t('<a class="btn btn-red" href="#/buy">Отримати ключ доступу</a>') : '')) + '<a class="btn btn-ghost" href="' + (USER ? '#/cabinet' : '#/register') + '">' + (USER ? t('Мій кабінет') : t('Створити кабінет')) + t('</a><button class="btn btn-ghost" type="button" id="again">Пройти ще раз</button>');
        btns.querySelector('#again').onclick = again;
      });
    });
  });
}

function viewTrial() {
  return API.listCourses(false).then(function (cs) {
    var c = cs.filter(function (x) { return x.lessons_count; })[0];
    if (!c) { $app.innerHTML = t('<div class="page"><div class="empty">Пробний урок з\'явиться, щойно буде створено перший курс.</div></div>'); return; }
    return API.listLessons(c.id).then(function (ls) { location.replace('#/lesson/' + ls[0].id); });
  });
}

/* ================= ADMIN ================= */
var adminTab = 'stats';
function viewAdmin() {
  if (!requireUser()) return Promise.resolve();
  if (USER.role !== 'admin') { $app.innerHTML = t('<div class="page"><div class="empty">Ця сторінка доступна лише адміністратору.</div></div>'); return Promise.resolve(); }
  $app.innerHTML = t('<div class="page"><div class="sec-head"><div class="eyebrow">Адмін-панель</div><h2>Керування MovieLang</h2></div><div class="tabs" role="tablist">') +
    [['stats',t('Статистика')],['users',t('Користувачі')],['courses',t('Курси й уроки')],['keys',t('Ключі доступу')],['site',t('Тексти сайту')],['look',t('Вигляд і кольори')]].map(function (t) { return '<button class="tab' + (adminTab === t[0] ? ' on' : '') + '" type="button" role="tab" data-t="' + t[0] + '">' + t[1] + '</button>'; }).join('') +
    t('</div><div id="adminBody"><p class="muted">Завантаження…</p></div></div>');
  $app.querySelectorAll('.tab').forEach(function (b) { b.onclick = function () { adminTab = b.dataset.t; viewAdmin(); }; });
  var body = document.getElementById('adminBody');
  var f = {stats:adminStats, users:adminUsers, courses:adminCourses, keys:adminKeys, site:adminSite, look:adminLook}[adminTab];
  return f(body).catch(function (e) { body.innerHTML = t('<div class="empty">Помилка: ') + esc(e.message) + '</div>'; });
}

function adminStats(body) {
  return Promise.all([API.adminData(), API.listCourses(true)]).then(function (r) {
    var d = r[0], cs = r[1], now = Date.now(), wk = 7 * 86400000;
    var students = d.users.filter(function (u) { return u.role !== 'admin'; });
    var newWeek = d.users.filter(function (u) { return now - new Date(u.created_at) < wk; }).length;
    var activated = d.keys.filter(function (k) { return k.activated_by; }).length;
    var avg = d.progress.length ? Math.round(d.progress.reduce(function (a, p) { return a + (+p.score || 0); }, 0) / d.progress.length) : 0;
    var activeWeek = {}; d.progress.forEach(function (p) { if (now - new Date(p.completed_at) < wk) activeWeek[p.user_id] = 1; });
    var perCourse = cs.map(function (c) { return {t:tr(c, 'title'), n:d.enrollments.filter(function (e) { return e.course_id === c.id; }).length}; });
    var maxC = Math.max.apply(null, perCourse.map(function (x) { return x.n; }).concat([1]));
    var daysArr = []; for (var i = 13; i >= 0; i--) { var day = new Date(now - i * 86400000).toISOString().slice(0, 10); daysArr.push({d:day, n:d.progress.filter(function (p) { return (p.completed_at || '').slice(0, 10) === day; }).length}); }
    var maxD = Math.max.apply(null, daysArr.map(function (x) { return x.n; }).concat([1]));
    body.innerHTML = '<div style="display:grid;gap:18px"><div class="stats">' +
      '<div class="stat"><b>' + students.length + t('</b><span>учнів усього</span></div><div class="stat"><b>') + newWeek + t('</b><span>нових за 7 днів</span></div>') +
      '<div class="stat"><b>' + Object.keys(activeWeek).length + t('</b><span>активних за 7 днів</span></div><div class="stat"><b>') + activated + ' / ' + d.keys.length + t('</b><span>ключів активовано</span></div></div>') +
      '<div class="stats"><div class="stat"><b>' + d.progress.length + t('</b><span>уроків пройдено</span></div><div class="stat"><b>') + avg + t('%</b><span>середній бал</span></div><div class="stat"><b>') + cs.length + t('</b><span>курсів</span></div><div class="stat"><b>') + d.enrollments.length + t('</b><span>записів на курси</span></div></div>') +
      t('<div class="rows"><div class="box"><h4>Пройдені уроки за 14 днів</h4><div class="week" style="grid-template-columns:repeat(14,1fr);height:140px">') +
      daysArr.map(function (x, i) { return '<div title="' + x.d + ': ' + x.n + '"><span style="color:var(--muted)">' + (x.n || '') + '</span><i style="height:' + Math.max(3, Math.round(x.n / maxD * 90)) + 'px"' + (i === 13 ? ' class="today"' : '') + '></i>' + x.d.slice(8) + '</div>'; }).join('') +
      t('</div></div><div class="box"><h4>Учні за курсами</h4><div class="bars">') + perCourse.map(function (x) { return '<div class="b"><span>' + esc(x.t) + '</span><div class="t"><i style="width:' + Math.round(x.n / maxC * 100) + '%"></i></div><b>' + x.n + '</b></div>'; }).join('') + '</div></div></div>' +
      (API.mode === 'demo' ? t('<div><button class="btn btn-danger btn-sm" type="button" id="resetDemo">Скинути демо-дані</button></div>') : '') + '</div>';
    var rd = document.getElementById('resetDemo');
    if (rd) rd.onclick = function () { if (rd.dataset.c) { API.resetDemo().then(function () { USER = null; renderNav(); location.hash = '#/login'; toast(t('Демо-дані скинуто')); }); } else { rd.dataset.c = 1; rd.textContent = t('Точно скинути? Натисни ще раз'); } };
  });
}

function adminUsers(body) {
  return API.adminData().then(function (d) {
    var rows = d.users.map(function (u) {
      var pr = d.progress.filter(function (p) { return p.user_id === u.id; }), enr = d.enrollments.filter(function (e) { return e.user_id === u.id; }).length;
      var avg = pr.length ? Math.round(pr.reduce(function (a, p) { return a + (+p.score || 0); }, 0) / pr.length) : 0;
      var last = pr.map(function (p) { return p.completed_at; }).sort().pop();
      return '<tr><td><b>' + esc(u.name || '—') + '</b><br><span class="muted small">' + esc(u.email) + '</span></td><td><span class="pill' + (u.role === 'admin' ? ' admin' : '') + '">' + esc(u.role) + '</span></td><td>' + fmtDate(u.created_at) + '</td><td class="num">' + enr + '</td><td class="num">' + pr.length + '</td><td class="num">' + (pr.length ? avg + '%' : '—') + '</td><td>' + fmtDate(last) + '</td><td>' +
        (u.id === USER.id ? t('<span class="muted small">це ви</span>') : '<button class="btn btn-ghost btn-sm" type="button" data-role="' + esc(u.id) + '" data-to="' + (u.role === 'admin' ? 'student' : 'admin') + '">' + (u.role === 'admin' ? t('Зробити учнем') : t('Зробити адміном')) + '</button>') + '</td></tr>';
    }).join('');
    body.innerHTML = t('<p class="muted" style="margin-bottom:14px">Усього: ') + d.users.length + t('</p><div class="tbl-wrap"><table class="tbl"><thead><tr><th>Користувач</th><th>Роль</th><th>Реєстрація</th><th>Курсів</th><th>Уроків</th><th>Сер. бал</th><th>Активність</th><th></th></tr></thead><tbody>') + rows + '</tbody></table></div>';
    body.querySelectorAll('[data-role]').forEach(function (b) { b.onclick = function () { API.setRole(b.dataset.role, b.dataset.to).then(function () { toast(t('Роль змінено')); viewAdmin(); }).catch(function (e) { toast(e.message, 'err'); }); }; });
  });
}

function adminCourses(body) {
  return API.listCourses(true).then(function (cs) {
    body.innerHTML = t('<div class="row" style="justify-content:space-between;margin-bottom:14px"><span class="muted">Курсів: ') + cs.length + t('</span><button class="btn btn-red btn-sm" type="button" id="newCourse">+ Новий курс</button></div>') +
      (cs.length ? t('<div class="tbl-wrap"><table class="tbl"><thead><tr><th>Курс</th><th>Тип</th><th>Рівень</th><th>Уроків</th><th>Ціна</th><th>Статус</th><th></th></tr></thead><tbody>') + cs.map(function (c) {
        return '<tr><td><b>' + esc(tr(c, 'title')) + '</b></td><td>' + (c.kind === 'series' ? t('Серіал') : t('Фільм')) + '</td><td>' + esc(c.level) + '</td><td class="num">' + c.lessons_count + '</td><td>' + esc(c.price) + '</td><td><span class="pill ' + (c.published ? 'ok' : 'warn') + '">' + (c.published ? t('опубліковано') : t('чернетка')) + '</span></td><td><button class="btn btn-ghost btn-sm" type="button" data-edit="' + esc(c.id) + t('">Редагувати</button></td></tr>');
      }).join('') + '</tbody></table></div>' : t('<div class="empty">Курсів ще немає. <button class="btn btn-ghost btn-sm" type="button" id="importSeed">Додати демо-курс «Гаррі Поттер»</button></div>'));
    document.getElementById('newCourse').onclick = function () { courseEditor(body, null); };
    body.querySelectorAll('[data-edit]').forEach(function (b) { b.onclick = function () { courseEditor(body, b.dataset.edit); }; });
    var imp = document.getElementById('importSeed');
    if (imp) imp.onclick = function () {
      imp.disabled = true;
      var c = JSON.parse(JSON.stringify(SEED_COURSES[0]));
      API.saveCourse(c).then(function (saved) { return SEED_HP_LESSONS.reduce(function (p, l) { return p.then(function () { var ll = JSON.parse(JSON.stringify(l)); ll.course_id = saved.id; return API.saveLesson(ll); }); }, Promise.resolve()); })
        .then(function () { toast(t('Демо-курс додано')); viewAdmin(); }).catch(function (e) { toast(e.message, 'err'); imp.disabled = false; });
    };
  });
}

function courseEditor(body, id) {
  var p = id ? Promise.all([API.getCourse(id), API.listLessons(id)]) : Promise.resolve([{title:'', kind:'film', level:'A2', price:'49 zł', poster:'p1', published:false, description:'', slug:''}, []]);
  return p.then(function (r) {
    var c = r[0], ls = r[1];
    body.innerHTML = t('<div style="display:grid;gap:18px"><button class="btn btn-ghost btn-sm" type="button" id="back" style="justify-self:start">← Усі курси</button>') +
      '<form class="panel form" id="cForm" novalidate><h3>' + (id ? t('Редагування курсу') : t('Новий курс')) + '</h3>' +
      t('<label class="fl" for="cTitle">Назва<input class="inp-s" id="cTitle" value="') + esc(c.title) + '" required></label>' +
      '<label class="fl" for="cTitlePl">🇵🇱 Tytuł po polsku<input class="inp-s" id="cTitlePl" value="' + esc(c.title_pl) + '"></label>' +
      t('<div class="grid3"><label class="fl" for="cKind">Тип<select class="inp-s" id="cKind"><option value="film"') + (c.kind !== 'series' ? ' selected' : '') + t('>Фільм</option><option value="series"') + (c.kind === 'series' ? ' selected' : '') + t('>Серіал</option></select></label>') +
      t('<label class="fl" for="cLevel">Рівень<input class="inp-s" id="cLevel" value="') + esc(c.level) + t('"></label><label class="fl" for="cPrice">Ціна<input class="inp-s" id="cPrice" value="') + esc(c.price) + '"></label></div>' +
      t('<div class="grid2"><label class="fl" for="cPoster">Колір постера<select class="inp-s" id="cPoster">') + POSTER_CLASSES.map(function (pc, i) { return '<option value="' + pc + '"' + (c.poster === pc ? ' selected' : '') + '>' + [t('Фіолетовий'),t('Бордовий'),t('Синій'),t('Зелений'),t('Червоний'),t('Золотий'),t('Індиго'),t('Рожевий')][i] + '</option>'; }).join('') + '</select></label>' +
      t('<label class="fl" for="cPub">Статус<select class="inp-s" id="cPub"><option value="1"') + (c.published ? ' selected' : '') + t('>Опубліковано</option><option value="0"') + (!c.published ? ' selected' : '') + t('>Чернетка</option></select></label></div>') +
      t('<label class="fl" for="cDesc">Опис<textarea class="inp-s" id="cDesc">') + esc(c.description) + '</textarea></label>' +
      '<label class="fl" for="cDescPl">🇵🇱 Opis po polsku<textarea class="inp-s" id="cDescPl">' + esc(c.description_pl) + '</textarea></label>' +
      t('<div class="row"><button class="btn btn-red" type="submit">Зберегти курс</button>') + (id ? t('<button class="btn btn-danger btn-sm" type="button" id="delC">Видалити курс</button>') : '') + '</div><div class="msg" id="cMsg"></div></form>' +
      (id ? t('<div class="panel" style="display:grid;gap:14px"><div class="row" style="justify-content:space-between"><h3>Уроки (') + ls.length + t(')</h3><button class="btn btn-red btn-sm" type="button" id="newL">+ Новий урок</button></div>') +
        (ls.length ? '<ul class="lessons" style="margin:0">' + ls.map(function (l) { return '<li><span class="lnum">' + String(l.num).padStart(2, '0') + '</span><span class="ltitle">' + esc(tr(l, 'title')) + '<small>' + esc(l.grammar) + ' · ' + (l.tasks || []).length + t(' завдань</small></span><button class="btn btn-ghost btn-sm" type="button" data-l="') + esc(l.id) + t('">Редагувати</button></li>'); }).join('') + '</ul>' : t('<div class="empty">Додай перший урок.</div>')) + '</div>' : t('<p class="muted">Після збереження курсу можна буде додавати уроки.</p>')) + '</div>';
    document.getElementById('back').onclick = function () { viewAdmin(); };
    document.getElementById('cForm').onsubmit = function (e) {
      e.preventDefault();
      var title = document.getElementById('cTitle').value.trim(), msg = document.getElementById('cMsg');
      if (!title) { msg.className = 'msg err'; msg.textContent = t('Вкажи назву курсу.'); return; }
      var nc = {id:id || undefined, title:title, slug:c.slug || title.toLowerCase().replace(/[^a-z0-9а-яіїєґ]+/gi, '-').slice(0, 60), kind:document.getElementById('cKind').value, level:document.getElementById('cLevel').value, price:document.getElementById('cPrice').value, poster:document.getElementById('cPoster').value, published:document.getElementById('cPub').value === '1', description:document.getElementById('cDesc').value, title_pl:document.getElementById('cTitlePl').value.trim(), description_pl:document.getElementById('cDescPl').value};
      API.saveCourse(nc).then(function (s) { toast(t('Курс збережено')); courseEditor(body, s.id || id); }).catch(function (err) { msg.className = 'msg err'; msg.textContent = err.message; });
    };
    var dc = document.getElementById('delC');
    if (dc) dc.onclick = function () { if (!dc.dataset.c) { dc.dataset.c = 1; dc.textContent = t('Видалити разом з уроками? Натисни ще раз'); return; } API.deleteCourse(id).then(function () { toast(t('Курс видалено')); viewAdmin(); }); };
    var nl = document.getElementById('newL');
    if (nl) nl.onclick = function () { lessonEditor(body, id, null, ls.length + 1); };
    body.querySelectorAll('[data-l]').forEach(function (b) { b.onclick = function () { lessonEditor(body, id, b.dataset.l); }; });
  });
}

function lessonEditor(body, courseId, lessonId, nextNum) {
  var p = lessonId ? API.getLesson(lessonId) : Promise.resolve({course_id:courseId, num:nextNum, title:'', grammar:'', scene:'', tasks:[]});
  return p.then(function (l) {
    var tasks = JSON.parse(JSON.stringify(l.tasks || []));
    function taskHtml(t, i) {
      return '<div class="task-edit" data-i="' + i + t('"><div class="row" style="justify-content:space-between"><b>Завдання ') + (i + 1) + '</b><button class="btn btn-danger btn-sm" type="button" data-del="' + i + t('">Видалити</button></div>') +
        t('<div class="grid2"><label class="fl">Тип<select class="inp-s" data-f="type">') + Object.keys(TASK_TYPES).map(function (k) { return '<option value="' + k + '"' + (t.type === k ? ' selected' : '') + '>' + TASK_TYPES[k] + '</option>'; }).join('') + '</select></label>' +
        t('<label class="fl">Опис сцени<input class="inp-s" data-f="scene" value="') + esc(t.scene) + '"></label></div>' +
        t('<label class="fl">Питання / речення (пропуск позначай ____)<input class="inp-s" data-f="q" value="') + esc(t.q) + '"></label>' +
        t('<div class="grid2"><label class="fl">Варіанти через « / »<input class="inp-s" data-f="options" value="') + esc((t.options || []).join(' / ')) + '"></label>' +
        t('<label class="fl">Номер правильного варіанта (1, 2, 3…)<input class="inp-s" data-f="answer" type="number" min="1" value="') + ((+t.answer || 0) + 1) + '"></label></div>' +
        t('<div class="grid2"><label class="fl">Фраза для озвучення (необов\'язково)<input class="inp-s" data-f="say" value="') + esc(t.say) + '"></label>' +
        t('<label class="fl">Пояснення після відповіді<input class="inp-s" data-f="tip" value="') + esc(t.tip) + '"></label></div></div>';
    }
    function collect() {
      body.querySelectorAll('.task-edit').forEach(function (el) {
        var i = +el.dataset.i, t = tasks[i];
        el.querySelectorAll('[data-f]').forEach(function (f) { var k = f.dataset.f, v = f.value; if (k === 'options') t.options = v.split('/').map(function (x) { return x.trim(); }).filter(Boolean); else if (k === 'answer') t.answer = Math.max(0, (parseInt(v, 10) || 1) - 1); else if (k === 'say') { if (v.trim()) t.say = v.trim(); else delete t.say; } else t[k] = v; });
      });
    }
    function render() {
      body.innerHTML = t('<div style="display:grid;gap:18px"><button class="btn btn-ghost btn-sm" type="button" id="backC" style="justify-self:start">← До курсу</button>') +
        '<form class="panel form" id="lForm" novalidate><h3>' + (lessonId ? t('Редагування уроку') : t('Новий урок')) + '</h3>' +
        t('<div class="grid3"><label class="fl" for="lNum">Номер<input class="inp-s" id="lNum" type="number" min="1" value="') + esc(l.num) + t('"></label><label class="fl" for="lTitle" style="grid-column:span 2">Назва уроку<input class="inp-s" id="lTitle" value="') + esc(l.title) + '"></label></div>' +
        t('<div class="grid2"><label class="fl" for="lGr">Граматика / тема<input class="inp-s" id="lGr" value="') + esc(l.grammar) + t('"></label><label class="fl" for="lScene">Сцена (опис своїми словами)<input class="inp-s" id="lScene" value="') + esc(l.scene) + '"></label></div>' +
        '<div class="grid2"><label class="fl" for="lTitlePl">🇵🇱 Tytuł lekcji po polsku<input class="inp-s" id="lTitlePl" value="' + esc(l.title_pl) + '"></label><label class="fl" for="lScenePl">🇵🇱 Scena po polsku<input class="inp-s" id="lScenePl" value="' + esc(l.scene_pl) + '"></label></div>' +
        t('<h3 style="margin-top:8px">Завдання (') + tasks.length + ')</h3>' + tasks.map(taskHtml).join('') +
        t('<button class="btn btn-ghost btn-sm" type="button" id="addT" style="justify-self:start">+ Додати завдання</button>') +
        t('<div class="row"><button class="btn btn-red" type="submit">Зберегти урок</button>') + (lessonId ? '<a class="btn btn-ghost btn-sm" href="#/lesson/' + esc(lessonId) + t('">Переглянути як учень</a><button class="btn btn-danger btn-sm" type="button" id="delL">Видалити урок</button>') : '') + '</div><div class="msg" id="lMsg"></div></form></div>';
      document.getElementById('backC').onclick = function () { courseEditor(body, courseId); };
      document.getElementById('addT').onclick = function () { collect(); tasks.push({type:'quiz', scene:'', q:'', options:[], answer:0, tip:''}); render(); };
      body.querySelectorAll('[data-del]').forEach(function (b) { b.onclick = function () { collect(); tasks.splice(+b.dataset.del, 1); render(); }; });
      document.getElementById('lForm').onsubmit = function (e) {
        e.preventDefault(); collect();
        var msg = document.getElementById('lMsg'), title = document.getElementById('lTitle').value.trim();
        if (!title) { msg.className = 'msg err'; msg.textContent = t('Вкажи назву уроку.'); return; }
        var bad = tasks.filter(function (t) { return !t.q.trim(); }).length;
        if (bad) { msg.className = 'msg err'; msg.textContent = t('У ') + bad + t(' завданні(ях) порожнє питання.'); return; }
        var nl = {id:lessonId || undefined, course_id:courseId, num:parseInt(document.getElementById('lNum').value, 10) || 1, title:title, grammar:document.getElementById('lGr').value, scene:document.getElementById('lScene').value, title_pl:document.getElementById('lTitlePl').value.trim(), scene_pl:document.getElementById('lScenePl').value.trim(), tasks:tasks};
        API.saveLesson(nl).then(function () { toast(t('Урок збережено')); courseEditor(body, courseId); }).catch(function (err) { msg.className = 'msg err'; msg.textContent = err.message; });
      };
      var dl = document.getElementById('delL');
      if (dl) dl.onclick = function () { if (!dl.dataset.c) { dl.dataset.c = 1; dl.textContent = t('Точно видалити? Натисни ще раз'); return; } API.deleteLesson(lessonId).then(function () { toast(t('Урок видалено')); courseEditor(body, courseId); }); };
    }
    render();
  });
}

function adminKeys(body) {
  return Promise.all([API.adminData(), API.listCourses(true)]).then(function (r) {
    var d = r[0], cs = r[1], cname = {}, uname = {};
    cs.forEach(function (c) { cname[c.id] = c.title; }); d.users.forEach(function (u) { uname[u.id] = u.email; });
    var keys = d.keys.slice().sort(function (a, b) { return (b.created_at || '').localeCompare(a.created_at || ''); });
    body.innerHTML = t('<form class="panel form" id="kForm" novalidate style="margin-bottom:18px"><h3>Згенерувати ключі</h3><div class="grid3"><label class="fl" for="kCourse">Курс<select class="inp-s" id="kCourse"><option value="">Усі курси (підписка)</option>') + cs.map(function (c) { return '<option value="' + esc(c.id) + '">' + esc(tr(c, 'title')) + '</option>'; }).join('') + '</select></label>' +
      t('<label class="fl" for="kN">Кількість<input class="inp-s" id="kN" type="number" min="1" max="100" value="5"></label><div style="align-self:end"><button class="btn btn-red" type="submit">Створити</button></div></div><div id="kNew"></div></form>') +
      t('<div class="tbl-wrap"><table class="tbl"><thead><tr><th>Ключ</th><th>Курс</th><th>Створено</th><th>Статус</th><th></th></tr></thead><tbody>') + keys.map(function (k) {
        return '<tr><td style="font-family:var(--f-mono)">' + esc(k.code) + '</td><td>' + esc(k.course_id ? (cname[k.course_id] || '—') : t('Усі курси')) + '</td><td>' + fmtDate(k.created_at) + '</td><td>' + (k.activated_by ? t('<span class="pill ok">активовано</span><br><span class="muted small">') + esc(uname[k.activated_by] || '') + ', ' + fmtDate(k.activated_at) + '</span>' : t('<span class="pill warn">вільний</span>')) + '</td><td>' + (k.activated_by ? '' : '<button class="btn btn-ghost btn-sm" type="button" data-copy="' + esc(k.code) + t('">Копіювати</button> <button class="btn btn-danger btn-sm" type="button" data-kdel="') + esc(k.code) + t('">Видалити</button>')) + '</td></tr>';
      }).join('') + '</tbody></table></div>';
    document.getElementById('kForm').onsubmit = function (e) {
      e.preventDefault();
      var n = Math.min(100, Math.max(1, parseInt(document.getElementById('kN').value, 10) || 1));
      API.createKeys(document.getElementById('kCourse').value, n).then(function (ks) { toast(t('Створено ключів: ') + ks.length); viewAdmin().then(function () { var box = document.getElementById('kNew'); if (box) box.innerHTML = t('<p class="muted small" style="margin-top:10px">Нові ключі:</p><pre style="font-family:var(--f-mono);color:var(--neon);white-space:pre-wrap;user-select:all">') + ks.map(function (k) { return esc(k.code); }).join('\n') + '</pre>'; }); }).catch(function (err) { toast(err.message, 'err'); });
    };
    body.querySelectorAll('[data-copy]').forEach(function (b) { b.onclick = function () { var c = b.dataset.copy; (navigator.clipboard ? navigator.clipboard.writeText(c) : Promise.reject()).then(function () { toast(t('Скопійовано: ') + c); }).catch(function () { toast(t('Ключ: ') + c); }); }; });
    body.querySelectorAll('[data-kdel]').forEach(function (b) { b.onclick = function () { if (!b.dataset.c) { b.dataset.c = 1; b.textContent = t('Точно?'); return; } API.deleteKey(b.dataset.kdel).then(function () { toast(t('Ключ видалено')); viewAdmin(); }); }; });
  });
}


var PICK_RULES = [
  ['.logo-mark,.logo-mark span', ['logo-bg','logo-inner','logo-text']], ['.ava', ['avatar-bg','avatar-text']], ['.tgl.on', ['toggle-bg','toggle-text','toggle-border']],
  ['.btn-red', ['btn-bg','btn-text']], ['.btn-ghost', ['btn2-text','btn2-border','btn2-hover']],
  ['.navlinks a[href="#/admin"]', ['nav-admin']], ['.navlinks a', ['nav-link','nav-link-hover']],
  ['.hero h1 .w:nth-child(1)', ['hero-1']], ['.hero h1 .w:nth-child(2)', ['hero-2']], ['.hero h1 .w:nth-child(3)', ['hero-3']],
  ['.eyebrow', ['eyebrow','eyebrow-dot']], ['.price.best .ribbon', ['highlight']], ['.badge.hot', ['badge-level']],
  ['.bar', ['progress-1','progress-2']], ['.progressbar', ['progress-1','progress-2']], ['.week', ['chart-bar']], ['.bars', ['progress-1','progress-2']],
  ['.toast.ok,.msg.ok,.tfb.ok,.pill.ok,.score', ['success']], ['.toast.err,.msg.err,.tfb.err', ['error']],
  ['input,textarea,select', ['input-bg','input-border','text']], ['footer', ['footer-text','divider']],
  ['h1,h2,h3,h4', ['heading']], ['a', ['link']], ['.hint,.hero-sub,.lnum,.dim-t', ['text-3']],
  ['.lead,.muted,.step p,.price p,.film-meta,.ltitle small,.stat span,label,details p', ['text-2']],
  ['.box,.stat,.lessons li,.payopt,.topt,.tscene,.dside', ['panel-bg','text']],
  ['.panel,.step,.price,.rev,details,.tcard,.dash,.tstep', ['card-bg','border','text']],
  ['nav.top', ['nav-bg','divider']]
];
function pickTokens(el) {
  var out = [];
  for (var n = el; n && n.nodeType === 1 && out.length < 4; n = n.parentElement) {
    for (var i = 0; i < PICK_RULES.length; i++) { try { if (n.matches(PICK_RULES[i][0])) { PICK_RULES[i][1].forEach(function (k) { if (out.indexOf(k) < 0) out.push(k); }); break; } } catch (e) {} }
  }
  ['text','page-bg'].forEach(function (k) { if (out.indexOf(k) < 0) out.push(k); });
  return out.slice(0, 5);
}
function tokenLabel(k) { for (var i = 0; i < THEME_TOKENS.length; i++) if (THEME_TOKENS[i][0] === k) return t(THEME_TOKENS[i][1]); return k; }

function adminLook(body) {
  var saved = parseCustomTheme(SETTINGS.theme_custom);
  var work = JSON.parse(JSON.stringify(saved));
  var presets = [];
  try { presets = JSON.parse(SETTINGS.theme_presets || '[]'); } catch (e) {}
  while (presets.length < 3) presets.push(null);
  var mode = THEME, device = 'desk', ifr, open = {}, picking = false, picked = [];
  function hex(c) { var m = String(c).match(/\d+(\.\d+)?/g); if (!m || /^#/.test(c)) return c; return '#' + m.slice(0, 3).map(function (x) { return ('0' + (+x).toString(16)).slice(-2); }).join(''); }
  function effective(k) {
    if (work[mode] && work[mode][k]) return work[mode][k];
    try { var d = ifr.contentDocument.documentElement; return hex(getComputedStyle(d).getPropertyValue('--' + k).trim() || '#000000'); } catch (e) { return '#000000'; }
  }
  function pushPreview() {
    if (!ifr || !ifr.contentDocument) return;
    var d = ifr.contentDocument, st = d.getElementById('previewTheme');
    if (!st) { st = d.createElement('style'); st.id = 'previewTheme'; d.head.appendChild(st); }
    st.textContent = themeCss(work).replace(/:root/g, 'html:root');
    d.documentElement.setAttribute('data-theme', mode);
    ['display','body'].forEach(function (f) { var n = work.fonts[f]; if (n && !d.querySelector('link[data-font="' + n + '"]')) { var l = d.createElement('link'); l.rel = 'stylesheet'; l.dataset.font = n; l.href = 'https://fonts.googleapis.com/css2?family=' + encodeURIComponent(n).replace(/%20/g, '+') + ':wght@400;600;700&display=swap'; d.head.appendChild(l); } });
  }
  function refreshSwatches() { body.querySelectorAll('[data-k]').forEach(function (i) { var v = effective(i.dataset.k); if (i.type === 'color') i.value = v; else i.value = v; }); body.querySelectorAll('[data-reset]').forEach(function (r) { r.hidden = !(work[mode] && work[mode][r.dataset.reset]); }); }
  function swRow(tk) { var k = tk[0]; return '<div class="sw"><input type="color" id="c_' + k + '" data-k="' + k + '" aria-label="' + esc(t(tk[1])) + '"><label for="c_' + k + '">' + t(tk[1]) + '</label><input class="inp-s hex" data-k="' + k + '" data-hexin="1" maxlength="7" aria-label="HEX"><button class="tgl" type="button" data-reset="' + k + '" title="' + t('Скинути') + '" hidden>↺</button></div>'; }
  function presetHtml() {
    return '<div class="presets">' + presets.map(function (p, i) {
      return '<div class="preset"><input class="inp-s" data-pname="' + i + '" value="' + esc(p ? p.name : t('Шаблон') + ' ' + (i + 1)) + '" aria-label="name">' +
        '<div class="row" style="gap:6px"><button class="btn btn-ghost btn-sm" type="button" data-psave="' + i + '">' + t('Зберегти сюди') + '</button>' +
        (p ? '<button class="btn btn-ghost btn-sm" type="button" data-pload="' + i + '">' + t('Завантажити') + '</button>' : '<span class="muted small">' + t('порожній') + '</span>') + '</div></div>';
    }).join('') + '</div>';
  }
  function render() {
    body.innerHTML = '<div class="look"><div class="look-side panel">' +
      '<div class="row" style="justify-content:space-between"><h3>' + t('Кольори') + '</h3><div class="row" style="gap:6px"><button class="tgl' + (mode === 'dark' ? ' on' : '') + '" type="button" data-m="dark">☾ ' + t('Темна') + '</button><button class="tgl' + (mode === 'light' ? ' on' : '') + '" type="button" data-m="light">☀ ' + t('Світла') + '</button></div></div>' +
      '<p class="muted small">' + t('Кожен елемент має власний колір. ↺ повертає стандартний.') + '</p>' +
      '<div class="picked" id="picked"' + (picked.length ? '' : ' hidden') + '><span class="small muted">' + t('Вибраний елемент') + ':</span>' + picked.map(function (k) { return '<button class="tgl" type="button" data-jump="' + k + '">' + tokenLabel(k) + '</button>'; }).join('') + '</div>' +
      THEME_GROUPS.map(function (g, gi) { return '<details class="grp"' + (open[gi] || gi === 0 ? ' open' : '') + ' data-g="' + gi + '"><summary>' + t(g[0]) + '</summary><div class="swatches">' + g[1].map(swRow).join('') + '</div></details>'; }).join('') +
      '<details class="grp" data-g="f"' + (open.f ? ' open' : '') + '><summary>' + t('Шрифти') + '</summary><div class="grid2" style="padding-top:8px">' +
      '<label class="fl" for="fDisp">' + t('Заголовки') + '<select class="inp-s" id="fDisp">' + FONT_CHOICES.display.map(function (f) { return '<option' + ((work.fonts.display || 'Dela Gothic One') === f ? ' selected' : '') + '>' + f + '</option>'; }).join('') + '</select></label>' +
      '<label class="fl" for="fBody">' + t('Основний текст') + '<select class="inp-s" id="fBody">' + FONT_CHOICES.body.map(function (f) { return '<option' + ((work.fonts.body || 'Onest') === f ? ' selected' : '') + '>' + f + '</option>'; }).join('') + '</select></label></div></details>' +
      '<div class="row"><button class="btn btn-red" type="button" id="lookSave">' + t('Опублікувати на сайті') + '</button><button class="btn btn-ghost btn-sm" type="button" id="lookDefault">' + t('Зберегти як стандартний шаблон') + '</button><button class="btn btn-ghost btn-sm" type="button" id="lookCancel">' + t('Скасувати зміни') + '</button><button class="btn btn-ghost btn-sm" type="button" id="lookReset">' + t('Скинути до стандартних') + '</button></div>' +
      '<h3 style="margin-top:6px">' + t('Шаблони') + '</h3><p class="muted small">' + t('Збережи поточні кольори в один із 3 слотів, щоб потім швидко повернутися до них.') + '</p>' + presetHtml() + '</div>' +
      '<div class="look-prev"><div class="row" style="justify-content:space-between"><div class="row" style="gap:6px;flex-wrap:wrap" id="pvNav">' +
      [['#/',t('Головна')],['#/catalog',t('Каталог')],['course',t('Курс')],['lesson',t('Урок')],['#/pricing',t('Тарифи')],['#/login',t('Вхід')],['#/cabinet',t('Кабінет')]].map(function (x) { return '<button class="tgl" type="button" data-go="' + x[0] + '">' + x[1] + '</button>'; }).join('') +
      '</div><div class="row" style="gap:6px"><button class="tgl pick' + (picking ? ' on' : '') + '" type="button" id="pickBtn" title="' + t('Клікни елемент у перегляді, щоб змінити його колір') + '">🎯 ' + t('Вибрати елемент') + '</button><button class="tgl' + (device === 'desk' ? ' on' : '') + '" type="button" data-dev="desk">🖥</button><button class="tgl' + (device === 'mob' ? ' on' : '') + '" type="button" data-dev="mob">📱</button></div></div>' +
      '<div class="pv-frame ' + device + '"><iframe id="pvFrame" title="' + t('Попередній перегляд') + '" src="' + location.pathname + '?preview=1#/"></iframe></div>' +
      '<p class="hint">' + t('Це справжній сайт: клікай і переходь між сторінками. Зміни видно лише тут, поки не натиснеш «Опублікувати».') + '</p></div></div>';
    ifr = document.getElementById('pvFrame');
    ifr.onload = function () { attachPick(); pushPreview(); setTimeout(function () { pushPreview(); refreshSwatches(); }, 600); try { ifr.contentWindow.addEventListener('hashchange', function () { setTimeout(pushPreview, 50); }); } catch (e) {} };
    bind();
  }
  function attachPick() {
    var d; try { d = ifr.contentDocument; } catch (e) { return; } if (!d || d.__pickBound) return; d.__pickBound = true;
    var hl = d.createElement('style'); hl.textContent = '.__pickhover{outline:2px dashed #ff2d95!important;outline-offset:2px!important;cursor:crosshair!important}'; d.head.appendChild(hl);
    var last;
    d.addEventListener('mouseover', function (e) { if (!picking) return; if (last) last.classList.remove('__pickhover'); last = e.target; last.classList.add('__pickhover'); }, true);
    d.addEventListener('mouseout', function () { if (last) last.classList.remove('__pickhover'); }, true);
    d.addEventListener('click', function (e) {
      if (!picking) return; e.preventDefault(); e.stopPropagation();
      if (last) last.classList.remove('__pickhover');
      picked = pickTokens(e.target); renderPicked(); jumpTo(picked[0]);
    }, true);
  }
  function renderPicked() {
    var p = document.getElementById('picked'); if (!p) return;
    p.hidden = !picked.length;
    p.innerHTML = '<span class="small muted">' + t('Вибраний елемент') + ':</span>' + picked.map(function (k) { return '<button class="tgl" type="button" data-jump="' + k + '">' + tokenLabel(k) + '</button>'; }).join('');
    p.querySelectorAll('[data-jump]').forEach(function (b) { b.onclick = function () { jumpTo(b.dataset.jump); }; });
  }
  function jumpTo(k) {
    var inp = body.querySelector('input[type=color][data-k="' + k + '"]'); if (!inp) return;
    var det = inp.closest('details'); if (det && !det.open) { det.open = true; open[det.dataset.g] = true; }
    var row = inp.closest('.sw');
    body.querySelectorAll('.sw.flash').forEach(function (x) { x.classList.remove('flash'); });
    row.classList.add('flash'); row.scrollIntoView({behavior:'smooth', block:'center'});
    body.querySelectorAll('[data-jump]').forEach(function (b) { b.classList.toggle('on', b.dataset.jump === k); });
    setTimeout(function () { try { inp.focus({preventScroll:true}); if (inp.showPicker) inp.showPicker(); } catch (e) {} }, 350);
  }
  function setColor(k, v) { work[mode] = work[mode] || {}; work[mode][k] = v; body.querySelectorAll('[data-k="' + k + '"]').forEach(function (i) { if (i.value !== v) i.value = v; }); var r = body.querySelector('[data-reset="' + k + '"]'); if (r) r.hidden = false; pushPreview(); }
  function bind() {
    body.querySelectorAll('details.grp').forEach(function (d) { d.ontoggle = function () { open[d.dataset.g] = d.open; }; });
    body.querySelectorAll('[data-m]').forEach(function (b) { b.onclick = function () { mode = b.dataset.m; body.querySelectorAll('[data-m]').forEach(function (x) { x.classList.toggle('on', x === b); }); pushPreview(); setTimeout(refreshSwatches, 80); }; });
    body.querySelectorAll('input[type=color][data-k]').forEach(function (i) { i.oninput = function () { setColor(i.dataset.k, i.value); }; });
    body.querySelectorAll('[data-hexin]').forEach(function (i) { i.oninput = function () { var v = i.value.trim(); if (v[0] !== '#') v = '#' + v; if (/^#[0-9a-fA-F]{6}$/.test(v)) setColor(i.dataset.k, v.toLowerCase()); }; });
    body.querySelectorAll('[data-reset]').forEach(function (b) { b.onclick = function () { if (work[mode]) delete work[mode][b.dataset.reset]; pushPreview(); setTimeout(refreshSwatches, 50); }; });
    document.getElementById('pickBtn').onclick = function () { picking = !picking; this.classList.toggle('on', picking); toast(picking ? t('Режим вибору: клікни будь-який елемент у перегляді') : t('Режим вибору вимкнено'), 'info'); };
    body.querySelectorAll('[data-jump]').forEach(function (b) { b.onclick = function () { jumpTo(b.dataset.jump); }; });
    document.getElementById('lookDefault').onclick = function () {
      var b = this; if (!b.dataset.c) { b.dataset.c = 1; b.textContent = t('Точно? Натисни ще раз'); return; }
      var v = JSON.stringify(work);
      API.saveSettings({theme_default: v}).then(function () { SETTINGS.theme_default = v; b.textContent = t('Зберегти як стандартний шаблон'); delete b.dataset.c; toast(t('Збережено як стандартний шаблон. Кнопка «Скинути до стандартних» тепер повертає до нього.')); }).catch(function (e) { toast(e.message, 'err'); });
    };
    document.getElementById('fDisp').onchange = function () { work.fonts.display = this.value; pushPreview(); };
    document.getElementById('fBody').onchange = function () { work.fonts.body = this.value; pushPreview(); };
    body.querySelectorAll('[data-dev]').forEach(function (b) { b.onclick = function () { device = b.dataset.dev; body.querySelector('.pv-frame').className = 'pv-frame ' + device; body.querySelectorAll('[data-dev]').forEach(function (x) { x.classList.toggle('on', x === b); }); }; });
    body.querySelectorAll('[data-go]').forEach(function (b) { b.onclick = function () {
      var g = b.dataset.go;
      if (g === 'course' || g === 'lesson') { API.listCourses(false).then(function (cs) { var c = cs.filter(function (x) { return x.lessons_count; })[0] || cs[0]; if (!c) return; if (g === 'course') ifr.contentWindow.location.hash = '#/course/' + c.id; else API.listLessons(c.id).then(function (ls) { if (ls[0]) ifr.contentWindow.location.hash = '#/lesson/' + ls[0].id; }); }); }
      else ifr.contentWindow.location.hash = g;
    }; });
    document.getElementById('lookCancel').onclick = function () { work = JSON.parse(JSON.stringify(saved)); pushPreview(); setTimeout(refreshSwatches, 50); render(); toast(t('Зміни скасовано'), 'info'); };
    document.getElementById('lookReset').onclick = function () { var b = this; if (!b.dataset.c) { b.dataset.c = 1; b.textContent = t('Точно? Натисни ще раз'); return; } work = SETTINGS.theme_default ? parseCustomTheme(SETTINGS.theme_default) : {dark:{}, light:{}, fonts:{}}; render(); toast(t('Повернено стандартні значення. Натисни «Опублікувати», щоб застосувати.'), 'info'); };
    document.getElementById('lookSave').onclick = function () {
      var v = JSON.stringify(work);
      API.saveSettings({theme_custom: v}).then(function () { SETTINGS.theme_custom = v; saved = JSON.parse(v); applyCustomTheme(saved); toast(t('Вигляд сайту опубліковано')); }).catch(function (e) { toast(e.message, 'err'); });
    };
    body.querySelectorAll('[data-psave]').forEach(function (b) { b.onclick = function () {
      var i = +b.dataset.psave, name = body.querySelector('[data-pname="' + i + '"]').value.trim() || (t('Шаблон') + ' ' + (i + 1));
      if (presets[i] && !b.dataset.c) { b.dataset.c = 1; b.textContent = t('Перезаписати? Натисни ще раз'); return; }
      presets[i] = {name: name, data: JSON.parse(JSON.stringify(work))};
      var v = JSON.stringify(presets);
      API.saveSettings({theme_presets: v}).then(function () { SETTINGS.theme_presets = v; toast(t('Шаблон збережено') + ': ' + name); render(); }).catch(function (e) { toast(e.message, 'err'); });
    }; });
    body.querySelectorAll('[data-pload]').forEach(function (b) { b.onclick = function () {
      var p = presets[+b.dataset.pload]; if (!p) return;
      work = parseCustomTheme(p.data); render(); toast(t('Шаблон завантажено в редактор. Натисни «Опублікувати», щоб застосувати на сайті.'), 'info');
    }; });
  }
  render();
  return Promise.resolve();
}

function adminSite(body) {
  return API.getSettings().then(function (s) {
    var fields = [['hero_eyebrow',t('Надзаголовок головної'),'input'],['hero_w1',t('Заголовок, слово 1'),'input'],['hero_w2',t('Заголовок, слово 2'),'input'],['hero_w3',t('Заголовок, слово 3'),'input'],['hero_lead',t('Опис під заголовком'),'textarea'],
      ['plan1_name',t('Тариф 1: назва'),'input'],['plan1_price',t('Тариф 1: ціна'),'input'],['plan1_text',t('Тариф 1: пункти (кожен з нового рядка)'),'textarea'],
      ['plan2_name',t('Тариф 2: назва'),'input'],['plan2_price',t('Тариф 2: ціна'),'input'],['plan2_text',t('Тариф 2: пункти'),'textarea'],
      ['plan3_name',t('Тариф 3: назва'),'input'],['plan3_price',t('Тариф 3: ціна'),'input'],['plan3_text',t('Тариф 3: пункти'),'textarea'],
      ['buy_info',t('Як купити ключ (текст на сторінці покупки)'),'textarea'],['faq',t('FAQ: кожен рядок «Питання|Відповідь»'),'textarea']];
    fields = fields.concat(fields.map(function (f) { return [f[0] + '_pl', '🇵🇱 ' + f[1], f[2]]; }));
    body.innerHTML = t('<form class="panel form" id="sForm" novalidate><h3>Тексти на сайті</h3><p class="muted small">Зміни одразу з\'являться на головній, у тарифах і FAQ.</p>') +
      fields.map(function (f) { var id = 's_' + f[0]; return '<label class="fl" for="' + id + '">' + f[1] + (f[2] === 'textarea' ? '<textarea class="inp-s" id="' + id + '" rows="' + (f[0] === 'faq' ? 8 : 4) + '">' + esc(s[f[0]]) + '</textarea>' : '<input class="inp-s" id="' + id + '" value="' + esc(s[f[0]]) + '">') + '</label>'; }).join('') +
      t('<div class="row"><button class="btn btn-red" type="submit">Зберегти зміни</button><a class="btn btn-ghost btn-sm" href="#/">Переглянути сайт</a></div></form>');
    document.getElementById('sForm').onsubmit = function (e) {
      e.preventDefault(); var o = {};
      fields.forEach(function (f) { o[f[0]] = document.getElementById('s_' + f[0]).value; });
      API.saveSettings(o).then(function () { SETTINGS = Object.assign({}, SETTINGS, o); toast(t('Тексти сайту збережено')); }).catch(function (err) { toast(err.message, 'err'); });
    };
  });
}

/* ================= router ================= */
function route() {
  var h = location.hash.replace(/^#\/?/, ''), parts = h.split('/'), p;
  window.scrollTo(0, 0);
  switch (parts[0]) {
    case '': p = viewHome(); break;
    case 'catalog': p = viewCatalog(); break;
    case 'pricing': p = viewPricing(); break;
    case 'buy': p = viewBuy(); break;
    case 'trial': p = viewTrial(); break;
    case 'login': p = viewAuth('login'); break;
    case 'register': p = viewAuth('register'); break;
    case 'cabinet': p = viewCabinet(); break;
    case 'course': p = viewCourse(parts[1]); break;
    case 'lesson': p = viewLesson(parts[1]); break;
    case 'admin': p = viewAdmin(); break;
    default: $app.innerHTML = t('<div class="page"><div class="empty">Сторінку не знайдено. <a href="#/">На головну</a></div></div>'); p = Promise.resolve();
  }
  Promise.resolve(p).catch(function (e) { $app.innerHTML = t('<div class="page"><div class="empty">Помилка: ') + esc(e.message) + '</div></div>'; });
}
window.addEventListener('hashchange', route);
$app.innerHTML = t('<div class="page"><p class="muted">Завантаження…</p></div>');
applyStatic();
if (/[?&]preview=1/.test(location.search)) document.documentElement.classList.add('is-preview');
Promise.all([API.getUser().catch(function () { return null; }), API.getSettings().catch(function () { return DEFAULT_SETTINGS; })]).then(function (r) {
  USER = r[0]; SETTINGS = r[1]; applyCustomTheme();
  var h = location.hash;
  if (/access_token=|type=signup|#\/confirmed/.test(h)) { history.replaceState(null, '', location.pathname + (USER ? '#/cabinet' : '#/login')); toast(USER ? t('Пошту підтверджено! Ласкаво просимо до MovieLang.') : t('Пошту підтверджено! Тепер увійди.')); }
  else if (/error_description=/.test(h)) { history.replaceState(null, '', location.pathname + '#/login'); toast(t('Посилання недійсне або застаріле. Увійди або зареєструйся ще раз.'), 'err'); }
  renderNav(); route();
});
})();
