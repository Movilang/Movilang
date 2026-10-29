import sys; sys.path.insert(0, '/home/claude/work/std'); from lib import *
g = 'uk'; L = Lesson('7acadd39-a5e2-4de1-8971-5f77dbaf92b1', g)
SC = 'Встав слово, обери правду, зрозумій героя|Wstaw słowo, oceń prawdę, zrozum bohatera|Fill the gap, judge true/false, read the hero'
gm = lambda q, o, a, e: mc(q, o, a, e, tag='gram'); wd = lambda q, o, a, e: mc(q, o, a, e, tag='word')
L.ref(0).intro('ТВОЯ РОЛЬ|TWOJA ROLA|YOUR ROLE', 'Ти їдеш на старому пікапі шукати Маккуїна по дорозі 66. Нарешті бачиш маленьке сонне містечко — Радіатор-Спрінгз. А на головній вулиці — червона машина і поліцейська сирена!|Jedziesz starym pikapem szukać Zygzaka drogą 66. W końcu widzisz małe senne miasteczko — Chłodnicę Górską. A na głównej ulicy — czerwone auto i policyjna syrena!|You drive an old pickup along Route 66 looking for McQueen. At last you see a sleepy little town — Radiator Springs. And on Main Street: a red car and a police siren!')
L.ref(1).match('СЦЕНА 1 · СЛОВА|SCENA 1 · SŁOWA|SCENE 1 · WORDS', ['вулиця=вулиця/ulica/street', 'кафе=кафе/kawiarnia/café', 'магазин=магазин/sklep/shop', 'світлофор=світлофор/światła/traffic light', 'жовтий=жовтий/żółty/yellow'])
L.set('СЦЕНА 1 · СОННЕ МІСТЕЧКО|SCENA 1 · SENNE MIASTECZKO|SCENE 1 · A SLEEPY TOWN', 'Ти в\'їжджаєш у Радіатор-Спрінгз.|Wjeżdżasz do Chłodnicy Górskiej.|You drive into Radiator Springs.', SC, [
 gap('Тут лише одна ____.', 'Tu jest tylko jedna ulica.|There is only one street.', ['вулиця', 'кава', 'шина'], 0, 'Вулиця = street.|Ulica.|Street.'),
 gap('Тут є ____!', 'Tu jest kawiarnia!|There is a café!', ['кафе', 'пустеля', 'гонка'], 0, 'Кафе = café.|Kawiarnia.|Café.'),
 gap('Є ____ шин.', 'Jest sklep z oponami.|There is a tyre shop.', ['магазин', 'мотель', 'місяць'], 0, 'Магазин = shop.|Sklep.|Shop.'),
 gap('Тут один ____.', 'Tu są jedne światła.|There is one traffic light.', ['світлофор', 'будинок', 'кактус'], 0, 'Світлофор.|Światła.|Traffic light.'),
 gap('Воно ____!', 'Jest żółte!|It\'s yellow!', ['жовте', 'червоне', 'синє'], 0, 'Жовтий = yellow.|Żółty.|Yellow.'),
 gap('Яке ____ містечко!', 'Jakie senne miasteczko!|What a sleepy town!', ['сонне', 'гучне', 'багате'], 0, 'Сонний = sleepy.|Senny.|Sleepy.'),
 tf(g, 'На вулиці багато машин.', 'Na ulicy jest dużo aut.|There are many cars on the street.', False, 'Тут немає машин — порожньо.|Nie ma aut — pusto.|No cars — it\'s empty.'),
])
L.ref(2).match('СЦЕНА 2 · СЛОВА|SCENA 2 · SŁOWA|SCENE 2 · WORDS', ['сирена=сирена/syrena/siren', 'закон=закон/prawo/law', 'позаду=позаду/z tyłu/behind', 'бензин=бензин/benzyna/gas', 'гонитва=гонитва/pościg/chase'])
L.set('СЦЕНА 2 · ГОНИТВА|SCENA 2 · POŚCIG|SCENE 2 · THE CHASE', 'Шериф їде за Маккуїном із сиреною.|Szeryf jedzie za Zygzakiem z syreną.|The Sheriff chases McQueen with his siren on.', SC, [
 gap('Що це за ____?', 'Co to za syrena?|What is that siren?', ['сирена', 'вулиця', 'кава'], 0, 'Сирена.|Syrena.|Siren.'),
 gap('Тут поліцейська ____!', 'Tu jest radiowóz!|There is a police car!', ['машина', 'вулиця', 'кава'], 0, 'Поліцейська машина.|Radiowóz.|Police car.'),
 gap('Стій, ____!', 'Stój, chłopcze!|Stop, boy!', ['хлопче', 'кактусе', 'магазине'], 0, 'Хлопче — кличний відмінок.|Wołacz.|Vocative.'),
 gap('Це ____!', 'To jest prawo!|This is the law!', ['закон', 'бензин', 'світлофор'], 0, 'Закон = law.|Prawo.|Law.'),
 gap('Він ____ мене!', 'On jest za mną!|He\'s behind me!', ['позаду', 'усередині', 'надворі'], 0, 'Позаду = behind.|Z tyłu.|Behind.'),
 gap('Це ____!', 'To pościg!|It\'s a chase!', ['гонитва', 'нічия', 'мрія'], 0, 'Гонитва = chase.|Pościg.|Chase.'),
 mc('Маккуїн думає, що сирена — це фанати. Чому він помиляється?', ['Це шериф, і він сердитий', 'Це музика в кафе', 'Це Мак'], 0, 'Шериф ловить його.|Szeryf go goni.|The Sheriff is chasing him.', 'McQueen thinks the siren is fans. Why is he wrong?|Zygzak myśli, że syrena to kibice. Dlaczego się myli?|McQueen thinks the siren is fans. Why is he wrong?'),
])
L.ref(3).match('СЦЕНА 3 · СЛОВА|SCENA 3 · SŁOWA|SCENE 3 · WORDS', ['головний=головний/główny/main', 'заправка=заправка/stacja benzynowa/gas station', 'конус=конус/pachołek/cone', 'статуя=статуя/pomnik/statue', 'кактус=кактус/kaktus/cactus'])
L.set('СЦЕНА 3 · ГОЛОВНА ВУЛИЦЯ|SCENA 3 · GŁÓWNA ULICA|SCENE 3 · MAIN STREET', 'Ти роздивляєшся містечко з пікапа.|Oglądasz miasteczko z pikapa.|You look at the town from the pickup.', SC, [
 gap('Це ____ вулиця.', 'To główna ulica.|This is the main street.', ['головна', 'жовта', 'сонна'], 0, 'Головний = main.|Główny.|Main.'),
 gap('Тут є ____?', 'Czy jest tu stacja benzynowa?|Is there a gas station?', ['заправка', 'статуя', 'сирена'], 0, 'Заправка.|Stacja benzynowa.|Gas station.'),
 gap('Номери — це ____!', 'Pokoje to pachołki!|The rooms are cones!', ['конуси', 'кактуси', 'вулиці'], 0, 'Конус = cone.|Pachołek.|Cone.'),
 gap('Подивись на ту ____!', 'Popatrz na ten pomnik!|Look at that statue!', ['статую', 'вулицю', 'каву'], 0, 'Статуя.|Pomnik.|Statue.'),
 gap('Світло ____.', 'Światło miga.|The light blinks.', ['блимає', 'спить', 'співає'], 0, 'Блимати = to blink.|Migać.|Blink.'),
 tf(g, 'Мотель у Радіатор-Спрінгз — з конусів.', 'Motel w Chłodnicy Górskiej jest z pachołków.|The motel is made of cones.', True, 'Так, мотель «Затишний конус».|Tak, motel z pachołków.|Yes, the Cozy Cone.'),
 tf(g, 'Світлофор у містечку червоний і зелений.', 'Światła są czerwone i zielone.|The traffic light is red and green.', False, 'Він тільки блимає жовтим.|Tylko miga na żółto.|It only blinks yellow.'),
])
L.intro('ПРАВИЛО|ZASADA|RULE', 'Є = there is / there are: Тут є кафе. Є магазин шин. Тут є старі будинки. Немає + родовий = there is no: Тут немає машин. Немає заправки. Питання: Тут є мотель? — Так, є. / Ні, немає.|Є = jest/są: Тут є кафе (tu jest kawiarnia). Немає + dopełniacz = nie ma: Тут немає машин (nie ma aut). Pytanie: Тут є мотель? — Так, є. / Ні, немає.|Є = there is/are: Тут є кафе. Немає + genitive = there is no: Тут немає машин. Question: Тут є мотель? — Так, є. / Ні, немає.')
L.set('ГРАМАТИКА · ЩО Є В МІСТЕЧКУ?|GRAMATYKA · CO JEST W MIASTECZKU?|GRAMMAR · WHAT\'S IN THE TOWN?', 'Ти описуєш Радіатор-Спрінгз команді по телефону.|Opisujesz Chłodnicę Górską zespołowi przez telefon.|You describe Radiator Springs to the team by phone.', 'Є / немає|Є / немає|Є / немає', [
 gm('«Тут ____ кафе.»', ['є', 'немає', 'нікого'], 0, 'Є кафе.|Jest kawiarnia.|There is a café.'),
 gm('«Тут немає ____.»', ['машин', 'машини є', 'машина'], 0, 'Родовий множини: машин.|Dopełniacz: машин.|Genitive: машин.'),
 gm('«____ магазин шин.»', ['Є', 'Немає', 'Нікого'], 0, 'Є.|Є.|Є.'),
 gm('«Тут є ____?» — «Так, є.»', ['мотель', 'мотелю', 'мотелі є'], 0, 'Після «є» — називний.|Mianownik.|Nominative.'),
 gm('«Тут немає ____.»', ['заправки', 'заправка', 'заправку'], 0, 'Родовий: заправки.|Dopełniacz.|Genitive.'),
 gm('«Тут є старі ____.»', ['будинки', 'будинків', 'будинок є'], 0, 'Називний множини.|Mianownik l.mn.|Nominative plural.'),
 gm('«Тут немає ____ світлофора.»', ['другого', 'другий', 'друга'], 0, 'Родовий: другого.|Dopełniacz.|Genitive.'),
 gm('«Тут є якісь машини?» — «Ні, ____.»', ['немає', 'є', 'нікого є'], 0, 'Ні, немає.|Nie ma.|No, there aren\'t.'),
 gm('«На вулиці ____ кактус.»', ['є', 'немає', 'нема є'], 0, 'Є кактус.|Jest kaktus.|There is a cactus.'),
 gm('«У містечку немає ____.»', ['стадіону', 'стадіон', 'стадіони є'], 0, 'Родовий: стадіону.|Dopełniacz.|Genitive.'),
 gm('«Тут ____ поліцейська машина!»', ['є', 'немає', 'нікого'], 0, 'Є.|Є.|Є.'),
 gm('«Тут немає ____» (людей).', ['нікого', 'ніхто', 'нічого'], 0, 'Нікого немає.|Nikogo nie ma.|Nobody.'),
])
L.reading('Путівник: Радіатор-Спрінгз|Przewodnik: Chłodnica Górska|Guide: Radiator Springs', 'ЧИТАННЯ|CZYTANIE|READING', 'Старий путівник по дорозі 66. Прочитай і обери слова.|Stary przewodnik po drodze 66. Przeczytaj po ukraińsku i wybierz słowa.|An old Route 66 guide. Read it in Ukrainian and choose the words.', [
 S('Радіатор-Спрінгз — маленьке містечко на дорозі 66.'),
 S('Тут лише одна головна ____.', ['вулиця', 'гонка', 'кава'], 0),
 S('На вулиці ____ кафе Фло.', ['є', 'немає', 'нікого'], 0),
 S('Там завжди смачний ____.', ['бензин', 'кактус', 'конус'], 0),
 S('Є також ____ шин Луїджі.', ['магазин', 'мотель', 'світлофор'], 0),
 S('Мотель дуже незвичайний: номери — це великі ____.', ['конуси', 'кактуси', 'статуї'], 0),
 S('У центрі стоїть стара ____.', ['статуя', 'сирена', 'шина'], 0),
 S('У містечку тільки один ____.', ['світлофор', 'стадіон', 'гелікоптер'], 0),
 S('Він не червоний і не зелений: він блимає ____.', ['жовтим', 'синім', 'фіолетовим'], 0),
 S('Тут немає великих ____.', ['будинків', 'будинок', 'будинки є'], 0),
 S('Навколо пустеля, пісок і ____.', ['кактуси', 'фанати', 'телевізори'], 0),
 S('Зараз на вулиці майже ____ машин.', ['немає', 'є', 'нікого'], 0),
 S('Містечко дуже ____.', ['сонне', 'гучне', 'багате'], 0),
 S('Але сьогодні вночі тут ____!', ['гонитва', 'нічия', 'мрія'], 0),
 S('Шериф із сиреною їде за червоною машиною.'),
 S('Хто ця машина? Ми знаємо: це Маккуїн!'),
], 'Є кафе, є магазин, але немає машин.|Jest kawiarnia i sklep, ale nie ma aut.|There\'s a café and a shop, but no cars.')
L.set('РОЗУМІННЯ ТЕКСТУ|ROZUMIENIE TEKSTU|READING CHECK', 'Питання до путівника.|Pytania do przewodnika.|Questions about the guide.', 'П\'ять питань|Pięć pytań|Five questions', [
 mc('Скільки головних вулиць у містечку?', ['Одна', 'Дві', 'Десять'], 0, 'Одна.|Jedna.|One.', 'How many main streets?|Ile głównych ulic?|How many main streets?'),
 mc('Чиє кафе на вулиці?', ['Фло', 'Мака', 'Короля'], 0, 'Кафе Фло.|Kawiarnia Flo.|Flo\'s café.', 'Whose café is it?|Czyja to kawiarnia?|Whose café is it?'),
 mc('Які номери в мотелі?', ['Конуси', 'Причепи', 'Будинки'], 0, 'Конуси.|Pachołki.|Cones.', 'What are the motel rooms like?|Jakie są pokoje w motelu?|What are the motel rooms?'),
 mc('Яким світлом блимає світлофор?', ['Жовтим', 'Червоним', 'Синім'], 0, 'Жовтим.|Żółtym.|Yellow.', 'What colour does the light blink?|Jakim światłem miga?|What colour does it blink?'),
 mc('Що сьогодні вночі на вулиці?', ['Гонитва', 'Свято', 'Гонка'], 0, 'Гонитва.|Pościg.|A chase.', 'What happens tonight?|Co dzieje się dziś w nocy?|What happens tonight?'),
])
L.quest('КВЕСТ: ДЕ МАККУЇН?|QUEST: GDZIE JEST ZYGZAK?|QUEST: WHERE IS McQUEEN?', 'Ти зупиняєшся біля кафе Фло й питаєш про Маккуїна. Говори українською.|Zatrzymujesz się przy kawiarni Flo i pytasz o Zygzaka. Mów po ukraińsku.|You stop at Flo\'s café and ask about McQueen. Speak Ukrainian.', 'alley', {
 's1': step('Фло: «Привіт, любий! Чим допомогти?»', 'Cześć, kochanie! W czym pomóc?|Hi, honey! How can I help?', 'Кафе Фло.|Kawiarnia Flo.|Flo\'s café.', [ch('Тут є червона машина?', True, 's2', 'Добре питання.|Dobre pytanie.|Good question.'), ch('Тут є червоної машини?', False, 's2', 'Після «є» — називний.|Po „є” mianownik.|Nominative after “є”.')]),
 's2': step('Фло: «Так, є! Але шериф його вже ловить.»', 'Tak! Ale szeryf już go goni.|Yes! But the sheriff is chasing him.', 'Чути сирену.|Słychać syrenę.|A siren is heard.', [ch('Де він зараз?', True, 's3', 'Так.|Tak.|Yes.'), ch('Де він є є?', False, 's3', 'Без «є».|Bez „є”.|No “є”.')]),
 's3': step('Фло: «На головній вулиці. Там є статуя.»', 'Na głównej ulicy. Tam jest pomnik.|On Main Street. There\'s a statue.', 'Шум на вулиці.|Hałas na ulicy.|Noise outside.', [ch('Дякую! А тут є заправка?', True, 's4', 'Корисно.|Przydatne.|Useful.'), ch('Дякую. Бувай.', True, 's4', 'Добре.|Dobrze.|OK.')]),
 's4': step('Фло: «Заправки немає, але в мене є бензин!»', 'Nie ma stacji, ale mam benzynę!|No station, but I have gas!', 'Фло усміхається.|Flo się uśmiecha.|Flo smiles.', [ch('Чудово! Я їду до статуї.', True, 'end_good', 'Вперед!|Naprzód!|Go!'), ch('Немає бензин?', False, 'end_bad', 'Треба «немає бензину», але Фло каже, що є!|„немає бензину” — ale Flo ma!|“немає бензину” — but Flo has some!')]),
}, {'end_good': end(True, 'Кінцівка: Слід знайдено|Zakończenie: Trop znaleziony|Ending: On the trail', 'Ти під\'їжджаєш до статуї… і бачиш безлад. Маккуїн тут! Але що він зробив з вулицею?|Podjeżdżasz do pomnika… i widzisz bałagan. Zygzak tu jest! Ale co zrobił z ulicą?|You drive up to the statue… and see a mess. McQueen is here! But what did he do to the street?'),
    'end_bad': end(False, 'Кінцівка: Заблукав|Zakończenie: Zgubiony|Ending: Lost', 'Фло тебе не зрозуміла. Спробуй ще: «Тут є червона машина?»|Flo cię nie zrozumiała. Spróbuj: „Тут є червона машина?”|Flo didn\'t understand. Try: “Тут є червона машина?”')})
