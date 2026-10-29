import sys; sys.path.insert(0, '/home/claude/work/std'); from lib import *
g = 'uk'; L = Lesson('201dd6c4-d3be-4682-aa65-551657ed0655', g)
gm = lambda q, o, a, e: mc(q, o, a, e, tag='gram'); wd = lambda q, o, a, e: mc(q, o, a, e, tag='word')
L.intro('ТВОЯ РОЛЬ · БОС АРКИ 1|TWOJA ROLA · BOSS ŁUKU 1|YOUR ROLE · ARC 1 BOSS', 'Кінець першої арки! Ти пройшов з Маккуїном усе: велику гонку, нічию, спонсорів, ніч у причепі й темну дорогу. Тепер доведи, що ти справжній механік команди.|Koniec pierwszego łuku! Przeszedłeś z Zygzakiem wszystko: wielki wyścig, remis, sponsorów, noc w przyczepie i ciemną drogę. Udowodnij, że jesteś prawdziwym mechanikiem zespołu.|End of Arc 1! You\'ve been through it all with McQueen: the big race, the tie, the sponsors, the night in the trailer and the dark road. Now prove you\'re a real crew member.')
L.ref(0)
L.match('СЛОВА АРКИ|SŁOWA ŁUKU|ARC WORDS', ['переможець=переможець/zwycięzca/winner', 'нічия=нічия/remis/tie', 'спонсор=спонсор/sponsor/sponsor', 'наліпка=наліпка/naklejka/sticker', 'двері=двері/drzwi/door'])
L.set('АРКА 1 · СЛОВА|ŁUK 1 · SŁOWA|ARC 1 · WORDS', 'Усі важливі слова першої арки.|Wszystkie ważne słowa pierwszego łuku.|All the key words of Arc 1.', 'Десять слів арки|Dziesięć słów łuku|Ten arc words', [
 wd('Маккуїн — червона гоночна ____.', ['машина', 'наліпка', 'стіна'], 0, 'Машина = car.|Auto.|Car.'),
 wd('Три машини на фініші разом — це ____.', ['нічия', 'аварія', 'крем'], 0, 'Нічия = tie.|Remis.|Tie.'),
 wd('Rust-eze — це ____ Маккуїна.', ['спонсор', 'брат', 'телевізор'], 0, 'Спонсор.|Sponsor.|Sponsor.'),
 wd('Бампер старий і ____.', ['іржавий', 'швидкий', 'гучний'], 0, 'Іржавий.|Zardzewiały.|Rusty.'),
 wd('Маккуїн любить свої ____ на стіні.', ['наліпки', 'двері', 'фари'], 0, 'Наліпки.|Naklejki.|Stickers.'),
 wd('Мак уночі дуже ____.', ['сонний', 'фіолетовий', 'новий'], 0, 'Сонний.|Senny.|Sleepy.'),
 wd('Чотири машини дуже ____.', ['яскраві', 'іржаві', 'тихі'], 0, 'Яскравий.|Jaskrawy.|Bright.'),
 wd('Двері причепа ____!', ['відчинені', 'сині', 'смішні'], 0, 'Відчинений.|Otwarty.|Open.'),
 wd('Маккуїн думає, що він ____.', ['переможець', 'брат', 'шум'], 0, 'Переможець.|Zwycięzca.|Winner.'),
 wd('Маккуїн не хоче бути ____.', ['другим', 'червоним', 'швидким'], 0, 'Другий.|Drugi.|Second.'),
])
L.intro('ПОВТОРЕННЯ ГРАМАТИКИ|POWTÓRKA GRAMATYKI|GRAMMAR REVIEW', 'Арка 1: Я гонщик (без «є») · мій/моя/моє/мої · цей/ця/це/ці і той/та/те/ті · у мене є / у мене немає + родовий.|Łuk 1: Я гонщик (bez „є”) · мій/моя/моє/мої · цей/той · у мене є / немає + dopełniacz.|Arc 1: Я гонщик (no “є”) · мій/моя/моє/мої · цей/той · у мене є / немає + genitive.')
L.set('АРКА 1 · ГРАМАТИКА|ŁUK 1 · GRAMATYKA|ARC 1 · GRAMMAR', 'Репліки з усієї арки.|Kwestie z całego łuku.|Lines from the whole arc.', 'Дванадцять реплік|Dwanaście kwestii|Twelve lines', [
 gm('«Я ____!»', ['переможець', 'є переможцем є', 'переможця'], 0, 'Без «є».|Bez „є”.|No “є”.'),
 gm('«Ти ____ механік.»', ['новий', 'нова', 'нові'], 0, 'Він: новий.|Męski.|Masculine.'),
 gm('«Це ____ мрія.»', ['мій', 'моя', 'моє'], 1, 'Мрія — вона.|Żeński.|Feminine.'),
 gm('«Тепер це ____ місце.»', ['мій', 'моя', 'моє'], 2, 'Місце — воно.|Nijaki.|Neuter.'),
 gm('«Ми ____ спонсори.»', ['твій', 'твоя', 'твої'], 2, 'Множина.|L. mnoga.|Plural.'),
 gm('«____ кубок новий» (поруч).', ['Цей', 'Ця', 'Це'], 0, 'Кубок — він.|Męski.|Masculine.'),
 gm('«____ дорога довга» (там).', ['Той', 'Та', 'Ті'], 1, 'Дорога — вона.|Żeński.|Feminine.'),
 gm('«Подивись на ____ наліпки!» (там).', ['ті', 'та', 'той'], 0, 'Множина.|L. mnoga.|Plural.'),
 gm('«У мене ____ телефону.»', ['немає', 'є', 'нема є'], 0, 'Немає + родовий.|Немає + dopełniacz.|Немає + genitive.'),
 gm('«У мене немає ____.»', ['карти', 'карта', 'карту'], 0, 'Родовий.|Dopełniacz.|Genitive.'),
 gm('«У тебе ____ телефон?»', ['є', 'немає', 'нікого'], 0, 'Є.|Є.|Є.'),
 gm('«Тут ____ немає.»', ['нікого', 'ніхто', 'нічия'], 0, 'Нікого немає.|Nikogo nie ma.|Nobody.'),
])
L.set('АРКА 1 · ІСТОРІЯ|ŁUK 1 · HISTORIA|ARC 1 · THE STORY', 'Що сталося в першій арці?|Co się stało w pierwszym łuku?|What happened in Arc 1?', 'Обери правду|Wybierz prawdę|Choose the truth', [
 tf(g, 'Перша гонка закінчилася нічиєю.', 'Pierwszy wyścig skończył się remisem.|The first race ended in a tie.', True, 'Три машини разом.|Trzy auta razem.|Three cars together.'),
 tf(g, 'Спонсор Маккуїна — Dinoco.', 'Sponsor Zygzaka to Dinoco.|McQueen\'s sponsor is Dinoco.', False, 'Його спонсор — Rust-eze.|Jego sponsor to Rust-eze.|His sponsor is Rust-eze.'),
 tf(g, 'Бригада механіків іде від Маккуїна.', 'Ekipa odchodzi od Zygzaka.|The crew leaves McQueen.', True, 'Так, і ти лишаєшся.|Tak, a ty zostajesz.|Yes, and you stay.'),
 tf(g, 'Мак везе Маккуїна до Каліфорнії.', 'Mack wiezie Zygzaka do Kalifornii.|Mack drives McQueen to California.', True, 'Так.|Tak.|Yes.'),
 tf(g, 'Уночі Мак не спить.', 'W nocy Mack nie śpi.|Mack doesn\'t sleep at night.', False, 'Він засинає за кермом.|Zasypia za kierownicą.|He falls asleep at the wheel.'),
 mc('Хто граються біля Мака на шосе?', ['Чотири яскраві машини', 'Король і Чік', 'Брати Rust-eze'], 0, 'Чотири машини.|Cztery auta.|Four cars.', 'Who plays tricks on Mack?|Kto robi żarty Mackowi?|Who plays tricks on Mack?'),
 mc('Чому Маккуїн у пустелі?', ['Поїхав за чужою вантажівкою', 'Хотів кави', 'Так сказав Король'], 0, 'Це помилка.|To błąd.|A mistake.', 'Why is McQueen in the desert?|Dlaczego Zygzak jest na pustyni?|Why is McQueen in the desert?'),
 mc('Що бачить Маккуїн у кінці арки?', ['Маленьке містечко', 'Стадіон', 'Гелікоптер'], 0, 'Містечко!|Miasteczko!|A small town!', 'What does McQueen see at the end?|Co widzi Zygzak na końcu?|What does McQueen see at the end?'),
])
L.reading('Історія першої арки: від стадіону до пустелі|Historia łuku 1: ze stadionu na pustynię|Arc 1: from the stadium to the desert', 'ЧИТАННЯ|CZYTANIE|READING', 'Прочитай історію арки й обери правильні слова.|Przeczytaj historię po ukraińsku i wybierz słowa.|Read the arc story in Ukrainian and choose the words.', [
 S('Великий стадіон. Тисячі фанатів.'),
 S('Блискавка Маккуїн — червона гоночна ____.', ['машина', 'стіна', 'кава'], 0),
 S('Він каже: «Я — ____».', ['швидкість', 'швидкий', 'швидко'], 0),
 S('Він дуже швидкий і дуже ____.', ['гордий', 'іржавий', 'тихий'], 0),
 S('На фініші три машини разом. Це ____.', ['нічия', 'помилка', 'мрія'], 0),
 S('Остання гонка буде в Каліфорнії.'),
 S('Спонсори Маккуїна — два смішні ____.', ['брати', 'знаки', 'фари'], 0),
 S('Їхня компанія ____.', ['маленька', 'багата', 'синя'], 0),
 S('Маккуїн мріє про ____ Dinoco.', ['синій', 'іржавий', 'тихий'], 0),
 S('Бригада механіків іде. Лишаєшся тільки ти й ____.', ['Мак', 'Король', 'Чік'], 0),
 S('Уночі Мак везе Маккуїна. На стінах причепа ____ наліпок.', ['багато', 'немає', 'нікого'], 0),
 S('Мак дуже ____.', ['сонний', 'новий', 'гучний'], 0),
 S('Він засинає за ____.', ['кермом', 'стіною', 'кавою'], 0),
 S('Чотири машини з гучною ____ жартують.', ['музикою', 'кавою', 'картою'], 0),
 S('Двері причепа відчиняються, і Маккуїн падає на ____.', ['дорогу', 'місяць', 'стіну'], 0),
 S('Він прокидається сам. У нього ____ карти.', ['немає', 'є', 'нікого'], 0),
 S('Він їде за чужою вантажівкою — це ____.', ['помилка', 'мрія', 'кава'], 0),
 S('Тепер він у пустелі. Пісок, кактуси, місяць.'),
 S('Нарешті він бачить ____.', ['містечко', 'стадіон', 'гелікоптер'], 0),
 S('Що там? Дізнаємося в другій арці!'),
], 'Арка 1 закінчилася в пустелі.|Łuk 1 skończył się na pustyni.|Arc 1 ends in the desert.')
L.quest('КВЕСТ: ДОВГА НІЧ|QUEST: DŁUGA NOC|QUEST: THE LONG NIGHT', 'Перепроживи всю ніч арки 1. Твої відповіді — українською — вирішують, як вона закінчиться.|Przeżyj jeszcze raz całą noc łuku 1. Twoje odpowiedzi po ukraińsku decydują o zakończeniu.|Relive the whole night of Arc 1. Your Ukrainian answers decide how it ends.', 'train', {
 's1': step('Маккуїн: «Ми — нічия? Ні! Я переможець!»', 'Remis? Nie! Jestem zwycięzcą!|A tie? No! I\'m the winner!', 'Стадіон після фінішу.|Stadion po mecie.|Stadium after the finish.', [ch('Це нічия. Буде ще гонка.', True, 's2', 'Так.|Tak.|Yes.'), ch('Ти є переможцем є.', False, 's2', 'Без «є»!|Bez „є”!|No “є”!')]),
 's2': step('Брати Rust-eze: «Ми твої спонсори!»', 'Jesteśmy twoimi sponsorami!|We\'re your sponsors!', 'Брати махають.|Bracia machają.|The brothers wave.', [ch('Привіт! Це наша команда.', True, 's3', 'Наша команда.|Наша команда.|Наша команда.'), ch('Привіт! Це наш команда.', False, 's3', 'Команда — вона: наша.|Żeński: наша.|Feminine: наша.')]),
 's3': step('Маккуїн: «Де моя бригада?»', 'Gdzie moja ekipa?|Where is my crew?', 'Трейлер порожній.|Przyczepa pusta.|Trailer empty.', [ch('Вони пішли. Але я тут.', True, 's4', 'Вірний!|Lojalny!|Loyal!'), ch('Тут нікого немає. Бувай!', False, 'end_bad', 'Ти теж пішов…|Też odszedłeś…|You left too…')]),
 's4': step('Мак: «Я такий сонний, малий…»', 'Jestem taki śpiący, mały…|I\'m so sleepy, kid…', 'Ніч на шосе.|Noc na autostradzie.|Night on the highway.', [ch('Маку, ось кава. Подивись на той знак — там кафе!', True, 's5', 'Добре.|Dobrze.|Good.'), ch('Ця кафе там.', False, 's5', 'Треба «те кафе».|Trzeba „те кафе”.|Use “те кафе”.')]),
 's5': step('Маккуїн (у пустелі): «У мене немає карти!»', 'Nie mam mapy!|I have no map!', 'Дзвінок у темряві.|Telefon w ciemności.|A call in the dark.', [ch('У мене є карта. Їдь до містечка!', True, 's6', 'Чудово.|Świetnie.|Great.'), ch('У мене немає карта.', False, 's6', 'Немає карти.|Немає карти.|Немає карти.')]),
 's6': step('Маккуїн: «Містечко! Нарешті! Я їду швидко!»', 'Miasteczko! Jadę szybko!|A town! I\'m going fast!', 'Світло містечка.|Światła miasteczka.|The town lights.', [ch('Ні! Їдь повільно!', True, 'end_good', 'Мудро.|Mądrze.|Wise.'), ch('Так! Швидше!', True, 'end_mid', 'Ой…|Oj…|Uh-oh…')]),
}, {'end_good': end(True, 'Кінцівка: Справжній механік|Zakończenie: Prawdziwy mechanik|Ending: A Real Mechanic', 'Маккуїн повільно в\'їжджає в містечко. Він каже: «Дякую, бригадо». Арку 1 пройдено!|Zygzak powoli wjeżdża do miasteczka. Mówi: „Дякую, бригадо”. Łuk 1 ukończony!|McQueen slowly enters the town. He says: “Дякую, бригадо”. Arc 1 complete!'),
    'end_mid': end(True, 'Кінцівка: Як у фільмі|Zakończenie: Jak w filmie|Ending: Like the film', 'Маккуїн мчить на головну вулицю… Хаос! Але це вже друга арка.|Zygzak pędzi na główną ulicę… Chaos! Ale to już łuk 2.|McQueen races onto Main Street… Chaos! But that\'s Arc 2.'),
    'end_bad': end(False, 'Кінцівка: Без команди|Zakończenie: Bez zespołu|Ending: No team', 'Маккуїн лишився зовсім сам. Спробуй ще — механік не кидає свою машину.|Zygzak został całkiem sam. Spróbuj jeszcze — mechanik nie zostawia swojego auta.|McQueen is all alone. Try again — a mechanic never leaves his car.')})
