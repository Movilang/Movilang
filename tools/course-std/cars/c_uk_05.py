import sys; sys.path.insert(0, '/home/claude/work/std'); from lib import *
g = 'uk'; L = Lesson('ec1506cc-d10d-42c0-8877-9f6a8220c364', g)
SC = 'Встав слово, обери правду, зрозумій героя|Wstaw słowo, oceń prawdę, zrozum bohatera|Fill the gap, judge true/false, read the hero'
gm = lambda q, o, a, e: mc(q, o, a, e, tag='gram')
L.ref(0).intro('ТВОЯ РОЛЬ|TWOJA ROLA|YOUR ROLE', 'Третя ночі. Мак спить за кермом. Чотири яскраві машини граються біля нього на шосе. Двері причепа відчиняються — і Маккуїн викочується в темряву. Ти бачиш це з вікна й хапаєш телефон.|Trzecia w nocy. Mack śpi za kierownicą. Cztery jaskrawe auta bawią się obok niego na autostradzie. Drzwi przyczepy się otwierają — i Zygzak wytacza się w ciemność. Widzisz to z okna i chwytasz telefon.|3 a.m. Mack is asleep at the wheel. Four bright cars play around him on the highway. The trailer door opens — and McQueen rolls out into the dark. You see it from the window and grab the phone.')
L.ref(1).match('СЦЕНА 1 · СЛОВА|SCENA 1 · SŁOWA|SCENE 1 · WORDS', ['шум=шум/hałas/noise', 'гучний=гучний/głośny/loud', 'яскравий=яскравий/jasny/bright', 'двері=двері/drzwi/door', 'тихий=тихий/cichy/quiet'])
L.set('СЦЕНА 1 · МАК ЗАСИНАЄ|SCENA 1 · MACK ZASYPIA|SCENE 1 · MACK FALLS ASLEEP', 'Чотири машини з гучною музикою оточують Мака.|Cztery auta z głośną muzyką otaczają Macka.|Four cars with loud music surround Mack.', SC, [
 gap('Мак ____!', 'Mack śpi!|Mack is asleep!', ['спить', 'кричить', 'їде'], 0, 'Спати = to sleep.|Spać.|To sleep.'),
 gap('Що це за ____?', 'Co to za hałas?|What is that noise?', ['шум', 'місяць', 'пісок'], 0, 'Шум = noise.|Hałas.|Noise.'),
 gap('Надто ____!', 'Za głośno!|Too loud!', ['гучно', 'тихо', 'повільно'], 0, 'Гучно = loud.|Głośno.|Loud.'),
 gap('Вони такі ____!', 'Są takie jaskrawe!|They are so bright!', ['яскраві', 'тихі', 'холодні'], 0, 'Яскравий = bright.|Jasny.|Bright.'),
 gap('Подивись на ____ машину!', 'Popatrz na fioletowe auto!|Look at the purple car!', ['фіолетову', 'тиху', 'загублену'], 0, 'Фіолетовий = purple.|Fioletowy.|Purple.'),
 gap('Двері ____!', 'Drzwi są otwarte!|The door is open!', ['відчинені', 'тихі', 'холодні'], 0, 'Відчинений = open.|Otwarty.|Open.'),
 tf(g, 'Маккуїн теж спить, коли падає з причепа.', 'Zygzak też śpi, gdy wypada z przyczepy.|McQueen is also asleep when he falls out.', True, 'Він спить і нічого не бачить.|Śpi i nic nie widzi.|He is asleep and sees nothing.'),
 tf(g, 'Чотири машини допомагають Макові.', 'Cztery auta pomagają Mackowi.|The four cars help Mack.', False, 'Вони жартують і заважають.|Żartują i przeszkadzają.|They play tricks.'),
])
L.ref(2).match('СЦЕНА 2 · СЛОВА|SCENA 2 · SŁOWA|SCENE 2 · WORDS', ['загублений=загублений/zgubiony/lost', 'телефон=телефон/telefon/phone', 'карта=карта/mapa/map', 'холодний=холодний/zimny/cold', 'допомога=допомога/pomoc/help'])
L.set('СЦЕНА 2 · САМ У ТЕМРЯВІ|SCENA 2 · SAM W CIEMNOŚCI|SCENE 2 · ALONE IN THE DARK', 'Маккуїн прокидається сам на темному шосе.|Zygzak budzi się sam na ciemnej autostradzie.|McQueen wakes up alone on the dark highway.', SC, [
 gap('Я ____!', 'Zgubiłem się!|I\'m lost!', ['загубився', 'співаю', 'виграв'], 0, 'Загубитися = to get lost.|Zgubić się.|Get lost.'),
 gap('У мене немає ____!', 'Nie mam reflektorów!|I have no headlights!', ['фар', 'фари', 'фара'], 0, 'Немає + фар.|Немає + фар.|Немає + фар.'),
 gap('У тебе є ____?', 'Masz telefon?|Do you have a phone?', ['телефон', 'пісок', 'місяць'], 0, 'Телефон = phone.|Telefon.|Phone.'),
 gap('У мене немає ____.', 'Nie mam mapy.|I have no map.', ['карти', 'карта', 'карту'], 0, 'Немає карти.|Немає карти.|Немає карти.'),
 gap('Тут так ____.', 'Tu jest tak zimno.|It\'s so cold here.', ['холодно', 'гучно', 'яскраво'], 0, 'Холодно = cold.|Zimno.|Cold.'),
 gap('Тут ____ немає.', 'Nikogo tu nie ma.|There is nobody here.', ['нікого', 'нічого', 'ніколи'], 0, 'Нікого = nobody.|Nikogo.|Nobody.'),
 mc('Маккуїн кричить: «Маку! Де ти?» Як він почувається?', ['Наляканий', 'Щасливий', 'Сонний'], 0, 'Йому страшно.|Boi się.|He is scared.', 'McQueen shouts: “Mack! Where are you?” How does he feel?|Zygzak krzyczy: „Mack! Gdzie jesteś?” Jak się czuje?|McQueen shouts: “Mack! Where are you?” How does he feel?'),
])
L.ref(3).match('СЦЕНА 3 · СЛОВА|SCENA 3 · SŁOWA|SCENE 3 · WORDS', ['з\'їзд=з\'їзд/zjazd/exit', 'помилка=помилка/błąd/mistake', 'пустеля=пустеля/pustynia/desert', 'місяць=місяць/księżyc/moon', 'містечко=містечко/miasteczko/small town'])
L.set('СЦЕНА 3 · НЕ ТА ВАНТАЖІВКА|SCENA 3 · NIE TA CIĘŻARÓWKA|SCENE 3 · THE WRONG TRUCK', 'Маккуїн їде за чужою вантажівкою й звертає з шосе.|Zygzak jedzie za obcą ciężarówką i zjeżdża z autostrady.|McQueen follows a stranger\'s truck off the highway.', SC, [
 gap('Де ____?', 'Gdzie jest zjazd?|Where is the exit?', ['з\'їзд', 'місяць', 'пісок'], 0, 'З\'їзд = exit.|Zjazd.|Exit.'),
 gap('Це ____!', 'To błąd!|This is a mistake!', ['помилка', 'корова', 'карта'], 0, 'Помилка = mistake.|Błąd.|Mistake.'),
 gap('Це ____!', 'To pustynia!|This is a desert!', ['пустеля', 'двері', 'музика'], 0, 'Пустеля = desert.|Pustynia.|Desert.'),
 gap('____! Усюди!', 'Piasek! Wszędzie!|Sand! Everywhere!', ['Пісок', 'Телефон', 'Шум'], 0, 'Пісок = sand.|Piasek.|Sand.'),
 gap('____! Нарешті!', 'Miasteczko! Nareszcie!|A town! Finally!', ['Містечко', 'Пустеля', 'Помилка'], 0, 'Містечко = small town.|Miasteczko.|Small town.'),
 tf(g, 'Вантажівка, за якою їде Маккуїн, — це Мак.', 'Ciężarówka, za którą jedzie Zygzak, to Mack.|The truck McQueen follows is Mack.', False, 'Це чужа вантажівка — помилка!|To obca ciężarówka — błąd!|It\'s a stranger\'s truck — a mistake!'),
 mc('Маккуїн бачить корову на дорозі. Що він каже?', ['«Корова? Тут?»', '«Мій кубок!»', '«Я сонний.»'], 0, 'Він здивований.|Jest zdziwiony.|He is surprised.', 'McQueen sees a cow on the road. What does he say?|Zygzak widzi krowę na drodze. Co mówi?|McQueen sees a cow on the road. What does he say?'),
])
L.intro('ПРАВИЛО|ZASADA|RULE', 'У мене є … = I have: У мене є телефон. У тебе є карта? Немає + родовий відмінок = I don\'t have: У мене немає телефону, немає карти, немає фар. Ніхто / нікого: Тут нікого немає.|У мене є … = mam: У мене є телефон (mam telefon). Немає + dopełniacz = nie mam: У мене немає телефону, карти, фар. Тут нікого немає = nikogo tu nie ma.|У мене є … = I have: У мене є телефон. Немає + genitive = I don\'t have: У мене немає телефону, карти, фар. Тут нікого немає = nobody is here.')
L.set('ГРАМАТИКА · Є ЧИ НЕМАЄ?|GRAMATYKA · MAM CZY NIE MAM?|GRAMMAR · HAVE OR NOT?', 'Що є і чого немає в Маккуїна вночі?|Co Zygzak ma, a czego nie ma w nocy?|What does McQueen have and not have tonight?', 'У мене є / у мене немає|У мене є / немає|У мене є / немає', [
 gm('«У мене ____ телефону!»', ['немає', 'є', 'нема є'], 0, 'Немає + родовий.|Немає + dopełniacz.|Немає + genitive.'),
 gm('«У тебе ____ карта?»', ['є', 'немає', 'нема'], 0, 'Питання: у тебе є…?|Pytanie: у тебе є…?|Question: у тебе є…?'),
 gm('«У мене немає ____.»', ['карти', 'карта', 'карту'], 0, 'Родовий: карти.|Dopełniacz: карти.|Genitive: карти.'),
 gm('«У мене немає ____!»', ['фар', 'фари', 'фара'], 0, 'Множина, родовий: фар.|L. mnoga: фар.|Plural genitive: фар.'),
 gm('«Тут ____ немає.»', ['нікого', 'ніхто', 'ніколи'], 0, 'Нікого немає.|Nikogo nie ma.|Nobody is here.'),
 gm('Мак: «У мене ____ причіп.»', ['є', 'немає', 'ні'], 0, 'У мене є причіп.|Mam przyczepę.|I have a trailer.'),
 gm('«У мене немає ____.»', ['телефону', 'телефон', 'телефона є'], 0, 'Родовий: телефону.|Dopełniacz: телефону.|Genitive: телефону.'),
 gm('«У Маккуїна немає ____.»', ['друзів', 'друзі', 'друг'], 0, 'Родовий множини: друзів.|Dopełniacz l.mn.: друзів.|Genitive plural: друзів.'),
 gm('«У мене є ____!» (на телефоні)', ['карта', 'карти', 'карту'], 0, 'Після «є» — називний.|Po „є” mianownik.|After “є” nominative.'),
 gm('«____ мене немає допомоги.»', ['У', 'В є', 'На'], 0, 'У мене…|У мене…|У мене…'),
 gm('«У нас немає ____!»', ['часу', 'час', 'часи'], 0, 'Родовий: часу.|Dopełniacz: часу.|Genitive: часу.'),
 gm('«У тебе ____ фари? — Так!»', ['є', 'немає', 'нікого'], 0, 'Є.|Є.|Є.'),
])
L.reading('Радіо 66: машина загубилася в пустелі|Radio 66: auto zgubiło się na pustyni|Radio 66: a car is lost in the desert', 'ЧИТАННЯ|CZYTANIE|READING', 'Прочитай новину й обери правильні слова.|Przeczytaj wiadomość po ukraińsku i wybierz słowa.|Read the news in Ukrainian and choose the words.', [
 S('Нічні новини Радіо 66.'),
 S('Сьогодні вночі на шосе ____ вантажівка Мак.', ['спала', 'співала', 'кричала'], 0),
 S('Біля неї їхали чотири ____ машини.', ['яскраві', 'тихі', 'іржаві'], 0),
 S('Була дуже ____ музика.', ['гучна', 'холодна', 'загублена'], 0),
 S('Двері причепа ____.', ['відчинилися', 'співали', 'спали'], 0),
 S('Зірка гонок Маккуїн упав на ____.', ['дорогу', 'місяць', 'телефон'], 0),
 S('Він прокинувся сам. У нього не було ____.', ['фар', 'фари', 'фара'], 0),
 S('У нього не було карти й ____.', ['телефону', 'телефон', 'телефони'], 0),
 S('Маккуїн кричав: «Маку! ____!»', ['Допоможи', 'Спи', 'Співай'], 0),
 S('Але там ____ не було.', ['нікого', 'ніхто', 'нічия'], 0),
 S('Він поїхав за іншою вантажівкою. Це була ____.', ['помилка', 'мрія', 'кава'], 0),
 S('Тепер він у ____.', ['пустелі', 'причепі', 'місті'], 0),
 S('Там тільки пісок, корови і ____.', ['місяць', 'кубок', 'крем'], 0),
 S('Механіки команди вже шукають його.'),
 S('Якщо ви бачили червону машину №95 — дзвоніть нам!'),
], 'Немає + родовий: немає фар, телефону.|Немає + dopełniacz.|Немає + genitive.')
L.set('РОЗУМІННЯ ТЕКСТУ|ROZUMIENIE TEKSTU|READING CHECK', 'Питання до новини.|Pytania do wiadomości.|Questions about the news.', 'П\'ять питань до тексту|Pięć pytań|Five questions', [
 mc('Що робив Мак?', ['Спав за кермом', 'Пив каву', 'Співав'], 0, 'Він спав.|Spał.|He slept.', 'What was Mack doing?|Co robił Mack?|What was Mack doing?'),
 mc('Скільки машин їхало біля Мака?', ['Чотири', 'Дві', 'Десять'], 0, 'Чотири.|Cztery.|Four.', 'How many cars drove near Mack?|Ile aut jechało obok Macka?|How many cars?'),
 mc('Чого не було в Маккуїна?', ['Карти й телефону', 'Кубка', 'Номера'], 0, 'Немає карти й телефону.|Nie miał mapy i telefonu.|No map, no phone.', 'What didn\'t McQueen have?|Czego nie miał Zygzak?|What didn\'t McQueen have?'),
 mc('Чому він у пустелі?', ['Поїхав за іншою вантажівкою', 'Хотів спати', 'Шукав каву'], 0, 'Це була помилка.|To był błąd.|It was a mistake.', 'Why is he in the desert?|Dlaczego jest na pustyni?|Why is he in the desert?'),
 mc('Хто його шукає?', ['Механіки команди', 'Корови', 'Нікого'], 0, 'Ти й команда!|Ty i zespół!|You and the team!', 'Who is looking for him?|Kto go szuka?|Who is looking for him?'),
])
L.quest('КВЕСТ: ДЗВІНОК|QUEST: TELEFON|QUEST: THE CALL', 'Ти дзвониш Маккуїну. Він у темряві. Допоможи йому українською.|Dzwonisz do Zygzaka. Jest w ciemności. Pomóż mu po ukraińsku.|You call McQueen. He is in the dark. Help him in Ukrainian.', 'forest', {
 's1': step('Маккуїн: «Алло? Хто це?»', 'Halo? Kto to?|Hello? Who is this?', 'Дзвінок у темряві.|Telefon w ciemności.|A call in the dark.', [ch('Це я, твій механік! Де ти?', True, 's2', 'Добре!|Dobrze!|Good!'), ch('Я є механік є.', False, 's1b', 'Так не кажуть.|Tak się nie mówi.|Not how we say it.')]),
 's1b': step('Маккуїн: «Що? Я не розумію!»', 'Co? Nie rozumiem!|What? I don\'t understand!', 'Шум у телефоні.|Szum w telefonie.|Static on the line.', [ch('Я механік. Де ти?', True, 's2', 'Так!|Tak!|Yes!'), ch('Механік де я?', False, 'end_bad', 'Неправильно.|Źle.|Wrong.')]),
 's2': step('Маккуїн: «Я не знаю! Тут темно!»', 'Nie wiem! Tu jest ciemno!|I don\'t know! It\'s dark!', 'Він наляканий.|Jest przestraszony.|He is scared.', [ch('У тебе є карта?', True, 's3', 'Добре питання.|Dobre pytanie.|Good question.'), ch('У тебе немає карта?', False, 's3', 'Треба «є карта» або «немає карти».|Trzeba „є карта” lub „немає карти”.|Use “є карта” or “немає карти”.')]),
 's3': step('Маккуїн: «Ні, у мене немає карти. Я бачу знак: містечко!»', 'Nie mam mapy. Widzę znak: miasteczko!|No map. I see a sign: a town!', 'Далеко світло.|Daleko światło.|A light far away.', [ch('Їдь туди повільно. Ми їдемо до тебе!', True, 'end_good', 'Чудово.|Świetnie.|Great.'), ch('Їдь швидко! Дуже швидко!', True, 'end_mid', 'Ой-ой…|Oj-oj…|Uh-oh…')]),
}, {'end_good': end(True, 'Кінцівка: Ми знайдемо тебе|Zakończenie: Znajdziemy cię|Ending: We\'ll find you', 'Маккуїн повільно їде до містечка. Він уже не такий наляканий: команда знає, де він.|Zygzak powoli jedzie do miasteczka. Już nie jest tak przestraszony: zespół wie, gdzie jest.|McQueen drives slowly to the town. He\'s less scared: the team knows where he is.'),
    'end_mid': end(True, 'Кінцівка: Як у фільмі|Zakończenie: Jak w filmie|Ending: Like the film', 'Маккуїн мчить у містечко… і влітає просто на головну вулицю. Ох! Далі — Радіатор-Спрінгз!|Zygzak pędzi do miasteczka… i wpada prosto na główną ulicę. Och! Dalej — Chłodnica Górska!|McQueen races into the town… right onto Main Street. Oh! Next: Radiator Springs!'),
    'end_bad': end(False, 'Кінцівка: Зв\'язок зник|Zakończenie: Brak zasięgu|Ending: Signal lost', 'Маккуїн тебе не зрозумів, і зв\'язок зник. Спробуй: «Я механік. Де ти?»|Zygzak cię nie zrozumiał. Spróbuj: „Я механік. Де ти?”|He didn\'t understand you. Try: “Я механік. Де ти?”')})
