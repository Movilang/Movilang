import sys; sys.path.insert(0, '/home/claude/work/std'); from lib import *
g = 'uk'; L = Lesson('d4649dc2-6f15-4467-9866-ac827ffa24fb', g)
L.ref(0).intro('ТВОЯ РОЛЬ|TWOJA ROLA|YOUR ROLE', 'Гонка закінчилася. Ти несеш ящик з інструментами до трейлера Маккуїна. Біля трейлера чекають двоє смішних старих братів — спонсори команди. Сьогодні ти дізнаєшся, хто є хто в команді.|Wyścig się skończył. Niesiesz skrzynkę z narzędziami do przyczepy Zygzaka. Przy przyczepie czekają dwaj zabawni starsi bracia — sponsorzy zespołu. Dziś dowiesz się, kto jest kim w zespole.|The race is over. You carry the toolbox to McQueen\'s trailer. Two funny old brothers — the team sponsors — are waiting there. Today you learn who is who in the team.')
L.ref(1).match('СЦЕНА 1 · СЛОВА|SCENA 1 · SŁOWA|SCENE 1 · WORDS', ['спонсор=спонсор/sponsor/sponsor', 'брат=брат/brat/brother', 'смішний=смішний/zabawny/funny', 'іржавий=іржавий/zardzewiały/rusty', 'крем=крем/krem/cream'])
L.set('СЦЕНА 1 · СПОНСОРИ|SCENA 1 · SPONSORZY|SCENE 1 · THE SPONSORS', 'Брати з Rust-eze вітають Маккуїна. Він червоніє.|Bracia z Rust-eze witają Zygzaka. On się czerwieni.|The Rust-eze brothers greet McQueen. He blushes.',
 'Встав слово, обери правду, зрозумій героя|Wstaw słowo, oceń prawdę, zrozum bohatera|Fill the gap, judge true/false, read the hero', [
 gap('Ми твої ____!', 'My jesteśmy twoimi sponsorami!|We are your sponsors!', ['спонсори', 'брати', 'фанати'], 0, 'Спонсор = sponsor.|Спонсор = sponsor.|Спонсор = sponsor.'),
 gap('Це мій ____.', 'To mój brat.|This is my brother.', ['крем', 'брат', 'бампер'], 1, 'Брат = brother.|Брат = brat.|Брат = brother.'),
 gap('Спробуй наш ____!', 'Spróbuj naszego kremu!|Try our cream!', ['крем', 'кубок', 'номер'], 0, 'Крем = cream.|Крем = krem.|Крем = cream.'),
 gap('Мій бампер ____.', 'Mój zderzak jest zardzewiały.|My bumper is rusty.', ['швидкий', 'іржавий', 'червоний'], 1, 'Іржавий = rusty.|Іржавий = zardzewiały.|Іржавий = rusty.'),
 tf(g, 'Спонсори Маккуїна — молоді й багаті.', 'Sponsorzy Zygzaka są młodzi i bogaci.|McQueen\'s sponsors are young and rich.', False, 'Вони старі й смішні.|Są starzy i zabawni.|They are old and funny.'),
 tf(g, 'Компанія Rust-eze продає крем для іржавих машин.', 'Firma Rust-eze sprzedaje krem do zardzewiałych aut.|Rust-eze sells a cream for rusty cars.', True, 'Так, це їхній крем.|Tak, to ich krem.|Yes, that is their cream.'),
 mc('Маккуїн каже братам: «Так-так, дякую…» і швидко їде. Як він почувається?', ['Щасливий', 'Збентежений', 'Сонний'], 1, 'Йому соромно за маленького спонсора.|Wstydzi się małego sponsora.|He is embarrassed by the small sponsor.', 'McQueen says “Yes, yes, thanks…” and drives off fast. How does he feel?|Zygzak mówi „Tak, tak, dzięki…” i szybko odjeżdża. Jak się czuje?|McQueen says “Yes, yes, thanks…” and drives off fast. How does he feel?'),
])
L.ref(2).match('СЦЕНА 2 · СЛОВА|SCENA 2 · SŁOWA|SCENE 2 · WORDS', ['мрія=мрія/marzenie/dream', 'багатий=багатий/bogaty/rich', 'гелікоптер=гелікоптер/helikopter/helicopter', 'бос=бос/szef/boss', 'логотип=логотип/logo/logo'])
L.set('СЦЕНА 2 · МРІЯ ПРО DINOCO|SCENA 2 · MARZENIE O DINOCO|SCENE 2 · THE DINOCO DREAM', 'Над стадіоном летить синій гелікоптер Dinoco. Маккуїн мріє.|Nad stadionem leci niebieski helikopter Dinoco. Zygzak marzy.|A blue Dinoco helicopter flies over the stadium. McQueen dreams.',
 'Встав слово, обери правду, зрозумій героя|Wstaw słowo, oceń prawdę, zrozum bohatera|Fill the gap, judge true/false, read the hero', [
 gap('Це моя ____!', 'To moje marzenie!|This is my dream!', ['мрія', 'робота', 'дружина'], 0, 'Мрія = dream.|Мрія = marzenie.|Мрія = dream.'),
 gap('Подивись на їхній ____!', 'Popatrz na ich helikopter!|Look at their helicopter!', ['гелікоптер', 'крем', 'причіп'], 0, 'Гелікоптер = helicopter.|Гелікоптер = helikopter.|Гелікоптер = helicopter.'),
 gap('Вони ____!', 'Oni są bogaci!|They are rich!', ['іржаві', 'багаті', 'порожні'], 1, 'Багатий = rich.|Багатий = bogaty.|Багатий = rich.'),
 gap('Подивись на мій ____!', 'Popatrz na moje logo!|Look at my logo!', ['логотип', 'брат', 'шум'], 0, 'Логотип = logo.|Логотип = logo.|Логотип = logo.'),
 tf(g, 'Dinoco — спонсор Короля.', 'Dinoco to sponsor Króla.|Dinoco is The King\'s sponsor.', True, 'Так, синій Dinoco — команда Короля.|Tak, niebieskie Dinoco to zespół Króla.|Yes, blue Dinoco is The King\'s team.'),
 mc('Король каже Маккуїну: «Тобі потрібна хороша команда, малий». Що він радить?', ['Купити гелікоптер', 'Мати друзів і команду', 'Їхати швидше'], 1, 'Король — мудрий.|Król jest mądry.|The King is wise.', 'The King: “You need a good team, kid.” What is his advice?|Król: „Potrzebujesz dobrego zespołu, mały”. Co radzi?|The King: “You need a good team, kid.” What is his advice?'),
 mc('Ти бачиш синій логотип Dinoco. Що ти кажеш Маккуїну?', ['«Колись це буде твоє місце!»', '«Це іржаве»', '«Я сонний»'], 0, 'Місце = place.|Місце = miejsce.|Місце = place.', 'You see the blue Dinoco logo. What do you say to McQueen?|Widzisz niebieskie logo Dinoco. Co mówisz Zygzakowi?|You see the blue Dinoco logo. What do you say to McQueen?', 'you'),
])
L.ref(3).match('СЦЕНА 3 · СЛОВА|SCENA 3 · SŁOWA|SCENE 3 · WORDS', ['вантажівка=вантажівка/ciężarówka/truck', 'причіп=причіп/przyczepa/trailer', 'найкращий=найкращий/najlepszy/best', 'вірний=вірний/lojalny/loyal', 'робота=робота/praca/job'])
L.set('СЦЕНА 3 · МАК|SCENA 3 · MACK|SCENE 3 · MACK', 'Мак, велика червона вантажівка, чекає. Бригада Маккуїна йде з команди.|Mack, wielka czerwona ciężarówka, czeka. Ekipa Zygzaka odchodzi z zespołu.|Mack, a big red truck, is waiting. McQueen\'s crew is quitting.',
 'Встав слово, обери правду, зрозумій героя|Wstaw słowo, oceń prawdę, zrozum bohatera|Fill the gap, judge true/false, read the hero', [
 gap('Я ____, малий.', 'Jestem ciężarówką, mały.|I\'m a truck, kid.', ['вантажівка', 'гелікоптер', 'логотип'], 0, 'Вантажівка = truck.|Вантажівка = ciężarówka.|Вантажівка = truck.'),
 gap('Сідай у ____!', 'Wsiadaj do przyczepy!|Get in the trailer!', ['причіп', 'крем', 'місто'], 0, 'Причіп = trailer.|Причіп = przyczepa.|Причіп = trailer.'),
 gap('Ти мій ____ друг.', 'Jesteś moim najlepszym przyjacielem.|You\'re my best friend.', ['іржавий', 'найкращий', 'порожній'], 1, 'Найкращий = best.|Найкращий = najlepszy.|Найкращий = best.'),
 gap('Я ____, малий.', 'Jestem lojalny, mały.|I\'m loyal, kid.', ['вірний', 'смішний', 'багатий'], 0, 'Вірний = loyal.|Вірний = lojalny.|Вірний = loyal.'),
 gap('Це моя ____.', 'To moja praca.|This is my job.', ['робота', 'мрія', 'бригада'], 0, 'Робота = job.|Робота = praca.|Робота = job.'),
 tf(g, 'Бригада механіків іде від Маккуїна.', 'Ekipa mechaników odchodzi od Zygzaka.|The pit crew leaves McQueen.', True, 'Він грубий з командою.|Jest niegrzeczny dla zespołu.|He is rude to the team.'),
 mc('Маккуїн питає: «Де моя бригада?» Ти стоїш поруч. Що ти кажеш?', ['«Я тут. Я твоя бригада.»', '«Тут порожньо.»', '«Я гелікоптер.»'], 0, 'Ти лишаєшся — ти вірний.|Zostajesz — jesteś lojalny.|You stay — you are loyal.', '“Where is my crew?” What do you say?|„Gdzie jest moja ekipa?” Co mówisz?|“Where is my crew?” What do you say?', 'you'),
])
L.intro('ПРАВИЛО|ZASADA|RULE', 'Мій / моя / моє / мої — за родом слова: мій брат, мій причіп; моя мрія, моя робота; моє місце, моє ім\'я; мої спонсори. Так само: твій / твоя / твоє / твої, наш / наша / наше / наші.|Мій / моя / моє / мої — według rodzaju: мій брат (mój brat), моя мрія (moje marzenie), моє місце (moje miejsce), мої спонсори (moi sponsorzy). Tak samo: твій/твоя/твоє/твої, наш/наша/наше/наші.|Мій / моя / моє / мої (my) follow the noun\'s gender: мій брат, моя мрія, моє місце, мої спонсори. Same for твій (your) and наш (our).')
G = 'Граматика: мій / моя / моє|Gramatyka: мій / моя / моє|Grammar: мій / моя / моє'
L.set('ГРАМАТИКА · ЧИЄ ЦЕ?|GRAMATYKA · CZYJE TO?|GRAMMAR · WHOSE IS IT?', 'Хто що має в команді Маккуїна? Обери правильну форму.|Kto co ma w zespole Zygzaka? Wybierz formę.|Who has what in McQueen\'s team? Choose the form.', 'Мій / моя / моє / мої|Мій / моя / моє / мої|Мій / моя / моє / мої', [
 mc('Маккуїн: «Це ____ мрія!»', ['мій', 'моя', 'моє'], 1, 'Мрія — вона: моя.|Мрія — rodzaj żeński: моя.|Мрія is feminine: моя.', tag='gram'),
 mc('Брат: «Це ____ брат.»', ['мій', 'моя', 'мої'], 0, 'Брат — він: мій.|Брат — męski: мій.|Брат is masculine: мій.', tag='gram'),
 mc('Маккуїн: «Тепер це ____ місце.»', ['мій', 'моя', 'моє'], 2, 'Місце — воно: моє.|Місце — nijaki: моє.|Місце is neuter: моє.', tag='gram'),
 mc('Брати: «Ми ____ спонсори!»', ['твій', 'твоя', 'твої'], 2, 'Спонсори — множина: твої.|Liczba mnoga: твої.|Plural: твої.', tag='gram'),
 mc('Мак: «Це ____ робота.»', ['мій', 'моя', 'моє'], 1, 'Робота — вона: моя.|Робота — żeński: моя.|Робота is feminine: моя.', tag='gram'),
 mc('Маккуїн: «Де ____ бригада?»', ['мій', 'моя', 'мої'], 1, 'Бригада — вона.|Бригада — żeński.|Бригада is feminine.', tag='gram'),
 mc('Мак: «____ причіп великий.»', ['Мій', 'Моя', 'Моє'], 0, 'Причіп — він.|Причіп — męski.|Причіп is masculine.', tag='gram'),
 mc('Брати: «Спробуй ____ крем!»', ['наш', 'наша', 'наше'], 0, 'Крем — він: наш.|Крем — męski: наш.|Крем is masculine: наш.', tag='gram'),
 mc('Брати: «____ компанія маленька.»', ['Наш', 'Наша', 'Наші'], 1, 'Компанія — вона.|Компанія — żeński.|Компанія is feminine.', tag='gram'),
 mc('Ти: «Мак — ____ друг!»', ['мій', 'моя', 'моє'], 0, 'Друг — він.|Друг — męski.|Друг is masculine.', tag='gram'),
 mc('Маккуїн: «Подивись на ____ логотип!»', ['мій', 'моя', 'мої'], 0, 'Логотип — він.|Логотип — męski.|Логотип is masculine.', tag='gram'),
 mc('Король: «Це ____ дружина.»', ['мій', 'моя', 'моє'], 1, 'Дружина — вона.|Дружина — żeński.|Дружина is feminine.', tag='gram'),
])
gp = lambda q, o, a: S(q, o, a)
L.reading('«Вісник боксу»: хто в команді Маккуїна?|„Wieści z boksu”: kto jest w zespole Zygzaka?|“Pit News”: who is on McQueen\'s team?', 'ЧИТАННЯ|CZYTANIE|READING', 'Прочитай статтю й обери правильні слова.|Przeczytaj artykuł po ukraińsku i wybierz właściwe słowa.|Read the article in Ukrainian and choose the right words.', [
 S('Після гонки Маккуїн їде до свого трейлера.'),
 gp('Там на нього чекають два старі ____.', ['брати', 'гелікоптери', 'логотипи'], 0),
 gp('Їхня компанія називається Rust-eze. Вона ____.', ['багата', 'маленька', 'синя'], 1),
 gp('Брати продають ____ для іржавих машин.', ['кубок', 'причіп', 'крем'], 2),
 S('Вони кажуть: «Ми твої спонсори!»'),
 gp('Маккуїн ____: йому соромно.', ['збентежений', 'сонний', 'вірний'], 0),
 S('Він дивиться на небо.'),
 gp('Там летить синій ____ Dinoco.', ['причіп', 'гелікоптер', 'бампер'], 1),
 gp('Dinoco — велика й ____ компанія.', ['іржава', 'порожня', 'багата'], 2),
 gp('Це ____ мрія Маккуїна.', ['моя', 'велика', 'тиха'], 1),
 S('Але бригада механіків іде з команди.'),
 gp('Маккуїн питає: «Де моя ____?»', ['бригада', 'дружина', 'мрія'], 0),
 S('Поруч стоїть Мак.'),
 gp('Мак — велика червона ____.', ['вантажівка', 'компанія', 'робота'], 0),
 gp('Він ____ і добрий.', ['вірний', 'іржавий', 'багатий'], 0),
 gp('Мак каже: «Це моя ____, малий».', ['мрія', 'робота', 'бригада'], 1),
 S('А ти? Ти теж лишаєшся. Ти — нова бригада Маккуїна.'),
], 'Мак і ти — справжня команда.|Mack i ty — prawdziwy zespół.|Mack and you are the real team.')
L.set('РОЗУМІННЯ ТЕКСТУ|ROZUMIENIE TEKSTU|READING CHECK', 'Питання до статті «Вісник боксу».|Pytania do artykułu.|Questions about the article.', 'П\'ять питань до тексту|Pięć pytań do tekstu|Five questions about the text', [
 mc('Хто такі брати з Rust-eze?', ['Механіки', 'Спонсори', 'Фанати'], 1, 'Вони спонсори.|Są sponsorami.|They are sponsors.', 'Who are the Rust-eze brothers?|Kim są bracia z Rust-eze?|Who are the Rust-eze brothers?'),
 mc('Що продає Rust-eze?', ['Шини', 'Крем', 'Гелікоптери'], 1, 'Крем для іржавих машин.|Krem do zardzewiałych aut.|A cream for rusty cars.', 'What does Rust-eze sell?|Co sprzedaje Rust-eze?|What does Rust-eze sell?'),
 mc('Про що мріє Маккуїн?', ['Про Dinoco', 'Про сон', 'Про крем'], 0, 'Dinoco — його мрія.|Dinoco to jego marzenie.|Dinoco is his dream.', 'What is McQueen\'s dream?|O czym marzy Zygzak?|What is McQueen\'s dream?'),
 mc('Хто йде з команди?', ['Мак', 'Бригада механіків', 'Брати'], 1, 'Бригада йде.|Ekipa odchodzi.|The crew leaves.', 'Who leaves the team?|Kto odchodzi z zespołu?|Who leaves the team?'),
 mc('Хто лишається з Маккуїном?', ['Мак і ти', 'Король', 'Ніхто'], 0, 'Мак вірний, і ти теж.|Mack jest lojalny, ty też.|Mack is loyal, and so are you.', 'Who stays with McQueen?|Kto zostaje z Zygzakiem?|Who stays with McQueen?'),
])
L.quest('КВЕСТ: НОВА БРИГАДА|QUEST: NOWA EKIPA|QUEST: THE NEW CREW', 'Бригада пішла. Маккуїн сердитий. Допоможи йому — українською.|Ekipa odeszła. Zygzak jest zły. Pomóż mu — po ukraińsku.|The crew has left. McQueen is angry. Help him — in Ukrainian.', 'pitch', {
 's1': step('Маккуїн: «Де моя бригада?»', 'Gdzie moja ekipa?|Where is my crew?', 'Трейлер порожній.|Przyczepa jest pusta.|The trailer is empty.', [ch('Вони пішли. Але я тут!', True, 's2', 'Добре!|Dobrze!|Good!'), ch('Моя бригада є тут є.', False, 's1b', 'Так не кажуть.|Tak się nie mówi.|Not how we say it.')]),
 's1b': step('Маккуїн: «Що? Говори нормально!»', 'Co? Mów normalnie!|What? Speak normally!', 'Він сердиться.|Jest zły.|He is angry.', [ch('Я твій механік.', True, 's2', 'Так!|Tak!|Yes!'), ch('Механік мій я.', False, 'end_bad', 'Неправильно.|Źle.|Wrong.')]),
 's2': step('Маккуїн: «Хто ці смішні брати?»', 'Kim są ci zabawni bracia?|Who are these funny brothers?', 'Брати махають.|Bracia machają.|The brothers wave.', [ch('Це наші спонсори.', True, 's3', 'Наші — множина.|Наші — l. mnoga.|Наші — plural.'), ch('Це наша спонсори.', False, 's3', 'Треба «наші».|Trzeba „наші”.|Use “наші”.')]),
 's3': step('Маккуїн: «Я хочу Dinoco, а не крем!»', 'Chcę Dinoco, nie krem!|I want Dinoco, not cream!', 'Гелікоптер Dinoco летить.|Helikopter Dinoco leci.|The Dinoco helicopter flies.', [ch('Спочатку — твоя команда. Мак вірний!', True, 'end_good', 'Мудро.|Mądrze.|Wise.'), ch('Добре. Їдь до Dinoco сам.', True, 'end_mid', 'Хм…|Hm…|Hm…')]),
}, {'end_good': end(True, 'Кінцівка: Команда|Zakończenie: Zespół|Ending: The Team', 'Маккуїн дивиться на Мака й на тебе. «Гаразд, бригадо. Їдемо в Каліфорнію!»|Zygzak patrzy na Macka i na ciebie. „Dobra, ekipo. Jedziemy do Kalifornii!”|McQueen looks at Mack and at you. “Okay, crew. To California!”'),
    'end_mid': end(True, 'Кінцівка: Сам|Zakończenie: Sam|Ending: Alone', 'Маккуїн їде в трейлер мовчки. Він ще не розуміє, що команда важлива.|Zygzak w milczeniu wjeżdża do przyczepy. Jeszcze nie rozumie, że zespół jest ważny.|McQueen silently drives into the trailer. He doesn\'t yet see that a team matters.'),
    'end_bad': end(False, 'Кінцівка: Не зрозумів|Zakończenie: Nie zrozumiał|Ending: Not understood', 'Маккуїн тебе не зрозумів. Спробуй ще: «Я твій механік».|Zygzak cię nie zrozumiał. Spróbuj: „Я твій механік”.|McQueen didn\'t understand. Try: “Я твій механік”.')})