L.set('ПИШИ Й СКЛАДАЙ|PISZ I UKŁADAJ|WRITE AND BUILD', 'Головні репліки першої арки.|Główne kwestie łuku 1.|Key lines of Arc 1.', 'Десять реплік|Dziesięć kwestii|Ten lines', [
 typ(g, 'Я — швидкість.', 'Jestem szybkością.|I am speed.', ['Я швидкість.']), order(g, ['Це', 'нічия!'], 'To remis!|It\'s a tie!'),
 typ(g, 'Ми твої спонсори!', 'Jesteśmy twoimi sponsorami!|We are your sponsors!'), order(g, ['Це', 'моя', 'мрія.'], 'To moje marzenie.|This is my dream.'),
 typ(g, 'Це мій кубок.', 'To mój puchar.|This is my cup.'), order(g, ['Той', 'кубок', 'старий.'], 'Tamten puchar jest stary.|That cup is old.'),
 typ(g, 'Мак спить!', 'Mack śpi!|Mack is asleep!'), order(g, ['Двері', 'відчинені!'], 'Drzwi są otwarte!|The door is open!'),
 typ(g, 'Я загубився!', 'Zgubiłem się!|I\'m lost!'), order(g, ['У', 'мене', 'немає', 'карти.'], 'Nie mam mapy.|I have no map.'),
])
L.speak('Я — швидкість! Це нічия, але в Каліфорнії я переможу!', 'Jestem szybkością! To remis, ale w Kalifornii wygram!|I am speed! It\'s a tie, but in California I\'ll win!')
L.final('ЗВІТ МЕХАНІКА · АРКА 1|RAPORT MECHANIKA · ŁUK 1|MECHANIC\'S REPORT · ARC 1', 'Напиши звіт про першу арку (30+ слів): хто такий Маккуїн? що сталося на гонці? хто спонсори? що сталося вночі? де Маккуїн тепер?|Napisz po ukraińsku raport o łuku 1 (30+ słów): kim jest Zygzak? co się stało na wyścigu? kim są sponsorzy? co się stało w nocy? gdzie jest teraz Zygzak?|Write a report on Arc 1 in Ukrainian (30+ words): who is McQueen? what happened at the race? who are the sponsors? what happened at night? where is McQueen now?',
 'Маккуїн — … На гонці … Наші спонсори … Уночі … Тепер він …', 30)
print(L.save('cars', 6))
