import sys; sys.path.insert(0, '/home/claude/work/std'); from lib import *
g = 'uk'; L = Lesson('6fdf9198-684b-4386-b271-d4ca51308294', g)
SC = 'Встав слово, обери правду, зрозумій героя|Wstaw słowo, oceń prawdę, zrozum bohatera|Fill the gap, judge true/false, read the hero'
L.ref(0).intro('ТВОЯ РОЛЬ|TWOJA ROLA|YOUR ROLE', 'Ніч. Ти їдеш у причепі Мака разом із Маккуїном до Каліфорнії. Тут кубки, фото й наліпки. Маккуїн усе тобі показує, а Мак за кермом дуже хоче спати.|Noc. Jedziesz w przyczepie Macka z Zygzakiem do Kalifornii. Są tu puchary, zdjęcia i naklejki. Zygzak wszystko ci pokazuje, a Mack za kierownicą bardzo chce spać.|Night. You ride in Mack\'s trailer with McQueen to California. There are cups, photos and stickers. McQueen shows you everything, and Mack at the wheel badly wants to sleep.')
L.ref(1).match('СЦЕНА 1 · СЛОВА|SCENA 1 · SŁOWA|SCENE 1 · WORDS', ['наліпка=наліпка/naklejka/sticker', 'телевізор=телевізор/telewizor/TV', 'стіна=стіна/ściana/wall', 'картинка=картинка/obrazek/picture', 'новий=новий/nowy/new'])
L.set('СЦЕНА 1 · У ПРИЧЕПІ|SCENA 1 · W PRZYCZEPIE|SCENE 1 · IN THE TRAILER', 'Маккуїн показує тобі свої речі.|Zygzak pokazuje ci swoje rzeczy.|McQueen shows you his things.', SC, [
 gap('____ мій кубок.', 'To mój puchar.|This is my cup.', ['Це', 'Ті', 'Ці'], 0, '«Це» — this is.|„Це” = to (jest).|“Це” = this is.'),
 gap('____ кубок старий.', 'Tamten puchar jest stary.|That cup is old.', ['Той', 'Та', 'Ті'], 0, 'Кубок — він: той.|Кубок — męski: той.|Masculine: той.'),
 gap('Подивись на ті ____!', 'Popatrz na tamte naklejki!|Look at those stickers!', ['наліпки', 'стіна', 'ніч'], 0, 'Наліпки = stickers.|Naklejki.|Stickers.'),
 gap('Увімкни ____!', 'Włącz telewizor!|Turn on the TV!', ['телевізор', 'стіну', 'каву'], 0, 'Телевізор = TV.|Telewizor.|TV.'),
 gap('Моє фото на ____.', 'Moje zdjęcie jest na ścianie.|My photo is on the wall.', ['стіні', 'дорозі', 'каві'], 0, 'На стіні = on the wall.|Na ścianie.|On the wall.'),
 tf(g, 'У причепі багато наліпок.', 'W przyczepie jest dużo naklejek.|There are many stickers in the trailer.', True, 'Так, Маккуїн їх любить.|Tak, Zygzak je kocha.|Yes, McQueen loves them.'),
 mc('Маккуїн показує все й каже «мій, мій, мій». Який він?', ['Гордий', 'Сонний', 'Наляканий'], 0, 'Він дуже гордий.|Jest bardzo dumny.|He is very proud.', 'McQueen shows everything: “mine, mine, mine”. What is he like?|Zygzak pokazuje wszystko: „moje, moje, moje”. Jaki jest?|McQueen shows everything: “mine, mine, mine”. What is he like?'),
])
L.ref(2).match('СЦЕНА 2 · СЛОВА|SCENA 2 · SŁOWA|SCENE 2 · WORDS', ['ніч=ніч/noc/night', 'сонний=сонний/senny/sleepy', 'дорога=дорога/droga/road', 'темний=темний/ciemny/dark', 'кава=кава/kawa/coffee'])
L.set('СЦЕНА 2 · ДОВГА НІЧ|SCENA 2 · DŁUGA NOC|SCENE 2 · THE LONG NIGHT', 'Мак позіхає. Маккуїн хоче їхати всю ніч.|Mack ziewa. Zygzak chce jechać całą noc.|Mack yawns. McQueen wants to drive all night.', SC, [
 gap('Уже пізня ____.', 'Już późna noc.|It\'s late at night.', ['ніч', 'кава', 'стіна'], 0, 'Ніч = night.|Noc.|Night.'),
 gap('Я такий ____.', 'Jestem taki śpiący.|I\'m so sleepy.', ['сонний', 'новий', 'темний'], 0, 'Сонний = sleepy.|Senny.|Sleepy.'),
 gap('____ довга.', 'Droga jest długa.|The road is long.', ['Дорога', 'Наліпка', 'Ніч'], 0, 'Дорога = road.|Droga.|Road.'),
 gap('Мені потрібна ____.', 'Potrzebuję kawy.|I need coffee.', ['кава', 'стіна', 'дорога'], 0, 'Кава = coffee.|Kawa.|Coffee.'),
 gap('Їдемо ____ ніч!', 'Jedziemy całą noc!|We drive all night!', ['всю', 'нову', 'темну'], 0, 'Всю ніч = all night.|Całą noc.|All night.'),
 tf(g, 'Мак хоче поспати, але Маккуїн каже «ні».', 'Mack chce się zdrzemnąć, ale Zygzak mówi „nie”.|Mack wants to nap but McQueen says “no”.', True, 'Маккуїн хоче бути першим у Каліфорнії.|Zygzak chce być pierwszy w Kalifornii.|McQueen wants to be first in California.'),
 mc('Мак: «Можна мені поспати, малий?» Що ти робиш?', ['Даю Макові каву й прошу Маккуїна про паузу', 'Вимикаю світло', 'Співаю гучно'], 0, 'Ти дбаєш про Мака.|Dbasz o Macka.|You care about Mack.', 'Mack: “Can I sleep, kid?” What do you do?|Mack: „Mogę się zdrzemnąć, mały?” Co robisz?|Mack: “Can I sleep, kid?” What do you do?', 'you'),
])
L.ref(3).match('СЦЕНА 3 · СЛОВА|SCENA 3 · SŁOWA|SCENE 3 · WORDS', ['шосе=шосе/autostrada/highway', 'місто=місто/miasto/city', 'знак=знак/znak/sign', 'вікно=вікно/okno/window', 'музика=музика/muzyka/music'])
L.set('СЦЕНА 3 · ШОСЕ|SCENA 3 · AUTOSTRADA|SCENE 3 · THE HIGHWAY', 'Ти дивишся у вікно причепа на нічне шосе.|Patrzysz przez okno przyczepy na nocną autostradę.|You look out of the trailer window at the night highway.', SC, [
 gap('Подивись у ____!', 'Popatrz przez okno!|Look out of the window!', ['вікно', 'місто', 'знак'], 0, 'Вікно = window.|Okno.|Window.'),
 gap('Подивись на той ____!', 'Popatrz na tamten znak!|Look at that sign!', ['знак', 'кава', 'ніч'], 0, 'Знак = sign.|Znak.|Sign.'),
 gap('Те ____ велике.', 'Tamto miasto jest duże.|That city is big.', ['місто', 'шосе', 'вікно'], 0, 'Місто — воно: те.|Місто — nijaki: те.|Neuter: те.'),
 gap('Мені подобається ця ____.', 'Lubię tę muzykę.|I like this music.', ['музика', 'дорога', 'наліпка'], 0, 'Музика = music.|Muzyka.|Music.'),
 gap('Повертай ____!', 'Skręcaj w prawo!|Turn right!', ['праворуч', 'вікно', 'чотири'], 0, 'Праворуч = right.|W prawo.|Right.'),
 tf(g, 'На шосе зовсім немає машин.', 'Na autostradzie nie ma żadnych aut.|There are no cars on the highway.', False, 'Шосе завантажене.|Autostrada jest zatłoczona.|The highway is busy.'),
 mc('Знак: «Каліфорнія — 1000 миль». Що це значить?', ['Ще дуже далеко', 'Ми вже тут', 'Треба ліворуч'], 0, 'Тисяча миль — далеко.|Tysiąc mil — daleko.|A thousand miles — far.', 'Sign: “California — 1000 miles”. What does it mean?|Znak: „Kalifornia — 1000 mil”. Co to znaczy?|Sign: “California — 1000 miles”. What does it mean?'),
])
L.intro('ПРАВИЛО|ZASADA|RULE', 'Цей / ця / це / ці — поруч (this/these): цей кубок, ця наліпка, це фото, ці картинки. Той / та / те / ті — далеко (that/those): той знак, та дорога, те місто, ті вогні. «Це мій кубок» = this is my cup.|Цей/ця/це/ці — blisko (ten/ta/to/ci): цей кубок, ця наліпка, це фото, ці картинки. Той/та/те/ті — daleko (tamten): той знак, та дорога, те місто, ті вогні. „Це мій кубок” = to mój puchar.|Цей/ця/це/ці = this/these (near): цей кубок, ця наліпка, це фото, ці картинки. Той/та/те/ті = that/those (far): той знак, та дорога, те місто, ті вогні.')
gm = lambda q, o, a, e: mc(q, o, a, e, tag='gram')
L.set('ГРАМАТИКА · ЦЕЙ ЧИ ТОЙ?|GRAMATYKA · TEN CZY TAMTEN?|GRAMMAR · THIS OR THAT?', 'Маккуїн показує речі в причепі й за вікном.|Zygzak pokazuje rzeczy w przyczepie i za oknem.|McQueen points at things in the trailer and outside.', 'Цей / ця / це / ці · той / та / те / ті|Цей / той|Цей / той', [
 gm('«____ кубок новий» (поруч).', ['Цей', 'Ця', 'Ці'], 0, 'Кубок — він.|Męski.|Masculine.'),
 gm('«____ наліпка червона» (поруч).', ['Цей', 'Ця', 'Це'], 1, 'Наліпка — вона.|Żeński.|Feminine.'),
 gm('«____ фото моє» (поруч).', ['Цей', 'Ця', 'Це'], 2, 'Фото — воно.|Nijaki.|Neuter.'),
 gm('«____ картинки гарні» (поруч).', ['Ці', 'Цей', 'Ця'], 0, 'Множина.|L. mnoga.|Plural.'),
 gm('«____ знак далеко» (там).', ['Той', 'Та', 'Те'], 0, 'Знак — він.|Męski.|Masculine.'),
 gm('«____ дорога довга» (там).', ['Той', 'Та', 'Ті'], 1, 'Дорога — вона.|Żeński.|Feminine.'),
 gm('«____ місто велике» (там).', ['Той', 'Та', 'Те'], 2, 'Місто — воно.|Nijaki.|Neuter.'),
 gm('«Подивись на ____ вогні!» (там).', ['ті', 'той', 'та'], 0, 'Множина.|L. mnoga.|Plural.'),
 gm('«____ телевізор старий» (поруч).', ['Цей', 'Ця', 'Ці'], 0, 'Телевізор — він.|Męski.|Masculine.'),
 gm('«____ кава гаряча» (поруч).', ['Цей', 'Ця', 'Це'], 1, 'Кава — вона.|Żeński.|Feminine.'),
 gm('«____ шосе завантажене» (там).', ['Той', 'Та', 'Те'], 2, 'Шосе — воно.|Nijaki.|Neuter.'),
 gm('«Я люблю ____ наліпки!» (поруч).', ['ці', 'цей', 'ця'], 0, 'Множина.|L. mnoga.|Plural.'),
])
L.reading('Щоденник механіка: ніч у причепі|Dziennik mechanika: noc w przyczepie|Mechanic\'s diary: a night in the trailer', 'ЧИТАННЯ|CZYTANIE|READING', 'Прочитай свій запис і обери правильні слова.|Przeczytaj swój wpis po ukraińsku i wybierz słowa.|Read your diary entry in Ukrainian and choose the words.', [
 S('Зараз ніч. Ми їдемо до Каліфорнії.'),
 S('Я в причепі Мака разом із Маккуїном.', ), S('Тут дуже гарно.', ),
 S('На ____ багато фото.', ['стіні', 'каві', 'ночі'], 0),
 S('Маккуїн каже: «____ мій кубок!»', ['Це', 'Ці', 'Ті'], 0),
 S('Потім він показує на полицю: «____ кубки старі».', ['Ті', 'Той', 'Та'], 0),
 S('Він дуже любить свої ____.', ['наліпки', 'дороги', 'кави'], 0),
 S('Мак за кермом. Він ____.', ['сонний', 'новий', 'гучний'], 0),
 S('Мак питає: «Можна мені ____?»', ['поспати', 'кава', 'вікно'], 0),
 S('Маккуїн каже: «Ні! Їдемо ____ ніч!»', ['всю', 'ці', 'той'], 0),
 S('Я дивлюся у ____.', ['вікно', 'стіну', 'телевізор'], 0),
 S('Надворі ____: тільки вогні міста.', ['темно', 'порожньо', 'смішно'], 0),
 S('Я бачу великий ____: «Каліфорнія».', ['знак', 'кубок', 'крем'], 0),
 S('Дорога дуже ____.', ['довга', 'нова', 'іржава'], 0),
 S('Я даю Макові ____.', ['каву', 'стіну', 'шосе'], 0),
 S('Але я теж хочу спати… Ця ніч дуже довга.'),
], 'Цей — поруч, той — далеко.|Цей — blisko, той — daleko.|Цей near, той far.')
L.set('РОЗУМІННЯ ТЕКСТУ|ROZUMIENIE TEKSTU|READING CHECK', 'Питання до твого щоденника.|Pytania do twojego dziennika.|Questions about your diary.', 'П\'ять питань до тексту|Pięć pytań do tekstu|Five questions', [
 mc('Куди ви їдете?', ['До Каліфорнії', 'Додому', 'На стадіон'], 0, 'До Каліфорнії.|Do Kalifornii.|To California.', 'Where are you going?|Dokąd jedziecie?|Where are you going?'),
 mc('Що на стіні?', ['Фото', 'Крем', 'Шини'], 0, 'Багато фото.|Dużo zdjęć.|Many photos.', 'What is on the wall?|Co jest na ścianie?|What is on the wall?'),
 mc('Чого хоче Мак?', ['Поспати', 'Співати', 'Гонку'], 0, 'Він сонний.|Jest śpiący.|He is sleepy.', 'What does Mack want?|Czego chce Mack?|What does Mack want?'),
 mc('Що каже Маккуїн?', ['Їдемо всю ніч!', 'Спимо!', 'Повертаймо додому!'], 0, 'Він не хоче чекати.|Nie chce czekać.|He won\'t wait.', 'What does McQueen say?|Co mówi Zygzak?|What does McQueen say?'),
 mc('Що ти даєш Макові?', ['Каву', 'Наліпку', 'Кубок'], 0, 'Каву.|Kawę.|Coffee.', 'What do you give Mack?|Co dajesz Mackowi?|What do you give Mack?'),
])
L.quest('КВЕСТ: НІЧНА ДОРОГА|QUEST: NOCNA DROGA|QUEST: NIGHT ROAD', 'Мак засинає за кермом. Ти — єдиний, хто це бачить.|Mack zasypia za kierownicą. Tylko ty to widzisz.|Mack is falling asleep at the wheel. Only you see it.', 'train', {
 's1': step('Мак: «Я такий сонний…»', 'Jestem taki śpiący…|I\'m so sleepy…', 'Друга ночі.|Druga w nocy.|2 a.m.', [ch('Маку, ось кава!', True, 's2', 'Добре!|Dobrze!|Good!'), ch('Ця кави тут.', False, 's2', 'Треба «Ось кава».|Trzeba „Ось кава”.|Say “Ось кава”.')]),
 's2': step('Маккуїн: «Хто це говорить?»', 'Kto to mówi?|Who is talking?', 'Маккуїн прокидається.|Zygzak się budzi.|McQueen wakes up.', [ch('Це я, твій механік.', True, 's3', 'Так!|Tak!|Yes!'), ch('Ці я механік.', False, 'end_bad', 'Неправильно.|Źle.|Wrong.')]),
 's3': step('Маккуїн: «Ми не зупиняємося!»', 'Nie zatrzymujemy się!|We don\'t stop!', 'Мак ледь бачить дорогу.|Mack ledwo widzi drogę.|Mack can barely see the road.', [ch('Подивись на той знак — там кафе. Зупинімося!', True, 'end_good', 'Розумно.|Mądrze.|Smart.'), ch('Гаразд, їдемо всю ніч.', True, 'end_mid', 'Небезпечно…|Niebezpiecznie…|Dangerous…')]),
}, {'end_good': end(True, 'Кінцівка: Перерва|Zakończenie: Przerwa|Ending: A Break', 'Мак п\'є каву на зупинці. Він знову бадьорий. Сьогодні ніхто не загубився.|Mack pije kawę na postoju. Znów jest rześki. Dziś nikt się nie zgubił.|Mack drinks coffee at the stop. He\'s awake again. Nobody gets lost tonight.'),
    'end_mid': end(True, 'Кінцівка: Як у фільмі|Zakończenie: Jak w filmie|Ending: Like the film', 'Мак засинає… Двері причепа відчиняються. Що буде далі — у наступному уроці!|Mack zasypia… Drzwi przyczepy się otwierają. Co dalej — w następnej lekcji!|Mack falls asleep… The trailer door opens. What happens next — in the next lesson!'),
    'end_bad': end(False, 'Кінцівка: Тебе не почули|Zakończenie: Nie usłyszeli cię|Ending: Not heard', 'Ніхто тебе не зрозумів. Спробуй: «Це я, твій механік».|Nikt cię nie zrozumiał. Spróbuj: „Це я, твій механік”.|Nobody understood. Try: “Це я, твій механік”.')})