L.set('ПИШИ Й СКЛАДАЙ|PISZ I UKŁADAJ|WRITE AND BUILD', 'Ти записуєш команду в блокнот механіка.|Zapisujesz zespół w notesie mechanika.|You write the team into your mechanic notebook.', 'Впиши й склади|Wpisz i ułóż|Type and build', [
 typ(g, 'Це мій брат.', 'To mój brat.|This is my brother.'), order(g, ['Ми', 'твої', 'спонсори!'], 'My jesteśmy twoimi sponsorami!|We are your sponsors!'),
 typ(g, 'Це моя мрія.', 'To moje marzenie.|This is my dream.'), order(g, ['Ти', 'мій', 'найкращий', 'друг.'], 'Jesteś moim najlepszym przyjacielem.|You are my best friend.'),
 typ(g, 'Я вірний.', 'Jestem lojalny.|I am loyal.'), order(g, ['Тепер', 'це', 'моє', 'місце.'], 'Teraz to moje miejsce.|Now this is my place.'),
 typ(g, 'Наша компанія маленька.', 'Nasza firma jest mała.|Our company is small.'), order(g, ['Сідай', 'у', 'причіп!'], 'Wsiadaj do przyczepy!|Get in the trailer!'),
])
L.speak('Ми твої спонсори! Спробуй наш крем!', 'Jesteśmy twoimi sponsorami! Spróbuj naszego kremu!|We are your sponsors! Try our cream!')
L.speak('Мак, ти мій найкращий друг. Сідай у причіп!', 'Mack, jesteś moim najlepszym przyjacielem. Wsiadaj!|Mack, you are my best friend. Get in!')
L.set('ПІСЛЯ ГОНКИ · СЛОВА|PO WYŚCIGU · SŁOWA|AFTER THE RACE · WORDS', 'Слова уроку в нових ситуаціях.|Słowa lekcji w nowych sytuacjach.|Lesson words in new situations.', 'Вісім питань на слова|Osiem pytań na słowa|Eight word questions', [
 mc('Машина стара, на ній ____.', ['іржа', 'мрія', 'музика'], 0, 'Іржа → іржавий.|Іржа → іржавий.|Іржа (rust) → іржавий.', tag='word'),
 mc('Компанія, яка дає гроші команді, — це ____.', ['спонсор', 'брат', 'причіп'], 0, 'Спонсор.|Sponsor.|Sponsor.', tag='word'),
 mc('Dinoco має багато грошей. Вона ____.', ['маленька', 'багата', 'іржава'], 1, 'Багатий = rich.|Bogaty.|Rich.', tag='word'),
 mc('Мак везе Маккуїна в ____.', ['причепі', 'гелікоптері', 'кремі'], 0, 'У причепі.|W przyczepie.|In the trailer.', tag='word'),
 mc('Мак завжди з Маккуїном. Він ____.', ['вірний', 'смішний', 'порожній'], 0, 'Вірний = loyal.|Lojalny.|Loyal.', tag='word'),
 mc('Знак компанії на машині — це ____.', ['логотип', 'бос', 'брат'], 0, 'Логотип.|Logo.|Logo.', tag='word'),
 mc('Брати жартують. Вони ____.', ['смішні', 'сонні', 'сині'], 0, 'Смішний = funny.|Zabawny.|Funny.', tag='word'),
 mc('Механіки Маккуїна — це його ____.', ['бригада', 'дружина', 'мрія'], 0, 'Бригада = crew.|Ekipa.|Crew.', tag='word'),
])
L.final('ЗАПИС У БЛОКНОТІ|WPIS W NOTESIE|NOTEBOOK ENTRY', 'Ти механік Маккуїна. Напиши про команду (25+ слів): хто спонсор? хто Мак? яка мрія Маккуїна? яка твоя мрія?|Jesteś mechanikiem Zygzaka. Napisz po ukraińsku o zespole (25+ słów): kto jest sponsorem? kim jest Mack? jakie jest marzenie Zygzaka? jakie jest twoje?|You are McQueen\'s mechanic. Write in Ukrainian about the team (25+ words): who is the sponsor? who is Mack? what is McQueen\'s dream? what is yours?',
 'Наш спонсор — … Мак — мій … Мрія Маккуїна — … Моя мрія — …', 25)
print(L.save('cars', 3))