L.set('ПИШИ Й СКЛАДАЙ|PISZ I UKŁADAJ|WRITE AND BUILD', 'Запиши, що кричить Маккуїн у темряві.|Zapisz, co krzyczy Zygzak w ciemności.|Write what McQueen shouts in the dark.', 'Впиши й склади|Wpisz i ułóż|Type and build', [
 typ(g, 'Я загубився!', 'Zgubiłem się!|I\'m lost!'), order(g, ['У', 'мене', 'немає', 'карти.'], 'Nie mam mapy.|I have no map.'),
 typ(g, 'Тут так холодно.', 'Tu jest tak zimno.|It\'s so cold here.'), order(g, ['У', 'тебе', 'є', 'телефон?'], 'Masz telefon?|Do you have a phone?'),
 typ(g, 'Двері відчинені!', 'Drzwi są otwarte!|The door is open!'), order(g, ['Тут', 'нікого', 'немає.'], 'Nikogo tu nie ma.|Nobody is here.'),
 typ(g, 'Це помилка!', 'To błąd!|This is a mistake!'), order(g, ['Містечко!', 'Нарешті!'], 'Miasteczko! Nareszcie!|A town! Finally!'),
])
L.speak('Маку! Де ти? Я загубився!', 'Mack! Gdzie jesteś? Zgubiłem się!|Mack! Where are you? I\'m lost!')
L.speak('У мене немає карти, але в мене є друзі.', 'Nie mam mapy, ale mam przyjaciół.|I have no map, but I have friends.')
L.set('НІЧ У ПУСТЕЛІ · СЛОВА|NOC NA PUSTYNI · SŁOWA|DESERT NIGHT · WORDS', 'Слова уроку в нових ситуаціях.|Słowa lekcji w nowych sytuacjach.|Lesson words in new situations.', 'Вісім питань на слова|Osiem pytań|Eight word questions', [
 mc('Уночі на небі ____.', ['місяць', 'пісок', 'шум'], 0, 'Місяць = moon.|Księżyc.|Moon.', tag='word'),
 mc('Там, де тільки пісок, — ____.', ['пустеля', 'місто', 'причіп'], 0, 'Пустеля.|Pustynia.|Desert.', tag='word'),
 mc('Не знаєш, де ти. Ти ____.', ['загублений', 'гучний', 'яскравий'], 0, 'Загублений.|Zgubiony.|Lost.', tag='word'),
 mc('Протилежне до «гучно» — ____.', ['тихо', 'яскраво', 'холодно'], 0, 'Тихо.|Cicho.|Quietly.', tag='word'),
 mc('Світло машини вночі — це ____.', ['фари', 'двері', 'карти'], 0, 'Фари.|Reflektory.|Headlights.', tag='word'),
 mc('Дорога з шосе — це ____.', ['з\'їзд', 'місяць', 'шум'], 0, 'З\'їзд.|Zjazd.|Exit.', tag='word'),
 mc('Коли страшно, кричиш: «____!»', ['Допоможіть', 'Добраніч', 'Дякую'], 0, 'Допомога → допоможіть.|Pomocy!|Help!', tag='word'),
 mc('На дорозі стоїть ____: «Му-у!»', ['корова', 'карта', 'помилка'], 0, 'Корова.|Krowa.|Cow.', tag='word'),
])
L.final('ПОВІДОМЛЕННЯ КОМАНДІ|WIADOMOŚĆ DO ZESPOŁU|MESSAGE TO THE TEAM', 'Напиши команді, що сталося вночі (25+ слів): що робив Мак? що сталося з Маккуїном? що в нього є і чого немає? де він зараз?|Napisz po ukraińsku do zespołu, co się stało w nocy (25+ słów): co robił Mack? co się stało z Zygzakiem? co ma, a czego nie ma? gdzie jest teraz?|Write to the team in Ukrainian what happened at night (25+ words): what did Mack do? what happened to McQueen? what does he have/not have? where is he now?',
 'Мак спав… Маккуїн … У нього немає … Зараз він …', 25)
print(L.save('cars', 5))
