/* MoviLang — клієнтський застосунок.
   Два режими бекенду: Supabase (якщо заповнено config.js) або DEMO (localStorage). */
(function () {
'use strict';

/* ================= helpers ================= */
var $app = document.getElementById('app');
function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]; }); }
function toast(msg, type) { type = type || 'ok'; var t = document.createElement('div'); t.className = 'toast ' + type; t.setAttribute('role', 'status'); t.innerHTML = '<span class="ti">' + (type === 'ok' ? '✓' : type === 'err' ? '!' : 'i') + '</span><span></span>'; t.lastChild.textContent = msg; document.body.appendChild(t); setTimeout(function () { t.remove(); }, 3800); }
function uid() { return 'id' + Math.random().toString(36).slice(2, 10) + Date.now().toString(36); }
function fmtDate(d) { if (!d) return '—'; try { return new Date(d).toLocaleDateString(SPEECH[LANG], {day:'2-digit',month:'2-digit',year:'numeric'}); } catch (e) { return d; } }
function genCode() { var a = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789', s = ''; for (var i = 0; i < 12; i++) { s += a[Math.floor(Math.random() * a.length)]; if (i === 3 || i === 7) s += '-'; } return s; }
var VOICE_CACHE = {};
function bestVoice(lang) {
  if (VOICE_CACHE[lang]) return VOICE_CACHE[lang];
  var vs = (window.speechSynthesis && speechSynthesis.getVoices()) || [], pre = lang.slice(0, 2).toLowerCase();
  var c = vs.filter(function (v) { return (v.lang || '').replace('_', '-').toLowerCase().indexOf(pre) === 0; });
  if (!c.length) return null;
  function sc(v) { var n = v.name || '', s = 0; if (/natural|neural/i.test(n)) s += 10; if (/online/i.test(n)) s += 6; if (/premium|enhanced|siri/i.test(n)) s += 6; if (/google/i.test(n)) s += 4; if ((v.lang || '').replace('_', '-').toLowerCase() === lang.toLowerCase()) s += 2; if (/compact|espeak/i.test(n)) s -= 8; return s; }
  c.sort(function (a, b) { return sc(b) - sc(a); });
  return (VOICE_CACHE[lang] = c[0]);
}
try { speechSynthesis.onvoiceschanged = function () { VOICE_CACHE = {}; }; } catch (e) {}
var TTS_OK = false, TTS_URLS = {}, TTS_AUDIO = null, TTS_SET = null;
function ttsClean(t) { return String(t || '').replace(/<[^>]+>/g, '').replace(/_{2,}/g, '…').replace(/\s+/g, ' ').trim(); }
function ttsHash(str) { var h1 = 0xdeadbeef, h2 = 0x41c6ce57; for (var i = 0, ch; i < str.length; i++) { ch = str.charCodeAt(i); h1 = Math.imul(h1 ^ ch, 2654435761); h2 = Math.imul(h2 ^ ch, 1597334677); } h1 = Math.imul(h1 ^ (h1 >>> 16), 2246822507) ^ Math.imul(h2 ^ (h2 >>> 13), 3266489909); h2 = Math.imul(h2 ^ (h2 >>> 16), 2246822507) ^ Math.imul(h1 ^ (h1 >>> 13), 3266489909); return (h2 >>> 0).toString(16).padStart(8, '0') + (h1 >>> 0).toString(16).padStart(8, '0'); }
function ttsPath(code, clean) { return 'g/' + code + '/' + ttsHash(code + '|v3|' + clean) + '.wav'; }
function loadTtsSet() { if (!API.ttsList) return; API.ttsList().then(function (ps) { TTS_SET = {}; ps.forEach(function (p) { TTS_SET[p] = 1; }); }).catch(function () {}); }
var SAY_LAST = {k:'', t:0};
function playClip(cl, lg) {
  var cd = lg.slice(0, 2), C0 = window.MOVILANG_CONFIG || {}, pth = cl && ttsPath(cd, cl);
  if (!(pth && TTS_SET && TTS_SET[pth] && C0.SUPABASE_URL)) return false;
  try { speechSynthesis.cancel(); } catch (e) {} if (TTS_AUDIO) { try { TTS_AUDIO.pause(); } catch (e) {} }
  TTS_AUDIO = new Audio('/a/' + pth); TTS_AUDIO._clip = 1;
  TTS_AUDIO.play().catch(function () {});
  return true;
}
function say(txt, lang) {
  var lg = lang || SPEECH[TARGET], cl = ttsClean(txt), now = Date.now();
  if (SAY_LAST.k === lg + cl && now - SAY_LAST.t < 700) return; SAY_LAST = {k:lg + cl, t:now};
  if (playClip(cl, lg)) return;
  lang = lang || SPEECH[TARGET]; var code = lang.slice(0, 2), clean = String(txt || '').replace(/<[^>]+>/g, '').replace(/_{2,}/g, '…').trim();
  var C = window.MOVILANG_CONFIG || {};
  if (!clean) return;
  var vsAll = (window.speechSynthesis && speechSynthesis.getVoices()) || [], noLocal = vsAll.length > 0 && !bestVoice(lang);
  if ((TTS_OK === false && !noLocal) || !C.SUPABASE_URL || !C.SUPABASE_ANON_KEY) return noLocal ? noVoice(code) : sayLocal(clean, lang);
  try { speechSynthesis.cancel(); } catch (e) {} if (TTS_AUDIO) { try { TTS_AUDIO.pause(); } catch (e) {} }
  var k = code + '|' + clean, play = function (u) { TTS_AUDIO = new Audio(u); TTS_AUDIO.play().catch(function () { sayLocal(clean, lang); }); };
  if (TTS_URLS[k]) return play(TTS_URLS[k]);
  fetch(C.SUPABASE_URL + '/functions/v1/tts', {method:'POST', headers:{'Content-Type':'application/json', apikey:C.SUPABASE_ANON_KEY, Authorization:'Bearer ' + C.SUPABASE_ANON_KEY}, body:JSON.stringify({text:clean, lang:code})})
    .then(function (r) { return r.json().then(function (j) { return {ok:r.ok, j:j}; }); })
    .then(function (x) { if (x.ok && x.j.url) { TTS_OK = true; TTS_URLS[k] = x.j.url; play(x.j.url); } else { if (x.j && x.j.error === 'no_key') TTS_OK = false; noLocal ? noVoice(code) : sayLocal(clean, lang); } })
    .catch(function () { noLocal ? noVoice(code) : sayLocal(clean, lang); });
}
function noVoice(code) { toast(tx({uk:'На цьому пристрої немає голосу для мови «' + code + '». Відкрий урок у Chrome або додай голос у налаштуваннях системи.', pl:'To urządzenie nie ma głosu dla języka „' + code + '”. Otwórz lekcję w Chrome albo dodaj głos w ustawieniach systemu.', en:'This device has no voice for “' + code + '”. Open the lesson in Chrome or add a voice in system settings.'}), 'info'); }
function sayLocal(txt, lang) { try { lang = lang || SPEECH[TARGET]; if (playClip(ttsClean(txt), lang)) return; if (TTS_AUDIO && TTS_AUDIO._clip && !TTS_AUDIO.paused && !TTS_AUDIO.ended) return; var u = new SpeechSynthesisUtterance(String(txt).replace(/_{2,}/g, '…')); u.lang = lang; var v = bestVoice(lang); if (v) u.voice = v; u.rate = v && /natural|neural|online|premium|enhanced/i.test(v.name) ? 1 : .92; u.pitch = 1; speechSynthesis.cancel(); speechSynthesis.speak(u); } catch (e) { toast(t('Озвучення недоступне в цьому браузері'), 'err'); } }
var TT_L = {
  uk:{intro:'СТАРТ', match:'ПАРИ', order:'ПОРЯДОК СЛІВ', type:'ВПИШИ', tf:'ПРАВДА / НІ', vocabulary:'СЛОВНИК', listening:'АУДІЮВАННЯ', subtitles:'СУБТИТРИ', grammar:'ГРАМАТИКА', speaking:'ГОВОРІННЯ', quiz:'МІНІ-КВІЗ', final:'ФІНАЛ', cards:'ПЕРСОНАЖІ', glossary:'СЛОВНИК СЦЕНИ', quest:'КВЕСТ', drill:'ТРЕНУВАННЯ'},
  pl:{intro:'START', match:'PARY', order:'SZYK ZDANIA', type:'WPISZ', tf:'PRAWDA / FAŁSZ', vocabulary:'SŁOWNICTWO', listening:'SŁUCHANIE', subtitles:'NAPISY', grammar:'GRAMATYKA', speaking:'MÓWIENIE', quiz:'MINI QUIZ', final:'FINAŁ', cards:'POSTACIE', glossary:'SŁOWNIK SCENY', quest:'QUEST', drill:'TRENING'}};
TT_L.uk.reading = 'ЧИТАННЯ'; TT_L.pl.reading = 'CZYTANIE';
function ttName(k) { return (TT_L[LANG] && TT_L[LANG][k]) || TASK_TYPES[k] || k; }
var TASK_TYPES = { reading:'READING', intro:'START', match:'MATCH', order:'WORD ORDER', type:'TYPE IT', tf:'TRUE / FALSE', vocabulary:'VOCABULARY', listening:'LISTENING', subtitles:'SUBTITLES', grammar:'GRAMMAR', speaking:'SPEAKING', quiz:'MINI QUIZ', final:'FINAL', cards:'CHARACTERS', glossary:'SCENE GLOSSARY', quest:'QUEST', drill:'DRILL' };
function isInfo(k) { return k === 'intro' || k === 'cards' || k === 'glossary'; }
var POSTER_CLASSES = ['p1','p2','p3','p4','p5','p6','p7','p8'];


/* ================= i18n + theme ================= */
var I18N_PL = {"З'єднай слова з перекладом": "Połącz słowa z tłumaczeniem", "Впиши пропущене слово": "Wpisz brakujące słowo", "Пиши мовою, яку вивчаєш…": "Pisz w języku, którego się uczysz…", "Говори…": "Mów…", "Мова навчання": "Język nauki", "Мова завдань і пояснень": "Język zadań i wyjaśnień", "Обери мови": "Wybierz języki", "Зберегти": "Zapisz", "Вивчаєш:": "Uczysz się:", "Цей урок ще недоступний обраною мовою. Скоро!": "Ta lekcja nie jest jeszcze dostępna w wybranym języku. Wkrótce!", "Підказки": "Wskazówki", "англійська": "angielski", "польська": "polski", "українська": "ukraiński", "Змінити": "Zmień", "Скоро цією мовою": "Wkrótce w tym języku", "Завдання": "Zadania","Повторна спроба: ":"Ponowna próba: ","%. Перший результат зберігається, новий показано в дужках.":"%. Pierwszy wynik zostaje, nowy pokazujemy w nawiasie.","Відповідь уже дано. Щоб змінити, пройди урок ще раз.":"Odpowiedź już udzielona. Aby ją zmienić, przejdź lekcję ponownie.","Є завдання без відповіді":"Masz zadania bez odpowiedzi","Натисни і говори":"Naciśnij i mów","Зарахувати цю спробу":"Zalicz tę próbę","Чудова вимова!":"Świetna wymowa!","Майже! Спробуй ще раз або зарахуй.":"Prawie! Spróbuj jeszcze raz albo zalicz.","Спробуй ще раз, говори чіткіше.":"Spróbuj jeszcze raz, mów wyraźniej.","Ще раз":"Jeszcze raz","Зараховано: ":"Zaliczono: ","Слухаю…":"Słucham…","Говори англійською…":"Mów po angielsku…","Дозволь доступ до мікрофона в браузері.":"Zezwól przeglądarce na dostęp do mikrofonu.","Не вдалося розпізнати. Спробуй ще раз.":"Nie udało się rozpoznać. Spróbuj ponownie.","Нічого не почуто. Спробуй ще раз.":"Nic nie usłyszano. Spróbuj ponownie.","Порівняй зі зразком (кнопка «Прослухати») і оціни себе.":"Porównaj z wzorem (przycisk „Odsłuchaj”) i oceń się.","Звучить добре":"Brzmi dobrze","Зупинити":"Zatrzymaj","Твій браузер не підтримує мікрофон. Повтори вголос і натисни «Пропустити».":"Twoja przeglądarka nie obsługuje mikrofonu. Powtórz na głos i kliknij „Pomiń”.","Обери правильне слово":"Wybierz właściwe słowo","Обери правильну форму":"Wybierz poprawną formę","Послухай і обери відповідь":"Posłuchaj i wybierz odpowiedź","Заповни пропуск у субтитрах":"Uzupełnij lukę w napisach","З'єднай англійські слова з перекладом":"Połącz angielskie słowa z tłumaczeniem","Склади речення з поданих слів":"Ułóż zdanie z podanych słów","Впиши пропущене слово англійською":"Wpisz brakujące słowo po angielsku","Правда чи неправда?":"Prawda czy fałsz?","Послухай і повтори вголос":"Posłuchaj i powtórz na głos","Питання за сюжетом":"Pytanie o fabułę","Фінальне завдання":"Zadanie końcowe","Сцена:":"Scena:","завдань":"zadań","хв":"min","Пиши англійською…":"Pisz po angielsku…","Я сказав(ла) це вголос":"Powiedziałem(-am) to na głos","Твоя відповідь":"Twoja odpowiedź","Перевірити":"Sprawdź","Натискай слова в правильному порядку…":"Klikaj słowa w odpowiedniej kolejności…","Очистити":"Wyczyść","Правда":"Prawda","Неправда":"Fałsz","Відповідь: ":"Odpowiedź: ","Правильно: ":"Poprawnie: ","Помилок: ":"Błędów: ","слів":"słów","Напиши щонайменше ":"Napisz co najmniej ","Завдання англійською · підказки":"Zadania po angielsku · wskazówki","РЕЗУЛЬТАТ":"WYNIK","Прослухати":"Odsłuchaj","Зберегти відповідь":"Zapisz odpowiedź","Пропустити":"Pomiń","Правильно! ":"Dobrze! ","Майже. ":"Prawie. ","Відповідь збережено! ":"Odpowiedź zapisana! ","Повний курс: 16 уроків B1–B2":"Pełny kurs: 16 lekcji B1–B2","Замінить поточні уроки цього курсу на нову програму (130 інтерактивних завдань з ілюстраціями).":"Zastąpi obecne lekcje tego kursu nowym programem (130 interaktywnych zadań z ilustracjami).","Завантажити 16 уроків":"Wgraj 16 lekcji","Готово! 16 уроків завантажено.":"Gotowe! Wgrano 16 lekcji.","Режим адміністратора увімкнено":"Tryb admina włączony","Ти бачиш сайт як учень":"Widzisz stronę jak uczeń","Режим адміністратора":"Tryb administratora","Адмін: увімк.":"Admin: wł.","Адмін: вимк.":"Admin: wył.","Відмінно! Ти готовий до повного марафону.":"Świetnie! Jesteś gotowy na cały maraton.","Гарний старт! Повний марафон допоможе закріпити.":"Dobry start! Pełny maraton pomoże to utrwalić.","Ще":"Jeszcze","уроків чекають на тебе:":"lekcji czeka na Ciebie:","уроків, фінальний проєкт і сертифікат":"lekcji, projekt końcowy i certyfikat","один раз · доступ на 12 місяців":"jednorazowo · dostęp na 12 miesięcy","Ілюстрація":"Ilustracja","MATCH: варіанти «слово=значення». WORD ORDER: слова в правильному порядку. TYPE IT: прийнятні відповіді. START: пункти «що вивчиш».":"MATCH: warianty „słowo=znaczenie”. WORD ORDER: słowa w poprawnej kolejności. TYPE IT: akceptowane odpowiedzi. START: punkty „czego się nauczysz”.","Логотип і значки":"Logo i ikony","Рамка логотипа ML":"Ramka logo ML","Фон усередині логотипа":"Tło wewnątrz logo","Літери ML":"Litery ML","Кружок з ініціалом":"Kółko z inicjałem","Ініціал у кружку":"Inicjał w kółku","Активна кнопка UA/PL: фон":"Aktywny przycisk UA/PL: tło","Активна кнопка UA/PL: текст":"Aktywny przycisk UA/PL: tekst","Активна кнопка UA/PL: рамка":"Aktywny przycisk UA/PL: ramka","Вибраний елемент":"Wybrany element","Зберегти як стандартний шаблон":"Zapisz jako szablon standardowy","Клікни елемент у перегляді, щоб змінити його колір":"Kliknij element w podglądzie, aby zmienić jego kolor","Вибрати елемент":"Wybierz element","Режим вибору: клікни будь-який елемент у перегляді":"Tryb wyboru: kliknij dowolny element w podglądzie","Режим вибору вимкнено":"Tryb wyboru wyłączony","Збережено як стандартний шаблон. Кнопка «Скинути до стандартних» тепер повертає до нього.":"Zapisano jako szablon standardowy. Przycisk „Przywróć domyślne” wraca teraz do niego.","<a href=\"#/admin\" style=\"color:var(--nav-admin)\">Адмін</a>":"<a href=\"#/admin\" style=\"color:var(--nav-admin)\">Admin</a>","Тло":"Tło","Текст":"Tekst","Головний екран":"Ekran główny","Меню":"Menu","Головна кнопка":"Główny przycisk","Другорядна кнопка":"Przycisk dodatkowy","Лінії та рамки":"Linie i ramki","Акценти":"Akcenty","Повідомлення":"Komunikaty","Фон сторінки":"Tło strony","Фон меню (верхня панель)":"Tło menu (górny pasek)","Фон карток і секцій":"Tło kart i sekcji","Фон елементів у картках":"Tło elementów w kartach","Фон полів вводу":"Tło pól formularza","Основний текст":"Tekst główny","Заголовки":"Nagłówki","Додатковий текст (описи)":"Tekst dodatkowy (opisy)","Приглушений текст (підказки)":"Tekst przygaszony (podpowiedzi)","Посилання":"Linki","Текст у футері":"Tekst w stopce","Надзаголовок":"Nadtytuł","Крапка перед надзаголовком":"Kropka przed nadtytułem","Заголовок: слово 1":"Nagłówek: słowo 1","Заголовок: слово 2":"Nagłówek: słowo 2","Заголовок: слово 3":"Nagłówek: słowo 3","Пункти меню":"Pozycje menu","Пункт меню при наведенні":"Pozycja menu po najechaniu","Пункт «Адмін»":"Pozycja „Admin”","Фон кнопки":"Tło przycisku","Текст кнопки":"Tekst przycisku","Рамка":"Ramka","Колір при наведенні":"Kolor po najechaniu","Рамки карток":"Ramki kart","Лінії-розділювачі":"Linie oddzielające","Рамки полів вводу":"Ramki pól formularza","Виділений тариф і стрічка":"Wyróżniony pakiet i wstążka","Значок рівня (A2–B1)":"Odznaka poziomu (A2–B1)","Прогрес: початок":"Postęp: początek","Прогрес: кінець":"Postęp: koniec","Стовпчики графіка":"Słupki wykresu","Успіх (зелений)":"Sukces (zielony)","Помилка (червоний)":"Błąd (czerwony)","Кожен елемент має власний колір. ↺ повертає стандартний.":"Każdy element ma własny kolor. ↺ przywraca domyślny.","Скинути":"Przywróć","Шаблон":"Szablon","Зберегти сюди":"Zapisz tutaj","Завантажити":"Wczytaj","порожній":"pusty","Опублікувати на сайті":"Opublikuj na stronie","Шаблони":"Szablony","Збережи поточні кольори в один із 3 слотів, щоб потім швидко повернутися до них.":"Zapisz obecne kolory w jednym z 3 slotów, aby szybko do nich wracać.","Курс":"Kurs","Урок":"Lekcja","Вхід":"Logowanie","Кабінет":"Konto","Головна":"Strona główna","Це справжній сайт: клікай і переходь між сторінками. Зміни видно лише тут, поки не натиснеш «Опублікувати».":"To prawdziwa strona: klikaj i przechodź między podstronami. Zmiany widać tylko tutaj, dopóki nie klikniesz „Opublikuj”.","Повернено стандартні значення. Натисни «Опублікувати», щоб застосувати.":"Przywrócono domyślne. Kliknij „Opublikuj”, aby zastosować.","Вигляд сайту опубліковано":"Wygląd strony opublikowany","Перезаписати? Натисни ще раз":"Nadpisać? Kliknij ponownie","Шаблон збережено":"Szablon zapisany","Шаблон завантажено в редактор. Натисни «Опублікувати», щоб застосувати на сайті.":"Szablon wczytany do edytora. Kliknij „Opublikuj”, aby zastosować na stronie.","Реєстрація":"Rejestracja","Пробний урок безкоштовно":"Darmowa lekcja próbna","Мої марафони":"Moje maratony","Пошта":"E-mail","активовано":"aktywowany","Каталог":"Katalog","Тарифи":"Cennik","Створити кабінет":"Załóż konto","Вигляд і кольори":"Wygląd i kolory","Кольори":"Kolory","Темна":"Ciemny","Світла":"Jasny","Окремі кольори для темної та світлої теми. Зміни видно у вікні попереднього перегляду одразу.":"Osobne kolory dla motywu ciemnego i jasnego. Zmiany od razu widać w oknie podglądu.","Шрифти":"Czcionki","Заголовки":"Nagłówki","Основний текст":"Tekst główny","Застосувати до всього сайту під час редагування":"Pokazuj zmiany na całej stronie podczas edycji","Зберегти вигляд":"Zapisz wygląd","Скинути до стандартних":"Przywróć domyślne","Скасувати зміни":"Anuluj zmiany","Попередній перегляд":"Podgląd","Посилання":"Link","Зміни скасовано":"Zmiany anulowane","Точно? Натисни ще раз":"Na pewno? Kliknij ponownie","Повернено стандартні значення. Натисни «Зберегти», щоб застосувати.":"Przywrócono domyślne. Kliknij „Zapisz”, aby zastosować.","Вигляд сайту збережено":"Wygląd strony zapisany","Фон сторінки":"Tło strony","Фон секцій і карток":"Tło sekcji i kart","Фон панелей і полів":"Tło paneli i pól","Рамки й лінії":"Ramki i linie","Додатковий текст":"Tekst dodatkowy","Приглушений текст":"Tekst przygaszony","Головний акцент (кнопки)":"Główny akcent (przyciski)","Текст на кнопках":"Tekst na przyciskach","Фіолетовий акцент":"Akcent fioletowy","Неоновий акцент (посилання, мітки)":"Akcent neonowy (linki, etykiety)","Виділення (рівні, значки)":"Wyróżnienia (poziomy, odznaki)","Успіх (зелений)":"Sukces (zielony)","Пошту підтверджено! Ласкаво просимо до MoviLang.":"E-mail potwierdzony! Witamy w MoviLang.","Пошту підтверджено! Тепер увійди.":"E-mail potwierdzony! Teraz się zaloguj.","Посилання недійсне або застаріле. Увійди або зареєструйся ще раз.":"Link jest nieważny lub wygasł. Zaloguj się lub zarejestruj ponownie.","Світла тема":"Jasny motyw","Темна тема":"Ciemny motyw","Потрібні права адміністратора": "Wymagane uprawnienia administratora", "Користувач з такою поштою вже існує": "Użytkownik z tym adresem e-mail już istnieje", "Невірна пошта або пароль": "Nieprawidłowy e-mail lub hasło", "Увійдіть в акаунт": "Zaloguj się na konto", "Такого ключа не знайдено. Перевір літери O та 0, I та 1.": "Nie znaleziono takiego klucza. Sprawdź litery O i 0, I i 1.", "Цей ключ уже активовано.": "Ten klucz został już aktywowany.", "Акаунт створено! Перевір пошту (і папку «Спам»), натисни посилання з листа, потім увійди.": "Konto utworzone! Sprawdź skrzynkę (i folder „Spam”), kliknij link z wiadomości, a potem się zaloguj.", "Пошту не підтверджено. Відкрий лист від Supabase і натисни посилання, потім увійди.": "E-mail niepotwierdzony. Otwórz wiadomość od Supabase, kliknij link, a potem się zaloguj.", "Невірна пошта або пароль.": "Nieprawidłowy e-mail lub hasło.", "Помилка входу: ": "Błąd logowania: ", "<a href=\"#/\">Головна</a><a href=\"#/catalog\">Каталог</a><a href=\"#/trial\">Пробний урок</a><a href=\"#/pricing\">Тарифи</a>": "<a href=\"#/\">Strona główna</a><a href=\"#/catalog\">Katalog</a><a href=\"#/trial\">Lekcja próbna</a><a href=\"#/pricing\">Cennik</a>", "<a href=\"#/cabinet\">Кабінет</a>": "<a href=\"#/cabinet\">Konto</a>", "<a href=\"#/admin\" style=\"color:var(--red)\">Адмін</a>": "<a href=\"#/admin\" style=\"color:var(--red)\">Admin</a>", "</span></a><button class=\"btn btn-ghost btn-sm\" type=\"button\" id=\"logoutBtn\">Вийти</button>": "</span></a><button class=\"btn btn-ghost btn-sm\" type=\"button\" id=\"logoutBtn\">Wyloguj</button>", "<a class=\"btn btn-ghost btn-sm\" href=\"#/login\">Увійти</a><a class=\"btn btn-red btn-sm\" href=\"#/register\">Реєстрація</a>": "<a class=\"btn btn-ghost btn-sm\" href=\"#/login\">Zaloguj się</a><a class=\"btn btn-red btn-sm\" href=\"#/register\">Rejestracja</a>", "Ви вийшли з акаунта": "Wylogowano", "СЕРІАЛ": "SERIAL", "ФІЛЬМ": "FILM", "<span class=\"tag new\">СКОРО</span>": "<span class=\"tag new\">WKRÓTCE</span>", "<div class=\"empty\">Курсів поки немає. Адміністратор може додати їх в адмін-панелі.</div>": "<div class=\"empty\">Na razie brak kursów. Administrator może je dodać w panelu admina.</div>", " уроків</span><b>": " lekcji</span><b>", "<span class=\"ribbon\">НАЙПОПУЛЯРНІШИЙ</span>": "<span class=\"ribbon\">NAJPOPULARNIEJSZY</span>", "\" href=\"#/buy\">Купити ключ</a></div>": "\" href=\"#/buy\">Kup klucz</a></div>", "Мій кабінет": "Moje konto", "Створити кабінет": "Załóż konto", "</a><a class=\"btn btn-ghost\" href=\"#/trial\">Пробний урок безкоштовно</a></div>": "</a><a class=\"btn btn-ghost\" href=\"#/trial\">Darmowa lekcja próbna</a></div>", "<div class=\"hero-meta\"><div><b>15 хв</b>на день</div><div><b>": "<div class=\"hero-meta\"><div><b>15 min</b>dziennie</div><div><b>", "</b>марафонів</div><div><b>6 типів</b>завдань</div></div></div>": "</b>maratonów</div><div><b>6 typów</b>zadań</div></div></div>", "<section><div class=\"sec-head\"><div class=\"eyebrow\">Як це працює</div><h2>Від квитка до першої розмови</h2></div><div class=\"steps\">": "<section><div class=\"sec-head\"><div class=\"eyebrow\">Jak to działa</div><h2>Od biletu do pierwszej rozmowy</h2></div><div class=\"steps\">", "Купуєш ключ": "Kupujesz klucz", "Обираєш фільм, пакет або підписку.": "Wybierasz film, pakiet lub subskrypcję.", "Активуєш": "Aktywujesz", "Вводиш код у кабінеті.": "Wpisujesz kod na swoim koncie.", "Відкриваєш марафон": "Otwierasz maraton", "Уроки за сценами фільму.": "Lekcje oparte na scenach z filmu.", "Виконуєш завдання": "Wykonujesz zadania", "Слова, аудіо, субтитри, граматика, говоріння.": "Słówka, audio, napisy, gramatyka, mówienie.", "Бачиш прогрес": "Widzisz postępy", "Статистика й бали в кабінеті.": "Statystyki i punkty na koncie.", "<section><div class=\"sec-head\"><div class=\"eyebrow\">Каталог</div><h2>Фільми та серіали</h2></div>": "<section><div class=\"sec-head\"><div class=\"eyebrow\">Katalog</div><h2>Filmy i seriale</h2></div>", "<section id=\"pricing\"><div class=\"sec-head\"><div class=\"eyebrow\">Тарифи</div><h2>Обери свій квиток</h2></div>": "<section id=\"pricing\"><div class=\"sec-head\"><div class=\"eyebrow\">Cennik</div><h2>Wybierz swój bilet</h2></div>", "<section><div class=\"sec-head\"><div class=\"eyebrow\">FAQ</div><h2>Питання та відповіді</h2></div>": "<section><div class=\"sec-head\"><div class=\"eyebrow\">FAQ</div><h2>Pytania i odpowiedzi</h2></div>", "<div class=\"page\"><div class=\"sec-head\"><div class=\"eyebrow\">Каталог</div><h2>Фільми та серіали</h2></div>": "<div class=\"page\"><div class=\"sec-head\"><div class=\"eyebrow\">Katalog</div><h2>Filmy i seriale</h2></div>", "<div class=\"page\"><div class=\"sec-head\"><div class=\"eyebrow\">Тарифи</div><h2>Обери свій квиток</h2></div>": "<div class=\"page\"><div class=\"sec-head\"><div class=\"eyebrow\">Cennik</div><h2>Wybierz swój bilet</h2></div>", "<div class=\"sec-head\" style=\"margin-top:30px\"><h2>Питання та відповіді</h2></div>": "<div class=\"sec-head\" style=\"margin-top:30px\"><h2>Pytania i odpowiedzi</h2></div>", "<div class=\"page\"><div class=\"sec-head\"><div class=\"eyebrow\">Купівля ключа</div><h2>Як отримати ключ доступу</h2><p class=\"lead\">": "<div class=\"page\"><div class=\"sec-head\"><div class=\"eyebrow\">Zakup klucza</div><h2>Jak zdobyć klucz dostępu</h2><p class=\"lead\">", "<div class=\"panel\" style=\"max-width:560px\"><h3>Уже маєш ключ?</h3><p class=\"muted\" style=\"margin-block:8px 14px\">Активуй його в особистому кабінеті.</p><a class=\"btn btn-red\" href=\"": "<div class=\"panel\" style=\"max-width:560px\"><h3>Masz już klucz?</h3><p class=\"muted\" style=\"margin-block:8px 14px\">Aktywuj go na swoim koncie.</p><a class=\"btn btn-red\" href=\"", "Перейти до кабінету": "Przejdź do konta", "Новий кабінет": "Nowe konto", "Вхід": "Logowanie", "Створи свій кабінет": "Załóż swoje konto", "З поверненням!": "Witaj ponownie!", "<label class=\"fl\" for=\"aName\">Ім'я<input class=\"inp-s\" id=\"aName\" autocomplete=\"name\" required></label>": "<label class=\"fl\" for=\"aName\">Imię<input class=\"inp-s\" id=\"aName\" autocomplete=\"name\" required></label>", "<label class=\"fl\" for=\"aEmail\">Пошта<input class=\"inp-s\" id=\"aEmail\" type=\"email\" autocomplete=\"email\" required></label>": "<label class=\"fl\" for=\"aEmail\">E-mail<input class=\"inp-s\" id=\"aEmail\" type=\"email\" autocomplete=\"email\" required></label>", "<label class=\"fl\" for=\"aPass\">Пароль": "<label class=\"fl\" for=\"aPass\">Hasło", " (мінімум 6 символів)": " (minimum 6 znaków)", "Зареєструватися": "Zarejestruj się", "Увійти": "Zaloguj się", "Вже є акаунт? <a href=\"#/login\">Увійти</a>": "Masz już konto? <a href=\"#/login\">Zaloguj się</a>", "Ще немає акаунта? <a href=\"#/register\">Створити кабінет</a>": "Nie masz jeszcze konta? <a href=\"#/register\">Załóż konto</a>", "<p class=\"hint\" style=\"margin-top:10px\">Демо: адмін admin@movielang.demo / admin123, учень olena@example.com / demo123</p>": "<p class=\"hint\" style=\"margin-top:10px\">Demo: admin admin@movielang.demo / admin123, uczeń olena@example.com / demo123</p>", "Введи коректну пошту, напр. name@gmail.com": "Wpisz poprawny e-mail, np. name@gmail.com", "Пароль має містити щонайменше 6 символів.": "Hasło musi mieć co najmniej 6 znaków.", "Вкажи своє ім'я.": "Podaj swoje imię.", "Зачекай…": "Chwileczkę…", "Кабінет створено!": "Konto utworzone!", "Вхід виконано": "Zalogowano", "Спершу увійди в акаунт": "Najpierw zaloguj się na konto", "Урок": "Lekcja", "Перший урок": "Pierwsza lekcja", "П'ять уроків": "Pięć lekcji", "Три дні навчання": "Trzy dni nauki", "Точність 90%+": "Trafność 90%+", "Два марафони": "Dwa maratony", "Марафон пройдено": "Maraton ukończony", "<div class=\"page\"><div class=\"sec-head\"><div class=\"eyebrow\">Особистий кабінет</div><h2>Привіт, ": "<div class=\"page\"><div class=\"sec-head\"><div class=\"eyebrow\">Moje konto</div><h2>Cześć, ", "<form class=\"form\" id=\"keyForm\" novalidate><label class=\"fl\" for=\"keyInput\">Активувати ключ<input class=\"inp\" id=\"keyInput\" placeholder=\"XXXX-XXXX-XXXX\" maxlength=\"14\" autocomplete=\"off\" style=\"font-size:15px;padding:11px 12px\"></label><button class=\"btn btn-red btn-sm\" type=\"submit\" style=\"justify-content:center\">Активувати</button><div class=\"msg small\" id=\"keyMsg\" role=\"status\"></div>": "<form class=\"form\" id=\"keyForm\" novalidate><label class=\"fl\" for=\"keyInput\">Aktywuj klucz<input class=\"inp\" id=\"keyInput\" placeholder=\"XXXX-XXXX-XXXX\" maxlength=\"14\" autocomplete=\"off\" style=\"font-size:15px;padding:11px 12px\"></label><button class=\"btn btn-red btn-sm\" type=\"submit\" style=\"justify-content:center\">Aktywuj</button><div class=\"msg small\" id=\"keyMsg\" role=\"status\"></div>", "<p class=\"hint\">Демо-ключ: HPS1-7KQ4-WZ9M</p>": "<p class=\"hint\">Klucz demo: HPS1-7KQ4-WZ9M</p>", "<a class=\"btn btn-ghost btn-sm\" href=\"#/admin\" style=\"justify-content:center\">Адмін-панель</a>": "<a class=\"btn btn-ghost btn-sm\" href=\"#/admin\" style=\"justify-content:center\">Panel admina</a>", "</b><span>уроків пройдено</span></div><div class=\"stat\"><b>": "</b><span>ukończonych lekcji</span></div><div class=\"stat\"><b>", "%</b><span>середній бал</span></div><div class=\"stat\"><b>": "%</b><span>średni wynik</span></div><div class=\"stat\"><b>", "</b><span>XP набрано</span></div><div class=\"stat\"><b>": "</b><span>zdobytych XP</span></div><div class=\"stat\"><b>", "</b><span>днів навчання</span></div></div>": "</b><span>dni nauki</span></div></div>", "<div class=\"rows\"><div class=\"box\"><h4>Мої марафони</h4>": "<div class=\"rows\"><div class=\"box\"><h4>Moje maratony</h4>", "<div class=\"empty small\">Марафонів ще немає. Активуй ключ або <a href=\"#/trial\">пройди пробний урок</a>.</div>": "<div class=\"empty small\">Nie masz jeszcze maratonów. Aktywuj klucz albo <a href=\"#/trial\">przejdź lekcję próbną</a>.</div>", "<a class=\"btn btn-ghost btn-sm\" href=\"#/catalog\" style=\"justify-self:start\">Каталог курсів</a></div>": "<a class=\"btn btn-ghost btn-sm\" href=\"#/catalog\" style=\"justify-self:start\">Katalog kursów</a></div>", "<div class=\"box\"><h4>Досягнення</h4><div class=\"ach\">": "<div class=\"box\"><h4>Osiągnięcia</h4><div class=\"ach\">", "<h4>Останні уроки</h4><div class=\"done-list\">": "<h4>Ostatnie lekcje</h4><div class=\"done-list\">", "<span class=\"muted\">Ще немає пройдених уроків</span>": "<span class=\"muted\">Brak ukończonych lekcji</span>", "Ключ має містити 12 символів.": "Klucz musi mieć 12 znaków.", "Ключ активовано! Марафон відкрито.": "Klucz aktywowany! Maraton odblokowany.", "<div class=\"page\"><div class=\"empty\">Курс не знайдено. <a href=\"#/catalog\">До каталогу</a></div></div>": "<div class=\"page\"><div class=\"empty\">Nie znaleziono kursu. <a href=\"#/catalog\">Do katalogu</a></div></div>", " уроків</span><span class=\"badge\">": " lekcji</span><span class=\"badge\">", "серіал": "serial", "фільм": "film", "<span class=\"badge\" style=\"color:var(--ok)\">доступ відкрито</span>": "<span class=\"badge\" style=\"color:var(--ok)\">dostęp odblokowany</span>", "<div class=\"row\"><a class=\"btn btn-red\" href=\"#/buy\">Купити ключ · ": "<div class=\"row\"><a class=\"btn btn-red\" href=\"#/buy\">Kup klucz · ", "<a class=\"btn btn-ghost\" href=\"#/cabinet\">Активувати ключ</a>": "<a class=\"btn btn-ghost\" href=\"#/cabinet\">Aktywuj klucz</a>", "<a class=\"btn btn-ghost\" href=\"#/register\">Створити кабінет</a>": "<a class=\"btn btn-ghost\" href=\"#/register\">Załóż konto</a>", " · безкоштовно": " · za darmo", "<div class=\"empty\" style=\"margin-top:20px\">Уроки цього марафону скоро з'являться.</div>": "<div class=\"empty\" style=\"margin-top:20px\">Lekcje tego maratonu pojawią się wkrótce.</div>", "</div><div class=\"panel\"><h3 style=\"margin-bottom:18px\">Типи завдань у курсі</h3><div class=\"task-types\">": "</div><div class=\"panel\"><h3 style=\"margin-bottom:18px\">Typy zadań w kursie</h3><div class=\"task-types\">", "</span><span class=\"tcount\">Завдання ": "</span><span class=\"tcount\">Zadanie ", " з ": " z ", "<div class=\"tscene\"><b>Сцена:</b> ": "<div class=\"tscene\"><b>Scena:</b> ", "<div><button class=\"speak\" type=\"button\" id=\"tsay\"><span class=\"play\"></span>Прослухати</button></div>": "<div><button class=\"speak\" type=\"button\" id=\"tsay\"><span class=\"play\"></span>Odsłuchaj</button></div>", "<textarea class=\"inp-s\" id=\"tfinal\" rows=\"6\" placeholder=\"My favourite scene is…\"></textarea><div class=\"row\"><button class=\"btn btn-red\" type=\"button\" id=\"tsubmit\">Зберегти відповідь</button><span class=\"hint\" id=\"wc\">0 слів</span></div>": "<textarea class=\"inp-s\" id=\"tfinal\" rows=\"6\" placeholder=\"My favourite scene is…\"></textarea><div class=\"row\"><button class=\"btn btn-red\" type=\"button\" id=\"tsubmit\">Zapisz odpowiedź</button><span class=\"hint\" id=\"wc\">0 słów</span></div>", "<div class=\"topts\"><button class=\"topt\" type=\"button\" data-s=\"1\">✓ Я повторив(ла)</button><button class=\"topt\" type=\"button\" data-s=\"0\">Пропустити</button></div>": "<div class=\"topts\"><button class=\"topt\" type=\"button\" data-s=\"1\">✓ Powtórzyłem(-am)</button><button class=\"topt\" type=\"button\" data-s=\"0\">Pomiń</button></div>", "<div class=\"tfb\" id=\"tfb\"></div><div class=\"tnav\"><span class=\"hint\">Підказки українською, завдання англійською</span><button class=\"btn btn-red\" type=\"button\" id=\"tnext\" hidden>Далі</button></div>": "<div class=\"tfb\" id=\"tfb\"></div><div class=\"tnav\"><span class=\"hint\">Wskazówki po polsku, zadania po angielsku</span><button class=\"btn btn-red\" type=\"button\" id=\"tnext\" hidden>Dalej</button></div>", " слів": " słów", "Напиши хоча б 20 слів (зараз ": "Napisz co najmniej 20 słów (teraz ", "Відповідь збережено! ": "Odpowiedź zapisana! ", "Далі": "Dalej", "Показати результат": "Pokaż wynik", "Правильно! ": "Dobrze! ", "Майже. ": "Prawie. ", "<div class=\"tres\"><span class=\"ttag\">РЕЗУЛЬТАТ</span><div class=\"big\">": "<div class=\"tres\"><span class=\"ttag\">WYNIK</span><div class=\"big\">", "</div><p class=\"lead\" style=\"text-align:center\" id=\"tresText\">Бал: ": "</div><p class=\"lead\" style=\"text-align:center\" id=\"tresText\">Wynik: ", "<div class=\"empty\">У цьому уроці ще немає завдань.</div>": "<div class=\"empty\">Ta lekcja nie ma jeszcze zadań.</div>", "<div class=\"page\"><div class=\"empty\">Урок не знайдено.</div></div>": "<div class=\"page\"><div class=\"empty\">Nie znaleziono lekcji.</div></div>", "<div class=\"page\"><div class=\"empty\">Цей урок відкривається після активації ключа. <a href=\"#/course/": "<div class=\"page\"><div class=\"empty\">Ta lekcja odblokuje się po aktywacji klucza. <a href=\"#/course/", "\">До марафону</a></div></div>": "\">Do maratonu</a></div></div>", "Марафон": "Maraton", "</a><div class=\"eyebrow\">Урок ": "</a><div class=\"eyebrow\">Lekcja ", "Бал: ": "Wynik: ", "%. Результат збережено в кабінеті.": "%. Wynik zapisany na Twoim koncie.", "%. Створи кабінет, щоб зберігати прогрес.": "%. Załóż konto, aby zapisywać postępy.", "\">Наступний урок</a>": "\">Następna lekcja</a>", "<a class=\"btn btn-red\" href=\"#/buy\">Отримати ключ доступу</a>": "<a class=\"btn btn-red\" href=\"#/buy\">Zdobądź klucz dostępu</a>", "</a><button class=\"btn btn-ghost\" type=\"button\" id=\"again\">Пройти ще раз</button>": "</a><button class=\"btn btn-ghost\" type=\"button\" id=\"again\">Przejdź jeszcze raz</button>", "<div class=\"page\"><div class=\"empty\">Пробний урок з'явиться, щойно буде створено перший курс.</div></div>": "<div class=\"page\"><div class=\"empty\">Lekcja próbna pojawi się, gdy zostanie utworzony pierwszy kurs.</div></div>", "<div class=\"page\"><div class=\"empty\">Ця сторінка доступна лише адміністратору.</div></div>": "<div class=\"page\"><div class=\"empty\">Ta strona jest dostępna tylko dla administratora.</div></div>", "<div class=\"page\"><div class=\"sec-head\"><div class=\"eyebrow\">Адмін-панель</div><h2>Керування MoviLang</h2></div><div class=\"tabs\" role=\"tablist\">": "<div class=\"page\"><div class=\"sec-head\"><div class=\"eyebrow\">Panel admina</div><h2>Zarządzanie MoviLang</h2></div><div class=\"tabs\" role=\"tablist\">", "Статистика": "Statystyki", "Користувачі": "Użytkownicy", "Курси й уроки": "Kursy i lekcje", "Ключі доступу": "Klucze dostępu", "Тексти сайту": "Teksty strony", "</div><div id=\"adminBody\"><p class=\"muted\">Завантаження…</p></div></div>": "</div><div id=\"adminBody\"><p class=\"muted\">Ładowanie…</p></div></div>", "<div class=\"empty\">Помилка: ": "<div class=\"empty\">Błąd: ", "</b><span>учнів усього</span></div><div class=\"stat\"><b>": "</b><span>uczniów łącznie</span></div><div class=\"stat\"><b>", "</b><span>нових за 7 днів</span></div>": "</b><span>nowych w 7 dni</span></div>", "</b><span>активних за 7 днів</span></div><div class=\"stat\"><b>": "</b><span>aktywnych w 7 dni</span></div><div class=\"stat\"><b>", "</b><span>ключів активовано</span></div></div>": "</b><span>aktywowanych kluczy</span></div></div>", "</b><span>курсів</span></div><div class=\"stat\"><b>": "</b><span>kursów</span></div><div class=\"stat\"><b>", "</b><span>записів на курси</span></div></div>": "</b><span>zapisów na kursy</span></div></div>", "<div class=\"rows\"><div class=\"box\"><h4>Пройдені уроки за 14 днів</h4><div class=\"week\" style=\"grid-template-columns:repeat(14,1fr);height:140px\">": "<div class=\"rows\"><div class=\"box\"><h4>Ukończone lekcje w ciągu 14 dni</h4><div class=\"week\" style=\"grid-template-columns:repeat(14,1fr);height:140px\">", "</div></div><div class=\"box\"><h4>Учні за курсами</h4><div class=\"bars\">": "</div></div><div class=\"box\"><h4>Uczniowie wg kursów</h4><div class=\"bars\">", "<div><button class=\"btn btn-danger btn-sm\" type=\"button\" id=\"resetDemo\">Скинути демо-дані</button></div>": "<div><button class=\"btn btn-danger btn-sm\" type=\"button\" id=\"resetDemo\">Zresetuj dane demo</button></div>", "Демо-дані скинуто": "Dane demo zresetowane", "Точно скинути? Натисни ще раз": "Na pewno? Kliknij ponownie", "<span class=\"muted small\">це ви</span>": "<span class=\"muted small\">to Ty</span>", "Зробити учнем": "Zmień na ucznia", "Зробити адміном": "Nadaj rolę admina", "<p class=\"muted\" style=\"margin-bottom:14px\">Усього: ": "<p class=\"muted\" style=\"margin-bottom:14px\">Łącznie: ", "</p><div class=\"tbl-wrap\"><table class=\"tbl\"><thead><tr><th>Користувач</th><th>Роль</th><th>Реєстрація</th><th>Курсів</th><th>Уроків</th><th>Сер. бал</th><th>Активність</th><th></th></tr></thead><tbody>": "</p><div class=\"tbl-wrap\"><table class=\"tbl\"><thead><tr><th>Użytkownik</th><th>Rola</th><th>Rejestracja</th><th>Kursy</th><th>Lekcje</th><th>Śr. wynik</th><th>Aktywność</th><th></th></tr></thead><tbody>", "Роль змінено": "Rola zmieniona", "<div class=\"row\" style=\"justify-content:space-between;margin-bottom:14px\"><span class=\"muted\">Курсів: ": "<div class=\"row\" style=\"justify-content:space-between;margin-bottom:14px\"><span class=\"muted\">Kursów: ", "</span><button class=\"btn btn-red btn-sm\" type=\"button\" id=\"newCourse\">+ Новий курс</button></div>": "</span><button class=\"btn btn-red btn-sm\" type=\"button\" id=\"newCourse\">+ Nowy kurs</button></div>", "<div class=\"tbl-wrap\"><table class=\"tbl\"><thead><tr><th>Курс</th><th>Тип</th><th>Рівень</th><th>Уроків</th><th>Ціна</th><th>Статус</th><th></th></tr></thead><tbody>": "<div class=\"tbl-wrap\"><table class=\"tbl\"><thead><tr><th>Kurs</th><th>Typ</th><th>Poziom</th><th>Lekcje</th><th>Cena</th><th>Status</th><th></th></tr></thead><tbody>", "Серіал": "Serial", "Фільм": "Film", "опубліковано": "opublikowany", "чернетка": "szkic", "\">Редагувати</button></td></tr>": "\">Edytuj</button></td></tr>", "<div class=\"empty\">Курсів ще немає. <button class=\"btn btn-ghost btn-sm\" type=\"button\" id=\"importSeed\">Додати демо-курс «Гаррі Поттер»</button></div>": "<div class=\"empty\">Nie ma jeszcze kursów. <button class=\"btn btn-ghost btn-sm\" type=\"button\" id=\"importSeed\">Dodaj kurs demo „Harry Potter”</button></div>", "Демо-курс додано": "Kurs demo dodany", "<div style=\"display:grid;gap:18px\"><button class=\"btn btn-ghost btn-sm\" type=\"button\" id=\"back\" style=\"justify-self:start\">← Усі курси</button>": "<div style=\"display:grid;gap:18px\"><button class=\"btn btn-ghost btn-sm\" type=\"button\" id=\"back\" style=\"justify-self:start\">← Wszystkie kursy</button>", "Редагування курсу": "Edycja kursu", "Новий курс": "Nowy kurs", "<label class=\"fl\" for=\"cTitle\">Назва<input class=\"inp-s\" id=\"cTitle\" value=\"": "<label class=\"fl\" for=\"cTitle\">Tytuł<input class=\"inp-s\" id=\"cTitle\" value=\"", "<div class=\"grid3\"><label class=\"fl\" for=\"cKind\">Тип<select class=\"inp-s\" id=\"cKind\"><option value=\"film\"": "<div class=\"grid3\"><label class=\"fl\" for=\"cKind\">Typ<select class=\"inp-s\" id=\"cKind\"><option value=\"film\"", ">Фільм</option><option value=\"series\"": ">Film</option><option value=\"series\"", ">Серіал</option></select></label>": ">Serial</option></select></label>", "<label class=\"fl\" for=\"cLevel\">Рівень<input class=\"inp-s\" id=\"cLevel\" value=\"": "<label class=\"fl\" for=\"cLevel\">Poziom<input class=\"inp-s\" id=\"cLevel\" value=\"", "\"></label><label class=\"fl\" for=\"cPrice\">Ціна<input class=\"inp-s\" id=\"cPrice\" value=\"": "\"></label><label class=\"fl\" for=\"cPrice\">Cena<input class=\"inp-s\" id=\"cPrice\" value=\"", "<div class=\"grid2\"><label class=\"fl\" for=\"cPoster\">Колір постера<select class=\"inp-s\" id=\"cPoster\">": "<div class=\"grid2\"><label class=\"fl\" for=\"cPoster\">Kolor plakatu<select class=\"inp-s\" id=\"cPoster\">", "Фіолетовий": "Fioletowy", "Бордовий": "Bordowy", "Синій": "Niebieski", "Зелений": "Zielony", "Червоний": "Czerwony", "Золотий": "Złoty", "Індиго": "Indygo", "Рожевий": "Różowy", "<label class=\"fl\" for=\"cPub\">Статус<select class=\"inp-s\" id=\"cPub\"><option value=\"1\"": "<label class=\"fl\" for=\"cPub\">Status<select class=\"inp-s\" id=\"cPub\"><option value=\"1\"", ">Опубліковано</option><option value=\"0\"": ">Opublikowany</option><option value=\"0\"", ">Чернетка</option></select></label></div>": ">Szkic</option></select></label></div>", "<label class=\"fl\" for=\"cDesc\">Опис<textarea class=\"inp-s\" id=\"cDesc\">": "<label class=\"fl\" for=\"cDesc\">Opis<textarea class=\"inp-s\" id=\"cDesc\">", "<div class=\"row\"><button class=\"btn btn-red\" type=\"submit\">Зберегти курс</button>": "<div class=\"row\"><button class=\"btn btn-red\" type=\"submit\">Zapisz kurs</button>", "<button class=\"btn btn-danger btn-sm\" type=\"button\" id=\"delC\">Видалити курс</button>": "<button class=\"btn btn-danger btn-sm\" type=\"button\" id=\"delC\">Usuń kurs</button>", "<div class=\"panel\" style=\"display:grid;gap:14px\"><div class=\"row\" style=\"justify-content:space-between\"><h3>Уроки (": "<div class=\"panel\" style=\"display:grid;gap:14px\"><div class=\"row\" style=\"justify-content:space-between\"><h3>Lekcje (", ")</h3><button class=\"btn btn-red btn-sm\" type=\"button\" id=\"newL\">+ Новий урок</button></div>": ")</h3><button class=\"btn btn-red btn-sm\" type=\"button\" id=\"newL\">+ Nowa lekcja</button></div>", " завдань</small></span><button class=\"btn btn-ghost btn-sm\" type=\"button\" data-l=\"": " zadań</small></span><button class=\"btn btn-ghost btn-sm\" type=\"button\" data-l=\"", "\">Редагувати</button></li>": "\">Edytuj</button></li>", "<div class=\"empty\">Додай перший урок.</div>": "<div class=\"empty\">Dodaj pierwszą lekcję.</div>", "<p class=\"muted\">Після збереження курсу можна буде додавати уроки.</p>": "<p class=\"muted\">Po zapisaniu kursu będzie można dodawać lekcje.</p>", "Вкажи назву курсу.": "Podaj tytuł kursu.", "Курс збережено": "Kurs zapisany", "Видалити разом з уроками? Натисни ще раз": "Usunąć razem z lekcjami? Kliknij ponownie", "Курс видалено": "Kurs usunięty", "\"><div class=\"row\" style=\"justify-content:space-between\"><b>Завдання ": "\"><div class=\"row\" style=\"justify-content:space-between\"><b>Zadanie ", "\">Видалити</button></div>": "\">Usuń</button></div>", "<div class=\"grid2\"><label class=\"fl\">Тип<select class=\"inp-s\" data-f=\"type\">": "<div class=\"grid2\"><label class=\"fl\">Typ<select class=\"inp-s\" data-f=\"type\">", "<label class=\"fl\">Опис сцени<input class=\"inp-s\" data-f=\"scene\" value=\"": "<label class=\"fl\">Opis sceny<input class=\"inp-s\" data-f=\"scene\" value=\"", "<label class=\"fl\">Питання / речення (пропуск позначай ____)<input class=\"inp-s\" data-f=\"q\" value=\"": "<label class=\"fl\">Pytanie / zdanie (lukę oznacz ____)<input class=\"inp-s\" data-f=\"q\" value=\"", "<div class=\"grid2\"><label class=\"fl\">Варіанти через « / »<input class=\"inp-s\" data-f=\"options\" value=\"": "<div class=\"grid2\"><label class=\"fl\">Warianty oddzielone « / »<input class=\"inp-s\" data-f=\"options\" value=\"", "<label class=\"fl\">Номер правильного варіанта (1, 2, 3…)<input class=\"inp-s\" data-f=\"answer\" type=\"number\" min=\"1\" value=\"": "<label class=\"fl\">Numer poprawnej odpowiedzi (1, 2, 3…)<input class=\"inp-s\" data-f=\"answer\" type=\"number\" min=\"1\" value=\"", "<div class=\"grid2\"><label class=\"fl\">Фраза для озвучення (необов'язково)<input class=\"inp-s\" data-f=\"say\" value=\"": "<div class=\"grid2\"><label class=\"fl\">Fraza do odsłuchu (opcjonalnie)<input class=\"inp-s\" data-f=\"say\" value=\"", "<label class=\"fl\">Пояснення після відповіді<input class=\"inp-s\" data-f=\"tip\" value=\"": "<label class=\"fl\">Wyjaśnienie po odpowiedzi<input class=\"inp-s\" data-f=\"tip\" value=\"", "<div style=\"display:grid;gap:18px\"><button class=\"btn btn-ghost btn-sm\" type=\"button\" id=\"backC\" style=\"justify-self:start\">← До курсу</button>": "<div style=\"display:grid;gap:18px\"><button class=\"btn btn-ghost btn-sm\" type=\"button\" id=\"backC\" style=\"justify-self:start\">← Do kursu</button>", "Редагування уроку": "Edycja lekcji", "Новий урок": "Nowa lekcja", "<div class=\"grid3\"><label class=\"fl\" for=\"lNum\">Номер<input class=\"inp-s\" id=\"lNum\" type=\"number\" min=\"1\" value=\"": "<div class=\"grid3\"><label class=\"fl\" for=\"lNum\">Numer<input class=\"inp-s\" id=\"lNum\" type=\"number\" min=\"1\" value=\"", "\"></label><label class=\"fl\" for=\"lTitle\" style=\"grid-column:span 2\">Назва уроку<input class=\"inp-s\" id=\"lTitle\" value=\"": "\"></label><label class=\"fl\" for=\"lTitle\" style=\"grid-column:span 2\">Tytuł lekcji<input class=\"inp-s\" id=\"lTitle\" value=\"", "<div class=\"grid2\"><label class=\"fl\" for=\"lGr\">Граматика / тема<input class=\"inp-s\" id=\"lGr\" value=\"": "<div class=\"grid2\"><label class=\"fl\" for=\"lGr\">Gramatyka / temat<input class=\"inp-s\" id=\"lGr\" value=\"", "\"></label><label class=\"fl\" for=\"lScene\">Сцена (опис своїми словами)<input class=\"inp-s\" id=\"lScene\" value=\"": "\"></label><label class=\"fl\" for=\"lScene\">Scena (opis własnymi słowami)<input class=\"inp-s\" id=\"lScene\" value=\"", "<h3 style=\"margin-top:8px\">Завдання (": "<h3 style=\"margin-top:8px\">Zadanie (", "<button class=\"btn btn-ghost btn-sm\" type=\"button\" id=\"addT\" style=\"justify-self:start\">+ Додати завдання</button>": "<button class=\"btn btn-ghost btn-sm\" type=\"button\" id=\"addT\" style=\"justify-self:start\">+ Dodaj zadanie</button>", "<div class=\"row\"><button class=\"btn btn-red\" type=\"submit\">Зберегти урок</button>": "<div class=\"row\"><button class=\"btn btn-red\" type=\"submit\">Zapisz lekcję</button>", "\">Переглянути як учень</a><button class=\"btn btn-danger btn-sm\" type=\"button\" id=\"delL\">Видалити урок</button>": "\">Zobacz jako uczeń</a><button class=\"btn btn-danger btn-sm\" type=\"button\" id=\"delL\">Usuń lekcję</button>", "Вкажи назву уроку.": "Podaj tytuł lekcji.", "У ": "W ", " завданні(ях) порожнє питання.": " zadaniu(-ach) brakuje pytania.", "Урок збережено": "Lekcja zapisana", "Точно видалити? Натисни ще раз": "Na pewno usunąć? Kliknij ponownie", "Урок видалено": "Lekcja usunięta", "<form class=\"panel form\" id=\"kForm\" novalidate style=\"margin-bottom:18px\"><h3>Згенерувати ключі</h3><div class=\"grid3\"><label class=\"fl\" for=\"kCourse\">Курс<select class=\"inp-s\" id=\"kCourse\"><option value=\"\">Усі курси (підписка)</option>": "<form class=\"panel form\" id=\"kForm\" novalidate style=\"margin-bottom:18px\"><h3>Wygeneruj klucze</h3><div class=\"grid3\"><label class=\"fl\" for=\"kCourse\">Kurs<select class=\"inp-s\" id=\"kCourse\"><option value=\"\">Wszystkie kursy (subskrypcja)</option>", "<label class=\"fl\" for=\"kN\">Кількість<input class=\"inp-s\" id=\"kN\" type=\"number\" min=\"1\" max=\"100\" value=\"5\"></label><div style=\"align-self:end\"><button class=\"btn btn-red\" type=\"submit\">Створити</button></div></div><div id=\"kNew\"></div></form>": "<label class=\"fl\" for=\"kN\">Ilość<input class=\"inp-s\" id=\"kN\" type=\"number\" min=\"1\" max=\"100\" value=\"5\"></label><div style=\"align-self:end\"><button class=\"btn btn-red\" type=\"submit\">Utwórz</button></div></div><div id=\"kNew\"></div></form>", "<div class=\"tbl-wrap\"><table class=\"tbl\"><thead><tr><th>Ключ</th><th>Курс</th><th>Створено</th><th>Статус</th><th></th></tr></thead><tbody>": "<div class=\"tbl-wrap\"><table class=\"tbl\"><thead><tr><th>Klucz</th><th>Kurs</th><th>Utworzono</th><th>Status</th><th></th></tr></thead><tbody>", "Усі курси": "Wszystkie kursy", "<span class=\"pill ok\">активовано</span><br><span class=\"muted small\">": "<span class=\"pill ok\">aktywowany</span><br><span class=\"muted small\">", "<span class=\"pill warn\">вільний</span>": "<span class=\"pill warn\">wolny</span>", "\">Копіювати</button> <button class=\"btn btn-danger btn-sm\" type=\"button\" data-kdel=\"": "\">Kopiuj</button> <button class=\"btn btn-danger btn-sm\" type=\"button\" data-kdel=\"", "\">Видалити</button>": "\">Usuń</button>", "Створено ключів: ": "Utworzono kluczy: ", "<p class=\"muted small\" style=\"margin-top:10px\">Нові ключі:</p><pre style=\"font-family:var(--f-mono);color:var(--neon);white-space:pre-wrap;user-select:all\">": "<p class=\"muted small\" style=\"margin-top:10px\">Nowe klucze:</p><pre style=\"font-family:var(--f-mono);color:var(--neon);white-space:pre-wrap;user-select:all\">", "Скопійовано: ": "Skopiowano: ", "Ключ: ": "Klucz: ", "Точно?": "Na pewno?", "Ключ видалено": "Klucz usunięty", "Надзаголовок головної": "Nadtytuł strony głównej", "Заголовок, слово 1": "Nagłówek, słowo 1", "Заголовок, слово 2": "Nagłówek, słowo 2", "Заголовок, слово 3": "Nagłówek, słowo 3", "Опис під заголовком": "Opis pod nagłówkiem", "Тариф 1: назва": "Pakiet 1: nazwa", "Тариф 1: ціна": "Pakiet 1: cena", "Тариф 1: пункти (кожен з нового рядка)": "Pakiet 1: punkty (każdy w nowej linii)", "Тариф 2: назва": "Pakiet 2: nazwa", "Тариф 2: ціна": "Pakiet 2: cena", "Тариф 2: пункти": "Pakiet 2: punkty", "Тариф 3: назва": "Pakiet 3: nazwa", "Тариф 3: ціна": "Pakiet 3: cena", "Тариф 3: пункти": "Pakiet 3: punkty", "Як купити ключ (текст на сторінці покупки)": "Jak kupić klucz (tekst na stronie zakupu)", "FAQ: кожен рядок «Питання|Відповідь»": "FAQ: każda linia „Pytanie|Odpowiedź”", "<form class=\"panel form\" id=\"sForm\" novalidate><h3>Тексти на сайті</h3><p class=\"muted small\">Зміни одразу з'являться на головній, у тарифах і FAQ.</p>": "<form class=\"panel form\" id=\"sForm\" novalidate><h3>Teksty na stronie</h3><p class=\"muted small\">Zmiany od razu pojawią się na stronie głównej, w cenniku i FAQ.</p>", "<div class=\"row\"><button class=\"btn btn-red\" type=\"submit\">Зберегти зміни</button><a class=\"btn btn-ghost btn-sm\" href=\"#/\">Переглянути сайт</a></div></form>": "<div class=\"row\"><button class=\"btn btn-red\" type=\"submit\">Zapisz zmiany</button><a class=\"btn btn-ghost btn-sm\" href=\"#/\">Zobacz stronę</a></div></form>", "Тексти сайту збережено": "Teksty strony zapisane", "<div class=\"page\"><div class=\"empty\">Сторінку не знайдено. <a href=\"#/\">На головну</a></div></div>": "<div class=\"page\"><div class=\"empty\">Nie znaleziono strony. <a href=\"#/\">Na stronę główną</a></div></div>", "<div class=\"page\"><div class=\"empty\">Помилка: ": "<div class=\"page\"><div class=\"empty\">Błąd: ", "<div class=\"page\"><p class=\"muted\">Завантаження…</p></div>": "<div class=\"page\"><p class=\"muted\">Ładowanie…</p></div>", "Озвучення недоступне в цьому браузері": "Odsłuch niedostępny w tej przeglądarce"};
var I18N_EN = {"Zadania": "Tasks", "%. Pierwszy wynik zostaje, nowy pokazujemy w nawiasie.": "%. Your first score stays; the new one is shown in brackets.", "%. Wynik zapisany na Twoim koncie.": "%. Saved to your account.", "%. Załóż konto, aby zapisywać postępy.": "%. Create an account to save your progress.", " (minimum 6 znaków)": " (at least 6 characters)", "0 słów": "0 words", "15 min": "15 min", "6 typów": "6 types", "Kup klucz · ": "Buy a key · ", "Kup klucz": "Buy a key", "Do maratonu": "Back to the marathon", "Następna lekcja": "Next lesson", "Admin: wył.": "Admin: off", "Admin: wł.": "Admin: on", "Aktywuj go na swoim koncie.": "Activate it in your account.", "Aktywuj klucz": "Activate a key", "Aktywujesz": "You activate it", "Aktywuj": "Activate", "Brak ukończonych lekcji": "No lessons completed yet", "Brzmi dobrze": "Sounds good", "Błąd logowania: ": "Login error: ", "Błąd: ": "Error: ", "Błędów: ": "Mistakes: ", "Cennik": "Pricing", "Chwileczkę…": "One moment…", "Ciemny motyw": "Dark theme", "Cześć, ": "Hi, ", "Dalej": "Next", "Darmowa lekcja próbna": "Free trial lesson", "Demo: admin admin@movielang.demo / admin123, uczeń olena@example.com / demo123": "Demo: admin admin@movielang.demo / admin123, student olena@example.com / demo123", "Do katalogu": "Back to catalogue", "Dobry start! Pełny maraton pomoże to utrwalić.": "Good start! The full marathon will help you lock it in.", "Dobrze! ": "Correct! ", "Dwa maratony": "Two marathons", "E-mail niepotwierdzony. Otwórz wiadomość od Supabase, kliknij link, a potem się zaloguj.": "Email not confirmed. Open the email we sent, click the link, then log in.", "E-mail potwierdzony! Teraz się zaloguj.": "Email confirmed! Now log in.", "E-mail potwierdzony! Witamy w MoviLang.": "Email confirmed! Welcome to MoviLang.", "SERIAL": "SERIES", "FILM": "FILM", "Fałsz": "False", "Filmy i seriale": "Films & series", "Hasło musi mieć co najmniej 6 znaków.": "The password must have at least 6 characters.", "Hasło": "Password", "Imię": "Name", "Jak to działa": "How it works", "Jak zdobyć klucz dostępu": "How to get an access key", "Jasny motyw": "Light theme", "lekcji czeka na Ciebie:": "lessons are waiting for you:", "lekcji, projekt końcowy i certyfikat": "lessons, a final project and a certificate", "Jeszcze raz": "Again", "Jeszcze": "Another", "Katalog kursów": "Course catalogue", "Katalog": "Catalogue", "Klikaj słowa w odpowiedniej kolejności…": "Tap the words in the right order…", "Klucz aktywowany! Maraton odblokowany.": "Key activated! The marathon is unlocked.", "Klucz demo: ": "Demo key: ", "Klucz musi mieć 12 znaków.": "The key must have 12 characters.", "Konto utworzone! Sprawdź skrzynkę (i folder „Spam”), kliknij link z wiadomości, a potem się zaloguj.": "Account created! Check your inbox (and the spam folder), click the link in the email, then log in.", "Konto utworzone!": "Account created!", "Konto": "Account", "Kupujesz klucz": "You buy a key", "Lekcja próbna pojawi się, gdy zostanie utworzony pierwszy kurs.": "The trial lesson will appear once the first course is created.", "Lekcja próbna": "Trial lesson", "Lekcje oparte na scenach z filmu.": "Lessons built on scenes from the film.", "Lekcje tego maratonu pojawią się wkrótce.": "Lessons for this marathon are coming soon.", "Link jest nieważny lub wygasł. Zaloguj się lub zarejestruj ponownie.": "The link is invalid or expired. Log in or sign up again.", "Logowanie": "Log in", "Maraton ukończony": "Marathon completed", "Maraton": "Marathon", "Masz już klucz?": "Already have a key?", "Masz już konto? ": "Already have an account? ", "Masz zadania bez odpowiedzi": "Some tasks are still unanswered", "Moje konto": "My account", "Moje maratony": "My marathons", "Mów po angielsku…": "Speak now…", "NAJPOPULARNIEJSZY": "MOST POPULAR", "Na razie brak kursów. Administrator może je dodać w panelu admina.": "No courses yet.", "Na stronę główną": "Go to the home page", "Naciśnij i mów": "Press and speak", "Najpierw zaloguj się na konto": "Please log in first", "Napisz co najmniej ": "Write at least ", "Nic nie usłyszano. Spróbuj ponownie.": "Nothing was heard. Try again.", "Nie masz jeszcze konta? ": "No account yet? ", "Nie masz jeszcze maratonów. Aktywuj klucz albo ": "No marathons yet. Activate a key or ", "Nie udało się rozpoznać. Spróbuj ponownie.": "Couldn't recognise that. Try again.", "Nie znaleziono kursu. ": "Course not found. ", "Nie znaleziono lekcji.": "Lesson not found.", "Nie znaleziono strony. ": "Page not found. ", "Nie znaleziono takiego klucza. Sprawdź litery O i 0, I i 1.": "Key not found. Check the letters O and 0, I and 1.", "Nieprawidłowy e-mail lub hasło": "Wrong email or password", "Nowe konto": "New account", "Od biletu do pierwszej rozmowy": "From ticket to your first conversation", "Odpowiedź już udzielona. Aby ją zmienić, przejdź lekcję ponownie.": "Already answered. To change it, take the lesson again.", "Odpowiedź zapisana! ": "Answer saved! ", "Odpowiedź: ": "Answer: ", "Odsłuch niedostępny w tej przeglądarce": "Audio isn't available in this browser", "Odsłuchaj": "Listen", "Osiągnięcia": "Achievements", "Ostatnie lekcje": "Recent lessons", "Otwierasz maraton": "You open the marathon", "Pierwsza lekcja": "First lesson", "Pisz po angielsku…": "Write in the language you're learning…", "Pięć lekcji": "Five lessons", "Podaj swoje imię.": "Enter your name.", "Pokaż wynik": "Show result", "Pomiń": "Skip", "Ponowna próba: ": "Retake: ", "Poprawnie: ": "Correct: ", "Porównaj z wzorem (przycisk „Odsłuchaj”) i oceń się.": "Compare with the model (Listen button) and rate yourself.", "Posłuchaj i powtórz na głos": "Listen and repeat out loud", "Posłuchaj i wybierz odpowiedź": "Listen and choose the answer", "Powiedziałem(-am) to na głos": "I said it out loud", "Połącz angielskie słowa z tłumaczeniem": "Match the words with their meanings", "Prawda czy fałsz?": "True or false?", "Prawda": "True", "Prawie! Spróbuj jeszcze raz albo zalicz.": "Almost! Try again or accept it.", "Prawie. ": "Almost. ", "Przejdź do konta": "Go to my account", "Przejdź jeszcze raz": "Take it again", "Pytania i odpowiedzi": "Questions & answers", "Pytanie o fabułę": "Plot question", "Rejestracja": "Sign up", "Scena:": "Scene:", "Sprawdź": "Check", "Spróbuj jeszcze raz, mów wyraźniej.": "Try again and speak more clearly.", "Statystyki i punkty na koncie.": "Stats and points in your account.", "Strona główna": "Home", "Słucham…": "Listening…", "Słówka, audio, napisy, gramatyka, mówienie.": "Vocabulary, audio, subtitles, grammar, speaking.", "Ta lekcja nie ma jeszcze zadań.": "This lesson has no tasks yet.", "Ta lekcja odblokuje się po aktywacji klucza. ": "This lesson unlocks after you activate a key. ", "Trafność 90%+": "Accuracy 90%+", "Trzy dni nauki": "Three days of learning", "Twoja odpowiedź": "Your answer", "Twoja przeglądarka nie obsługuje mikrofonu. Powtórz na głos i kliknij „Pomiń”.": "Your browser doesn't support the microphone. Say it out loud and press Skip.", "Typy zadań w kursie": "Task types in this course", "Uzupełnij lukę w napisach": "Fill the gap in the subtitles", "Ułóż zdanie z podanych słów": "Build the sentence from the words", "Użytkownik z tym adresem e-mail już istnieje": "A user with this email already exists", "WKRÓTCE": "SOON", "WYNIK": "RESULT", "Widzisz postępy": "You see your progress", "Widzisz stronę jak uczeń": "You see the site as a student", "Witaj ponownie!": "Welcome back!", "Wpisujesz kod na swoim koncie.": "You enter the code in your account.", "Wpisz brakujące słowo po angielsku": "Type the missing word", "Wpisz poprawny e-mail, np. name@gmail.com": "Enter a valid email, e.g. name@gmail.com", "Wybierasz film, pakiet lub subskrypcję.": "Pick a film, a bundle or a subscription.", "Wybierz poprawną formę": "Choose the correct form", "Wybierz swój bilet": "Choose your ticket", "Wybierz właściwe słowo": "Choose the right word", "Wyczyść": "Clear", "Wykonujesz zadania": "You do the tasks", "Wylogowano": "Logged out", "Wyloguj": "Log out", "Wynik: ": "Score: ", "Zadania po angielsku · wskazówki": "Tasks in the target language · hints", "Zadanie końcowe": "Final task", "Zakup klucza": "Buy a key", "Zalicz tę próbę": "Accept this attempt", "Zaliczono: ": "Accepted: ", "Zalogowano": "Logged in", "Zaloguj się na konto": "Log in to your account", "Zaloguj się": "Log in", "Zapisz odpowiedź": "Save answer", "Zarejestruj się": "Sign up", "Zatrzymaj": "Stop", "Załóż konto": "Create account", "Załóż swoje konto": "Create your account", "Zdobądź klucz dostępu": "Get an access key", "Zezwól przeglądarce na dostęp do mikrofonu.": "Allow microphone access in your browser.", "aktywowany": "activated", "dni nauki": "days of learning", "dostęp odblokowany": "access unlocked", "dziennie": "per day", "jednorazowo · dostęp na 12 miesięcy": "one-off · 12 months of access", "kursów": "courses", "maratonów": "marathons", "przejdź lekcję próbną": "try the trial lesson", "słów": "words", "ukończonych lekcji": "lessons completed", "zadań": "tasks", "zdobytych XP": "XP earned", " · za darmo": " · free", "Ładowanie…": "Loading…", "Świetna wymowa!": "Great pronunciation!", "Świetnie! Jesteś gotowy na cały maraton.": "Great! You're ready for the full marathon.", "średni wynik": "average score", "Wskazówki po polsku, zadania po angielsku": "Hints in your language, tasks in the target language", "Serial": "Series", "serial": "series", "film": "film", "lekcji": "lessons", "Lekcja": "Lesson", "Zadanie ": "Task ", "Film": "Film", "Cześć,": "Hi,", "Wynik:": "Score:", "Błąd:": "Error:", "min": "min", "z": "of", "E-mail": "Email", "Statystyki": "Statistics", "Poziom": "Level", "Lekcje": "Lessons", "← Do kursu": "← Back to course", "← Wszystkie kursy": "← All courses", "✓ Powtórzyłem(-am)": "✓ I repeated it", "Pełny kurs: 16 lekcji B1–B2": "Full course: 16 lessons B1–B2", "Nie ma jeszcze kursów.": "No courses yet.", "Ten klucz został już aktywowany.": "This key has already been activated.", "Napisz co najmniej 20 słów (teraz": "Write at least 20 words (now", "Masz już konto?": "Already have an account?", "Nie masz jeszcze konta?": "No account yet?", "Kup klucz ·": "Buy a key ·", "Nie znaleziono kursu.": "Course not found.", "Nie znaleziono strony.": "Page not found.", "Nieprawidłowy e-mail lub hasło.": "Wrong email or password.", "Nie masz jeszcze maratonów. Aktywuj klucz albo": "No marathons yet. Activate a key or", "Klucz": "Key", "Kurs": "Course", "Opis": "Description", "Panel admina": "Admin panel", "Tryb administratora": "Admin mode", "Wszystkie kursy": "All courses", "Wszystkie kursy (subskrypcja)": "All courses (subscription)", "Użytkownicy": "Users", "Kursy": "Courses", "Połącz słowa z tłumaczeniem": "Match the words with their meanings", "Wpisz brakujące słowo": "Type the missing word", "Pisz w języku, którego się uczysz…": "Write in the language you're learning…", "Mów…": "Speak now…", "Język nauki": "Language you learn", "Język zadań i wyjaśnień": "Language of tasks & explanations", "Wybierz języki": "Choose your languages", "Zapisz": "Save", "Uczysz się:": "You learn:", "Ta lekcja nie jest jeszcze dostępna w wybranym języku. Wkrótce!": "This lesson isn't available in the chosen language yet. Coming soon!", "Uczę się": "I learn", "Wskazówki": "Hints", "angielski": "English", "polski": "Polish", "ukraiński": "Ukrainian", "Zmień": "Change", "Wkrótce w tym języku": "Coming soon in this language"};
var LANGS = ['en','pl','uk'], LANG = 'uk', TARGET = 'en', LANG_SET = false;
var NAV_L = (navigator.language || '').slice(0, 2);
try { LANG = localStorage.getItem('ml_lang') || (NAV_L === 'pl' ? 'pl' : NAV_L === 'uk' ? 'uk' : NAV_L === 'en' ? 'en' : 'uk'); TARGET = localStorage.getItem('ml_target') || 'en'; LANG_SET = !!localStorage.getItem('ml_target'); } catch (e) {}
if (LANGS.indexOf(LANG) < 0) LANG = 'uk'; if (LANGS.indexOf(TARGET) < 0) TARGET = 'en';
var SPEECH = {en:'en-GB', pl:'pl-PL', uk:'uk-UA'}, FLAG = {en:'EN', pl:'PL', uk:'UA'};
var T_CACHE = {};
function enSeg(p) { if (I18N_EN[p] != null) return I18N_EN[p]; return p.split(/(<[^>]+>)/).map(function (seg) { if (!seg || seg.charAt(0) === '<') return seg; var m = seg.match(/^(\s*)([\s\S]*?)(\s*)$/); var k = m[2], q = k.lastIndexOf('">'); if (I18N_EN[k] != null) return m[1] + I18N_EN[k] + m[3]; if (q > -1 && I18N_EN[k.slice(q + 2)] != null) return m[1] + k.slice(0, q + 2) + I18N_EN[k.slice(q + 2)] + m[3]; return seg; }).join(''); }
function t(s) {
  if (LANG === 'pl') return I18N_PL[s] != null ? I18N_PL[s] : s;
  if (LANG === 'en') { if (T_CACHE[s] != null) return T_CACHE[s]; var p = I18N_PL[s]; return (T_CACHE[s] = p == null ? s : enSeg(p)); }
  return s;
}
function langName(l) { return t({en:'англійська', pl:'польська', uk:'українська'}[l]); }
function setLang(l) { LANG = l; try { localStorage.setItem('ml_lang', l); } catch (e) {} applyStatic(); renderNav(); route(); }
function setLangs(target, sup) { TARGET = target; LANG = sup; LANG_SET = true; try { localStorage.setItem('ml_target', target); localStorage.setItem('ml_lang', sup); } catch (e) {} applyStatic(); renderNav(); route(); }
function lGram(l) { var v = l.variants; if (TARGET === 'en' && v && v['grammar_' + LANG]) return v['grammar_' + LANG]; return (TARGET !== 'en' && v && (v[TARGET + '_grammar_' + LANG] || v[TARGET + '_grammar'])) || l.grammar; }
var CAB_T = null, LAST_TIMES = null;
function tx(o) { return o[LANG] || o.uk; }
function mbox(html) { var old = document.getElementById('mBox'); if (old) old.remove(); var w = document.createElement('div'); w.id = 'mBox'; w.className = 'lmodal'; w.innerHTML = '<div class="lbox" role="dialog" aria-modal="true">' + html + '</div>'; w.onclick = function (e) { if (e.target === w) w.remove(); }; document.body.appendChild(w); return w; }
function pickTargetModal(title, exclude, cb) {
  var opts = LANGS.filter(function (l) { return (exclude || []).indexOf(l) < 0; });
  var w = mbox('<h3>' + esc(title) + '</h3><div class="lrow" style="margin-top:14px">' + opts.map(function (l) { return '<button type="button" class="lopt" data-pk="' + l + '"><b>' + FLAG[l] + '</b><span>' + esc(langName(l)) + '</span></button>'; }).join('') + '</div>');
  w.querySelectorAll('[data-pk]').forEach(function (b) { b.onclick = function () { w.remove(); cb(b.dataset.pk); }; });
}
function removeLangFlow(c, tg, langsOfCourse, lessonIds) {
  var name = esc(tr(c, 'title')), ln = esc(langName(tg));
  if (langsOfCourse.length > 1) {
    var w = mbox('<h3>' + tx({uk:'Точно видалити результати?', pl:'Na pewno usunąć wyniki?', en:'Delete your results?'}) + '</h3><p class="muted">' + tx({uk:'Мова «' + ln + '» у марафоні «' + name + '». Ти вже почав(-ла), а кожен урок наближає до мети. Ми в тебе віримо, ще кілька сцен, і буде результат! 💪', pl:'Język „' + ln + '” w maratonie „' + name + '”. Już zacząłeś(-ęłaś), a każda lekcja przybliża cię do celu. Wierzymy w ciebie, jeszcze kilka scen i będzie efekt! 💪', en:'“' + ln + '” in “' + name + '”. You\'ve already started, and every lesson gets you closer. We believe in you: a few more scenes and you\'ll see results! 💪'}) + '</p><div class="row" style="justify-content:flex-end;margin-top:16px;gap:8px"><button class="btn btn-ghost btn-sm" type="button" id="mDel">' + tx({uk:'Так, видалити', pl:'Tak, usuń', en:'Yes, delete'}) + '</button><button class="btn btn-red" type="button" id="mStay">' + tx({uk:'Залишаюсь і вчуся', pl:'Zostaję i się uczę', en:'I\'ll keep learning'}) + '</button></div>');
    w.querySelector('#mStay').onclick = function () { w.remove(); toast(tx({uk:'Так тримати! 🎬', pl:'Tak trzymaj! 🎬', en:'That\'s the spirit! 🎬'})); };
    w.querySelector('#mDel').onclick = function () { API.removeLang(c.id, tg).then(function () { w.remove(); toast(tx({uk:'Результати видалено', pl:'Wyniki usunięte', en:'Results deleted'})); route(); }).catch(function (e) { toast(e.message, 'err'); }); };
    return;
  }
  var w1 = mbox('<h3>' + tx({uk:'Цю мову не можна анулювати', pl:'Tego języka nie można anulować', en:'This language can\'t be removed'}) + '</h3><p class="muted">' + tx({uk:'У марафоні має бути розпочата хоча б одна мова. Можна лише видалити весь марафон «' + name + '» з кабінету.', pl:'W maratonie musi być rozpoczęty co najmniej jeden język. Możesz tylko usunąć cały maraton „' + name + '” z konta.', en:'A marathon needs at least one started language. You can only remove the whole marathon “' + name + '” from your account.'}) + '</p><div class="row" style="justify-content:flex-end;margin-top:16px;gap:8px"><button class="btn btn-red" type="button" id="mKeep">' + tx({uk:'Залишити', pl:'Zostaw', en:'Keep it'}) + '</button><button class="btn btn-ghost btn-sm" type="button" id="mNext">' + tx({uk:'Видалити весь марафон', pl:'Usuń cały maraton', en:'Remove the whole marathon'}) + '</button></div>');
  w1.querySelector('#mKeep').onclick = function () { w1.remove(); };
  w1.querySelector('#mNext').onclick = function () {
    var w2 = mbox('<h3>' + tx({uk:'Ти впевнений(-а)?', pl:'Jesteś pewien(-na)?', en:'Are you sure?'}) + '</h3><p class="muted">' + tx({uk:'Марафон зникне з кабінету разом з усіма результатами і доступом. Це не можна скасувати.', pl:'Maraton zniknie z konta razem ze wszystkimi wynikami i dostępem. Tego nie można cofnąć.', en:'The marathon will disappear from your account with all results and access. This can\'t be undone.'}) + '</p><div class="row" style="justify-content:flex-end;margin-top:16px;gap:8px"><button class="btn btn-red" type="button" id="mKeep2">' + tx({uk:'Ні, залишити', pl:'Nie, zostaw', en:'No, keep it'}) + '</button><button class="btn btn-ghost btn-sm" type="button" id="mNext2">' + tx({uk:'Так, далі', pl:'Tak, dalej', en:'Yes, continue'}) + '</button></div>');
    w2.querySelector('#mKeep2').onclick = function () { w2.remove(); };
    w2.querySelector('#mNext2').onclick = function () {
      var phrase = tx({uk:'так, хочу', pl:'tak, chcę', en:'yes, I want'});
      var w3 = mbox('<h3>' + tx({uk:'Останній крок', pl:'Ostatni krok', en:'Last step'}) + '</h3><p class="muted">' + tx({uk:'Щоб підтвердити, введи:', pl:'Aby potwierdzić, wpisz:', en:'To confirm, type:'}) + ' <b>' + esc(phrase) + '</b></p><input class="inp-s" id="mPhrase" autocomplete="off" style="width:100%;margin-top:10px"><div class="row" style="justify-content:flex-end;margin-top:16px;gap:8px"><button class="btn btn-ghost btn-sm" type="button" id="mCancel">' + tx({uk:'Скасувати', pl:'Anuluj', en:'Cancel'}) + '</button><button class="btn btn-danger btn-sm" type="button" id="mFinal" disabled>' + tx({uk:'Видалити марафон', pl:'Usuń maraton', en:'Remove marathon'}) + '</button></div>');
      var inp = w3.querySelector('#mPhrase'), fb = w3.querySelector('#mFinal'); inp.focus();
      var normP = function (s) { return s.toLowerCase().replace(/[^\p{L}\s]/gu, '').replace(/\s+/g, ' ').trim(); };
      inp.oninput = function () { fb.disabled = normP(inp.value) !== normP(phrase); };
      w3.querySelector('#mCancel').onclick = function () { w3.remove(); };
      fb.onclick = function () { API.removeCourse(c.id, langsOfCourse).then(function () { w3.remove(); toast(tx({uk:'Марафон видалено з кабінету', pl:'Maraton usunięty z konta', en:'Marathon removed'})); route(); }).catch(function (e) { toast(e.message, 'err'); }); };
    };
  };
}
function lessonTasks(l) { if (TARGET === 'en') return l.tasks || []; var v = l.variants && l.variants[TARGET]; return v && v.length ? v : null; }
function langModal(first) {
  var old = document.getElementById('langModal'); if (old) old.remove();
  var tg = TARGET, sp = LANG, w = document.createElement('div'); w.id = 'langModal'; w.className = 'lmodal';
  function opts(cur, attr) { return LANGS.map(function (l) { return '<button type="button" class="lopt' + (l === cur ? ' on' : '') + '" data-' + attr + '="' + l + '"><b>' + FLAG[l] + '</b><span>' + esc(langName(l)) + '</span></button>'; }).join(''); }
  function draw() { w.innerHTML = '<div class="lbox" role="dialog" aria-modal="true"><h3>' + t('Обери мови') + '</h3><div class="llabel">🎬 ' + t('Мова навчання') + '</div><div class="lrow">' + opts(tg, 'lt') + '</div><div class="llabel">💬 ' + t('Мова завдань і пояснень') + '</div><div class="lrow">' + opts(sp, 'ls') + '</div><div class="row" style="justify-content:flex-end;margin-top:18px"><button class="btn btn-red" type="button" id="lSave">' + t('Зберегти') + '</button></div></div>';
    w.querySelectorAll('[data-lt]').forEach(function (b) { b.onclick = function () { tg = b.dataset.lt; draw(); }; });
    w.querySelectorAll('[data-ls]').forEach(function (b) { b.onclick = function () { sp = b.dataset.ls; draw(); }; });
    w.querySelector('#lSave').onclick = function () { w.remove(); setLangs(tg, sp); }; }
  draw(); w.onclick = function (e) { if (e.target === w && !first) w.remove(); };
  document.body.appendChild(w);
}
var THEME = 'dark';
try { THEME = localStorage.getItem('ml_theme') || 'dark'; } catch (e) {}
function applyTheme() { document.documentElement.setAttribute('data-theme', THEME); }
function toggleTheme() { THEME = THEME === 'dark' ? 'light' : 'dark'; try { localStorage.setItem('ml_theme', THEME); } catch (e) {} applyTheme(); renderNav(); }
applyTheme();
function applyStatic() {
  document.documentElement.lang = LANG;
  var sl = tx({uk:'МОВИ ЧЕРЕЗ КІНО', pl:'JĘZYKI PRZEZ KINO', en:'LANGUAGES THROUGH CINEMA'}); var lg = document.querySelector('.logo small'); if (lg) lg.textContent = sl; var fs = document.getElementById('footSlogan'); if (fs) fs.textContent = '© 2026 MoviLang · ' + sl.charAt(0) + sl.slice(1).toLowerCase();
  var d = document.getElementById('discl'); if (d) d.textContent = LANG === 'pl' ? 'Tytuły filmów i seriali służą do opisu treści kursów; projekt nie jest powiązany z właścicielami praw.' : "Назви фільмів і серіалів використано для опису змісту курсів; проєкт не пов'язаний із правовласниками.";
  var b = document.getElementById('demoBar'); if (b) b.textContent = LANG === 'pl' ? 'Tryb demo: dane zapisują się tylko w tej przeglądarce. Admin: admin@movielang.demo / admin123' : 'Демо-режим: дані зберігаються лише в цьому браузері. Адмін: admin@movielang.demo / admin123';
}
function tr(o, k) { if (!o) return ''; if (LANG === 'pl' && o[k + '_pl']) return o[k + '_pl']; if (LANG === 'en') return o[k + '_en'] || o[k + '_pl'] || o[k]; return o[k]; }

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

var EN_SETTINGS = {hero_eyebrow:'Online language marathons · EN · PL · UA', hero_w1:'Watch.', hero_w2:'Understand.', hero_w3:'Speak.', hero_lead:'Learn English, Polish or Ukrainian through scenes from films and series. Pick the language you learn and the language of your hints, open a marathon and do short daily tasks: words from the scene, listening, subtitles with gaps, grammar and speaking.', plan1_name:'One film', plan1_text:'1 marathon of your choice\n7–10 lessons\nGlossary and flashcards\nCertificate after the final', plan2_name:'Film bundle', plan2_text:'3 marathons of your choice\nSpeaking tasks reviewed\nExtended glossary with audio\nKey can be given as a gift', plan3_name:'Subscription', plan3_price:'59 zł / month', plan3_text:'All marathons in the catalogue\nNew marathons every month\nOnline conversation club\nCancel in one click', buy_info:'To buy a key, write to us: info.movielang@gmail.com — the key arrives by email within an hour.', faq:'Do I need the film itself?|No. Lessons include scene descriptions and learning audio, and we create all tasks ourselves.\nWhich languages can I learn?|English, Polish and Ukrainian. Hints and explanations can be in any of the three.\nWhat is an access key?|A personal 12-character code. Enter it in your account to unlock a marathon.\nHow long is a lesson?|10–15 minutes.'};
function LS() { var o = {}; for (var k in DEFAULT_SETTINGS) { if (/_(pl|en)$/.test(k)) continue; var v = SETTINGS[k]; if (LANG === 'pl' && SETTINGS[k + '_pl']) v = SETTINGS[k + '_pl']; if (LANG === 'en') v = SETTINGS[k + '_en'] || EN_SETTINGS[k] || SETTINGS[k + '_pl'] || v; o[k] = v; } return o; }

/* ================= default content ================= */
var DEFAULT_SETTINGS = {
  theme_custom: '', theme_presets: '', theme_default: '',
  hero_eyebrow: 'Онлайн-марафони мов · EN · PL · UA',
  hero_w1: 'Дивись.', hero_w2: 'Розумій.', hero_w3: 'Говори.',
  hero_lead: 'Вчи англійську, польську чи українську на сценах з улюблених фільмів і серіалів. Обери мову навчання і мову підказок, відкрий марафон і щодня проходь короткі завдання: слова зі сцени, аудіювання, субтитри з пропусками, граматику і говоріння.',
  plan1_name: 'Один фільм', plan1_price: '49 zł', plan1_text: '1 марафон на вибір\n7–10 уроків\nСловник і картки\nСертифікат після фіналу',
  plan2_name: 'Пакет фільмів', plan2_price: '119 zł', plan2_text: '3 марафони на вибір\nПеревірка speaking-завдань\nРозширений словник з аудіо\nКлюч можна подарувати',
  plan3_name: 'Підписка', plan3_price: '59 zł / міс', plan3_text: 'Усі марафони каталогу\nНові марафони щомісяця\nРозмовний клуб онлайн\nСкасування в один клік',
  buy_info: 'Щоб купити ключ, напишіть нам: info.movielang@gmail.com — ключ надійде на пошту протягом години.',
  faq: 'Чи потрібно мати сам фільм?|Ні. Уроки містять опис сцен і навчальні аудіо, а всі завдання ми створюємо самі.\nЯкий рівень англійської потрібен?|Від A2. Кожен марафон має позначку рівня, а пояснення граматики написані українською.\nЩо таке ключ доступу?|Персональний код з 12 символів. Введи його в кабінеті, і марафон відкриється.\nСкільки часу займає урок?|10–15 хвилин. Прогрес зберігається після кожного уроку.\nЧи можна подарувати ключ?|Так. Ключ не прив\'язаний до покупця, доки його не активовано.',
  hero_eyebrow_pl: 'Maratony językowe online · EN · PL · UA',
  hero_w1_pl: 'Oglądaj.', hero_w2_pl: 'Rozumiej.', hero_w3_pl: 'Mów.',
  hero_lead_pl: 'Ucz się angielskiego, polskiego lub ukraińskiego na scenach z ulubionych filmów i seriali. Wybierz język nauki i język wskazówek, otwórz maraton i codziennie wykonuj krótkie zadania: słówka ze sceny, słuchanie, napisy z lukami, gramatykę i mówienie.',
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
    ttsList: function () { return P([]); }, token: function () { return P(null); },
    knownList: function (tg) { var u = me(); if (!u) return P([]); return P((load().known || []).filter(function (k) { return k.user_id === u.id && k.target === tg; })); },
    setKnown: function (tg, word, val) { var u = me(); var db = load(); db.known = (db.known || []).filter(function (k) { return !(k.user_id === u.id && k.target === tg && k.word === word); }); if (val) db.known.push({user_id:u.id, target:tg, word:word, known:true}); save(); return P(true); },
    saveWriting: function (w) { var u = me(); var db = load(); db.writings = db.writings || []; w.id = Date.now(); w.user_id = u.id; w.created_at = new Date().toISOString(); db.writings.push(w); save(); return P(w); },
    updateWriting: function (id, patch) { var db = load(); (db.writings || []).forEach(function (w) { if (w.id === id) for (var k in patch) w[k] = patch[k]; }); save(); return P(true); },
    myWritings: function () { var u = me(); if (!u) return P([]); return P((load().writings || []).filter(function (w) { return w.user_id === u.id; }).reverse()); },
    myLangs: function () { var u = me(); if (!u) return P([]); return P((load().elangs || []).filter(function (e) { return e.user_id === u.id; })); },
    addLang: function (cid, tg, hidden) { var u = me(); var db = load(); db.elangs = db.elangs || []; var e = db.elangs.filter(function (e) { return e.user_id === u.id && e.course_id === cid && e.target === tg; })[0]; if (e) e.hidden = !!hidden; else db.elangs.push({user_id:u.id, course_id:cid, target:tg, hidden:!!hidden}); save(); return P(true); },
    saveTimes: function (lessonId, score, tm) { var u = me(); if (!u) return P(false); var db = load(); db.times = db.times || []; db.times.push({user_id:u.id, lesson_id:lessonId, target:TARGET, score:score, total_sec:tm.total, per_task:tm.per, created_at:new Date().toISOString()}); save(); return P(true); },
    adminAnalytics: function () { needAdmin(); var db = load(); return P({courses:db.courses, lessons:db.lessons, progress:db.progress.filter(function (x) { return (x.target || 'en') === 'en'; }), progress_lang:db.progress.filter(function (x) { return (x.target || 'en') !== 'en'; }), times:db.times || [], elangs:db.elangs || []}); },
    adminUser: function (uid) { needAdmin(); var db = load(); var u = db.users.filter(function (x) { return x.id === uid; })[0] || {}; var pr = db.progress.filter(function (p) { return p.user_id === uid; }); return P({user:{id:u.id, email:u.email, name:u.name, role:u.role, created_at:u.created_at}, times:(db.times || []).filter(function (x) { return x.user_id === uid; }), progress:pr.filter(function (p) { return (p.target || 'en') === 'en'; }), progress_lang:pr.filter(function (p) { return (p.target || 'en') !== 'en'; }), lessons:db.lessons, courses:db.courses}); },
    adminTimes: function () { needAdmin(); var db = load(); return P({times:(db.times || []).slice().reverse(), users:db.users, lessons:db.lessons}); },
    adminSetProgress: function (lessonIds, tg, score) { var u = me(); var db = load(); lessonIds.forEach(function (lid) { var ex = db.progress.filter(function (p) { return p.user_id === u.id && p.lesson_id === lid && (p.target || 'en') === tg; })[0]; if (ex) { ex.score = score; ex.retry_score = null; } else db.progress.push({user_id:u.id, lesson_id:lid, target:tg, score:score, completed_at:new Date().toISOString()}); }); save(); return P(true); },
    adminResetOwn: function (lessonIds, tg) { var u = me(); var db = load(); db.progress = db.progress.filter(function (p) { return !(p.user_id === u.id && (p.target || 'en') === tg && lessonIds.indexOf(p.lesson_id) > -1); }); save(); return P(true); },
    removeLang: function (cid, tg) { return this.addLang(cid, tg, true); },
    removeCourse: function (cid, langs) { var self = this; var u = me(); langs.forEach(function (l) { self.addLang(cid, l, true); }); var db = load(); db.enrollments = db.enrollments.filter(function (e) { return !(e.user_id === u.id && e.course_id === cid); }); save(); return P(true); },
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
    myProgress: function (tg) { tg = tg || TARGET; var u = me(); if (!u) return P([]); return P(load().progress.filter(function (p) { return p.user_id === u.id && (p.target || 'en') === tg; })); },
    saveProgress: function (lessonId, score, answer) {
      var u = me(); if (!u) return P(false); var db = load();
      var ex = db.progress.filter(function (p) { return p.user_id === u.id && p.lesson_id === lessonId && (p.target || 'en') === TARGET; })[0];
      if (ex) { ex.retry_score = score; ex.retry_at = new Date().toISOString(); if (answer) ex.answer = answer; save(); return P({retry:true}); }
      db.progress.push({user_id:u.id, lesson_id:lessonId, target:TARGET, score:score, answer:answer || null, completed_at:new Date().toISOString()}); save(); return P({retry:false});
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
    mode:'supabase', sb:sb,
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
    saveLesson: function (l) { var row = {course_id:l.course_id, num:l.num, title:l.title, title_pl:l.title_pl || null, scene_pl:l.scene_pl || null, grammar:l.grammar}; if (l.title_en !== undefined) { row.title_en = l.title_en; row.scene_en = l.scene_en; } row = Object.assign(row, {scene:l.scene, tasks:l.tasks}); if (l.variants !== undefined) row.variants = l.variants; if (l.id) row.id = l.id; return sb.from('lessons').upsert(row).select().single().then(ok); },
    deleteLesson: function (id) { return sb.from('lessons').delete().eq('id', id).then(ok); },
    myEnrollments: function () { if (!cachedUser) return Promise.resolve([]); return sb.from('enrollments').select('course_id').eq('user_id', cachedUser.id).then(ok).then(function (r) { return r.map(function (x) { return x.course_id; }); }); },
    ttsList: function () { var out = []; function pg(o) { return sb.from('tts_clips').select('path').range(o, o + 999).then(function (r) { if (r.error) throw r.error; out = out.concat(r.data.map(function (x) { return x.path; })); return r.data.length === 1000 ? pg(o + 1000) : out; }); } return pg(0); },
    ttsAdd: function (row) { return sb.from('tts_clips').upsert(row).then(function (r) { if (r.error) throw r.error; }); },
    token: function () { return sb.auth.getSession().then(function (r) { return r.data.session && r.data.session.access_token; }); },
    knownList: function (tg) { if (!cachedUser) return Promise.resolve([]); return sb.from('word_known').select('word,known').eq('user_id', cachedUser.id).eq('target', tg).then(ok); },
    setKnown: function (tg, word, val) { if (!cachedUser) return Promise.resolve(false); var q = val ? sb.from('word_known').upsert({user_id:cachedUser.id, target:tg, word:word, known:true, updated_at:new Date().toISOString()}) : sb.from('word_known').delete().eq('user_id', cachedUser.id).eq('target', tg).eq('word', word); return q.then(ok); },
    saveWriting: function (w) { w.user_id = cachedUser.id; return sb.from('writings').insert(w).select().single().then(ok); },
    updateWriting: function (id, patch) { return sb.from('writings').update(patch).eq('id', id).then(ok); },
    myWritings: function () { if (!cachedUser) return Promise.resolve([]); return sb.from('writings').select('*').eq('user_id', cachedUser.id).order('created_at', {ascending:false}).limit(50).then(ok); },
    myLangs: function () { if (!cachedUser) return Promise.resolve([]); return sb.from('enrollment_langs').select('*').eq('user_id', cachedUser.id).then(ok); },
    addLang: function (cid, tg, hidden) { return sb.from('enrollment_langs').upsert({user_id:cachedUser.id, course_id:cid, target:tg, hidden:!!hidden}).then(ok); },
    saveTimes: function (lessonId, score, tm) { if (!cachedUser) return Promise.resolve(false); return sb.from('task_times').insert({user_id:cachedUser.id, lesson_id:lessonId, target:TARGET, score:score, total_sec:tm.total, per_task:tm.per}).then(ok); },
    adminAnalytics: function () { return Promise.all([sb.from('courses').select('*'), sb.from('lessons').select('*').order('num'), sb.from('progress').select('*'), sb.from('progress_lang').select('*'), sb.from('task_times').select('*').limit(5000), sb.from('enrollment_langs').select('*')]).then(function (r) { r.forEach(ok); return {courses:r[0].data, lessons:r[1].data, progress:r[2].data, progress_lang:r[3].data, times:r[4].data, elangs:r[5].data}; }); },
    adminUser: function (uid) { return Promise.all([sb.from('profiles').select('*').eq('id', uid).maybeSingle(), sb.from('task_times').select('*').eq('user_id', uid).order('created_at', {ascending:false}).limit(2000), sb.from('progress').select('*').eq('user_id', uid), sb.from('progress_lang').select('*').eq('user_id', uid), sb.from('lessons').select('id,num,title,title_pl,title_en,course_id'), sb.from('courses').select('id,title,title_pl,title_en')]).then(function (r) { r.forEach(ok); return {user:r[0].data, times:r[1].data || [], progress:r[2].data || [], progress_lang:r[3].data || [], lessons:r[4].data || [], courses:r[5].data || []}; }); },
    adminTimes: function () { return Promise.all([sb.from('task_times').select('*').order('created_at', {ascending:false}).limit(300), sb.from('profiles').select('id,name,email'), sb.from('lessons').select('id,num,title,title_pl,title_en,course_id')]).then(function (r) { r.forEach(ok); return {times:r[0].data, users:r[1].data, lessons:r[2].data}; }); },
    adminSetProgress: function (lessonIds, tg, score) { var uid = cachedUser.id, now = new Date().toISOString(); var rows = lessonIds.map(function (lid) { var x = {user_id:uid, lesson_id:lid, score:score, retry_score:null, completed_at:now}; if (tg !== 'en') x.target = tg; return x; }); return sb.from(tg === 'en' ? 'progress' : 'progress_lang').upsert(rows).then(ok); },
    adminResetOwn: function (lessonIds, tg) { var uid = cachedUser.id; return (tg === 'en' ? sb.from('progress').delete().eq('user_id', uid).in('lesson_id', lessonIds) : sb.from('progress_lang').delete().eq('user_id', uid).eq('target', tg).in('lesson_id', lessonIds)).then(ok); },
    removeLang: function (cid, tg) { return this.addLang(cid, tg, true); },
    removeCourse: function (cid, langs) { var uid = cachedUser.id; return sb.from('enrollment_langs').upsert(langs.map(function (l) { return {user_id:uid, course_id:cid, target:l, hidden:true}; })).then(ok).then(function () { return sb.from('enrollments').delete().eq('user_id', uid).eq('course_id', cid).then(ok); }); },
    activateKey: function (code) { return sb.rpc('activate_key', {p_code:code.trim().toUpperCase()}).then(ok); },
    myProgress: function (tg) { tg = tg || TARGET; if (!cachedUser) return Promise.resolve([]); var q = sb.from(tg === 'en' ? 'progress' : 'progress_lang').select('*').eq('user_id', cachedUser.id); if (tg !== 'en') q = q.eq('target', tg); return q.then(ok); },
    saveProgress: function (lessonId, score, answer) {
      if (!cachedUser) return Promise.resolve(false);
      var tb = TARGET === 'en' ? 'progress' : 'progress_lang', tg = TARGET;
      function f(q) { return tg === 'en' ? q : q.eq('target', tg); }
      return f(sb.from(tb).select('lesson_id').eq('user_id', cachedUser.id).eq('lesson_id', lessonId)).maybeSingle().then(function (r) {
        if (r.data) { var upd = {retry_score:score, retry_at:new Date().toISOString()}; if (answer) upd.answer = answer; return f(sb.from(tb).update(upd).eq('user_id', cachedUser.id).eq('lesson_id', lessonId)).then(ok).then(function () { return {retry:true}; }); }
        var row = {user_id:cachedUser.id, lesson_id:lessonId, score:score, answer:answer || null, completed_at:new Date().toISOString()}; if (tg !== 'en') row.target = tg;
        return sb.from(tb).insert(row).then(ok).then(function () { return {retry:false}; });
      });
    },
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
var cfg = window.MOVILANG_CONFIG || {};
var API = (cfg.SUPABASE_URL && cfg.SUPABASE_ANON_KEY && window.supabase) ? SupabaseBackend(cfg.SUPABASE_URL, cfg.SUPABASE_ANON_KEY) : DemoBackend();
/* ---- read cache: makes navigation instant after the first load ---- */
(function () {
  var C = {}, TTL = 5 * 60 * 1000, READS = {listCourses:1, getCourse:1, listLessons:1, getLesson:1, myEnrollments:1, myProgress:1, myLangs:1, getSettings:1};
  var keep = {getUser:1, mode:1, signIn:0};
  function memo(name, fn) { return function () { var k = name + '|' + JSON.stringify([].slice.call(arguments)) + (name === 'myProgress' && !arguments.length ? '|' + TARGET : ''), e = C[k];
    if (e && Date.now() - e.t < TTL) return e.p;
    var pr = fn.apply(API, arguments); C[k] = {t:Date.now(), p:pr}; pr.catch(function () { delete C[k]; }); return pr; }; }
  Object.keys(API).forEach(function (n) {
    if (typeof API[n] !== 'function') return; var fn = API[n];
    if (READS[n]) API[n] = memo(n, fn);
    else if (n !== 'getUser') API[n] = function () { C = {}; return fn.apply(API, arguments); };
  });
  var gl = API.getLesson, gc = API.getCourse;
  API.getLesson = function (id) { for (var k in C) if (k.indexOf('listLessons|') === 0 && C[k].done) { var l = C[k].done.filter(function (x) { return x.id === id; })[0]; if (l) return Promise.resolve(l); } return gl(id); };
  API.getCourse = function (id) { for (var k in C) if (k.indexOf('listCourses|') === 0 && C[k].done) { var c = C[k].done.filter(function (x) { return x.id === id; })[0]; if (c) return Promise.resolve(c); } return gc(id); };
  var ll = API.listLessons, lc = API.listCourses;
  API.listLessons = function (cid) { var p = ll(cid); var k = 'listLessons|' + JSON.stringify([cid]); p.then(function (r) { if (C[k]) C[k].done = r; }); return p; };
  API.listCourses = function (all) { var p = lc(all); var k = 'listCourses|' + JSON.stringify(all === undefined ? [] : [all]); p.then(function (r) { if (C[k]) C[k].done = r; }); return p; };
  API.clearCache = function () { C = {}; };
  API.prefetch = function () { API.listCourses(false).then(function (cs) { cs.forEach(function (c) { if (c.lessons_count) API.listLessons(c.id); }); }).catch(function () {}); };
})();
if (API.mode === 'demo') document.getElementById('demoBar').hidden = false;
var USER = null, SETTINGS = DEFAULT_SETTINGS;
var ADMIN_MODE = true; try { ADMIN_MODE = localStorage.getItem('ml_admin_mode') !== '0'; } catch (e) {}
function isAdm() { return !!(USER && USER.role === 'admin' && ADMIN_MODE); }
function setAdminMode(on) { ADMIN_MODE = on; try { localStorage.setItem('ml_admin_mode', on ? '1' : '0'); } catch (e) {} renderNav(); if (on) location.hash = '#/admin'; else if (/^#\/admin/.test(location.hash)) location.hash = '#/'; else route(); toast(on ? t('Режим адміністратора увімкнено') : t('Ти бачиш сайт як учень'), 'info'); }

var MI = {
  home:'<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/></svg>',
  cat:'<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 4v16M17 4v16M3 9h4M3 15h4M17 9h4M17 15h4"/></svg>',
  play:'<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M10 8.5l6 3.5-6 3.5z"/></svg>',
  user:'<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/></svg>',
  more:'<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'
};
function mActive() { var h = location.hash || '#/'; document.querySelectorAll('.mnav a[data-m]').forEach(function (a) { var m = a.dataset.m, on = m === '#/' ? (h === '#/' || h === '') : h.indexOf(m) === 0 || (m === '#/catalog' && h.indexOf('#/course') === 0) || (m === '#/trial' && h.indexOf('#/lesson') === 0); a.classList.toggle('on', on); }); }
function renderMobileNav() {
  var n = document.getElementById('mnav'); if (!n) { n = document.createElement('nav'); n.id = 'mnav'; n.className = 'mnav'; document.body.appendChild(n); window.addEventListener('hashchange', mActive); }
  var L = function (uk, pl, en) { return tx({uk:uk, pl:pl, en:en}); };
  n.innerHTML = '<a href="#/" data-m="#/">' + MI.home + '<span>' + L('Головна', 'Start', 'Home') + '</span></a>' +
    '<a href="#/catalog" data-m="#/catalog">' + MI.cat + '<span>' + L('Каталог', 'Katalog', 'Catalogue') + '</span></a>' +
    '<a href="#/trial" data-m="#/trial">' + MI.play + '<span>' + L('Урок', 'Lekcja', 'Lesson') + '</span></a>' +
    '<a href="' + (USER ? '#/cabinet' : '#/login') + '" data-m="' + (USER ? '#/cabinet' : '#/login') + '">' + MI.user + '<span>' + (USER ? L('Кабінет', 'Konto', 'Account') : L('Увійти', 'Zaloguj', 'Log in')) + '</span></a>' +
    '<button type="button" id="mMore">' + MI.more + '<span>' + L('Ще', 'Więcej', 'More') + '</span></button>';
  mActive();
  document.getElementById('mMore').onclick = function () {
    var adm = USER && USER.role === 'admin';
    var w = mbox('<div class="msheet">' + (USER ? '<div class="mrow muted small">' + esc(USER.name || '') + ' · ' + esc(USER.email || '') + '</div>' : '') +
      '<button type="button" class="mitemrow" id="msLang">🌐 ' + L('Мови', 'Języki', 'Languages') + '<b>🎬 ' + FLAG[TARGET] + ' · 💬 ' + FLAG[LANG] + '</b></button>' +
      '<button type="button" class="mitemrow" id="msTheme">' + (THEME === 'dark' ? '☀ ' + L('Світла тема', 'Jasny motyw', 'Light theme') : '☾ ' + L('Темна тема', 'Ciemny motyw', 'Dark theme')) + '</button>' +
      '<a class="mitemrow" href="#/guide">📘 ' + L('Посібник з граматики', 'Poradnik gramatyczny', 'Grammar guide') + '</a>' +
      (USER ? '<a class="mitemrow" href="#/words">📖 ' + L('Мій словник', 'Mój słownik', 'My words') + '</a>' : '') +
      '<a class="mitemrow" href="#/pricing">💳 ' + L('Тарифи', 'Cennik', 'Pricing') + '</a>' +
      (adm ? '<button type="button" class="mitemrow" id="msAdm">⚙ ' + L('Режим адміна', 'Tryb admina', 'Admin mode') + '<b>' + (ADMIN_MODE ? L('увімк.', 'wł.', 'on') : L('вимк.', 'wył.', 'off')) + '</b></button>' + (ADMIN_MODE ? '<a class="mitemrow" href="#/admin">🛠 ' + L('Адмін-панель', 'Panel admina', 'Admin panel') + '</a>' : '') : '') +
      (USER ? '<button type="button" class="mitemrow" id="msOut">↩ ' + L('Вийти', 'Wyloguj', 'Log out') + '</button>' : '<a class="mitemrow" href="#/register">✦ ' + L('Реєстрація', 'Rejestracja', 'Sign up') + '</a>') + '</div>');
    w.classList.add('msheetw');
    w.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { w.remove(); }); });
    w.querySelector('#msLang').onclick = function () { w.remove(); langModal(false); };
    w.querySelector('#msTheme').onclick = function () { w.remove(); toggleTheme(); };
    var ma = w.querySelector('#msAdm'); if (ma) ma.onclick = function () { w.remove(); setAdminMode(!ADMIN_MODE); };
    var mo = w.querySelector('#msOut'); if (mo) mo.onclick = function () { w.remove(); API.signOut().then(function () { USER = null; location.hash = '#/'; renderNav(); route(); }); };
  };
}
function renderNav() {
  var links = '<a href="#/">' + tx({uk:'Головна', pl:'Strona główna', en:'Home'}) + '</a><a href="#/catalog">' + tx({uk:'Каталог', pl:'Katalog', en:'Catalogue'}) + '</a><a href="#/trial">' + tx({uk:'Пробний урок', pl:'Lekcja próbna', en:'Trial lesson'}) + '</a>' + (USER ? '' : '<a href="#/test">' + tx({uk:'Тест рівня', pl:'Test poziomu', en:'Level test'}) + '</a>') + '<a href="#/guide">' + tx({uk:'Посібник', pl:'Poradnik', en:'Guide'}) + '</a>' + (USER ? '<a href="#/words">' + tx({uk:'Словник', pl:'Słownik', en:'Words'}) + '</a>' : '') + '<a href="#/pricing">' + tx({uk:'Тарифи', pl:'Cennik', en:'Pricing'}) + '</a>';
  if (USER) links += '<a href="#/cabinet">' + tx({uk:'Кабінет', pl:'Konto', en:'Account'}) + '</a>';
  if (isAdm()) links += '<a href="#/admin" style="color:var(--nav-admin)">' + tx({uk:'Адмін', pl:'Admin', en:'Admin'}) + '</a>';
  document.getElementById('navlinks').innerHTML = links;
  var adm = (USER && USER.role === 'admin') ? '<button class="tgl admsw' + (ADMIN_MODE ? ' on' : '') + '" type="button" id="admSw" title="' + t('Режим адміністратора') + '">⚙ ' + (ADMIN_MODE ? t('Адмін: увімк.') : t('Адмін: вимк.')) + '</button>' : '';
  var tg = adm + '<div class="row" style="gap:6px"><button class="tgl langbtn" type="button" id="langBtn" title="' + t('Обери мови') + '">🎬 ' + FLAG[TARGET] + ' · 💬 ' + FLAG[LANG] + '</button><button class="tgl" type="button" id="themeBtn" aria-label="' + (THEME === 'dark' ? t('Світла тема') : t('Темна тема')) + '">' + (THEME === 'dark' ? '☀' : '☾') + '</button></div>';
  document.getElementById('navuser').innerHTML = tg + (USER
    ? '<a class="userchip" href="#/cabinet" style="text-decoration:none"><span class="ava">' + esc((USER.name || '?')[0].toUpperCase()) + '</span><span class="muted" style="max-width:120px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">' + esc(USER.name) + t('</span></a><button class="btn btn-ghost btn-sm" type="button" id="logoutBtn">Вийти</button>')
    : t('<a class="btn btn-ghost btn-sm" href="#/login">Увійти</a><a class="btn btn-red btn-sm" href="#/register">Реєстрація</a>'));
  document.getElementById('langBtn').onclick = function () { langModal(false); };
  document.getElementById('themeBtn').onclick = toggleTheme;
  var asw = document.getElementById('admSw'); if (asw) asw.onclick = function () { setAdminMode(!ADMIN_MODE); };
  renderMobileNav();
  var lb = document.getElementById('logoutBtn');
  if (lb) lb.onclick = function () { API.signOut().then(function () { USER = null; toast(t('Ви вийшли з акаунта')); location.hash = '#/'; renderNav(); route(); }); };
}

/* ================= views ================= */
function heroSvg() {
  return '<svg class="scene" viewBox="0 0 800 500" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><defs><radialGradient id="glow" cx="62%" cy="40%" r="45%"><stop offset="0" stop-color="#ffd27a" stop-opacity=".75"/><stop offset=".5" stop-color="#8b5cf6" stop-opacity=".25"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient><linearGradient id="floor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a1230"/><stop offset="1" stop-color="#050409"/></linearGradient></defs><rect width="800" height="500" fill="url(#floor)"/><rect width="800" height="500" fill="url(#glow)"/><rect x="90" y="70" width="150" height="190" rx="75" fill="#0c0a1a" stroke="#3a2f63" stroke-width="4"/><g transform="translate(470 150) rotate(-12)"><rect width="140" height="92" rx="6" fill="#efe2c4"/><path d="M0 6 L70 54 L140 6" fill="none" stroke="#c9b48a" stroke-width="3"/><circle cx="70" cy="56" r="15" fill="#b3202f"/></g><g fill="#ffe7a8"><circle cx="440" cy="120" r="2.5"/><circle cx="640" cy="110" r="2"/><circle cx="610" cy="280" r="2.5"/></g><g fill="#05040a"><circle cx="300" cy="250" r="44"/><path d="M210 500 C210 380 240 310 300 300 C360 310 392 380 392 500 Z"/></g></svg>';
}
function isFreeCourse(c) { return !!c && /^\s*(0|free|darmo|za darmo|безкошт)/i.test(String(c.price || '')); }
function priceTxt(c) { return isFreeCourse(c) ? tx({uk:'Безкоштовно', pl:'Za darmo', en:'Free'}) : (c.price || ''); }
function posterHtml(c, small) {
  var cls = POSTER_CLASSES.indexOf(c.poster) > -1 ? c.poster : 'p1';
  return '<div class="poster ' + cls + '"' + (small ? ' style="width:120px;flex:0 0 120px;padding:10px"' : '') + '><span class="perf l"></span><span class="perf r"></span>' +
    (small ? '' : '<span class="tag">' + (c.kind === 'series' ? t('СЕРІАЛ') : t('ФІЛЬМ')) + ' · ' + esc(c.level) + '</span>' + (c.lessons_count ? (isFreeCourse(c) ? '<span class="tag new">' + tx({uk:'БЕЗКОШТОВНО', pl:'ZA DARMO', en:'FREE'}) + '</span>' : '') : t('<span class="tag new">СКОРО</span>'))) +
    '<div class="ptitle"' + (small ? ' style="font-size:14px"' : '') + '>' + esc(tr(c, 'title')) + '</div></div>';
}
function catalogGrid(courses) {
  if (!courses.length) return t('<div class="empty">Курсів поки немає. Адміністратор може додати їх в адмін-панелі.</div>');
  return '<div class="grid-films">' + courses.map(function (c) {
    return '<a class="film" href="#/course/' + esc(c.id) + '">' + posterHtml(c) + '<div class="film-meta"><span>' + (c.lessons_count || 0) + t(' уроків</span><b>') + esc(priceTxt(c)) + '</b></div></a>';
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
  return Promise.all([API.listCourses(true), API.myEnrollments(), API.myProgress('en'), API.myProgress('pl'), API.myProgress('uk'), API.myLangs()]).then(function (r) {
    var byT = {en:r[2], pl:r[3], uk:r[4]}, elangs = r[5];
    var courses = r[0], enr = r[1], started, prog;
    var lessonPromises = enr.map(function (cid) { return API.listLessons(cid); });
    return Promise.all(lessonPromises).then(function (lessonLists) {
      var doneIds = {};
      var lessonIdsOf = {}; enr.forEach(function (cid, i) { lessonIdsOf[cid] = lessonLists[i].map(function (l) { return l.id; }); });
      function langsOf(cid) { var ids = lessonIdsOf[cid] || []; return LANGS.filter(function (l) { var row = elangs.filter(function (e) { return e.course_id === cid && e.target === l; })[0]; return row ? !row.hidden : byT[l].some(function (p) { return ids.indexOf(p.lesson_id) > -1; }); }); }
      started = LANGS.filter(function (l) { return enr.some(function (cid) { return langsOf(cid).indexOf(l) > -1; }); });
      if (!CAB_T || started.indexOf(CAB_T) < 0) CAB_T = started.indexOf(TARGET) > -1 ? TARGET : (started[0] || TARGET);
      var visIds = []; enr.forEach(function (cid) { if (langsOf(cid).indexOf(CAB_T) > -1) visIds = visIds.concat(lessonIdsOf[cid]); });
      prog = byT[CAB_T].filter(function (p) { return visIds.indexOf(p.lesson_id) > -1; }); doneIds = {}; prog.forEach(function (p) { doneIds[p.lesson_id] = p; });
      var avg = prog.length ? Math.round(prog.reduce(function (a, p) { return a + (+p.score || 0); }, 0) / prog.length) : 0;
      var xp = prog.reduce(function (a, p) { return a + Math.round((+p.score || 0) / 10) * 10; }, 0);
      var days = {}; prog.forEach(function (p) { days[(p.completed_at || '').slice(0, 10)] = 1; });
      var allLessons = {}; lessonLists.forEach(function (ls) { ls.forEach(function (l) { allLessons[l.id] = l; }); });
      var my = enr.map(function (cid, i) { var c = courses.filter(function (x) { return x.id === cid; })[0]; if (!c) return ''; var ls = lessonLists[i], ids = lessonIdsOf[cid], cl = langsOf(cid);
        var rows = cl.map(function (l) { var pr = byT[l].filter(function (p) { return ids.indexOf(p.lesson_id) > -1; }), avail = ls.filter(function (x) { return l === 'en' || (x.variants && x.variants[l] && x.variants[l].length); }).length || ls.length, d = pr.length, pct = avail ? Math.round(d / avail * 100) : 0, av = d ? Math.round(pr.reduce(function (a, p) { return a + (+p.score || 0); }, 0) / d) : 0;
          return '<div class="lprog"><button type="button" class="lgo" data-go-c="' + esc(cid) + '" data-go-l="' + l + '"><span class="lflag">' + FLAG[l] + '</span><span class="lname">' + esc(langName(l)) + '</span><span class="lbar"><i style="width:' + pct + '%;background:' + (pct === 100 ? 'var(--ok)' : 'linear-gradient(90deg,var(--progress-1),var(--progress-2))') + '"></i></span><b>' + d + ' / ' + avail + (d ? ' · ' + av + '%' : '') + '</b></button>' + (d >= avail ? '<span class="ldel ldone" title="' + tx({uk:'Марафон цією мовою завершено, результат зберігається назавжди', pl:'Maraton w tym języku ukończony, wynik zostaje na zawsze', en:'Marathon completed in this language, the result stays forever'}) + '">🏁</span>' : '<button type="button" class="ldel" title="' + tx({uk:'Видалити результати', pl:'Usuń wyniki', en:'Delete results'}) + '" data-del-c="' + esc(cid) + '" data-del-l="' + l + '">✕</button>') + '</div>'; }).join('');
        if (!cl.length) rows = '<p class="muted small">' + tx({uk:'Обери мову, щоб почати цей марафон.', pl:'Wybierz język, aby zacząć ten maraton.', en:'Choose a language to start this marathon.'}) + '</p>';
        return '<div class="cprog"><div class="top"><a href="#/course/' + esc(c.id) + '">' + esc(tr(c, 'title')) + '</a></div>' + rows + (cl.length < 3 ? '<button type="button" class="btn btn-ghost btn-sm" data-add-c="' + esc(cid) + '">+ ' + tx({uk:'Додати мову', pl:'Dodaj język', en:'Add a language'}) + '</button>' : '') + '</div>'; }).join('');
      var recent = prog.slice().sort(function (a, b) { return (b.completed_at || '').localeCompare(a.completed_at || ''); }).slice(0, 6).map(function (p) { var l = allLessons[p.lesson_id]; return '<div><span>' + esc(l ? l.num + '. ' + tr(l, 'title') : t('Урок')) + '</span><b class="score">' + esc(scoreTxt(p)) + '</b></div>'; }).join('');
      var medals = [[prog.length >= 1, '1', t('Перший урок')], [prog.length >= 5, '5', t('П\'ять уроків')], [Object.keys(days).length >= 3, '3🔥', t('Три дні навчання')], [avg >= 90 && prog.length > 0, '★', t('Точність 90%+')], [enr.length >= 2, '2', t('Два марафони')], [lessonLists.some(function (ls) { return ls.length && ls.every(function (l) { return doneIds[l.id]; }); }), '🏁', t('Марафон пройдено')]];
      $app.innerHTML = t('<div class="page"><div class="sec-head"><div class="eyebrow">Особистий кабінет</div><h2>Привіт, ') + esc(USER.name) + '!</h2></div>' +
        '<div class="dash"><aside class="dside"><div class="user"><div class="ava">' + esc(USER.name[0].toUpperCase()) + '</div><div><b>' + esc(USER.name) + '</b><small>' + esc(USER.email) + '</small></div></div>' +
        t('<form class="form" id="keyForm" novalidate><label class="fl" for="keyInput">Активувати ключ<input class="inp" id="keyInput" placeholder="XXXX-XXXX-XXXX" maxlength="14" autocomplete="off" style="font-size:15px;padding:11px 12px"></label><button class="btn btn-red btn-sm" type="submit" style="justify-content:center">Активувати</button><div class="msg small" id="keyMsg" role="status"></div>') +
        (API.mode === 'demo' ? t('<p class="hint">Демо-ключ: HPS1-7KQ4-WZ9M</p>') : '') + '</form>' +
        (isAdm() ? t('<a class="btn btn-ghost btn-sm" href="#/admin" style="justify-content:center">Адмін-панель</a>') : '') + '</aside>' +
        '<div class="dmain">' + (started.length > 1 ? '<div class="cabtabs">' + started.map(function (l) { var pr = byT[l], av = pr.length ? Math.round(pr.reduce(function (a, p) { return a + (+p.score || 0); }, 0) / pr.length) : 0; return '<button type="button" class="cabtab' + (l === CAB_T ? ' on' : '') + '" data-cab="' + l + '"><b>' + FLAG[l] + '</b><span>' + esc(langName(l)) + '</span><small>' + pr.length + ' ' + t('уроків') + (pr.length ? ' · ' + av + '%' : '') + '</small></button>'; }).join('') + '</div>' : (started.length ? '<p class="eyebrow" style="margin-bottom:12px">' + FLAG[CAB_T] + ' · ' + esc(langName(CAB_T)) + '</p>' : '')) + '<div class="stats"><div class="stat"><b>' + prog.length + t('</b><span>уроків пройдено</span></div><div class="stat"><b>') + avg + t('%</b><span>середній бал</span></div><div class="stat"><b>') + xp + t('</b><span>XP набрано</span></div><div class="stat"><b>') + Object.keys(days).length + t('</b><span>днів навчання</span></div></div>') +
        t('<div class="rows"><div class="box"><h4>Мої марафони</h4>') + (my || t('<div class="empty small">Марафонів ще немає. Активуй ключ або <a href="#/trial">пройди пробний урок</a>.</div>')) + t('<a class="btn btn-ghost btn-sm" href="#/catalog" style="justify-self:start">Каталог курсів</a></div>') +
        t('<div class="box"><h4>Досягнення</h4>') + '<a class="btn btn-red btn-sm ach-go" href="#/achievements">🏆 ' + tx({uk:'Мої нагороди і сертифікати', pl:'Moje nagrody i certyfikaty', en:'My rewards and certificates'}) + '</a>' + t('<div class="ach">') + medals.map(function (m) { return '<div class="medal' + (m[0] ? '' : ' off') + '"><span class="m" style="border-color:' + (m[0] ? 'var(--gold)' : 'var(--dim)') + ';color:' + (m[0] ? 'var(--gold)' : 'var(--dim)') + '">' + m[1] + '</span>' + m[2] + '</div>'; }).join('') + '</div>' +
        t('<h4>Останні уроки</h4><div class="done-list">') + (recent || t('<span class="muted">Ще немає пройдених уроків</span>')) + '</div></div></div></div></div></div>';
      renderWritings(document.querySelector('.dmain')); processPendingWritings();
      document.querySelectorAll('[data-go-c]').forEach(function (b) { b.onclick = function () { setLangs(b.dataset.goL, LANG); location.hash = '#/course/' + b.dataset.goC; }; });
      document.querySelectorAll('[data-add-c]').forEach(function (b) { b.onclick = function () { var cid = b.dataset.addC; pickTargetModal(tx({uk:'Яку мову додати до марафону?', pl:'Jaki język dodać do maratonu?', en:'Which language do you want to add?'}), langsOf(cid), function (tg) { API.addLang(cid, tg).then(function () { setLangs(tg, LANG); toast(tx({uk:'Мову додано. Успіхів!', pl:'Język dodany. Powodzenia!', en:'Language added. Good luck!'})); location.hash = '#/course/' + cid; }); }); }; });
      document.querySelectorAll('[data-del-c]').forEach(function (b) { b.onclick = function () { var cid = b.dataset.delC, c = courses.filter(function (x) { return x.id === cid; })[0]; removeLangFlow(c, b.dataset.delL, langsOf(cid), lessonIdsOf[cid] || []); }; });
      document.querySelectorAll('[data-cab]').forEach(function (b) { b.onclick = function () { CAB_T = b.dataset.cab; route(); }; });
      var inp = document.getElementById('keyInput'), msg = document.getElementById('keyMsg');
      inp.oninput = function () { var v = inp.value.toUpperCase().replace(/[^A-Z0-9]/g, '').slice(0, 12); inp.value = v.replace(/(.{4})(?=.)/g, '$1-'); };
      document.getElementById('keyForm').onsubmit = function (e) {
        e.preventDefault();
        if (inp.value.replace(/-/g, '').length !== 12) { msg.className = 'msg small err'; msg.textContent = t('Ключ має містити 12 символів.'); return; }
        API.activateKey(inp.value).then(function (res) {
          if (res.ok) { toast(t('Ключ активовано! Марафон відкрито.'));
            pickTargetModal(tx({uk:'Якою мовою хочеш вивчати цей марафон?', pl:'W jakim języku chcesz uczyć się w tym maratonie?', en:'Which language do you want to learn in this marathon?'}), [], function (tg) {
              API.myEnrollments().then(function (ids) { var cids = res.course_id ? [res.course_id] : ids; return Promise.all(cids.map(function (cid) { return API.addLang(cid, tg); })).then(function () { setLangs(tg, LANG); CAB_T = tg; if (res.course_id) location.hash = '#/course/' + res.course_id; else route(); }); });
            }); } else { msg.className = 'msg small err'; msg.textContent = res.msg; }
        }).catch(function (err) { msg.className = 'msg small err'; msg.textContent = err.message; });
      };
    });
  });
}

function viewCourse(id) {
  return Promise.all([API.getCourse(id), API.listLessons(id), API.myEnrollments(), API.myProgress()]).then(function (r) {
    var c = r[0], ls = r[1], enrolled = r[2].indexOf(id) > -1 || isAdm() || isFreeCourse(c), done = {};
    setAmbient(ambTheme(c));
    if (!c) { $app.innerHTML = t('<div class="page"><div class="empty">Курс не знайдено. <a href="#/catalog">До каталогу</a></div></div>'); return; }
    r[3].forEach(function (p) { done[p.lesson_id] = p; });
    var types = {}; ls.forEach(function (l) { (l.tasks || []).forEach(function (t) { types[t.type] = 1; }); });
    $app.innerHTML = '<div class="page"><div class="mcard"><div class="panel"><div class="mhead">' + posterHtml(c, true) + '<div class="mhead-info"><div class="badges"><span class="badge hot">' + esc(c.level) + '</span><span class="badge">' + ls.length + t(' уроків</span><span class="badge">') + (c.kind === 'series' ? t('серіал') : t('фільм')) + '</span>' + (enrolled ? t('<span class="badge" style="color:var(--ok)">доступ відкрито</span>') : '') + '</div>' +
      '<h2 style="font-size:clamp(24px,3.4vw,36px)">' + esc(tr(c, 'title')) + '</h2><p class="muted">' + esc(tr(c, 'description')) + '</p>' +
      (enrolled ? '' : t('<div class="row"><a class="btn btn-red" href="#/buy">Купити ключ · ') + esc(c.price) + '</a>' + (USER ? t('<a class="btn btn-ghost" href="#/cabinet">Активувати ключ</a>') : t('<a class="btn btn-ghost" href="#/register">Створити кабінет</a>')) + '</div>') + '</div></div>' +
      (isAdm() && ls.length ? '<div class="admtools"><b>🛠 ' + tx({uk:'Тест адміна', pl:'Test admina', en:'Admin test'}) + ' · ' + FLAG[TARGET] + '</b><span class="hint">' + tx({uk:'Змінює лише твої результати', pl:'Zmienia tylko twoje wyniki', en:'Changes only your own results'}) + '</span><div class="row" style="gap:6px;flex-wrap:wrap"><select class="inp-s" id="admLes" style="max-width:260px"><option value="">' + tx({uk:'Усі уроки', pl:'Wszystkie lekcje', en:'All lessons'}) + '</option>' + ls.filter(function (x) { return !!lessonTasks(x); }).map(function (x) { return '<option value="' + esc(x.id) + '">' + x.num + '. ' + esc(tr(x, 'title')) + '</option>'; }).join('') + '</select><input class="inp-s" id="admPct" type="number" min="0" max="100" value="100" style="width:80px"><button class="btn btn-ghost btn-sm" type="button" id="admFill">' + tx({uk:'Зарахувати', pl:'Zalicz', en:'Apply'}) + '</button><button class="btn btn-ghost btn-sm" type="button" id="admReset">' + tx({uk:'Скинути мої результати', pl:'Wyczyść moje wyniki', en:'Reset my results'}) + '</button></div></div>' : '') +
      (ls.length ? '<ul class="lessons">' + ls.map(function (l, i) {
        var arc = l.variants && l.variants.arc, prevArc = i && ls[i - 1].variants && ls[i - 1].variants.arc, arcH = arc && arc !== prevArc ? '<li class="arc-h">' + esc(l.variants['arc_' + LANG] || arc) + '</li>' : '';
        var avail = !!lessonTasks(l), free0 = i === 0 && c.free_first !== false, open = (enrolled || free0) && avail, isDone = done[l.id];
        var inner = '<li class="' + (isDone ? 'done' : '') + '"><span class="lnum">' + (isDone ? '✓ ' : '') + String(l.num).padStart(2, '0') + '</span><span class="ltitle">' + esc(tr(l, 'title')) + '<small>' + esc(lGram(l)) + (free0 && !enrolled ? t(' · безкоштовно') : '') + (!avail ? ' · ' + t('Скоро цією мовою') + ' ' + FLAG[TARGET] : '') + '</small></span>' + (open ? (isDone ? '<b class="score">' + esc(scoreTxt(isDone)) + '</b>' : '<span class="lock" style="color:var(--neon)">▶</span>') : '<span class="lock">🔒</span>') + '</li>';
        return arcH + (open ? '<a class="lesson-link" href="#/lesson/' + esc(l.id) + '">' + inner + '</a>' : inner);
      }).join('') + '</ul>' : t('<div class="empty" style="margin-top:20px">Уроки цього марафону скоро з\'являться.</div>')) +
      t('</div><div class="panel"><h3 style="margin-bottom:18px">Типи завдань у курсі</h3><div class="task-types">') + Object.keys(types).map(function (t) { return '<div class="ttype"><span class="k q">' + esc(t.slice(0, 2).toUpperCase()) + '</span><div><b>' + esc(ttName(t)) + '</b></div></div>'; }).join('') + '</div></div></div></div>';
    var af = document.getElementById('admFill');
    if (af) { var avIds = ls.filter(function (x) { return !!lessonTasks(x); }).map(function (x) { return x.id; });
      var pick = function () { var s = document.getElementById('admLes').value; return s ? [s] : avIds; };
      af.onclick = function () { var ids = pick(), v = Math.max(0, Math.min(100, +document.getElementById('admPct').value || 0)); API.adminSetProgress(ids, TARGET, v).then(function () { return API.addLang(id, TARGET); }).then(function () { toast(tx({uk:'Готово: ', pl:'Gotowe: ', en:'Done: '}) + ids.length + ' × ' + v + '%'); route(); }).catch(function (e) { toast(e.message, 'err'); }); };
      document.getElementById('admReset').onclick = function () { API.adminResetOwn(pick(), TARGET).then(function () { toast(tx({uk:'Результати скинуто', pl:'Wyniki wyczyszczone', en:'Results reset'})); route(); }).catch(function (e) { toast(e.message, 'err'); }); }; }
  });
}


function ttsTextsOf(ls, tg) {
  var out = {}, saved = TARGET; TARGET = tg;
  function add(v) { var c = ttsClean(v); if (c && c.length <= 500 && /\p{L}/u.test(c)) out[c] = 1; }
  try { ls.forEach(function (l) { (lessonTasks(l) || []).forEach(function (tk) {
    if (tk.type === 'glossary') (tk.items || []).forEach(function (w) { add(w.w); });
    if (tk.say) add(tk.say);
    if (tk.type === 'match') (lf(tk, 'options') || tk.options || []).forEach(function (x) { add(String(x).split('=')[0]); });
  }); }); } finally { TARGET = saved; }
  return Object.keys(out);
}
var VOX_RUN = false;
function adminVoices(ls) {
  var host = document.querySelector('.admtools'); if (!host) return;
  var box = document.createElement('div'); box.className = 'voxbox';
  box.innerHTML = '<b>🔊 ' + tx({uk:'Голоси курсу (Gemini)', pl:'Głosy kursu (Gemini)', en:'Course voices (Gemini)'}) + '</b> <span class="hint" id="voxSt">…</span><div class="row" style="gap:6px;flex-wrap:wrap;margin-top:6px">' + ['en', 'pl', 'uk'].map(function (g) { return '<label class="small"><input type="checkbox" class="voxl" value="' + g + '" checked> ' + FLAG[g] + '</label>'; }).join(' ') + '<button type="button" class="btn btn-ghost btn-s" id="voxGo">▶ ' + tx({uk:'Згенерувати', pl:'Generuj', en:'Generate'}) + '</button></div>';
  host.appendChild(box);
  var st = box.querySelector('#voxSt');
  function todo() { var L = [].slice.call(box.querySelectorAll('.voxl:checked')).map(function (x) { return x.value; }), all = [];
    L.forEach(function (g) { ttsTextsOf(ls, g).forEach(function (t) { var p = ttsPath(g, t); if (!TTS_SET || !TTS_SET[p]) all.push({g:g, t:t, p:p}); }); }); return all; }
  function count() { var n = 0; [].slice.call(box.querySelectorAll('.voxl:checked')).forEach(function (c) { n += ttsTextsOf(ls, c.value).length; }); var left = todo().length; st.textContent = tx({uk:'готово ', pl:'gotowe ', en:'done '}) + (n - left) + ' / ' + n; }
  API.ttsList().then(function (ps) { TTS_SET = {}; ps.forEach(function (p) { TTS_SET[p] = 1; }); count(); }).catch(function () { count(); });
  var purged = ''; try { purged = localStorage.getItem('ml_tts_purged'); } catch (e) {}
  if (!purged && API.token) API.token().then(function (tok) { var C = window.MOVILANG_CONFIG || {}; if (!tok || !C.SUPABASE_URL) return;
    return fetch(C.SUPABASE_URL + '/functions/v1/tts', {method:'POST', headers:{'Content-Type':'application/json', apikey:C.SUPABASE_ANON_KEY, Authorization:'Bearer ' + tok}, body:JSON.stringify({purge:true})}).then(function (r) { return r.json(); }).then(function (j) { if (j && j.removed != null) { try { localStorage.setItem('ml_tts_purged', '1'); } catch (e) {} if (j.removed) toast('Supabase: ' + j.removed + ' old clips removed'); } }); }).catch(function () {});
  box.querySelectorAll('.voxl').forEach(function (c) { c.onchange = count; });
  box.querySelector('#voxGo').onclick = function () {
    if (VOX_RUN) { VOX_RUN = false; return; }
    var list = todo(), i = 0, btn = this, C = window.MOVILANG_CONFIG || {}; if (!list.length) return toast('✓');
    VOX_RUN = true; btn.textContent = '■ Stop';
    API.token().then(function (tok) {
      function next() {
        if (!VOX_RUN || i >= list.length || !document.body.contains(box)) { VOX_RUN = false; btn.textContent = '▶ ' + tx({uk:'Згенерувати', pl:'Generuj', en:'Generate'}); count(); return; }
        var it = list[i++]; st.textContent = i + ' / ' + list.length + ' · ' + it.t.slice(0, 40);
        var H = {'Content-Type':'application/json', apikey:C.SUPABASE_ANON_KEY, Authorization:'Bearer ' + tok}, model = '';
        fetch(C.SUPABASE_URL + '/functions/v1/tts', {method:'POST', headers:H, body:JSON.stringify({text:it.t, lang:it.g})})
          .then(function (r) { return r.json().then(function (j) { return {s:r.status, j:j}; }); })
          .then(function (x) {
            if (x.s === 429) { var e = new Error(tx({uk:'Денний ліміт Gemini вичерпано. Продовж завтра — готові голоси збережено.', pl:'Dzienny limit Gemini wyczerpany. Kontynuuj jutro — gotowe głosy są zapisane.', en:'Gemini daily limit reached. Continue tomorrow — finished clips are saved.'})); e.info = 1; if (x.j && x.j.detail && /\[cloud-tts/.test(x.j.detail)) e.message += ' — ' + x.j.detail.slice(0, 160); throw e; }
            if (!x.j || !x.j.audio) throw new Error((x.j && (x.j.error + ' ' + (x.j.detail || ''))) || x.s);
            model = x.j.model || ''; var bin = atob(x.j.audio), u8 = new Uint8Array(bin.length); for (var q = 0; q < bin.length; q++) u8[q] = bin.charCodeAt(q);
            return fetch('/a/' + it.p, {method:'PUT', headers:{'Content-Type':'audio/wav', Authorization:'Bearer ' + tok}, body:u8});
          })
          .then(function (r) { if (!r.ok) return r.text().then(function (t) { throw new Error('R2 ' + r.status + ': ' + t); }); return API.ttsAdd({path:it.p, lang:it.g, text:it.t, model:'r2:' + model}); })
          .then(function () { TTS_SET[it.p] = 1; setTimeout(next, 1200); })
          .catch(function (e) { toast((e.info ? '' : 'TTS: ') + String(e.message || e).slice(0, 180), e.info ? 'info' : 'err'); VOX_RUN = false; next(); });
      }
      next();
    });
  };
}
/* ---------- illustrations (original SVG, no film stills) ---------- */
var ILLU_KEYS = ['castle','stairs','snake','letter','cake','alley','wand','train','hat','potion','broom','troll','pitch','mirror','forest','chess','stone','owl','tomb','crow','ring','vervain','diary','candles','manor','comet'];
function illu(key) {
  var g = '#f1c27d', c = '#efe2c4', d = '#0b0b14', a = '#e8253a';
  var art = {
    castle: '<path d="M190 250V150l20-30 20 30v100M260 250V110l25-40 25 40v140M340 250V160l20-30 20 30v90M410 250V130l22-35 22 35v120" fill="' + d + '" stroke="' + g + '" stroke-width="3"/><g fill="' + g + '"><rect x="280" y="150" width="10" height="16"/><rect x="425" y="170" width="10" height="16"/><rect x="205" y="185" width="8" height="14"/></g>',
    stairs: '<path d="M150 260h80v-30h60v-30h60v-30h60v-30h60v-30h80" fill="none" stroke="' + g + '" stroke-width="5"/><rect x="190" y="180" width="70" height="80" fill="' + d + '" stroke="' + c + '" stroke-width="3"/><path d="M200 195h50M200 210h50M200 225h50M215 185v70M235 185v70" stroke="' + c + '" stroke-width="2"/>',
    snake: '<rect x="170" y="80" width="300" height="170" rx="8" fill="#1d3a4a" stroke="' + c + '" stroke-width="4" opacity=".9"/><path d="M200 220c40-60 80 40 120-20s80 40 120-10" fill="none" stroke="#6fbf73" stroke-width="16" stroke-linecap="round"/><circle cx="440" cy="190" r="10" fill="#6fbf73"/><path d="M175 85l290 160" stroke="#fff" stroke-width="2" opacity=".4"/>',
    letter: '<g transform="rotate(-8 320 160)"><rect x="220" y="100" width="200" height="130" rx="8" fill="' + c + '"/><path d="M220 106l100 70 100-70" fill="none" stroke="#c9b48a" stroke-width="4"/><circle cx="320" cy="178" r="20" fill="' + a + '"/></g><g fill="' + c + '" opacity=".6"><rect x="120" y="60" width="60" height="40" rx="4" transform="rotate(14 150 80)"/><rect x="470" y="70" width="60" height="40" rx="4" transform="rotate(-18 500 90)"/><rect x="480" y="200" width="50" height="34" rx="4" transform="rotate(10 505 217)"/></g>',
    cake: '<rect x="230" y="160" width="180" height="80" rx="10" fill="#d97aa0"/><path d="M230 175c20 15 40-10 60 5s40-10 60 5 40-10 60 5" fill="none" stroke="#fff" stroke-width="6"/><rect x="314" y="120" width="12" height="40" fill="' + c + '"/><path d="M320 100c-10 10-6 20 0 22 6-2 10-12 0-22z" fill="' + g + '"/><text x="320" y="215" text-anchor="middle" font-size="22" font-weight="700" fill="#3a1a2a">HAPPY BIRTHDAY</text>',
    alley: '<g stroke="' + g + '" stroke-width="3" fill="' + d + '"><path d="M120 260V110l60-30 60 30v150z"/><path d="M250 260V90l70-35 70 35v170z"/><path d="M400 260V120l60-30 60 30v140z"/></g><g fill="' + g + '"><rect x="150" y="150" width="60" height="18"/><rect x="285" y="130" width="70" height="18"/><rect x="430" y="160" width="60" height="18"/></g>',
    wand: '<g fill="none" stroke="' + c + '" stroke-width="3"><rect x="150" y="150" width="90" height="34"/><rect x="160" y="184" width="90" height="34"/><rect x="150" y="218" width="90" height="34"/></g><path d="M300 240L460 90" stroke="#8a5a3a" stroke-width="12" stroke-linecap="round"/><g fill="' + g + '"><circle cx="475" cy="78" r="6"/><circle cx="500" cy="100" r="4"/><circle cx="460" cy="55" r="4"/><circle cx="510" cy="65" r="3"/></g>',
    train: '<rect x="180" y="150" width="260" height="70" rx="10" fill="' + a + '"/><rect x="440" y="120" width="70" height="100" rx="6" fill="' + a + '"/><rect x="200" y="125" width="40" height="25" fill="' + d + '"/><g fill="' + d + '"><circle cx="220" cy="235" r="18"/><circle cx="300" cy="235" r="18"/><circle cx="380" cy="235" r="18"/><circle cx="470" cy="235" r="18"/></g><g fill="#fff" opacity=".35"><circle cx="220" cy="100" r="22"/><circle cx="185" cy="70" r="28"/><circle cx="150" cy="45" r="32"/></g>',
    hat: '<path d="M220 240c40-10 160-10 200 0-30-60-40-120-70-170-10 40-60 60-60 80 0 30-50 60-70 90z" fill="#5a4030" stroke="' + g + '" stroke-width="3"/><ellipse cx="320" cy="245" rx="130" ry="18" fill="#4a3426"/><path d="M290 170q30 15 60 0" stroke="' + d + '" stroke-width="4" fill="none"/>',
    potion: '<path d="M300 90h40v40l50 90q8 22-18 26H268q-26-4-18-26l50-90z" fill="#6fcf97" opacity=".85" stroke="' + c + '" stroke-width="4"/><g fill="#fff" opacity=".7"><circle cx="305" cy="200" r="7"/><circle cx="330" cy="180" r="5"/><circle cx="345" cy="210" r="6"/></g><path d="M200 255h240" stroke="' + g + '" stroke-width="4"/>',
    broom: '<path d="M170 230L440 100" stroke="#8a5a3a" stroke-width="10" stroke-linecap="round"/><path d="M440 100l60-20-10 40-20 30z" fill="' + g + '"/><circle cx="220" cy="110" r="14" fill="' + g + '"/><path d="M206 110c-20-10-30 0-40-8M234 110c20-10 30 0 40-8" stroke="' + c + '" stroke-width="3" fill="none"/>',
    troll: '<path d="M240 260c-10-90 20-160 80-170 60 10 90 80 80 170z" fill="#5b6b4a"/><circle cx="300" cy="140" r="6" fill="' + g + '"/><circle cx="340" cy="140" r="6" fill="' + g + '"/><path d="M420 260l60-150" stroke="#6b4a2a" stroke-width="22" stroke-linecap="round"/>',
    pitch: '<g fill="none" stroke="' + g + '" stroke-width="5"><circle cx="230" cy="100" r="28"/><circle cx="320" cy="80" r="32"/><circle cx="410" cy="100" r="28"/></g><g stroke="' + g + '" stroke-width="5"><path d="M230 128v130M320 112v146M410 128v130"/></g><circle cx="500" cy="170" r="10" fill="' + g + '"/><path d="M490 168c-14-10-24-4-30 2M510 168c14-10 24-4 30 2" stroke="' + c + '" stroke-width="3" fill="none"/>',
    mirror: '<rect x="250" y="50" width="140" height="210" rx="70" fill="#22304a" stroke="' + g + '" stroke-width="8"/><ellipse cx="320" cy="150" rx="45" ry="70" fill="#9fd3ff" opacity=".25"/><path d="M270 270h100" stroke="' + g + '" stroke-width="10"/>',
    forest: '<g fill="#0f2a1c" stroke="#3b6b4a" stroke-width="2"><path d="M140 260l40-140 40 140z"/><path d="M200 260l50-170 50 170z"/><path d="M380 260l50-170 50 170z"/><path d="M450 260l40-130 40 130z"/></g><ellipse cx="330" cy="240" rx="40" ry="8" fill="#cfe8ff" opacity=".8"/>',
    chess: '<g>' + [0,1,2,3,4,5].map(function (r) { return [0,1,2,3,4,5,6,7].map(function (q) { return '<rect x="' + (192 + q * 32) + '" y="' + (70 + r * 32) + '" width="32" height="32" fill="' + ((r + q) % 2 ? '#3a2e24' : c) + '"/>'; }).join(''); }).join('') + '</g><path d="M300 150c0-30 40-40 50-10l10 20-20 0 0 40h-40z" fill="' + d + '" stroke="' + g + '" stroke-width="3"/>',
    stone: '<path d="M320 70l60 60-60 120-60-120z" fill="' + a + '" stroke="#ff9aa8" stroke-width="3"/><path d="M260 130h120M320 70l-20 60 20 120 20-120z" stroke="#ff9aa8" stroke-width="2" fill="none" opacity=".7"/>',
    owl: '<ellipse cx="320" cy="170" rx="70" ry="85" fill="#e8e1d8"/><circle cx="295" cy="140" r="20" fill="#fff"/><circle cx="345" cy="140" r="20" fill="#fff"/><circle cx="295" cy="140" r="9" fill="' + d + '"/><circle cx="345" cy="140" r="9" fill="' + d + '"/><path d="M312 165l8 14 8-14z" fill="' + g + '"/><rect x="380" y="200" width="70" height="44" rx="4" fill="' + c + '" transform="rotate(-12 415 222)"/>',
    tomb: '<path d="M210 260V150q110-90 220 0v110z" fill="#1a1626" stroke="' + g + '" stroke-width="4"/><path d="M270 260v-80q50-40 100 0v80" fill="' + d + '" stroke="' + c + '" stroke-width="3"/><path d="M320 120v-30M305 105h30" stroke="' + g + '" stroke-width="4"/><path d="M120 262h400" stroke="#4a4560" stroke-width="4"/><g fill="#3d5a3a"><path d="M150 262q10-40 25 0z"/><path d="M470 262q12-50 28 0z"/></g>',
    crow: '<circle cx="470" cy="80" r="42" fill="' + c + '" opacity=".85"/><path d="M180 230q120-30 260 0" stroke="#4a3a2a" stroke-width="10" fill="none"/><path d="M300 215q-10-45 25-70q30-15 55 5l25-5-20 18q5 40-30 55z" fill="' + d + '" stroke="#26203a" stroke-width="2"/><path d="M330 175l-55 25 30 5z" fill="' + d + '"/><circle cx="372" cy="158" r="3" fill="' + a + '"/>',
    ring: '<ellipse cx="320" cy="170" rx="90" ry="70" fill="none" stroke="' + g + '" stroke-width="14"/><ellipse cx="320" cy="170" rx="90" ry="70" fill="none" stroke="#fff6" stroke-width="2"/><path d="M285 85l35-35 35 35-35 30z" fill="#2a49c9" stroke="' + g + '" stroke-width="4"/><path d="M320 50v65M285 85h70" stroke="#9fb2ff" stroke-width="1.5" opacity=".6"/>',
    vervain: '<path d="M300 110h40v20q30 15 30 60v60q0 15-15 15h-70q-15 0-15-15v-60q0-45 30-60z" fill="#ffffff14" stroke="' + c + '" stroke-width="3"/><path d="M280 200h80v50q0 10-10 10h-60q-10 0-10-10z" fill="#7b5bd6" opacity=".7"/><rect x="295" y="92" width="50" height="20" rx="4" fill="#6b4a2a"/><g stroke="#6fbf73" stroke-width="3" fill="none"><path d="M430 260q-10-80 20-160"/><path d="M445 160l20-15M440 200l-22-12M450 125l18-18"/></g><g fill="#a98bff"><circle cx="452" cy="98" r="6"/><circle cx="468" cy="142" r="5"/><circle cx="416" cy="186" r="5"/><circle cx="470" cy="104" r="4"/></g>',
    diary: '<g transform="rotate(-6 320 170)"><rect x="200" y="90" width="240" height="160" rx="10" fill="#4a2030" stroke="' + g + '" stroke-width="3"/><rect x="214" y="100" width="212" height="140" rx="4" fill="' + c + '"/><path d="M320 100v140" stroke="#c9b48a" stroke-width="3"/><g stroke="#8a7a60" stroke-width="2"><path d="M232 130h70M232 150h76M232 170h60M232 190h72M338 130h70M338 150h64M338 170h74"/></g></g><path d="M455 85l-80 120" stroke="' + d + '" stroke-width="6" stroke-linecap="round"/><path d="M455 85l-80 120" stroke="' + g + '" stroke-width="2"/>',
    candles: '<g fill="' + c + '"><rect x="230" y="160" width="26" height="100" rx="3"/><rect x="300" y="130" width="30" height="130" rx="3"/><rect x="372" y="175" width="24" height="85" rx="3"/></g><g fill="#ffb347"><path d="M243 160q-12-20 0-38q12 18 0 38z"/><path d="M315 130q-14-24 0-44q14 20 0 44z"/><path d="M384 175q-11-18 0-34q11 16 0 34z"/></g><circle cx="315" cy="110" r="60" fill="#ffb34722"/><path d="M190 262h260" stroke="' + g + '" stroke-width="4"/>',
    manor: '<path d="M170 260V150l150-70 150 70v110z" fill="#15121f" stroke="' + g + '" stroke-width="3"/><path d="M290 260v-60h60v60" fill="' + d + '" stroke="' + c + '" stroke-width="2"/><g fill="#ffcf6b"><rect x="205" y="170" width="30" height="36" opacity=".9"/><rect x="405" y="170" width="30" height="36" opacity=".35"/><rect x="305" y="130" width="30" height="34" opacity=".7"/></g><path d="M120 262h400" stroke="#4a4560" stroke-width="4"/><path d="M100 230q120-30 220 0t220 0" stroke="#ffffff22" stroke-width="18" fill="none"/>',
    comet: '<path d="M140 240L430 90" stroke="url(#cmt)" stroke-width="18" stroke-linecap="round"/><defs><linearGradient id="cmt" x1="0" x2="1"><stop offset="0" stop-color="#9fd8ff" stop-opacity="0"/><stop offset="1" stop-color="#e8f6ff"/></linearGradient></defs><circle cx="440" cy="85" r="16" fill="#fff"/><path d="M100 262q110-50 220-20t220-10" fill="#0a0a12" stroke="#2c2840" stroke-width="3"/>'
  }[key];
  if (!art) return '';
  return '<svg class="illu-svg ik-' + key + '" viewBox="0 0 640 300" role="img" aria-label="' + esc(key) + '"><defs><radialGradient id="ig' + key + '" cx="50%" cy="35%" r="75%"><stop offset="0" stop-color="#2b2350"/><stop offset="1" stop-color="#0b0a14"/></radialGradient></defs><rect width="640" height="300" fill="url(#ig' + key + ')"/><g fill="#fff" opacity=".5"><circle cx="60" cy="40" r="1.6"/><circle cx="580" cy="60" r="1.4"/><circle cx="520" cy="30" r="1.2"/><circle cx="110" cy="120" r="1.2"/></g><g class="art">' + art + '</g><text x="16" y="24" font-family="monospace" font-size="12" fill="#fff" opacity=".7">● SCENE</text></svg>';
}


/* ---------- achievements & certificates ---------- */
function viewAchievements() {
  if (!requireUser()) return Promise.resolve();
  return Promise.all([API.listCourses(true), API.myEnrollments(), API.myProgress('en'), API.myProgress('pl'), API.myProgress('uk')]).then(function (r) {
    var courses = r[0], enr = r[1], byT = {en:r[2], pl:r[3], uk:r[4]};
    return Promise.all(enr.map(function (cid) { return API.listLessons(cid); })).then(function (lists) {
      var certs = [], badges = [], totalLessons = 0;
      enr.forEach(function (cid, i) {
        var c = courses.filter(function (x) { return x.id === cid; })[0]; if (!c) return;
        var ls = lists[i];
        LANGS.forEach(function (lg) {
          var avail = ls.filter(function (x) { return lg === 'en' || (x.variants && x.variants[lg] && x.variants[lg].length); });
          if (!avail.length) return;
          var pr = byT[lg].filter(function (p) { return avail.some(function (x) { return x.id === p.lesson_id; }); });
          if (!pr.length) return;
          totalLessons += pr.length;
          pr.forEach(function (p) { var l = avail.filter(function (x) { return x.id === p.lesson_id; })[0], b = l && l.variants && l.variants.badge;
            badges.push({icon:b ? b.icon : '🎬', name:b ? lf(b, 'name') : tr(l, 'title'), text:b ? lf(b, 'text') : '', course:tr(c, 'title'), lang:lg, score:+p.score || 0, date:p.completed_at, num:l ? l.num : 0}); });
          var dates = pr.map(function (p) { return p.completed_at || ''; }).filter(Boolean).sort();
          var avg = Math.round(pr.reduce(function (a, p) { return a + (+p.score || 0); }, 0) / pr.length);
          var last = avail[avail.length - 1], lastP = pr.filter(function (p) { return p.lesson_id === last.id; })[0];
          var certName = (last.variants && (last.variants['cert_' + LANG] || last.variants.cert)) || tx({uk:'Випускник марафону', pl:'Absolwent maratonu', en:'Marathon graduate'});
          var done = pr.length >= avail.length && (!lastP || (+lastP.score || 0) >= 70);
          certs.push({c:c, lang:lg, done:done, title:certName, start:dates[0], end:dates[dates.length - 1], avg:avg, n:pr.length, total:avail.length,
            badges:pr.length, id:'ML-' + String(cid).replace(/[^a-z0-9]/gi, '').slice(0, 4).toUpperCase() + '-' + lg.toUpperCase() + '-' + String(USER.id || '').replace(/[^a-z0-9]/gi, '').slice(-4).toUpperCase()});
        });
      });
      badges.sort(function (a, b) { return (b.date || '').localeCompare(a.date || ''); });
      var L3 = function (o) { return tx(o); };
      var certHtml = certs.map(function (k, i) {
        var pct = Math.round(k.n / k.total * 100);
        return '<div class="cert3d' + (k.done ? '' : ' locked') + '" data-ci="' + i + '"><div class="c3-in">' +
          '<div class="c3-face c3-front"><div class="c3-glow"></div><div class="c3-seal">' + (k.done ? '🏆' : '🔒') + '</div>' +
          '<div class="eyebrow">' + L3({uk:'Сертифікат MoviLang', pl:'Certyfikat MoviLang', en:'MoviLang Certificate'}) + ' · ' + FLAG[k.lang] + '</div>' +
          '<h3>' + esc(k.done ? k.title : L3({uk:'Ще не відкрито', pl:'Jeszcze zablokowany', en:'Not unlocked yet'})) + '</h3>' +
          '<p class="c3-name">' + esc(USER.name || USER.email) + '</p>' +
          '<p class="muted small">' + esc(tr(k.c, 'title')) + ' · ' + esc(langName(k.lang)) + '</p>' +
          '<div class="c3-dates"><div><small>' + L3({uk:'Початок', pl:'Start', en:'Started'}) + '</small><b>' + fmtDate(k.start) + '</b></div><div><small>' + L3({uk:'Завершення', pl:'Ukończenie', en:'Completed'}) + '</small><b>' + (k.done ? fmtDate(k.end) : '—') + '</b></div><div><small>' + L3({uk:'Середній бал', pl:'Średni wynik', en:'Average'}) + '</small><b>' + k.avg + '%</b></div></div>' +
          (k.done ? '' : '<div class="c3-prog"><i style="width:' + pct + '%"></i></div><p class="small muted">' + k.n + ' / ' + k.total + ' · ' + L3({uk:'фінальний іспит від 70%', pl:'egzamin końcowy od 70%', en:'final exam 70%+'}) + '</p>') +
          '<p class="c3-hint">' + L3({uk:'Натисни, щоб перевернути', pl:'Kliknij, aby odwrócić', en:'Tap to flip'}) + ' ↻</p></div>' +
          '<div class="c3-face c3-back"><div class="eyebrow">' + L3({uk:'Деталі', pl:'Szczegóły', en:'Details'}) + '</div>' +
          '<div class="c3-stats"><div><b>' + k.n + '</b><span>' + L3({uk:'уроків', pl:'lekcji', en:'lessons'}) + '</span></div><div><b>' + k.avg + '%</b><span>' + L3({uk:'точність', pl:'trafność', en:'accuracy'}) + '</span></div><div><b>' + k.badges + '</b><span>' + L3({uk:'нагород', pl:'nagród', en:'rewards'}) + '</span></div></div>' +
          '<p class="small muted">ID: ' + esc(k.id) + '</p>' +
          (k.done ? '<div class="row" style="justify-content:center"><button class="btn btn-red btn-sm" type="button" data-print="' + i + '">🖨 ' + L3({uk:'Друкувати / PDF', pl:'Drukuj / PDF', en:'Print / PDF'}) + '</button></div>' : '<a class="btn btn-ghost btn-sm" href="#/course/' + esc(k.c.id) + '">' + L3({uk:'Продовжити марафон', pl:'Kontynuuj maraton', en:'Continue the marathon'}) + '</a>') +
          '</div></div></div>';
      }).join('');
      var badgeHtml = badges.map(function (b) { return '<div class="bdg" title="' + esc(b.text) + '"><span class="bdg-i">' + esc(b.icon) + '</span><b>' + esc(b.name) + '</b><small>' + FLAG[b.lang] + ' ' + esc(b.course) + ' · ' + b.score + '%</small></div>'; }).join('');
      $app.innerHTML = '<div class="page"><div class="sec-head"><a href="#/cabinet" class="muted small">← ' + t('Мій кабінет') + '</a><div class="eyebrow">' + L3({uk:'Досягнення', pl:'Osiągnięcia', en:'Achievements'}) + '</div><h2>' + L3({uk:'Мої нагороди і сертифікати', pl:'Moje nagrody i certyfikaty', en:'My rewards and certificates'}) + '</h2><p class="lead">' + totalLessons + ' ' + L3({uk:'пройдених уроків', pl:'ukończonych lekcji', en:'lessons completed'}) + ' · ' + badges.length + ' ' + L3({uk:'нагород', pl:'nagród', en:'rewards'}) + ' · ' + certs.filter(function (k) { return k.done; }).length + ' ' + L3({uk:'сертифікатів', pl:'certyfikatów', en:'certificates'}) + '</p></div>' +
        '<h3 style="margin:8px 0 14px">' + L3({uk:'Сертифікати', pl:'Certyfikaty', en:'Certificates'}) + '</h3>' + (certHtml ? '<div class="certs">' + certHtml + '</div>' : '<div class="empty">' + L3({uk:'Почни марафон — тут з\'явиться твій сертифікат.', pl:'Zacznij maraton — tu pojawi się twój certyfikat.', en:'Start a marathon — your certificate will appear here.'}) + '</div>') +
        '<h3 style="margin:28px 0 14px">' + L3({uk:'Колекція нагород', pl:'Kolekcja nagród', en:'Reward collection'}) + '</h3>' + (badgeHtml ? '<div class="bdgs">' + badgeHtml + '</div>' : '<div class="empty">' + L3({uk:'Пройди перший урок, щоб отримати нагороду.', pl:'Ukończ pierwszą lekcję, aby zdobyć nagrodę.', en:'Finish your first lesson to earn a reward.'}) + '</div>') + '</div>';
      document.querySelectorAll('.cert3d').forEach(function (el) {
        var inn = el.querySelector('.c3-in'), flipped = false;
        el.onclick = function (e) { if (e.target.closest('button,a')) return; flipped = !flipped; el.classList.toggle('flip', flipped); inn.style.transform = flipped ? 'rotateY(180deg)' : ''; };
        el.onmousemove = function (e) { var r = el.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5; inn.style.transform = 'rotateY(' + ((flipped ? 180 : 0) + x * 16) + 'deg) rotateX(' + (-y * 12) + 'deg)'; el.style.setProperty('--gx', (x + .5) * 100 + '%'); el.style.setProperty('--gy', (y + .5) * 100 + '%'); };
        el.onmouseleave = function () { inn.style.transform = ''; };
      });
      document.querySelectorAll('[data-print]').forEach(function (b) { b.onclick = function () { var el = b.closest('.cert3d'); el.classList.remove('flip'); el.classList.add('printing'); setTimeout(function () { window.print(); el.classList.remove('printing'); }, 300); }; });
    });
  });
}
/* ---------- lesson player ---------- */
function scoreTxt(p) { return p.score + '%' + (p.retry_score != null ? ' (' + p.retry_score + '%)' : ''); }
function lf(tk, k) { var v = tk[k + '_' + LANG]; return v != null && v !== '' ? v : tk[k]; }
var TASK_INS = {vocabulary:'Обери правильне слово', grammar:'Обери правильну форму', listening:'Послухай і обери відповідь', subtitles:'Заповни пропуск у субтитрах', match:'З\'єднай слова з перекладом', order:'Склади речення з поданих слів', type:'Впиши пропущене слово', tf:'Правда чи неправда?', speaking:'Послухай і повтори вголос', quiz:'Питання за сюжетом', final:'Фінальне завдання'};
function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var x = a[i]; a[i] = a[j]; a[j] = x; } return a; }
function norm(s) { return String(s || '').toLowerCase().replace(/[’']/g, "'").replace(/[^\p{L}\p{N}' ]+/gu, ' ').replace(/\s+/g, ' ').trim(); }
/* auto "reading" task: the lesson's own gap sentences joined into one short text with grammar choices */
function withReading(tasks) {
  if (!tasks.length || tasks.some(function (x) { return x.type === 'reading'; })) return tasks;
  var items = [];
  tasks.forEach(function (x) {
    if ((x.type === 'grammar' || x.type === 'subtitles') && /_{3,}/.test(x.q || '') && (x.options || []).length > 1) items.push({q:x.q, options:x.options, answer:+x.answer || 0});
    if (x.type === 'drill') (x.items || []).forEach(function (it) { if (/_{3,}/.test(it.q || '') && (it.options || []).length > 1) items.push({q:it.q, options:it.options, answer:+it.answer || 0}); });
  });
  items = items.filter(function (it) { return (it.q.match(/_{3,}/g) || []).length === 1; }).slice(0, 5);
  if (items.length < 2) return tasks;
  var rt = {type:'reading', items:items, _auto:1};
  var at = tasks.length; for (var i = tasks.length - 1; i > tasks.length / 2; i--) if (tasks[i].type === 'speaking' || tasks[i].type === 'final') at = i;
  return tasks.slice(0, at).concat([rt], tasks.slice(at));
}
var SKIPPABLE = {speaking:1, listening:1, type:1, final:1, subtitles:1};
/* ---------- personal dictionary + flashcards ---------- */
var WDEFS = {};
function loadDefs() { if (WDEFS[TARGET] !== undefined || TARGET === 'en') return Promise.resolve(); WDEFS[TARGET] = {}; return fetch('content/defs_' + TARGET + '.json').then(function (r) { return r.ok ? r.json() : {}; }).then(function (j) { WDEFS[TARGET] = j || {}; }).catch(function () {}); }
function wordMeaning(w) {
  if (LANG === TARGET) { var d = (WDEFS[TARGET] || {})[w.w]; if (d) return d; if (TARGET === 'en' && w.uk_en) return w.uk_en; return w.ex ? tx({uk:'напр.: ', pl:'np.: ', en:'e.g. '}) + w.ex : ''; }
  return lf(w, 'uk');
}
function wordsOf(lessons) {
  var seen = {}, out = [];
  lessons.forEach(function (l) {
    (lessonTasks(l) || []).forEach(function (tk) {
      if (tk.type === 'glossary') (tk.items || []).forEach(function (w) { if (!w.w || seen[w.w]) return; seen[w.w] = 1; out.push({w:w.w, m:wordMeaning(w), ipa:w.ipa || '', ex:w.ex || '', lesson:l.num}); });
      if (tk.type === 'match') (lf(tk, 'options') || []).forEach(function (o) { var s = String(o).split('='), k = (s[0] || '').trim(); if (!k || seen[k]) return; seen[k] = 1; var m = (s[1] || '').trim(); if (LANG === TARGET && (WDEFS[TARGET] || {})[k]) m = WDEFS[TARGET][k]; out.push({w:k, m:m, ipa:'', ex:'', lesson:l.num}); });
    });
  });
  return out;
}
var WKEY = function () { return 'ml_known_' + TARGET; };
function knownSet() { try { return JSON.parse(localStorage.getItem(WKEY()) || '{}'); } catch (e) { return {}; } }
function saveKnown(k) { try { localStorage.setItem(WKEY(), JSON.stringify(k)); } catch (e) {} }
function setKnownWord(word, val) { var k = knownSet(); if (val) k[word] = 1; else delete k[word]; saveKnown(k); if (USER) API.setKnown(TARGET, word, !!val).catch(function () {}); return k; }
function syncKnown() {
  if (!USER) return Promise.resolve();
  return API.knownList(TARGET).then(function (rows) {
    var local = knownSet(), server = {}; rows.forEach(function (r) { if (r.known !== false) server[r.word] = 1; });
    var synced = false; try { synced = localStorage.getItem(WKEY() + '_synced') === '1'; } catch (e) {}
    if (!synced) Object.keys(local).forEach(function (w) { if (!server[w]) { server[w] = 1; API.setKnown(TARGET, w, true).catch(function () {}); } });
    saveKnown(server); try { localStorage.setItem(WKEY() + '_synced', '1'); } catch (e) {}
  }).catch(function () {});
}
var WV = {mode:'list', q:'', only:'all'};
function viewWords() {
  if (!requireUser()) return Promise.resolve();
  return Promise.all([API.listCourses(false), API.myEnrollments(), API.myProgress(), loadDefs(), syncKnown()]).then(function (r) {
    var cs = r[0], enr = r[1], prog = r[2], done = {}; prog.forEach(function (p) { done[p.lesson_id] = 1; });
    var ids = isAdm() ? cs.map(function (c) { return c.id; }) : cs.filter(function (c) { return enr.indexOf(c.id) > -1; }).map(function (c) { return c.id; });
    return Promise.all(ids.map(function (id) { return API.listLessons(id); })).then(function (lists) {
      var L = function (uk, pl, en) { return tx({uk:uk, pl:pl, en:en}); };
      var groups = lists.map(function (ls, i) { var c = cs.filter(function (x) { return x.id === ids[i]; })[0]; var useLs = ls.filter(function (l) { return isAdm() || done[l.id]; }); return {c:c, words:wordsOf(useLs)}; }).filter(function (g) { return g.words.length; });
      var all = []; groups.forEach(function (g) { all = all.concat(g.words); });
      var known = knownSet();
      var head = '<div class="page"><div class="sec-head"><div class="eyebrow">' + FLAG[TARGET] + ' · ' + esc(langName(TARGET)) + '</div><h2>' + L('Мій словник', 'Mój słownik', 'My words') + '</h2><p class="lead">' + L('Слова з уроків, які ти пройшов. Повторюй їх у картках.', 'Słowa z lekcji, które ukończyłeś. Powtarzaj je na fiszkach.', 'Words from the lessons you have completed. Review them as flashcards.') + '</p></div>';
      if (!all.length) { $app.innerHTML = head + '<div class="empty">' + L('Тут з\'являться слова, щойно ти пройдеш перший урок.', 'Słowa pojawią się tu po ukończeniu pierwszej lekcji.', 'Words will appear here after your first lesson.') + ' <a href="#/trial">' + L('Почати урок', 'Zacznij lekcję', 'Start a lesson') + '</a></div></div>'; return; }
      var nKnown = all.filter(function (w) { return known[w.w]; }).length;
      var tabs = '<div class="row" style="gap:8px;flex-wrap:wrap;margin-bottom:14px"><button class="vtab' + (WV.mode === 'list' ? ' on' : '') + '" data-wm="list">📖 ' + L('Список', 'Lista', 'List') + '</button><button class="vtab' + (WV.mode === 'cards' ? ' on' : '') + '" data-wm="cards">🃏 ' + L('Картки', 'Fiszki', 'Flashcards') + '</button><span class="muted small" style="align-self:center">' + all.length + ' ' + L('слів', 'słów', 'words') + ' · ✓ ' + nKnown + ' ' + L('вивчено', 'opanowanych', 'learned') + '</span></div>';
      if (WV.mode === 'list') {
        $app.innerHTML = head + tabs + '<input class="inp-s" id="wq" placeholder="🔍 ' + L('Пошук слова', 'Szukaj słowa', 'Search') + '" value="' + esc(WV.q) + '" style="max-width:360px;margin-bottom:14px">' +
          groups.map(function (g) { return '<div class="panel" style="margin-bottom:16px"><h3 style="margin-bottom:10px">' + esc(tr(g.c, 'title')) + '</h3><div class="wlist">' + g.words.map(function (w) { return '<div class="wrow' + (known[w.w] ? ' known' : '') + '" data-w="' + esc(w.w.toLowerCase() + ' ' + String(w.m).toLowerCase()) + '"><button type="button" class="spk" data-say="' + esc(w.w) + '">🔊</button><b>' + esc(w.w) + '</b><span class="muted small">' + esc(w.ipa) + '</span><span>' + esc(w.m) + '</span><button type="button" class="wk" data-k="' + esc(w.w) + '" title="' + L('Вивчено', 'Opanowane', 'Learned') + '">' + (known[w.w] ? '✓' : '○') + '</button></div>'; }).join('') + '</div></div>'; }).join('') + '</div>';
        var wq = document.getElementById('wq'), filt = function () { var q = wq.value.toLowerCase().trim(); WV.q = wq.value; document.querySelectorAll('.wrow').forEach(function (r) { r.hidden = q && r.dataset.w.indexOf(q) < 0; }); }; wq.oninput = filt; filt();
        document.querySelectorAll('.wk').forEach(function (b) { b.onclick = function () { var k = setKnownWord(b.dataset.k, !knownSet()[b.dataset.k]); b.textContent = k[b.dataset.k] ? '✓' : '○'; b.parentNode.classList.toggle('known', !!k[b.dataset.k]); }; });
      } else {
        var deck = shuffle(all.filter(function (w) { return WV.only === 'all' || !known[w.w]; })), i = 0, flipped = false;
        $app.innerHTML = head + tabs + '<div class="row" style="gap:8px;margin-bottom:12px"><button class="vtab' + (WV.only === 'all' ? ' on' : '') + '" data-wo="all">' + L('Усі', 'Wszystkie', 'All') + '</button><button class="vtab' + (WV.only === 'new' ? ' on' : '') + '" data-wo="new">' + L('Ще не вивчені', 'Do nauki', 'To learn') + '</button><label class="muted small" style="align-self:center;margin-left:8px"><input type="checkbox" id="wrev"> ' + L('Спершу значення', 'Najpierw znaczenie', 'Meaning first') + '</label></div><div id="fcw"></div>';
        var rev = false, box = document.getElementById('fcw');
        var draw = function () {
          if (!deck.length) { box.innerHTML = '<div class="empty">🎉 ' + L('Усі слова вивчено!', 'Wszystkie słowa opanowane!', 'All words learned!') + '</div>'; return; }
          if (i >= deck.length) { box.innerHTML = '<div class="empty">✓ ' + L('Колоду пройдено.', 'Talia przerobiona.', 'Deck finished.') + ' <button class="btn btn-red btn-sm" type="button" id="fcAgain">' + L('Ще раз', 'Jeszcze raz', 'Again') + '</button></div>'; document.getElementById('fcAgain').onclick = function () { deck = shuffle(deck); i = 0; draw(); }; return; }
          var w = deck[i], front = rev ? w.m : w.w, back = rev ? w.w : w.m;
          box.innerHTML = '<div class="fc-meta muted small">' + (i + 1) + ' / ' + deck.length + '</div><button type="button" class="fcard' + (flipped ? ' flip' : '') + '" id="fcard"><span class="fc-in"><span class="fc-f"><b>' + esc(front) + '</b>' + (!rev && w.ipa ? '<small>' + esc(w.ipa) + '</small>' : '') + '<em>' + L('натисни, щоб перевернути', 'kliknij, aby odwrócić', 'tap to flip') + '</em></span><span class="fc-b"><b>' + esc(back) + '</b>' + (w.ex ? '<small>' + esc(w.ex) + '</small>' : '') + '</span></span></button>' +
            '<div class="row fc-btns"><button type="button" class="spk" id="fcSay" data-say="' + esc(w.w) + '">🔊</button><button class="btn btn-ghost" type="button" id="fcAgainW">↺ ' + L('Ще вчу', 'Jeszcze się uczę', 'Still learning') + '</button><button class="btn btn-red" type="button" id="fcKnow">✓ ' + L('Знаю', 'Znam', 'I know it') + '</button></div>';
          document.getElementById('fcard').onclick = function () { flipped = !flipped; this.classList.toggle('flip', flipped); };
          document.getElementById('fcSay').onclick = function () { say(w.w); };
          document.getElementById('fcKnow').onclick = function () { setKnownWord(w.w, true); i++; flipped = false; draw(); };
          document.getElementById('fcAgainW').onclick = function () { if (knownSet()[w.w]) setKnownWord(w.w, false); deck.push(w); i++; flipped = false; draw(); };
        };
        document.getElementById('wrev').onchange = function (e) { rev = e.target.checked; flipped = false; draw(); };
        document.querySelectorAll('[data-wo]').forEach(function (b) { b.onclick = function () { WV.only = b.dataset.wo; viewWords(); }; });
        draw();
      }
      document.querySelectorAll('[data-wm]').forEach(function (b) { b.onclick = function () { WV.mode = b.dataset.wm; viewWords(); }; });
      document.querySelectorAll('.wrow .spk').forEach(function (s) { s.onclick = function () { say(s.dataset.say); }; });
    });
  });
}
function ltSlim(m) { if (m.msg) return m; return {o:m.offset, l:m.length, msg:m.message, r:(m.replacements || []).slice(0, 3).map(function (x) { return x.value; })}; }
function ltHtml(text, ms) {
  ms = ms.map(function (m) { return m.msg ? m : ltSlim(m); });
  if (ms.length === 1 && !ms[0].l) return '<b>⚠ ' + esc(ms[0].msg) + '</b>';
  if (!ms.length) return '<b>✓ ' + tx({uk:'Помилок не знайдено. Чудово!', pl:'Nie znaleziono błędów. Świetnie!', en:'No mistakes found. Great!'}) + '</b>';
  return '<b>' + tx({uk:'Знайдено можливих помилок: ', pl:'Znalezione możliwe błędy: ', en:'Possible mistakes found: '}) + ms.length + '</b><ol>' + ms.slice(0, 20).map(function (m) { return '<li><span class="ltbad">' + esc(text.substr(m.o, m.l)) + '</span>' + (m.r && m.r.length ? ' → <span class="ltgood">' + esc(m.r.join(' / ')) + '</span>' : '') + '<br><span class="muted small">' + esc(m.msg) + '</span></li>'; }).join('') + '</ol>';
}
function renderWritings(host) {
  if (!host || !USER) return;
  API.myWritings().then(function (ws) {
    if (!ws.length) return;
    var L = function (uk, pl, en) { return tx({uk:uk, pl:pl, en:en}); };
    var box = document.createElement('div'); box.className = 'box'; box.id = 'myTexts'; box.style.marginTop = '18px';
    box.innerHTML = '<h4>✍ ' + L('Мої тексти', 'Moje teksty', 'My texts') + '</h4><div class="wtexts">' + ws.map(function (w) {
      var n = w.issues && w.issues.ai ? (w.issues.errors || []).length : (w.issues || []).length, st = w.status === 'pending' ? '<span class="pill warn">⏳ ' + L('чекає на перевірку', 'czeka na sprawdzenie', 'waiting for check') + '</span>' : '<span class="pill ' + (n ? 'warn' : 'ok') + '">' + (n ? n + ' ' + L('помилок', 'błędów', 'mistakes') : '✓ ' + L('без помилок', 'bez błędów', 'no mistakes')) + '</span>' + (w.seen ? '' : ' <span class="pill ok">' + L('нове', 'nowe', 'new') + '</span>');
      return '<details class="wtxt" data-id="' + esc(w.id) + '"' + (w.seen ? '' : ' data-unseen="1"') + '><summary><span>' + FLAG[w.target || 'en'] + ' · ' + fmtDate(w.created_at) + '</span><span class="muted small wsnip">' + esc(String(w.text).slice(0, 60)) + '…</span>' + st + '</summary><div class="wbody"><p class="wfull">' + esc(w.text) + '</p>' + (w.status === 'pending' ? '<p class="muted small">' + L('Ми перевіримо текст автоматично, щойно сервіс буде доступний. Сайт повідомить, коли результат буде готовий.', 'Sprawdzimy tekst automatycznie, gdy usługa będzie dostępna. Strona da znać, gdy wynik będzie gotowy.', 'We will check it automatically when the service is available. The site will notify you.') + '</p>' : '<div class="ltbox">' + issuesHtml(w.text, w.issues) + '</div>') + '</div></details>';
    }).join('') + '</div>';
    host.appendChild(box);
    box.querySelectorAll('details[data-unseen]').forEach(function (d) { d.addEventListener('toggle', function () { if (d.open && d.dataset.unseen) { delete d.dataset.unseen; API.updateWriting(+d.dataset.id || d.dataset.id, {seen:true}).catch(function () {}); } }); });
    if (location.hash.indexOf('texts') > -1) box.scrollIntoView({behavior:'smooth'});
  }).catch(function () {});
}
function aiCheck(text, task, tg) {
  var C = window.MOVILANG_CONFIG || {};
  if (!C.SUPABASE_URL || !C.SUPABASE_ANON_KEY) return Promise.reject(new Error('demo'));
  return fetch(C.SUPABASE_URL + '/functions/v1/ai-check', {method:'POST', headers:{'Content-Type':'application/json', apikey:C.SUPABASE_ANON_KEY, Authorization:'Bearer ' + C.SUPABASE_ANON_KEY}, body:JSON.stringify({text:text, task:task || '', target:tg, support:LANG, level:'B1'})})
    .then(function (r) { return r.json().then(function (j) { if (!r.ok || j.error) { var em = (j.error || 'ai') + (j.detail ? ': ' + j.detail : ''); if (isAdm()) toast('AI: ' + em.slice(0, 220), 'err'); try { console.warn('ai-check', em); } catch (e) {} throw new Error(em); } return j; }); });
}
function smartCheck(text, task, tg) {
  tg = tg || TARGET;
  return aiCheck(text, task, tg).then(function (o) {
    var iss = {ai:1, score:o.score, lang_ok:o.lang_ok, task_done:o.task_done, comment:o.comment, errors:o.errors || []};
    return {issues:iss, score:o.score, wrongLang:!o.lang_ok, pass:!!(o.lang_ok && o.task_done && o.score >= 60)};
  });
}
function aiHtml(o) {
  var L = function (uk, pl, en) { return tx({uk:uk, pl:pl, en:en}); };
  var sc = +o.score || 0, col = sc >= 80 ? 'ok' : sc >= 60 ? 'warn' : 'bad';
  return '<div class="aihead"><span class="aiscore ' + col + '">' + sc + '<small>/100</small></span><div><b>🤖 ' + L('Оцінка ШІ-вчителя', 'Ocena nauczyciela AI', 'AI teacher feedback') + '</b><div class="muted small">' + (o.lang_ok ? '✓ ' + L('правильна мова', 'właściwy język', 'right language') : '⚠ ' + L('не та мова', 'zły język', 'wrong language')) + ' · ' + (o.task_done ? '✓ ' + L('завдання виконано', 'zadanie wykonane', 'task done') : '⚠ ' + L('завдання виконано не повністю', 'zadanie wykonane częściowo', 'task not fully done')) + '</div></div></div>' +
    (o.comment ? '<p class="aicomment">' + esc(o.comment) + '</p>' : '') +
    ((o.errors || []).length ? '<ol>' + o.errors.map(function (e) { return '<li><span class="ltbad">' + esc(e.wrong) + '</span> → <span class="ltgood">' + esc(e.fix) + '</span><br><span class="muted small">' + esc(e.why) + '</span></li>'; }).join('') + '</ol>' : '<b>✓ ' + L('Помилок не знайдено.', 'Nie znaleziono błędów.', 'No mistakes found.') + '</b>') +
    '<p class="muted small" style="margin-top:8px">' + L('Оцінку зробив ШІ — він може помилятися.', 'Ocenę wystawiło AI — może się mylić.', 'Graded by AI — it can make mistakes.') + '</p>';
}
function issuesHtml(text, iss) { return iss && iss.ai ? aiHtml(iss) : ltHtml(text, iss || []); }
var PW_BUSY = false;
function processPendingWritings() {
  if (!USER || PW_BUSY) return; PW_BUSY = true;
  API.myWritings().then(function (ws) {
    var pend = ws.filter(function (w) { return w.status === 'pending'; }).slice(0, 3), okN = 0;
    return pend.reduce(function (pr, w) { return pr.then(function () {
      return smartCheck(w.text, w.task, w.target || TARGET).then(function (r) { okN++; return API.updateWriting(w.id, {status:'checked', issues:r.issues, score:r.score, checked_at:new Date().toISOString(), seen:false}); }).catch(function (e) { if (isAdm()) toast('AI: ' + ((e && e.message) || e)); });
    }); }, Promise.resolve()).then(function () { if (okN) { if (API.clearCache) API.clearCache(); toast('✓ ' + tx({uk:'Твій текст перевірено! Результат — у Кабінет → Мої тексти.', pl:'Twój tekst został sprawdzony! Wynik w Konto → Moje teksty.', en:'Your text has been checked! See Account → My texts.'})); } });
  }).catch(function () {}).then(function () { PW_BUSY = false; });
}
function runPlayer(container, lesson, onFinish, ctxLs) {
  var hints = {}, tStart = {}, durs = {}, tasks = withReading((lessonTasks(lesson) || []).filter(function (x) { return !(x.say && x.type !== 'speaking'); })), cur = 0, res = [], finalText = '', snaps = [], maxReached = 0;
  var FREE = isAdm() && ADMIN_MODE; if (FREE) maxReached = tasks.length - 1;
  var scored = tasks.filter(function (x) { return !isInfo(x.type); }).length;
  function numOf(i) { var n = 0; for (var j = 0; j <= i; j++) if (!isInfo(tasks[j].type)) n++; return n; }
  function tag(tk) { return lf(tk, 'label') || ttName(tk.type); }
  container.innerHTML = (FREE ? '<div class="admnav">🛠 ' + tx({uk:'Режим адміна: можна вільно переходити між завданнями справа, не відповідаючи.', pl:'Tryb admina: możesz swobodnie przechodzić między zadaniami po prawej, bez odpowiadania.', en:'Admin mode: jump freely between tasks on the right without answering.'}) + '</div>' : '') + '<div class="trial"><div class="tcard" id="tcard" aria-live="polite"></div><div class="tside" id="tside"></div></div>';
  var card = container.querySelector('#tcard'), side = container.querySelector('#tside');
  function renderSide() { side.innerHTML = tasks.map(function (tk, i) { var c = i === cur ? 'on' : ''; if (res[i] === true) c += ' ok'; if (res[i] === false) c += ' bad'; return '<button type="button" class="tstep ' + c + (i <= maxReached && i !== cur ? ' nav' : '') + '" data-go="' + i + '"' + (i > maxReached ? ' disabled' : '') + '><i>' + (tk.type === 'intro' ? '▶' : isInfo(tk.type) ? '📖' : numOf(i)) + '</i>' + esc(tag(tk)) + (res[i] != null ? '' : '') + '</button>'; }).join('');
    side.querySelectorAll('[data-go]').forEach(function (b) { b.onclick = function () { var i = +b.dataset.go; if (i <= maxReached && i !== cur) { cur = i; render(); } }; }); }
  function plainQ(s) { return String(s || '').replace(/<[^>]+>/g, '').replace(/_{2,}/g, '…'); }
  function qHtml(tk) { return esc(lf(tk, 'q')).replace(/&lt;(\/?)(b|i)&gt;/g, '<$1$2>').replace(/_{3,}/g, '<span class="gap">____</span>'); }
  function head(tk) {
    var n = numOf(cur);
    return '<div class="ttop"><span class="ttag">' + esc(tag(tk)) + '</span>' + (isInfo(tk.type) ? '' : '<span class="tcount">' + n + ' / ' + scored + '</span>') + '</div>' +
      (tk.img ? '<div class="illu">' + illu(tk.img) + '</div>' : '') +
      (tk.ins ? '<div class="tins">' + esc(lf(tk, 'ins')) + '</div>' : TASK_INS[tk.type] ? '<div class="tins">' + t(TASK_INS[tk.type]) + '</div>' : '') +
      (tk.scene ? '<div class="tscene"><b>' + t('Сцена:') + '</b> ' + esc(lf(tk, 'scene')) + '</div>' : '') + '<div class="tq' + ((isInfo(tk.type) && tk.type !== 'intro') || tk.type === 'quest' ? ' tq-info' : '') + '">' + (isInfo(tk.type) ? esc(lf(tk, 'q') || '') : qHtml(tk)) + (!isInfo(tk.type) && tk.type !== 'quest' && tk.q && !tk['q_' + LANG] ? ' <button type="button" class="spk" data-say="' + esc(plainQ(tk.q)) + '" title="' + tx({uk:'Прослухати', pl:'Odsłuchaj', en:'Listen'}) + '">🔊</button>' : '') + '</div>' +
      (!isInfo(tk.type) && !tk['q_' + LANG] && tk['qt_' + LANG] ? '<div class="qtrw"><button type="button" class="qtrb" id="qtrBtn">🌐 ' + tx({uk:'Перекласти питання', pl:'Przetłumacz pytanie', en:'Translate the question'}) + '</button><div class="qtrt" id="qtrText" hidden>' + esc(tk['qt_' + LANG]).replace(/&lt;(\/?)(b|i)&gt;/g, '<$1$2>').replace(/_{3,}/g, '<span class="gap">____</span>') + '</div></div>' : '') +
      (gRuleTask(tk, lesson) ? '<div class="rulew"><button type="button" class="qtrb rulebtn" id="ruleBtn">📘 ' + tx({uk:'Нагадати правило', pl:'Przypomnij zasadę', en:'Show the rule'}) + '</button><div class="rulebox" id="ruleBox" hidden></div></div>' : '') +
      (tk.say && tk.type === 'speaking' ? '<div class="sayline">' + esc(tk.say) + '</div>' : '');
  }
  function foot() { var tk0 = tasks[cur] || {}; return '<div class="tfb" id="tfb"></div><div class="tnav"><span class="hint">' + (SKIPPABLE[tk0.type] && tk0.type !== 'speaking' ? '<button type="button" class="skipb" id="skipErr">' + tx({uk:'Не можу зараз (пропустити)', pl:'Nie mogę teraz (pomiń)', en:'Can\'t do it now (skip)'}) + '</button> ' : '') + '<span class="hint">' + t('Завдання') + ': ' + FLAG[TARGET] + ' · ' + t('Підказки') + ': ' + FLAG[LANG] + '</span></span><button class="btn btn-red" type="button" id="tnext" hidden>' + t('Далі') + '</button></div>'; }
  function skipMsg() { return '⚠ ' + tx({uk:'Завдання пропущено — зараховано як помилку. Можна повернутися до нього, пройшовши урок ще раз.', pl:'Zadanie pominięte — liczy się jako błąd. Możesz do niego wrócić, przechodząc lekcję jeszcze raz.', en:'Task skipped — it counts as a mistake. You can come back to it by retaking the lesson.'}); }
  var firstR = true;
  function render() {
    render0();
    var sk = card.querySelector('#skipErr'); if (sk) sk.onclick = function () { if (snaps[cur] || res[cur] != null) return; sk.disabled = true; done(false, skipMsg()); };
    if (firstR) { firstR = false; return; }
    var r = card.getBoundingClientRect(); if (r.top < 70 || r.top > window.innerHeight * 0.35) window.scrollTo({top:window.pageYOffset + r.top - 84, behavior:'smooth'});
  }
  function render0() {
    card.classList.remove('tin'); void card.offsetWidth; card.classList.add('tin');
    var tk = tasks[cur]; if (cur > maxReached) maxReached = cur; if (!snaps[cur] && tStart[cur] == null) tStart[cur] = Date.now(); renderSide();
    if (snaps[cur]) { card.innerHTML = '<div class="tlock">🔒 ' + t('Відповідь уже дано. Щоб змінити, пройди урок ще раз.') + '</div>' + snaps[cur]; bindSay(tk); var nb = card.querySelector('#tnext'); if (nb) { nb.hidden = false; nb.disabled = false; nb.textContent = cur < tasks.length - 1 ? t('Далі') : t('Показати результат'); nb.onclick = next; } return; }
    var h = head(tk), type = tk.type;
    if (type === 'intro') {
      h += '<ul class="goals">' + (lf(tk, 'options') || []).map(function (o) { return '<li>' + esc(o) + '</li>'; }).join('') + '</ul><div class="row"><button class="btn btn-red" type="button" id="tstart"><span class="play"></span>' + (tk.tip ? esc(lf(tk, 'tip')) : 'Start') + '</button><span class="hint">' + scored + ' ' + t('завдань') + ' · ~' + Math.max(5, Math.round(scored * 1.5)) + ' ' + t('хв') + '</span></div>';
      card.innerHTML = h; card.querySelector('#tstart').onclick = function () { res[cur] = null; next(); }; bindSay(tk); return;
    }
    if (type === 'cards' || type === 'glossary') {
      if (type === 'cards') h += '<div class="pcards">' + (tk.cards || []).map(function (c) { return '<div class="pcard' + (c.upd ? ' upd' : '') + '"><div class="pc-n"><b>' + esc(LANG === 'uk' ? c.uk : c.en) + '</b>' + (LANG === 'uk' ? ' <span class="muted small">' + esc(c.en) + '</span>' : '') + (c.upd ? ' <span class="pc-u">' + tx({uk:'оновлено', pl:'nowość', en:'updated'}) + '</span>' : '') + '</div><div class="pc-r">' + esc(lf(c, 'role')) + '</div></div>'; }).join('') + '</div>';
      else h += '<div class="gloss">' + (tk.items || []).map(function (w) { return '<details class="gw"><summary><b>' + esc(w.w) + '</b> <span class="spk spk-in" role="button" data-say="' + esc(w.w) + '">🔊</span> <span class="gw-ipa">' + esc(w.ipa || '') + '</span><span class="gw-uk">' + esc(wordMeaning(w)) + '</span></summary><div class="gw-b"><div class="gw-meta">' + esc(w.pos || '') + (w.lvl ? ' · <b>' + esc(w.lvl === 'HP' ? tx({uk:'світ Гаррі Поттера', pl:'świat Harry\'ego Pottera', en:'Harry Potter world'}) : w.lvl) + '</b>' : '') + '</div>' + (w.who ? '<p>🎬 ' + esc(lf(w, 'who')) + '</p>' : '') + (w.line ? '<p class="gw-line">«' + esc(w.line) + '» <span class="spk spk-in" role="button" data-say="' + esc(w.line) + '">🔊</span></p>' : '') + (w.ex ? '<p class="gw-ex">✎ ' + esc(w.ex) + ' <span class="spk spk-in" role="button" data-say="' + esc(w.ex) + '">🔊</span></p>' : '') + '</div></details>'; }).join('') + '</div>';
      h += '<div class="row"><button class="btn btn-red" type="button" id="tstart">' + tx({uk:'Далі', pl:'Dalej', en:'Next'}) + '</button></div>';
      card.innerHTML = h; card.querySelector('#tstart').onclick = function () { res[cur] = null; next(); }; bindSay(tk); return;
    }
    if (type === 'drill') {
      var its = tk.items || [], got = 0, answered = 0;
      h += '<div class="drill">' + its.map(function (it, k) { return '<div class="dr-it" data-k="' + k + '"><div class="dr-q"><span class="dr-n">' + (k + 1) + '</span> ' + qHtml({q:lf(it, 'q')}) + (it['q_' + LANG] ? '' : ' <button type="button" class="spk" data-say="' + esc(plainQ(it.q)) + '">🔊</button>') + '</div><div class="dr-opts">' + (it.options || []).map(function (o, j) { return '<button type="button" class="dr-o" data-j="' + j + '">' + esc(o) + '</button>'; }).join('') + '</div><div class="dr-fb"></div></div>'; }).join('') + '</div><div class="dr-score" id="drScore">0 / ' + its.length + '</div>' + foot();
      card.innerHTML = h; bindSay(tk);
      card.querySelectorAll('.dr-it').forEach(function (row) {
        var it = its[+row.dataset.k];
        row.querySelectorAll('.dr-o').forEach(function (b) { b.onclick = function () {
          var j = +b.dataset.j, ok = j === +it.answer; answered++; if (ok) got++;
          row.querySelectorAll('.dr-o').forEach(function (x) { x.disabled = true; if (+x.dataset.j === +it.answer) x.classList.add('right'); });
          if (!ok) b.classList.add('wrong');
          var g = row.querySelector('.gap'); if (g) g.textContent = it.options[it.answer];
          row.classList.add(ok ? 'ok' : 'bad');
          row.querySelector('.dr-fb').textContent = (ok ? '✓ ' : '✗ ') + (lf(it, 'exp') || '');
          card.querySelector('#drScore').textContent = got + ' / ' + its.length;
          if (answered === its.length) done(got / its.length >= 0.7, got + ' / ' + its.length + '. ' + (lf(tk, 'tip') || ''));
        }; });
      });
      if (FREE && cur < tasks.length - 1) { var nbd = card.querySelector('#tnext'); nbd.hidden = false; nbd.textContent = '⏭ ' + tx({uk:'Пропустити (адмін)', pl:'Pomiń (admin)', en:'Skip (admin)'}); nbd.onclick = function () { cur++; render(); }; }
      return;
    }
    if (type === 'quest') {
      h += '<div class="quest" id="quest"></div>' + foot(); card.innerHTML = h; bindSay(tk);
      var qbox = card.querySelector('#quest'), steps = tk.steps || {}, path = [];
      var qstep = function (id) {
        var e = (tk.endings || {})[id];
        if (e) { qbox.innerHTML = '<div class="qend ' + (e.good ? 'good' : 'bad') + '"><b>' + esc(lf(e, 'title')) + '</b><p>' + esc(lf(e, 'text')) + '</p></div>'; done(!!e.good, (e.good ? t('Правильно! ') : t('Майже. ')) + (lf(tk, 'tip') || '')); return; }
        var st = steps[id]; if (!st) return; path.push(id);
        qbox.innerHTML = '<div class="qstep"><div class="qnum">' + tx({uk:'Крок', pl:'Krok', en:'Step'}) + ' ' + path.length + '</div>' + (st.scene ? '<div class="tscene">' + esc(lf(st, 'scene')) + '</div>' : '') + '<div class="tq">' + qHtml({q:st.q}) + ' <button type="button" class="spk" data-say="' + esc(plainQ(st.q)) + '">🔊</button></div><div class="topts">' + (st.choices || []).map(function (c, i) { return '<button class="qopt topt" type="button" data-qi="' + i + '">' + esc(c.t) + '</button>'; }).join('') + '</div><div class="qfb" id="qfb"></div></div>';
        qbox.querySelectorAll('.spk').forEach(function (s) { s.onclick = function () { say(s.dataset.say); }; });
        qbox.querySelectorAll('[data-qi]').forEach(function (b) { b.onclick = function () {
          var c = st.choices[+b.dataset.qi]; qbox.querySelectorAll('[data-qi]').forEach(function (x) { x.disabled = true; }); b.classList.add(c.ok === false ? 'wrong' : 'right');
          var fb = qbox.querySelector('#qfb'); fb.innerHTML = (c.fb ? '<p>' + esc(lf(c, 'fb')) + '</p>' : '') + '<button class="btn btn-ghost btn-sm" type="button" id="qgo">' + tx({uk:'Далі', pl:'Dalej', en:'Next'}) + ' →</button>';
          fb.querySelector('#qgo').onclick = function () { qstep(c.next); };
        }; });
      };
      if (FREE && cur < tasks.length - 1) { var nbq = card.querySelector('#tnext'); nbq.hidden = false; nbq.textContent = '⏭ ' + tx({uk:'Пропустити (адмін)', pl:'Pomiń (admin)', en:'Skip (admin)'}); nbq.onclick = function () { cur++; render(); }; }
      qstep(tk.start || Object.keys(steps)[0]); return;
    }
    if (type === 'reading') {
      var its = tk.items || [];
      h = h.replace('<div class="tq', '<div class="tins">' + tx({uk:'Прочитай текст і обери правильні форми', pl:'Przeczytaj tekst i wybierz poprawne formy', en:'Read the text and choose the correct forms'}) + '</div><div class="tq');
      h += '<div class="rtext">' + its.map(function (it, k) { var parts = esc(String(it.q).replace(/<[^>]+>/g, '')).split(/_{3,}/); return parts[0] + '<select class="rsel" data-k="' + k + '"><option value="">…</option>' + it.options.map(function (o, j) { return '<option value="' + j + '">' + esc(o) + '</option>'; }).join('') + '</select>' + (parts[1] || ''); }).join(' ') + '</div><div class="row"><button class="btn btn-red" type="button" id="rcheck">' + t('Перевірити') + '</button></div>';
      h += foot(); card.innerHTML = h; bindSay(tk);
      card.querySelector('#rcheck').onclick = function () {
        var sels = card.querySelectorAll('.rsel'), good = 0;
        if ([].some.call(sels, function (s) { return s.value === ''; })) { var fb0 = card.querySelector('#tfb'); fb0.className = 'tfb err'; fb0.textContent = tx({uk:'Заповни всі пропуски.', pl:'Uzupełnij wszystkie luki.', en:'Fill in all the gaps.'}); return; }
        sels.forEach(function (s) { var it = its[+s.dataset.k], ok = +s.value === it.answer; if (ok) good++; s.classList.add(ok ? 'right' : 'wrong'); if (!ok) s.insertAdjacentHTML('afterend', '<span class="rfix">' + esc(it.options[it.answer]) + '</span>'); s.disabled = true; });
        var ok = good >= Math.ceil(its.length * 0.67); this.disabled = true;
        done(ok, (ok ? t('Правильно! ') : t('Майже. ')) + good + ' / ' + its.length);
      };
      return;
    }
    if (type === 'final') h += '<textarea class="inp-s" id="tfinal" rows="7" placeholder="' + t('Пиши мовою, яку вивчаєш…') + '"></textarea><div class="row"><button class="btn btn-red" type="button" id="tsubmit">' + t('Зберегти відповідь') + '</button><span class="hint" id="wc">0</span></div>';
    else if (type === 'speaking') h += '<div class="mic"><button class="btn btn-red" type="button" id="micBtn">🎤 ' + t('Натисни і говори') + '</button><div class="mic-out" id="micOut" aria-live="polite"></div></div><div class="row"><button class="btn btn-ghost btn-sm" type="button" id="micAccept" hidden>' + t('Зарахувати цю спробу') + '</button><button class="topt" type="button" data-s="0" style="flex:0 0 auto">' + t('Пропустити') + '</button></div>';
    else if (type === 'type') h += '<div class="row"><input class="inp-s" id="ttype" autocomplete="off" spellcheck="false" placeholder="' + t('Твоя відповідь') + '" style="flex:1;min-width:200px"><button class="btn btn-red" type="button" id="tcheck">' + t('Перевірити') + '</button></div>';
    else if (type === 'order') h += '<div class="oline" id="oline"><span class="hint">' + t('Натискай слова в правильному порядку…') + '</span></div><div class="ochips" id="ochips">' + shuffle((tk.options || []).map(function (w, i) { return {w:w, i:i}; })).map(function (o) { return '<button class="ochip" type="button" data-oi="' + o.i + '">' + esc(o.w) + '</button>'; }).join('') + '</div><div class="row"><button class="btn btn-red" type="button" id="tcheck">' + t('Перевірити') + '</button><button class="btn btn-ghost btn-sm" type="button" id="oclear">' + t('Очистити') + '</button></div>';
    else if (type === 'match') {
      var pairs = (lf(tk, 'options') || []).map(function (p, i) { var s = String(p).split('='), l0 = s[0].trim(), dd = LANG === TARGET && (WDEFS[TARGET] || {})[l0]; return {l:l0, r:dd || (s[1] || '').trim(), i:i}; });
      h += '<div class="match"><div class="mcol">' + pairs.map(function (p) { return '<button class="mitem" type="button" data-ml="' + p.i + '">' + esc(p.l) + '<span class="spk spk-in" role="button" data-say="' + esc(p.l) + '">🔊</span></button>'; }).join('') + '</div><div class="mcol">' + shuffle(pairs).map(function (p) { return '<button class="mitem" type="button" data-mr="' + p.i + '">' + esc(p.r) + '</button>'; }).join('') + '</div></div>';
    }
    else h += '<div class="topts">' + (tk.options || []).map(function (o, i) { return '<button class="topt" type="button" data-i="' + i + '">' + esc(tk.type === 'tf' ? t(o === 'True' ? 'Правда' : 'Неправда') : o) + (tk.type !== 'tf' ? '<span class="spk spk-in" role="button" data-say="' + esc(o) + '">🔊</span>' : '') + '</button>'; }).join('') + '</div>';
    h += foot(); card.innerHTML = h; bindSay(tk);
    if (FREE && cur < tasks.length - 1) { var nb2 = card.querySelector('#tnext'); nb2.hidden = false; nb2.textContent = '⏭ ' + tx({uk:'Пропустити (адмін)', pl:'Pomiń (admin)', en:'Skip (admin)'}); nb2.onclick = function () { cur++; render(); }; }
    card.querySelectorAll('.topt').forEach(function (b) { b.onclick = function () { answerMC(b); }; });
    if (type === 'type') { var inp = card.querySelector('#ttype'); inp.focus(); var chk = function () { var ok = (tk.options || []).some(function (a) { return norm(a) === norm(inp.value); }); inp.disabled = true; done(ok, (ok ? t('Правильно! ') : t('Відповідь: ') + tk.options[0] + '. ') + (lf(tk, 'tip') || '')); }; card.querySelector('#tcheck').onclick = chk; inp.onkeydown = function (e) { if (e.key === 'Enter') chk(); }; }
    if (type === 'order') {
      var picked = [], line = card.querySelector('#oline');
      var draw = function () { line.innerHTML = picked.length ? picked.map(function (i, pos) { return '<button class="ochip in" type="button" data-pos="' + pos + '">' + esc(tk.options[i]) + '</button>'; }).join('') : '<span class="hint">' + t('Натискай слова в правильному порядку…') + '</span>'; line.querySelectorAll('[data-pos]').forEach(function (b) { b.onclick = function () { var i = picked.splice(+b.dataset.pos, 1)[0]; card.querySelector('[data-oi="' + i + '"]').disabled = false; draw(); }; }); };
      card.querySelectorAll('[data-oi]').forEach(function (b) { b.onclick = function () { picked.push(+b.dataset.oi); b.disabled = true; draw(); }; });
      card.querySelector('#oclear').onclick = function () { picked = []; card.querySelectorAll('[data-oi]').forEach(function (b) { b.disabled = false; }); draw(); };
      card.querySelector('#tcheck').onclick = function () { var got = picked.map(function (i) { return tk.options[i]; }).join(' '), ok = norm(got) === norm(tk.options.join(' ')); line.classList.add(ok ? 'good' : 'bad'); card.querySelectorAll('.ochip').forEach(function (x) { x.disabled = true; }); done(ok, (ok ? t('Правильно! ') : t('Правильно: ') + tk.options.join(' ') + '. ') + (lf(tk, 'tip') || '')); };
    }
    if (type === 'match') {
      var selL = null, matched = 0, errors = 0, total = (lf(tk, 'options') || []).length;
      card.querySelectorAll('[data-ml]').forEach(function (b) { b.onclick = function () { card.querySelectorAll('[data-ml]').forEach(function (x) { x.classList.remove('sel'); }); selL = b; b.classList.add('sel'); }; });
      card.querySelectorAll('[data-mr]').forEach(function (b) { b.onclick = function () {
        if (!selL) return;
        if (selL.dataset.ml === b.dataset.mr) { selL.classList.remove('sel'); selL.classList.add('right'); b.classList.add('right'); selL.disabled = b.disabled = true; selL = null; matched++; if (matched === total) done(errors <= 1, (errors <= 1 ? t('Правильно! ') : t('Помилок: ') + errors + '. ') + (lf(tk, 'tip') || '')); }
        else { errors++; b.classList.add('wrong'); setTimeout(function () { b.classList.remove('wrong'); }, 500); }
      }; });
    }
    if (type === 'speaking') bindMic(tk);
    var ta = card.querySelector('#tfinal');
    if (ta) { var minW = +(tk.answer || 40) || 40; ta.oninput = function () { card.querySelector('#wc').textContent = ta.value.trim().split(/\s+/).filter(Boolean).length + ' / ' + minW + ' ' + t('слів'); };
      card.querySelector('#tsubmit').onclick = function () { var n = ta.value.trim().split(/\s+/).filter(Boolean).length; if (n < minW) { var fb = card.querySelector('#tfb'); fb.className = 'tfb err'; fb.textContent = t('Напиши щонайменше ') + minW + ' ' + t('слів') + ' (' + n + ').'; return; } finalText = ta.value.trim(); ta.disabled = true; var sb0 = card.querySelector('#tsubmit'); sb0.disabled = true; sb0.textContent = '⏳ ' + tx({uk:'Перевіряю текст…', pl:'Sprawdzam tekst…', en:'Checking your text…'});
        var fin0 = function () { sb0.textContent = '✓ ' + tx({uk:'Збережено', pl:'Zapisano', en:'Saved'}); };
        var taskQ = String(lf(tk, 'q') || tk.q || '').replace(/<[^>]+>/g, '');
        var base = {lesson_id:lesson.id || null, target:TARGET, support:LANG, task:taskQ, text:finalText};
        sb0.textContent = '⏳ ' + tx({uk:'Вчитель-ШІ перевіряє…', pl:'Nauczyciel AI sprawdza…', en:'AI teacher is checking…'});
        smartCheck(finalText, taskQ, TARGET).then(function (r) {
          fin0(); var box = document.createElement('div'); box.className = 'ltbox'; box.innerHTML = issuesHtml(finalText, r.issues); ta.insertAdjacentElement('afterend', box);
          if (USER) API.saveWriting(Object.assign({}, base, {status:'checked', issues:r.issues, score:r.score, checked_at:new Date().toISOString(), seen:true})).catch(function () {});
          var msg = r.wrongLang ? tx({uk:'Текст написано не тією мовою. ', pl:'Tekst jest w innym języku. ', en:'Wrong language. '}) : r.pass ? t('Відповідь збережено! ') : tx({uk:'Текст збережено. Переглянь виправлення вище. ', pl:'Tekst zapisany. Przejrzyj poprawki powyżej. ', en:'Text saved. Review the corrections above. '});
          done(!!r.pass, msg + (lf(tk, 'tip') || ''));
        }).catch(function () {
          fin0(); var wait = document.createElement('div'); wait.className = 'ltbox ltwait';
          wait.innerHTML = '<b>⏳ ' + tx({uk:'Перевірку тексту відкладено', pl:'Sprawdzenie tekstu odłożone', en:'Text check postponed'}) + '</b><p>' + (USER ? tx({uk:'Сервіс перевірки зараз перевантажений. Твій текст збережено — ми перевіримо його автоматично, щойно сервіс звільниться. Результат побачиш у <a href="#/cabinet">Кабінет → Мої тексти</a>, а коли він буде готовий, сайт тебе повідомить.', pl:'Usługa sprawdzania jest teraz przeciążona. Twój tekst jest zapisany — sprawdzimy go automatycznie, gdy usługa będzie dostępna. Wynik zobaczysz w <a href="#/cabinet">Konto → Moje teksty</a>, a strona da ci znać, gdy będzie gotowy.', en:'The checking service is busy right now. Your text is saved — we will check it automatically as soon as it is available. You will find the result in <a href="#/cabinet">Account → My texts</a>, and the site will let you know when it is ready.'}) : tx({uk:'Сервіс перевірки зараз перевантажений. Створи кабінет, щоб зберігати тексти й отримувати перевірку пізніше.', pl:'Usługa sprawdzania jest teraz przeciążona. Załóż konto, aby zapisywać teksty i otrzymać sprawdzenie później.', en:'The checking service is busy. Create an account to save texts and get them checked later.'})) + '</p>';
          ta.insertAdjacentElement('afterend', wait);
          if (USER) API.saveWriting(Object.assign({}, base, {status:'pending'})).then(function () { setTimeout(processPendingWritings, 60000); }).catch(function () {});
          done(true, t('Відповідь збережено! ') + (lf(tk, 'tip') || ''));
        }); }; }
  }
  function similarity(target, said) {
    var a = norm(target).split(' '), b = norm(said).split(' '), hit = 0, used = {};
    a.forEach(function (w) { for (var j = 0; j < b.length; j++) if (!used[j] && b[j] === w) { used[j] = 1; hit++; break; } });
    return a.length ? Math.round(hit / a.length * 100) : 0;
  }
  function bindMic(tk) {
    var btn = card.querySelector('#micBtn'), out = card.querySelector('#micOut'), acc = card.querySelector('#micAccept'), best = 0, tries = 0;
    var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    function result(said) {
      tries++; var p = similarity(tk.say, said); best = Math.max(best, p);
      out.innerHTML = '<div class="said">«' + esc(said) + '»</div><div class="meter"><i style="width:' + p + '%"></i></div><b>' + p + '%</b> ' + (p >= 80 ? t('Чудова вимова!') : p >= 50 ? t('Майже! Спробуй ще раз або зарахуй.') : t('Спробуй ще раз, говори чіткіше.'));
      if (p >= 80) { done(true, t('Правильно! ') + (lf(tk, 'tip') || '')); return; }
      acc.hidden = false; btn.textContent = '🎤 ' + t('Ще раз');
    }
    acc.onclick = function () { done(best >= 50, (best >= 50 ? t('Зараховано: ') : t('Майже. ')) + best + '%. ' + (lf(tk, 'tip') || '')); };
    if (SR) {
      btn.onclick = function () {
        var r = new SR(); r.lang = SPEECH[TARGET]; r.interimResults = true; r.maxAlternatives = 3; var fin = '';
        btn.disabled = true; btn.textContent = '🔴 ' + t('Слухаю…'); out.innerHTML = '<span class="hint">' + t('Говори…') + '</span>';
        r.onresult = function (e) { var txt = ''; for (var i = 0; i < e.results.length; i++) { txt += e.results[i][0].transcript; if (e.results[i].isFinal) fin = txt; } out.innerHTML = '<div class="said">«' + esc(txt) + '»</div>'; };
        r.onerror = function (e) { btn.disabled = false; btn.textContent = '🎤 ' + t('Натисни і говори'); out.innerHTML = '<span class="tfb err">' + (e.error === 'not-allowed' ? t('Дозволь доступ до мікрофона в браузері.') : t('Не вдалося розпізнати. Спробуй ще раз.')) + '</span>'; };
        r.onend = function () { btn.disabled = false; if (fin || out.textContent.length > 4) result(fin || out.textContent.replace(/[«»]/g, '')); else if (!out.querySelector('.err')) { btn.textContent = '🎤 ' + t('Натисни і говори'); out.innerHTML = '<span class="hint">' + t('Нічого не почуто. Спробуй ще раз.') + '</span>'; } };
        try { r.start(); } catch (e) { btn.disabled = false; }
      };
    } else if (navigator.mediaDevices && window.MediaRecorder) {
      btn.onclick = function () {
        navigator.mediaDevices.getUserMedia({audio:true}).then(function (st) {
          var rec = new MediaRecorder(st), chunks = []; rec.ondataavailable = function (e) { chunks.push(e.data); };
          rec.onstop = function () { st.getTracks().forEach(function (x) { x.stop(); }); var url = URL.createObjectURL(new Blob(chunks)); out.innerHTML = '<audio controls src="' + url + '"></audio><div class="hint">' + t('Порівняй зі зразком (кнопка «Прослухати») і оціни себе.') + '</div><div class="row"><button class="topt" type="button" data-s="1">✓ ' + t('Звучить добре') + '</button></div>'; out.querySelector('[data-s]').onclick = function () { done(true, t('Правильно! ') + (lf(tk, 'tip') || '')); }; btn.textContent = '🎤 ' + t('Ще раз'); btn.disabled = false; };
          rec.start(); btn.textContent = '⏹ ' + t('Зупинити'); btn.onclick = function () { rec.stop(); btn.onclick = null; setTimeout(function () { bindMic(tk); }, 0); };
        }).catch(function () { out.innerHTML = '<span class="tfb err">' + t('Дозволь доступ до мікрофона в браузері.') + '</span>'; });
      };
    } else { btn.disabled = true; out.innerHTML = '<span class="hint">' + t('Твій браузер не підтримує мікрофон. Повтори вголос і натисни «Пропустити».') + '</span>'; }
  }
  function bindSay(tk) { var sb = card.querySelector('#tsay'); if (sb) sb.onclick = function () { say(tk.say); };
    var rb = card.querySelector('#ruleBtn'); if (rb) { rb.disabled = false; rb.onclick = function () { var bx = card.querySelector('#ruleBox'); if (!bx.hidden) { bx.hidden = true; rb.classList.remove('on'); return; } bx.hidden = false; rb.classList.add('on'); hintMark('rule'); bx.innerHTML = '<span class="muted small">…</span>'; loadGuide(TARGET).then(function () { var info = gTaskTopics(tk, lesson, ctxLs || [], TARGET); if (!info) { bx.innerHTML = '<span class="muted small">' + tx({uk:'Для цього завдання окремого правила немає — орієнтуйся на сцену і слова.', pl:'Do tego zadania nie ma osobnej zasady — kieruj się sceną i słowami.', en:'There is no separate rule for this task: use the scene and the words.'}) + '</span>'; return; } gRulePanel(bx, info, TARGET); }).catch(function () { bx.textContent = tx({uk:'Не вдалося завантажити правило.', pl:'Nie udało się wczytać zasady.', en:'Could not load the rule.'}); }); }; }
    var qb = card.querySelector('#qtrBtn'); if (qb) qb.onclick = function () { var tt = card.querySelector('#qtrText'); tt.hidden = !tt.hidden; if (!tt.hidden) hintMark('tr'); qb.classList.toggle('on', !tt.hidden); };
    card.querySelectorAll('.spk').forEach(function (s) { s.addEventListener('click', function (e) { e.stopPropagation(); e.preventDefault(); hintMark('say'); say(s.dataset.say); }, true); }); }
  function hintMark(k) { if (snaps[cur]) return; var h = hints[cur] = hints[cur] || {}; h[k] = (h[k] || 0) + 1; }
  function done(ok, text) {
    durs[cur] = Math.max(1, Math.round((Date.now() - (tStart[cur] || Date.now())) / 1000));
    res[cur] = ok; var fb = card.querySelector('#tfb'); fb.className = 'tfb ' + (ok ? 'ok' : 'err'); fb.textContent = text;
    card.querySelectorAll('.topt,#tsubmit,#tcheck').forEach(function (x) { x.disabled = true; });
    card.querySelectorAll('button:not(#tnext):not(#tsay):not(#ruleBtn):not(.g-chip):not(.spk),input:not(.g-q),select:not(.g-sel),textarea').forEach(function (x) { x.disabled = true; });
    var n = card.querySelector('#tnext'); n.hidden = false; n.textContent = cur < tasks.length - 1 ? t('Далі') : t('Показати результат');
    snaps[cur] = card.innerHTML;
    renderSide(); n.onclick = next; n.focus();
  }
  function answerMC(b) {
    var tk = tasks[cur], ok;
    if (b.dataset.s != null) { ok = b.dataset.s === '1'; if (!ok) { done(false, skipMsg()); return; } }
    else { ok = +b.dataset.i === +tk.answer; card.querySelectorAll('.topt').forEach(function (x) { if (+x.dataset.i === +tk.answer) x.classList.add('right'); }); if (!ok) b.classList.add('wrong'); var g = card.querySelector('.gap'); if (g) g.textContent = tk.options[tk.answer]; }
    var why = lf(tk, 'why'), w = why && b.dataset.i != null ? why[+b.dataset.i] : '';
    done(ok, (ok ? t('Правильно! ') : t('Майже. ')) + (w ? w + ' ' : '') + (lf(tk, 'tip') || ''));
  }
  function next() { if (cur < tasks.length - 1) { cur++; render(); } else if (res.filter(function (x, i) { return !isInfo(tasks[i].type) && x == null; }).length && firstOpen() > -1) { cur = firstOpen(); render(); toast(t('Є завдання без відповіді'), 'info'); } else finish(); }
  function firstOpen() { for (var i = 0; i < tasks.length; i++) if (!isInfo(tasks[i].type) && res[i] == null) return i; return -1; }
  function finish() {
    var per = tasks.map(function (tk, i) { var o = {n:i, type:tk.type, sec:durs[i] || 0, ok:res[i] == null ? null : !!res[i]}; if (hints[i]) o.h = hints[i]; return o; }); LAST_TIMES = {total:per.reduce(function (a, x) { return a + x.sec; }, 0), per:per};
    var sc = res.filter(function (x) { return x === true; }).length, pct = scored ? Math.round(sc / scored * 100) : 0; cur = tasks.length; renderSide();
    card.innerHTML = '<div class="tres"><span class="ttag">' + t('РЕЗУЛЬТАТ') + '</span><div class="big">' + sc + ' / ' + scored + '</div><p class="lead" style="text-align:center" id="tresText">' + pct + '%</p><div id="tresExtra" style="width:100%"></div><div class="row" style="justify-content:center" id="tresBtns"></div></div>';
    onFinish(pct, finalText, card.querySelector('#tresText'), card.querySelector('#tresBtns'), function () { cur = 0; res = []; snaps = []; hints = {}; maxReached = FREE ? tasks.length - 1 : 0; tStart = {}; durs = {}; render(); }, card.querySelector('#tresExtra'));
  }
  loadGuide(TARGET).catch(function () {});
  if (!tasks.length) { card.innerHTML = t('<div class="empty">У цьому уроці ще немає завдань.</div>'); return; }
  render();
}

/* ================= grammar guide ================= */
var GUIDE_P = {};
function loadGuide(tg) {
  if (window.GUIDE && window.GUIDE[tg]) return Promise.resolve(window.GUIDE[tg]);
  if (!GUIDE_P[tg]) GUIDE_P[tg] = new Promise(function (res, rej) { var s = document.createElement('script'); s.src = 'guide-' + tg + '.js?v=37'; s.onload = function () { res(window.GUIDE[tg]); }; s.onerror = function () { delete GUIDE_P[tg]; rej(new Error('guide')); }; document.head.appendChild(s); });
  return GUIDE_P[tg];
}
function gTxt(o) { return o == null ? '' : typeof o === 'string' ? o : (o[LANG] || o.uk || ''); }
function gTopic(tg, id) { return ((window.GUIDE || {})[tg] || []).filter(function (x) { return x.id === id; })[0]; }
function gMatch(tg, text) { if (!text) return null; var o = (window.GUIDE || {})[tg + '_order'] || []; for (var i = 0; i < o.length; i++) { var tp = gTopic(tg, o[i]); if (tp && tp.k.test(text)) return tp; } return null; }
function gLessonTitle(l, tg) { if (!l) return ''; if (tg === 'en') return l.grammar || ''; var v = l.variants || {}; return v[tg + '_grammar'] || ''; }
function gRuleTask(tk, l) { if (isInfo(tk.type) || /^(final|speaking|vocabulary|match)$/.test(tk.type)) return false; if (/СЛОВНИК|VOCAB|SŁOWN/i.test(tk.label || '')) return false; if (gIsReview(l)) return false; return /^(grammar|type|order|drill|quest|tf)$/.test(tk.type); }
function gIsReview(l) { return /^(Повторення|Усе|Уся)/.test(l.grammar || '') || !!(l.variants && l.variants.cert); }
function gTable(tb) {
  if (!tb) return '';
  return '<div class="g-tw"><table class="g-tb"><thead><tr>' + tb.h.map(function (c) { return '<th>' + esc(gTxt(c)) + '</th>'; }).join('') + '</tr></thead><tbody>' + tb.r.map(function (r) { return '<tr>' + r.map(function (c, i) { return i === 0 ? '<th scope="row">' + esc(gTxt(c)) + '</th>' : '<td>' + esc(gTxt(c)) + '</td>'; }).join('') + '</tr>'; }).join('') + '</tbody></table></div>';
}
function gExamples(tp, tg, n) { var ex = (tp.ex || []).slice(0, n || 99); return ex.length ? '<ul class="g-ex">' + ex.map(function (e) { return '<li><span>' + esc(e) + '</span> <button type="button" class="spk" data-gsay="' + esc(e) + '" data-glang="' + tg + '" title="' + tx({uk:'Прослухати', pl:'Odsłuchaj', en:'Listen'}) + '">🔊</button></li>'; }).join('') + '</ul>' : ''; }
function gRuleCompact(tp, tg) {
  return '<div class="g-mini"><b class="g-mt">' + esc(gTxt(tp.t)) + '</b><p>' + esc(gTxt(tp.s)) + '</p>' + gTable(tp.tb) + gExamples(tp, tg, 2) +
    '<a class="g-more" href="#/guide/' + tg + '/' + tp.id + '" target="_blank" rel="noopener">📖 ' + tx({uk:'Детальніше в посібнику', pl:'Więcej w poradniku', en:'More in the guide'}) + ' ↗</a></div>';
}
function gBindSay(root) { root.querySelectorAll('[data-gsay]').forEach(function (b) { b.onclick = function (e) { e.preventDefault(); e.stopPropagation(); say(b.dataset.gsay, SPEECH[b.dataset.glang]); }; }); }
/* in-lesson helper: candidate topic ids for a task */
function gTaskTopics(tk, lesson, ls, tg) {
  var cands = [], seen = {};
  function add(tp) { if (tp && !seen[tp.id]) { seen[tp.id] = 1; cands.push(tp); } }
  var review = gIsReview(lesson), pick = null;
  if (!review) { add(gMatch(tg, gLessonTitle(lesson, tg))); return cands.length ? {list:cands, pick:cands[0]} : null; }
  var idx = ls.map(function (x) { return x.id; }).indexOf(lesson.id), from = 0;
  if (!(lesson.variants && lesson.variants.cert)) for (var i = idx - 1; i >= 0; i--) if (gIsReview(ls[i])) { from = i + 1; break; }
  var byNum = {}; ls.forEach(function (x) { byNum[x.num] = x; });
  var m = String(tk.tip || '').match(/(?:Урок|уроку|уроків|Lekcja|lekcji|Lesson)\s*(\d+)/);
  if (m && byNum[+m[1]]) pick = gMatch(tg, gLessonTitle(byNum[+m[1]], tg));
  for (var j = from; j < (idx < 0 ? ls.length : idx); j++) if (!gIsReview(ls[j])) add(gMatch(tg, gLessonTitle(ls[j], tg)));
  if (!pick) { var txt = [tk.q, tk.tip, (tk.options || []).join(' '), (tk.why || []).join(' ')].join(' '); for (var c = 0; c < cands.length && !pick; c++) if (cands[c].k.test(txt)) pick = cands[c]; }
  if (!pick && !/^(grammar|type|order|drill|quest)$/.test(tk.type)) return null;
  if (pick) add(pick);
  return cands.length ? {list:cands, pick:pick || cands[0]} : null;
}
function gRulePanel(box, info, tg) {
  var tp = info.pick;
  box.innerHTML = '<div class="g-mini"><b class="g-mt">' + esc(gTxt(tp.t)) + '</b><p>' + esc(gTxt(tp.s)) + '</p><a class="g-more" href="#/guide/' + tg + '/' + tp.id + '" target="_blank" rel="noopener">📖 ' + tx({uk:'Детальніше в посібнику', pl:'Więcej w poradniku', en:'More in the guide'}) + ' ↗</a></div>';
}
/* full guide page */
function viewGuide(tg, id) {
  tg = /^(en|pl|uk)$/.test(tg || '') ? tg : TARGET; var q = '';
  $app.innerHTML = '<div class="page"><p class="muted">' + tx({uk:'Відкриваю посібник…', pl:'Otwieram poradnik…', en:'Opening the guide…'}) + '</p></div>';
  return loadGuide(tg).then(function (list) {
    var groups = window.GUIDE[tg + '_groups'] || {}, cur = gTopic(tg, id) || list[0];
    var names = {en:tx({uk:'Англійська', pl:'Angielski', en:'English'}), pl:tx({uk:'Польська', pl:'Polski', en:'Polish'}), uk:tx({uk:'Українська', pl:'Ukraiński', en:'Ukrainian'})};
    $app.innerHTML = '<div class="page guide"><div class="sec-head"><div class="eyebrow">' + tx({uk:'Посібник', pl:'Poradnik', en:'Guide'}) + '</div><h2>' + tx({uk:'Граматика коротко і з прикладами', pl:'Gramatyka krótko i z przykładami', en:'Grammar, short and with examples'}) + '</h2><p class="lead">' + tx({uk:'Правила, таблиці й типові помилки. Пояснення — твоєю мовою, приклади — мовою, яку вивчаєш.', pl:'Zasady, tabele i typowe błędy. Wyjaśnienia w twoim języku, przykłady w języku, którego się uczysz.', en:'Rules, tables and common mistakes. Explanations in your language, examples in the language you are learning.'}) + '</p></div>' +
      '<div class="g-top"><div class="g-tabs" role="tablist">' + ['en', 'pl', 'uk'].map(function (l) { return '<a role="tab" class="g-tab' + (l === tg ? ' on' : '') + '" aria-selected="' + (l === tg) + '" href="#/guide/' + l + '">' + FLAG[l] + ' · ' + names[l] + '</a>'; }).join('') + '</div><input class="inp-s g-q" id="gQ" type="search" placeholder="' + tx({uk:'Пошук правила…', pl:'Szukaj zasady…', en:'Search rules…'}) + '"></div>' +
      '<div class="g-wrap"><aside class="g-toc" id="gToc"></aside><article class="g-art" id="gArt"></article></div></div>';
    var toc = document.getElementById('gToc'), art = document.getElementById('gArt');
    function drawToc() {
      var ql = q.toLowerCase(), hit = function (tp) { return !ql || (gTxt(tp.t) + ' ' + gTxt(tp.s) + ' ' + (tp.ex || []).join(' ')).toLowerCase().indexOf(ql) > -1; };
      var html = '';
      Object.keys(groups).forEach(function (g) { var items = list.filter(function (tp) { return tp.g === g && hit(tp); }); if (!items.length) return; html += '<div class="g-grp">' + esc(gTxt(groups[g])) + '</div>' + items.map(function (tp) { return '<a class="g-li' + (tp === cur ? ' on' : '') + '" href="#/guide/' + tg + '/' + tp.id + '">' + esc(gTxt(tp.t)) + '</a>'; }).join(''); });
      toc.innerHTML = html || '<p class="muted small">' + tx({uk:'Нічого не знайдено.', pl:'Nic nie znaleziono.', en:'Nothing found.'}) + '</p>';
    }
    function drawArt() {
      var tp = cur, i = list.indexOf(tp), prev = list[i - 1], nxt = list[i + 1], b = (tp.b && (tp.b[LANG] || tp.b.uk)) || [];
      art.innerHTML = '<div class="eyebrow">' + esc(gTxt(groups[tp.g])) + '</div><h3 class="g-h">' + esc(gTxt(tp.t)) + '</h3><p class="g-sum">' + esc(gTxt(tp.s)) + '</p>' +
        (b.length ? '<ul class="g-pts">' + b.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') + '</ul>' : '') + gTable(tp.tb) +
        ((tp.ex || []).length ? '<h4>' + tx({uk:'Приклади', pl:'Przykłady', en:'Examples'}) + '</h4>' + gExamples(tp, tg) : '') +
        ((tp.m || []).length ? '<h4>' + tx({uk:'Типові помилки', pl:'Typowe błędy', en:'Common mistakes'}) + '</h4><ul class="g-mis">' + tp.m.map(function (p) { return '<li><s>✗ ' + esc(p[0]) + '</s><b>✓ ' + esc(p[1]) + '</b></li>'; }).join('') + '</ul>' : '') +
        '<div class="g-nav">' + (prev ? '<a class="btn btn-ghost btn-sm" href="#/guide/' + tg + '/' + prev.id + '">← ' + esc(gTxt(prev.t)) + '</a>' : '<span></span>') + (nxt ? '<a class="btn btn-ghost btn-sm" href="#/guide/' + tg + '/' + nxt.id + '">' + esc(gTxt(nxt.t)) + ' →</a>' : '') + '</div>';
      gBindSay(art);
    }
    drawToc(); drawArt();
    var qi = document.getElementById('gQ'); qi.oninput = function () { q = qi.value.trim(); drawToc(); };
    if (id) { var a = document.getElementById('gArt'); if (a && window.innerWidth < 860) setTimeout(function () { a.scrollIntoView({block:'start'}); }, 50); }
  });
}

function viewLesson(id) {
  return loadDefs().then(function () { return API.getLesson(id); }).then(function (l) {
    if (!l) { $app.innerHTML = t('<div class="page"><div class="empty">Урок не знайдено.</div></div>'); return; }
    return Promise.all([API.getCourse(l.course_id), API.listLessons(l.course_id), API.myEnrollments()]).then(function (r) {
      var c = r[0], ls = r[1], enrolled = r[2].indexOf(l.course_id) > -1 || isAdm() || isFreeCourse(c);
      setAmbient(ambTheme(c));
      var isFirst = ls.length && ls[0].id === l.id && !(c && c.free_first === false), idx = ls.map(function (x) { return x.id; }).indexOf(l.id), nextL = ls[idx + 1];
      if (!lessonTasks(l)) { $app.innerHTML = '<div class="page"><div class="empty">' + t('Цей урок ще недоступний обраною мовою. Скоро!') + ' <a href="#/course/' + esc(l.course_id) + '">' + t('До марафону') + '</a></div></div>'; return; }
      if (!enrolled && !isFirst) { $app.innerHTML = t('<div class="page"><div class="empty">Цей урок відкривається після активації ключа. <a href="#/course/') + esc(l.course_id) + t('">До марафону</a></div></div>'); return; }
      $app.innerHTML = '<div class="page"><div class="sec-head"><a href="#/course/' + esc(l.course_id) + '" class="muted small">← ' + esc(c ? tr(c, 'title') : t('Марафон')) + t('</a><div class="eyebrow">Урок ') + l.num + ' · ' + esc(lGram(l)) + '</div><h2>' + esc(tr(l, 'title')) + '</h2><p class="lead">' + esc(tr(l, 'scene')) + '</p></div><div id="player"></div></div>';
      runPlayer(document.getElementById('player'), l, function (pct, finalText, textEl, btns, again, extra) {
        if (!enrolled && extra) { var rest = ls.slice(idx + 1); extra.innerHTML = '<div class="upsell"><h3>' + (pct >= 70 ? t('Відмінно! Ти готовий до повного марафону.') : t('Гарний старт! Повний марафон допоможе закріпити.')) + '</h3><p class="muted">' + t('Ще') + ' ' + rest.length + ' ' + t('уроків чекають на тебе:') + '</p><ol class="uplist">' + rest.slice(0, 6).map(function (x) { return '<li><b>' + esc(tr(x, 'title')) + '</b> <span class="muted small">· ' + esc(x.grammar) + '</span></li>'; }).join('') + (rest.length > 6 ? '<li class="muted">+ ' + (rest.length - 6) + ' ' + t('уроків, фінальний проєкт і сертифікат') + '</li>' : '') + '</ol><div class="price-tag"><b>' + esc(c ? c.price : '') + '</b> <span class="muted">' + t('один раз · доступ на 12 місяців') + '</span></div></div>'; }
        var vb = l.variants || {};
        if (extra && vb.badge && pct >= 50) extra.insertAdjacentHTML('afterbegin', '<div class="badge-win"><span class="bw-i">' + esc(vb.badge.icon || '🏅') + '</span><div><div class="eyebrow">' + tx({uk:'Нагорода уроку', pl:'Nagroda lekcji', en:'Lesson reward'}) + '</div><b>' + esc(lf(vb.badge, 'name')) + '</b><p class="muted small">' + esc(lf(vb.badge, 'text') || '') + '</p></div></div>');
        if (extra && vb.cert && pct >= 70) extra.insertAdjacentHTML('beforeend', '<div class="cert" id="certBox"><div class="eyebrow">' + tx({uk:'Сертифікат', pl:'Certyfikat', en:'Certificate'}) + '</div><h3>' + esc(vb['cert_' + LANG] || vb.cert) + '</h3><p>' + esc(USER && (USER.name || USER.email) || '') + '</p><p class="muted small">' + esc(c ? tr(c, 'title') : '') + ' · ' + new Date().toLocaleDateString() + ' · ' + pct + '%</p><button class="btn btn-ghost btn-sm" type="button" onclick="window.print()">' + tx({uk:'Друкувати', pl:'Drukuj', en:'Print'}) + '</button></div>');
        if (USER && LAST_TIMES) API.saveTimes(l.id, pct, LAST_TIMES).catch(function () {});
        if (USER) { API.saveProgress(l.id, pct, finalText).then(function (r) { textEl.textContent = r && r.retry ? t('Повторна спроба: ') + pct + t('%. Перший результат зберігається, новий показано в дужках.') : t('Бал: ') + pct + t('%. Результат збережено в кабінеті.'); }); }
        else textEl.textContent = t('Бал: ') + pct + t('%. Створи кабінет, щоб зберігати прогрес.');
        btns.innerHTML = (nextL && enrolled ? '<a class="btn btn-red" href="#/lesson/' + esc(nextL.id) + t('">Наступний урок</a>') : (!enrolled ? t('<a class="btn btn-red" href="#/buy">Отримати ключ доступу</a>') : '')) + '<a class="btn btn-ghost" href="' + (USER ? '#/cabinet' : '#/register') + '">' + (USER ? t('Мій кабінет') : t('Створити кабінет')) + t('</a><button class="btn btn-ghost" type="button" id="again">Пройти ще раз</button>');
        btns.querySelector('#again').onclick = again;
      }, ls);
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
function fmtSec(s) { s = +s || 0; var m = Math.floor(s / 60), r = s % 60; return (m ? m + ' хв ' : '') + r + ' с'; }
var AN = {c:null, t:'en'};
function adminAnalytics(body) {
  return API.adminAnalytics().then(function (d) {
    var L = function (uk, pl, en) { return tx({uk:uk, pl:pl, en:en}); };
    var cs = d.courses.filter(function (c) { return d.lessons.some(function (l) { return l.course_id === c.id; }); });
    if (!cs.length) { body.innerHTML = '<div class="empty">' + L('Ще немає курсів з уроками.', 'Brak kursów z lekcjami.', 'No courses with lessons yet.') + '</div>'; return; }
    if (!AN.c || !cs.some(function (c) { return c.id === AN.c; })) AN.c = cs[0].id;
    var tg = AN.t, ls = d.lessons.filter(function (l) { return l.course_id === AN.c; }).sort(function (a, b) { return a.num - b.num; });
    var tasksOf = function (l) { return tg === 'en' ? (l.tasks || []) : ((l.variants && l.variants[tg]) || []); };
    ls = ls.filter(function (l) { return tasksOf(l).length; });
    var ids = ls.map(function (l) { return l.id; });
    var prog = (tg === 'en' ? d.progress : d.progress_lang.filter(function (x) { return x.target === tg; })).filter(function (x) { return ids.indexOf(x.lesson_id) > -1; });
    var times = d.times.filter(function (x) { return (x.target || 'en') === tg && ids.indexOf(x.lesson_id) > -1; });
    var users = {}; prog.forEach(function (x) { users[x.user_id] = 1; }); d.elangs.forEach(function (e) { if (e.course_id === AN.c && e.target === tg) users[e.user_id] = 1; });
    var started = Object.keys(users).length;
    var per = ls.map(function (l) { var pr = prog.filter(function (x) { return x.lesson_id === l.id; }), tm = times.filter(function (x) { return x.lesson_id === l.id; });
      return {l:l, n:pr.length, avg:pr.length ? Math.round(pr.reduce(function (a, x) { return a + (+x.score || 0); }, 0) / pr.length) : null, sec:tm.length ? Math.round(tm.reduce(function (a, x) { return a + (+x.total_sec || 0); }, 0) / tm.length) : null, tries:tm.length}; });
    var finished = ls.length ? per[per.length - 1].n : 0, maxN = Math.max(started, 1);
    var worst = -1, worstDrop = 0; per.forEach(function (x, i) { var prev = i ? per[i - 1].n : started, drop = prev - x.n; if (drop > worstDrop) { worstDrop = drop; worst = i; } });
    var agg = {}; times.forEach(function (x) { (x.per_task || []).forEach(function (p) { if (p.type === 'intro' || p.ok == null) return; var k = x.lesson_id + '|' + p.n, a = agg[k] || (agg[k] = {lid:x.lesson_id, n:p.n, type:p.type, cnt:0, bad:0, sec:0}); a.cnt++; if (!p.ok) a.bad++; a.sec += +p.sec || 0; }); });
    var hardAll = Object.keys(agg).map(function (k) { var a = agg[k]; a.err = Math.round(a.bad / a.cnt * 100); a.avg = Math.round(a.sec / a.cnt); return a; }), hard3 = hardAll.filter(function (a) { return a.cnt >= 3; }), hard = (hard3.length ? hard3 : hardAll).sort(function (a, b) { return b.err - a.err || b.avg - a.avg; }).slice(0, 12);
    var lById = {}; ls.forEach(function (l) { lById[l.id] = l; });
    var allSec = times.length ? Math.round(times.reduce(function (a, x) { return a + (+x.total_sec || 0); }, 0) / times.length) : 0;
    var avgAll = prog.length ? Math.round(prog.reduce(function (a, x) { return a + (+x.score || 0); }, 0) / prog.length) : 0;
    body.innerHTML = '<p class="hint" style="margin-bottom:12px">🔒 ' + L('Бачить лише адміністратор.', 'Widzi tylko administrator.', 'Visible to the admin only.') + '</p>' +
      '<div class="row" style="gap:8px;flex-wrap:wrap;margin-bottom:16px"><select class="inp-s" id="anC" style="max-width:340px">' + cs.map(function (c) { return '<option value="' + esc(c.id) + '"' + (c.id === AN.c ? ' selected' : '') + '>' + esc(tr(c, 'title')) + '</option>'; }).join('') + '</select>' +
      LANGS.map(function (x) { return '<button type="button" class="vtab' + (x === tg ? ' on' : '') + '" data-ant="' + x + '">' + FLAG[x] + '</button>'; }).join('') + '</div>' +
      '<div class="stats" style="margin-bottom:18px"><div class="stat"><b>' + started + '</b><span>' + L('почали', 'zaczęło', 'started') + '</span></div><div class="stat"><b>' + finished + '</b><span>' + L('завершили', 'ukończyło', 'finished') + (started ? ' (' + Math.round(finished / started * 100) + '%)' : '') + '</span></div><div class="stat"><b>' + avgAll + '%</b><span>' + L('середній бал', 'średni wynik', 'average score') + '</span></div><div class="stat"><b>' + fmtSec(allSec) + '</b><span>' + L('сер. час уроку', 'śr. czas lekcji', 'avg lesson time') + '</span></div></div>' +
      '<div class="panel" style="margin-bottom:18px"><h3 style="margin-bottom:6px">' + L('Де учні кидають курс', 'Gdzie uczniowie porzucają kurs', 'Where students drop off') + '</h3>' +
      (worst > -1 && worstDrop > 0 ? '<p class="muted small" style="margin-bottom:12px">⚠ ' + L('Найбільший відтік перед уроком ', 'Największy odpływ przed lekcją ', 'Biggest drop before lesson ') + per[worst].l.num + ': −' + worstDrop + '</p>' : '<p class="muted small" style="margin-bottom:12px">' + L('Даних ще мало — графік наповниться, коли учні проходитимуть уроки.', 'Mało danych — wykres zapełni się, gdy uczniowie będą przechodzić lekcje.', 'Not much data yet — the chart fills in as students take lessons.') + '</p>') +
      '<div class="funnel"><div class="frow"><span class="fl0">' + L('Старт', 'Start', 'Start') + '</span><span class="fbar"><i style="width:' + (started / maxN * 100) + '%"></i></span><b>' + started + '</b><span></span><span></span></div>' +
      per.map(function (x, i) { return '<div class="frow' + (i === worst && worstDrop > 0 ? ' fworst' : '') + '"><span class="fl0">' + x.l.num + '. ' + esc(tr(x.l, 'title')) + '</span><span class="fbar"><i style="width:' + (x.n / maxN * 100) + '%"></i></span><b>' + x.n + '</b><span class="muted small">' + (x.avg != null ? x.avg + '%' : '—') + '</span><span class="muted small">' + (x.sec != null ? fmtSec(x.sec) : '—') + '</span></div>'; }).join('') +
      '<div class="frow fhead muted small"><span></span><span></span><span>' + L('пройшли', 'ukończyło', 'done') + '</span><span>' + L('бал', 'wynik', 'score') + '</span><span>' + L('час', 'czas', 'time') + '</span></div></div></div>' +
      '<div class="panel"><h3 style="margin-bottom:6px">' + L('Найважчі завдання', 'Najtrudniejsze zadania', 'Hardest tasks') + '</h3><p class="muted small" style="margin-bottom:12px">' + L('За відсотком помилок у перших і повторних спробах.', 'Według odsetka błędów we wszystkich podejściach.', 'By error rate across all attempts.') + '</p>' +
      (hard.length ? '<div class="tbl-wrap"><table class="tbl"><thead><tr><th>' + L('Урок', 'Lekcja', 'Lesson') + '</th><th>' + L('Завдання', 'Zadanie', 'Task') + '</th><th>' + L('Помилки', 'Błędy', 'Errors') + '</th><th>' + L('Сер. час', 'Śr. czas', 'Avg time') + '</th><th>' + L('Спроб', 'Podejść', 'Attempts') + '</th></tr></thead><tbody>' +
        hard.map(function (a) { var l = lById[a.lid] || {}, tk = tasksOf(l)[a.n] || {}; return '<tr><td>' + (l.num || '') + '</td><td><b>' + esc(ttName(a.type)) + '</b><br><span class="muted small">' + esc(String(tk.q || '').replace(/<[^>]+>/g, '').slice(0, 90)) + '</span></td><td><span class="pill ' + (a.err >= 50 ? 'warn' : 'ok') + '">' + a.err + '%</span></td><td>' + fmtSec(a.avg) + '</td><td>' + a.cnt + '</td></tr>'; }).join('') + '</tbody></table></div>'
        : '<div class="empty small">' + L('Ще немає проходжень з записаним часом.', 'Brak podejść z zapisanym czasem.', 'No attempts with recorded time yet.') + '</div>') + '</div>';
    document.getElementById('anC').onchange = function (e) { AN.c = e.target.value; adminAnalytics(body); };
    body.querySelectorAll('[data-ant]').forEach(function (b) { b.onclick = function () { AN.t = b.dataset.ant; adminAnalytics(body); }; });
  });
}
function adminTimes(body) {
  return API.adminTimes().then(function (d) {
    var U = {}, L = {}; d.users.forEach(function (u) { U[u.id] = u; }); d.lessons.forEach(function (l) { L[l.id] = l; });
    if (!d.times.length) { body.innerHTML = '<div class="empty">' + tx({uk:'Ще немає даних. Час записується після кожного проходження уроку.', pl:'Brak danych. Czas zapisuje się po każdym przejściu lekcji.', en:'No data yet. Time is saved after each lesson attempt.'}) + '</div>'; return; }
    body.innerHTML = '<p class="hint" style="margin-bottom:12px">🔒 ' + tx({uk:'Бачить лише адміністратор.', pl:'Widzi tylko administrator.', en:'Visible to the admin only.'}) + '</p><div class="ttimes">' + d.times.map(function (x, i) { var u = U[x.user_id] || {}, l = L[x.lesson_id] || {};
      return '<details class="tt"><summary><span><b class="au-link" role="button" data-uid="' + esc(x.user_id) + '">' + esc(u.name || u.email || '?') + ' 📊</b> <span class="muted small">' + esc(u.email || '') + '</span></span><span>' + (l.num ? l.num + '. ' : '') + esc(tr(l, 'title') || '') + '</span><span class="badge">' + FLAG[x.target || 'en'] + '</span><span>' + (x.score != null ? x.score + '%' : '') + '</span><b>' + fmtSec(x.total_sec) + '</b><span class="muted small">' + fmtDate(x.created_at) + '</span></summary><div class="ttper">' + (x.per_task || []).filter(function (p) { return p.type !== 'intro'; }).map(function (p, k) { return '<div><span>' + (k + 1) + '. ' + esc(ttName(p.type)) + '</span><span>' + (p.ok === true ? '✓' : p.ok === false ? '✗' : '–') + '</span><b>' + fmtSec(p.sec) + '</b></div>'; }).join('') + '</div></details>'; }).join('') + '</div>';
    body.querySelectorAll('[data-uid]').forEach(function (b) { b.onclick = function (e) { e.preventDefault(); ADM_UID = b.dataset.uid; adminUser(body, ADM_UID); window.scrollTo(0, 0); }; });
  });
}
function viewAdmin() {
  if (!requireUser()) return Promise.resolve();
  if (USER.role === 'admin' && !ADMIN_MODE) { ADMIN_MODE = true; try { localStorage.setItem('ml_admin_mode', '1'); } catch (e) {} renderNav(); }
  if (USER.role !== 'admin') { $app.innerHTML = t('<div class="page"><div class="empty">Ця сторінка доступна лише адміністратору.</div></div>'); return Promise.resolve(); }
  $app.innerHTML = t('<div class="page"><div class="sec-head"><div class="eyebrow">Адмін-панель</div><h2>Керування MoviLang</h2></div><div class="tabs" role="tablist">') +
    [['stats',t('Статистика')],['users',t('Користувачі')],['courses',t('Курси й уроки')],['keys',t('Ключі доступу')],['site',t('Тексти сайту')],['look',t('Вигляд і кольори')],['analytics','📊 ' + tx({uk:'Аналітика', pl:'Analityka', en:'Analytics'})],['times','⏱ ' + tx({uk:'Час', pl:'Czas', en:'Time'})],['sales','💳 ' + tx({uk:'Продажі', pl:'Sprzedaż', en:'Sales'})]].map(function (t) { return '<button class="tab' + (adminTab === t[0] ? ' on' : '') + '" type="button" role="tab" data-t="' + t[0] + '">' + t[1] + '</button>'; }).join('') +
    t('</div><div id="adminBody"><p class="muted">Завантаження…</p></div></div>');
  $app.querySelectorAll('.tab').forEach(function (b) { b.onclick = function () { adminTab = b.dataset.t; ADM_UID = null; viewAdmin(); }; });
  var body = document.getElementById('adminBody');
  var f = {stats:adminStats, users:adminUsers, courses:adminCourses, keys:adminKeys, site:adminSite, look:adminLook, times:adminTimes, analytics:adminAnalytics, sales:adminSales}[adminTab];
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

var ADM_UID = null;
function adminUser(body, uid) {
  var L3 = function (uk, pl, en) { return tx({uk:uk, pl:pl, en:en}); };
  body.innerHTML = '<p class="muted">' + L3('Завантаження…', 'Ładowanie…', 'Loading…') + '</p>';
  return API.adminUser(uid).then(function (d) {
    var u = d.user || {}, LS = {}, CS = {}; d.lessons.forEach(function (l) { LS[l.id] = l; }); d.courses.forEach(function (c) { CS[c.id] = c; });
    var prog = d.progress.map(function (p) { return Object.assign({target:'en'}, p); }).concat(d.progress_lang), times = d.times.slice().sort(function (a, b) { return a.created_at < b.created_at ? 1 : -1; });
    var totalSec = times.reduce(function (a, x) { return a + (+x.total_sec || 0); }, 0);
    var avgScore = prog.length ? Math.round(prog.reduce(function (a, p) { return a + (+p.score || 0); }, 0) / prog.length) : null;
    var tasks = [], byType = {}, hintTasks = 0, answered = 0, okN = 0;
    times.forEach(function (x) { (x.per_task || []).forEach(function (p) { if (isInfo(p.type) || p.type === 'intro') return; tasks.push(p); var b = byType[p.type] = byType[p.type] || {n:0, ok:0, ans:0, sec:0, h:0};
      b.n++; b.sec += +p.sec || 0; if (p.ok != null) { b.ans++; answered++; if (p.ok) { b.ok++; okN++; } } var hh = p.h && (p.h.rule || p.h.tr || p.h.say); if (hh) { b.h++; hintTasks++; } }); });
    var types = Object.keys(byType).map(function (k) { var b = byType[k]; return {k:k, n:b.n, acc:b.ans ? Math.round(b.ok / b.ans * 100) : null, avg:Math.round(b.sec / b.n), hp:Math.round(b.h / b.n * 100)}; }).sort(function (a, b) { return b.avg - a.avg; });
    var withAcc = types.filter(function (x) { return x.acc != null && x.n >= 2; });
    var best = withAcc.slice().sort(function (a, b) { return b.acc - a.acc; })[0], worst = withAcc.slice().sort(function (a, b) { return a.acc - b.acc; })[0], slow = types[0], hintMost = types.slice().sort(function (a, b) { return b.hp - a.hp; })[0];
    var days = [], now = Date.now(); for (var i = 29; i >= 0; i--) { var dd = new Date(now - i * 86400000).toISOString().slice(0, 10); days.push({d:dd, s:times.filter(function (x) { return (x.created_at || '').slice(0, 10) === dd; }).reduce(function (a, x) { return a + (+x.total_sec || 0); }, 0)}); }
    var maxD = Math.max.apply(null, days.map(function (x) { return x.s; }).concat([60]));
    var hours = [0, 0, 0, 0]; times.forEach(function (x) { var h = new Date(x.created_at).getHours(); hours[h < 6 ? 3 : h < 12 ? 0 : h < 18 ? 1 : 2]++; });
    var hourNames = [L3('ранок', 'rano', 'morning'), L3('день', 'dzień', 'afternoon'), L3('вечір', 'wieczór', 'evening'), L3('ніч', 'noc', 'night')], favH = times.length ? hourNames[hours.indexOf(Math.max.apply(null, hours))] : '—';
    var last = [times[0] && times[0].created_at].concat(prog.map(function (p) { return p.retry_at || p.completed_at; })).filter(Boolean).sort().pop();
    var langs = {}; prog.forEach(function (p) { langs[p.target] = 1; }); times.forEach(function (x) { langs[x.target || 'en'] = 1; });
    var courseRows = {}; prog.forEach(function (p) { var l = LS[p.lesson_id]; if (!l) return; var key = l.course_id + '|' + p.target, r = courseRows[key] = courseRows[key] || {c:CS[l.course_id], tg:p.target, n:0, sum:0, total:d.lessons.filter(function (x) { return x.course_id === l.course_id; }).length}; r.n++; r.sum += +p.score || 0; });
    function hIc(h) { return h ? (h.rule ? ' 📘' + (h.rule > 1 ? '×' + h.rule : '') : '') + (h.tr ? ' 🌐' : '') + (h.say ? ' 🔊' + (h.say > 1 ? '×' + h.say : '') : '') : ''; }
    function lname(id) { var l = LS[id]; if (!l) return '?'; var c = CS[l.course_id]; return (c ? tr(c, 'title') + ' · ' : '') + l.num + '. ' + tr(l, 'title'); }
    var ins = [];
    if (slow) ins.push(L3('Найдовше думає над', 'Najdłużej myśli nad', 'Spends longest on') + ' <b>' + esc(ttName(slow.k)) + '</b> (' + fmtSec(slow.avg) + ')');
    if (best) ins.push(L3('Найкраще виходить', 'Najlepiej idzie', 'Strongest at') + ' <b>' + esc(ttName(best.k)) + '</b> (' + best.acc + '%)');
    if (worst && worst !== best) ins.push(L3('Найважче дається', 'Najtrudniej idzie', 'Weakest at') + ' <b>' + esc(ttName(worst.k)) + '</b> (' + worst.acc + '%)');
    if (hintMost && hintMost.hp) ins.push(L3('Найчастіше бере підказки в', 'Najczęściej sięga po podpowiedzi w', 'Uses hints most in') + ' <b>' + esc(ttName(hintMost.k)) + '</b> (' + hintMost.hp + '%)');
    ins.push(L3('Найчастіше вчиться', 'Najczęściej uczy się', 'Usually studies in the') + ': <b>' + favH + '</b>');
    body.innerHTML = '<div class="au">' +
      '<button class="btn btn-ghost btn-sm" type="button" id="auBack">← ' + L3('Усі користувачі', 'Wszyscy użytkownicy', 'All users') + '</button>' +
      '<div class="au-head"><span class="ava au-ava">' + esc((u.name || u.email || '?')[0].toUpperCase()) + '</span><div><h3>' + esc(u.name || '—') + '</h3><div class="muted small">' + esc(u.email || '') + ' · ' + esc(u.role || '') + ' · ' + L3('з', 'od', 'since') + ' ' + fmtDate(u.created_at) + ' · ' + L3('остання активність', 'ostatnia aktywność', 'last active') + ': ' + fmtDate(last) + ' · ' + Object.keys(langs).map(function (l) { return FLAG[l]; }).join(' ') + '</div></div></div>' +
      '<div class="stats"><div class="stat"><b>' + prog.length + '</b><span>' + L3('уроків пройдено', 'lekcji ukończonych', 'lessons done') + '</span></div><div class="stat"><b>' + (avgScore == null ? '—' : avgScore + '%') + '</b><span>' + L3('середній бал', 'średni wynik', 'average score') + '</span></div><div class="stat"><b>' + fmtSec(totalSec) + '</b><span>' + L3('усього часу', 'łączny czas', 'total time') + '</span></div><div class="stat"><b>' + times.length + '</b><span>' + L3('спроб уроків', 'podejść do lekcji', 'lesson attempts') + '</span></div></div>' +
      '<div class="stats"><div class="stat"><b>' + (times.length ? fmtSec(Math.round(totalSec / times.length)) : '—') + '</b><span>' + L3('в середньому на урок', 'średnio na lekcję', 'average per lesson') + '</span></div><div class="stat"><b>' + (answered ? Math.round(okN / answered * 100) + '%' : '—') + '</b><span>' + L3('правильних відповідей', 'poprawnych odpowiedzi', 'correct answers') + '</span></div><div class="stat"><b>' + (tasks.length ? Math.round(hintTasks / tasks.length * 100) + '%' : '—') + '</b><span>' + L3('завдань з підказкою', 'zadań z podpowiedzią', 'tasks with a hint') + '</span></div><div class="stat"><b>' + tasks.length + '</b><span>' + L3('завдань розв\'язано', 'zadań rozwiązanych', 'tasks done') + '</span></div></div>' +
      (times.length ? '<div class="box au-ins"><h4>💡 ' + L3('Коротко', 'W skrócie', 'In short') + '</h4><ul>' + ins.map(function (x) { return '<li>' + x + '</li>'; }).join('') + '</ul></div>' : '') +
      '<div class="box"><h4>' + L3('Час навчання за 30 днів', 'Czas nauki w ostatnich 30 dniach', 'Study time, last 30 days') + '</h4><div class="week au-days">' + days.map(function (x, i) { return '<div title="' + x.d + ': ' + fmtSec(x.s) + '"><i style="height:' + Math.max(2, Math.round(x.s / maxD * 90)) + 'px"' + (i === 29 ? ' class="today"' : '') + '></i>' + (i % 5 === 4 ? x.d.slice(8) : '') + '</div>'; }).join('') + '</div></div>' +
      (types.length ? '<div class="box"><h4>' + L3('Типи завдань', 'Typy zadań', 'Task types') + '</h4><div class="tbl-wrap"><table class="tbl"><thead><tr><th>' + L3('Тип', 'Typ', 'Type') + '</th><th>' + L3('Скільки', 'Ile', 'Count') + '</th><th>' + L3('Правильно', 'Poprawnie', 'Correct') + '</th><th>' + L3('Сер. час', 'Śr. czas', 'Avg time') + '</th><th>' + L3('З підказкою', 'Z podpowiedzią', 'With hint') + '</th></tr></thead><tbody>' + types.map(function (x) { return '<tr><td>' + esc(ttName(x.k)) + '</td><td class="num">' + x.n + '</td><td class="num">' + (x.acc == null ? '—' : '<span class="au-acc" style="--p:' + x.acc + '%">' + x.acc + '%</span>') + '</td><td class="num">' + fmtSec(x.avg) + '</td><td class="num">' + x.hp + '%</td></tr>'; }).join('') + '</tbody></table></div></div>' : '') +
      (Object.keys(courseRows).length ? '<div class="box"><h4>' + L3('Курси', 'Kursy', 'Courses') + '</h4><div class="bars">' + Object.keys(courseRows).map(function (k) { var r = courseRows[k]; return '<div class="b"><span>' + esc(r.c ? tr(r.c, 'title') : '?') + ' ' + FLAG[r.tg] + '</span><div class="t"><i style="width:' + Math.round(r.n / Math.max(1, r.total) * 100) + '%"></i></div><b>' + r.n + '/' + r.total + ' · ' + Math.round(r.sum / r.n) + '%</b></div>'; }).join('') + '</div></div>' : '') +
      '<div class="box"><h4>' + L3('Історія спроб', 'Historia podejść', 'Attempt history') + '</h4>' + (times.length ? '<p class="hint">📘 ' + L3('правило', 'zasada', 'rule') + ' · 🌐 ' + L3('переклад питання', 'tłumaczenie pytania', 'question translation') + ' · 🔊 ' + L3('прослуховування', 'odsłuch', 'listening') + '</p><div class="ttimes">' + times.map(function (x) { var per = (x.per_task || []).filter(function (p) { return !isInfo(p.type) && p.type !== 'intro'; }), hn = per.filter(function (p) { return p.h; }).length, dt = new Date(x.created_at);
        return '<details class="tt"><summary><span class="muted small">' + fmtDate(x.created_at) + ' ' + String(dt.getHours()).padStart(2, '0') + ':' + String(dt.getMinutes()).padStart(2, '0') + '</span><span>' + esc(lname(x.lesson_id)) + '</span><span class="badge">' + FLAG[x.target || 'en'] + '</span><span>' + (x.score != null ? x.score + '%' : '') + '</span><b>' + fmtSec(x.total_sec) + '</b><span class="muted small">' + (hn ? hn + ' ' + L3('з підказкою', 'z podpowiedzią', 'with hint') : '') + '</span></summary><div class="ttper">' + per.map(function (p, k) { return '<div><span>' + (k + 1) + '. ' + esc(ttName(p.type)) + hIc(p.h) + '</span><span>' + (p.ok === true ? '✓' : p.ok === false ? '✗' : '–') + '</span><b>' + fmtSec(p.sec) + '</b></div>'; }).join('') + '</div></details>'; }).join('') + '</div>' : '<p class="muted">' + L3('Ще немає записаних спроб.', 'Brak zapisanych podejść.', 'No attempts recorded yet.') + '</p>') + '</div>' +
      (prog.filter(function (p) { return p.answer; }).length ? '<div class="box"><h4>✍ ' + L3('Письмові відповіді', 'Odpowiedzi pisemne', 'Written answers') + '</h4><div class="ttimes">' + prog.filter(function (p) { return p.answer; }).map(function (p) { return '<details class="tt"><summary><span>' + esc(lname(p.lesson_id)) + '</span><span class="badge">' + FLAG[p.target] + '</span><span class="muted small">' + fmtDate(p.completed_at) + '</span></summary><p class="au-ans">' + esc(p.answer) + '</p></details>'; }).join('') + '</div></div>' : '') +
      '</div>';
    document.getElementById('auBack').onclick = function () { ADM_UID = null; adminTab = 'users'; viewAdmin(); };
  });
}

function adminUsers(body) {
  if (ADM_UID) return adminUser(body, ADM_UID);
  return API.adminData().then(function (d) {
    var rows = d.users.map(function (u) {
      var pr = d.progress.filter(function (p) { return p.user_id === u.id; }), enr = d.enrollments.filter(function (e) { return e.user_id === u.id; }).length;
      var avg = pr.length ? Math.round(pr.reduce(function (a, p) { return a + (+p.score || 0); }, 0) / pr.length) : 0;
      var last = pr.map(function (p) { return p.completed_at; }).sort().pop();
      return '<tr><td><button type="button" class="au-link" data-uid="' + esc(u.id) + '"><b>' + esc(u.name || '—') + '</b> <span class="au-more">📊</span><br><span class="muted small">' + esc(u.email) + '</span></button></td><td><span class="pill' + (u.role === 'admin' ? ' admin' : '') + '">' + esc(u.role) + '</span></td><td>' + fmtDate(u.created_at) + '</td><td class="num">' + enr + '</td><td class="num">' + pr.length + '</td><td class="num">' + (pr.length ? avg + '%' : '—') + '</td><td>' + fmtDate(last) + '</td><td>' +
        (u.id === USER.id ? t('<span class="muted small">це ви</span>') : '<button class="btn btn-ghost btn-sm" type="button" data-role="' + esc(u.id) + '" data-to="' + (u.role === 'admin' ? 'student' : 'admin') + '">' + (u.role === 'admin' ? t('Зробити учнем') : t('Зробити адміном')) + '</button>') + '</td></tr>';
    }).join('');
    body.innerHTML = t('<p class="muted" style="margin-bottom:14px">Усього: ') + d.users.length + t('</p><div class="tbl-wrap"><table class="tbl"><thead><tr><th>Користувач</th><th>Роль</th><th>Реєстрація</th><th>Курсів</th><th>Уроків</th><th>Сер. бал</th><th>Активність</th><th></th></tr></thead><tbody>') + rows + '</tbody></table></div>';
    body.querySelectorAll('[data-uid]').forEach(function (b) { b.onclick = function () { ADM_UID = b.dataset.uid; adminUser(body, ADM_UID); window.scrollTo(0, 0); }; });
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
      (id && c.slug === 'harry-potter-1' ? '<div class="panel" style="display:grid;gap:10px;border-color:var(--highlight)"><h3>' + t('Повний курс: 16 уроків B1–B2') + '</h3><p class="muted small">' + t('Замінить поточні уроки цього курсу на нову програму (130 інтерактивних завдань з ілюстраціями).') + '</p><div class="row"><button class="btn btn-red btn-sm" type="button" id="importHP">' + t('Завантажити 16 уроків') + '</button><span class="small muted" id="importMsg"></span></div></div>' : '') +
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
    var ih = document.getElementById('importHP');
    if (ih) ih.onclick = function () {
      if (!ih.dataset.c) { ih.dataset.c = 1; ih.textContent = t('Точно? Натисни ще раз'); return; }
      ih.disabled = true; var msg = document.getElementById('importMsg'); msg.textContent = t('Завантаження…');
      fetch('content/hp1.json?v=' + Date.now()).then(function (r) { return r.json(); }).then(function (data) {
        var byNum = {}; ls.forEach(function (l) { byNum[l.num] = l; });
        var keep = {}; data.forEach(function (d) { keep[d.num] = 1; });
        var ops = data.map(function (d) { var row = {course_id:id, num:d.num, title:d.title, title_pl:d.title_pl, title_en:d.title_en || null, scene_en:d.scene_en || null, grammar:d.grammar, scene:d.scene, scene_pl:d.scene_pl, variants:d.variants || null, tasks:d.tasks}; if (byNum[d.num]) row.id = byNum[d.num].id; return row; });
        var extra = ls.filter(function (l) { return !keep[l.num]; });
        return ops.reduce(function (p, row, i) { return p.then(function () { msg.textContent = (i + 1) + ' / ' + ops.length; return API.saveLesson(row); }); }, Promise.resolve())
          .then(function () { return Promise.all(extra.map(function (l) { return API.deleteLesson(l.id); })); })
          .then(function () { var cc = Object.assign({}, c, {level:'B1–B2'}); delete cc.lessons_count; return API.saveCourse(cc); });
      }).then(function () { toast(t('Готово! 16 уроків завантажено.')); courseEditor(body, id); }).catch(function (e) { ih.disabled = false; msg.textContent = ''; toast(e.message, 'err'); });
    };
    var nl = document.getElementById('newL');
    if (nl) nl.onclick = function () { lessonEditor(body, id, null, ls.length + 1); };
    body.querySelectorAll('[data-l]').forEach(function (b) { b.onclick = function () { lessonEditor(body, id, b.dataset.l); }; });
  });
}

function lessonEditor(body, courseId, lessonId, nextNum) {
  var p = lessonId ? API.getLesson(lessonId) : Promise.resolve({course_id:courseId, num:nextNum, title:'', grammar:'', scene:'', tasks:[]});
  return p.then(function (l) {
    var V = JSON.parse(JSON.stringify(l.variants || {}));
    var sets = {en:JSON.parse(JSON.stringify(l.tasks || [])), pl:V.pl || [], uk:V.uk || []}, VER = 'en', tasks = sets.en;
    var VNAME = {en:'🇬🇧 EN (' + tx({uk:'основна', pl:'główna', en:'base'}) + ')', pl:'🇵🇱 PL', uk:'🇺🇦 UA'};
    function tipKeys() { return VER === 'en' ? ['tip', 'tip_uk', 'tip_pl'] : ['tip_en', 'tip_uk', 'tip_pl']; }
    function qtKeys() { return LANGS.filter(function (x) { return x !== VER; }).map(function (x) { return 'qt_' + x; }); }
    var BASE = ['type', 'img', 'q', 'options', 'answer', 'say'];
    function handled() { return BASE.concat(tipKeys(), qtKeys()); }
    function extraOf(tk) { var o = {}, h = handled(); Object.keys(tk).forEach(function (k) { if (h.indexOf(k) < 0) o[k] = tk[k]; }); return Object.keys(o).length ? JSON.stringify(o, null, 1) : ''; }
    var LBL = {tip:'💡 EN', tip_en:'💡 EN', tip_uk:'💡 UA', tip_pl:'💡 PL', qt_en:'🌐 EN', qt_uk:'🌐 UA', qt_pl:'🌐 PL'};
    function taskHtml(tk, i) {
      return '<div class="task-edit" data-i="' + i + t('"><div class="row" style="justify-content:space-between"><b>Завдання ') + (i + 1) + '</b><button class="btn btn-danger btn-sm" type="button" data-del="' + i + t('">Видалити</button></div>') +
        t('<div class="grid2"><label class="fl">Тип<select class="inp-s" data-f="type">') + Object.keys(TASK_TYPES).map(function (k) { return '<option value="' + k + '"' + (tk.type === k ? ' selected' : '') + '>' + TASK_TYPES[k] + '</option>'; }).join('') + '</select></label>' +
        '<label class="fl">' + t('Ілюстрація') + '<select class="inp-s" data-f="img"><option value="">—</option>' + ILLU_KEYS.map(function (k) { return '<option' + (tk.img === k ? ' selected' : '') + '>' + k + '</option>'; }).join('') + '</select></label></div>' +
        t('<label class="fl">Питання / речення (пропуск позначай ____)<input class="inp-s" data-f="q" value="') + esc(tk.q) + '"></label>' +
        t('<div class="grid2"><label class="fl">Варіанти через « / »<input class="inp-s" data-f="options" value="') + esc((tk.options || []).join(' / ')) + '"></label>' +
        t('<label class="fl">Номер правильного варіанта (1, 2, 3…)<input class="inp-s" data-f="answer" type="number" min="1" value="') + ((+tk.answer || 0) + 1) + '"></label></div>' +
        t('<label class="fl">Фраза для озвучення (необов\'язково)<input class="inp-s" data-f="say" value="') + esc(tk.say) + '"></label>' +
        '<details class="vx"><summary>' + tx({uk:'Підказки й переклади', pl:'Wskazówki i tłumaczenia', en:'Hints & translations'}) + '</summary>' +
        '<div class="grid3">' + tipKeys().map(function (k) { return '<label class="fl">' + LBL[k] + ' ' + tx({uk:'пояснення', pl:'wyjaśnienie', en:'explanation'}) + '<textarea class="inp-s" rows="2" data-f="' + k + '">' + esc(tk[k] || '') + '</textarea></label>'; }).join('') + '</div>' +
        '<div class="grid2">' + qtKeys().map(function (k) { return '<label class="fl">' + LBL[k] + ' ' + tx({uk:'переклад питання', pl:'tłumaczenie pytania', en:'question translation'}) + '<input class="inp-s" data-f="' + k + '" value="' + esc(tk[k] || '') + '"></label>'; }).join('') + '</div>' +
        '<label class="fl">' + tx({uk:'Інші поля (JSON: options_uk, q_pl…)', pl:'Inne pola (JSON: options_uk, q_pl…)', en:'Other fields (JSON: options_uk, q_pl…)'}) + '<textarea class="inp-s mono" rows="3" data-x="1">' + esc(extraOf(tk)) + '</textarea></label></details></div>';
    }
    function collect() {
      var err = null;
      body.querySelectorAll('.task-edit').forEach(function (el) {
        var i = +el.dataset.i, tk = tasks[i], keep = {};
        handled().forEach(function (k) { delete tk[k]; });
        el.querySelectorAll('[data-f]').forEach(function (f) { var k = f.dataset.f, v = f.value; if (k === 'options') tk.options = v.split('/').map(function (x) { return x.trim(); }).filter(Boolean); else if (k === 'answer') tk.answer = Math.max(0, (parseInt(v, 10) || 1) - 1); else if (v.trim() || k === 'q' || k === 'type') tk[k] = k === 'q' || k === 'type' ? v : v.trim(); });
        var x = el.querySelector('[data-x]'); if (x) {
          Object.keys(tk).forEach(function (k) { if (handled().indexOf(k) < 0) delete tk[k]; });
          if (x.value.trim()) { try { var o = JSON.parse(x.value); Object.keys(o).forEach(function (k) { tk[k] = o[k]; }); } catch (e) { err = tx({uk:'Помилка JSON у завданні ', pl:'Błąd JSON w zadaniu ', en:'JSON error in task '}) + (i + 1); } }
        }
      });
      return err;
    }
    function render() {
      body.innerHTML = t('<div style="display:grid;gap:18px"><button class="btn btn-ghost btn-sm" type="button" id="backC" style="justify-self:start">← До курсу</button>') +
        '<form class="panel form" id="lForm" novalidate><h3>' + (lessonId ? t('Редагування уроку') : t('Новий урок')) + '</h3>' +
        t('<div class="grid3"><label class="fl" for="lNum">Номер<input class="inp-s" id="lNum" type="number" min="1" value="') + esc(l.num) + t('"></label><label class="fl" for="lTitle" style="grid-column:span 2">Назва уроку<input class="inp-s" id="lTitle" value="') + esc(l.title) + '"></label></div>' +
        t('<div class="grid2"><label class="fl" for="lGr">Граматика / тема<input class="inp-s" id="lGr" value="') + esc(l.grammar) + t('"></label><label class="fl" for="lScene">Сцена (опис своїми словами)<input class="inp-s" id="lScene" value="') + esc(l.scene) + '"></label></div>' +
        '<div class="grid2"><label class="fl" for="lTitlePl">🇵🇱 Tytuł lekcji po polsku<input class="inp-s" id="lTitlePl" value="' + esc(l.title_pl) + '"></label><label class="fl" for="lScenePl">🇵🇱 Scena po polsku<input class="inp-s" id="lScenePl" value="' + esc(l.scene_pl) + '"></label></div>' +
        '<div class="grid2"><label class="fl" for="lTitleEn">🇬🇧 Lesson title in English<input class="inp-s" id="lTitleEn" value="' + esc(l.title_en || '') + '"></label><label class="fl" for="lSceneEn">🇬🇧 Scene in English<input class="inp-s" id="lSceneEn" value="' + esc(l.scene_en || '') + '"></label></div>' +
        '<h3 style="margin-top:8px">' + tx({uk:'Мова навчання цієї версії', pl:'Język nauki tej wersji', en:'Target language of this version'}) + '</h3>' +
        '<div class="vtabs">' + LANGS.map(function (x) { return '<button type="button" class="vtab' + (x === VER ? ' on' : '') + '" data-ver="' + x + '">' + VNAME[x] + ' <span class="muted small">' + sets[x].length + '</span></button>'; }).join('') + '</div>' +
        (VER !== 'en' ? '<div class="grid3">' + LANGS.map(function (sp) { return '<label class="fl">📘 ' + FLAG[sp] + ' ' + tx({uk:'тема граматики', pl:'temat gramatyki', en:'grammar label'}) + '<input class="inp-s" data-g="' + sp + '" value="' + esc(V[VER + '_grammar_' + sp] || '') + '"></label>'; }).join('') + '</div>' : '') +
        (VER !== 'en' && !tasks.length ? '<div class="empty small">' + tx({uk:'Цієї версії ще немає. Учні бачать урок як «скоро».', pl:'Tej wersji jeszcze nie ma. Uczniowie widzą lekcję jako „wkrótce”.', en:'No version yet. Students see this lesson as “coming soon”.'}) + ' <button class="btn btn-ghost btn-sm" type="button" id="copyEn">' + tx({uk:'Скопіювати структуру з EN', pl:'Skopiuj strukturę z EN', en:'Copy structure from EN'}) + '</button></div>' : '') +
        t('<h3 style="margin-top:8px">Завдання (') + tasks.length + ')</h3>' + tasks.map(taskHtml).join('') +
        t('<button class="btn btn-ghost btn-sm" type="button" id="addT" style="justify-self:start">+ Додати завдання</button>') +
        t('<div class="row"><button class="btn btn-red" type="submit">Зберегти урок</button>') + (lessonId ? '<a class="btn btn-ghost btn-sm" href="#/lesson/' + esc(lessonId) + t('">Переглянути як учень</a><button class="btn btn-danger btn-sm" type="button" id="delL">Видалити урок</button>') : '') + '</div><div class="msg" id="lMsg"></div></form></div>';
      function grabG() { body.querySelectorAll('[data-g]').forEach(function (g) { var k = VER + '_grammar_' + g.dataset.g; if (g.value.trim()) V[k] = g.value.trim(); else delete V[k]; }); }
      document.getElementById('backC').onclick = function () { courseEditor(body, courseId); };
      body.querySelectorAll('[data-ver]').forEach(function (b) { b.onclick = function () { var e = collect(); if (e) { toast(e, 'err'); return; } grabG(); VER = b.dataset.ver; tasks = sets[VER]; render(); }; });
      var ce = document.getElementById('copyEn'); if (ce) ce.onclick = function () { sets[VER] = sets.en.map(function (x) { return {type:x.type, img:x.img, q:'', options:[], answer:x.answer || 0}; }).map(function (x) { if (!x.img) delete x.img; return x; }); tasks = sets[VER]; render(); };
      document.getElementById('addT').onclick = function () { collect(); tasks.push({type:'quiz', q:'', options:[], answer:0}); render(); };
      body.querySelectorAll('[data-del]').forEach(function (b) { b.onclick = function () { collect(); tasks.splice(+b.dataset.del, 1); render(); }; });
      document.getElementById('lForm').onsubmit = function (e) {
        e.preventDefault(); var msg = document.getElementById('lMsg'), ce2 = collect(); grabG();
        if (ce2) { msg.className = 'msg err'; msg.textContent = ce2; return; }
        var title = document.getElementById('lTitle').value.trim();
        if (!title) { msg.className = 'msg err'; msg.textContent = t('Вкажи назву уроку.'); return; }
        var bad = []; LANGS.forEach(function (x) { var n = sets[x].filter(function (tk) { return !String(tk.q || '').trim(); }).length; if (n) bad.push(FLAG[x] + ': ' + n); });
        if (bad.length) { msg.className = 'msg err'; msg.textContent = tx({uk:'Порожні питання — ', pl:'Puste pytania — ', en:'Empty questions — '}) + bad.join(', '); return; }
        V.pl = sets.pl; V.uk = sets.uk; if (!V.pl.length) delete V.pl; if (!V.uk.length) delete V.uk;
        var nl = {id:lessonId || undefined, course_id:courseId, num:parseInt(document.getElementById('lNum').value, 10) || 1, title:title, grammar:document.getElementById('lGr').value, scene:document.getElementById('lScene').value, title_pl:document.getElementById('lTitlePl').value.trim(), scene_pl:document.getElementById('lScenePl').value.trim(), title_en:document.getElementById('lTitleEn').value.trim() || null, scene_en:document.getElementById('lSceneEn').value.trim() || null, tasks:sets.en, variants:V};
        if (l.variants === undefined && !V.pl && !V.uk) delete nl.variants;
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
/* ---------- ambient course backgrounds (subtle) ---------- */
function ambTheme(c) { var s = (c && (c.slug || '')) || ''; return /^harry/.test(s) ? 'hp' : /^vampire/.test(s) ? 'tvd' : null; }
var AMB_CUR = null;
function setAmbient(theme) {
  if (theme === AMB_CUR) return; AMB_CUR = theme;
  var el = document.getElementById('amb'); if (el) el.remove();
  document.body.classList.toggle('has-amb', !!theme);
  if (!theme) return;
  el = document.createElement('div'); el.id = 'amb'; el.className = 'amb amb-' + theme; el.setAttribute('aria-hidden', 'true');
  var h = '', i;
  if (theme === 'hp') {
    var spots = [[6,18],[14,62],[22,34],[31,78],[44,12],[57,55],[66,26],[74,70],[83,40],[92,16],[38,88],[88,82]];
    for (i = 0; i < spots.length; i++) h += '<span class="cdl" style="left:' + spots[i][0] + '%;top:' + spots[i][1] + '%;--d:' + (6 + (i % 5)) + 's;--o:' + (-i * 1.3) + 's;--s:' + (0.7 + (i % 3) * 0.2) + '"><i></i></span>';
  } else if (theme === 'tvd') {
    h = '<span class="moon"></span><span class="fog f1"></span><span class="fog f2"></span>';
    for (i = 0; i < 3; i++) h += '<span class="bat" style="--o:' + (-i * 9) + 's;--y:' + (12 + i * 14) + '%"><svg viewBox="0 0 64 24" width="34" height="13"><path d="M32 14c-2-4-6-6-10-4 1-4-3-7-7-6 2 2 2 4 1 6-4-3-9-3-12 0 6 0 9 3 10 6 3-2 7-2 10 0 2-1 5-2 8-2 3 0 6 1 8 2 3-2 7-2 10 0 1-3 4-6 10-6-3-3-8-3-12 0-1-2-1-4 1-6-4-1-8 2-7 6-4-2-8 0-10 4z" fill="currentColor"/></svg></span>';
  }
  el.innerHTML = h; document.body.insertBefore(el, document.body.firstChild);
}
document.addEventListener('visibilitychange', function () { document.body.classList.toggle('amb-paused', document.hidden); });
/* ================= EXTRAS 2026-10-18: оплата, пакет, тест рівня, серія, повторення, продажі ================= */
function todayStr(off) { var d = new Date(Date.now() + (off || 0) * 86400000); return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0'); }
function lsGet(k, d) { try { var v = localStorage.getItem(k); return v == null ? d : JSON.parse(v); } catch (e) { return d; } }
function lsSet(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }

/* ---------- оплата ---------- */
function startCheckout(courseId, bundle) {
  if (!USER) { toast(tx({uk:'Спершу створи кабінет або увійди — так курс одразу з\'явиться в тебе.', pl:'Najpierw załóż konto lub zaloguj się — kurs od razu pojawi się na Twoim koncie.', en:'Create an account or log in first — the course will appear in it right away.'}), 'info'); lsSet('ml_after_login', bundle ? 'bundle' : courseId); location.hash = '#/register'; return; }
  if (API.mode === 'demo' || !API.token) { location.hash = '#/buy'; return; }
  toast(tx({uk:'Відкриваю оплату…', pl:'Otwieram płatność…', en:'Opening checkout…'}), 'info');
  API.token().then(function (tk) {
    return fetch(cfg.SUPABASE_URL + '/functions/v1/checkout', {method:'POST', headers:{'Content-Type':'application/json', Authorization:'Bearer ' + tk, apikey:cfg.SUPABASE_ANON_KEY}, body:JSON.stringify(bundle ? {bundle:true} : {course_id:courseId})});
  }).then(function (r) { return r.json().then(function (j) { if (!r.ok || !j.url) throw new Error(j.error || 'HTTP ' + r.status); return j; }); })
    .then(function (j) { location.href = j.url; })
    .catch(function (e) { toast(tx({uk:'Онлайн-оплата поки недоступна: ', pl:'Płatność online jest chwilowo niedostępna: ', en:'Online payment is unavailable: '}) + e.message, 'err'); location.hash = '#/buy'; });
}
document.addEventListener('click', function (e) {
  var a = e.target.closest && e.target.closest('a[href="#/buy"]'), hp = location.hash.split('/');
  if (a && (hp[1] === 'course' || hp[1] === 'lesson') && hp[2]) { e.preventDefault(); if (hp[1] === 'course') startCheckout(hp[2]); else API.getLesson(hp[2]).then(function (l) { startCheckout(l && l.course_id); }); return; }
  var b = e.target.closest && e.target.closest('[data-buy-course],[data-buy-bundle]'); if (!b) return;
  e.preventDefault(); startCheckout(b.dataset.buyCourse || null, b.hasAttribute('data-buy-bundle'));
});
function bundleHtml() {
  var price = (SETTINGS && SETTINGS.bundle_price) || '149 zł';
  return '<div class="panel bundle"><div><div class="eyebrow">' + tx({uk:'ПАКЕТ', pl:'PAKIET', en:'BUNDLE'}) + '</div><h3>' + tx({uk:'Усі марафони в одному ключі', pl:'Wszystkie maratony w jednym kluczu', en:'Every marathon in one key'}) + '</h3>' +
    '<p class="muted">' + tx({uk:'Гаррі Поттер, Щоденники вампіра, Сам удома, Друзі — і всі нові курси, що з\'являться. Три мови: EN · PL · UA.', pl:'Harry Potter, Pamiętniki wampirów, Kevin sam w domu, Przyjaciele, Zwierzogród — i wszystkie nowe kursy. Trzy języki: EN · PL · UA.', en:'Harry Potter, The Vampire Diaries, Home Alone, Friends, Zootopia — and every new course. Three languages: EN · PL · UA.'}) + '</p></div>' +
    '<div class="bundle-buy"><div class="amount">' + esc(price) + '</div><button class="btn btn-red" type="button" data-buy-bundle>' + tx({uk:'Купити пакет', pl:'Kup pakiet', en:'Buy the bundle'}) + '</button><small class="muted">BLIK · Przelewy24 · ' + tx({uk:'картка', pl:'karta', en:'card'}) + '</small></div></div>';
}
function viewPaid(sid) {
  if (!requireUser()) return Promise.resolve();
  $app.innerHTML = '<div class="page"><div class="panel paid"><div class="c3-seal">⏳</div><h2>' + tx({uk:'Перевіряємо оплату…', pl:'Sprawdzamy płatność…', en:'Checking your payment…'}) + '</h2><p class="muted" id="paidMsg">' + tx({uk:'Зазвичай це кілька секунд. BLIK і Przelewy24 інколи до хвилини.', pl:'Zwykle to kilka sekund. BLIK i Przelewy24 czasem do minuty.', en:'Usually a few seconds; BLIK and Przelewy24 can take up to a minute.'}) + '</p></div></div>';
  var tries = 0;
  function poll() {
    if (!API.sb) return Promise.resolve();
    return API.sb.from('orders').select('*').eq('session_id', sid).maybeSingle().then(function (r) {
      var o = r.data;
      if (o && o.status === 'paid') {
        API.clearCache && API.clearCache();
        var box = $app.querySelector('.paid'); if (!box) return;
        box.innerHTML = '<div class="c3-seal">🎉</div><h2>' + tx({uk:'Оплату отримано! Курс відкрито.', pl:'Płatność przyjęta! Kurs odblokowany.', en:'Payment received! Course unlocked.'}) + '</h2>' +
          '<p class="muted">' + tx({uk:'Твій ключ (про всяк випадок, щоб подарувати чи зберегти):', pl:'Twój klucz (na wszelki wypadek — do zachowania lub podarowania):', en:'Your key (keep it or gift it):'}) + '</p><p class="keycode">' + esc(String(o.key_code || '').replace(/(.{4})(?=.)/g, '$1-')) + '</p>' +
          '<div class="row" style="justify-content:center">' + (o.course_id ? '<a class="btn btn-red" href="#/course/' + esc(o.course_id) + '">' + tx({uk:'До курсу', pl:'Do kursu', en:'Go to the course'}) + '</a>' : '') + '<a class="btn btn-ghost" href="#/cabinet">' + tx({uk:'Мій кабінет', pl:'Mój kabinet', en:'My dashboard'}) + '</a></div>';
        return;
      }
      if (++tries < 40) setTimeout(poll, 2500);
      else { var m = document.getElementById('paidMsg'); if (m) m.innerHTML = tx({uk:'Оплата ще обробляється. Курс з\'явиться в кабінеті автоматично. Якщо ні — напиши на ', pl:'Płatność jest jeszcze przetwarzana. Kurs pojawi się w kabinecie automatycznie. Jeśli nie — napisz na ', en:'The payment is still processing; the course will appear automatically. If not, write to '}) + 'info.movielang@gmail.com'; }
    });
  }
  poll(); return Promise.resolve();
}

/* ---------- тест рівня ---------- */
var LVL_Q = [
 ['A1', 'My sister ____ a teacher.', ['is', 'are', 'am', 'be']],
 ['A1', 'I ____ coffee every morning.', ['drink', 'drinks', 'drinking', 'am drink']],
 ['A1', 'There ____ two cats in the kitchen.', ['are', 'is', 'be', 'has']],
 ['A2', 'Yesterday we ____ to the cinema.', ['went', 'go', 'goed', 'have gone']],
 ['A2', 'Look! It ____ outside.', ['is raining', 'rains', 'rain', 'raining']],
 ['A2', 'This film is ____ than the book.', ['better', 'more good', 'best', 'gooder']],
 ['B1', 'I ____ never ____ to London.', ['have / been', 'did / go', 'was / be', 'have / go']],
 ['B1', 'If it rains tomorrow, we ____ at home.', ['will stay', 'stay', 'would stay', 'stayed']],
 ['B1', 'The letter ____ by Harry\'s owl.', ['was brought', 'brought', 'was bring', 'has bring']],
 ['B2', 'If I ____ about the party, I would have come.', ['had known', 'knew', 'have known', 'would know']],
 ['B2', 'She asked me where ____.', ['I lived', 'did I live', 'do I live', 'I do live']],
 ['B2', 'I wish I ____ so much yesterday.', ['hadn\'t said', 'didn\'t say', 'don\'t say', 'wouldn\'t say']]
];
var LVL_REC = {A1:'A1–A2', A2:'A2', B1:'B1', B2:'B2'};
function viewTest() {
  var qs = LVL_Q.map(function (q) { return {lvl:q[0], q:q[1], right:q[2][0], opts:shuffle(q[2])}; }), i = 0, score = {A1:0, A2:0, B1:0, B2:0};
  function render() {
    if (i >= qs.length) return finish();
    var q = qs[i];
    $app.innerHTML = '<div class="page"><div class="sec-head"><div class="eyebrow">' + tx({uk:'Тест рівня', pl:'Test poziomu', en:'Level test'}) + ' · ' + (i + 1) + ' / ' + qs.length + '</div><h2>' + tx({uk:'Обери правильну відповідь', pl:'Wybierz poprawną odpowiedź', en:'Choose the right answer'}) + '</h2></div>' +
      '<div class="panel lvltest"><div class="c3-prog"><i style="width:' + Math.round(i / qs.length * 100) + '%"></i></div><p class="lvl-q">' + esc(q.q).replace('____', '<span class="gap">____</span>') + '</p><div class="lvl-opts">' +
      q.opts.map(function (o, k) { return '<button type="button" class="btn btn-ghost" data-k="' + k + '">' + esc(o) + '</button>'; }).join('') + '</div><button type="button" class="btn btn-ghost btn-sm" id="lvlSkip">' + tx({uk:'Не знаю', pl:'Nie wiem', en:'I don\'t know'}) + '</button></div></div>';
    $app.querySelectorAll('[data-k]').forEach(function (b) { b.onclick = function () { var ok = q.opts[+b.dataset.k] === q.right; if (ok) score[q.lvl]++; b.classList.add(ok ? 'right' : 'wrong'); setTimeout(function () { i++; render(); }, 350); }; });
    document.getElementById('lvlSkip').onclick = function () { i++; render(); };
  }
  function finish() {
    var lvl = 'A1'; if (score.A1 >= 2) lvl = 'A2'; if (lvl === 'A2' && score.A2 >= 2) lvl = 'B1'; if (lvl === 'B1' && score.B1 >= 2) lvl = 'B2'; if (lvl === 'B2' && score.B2 < 2) lvl = 'B1+';
    if (lvl === 'B1+') lvl = 'B1';
    lsSet('ml_level', lvl); if (USER && API.sb) API.sb.rpc('set_my_level', {p_level:lvl}).then(function () {}, function () {});
    var total = score.A1 + score.A2 + score.B1 + score.B2;
    return API.listCourses(false).then(function (cs) {
      var order = ['A1', 'A2', 'B1', 'B2'], li = order.indexOf(lvl);
      function fit(c) { var lv = String(c.level || '').match(/[ABC][12]/g) || []; return lv.some(function (x) { var k = order.indexOf(x); return k === li || k === li + 1; }); }
      var rec = cs.filter(fit); if (!rec.length) rec = cs.slice(0, 2);
      var desc = {A1:tx({uk:'Початковий. Почни з простих сцен і базових часів.', pl:'Początkujący. Zacznij od prostych scen i podstawowych czasów.', en:'Beginner. Start with simple scenes and basic tenses.'}), A2:tx({uk:'Базовий. Ти розумієш прості діалоги — час для комедій і сімейного кіно.', pl:'Podstawowy. Rozumiesz proste dialogi — czas na komedie i kino familijne.', en:'Elementary. You follow simple dialogue — time for comedies and family films.'}), B1:tx({uk:'Середній. Серіали з живою розмовною мовою — саме для тебе.', pl:'Średni. Seriale z żywym, potocznym językiem są dla Ciebie.', en:'Intermediate. Series with real everyday speech are for you.'}), B2:tx({uk:'Вище середнього. Складна граматика й швидкі діалоги.', pl:'Wyższy średni. Trudna gramatyka i szybkie dialogi.', en:'Upper-intermediate. Advanced grammar and fast dialogue.'})}[lvl];
      $app.innerHTML = '<div class="page"><div class="panel paid"><div class="eyebrow">' + tx({uk:'Твій результат', pl:'Twój wynik', en:'Your result'}) + ' · ' + total + ' / ' + qs.length + '</div><div class="lvl-big">' + lvl + '</div><p class="lead">' + desc + '</p></div>' +
        '<div class="sec-head" style="margin-top:28px"><h2>' + tx({uk:'Рекомендовані марафони', pl:'Polecane maratony', en:'Recommended marathons'}) + '</h2></div>' + catalogGrid(rec) +
        '<div class="row" style="justify-content:center;margin-top:20px"><a class="btn btn-red" href="#/trial">' + tx({uk:'Безкоштовний пробний урок', pl:'Darmowa lekcja próbna', en:'Free trial lesson'}) + '</a><button class="btn btn-ghost" type="button" id="lvlAgain">' + tx({uk:'Пройти ще раз', pl:'Powtórz test', en:'Retake'}) + '</button></div></div>';
      document.getElementById('lvlAgain').onclick = function () { viewTest(); };
    });
  }
  render(); return Promise.resolve();
}
function levelTeaser() {
  var lv = lsGet('ml_level', null);
  return '<section><div class="panel teaser"><div><div class="eyebrow">' + tx({uk:'2 хвилини', pl:'2 minuty', en:'2 minutes'}) + '</div><h3>' + (lv ? tx({uk:'Твій рівень: ', pl:'Twój poziom: ', en:'Your level: '}) + lv : tx({uk:'Не знаєш свій рівень?', pl:'Nie znasz swojego poziomu?', en:'Not sure about your level?'})) + '</h3><p class="muted">' + tx({uk:'12 питань — і ми підкажемо, з якого фільму почати.', pl:'12 pytań — i podpowiemy, od którego filmu zacząć.', en:'12 questions and we\'ll tell you which film to start with.'}) + '</p></div><a class="btn btn-red" href="#/test">' + (lv ? tx({uk:'Пройти ще раз', pl:'Zrób test ponownie', en:'Retake the test'}) : tx({uk:'Пройти тест рівня', pl:'Zrób test poziomu', en:'Take the level test'})) + '</a></div></section>';
}

/* ---------- активність, серія 🔥 і денна ціль ---------- */
function bumpActivity(lessons, reviews) {
  var d = todayStr(), loc = lsGet('ml_act', {}); var r = loc[d] || {l:0, r:0}; r.l += lessons; r.r += reviews; loc[d] = r; lsSet('ml_act', loc);
  if (USER && API.sb) API.sb.rpc('bump_activity', {p_day:d, p_lessons:lessons, p_reviews:reviews}).then(function () {}, function () {});
}
function loadActivity() {
  var loc = lsGet('ml_act', {});
  var pr = (USER && API.sb) ? API.sb.from('activity').select('*').eq('user_id', USER.id).then(function (r) { return r.data || []; }, function () { return []; }) : Promise.resolve([]);
  return Promise.all([pr, Promise.all(LANGS.map(function (l) { return API.myProgress(l).catch(function () { return []; }); }))]).then(function (r) {
    var days = {};
    Object.keys(loc).forEach(function (d) { days[d] = {l:loc[d].l || 0, r:loc[d].r || 0}; });
    r[0].forEach(function (a) { var x = days[a.day] || {l:0, r:0}; x.l = Math.max(x.l, a.lessons); x.r = Math.max(x.r, a.reviews); days[a.day] = x; });
    r[1].forEach(function (ps) { ps.forEach(function (p) { [p.completed_at, p.retry_at].forEach(function (ts) { if (!ts) return; var dd = new Date(ts), k = dd.getFullYear() + '-' + String(dd.getMonth() + 1).padStart(2, '0') + '-' + String(dd.getDate()).padStart(2, '0'); var x = days[k] || {l:0, r:0}; x.l = Math.max(x.l, 1); days[k] = x; }); }); });
    var streak = 0, off = days[todayStr()] ? 0 : -1;
    while (days[todayStr(off - streak)]) streak++;
    var best = 0, run = 0, keys = Object.keys(days).sort(), prev = null;
    keys.forEach(function (k) { var t0 = new Date(k + 'T12:00:00').getTime(); run = prev && Math.round((t0 - prev) / 86400000) === 1 ? run + 1 : 1; prev = t0; best = Math.max(best, run); });
    return {days:days, streak:streak, best:Math.max(best, streak), today:days[todayStr()] || {l:0, r:0}};
  });
}
function goalOf() { return lsGet('ml_goal', {l:1, r:10}); }
function todayBoxHtml(a, due) {
  var g = goalOf(), tl = a.today.l, trv = a.today.r, done = tl >= g.l && trv >= g.r;
  var pct = Math.round(Math.min(1, (Math.min(tl, g.l) + Math.min(trv, g.r) / Math.max(g.r, 1) * Math.max(g.l, 1)) / (g.l * 2)) * 100);
  var wk = []; for (var i = 6; i >= 0; i--) { var d = todayStr(-i); wk.push('<i class="' + (a.days[d] ? 'on' : '') + (i === 0 ? ' now' : '') + '" title="' + d + '"></i>'); }
  return '<div class="box today"><div class="today-top"><div class="streak"><span class="fire' + (a.streak ? '' : ' off') + '">🔥</span><div><b>' + a.streak + '</b><small>' + tx({uk:'днів поспіль', pl:'dni z rzędu', en:'day streak'}) + '</small></div></div>' +
    '<div class="goal"><div class="ring" style="--p:' + pct + '"><span>' + (done ? '✓' : pct + '%') + '</span></div><div><b>' + tx({uk:'Ціль на сьогодні', pl:'Cel na dziś', en:'Today\'s goal'}) + '</b><small>' + tx({uk:'уроки', pl:'lekcje', en:'lessons'}) + ' ' + Math.min(tl, g.l) + '/' + g.l + ' · ' + tx({uk:'слова', pl:'słowa', en:'words'}) + ' ' + Math.min(trv, g.r) + '/' + g.r + '</small><button type="button" class="linkbtn small" id="goalEdit">' + tx({uk:'змінити ціль', pl:'zmień cel', en:'change goal'}) + '</button></div></div></div>' +
    '<div class="wkdots">' + wk.join('') + '<small class="muted">' + tx({uk:'рекорд: ', pl:'rekord: ', en:'best: '}) + a.best + '</small></div>' +
    '<a class="btn ' + (due ? 'btn-red' : 'btn-ghost') + ' btn-sm" href="#/review">🧠 ' + tx({uk:'Повторення дня', pl:'Powtórka dnia', en:'Daily review'}) + (due ? ' · ' + due : '') + '</a>' +
    (!a.today.l && !a.today.r && a.streak ? '<p class="small warn-t">' + tx({uk:'Позайматися сьогодні — і серія не згорить!', pl:'Poćwicz dziś, żeby nie stracić serii!', en:'Practise today to keep your streak!'}) + '</p>' : '') + '</div>';
}
function bindGoal() {
  var b = document.getElementById('goalEdit'); if (!b) return;
  b.onclick = function () {
    var g = goalOf();
    var w = mbox('<h3>' + tx({uk:'Денна ціль', pl:'Cel dzienny', en:'Daily goal'}) + '</h3><div class="form"><label class="fl">' + tx({uk:'Уроків на день', pl:'Lekcji dziennie', en:'Lessons per day'}) + '<input class="inp" type="number" min="0" max="5" id="gL" value="' + g.l + '"></label><label class="fl">' + tx({uk:'Слів на повторення', pl:'Słów do powtórki', en:'Words to review'}) + '<input class="inp" type="number" min="0" max="100" step="5" id="gR" value="' + g.r + '"></label><button class="btn btn-red" type="button" id="gSave">' + tx({uk:'Зберегти', pl:'Zapisz', en:'Save'}) + '</button></div>');
    w.querySelector('#gSave').onclick = function () { lsSet('ml_goal', {l:Math.max(0, Math.min(5, +w.querySelector('#gL').value || 0)), r:Math.max(0, Math.min(100, +w.querySelector('#gR').value || 0))}); w.remove(); route(); };
  };
}

/* ---------- повторення слів (SRS: 1 · 3 · 7 · 14 · 30 днів) ---------- */
var SRS_STEPS = [1, 3, 7, 14, 30], SRS_NEW = 10;
function srsLocalKey() { return 'ml_srs_' + TARGET; }
function srsRows() {
  if (USER && API.sb) return API.sb.from('word_review').select('*').eq('user_id', USER.id).eq('target', TARGET).then(function (r) { var o = {}; (r.data || []).forEach(function (x) { o[x.word] = x; }); return o; }, function () { return lsGet(srsLocalKey(), {}); });
  return Promise.resolve(lsGet(srsLocalKey(), {}));
}
function srsSave(row) {
  var loc = lsGet(srsLocalKey(), {}); loc[row.word] = row; lsSet(srsLocalKey(), loc);
  if (USER && API.sb) API.sb.from('word_review').upsert({user_id:USER.id, target:TARGET, word:row.word, meaning:row.meaning, step:row.step, due:row.due, updated_at:new Date().toISOString()}).then(function () {}, function () {});
}
function srsPool() {
  return loadDefs().then(function () { return Promise.all([API.myEnrollments(), API.myProgress(TARGET)]); }).then(function (r) {
    var enr = r[0], done = {}; r[1].forEach(function (p) { done[p.lesson_id] = 1; });
    return Promise.all(enr.map(function (cid) { return API.listLessons(cid); })).then(function (lists) {
      var ls = []; lists.forEach(function (x) { x.forEach(function (l) { if (done[l.id]) ls.push(l); }); });
      return wordsOf(ls).filter(function (w) { return w.m; });
    });
  });
}
function srsQueue() {
  return Promise.all([srsPool(), srsRows()]).then(function (r) {
    var pool = r[0], rows = r[1], known = knownSet(), today = todayStr(), due = [], fresh = [];
    var byW = {}; pool.forEach(function (w) { byW[w.w] = w; });
    Object.keys(rows).forEach(function (k) { var x = rows[k]; if (x.due <= today && x.step < SRS_STEPS.length + 1) due.push({w:k, m:(byW[k] && byW[k].m) || x.meaning, ipa:byW[k] ? byW[k].ipa : '', ex:byW[k] ? byW[k].ex : '', row:x}); });
    var newToday = lsGet('ml_srs_new_' + TARGET, {d:'', n:0}); if (newToday.d !== today) newToday = {d:today, n:0};
    pool.forEach(function (w) { if (!rows[w.w] && !known[w.w]) fresh.push(w); });
    fresh = fresh.slice(0, Math.max(0, SRS_NEW - newToday.n));
    return {due:due, fresh:fresh, pool:pool, newToday:newToday};
  });
}
function viewReview() {
  if (!requireUser()) return Promise.resolve();
  $app.innerHTML = '<div class="page"><p class="muted">' + t('Завантаження…') + '</p></div>';
  return srsQueue().then(function (q) {
    var cards = q.due.concat(q.fresh.map(function (w) { return {w:w.w, m:w.m, ipa:w.ipa, ex:w.ex, row:null}; }));
    cards = shuffle(cards);
    var head = '<div class="sec-head"><a href="#/cabinet" class="muted small">← ' + t('Мій кабінет') + '</a><div class="eyebrow">' + tx({uk:'Повторення дня', pl:'Powtórka dnia', en:'Daily review'}) + ' · ' + FLAG[TARGET] + '</div>';
    if (!q.pool.length) { $app.innerHTML = '<div class="page">' + head + '<h2>' + tx({uk:'Поки нічого повторювати', pl:'Na razie nie ma czego powtarzać', en:'Nothing to review yet'}) + '</h2><p class="lead">' + tx({uk:'Пройди перший урок — слова з нього з\'являться тут і повертатимуться через 1, 3, 7, 14 і 30 днів.', pl:'Przejdź pierwszą lekcję — jej słowa pojawią się tutaj i będą wracać po 1, 3, 7, 14 i 30 dniach.', en:'Finish a lesson — its words will show up here and come back after 1, 3, 7, 14 and 30 days.'}) + '</p></div></div>'; return; }
    if (!cards.length) { $app.innerHTML = '<div class="page">' + head + '<h2>✓ ' + tx({uk:'На сьогодні все!', pl:'Na dziś wszystko!', en:'All done for today!'}) + '</h2><p class="lead">' + tx({uk:'Наступні слова чекають на тебе завтра. Мозок дякує 🧠', pl:'Kolejne słowa czekają na Ciebie jutro. Mózg dziękuje 🧠', en:'More words tomorrow. Your brain says thanks 🧠'}) + '</p></div><div class="row"><a class="btn btn-red" href="#/cabinet">' + t('Мій кабінет') + '</a><a class="btn btn-ghost" href="#/words">' + tx({uk:'Мій словник', pl:'Mój słownik', en:'My words'}) + '</a></div></div>'; return; }
    var i = 0, good = 0, total = cards.length, again = [];
    function show() {
      if (i >= cards.length) {
        if (again.length) { cards = cards.concat(again); again = []; }
        else return end();
      }
      var c = cards[i], others = shuffle(q.pool.filter(function (w) { return w.w !== c.w && w.m && w.m !== c.m; })).slice(0, 3).map(function (w) { return w.m; });
      var opts = shuffle([c.m].concat(others));
      $app.innerHTML = '<div class="page">' + head + '<h2>' + tx({uk:'Що означає це слово?', pl:'Co znaczy to słowo?', en:'What does this word mean?'}) + '</h2></div>' +
        '<div class="panel srs"><div class="c3-prog"><i style="width:' + Math.round(Math.min(i, total) / total * 100) + '%"></i></div><div class="srs-tag">' + (c.row ? tx({uk:'повторення', pl:'powtórka', en:'review'}) : tx({uk:'нове слово', pl:'nowe słowo', en:'new word'})) + '</div>' +
        '<div class="srs-w">' + esc(c.w) + ' <button type="button" class="linkbtn" id="srsSay" aria-label="say">🔊</button></div>' + (c.ipa ? '<div class="muted">' + esc(c.ipa) + '</div>' : '') +
        '<div class="lvl-opts">' + opts.map(function (o, k) { return '<button type="button" class="btn btn-ghost" data-k="' + k + '">' + esc(o) + '</button>'; }).join('') + '</div><div id="srsEx" class="muted small"></div></div></div>';
      document.getElementById('srsSay').onclick = function () { say(c.w); };
      $app.querySelectorAll('[data-k]').forEach(function (b) { b.onclick = function () {
        var ok = opts[+b.dataset.k] === c.m; $app.querySelectorAll('[data-k]').forEach(function (x) { x.disabled = true; if (opts[+x.dataset.k] === c.m) x.classList.add('right'); }); if (!ok) b.classList.add('wrong');
        var step = c.row ? c.row.step : 0;
        if (!c.retry) {
          if (ok) { good++; step = Math.min(step + 1, SRS_STEPS.length); } else step = 0;
          var nd = todayStr(ok ? SRS_STEPS[Math.max(0, step - 1)] : 1);
          srsSave({word:c.w, meaning:c.m, step:step, due:nd});
          if (!c.row) { q.newToday.n++; lsSet('ml_srs_new_' + TARGET, q.newToday); }
          bumpActivity(0, 1);
        }
        if (!ok) again.push({w:c.w, m:c.m, ipa:c.ipa, ex:c.ex, row:{step:0}, retry:true});
        if (c.ex) document.getElementById('srsEx').textContent = '“' + c.ex + '”';
        setTimeout(function () { i++; show(); }, ok ? 650 : 1500);
      }; });
    }
    function end() {
      var pct = Math.round(good / total * 100);
      $app.innerHTML = '<div class="page"><div class="panel paid"><div class="c3-seal">' + (pct >= 80 ? '🏆' : '🧠') + '</div><h2>' + tx({uk:'Повторення завершено!', pl:'Powtórka ukończona!', en:'Review complete!'}) + '</h2><p class="lead">' + good + ' / ' + total + ' · ' + pct + '%</p><p class="muted">' + tx({uk:'Слова з помилками повернуться завтра, правильні — пізніше.', pl:'Słowa z błędami wrócą jutro, poprawne — później.', en:'Missed words return tomorrow, the rest later.'}) + '</p><div class="row" style="justify-content:center"><a class="btn btn-red" href="#/cabinet">' + t('Мій кабінет') + '</a></div></div></div>';
    }
    show();
  });
}

/* ---------- обгортки існуючих сторінок ---------- */
var _viewCabinet = viewCabinet;
viewCabinet = function () {
  return Promise.resolve(_viewCabinet()).then(function () {
    var main = document.querySelector('.dmain'); if (!main || !USER) return;
    var ph = document.createElement('div'); ph.className = 'today-wrap'; main.insertBefore(ph, main.firstChild);
    return Promise.all([loadActivity(), srsQueue().catch(function () { return {due:[], fresh:[]}; })]).then(function (r) { ph.innerHTML = todayBoxHtml(r[0], r[1].due.length + r[1].fresh.length); bindGoal(); });
  }).then(function () {
    var pend = lsGet('ml_after_login', null); if (pend && USER) { lsSet('ml_after_login', null); startCheckout(pend === 'bundle' ? null : pend, pend === 'bundle'); }
  });
};
var _viewHome = viewHome;
viewHome = function () { return Promise.resolve(_viewHome()).then(function () { var s = $app.querySelector('#pricing'); if (s) { s.insertAdjacentHTML('beforebegin', levelTeaser()); s.insertAdjacentHTML('beforeend', bundleHtml()); } }); };
var _viewPricing = viewPricing;
viewPricing = function () { return Promise.resolve(_viewPricing()).then(function () { var p = $app.querySelector('.prices'); if (p) p.insertAdjacentHTML('afterend', bundleHtml()); }); };
var _viewBuy = viewBuy;
viewBuy = function () { return Promise.resolve(_viewBuy()).then(function () { var p = $app.querySelector('.prices'); if (p) p.insertAdjacentHTML('afterend', bundleHtml()); }); };
if (API.myEnrollments) { var _me = API.myEnrollments; API.myEnrollments = function () { return Promise.all([_me.apply(API, arguments), API.listCourses(false).catch(function () { return []; })]).then(function (r) { var ids = r[0].slice(); r[1].forEach(function (c) { if (isFreeCourse(c) && c.lessons_count && ids.indexOf(c.id) < 0) ids.push(c.id); }); return ids; }); }; }
if (API.saveProgress) { var _sp = API.saveProgress; API.saveProgress = function () { bumpActivity(1, 0); return _sp.apply(API, arguments); }; }

/* ---------- адмін: продажі та воронка ---------- */
function adminSales(body) {
  if (!API.sb) { body.innerHTML = '<div class="empty">' + tx({uk:'Доступно лише з базою Supabase.', pl:'Dostępne tylko z bazą Supabase.', en:'Requires Supabase.'}) + '</div>'; return Promise.resolve(); }
  var sb = API.sb;
  return Promise.all([sb.from('orders').select('*').order('created_at', {ascending:false}).limit(500), API.listCourses(true), sb.from('lessons').select('id,num,course_id'), sb.from('progress').select('user_id,lesson_id'), sb.from('progress_lang').select('user_id,lesson_id'), sb.from('enrollments').select('*'), sb.from('profiles').select('id,email,created_at,level'), sb.from('activity').select('*').gte('day', todayStr(-29))]).then(function (r) {
    var orders = r[0].data || [], cs = r[1], ls = r[2].data || [], prog = (r[3].data || []).concat(r[4].data || []), enr = r[5].data || [], users = r[6].data || [], act = r[7].data || [];
    var paid = orders.filter(function (o) { return o.status === 'paid'; }), now = Date.now();
    var sum = function (a) { return a.reduce(function (s, o) { return s + (+o.amount || 0); }, 0) / 100; };
    var m30 = paid.filter(function (o) { return now - new Date(o.paid_at || o.created_at) < 30 * 86400000; });
    var cname = function (id) { var c = cs.filter(function (x) { return x.id === id; })[0]; return c ? tr(c, 'title') : '—'; };
    var buyers = {}; enr.forEach(function (e) { buyers[e.user_id] = 1; });
    var conv = users.length ? Math.round(Object.keys(buyers).length / users.length * 100) : 0;
    var dau = {}; act.forEach(function (a) { dau[a.day] = (dau[a.day] || 0) + 1; });
    var lvls = {}; users.forEach(function (u) { if (u.level) lvls[u.level] = (lvls[u.level] || 0) + 1; });
    var funnels = cs.map(function (c) {
      var cl = ls.filter(function (l) { return l.course_id === c.id; }).sort(function (a, b) { return a.num - b.num; });
      var byL = {}; prog.forEach(function (p) { (byL[p.lesson_id] = byL[p.lesson_id] || {})[p.user_id] = 1; });
      var cnt = cl.map(function (l) { return {n:l.num, u:Object.keys(byL[l.id] || {}).length}; });
      var max = Math.max.apply(null, cnt.map(function (x) { return x.u; }).concat([1]));
      var drop = null; for (var k = 1; k < cnt.length; k++) { var d = cnt[k - 1].u - cnt[k].u; if (cnt[k - 1].u && (!drop || d > drop.d)) drop = {d:d, n:cnt[k].n}; }
      return '<div class="box"><h4>' + esc(tr(c, 'title')) + '</h4><div class="funnel">' + cnt.map(function (x) { return '<i title="' + tx({uk:'Урок ', pl:'Lekcja ', en:'Lesson '}) + x.n + ': ' + x.u + '" style="height:' + Math.max(2, Math.round(x.u / max * 80)) + 'px"></i>'; }).join('') + '</div><p class="small muted">' + tx({uk:'Почали: ', pl:'Zaczęło: ', en:'Started: '}) + (cnt[0] ? cnt[0].u : 0) + ' · ' + tx({uk:'дійшли до кінця: ', pl:'doszło do końca: ', en:'finished: '}) + (cnt.length ? cnt[cnt.length - 1].u : 0) + (drop && drop.d > 0 ? ' · ' + tx({uk:'найбільший відтік перед уроком ', pl:'największy odpływ przed lekcją ', en:'biggest drop before lesson '}) + drop.n + ' (−' + drop.d + ')' : '') + '</p></div>';
    }).join('');
    body.innerHTML = '<div style="display:grid;gap:18px"><div class="stats">' +
      '<div class="stat"><b>' + sum(m30).toFixed(0) + ' zł</b><span>' + tx({uk:'виручка за 30 днів', pl:'przychód 30 dni', en:'revenue, 30 days'}) + '</span></div>' +
      '<div class="stat"><b>' + sum(paid).toFixed(0) + ' zł</b><span>' + tx({uk:'виручка всього', pl:'przychód łącznie', en:'total revenue'}) + '</span></div>' +
      '<div class="stat"><b>' + paid.length + '</b><span>' + tx({uk:'оплачених замовлень', pl:'opłaconych zamówień', en:'paid orders'}) + '</span></div>' +
      '<div class="stat"><b>' + conv + '%</b><span>' + tx({uk:'реєстрацій → курс', pl:'rejestracji → kurs', en:'signups → course'}) + '</span></div></div>' +
      '<div class="stats"><div class="stat"><b>' + (dau[todayStr()] || 0) + '</b><span>' + tx({uk:'активних сьогодні', pl:'aktywnych dziś', en:'active today'}) + '</span></div><div class="stat"><b>' + orders.filter(function (o) { return o.status !== 'paid'; }).length + '</b><span>' + tx({uk:'кинутих кошиків', pl:'porzuconych koszyków', en:'abandoned checkouts'}) + '</span></div><div class="stat"><b>' + (Object.keys(lvls).map(function (k) { return k + ': ' + lvls[k]; }).join(' · ') || '—') + '</b><span>' + tx({uk:'рівні з тесту', pl:'poziomy z testu', en:'test levels'}) + '</span></div></div>' +
      '<h3>' + tx({uk:'Воронка уроків (скільки учнів пройшли кожен урок)', pl:'Lejek lekcji (ilu uczniów przeszło każdą lekcję)', en:'Lesson funnel (students per lesson)'}) + '</h3><div class="rows">' + funnels + '</div>' +
      '<h3>' + tx({uk:'Останні замовлення', pl:'Ostatnie zamówienia', en:'Latest orders'}) + '</h3><div class="tbl-wrap"><table class="tbl"><tr><th>' + tx({uk:'Дата', pl:'Data', en:'Date'}) + '</th><th>E-mail</th><th>' + tx({uk:'Що', pl:'Co', en:'What'}) + '</th><th>' + tx({uk:'Сума', pl:'Kwota', en:'Amount'}) + '</th><th>' + tx({uk:'Статус', pl:'Status', en:'Status'}) + '</th><th>' + tx({uk:'Ключ', pl:'Klucz', en:'Key'}) + '</th></tr>' +
      (orders.slice(0, 50).map(function (o) { return '<tr><td>' + fmtDate(o.created_at) + '</td><td>' + esc(o.email || '') + '</td><td>' + esc(o.bundle ? tx({uk:'Пакет', pl:'Pakiet', en:'Bundle'}) : cname(o.course_id)) + '</td><td>' + ((+o.amount || 0) / 100).toFixed(2) + ' zł</td><td>' + (o.status === 'paid' ? '✅' : '⏳') + '</td><td><code>' + esc(o.key_code || '') + '</code></td></tr>'; }).join('') || '<tr><td colspan="6" class="muted">' + tx({uk:'Ще немає замовлень', pl:'Brak zamówień', en:'No orders yet'}) + '</td></tr>') + '</table></div></div>';
  });
}

function route() {
  var h = location.hash.replace(/^#\/?/, ''), parts = h.split('/'), p;
  var nav = ROUTE_LAST !== h; ROUTE_LAST = h;
  if (nav && parts[0] !== 'course' && parts[0] !== 'lesson') setAmbient(null);
  if (nav) { $app.classList.remove('pg-in'); $app.classList.add('pg-leave'); window.scrollTo(0, 0); }
  switch (parts[0]) {
    case '': p = viewHome(); break;
    case 'catalog': p = viewCatalog(); break;
    case 'pricing': p = viewPricing(); break;
    case 'buy': p = viewBuy(); break;
    case 'trial': p = viewTrial(); break;
    case 'login': p = viewAuth('login'); break;
    case 'register': p = viewAuth('register'); break;
    case 'cabinet': p = viewCabinet(); break;
    case 'achievements': p = viewAchievements(); break;
    case 'course': p = viewCourse(parts[1]); break;
    case 'lesson': p = viewLesson(parts[1]); break;
    case 'guide': p = viewGuide(parts[1], parts[2]); break;
    case 'words': p = viewWords(); break;
    case 'admin': p = viewAdmin(); break;
    case 'test': p = viewTest(); break;
    case 'review': p = viewReview(); break;
    case 'paid': p = viewPaid(parts[1]); break;
    default: $app.innerHTML = t('<div class="page"><div class="empty">Сторінку не знайдено. <a href="#/">На головну</a></div></div>'); p = Promise.resolve();
  }
  Promise.resolve(p).catch(function (e) { $app.innerHTML = t('<div class="page"><div class="empty">Помилка: ') + esc(e.message) + '</div></div>'; })
    .then(function () { if (!nav) return; $app.classList.remove('pg-leave'); void $app.offsetWidth; $app.classList.add('pg-in'); });
}
var ROUTE_LAST = null;
window.addEventListener('hashchange', route);
$app.innerHTML = t('<div class="page"><p class="muted">Завантаження…</p></div>');
applyStatic();
if (/[?&]preview=1/.test(location.search)) document.documentElement.classList.add('is-preview');
Promise.all([API.getUser().catch(function () { return null; }), API.getSettings().catch(function () { return DEFAULT_SETTINGS; })]).then(function (r) {
  USER = r[0]; SETTINGS = r[1]; applyCustomTheme();
  var h = location.hash;
  if (/access_token=|type=signup|#\/confirmed/.test(h)) { history.replaceState(null, '', location.pathname + (USER ? '#/cabinet' : '#/login')); toast(USER ? t('Пошту підтверджено! Ласкаво просимо до MoviLang.') : t('Пошту підтверджено! Тепер увійди.')); }
  else if (/error_description=/.test(h)) { history.replaceState(null, '', location.pathname + '#/login'); toast(t('Посилання недійсне або застаріле. Увійди або зареєструйся ще раз.'), 'err'); }
  renderNav(); route();
  if (!LANG_SET) langModal(true);
  setTimeout(function () { API.prefetch(); }, 300);
  setTimeout(processPendingWritings, 4000); setTimeout(loadTtsSet, 1500); setInterval(processPendingWritings, 5 * 60 * 1000);
});
})();