L.set('ПИШИ Й СКЛАДАЙ|PISZ I UKŁADAJ|WRITE AND BUILD', 'Записуй репліки цієї ночі.|Zapisuj kwestie tej nocy.|Write down the lines of this night.', 'Впиши й склади|Wpisz i ułóż|Type and build', [
 typ(g, 'Це мій кубок.', 'To mój puchar.|This is my cup.'), order(g, ['Той', 'кубок', 'старий.'], 'Tamten puchar jest stary.|That cup is old.'),
 typ(g, 'Я такий сонний.', 'Jestem taki śpiący.|I\'m so sleepy.'), order(g, ['Мені', 'потрібна', 'кава.'], 'Potrzebuję kawy.|I need coffee.'),
 typ(g, 'Дорога довга.', 'Droga jest długa.|The road is long.'), order(g, ['Подивись', 'на', 'той', 'знак!'], 'Popatrz na tamten znak!|Look at that sign!'),
 typ(g, 'Увімкни телевізор!', 'Włącz telewizor!|Turn on the TV!'), order(g, ['Мені', 'подобається', 'ця', 'музика.'], 'Lubię tę muzykę.|I like this music.'),
])
L.speak('Це мій кубок. А ті кубки старі.', 'To mój puchar. A tamte puchary są stare.|This is my cup. And those cups are old.')
L.speak('Маку, ось кава. Дорога довга!', 'Mack, oto kawa. Droga jest długa!|Mack, here\'s coffee. The road is long!')
L.set('ДОРОГА · СЛОВА|DROGA · SŁOWA|THE ROAD · WORDS', 'Слова уроку в нових ситуаціях.|Słowa lekcji w nowych sytuacjach.|Lesson words in new situations.', 'Вісім питань на слова|Osiem pytań|Eight word questions', [
 mc('Удень світло, уночі ____.', ['темно', 'гучно', 'ново'], 0, 'Темно = dark.|Ciemno.|Dark.', tag='word'),
 mc('Велика дорога між містами — це ____.', ['шосе', 'стіна', 'кава'], 0, 'Шосе = highway.|Autostrada.|Highway.', tag='word'),
 mc('Маленькі картинки на причепі — це ____.', ['наліпки', 'вікна', 'знаки'], 0, 'Наліпки.|Naklejki.|Stickers.', tag='word'),
 mc('Коли хочеш спати, ти ____.', ['сонний', 'новий', 'гучний'], 0, 'Сонний.|Senny.|Sleepy.', tag='word'),
 mc('Лос-Анджелес — велике ____.', ['місто', 'вікно', 'світло'], 0, 'Місто.|Miasto.|City.', tag='word'),
 mc('Мак п\'є ____, щоб не спати.', ['каву', 'музику', 'стіну'], 0, 'Каву.|Kawę.|Coffee.', tag='word'),
 mc('«Каліфорнія — 10 миль» — це ____.', ['знак', 'телевізор', 'кубок'], 0, 'Знак.|Znak.|Sign.', tag='word'),
 mc('Протилежне до «праворуч» — ____.', ['ліворуч', 'довго', 'темно'], 0, 'Ліворуч = left.|W lewo.|Left.', tag='word'),
])
L.final('ЗАПИС У БЛОКНОТІ|WPIS W NOTESIE|NOTEBOOK ENTRY', 'Опиши причіп Мака (25+ слів): що там є? що поруч (цей/ця/це), що далеко (той/та/те)? як ви їдете вночі?|Opisz po ukraińsku przyczepę Macka (25+ słów): co w niej jest? co blisko (цей/ця/це), co daleko (той/та/те)? jak jedziecie nocą?|Describe Mack\'s trailer in Ukrainian (25+ words): what is there? what is near (цей), what is far (той)? how do you drive at night?',
 'У причепі є … Цей кубок … Та дорога … Мак …', 25)
print(L.save('cars', 4))