L.set('ПИШИ Й СКЛАДАЙ|PISZ I UKŁADAJ|WRITE AND BUILD', 'Твоє повідомлення команді про містечко.|Twoja wiadomość do zespołu o miasteczku.|Your message to the team about the town.', 'Впиши й склади|Wpisz i ułóż|Type and build', [
 typ(g, 'Тут є кафе.', 'Tu jest kawiarnia.|There is a café here.'), order(g, ['Тут', 'лише', 'одна', 'вулиця.'], 'Tu jest tylko jedna ulica.|There is only one street.'),
 typ(g, 'Тут немає машин.', 'Nie ma tu aut.|There are no cars here.'), order(g, ['Тут', 'є', 'мотель?'], 'Czy jest tu motel?|Is there a motel here?'),
 typ(g, 'Світло блимає.', 'Światło miga.|The light blinks.'), order(g, ['Подивись', 'на', 'ту', 'статую!'], 'Popatrz na ten pomnik!|Look at that statue!'),
 typ(g, 'Це закон!', 'To prawo!|This is the law!'), order(g, ['Яке', 'сонне', 'містечко!'], 'Jakie senne miasteczko!|What a sleepy town!'),
])
L.speak('Тут є кафе й магазин шин, але немає машин.', 'Jest kawiarnia i sklep z oponami, ale nie ma aut.|There\'s a café and a tyre shop, but no cars.')
L.speak('Стій, хлопче! Це закон!', 'Stój, chłopcze! To prawo!|Stop, boy! This is the law!')
L.set('МІСТЕЧКО · СЛОВА|MIASTECZKO · SŁOWA|THE TOWN · WORDS', 'Слова уроку в нових ситуаціях.|Słowa lekcji w nowych sytuacjach.|Lesson words in new situations.', 'Вісім питань на слова|Osiem pytań|Eight word questions', [
 wd('Де купити шини? У ____.', ['магазині', 'кафе', 'мотелі'], 0, 'У магазині.|W sklepie.|In the shop.'),
 wd('Де спати вночі? У ____.', ['мотелі', 'світлофорі', 'кактусі'], 0, 'У мотелі.|W motelu.|In the motel.'),
 wd('Де пити каву? У ____.', ['кафе', 'заправці', 'статуї'], 0, 'У кафе.|W kawiarni.|In the café.'),
 wd('Де купити бензин? На ____.', ['заправці', 'вулиці', 'статуї'], 0, 'На заправці.|Na stacji.|At the gas station.'),
 wd('Рослина в пустелі — ____.', ['кактус', 'конус', 'закон'], 0, 'Кактус.|Kaktus.|Cactus.'),
 wd('Шериф каже: «Це ____!»', ['закон', 'кафе', 'кактус'], 0, 'Закон.|Prawo.|Law.'),
 wd('Шериф їде ____ Маккуїна.', ['позаду', 'усередині', 'під'], 0, 'Позаду.|Za.|Behind.'),
 wd('Колір світлофора в містечку — ____.', ['жовтий', 'синій', 'фіолетовий'], 0, 'Жовтий.|Żółty.|Yellow.'),
])
L.final('ЛИСТІВКА З ДОРОГИ 66|POCZTÓWKA Z DROGI 66|POSTCARD FROM ROUTE 66', 'Напиши листівку команді (25+ слів): що є в Радіатор-Спрінгз? чого там немає? що ти бачиш на головній вулиці?|Napisz po ukraińsku pocztówkę do zespołu (25+ słów): co jest w Chłodnicy Górskiej? czego tam nie ma? co widzisz na głównej ulicy?|Write a postcard to the team in Ukrainian (25+ words): what is in Radiator Springs? what isn\'t there? what do you see on Main Street?',
 'Привіт! Я в Радіатор-Спрінгз. Тут є … Тут немає … На головній вулиці …', 25, 'letter')
print(L.save('cars', 7))
