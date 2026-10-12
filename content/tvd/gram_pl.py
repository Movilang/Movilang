# Wersja kursu dla uczących się POLSKIEGO. Gramatyka polska B1→B2 + dziennik.
# Każde zadanie: (pytanie, [opcje], poprawna, [(uk, pl, en) dla każdej opcji], (tip uk, pl, en))
G = {}
D = {}  # dziennik: (polecenie po polsku, min. słów, (tip uk, pl, en))
T = {}  # tytuł gramatyki: (uk, pl, en)

T[1] = ("Теперішній час: -ę/-esz, -am/-asz", "Czas teraźniejszy: koniugacje -ę/-esz, -am/-asz", "Present tense: -ę/-esz and -am/-asz verbs")
G[1] = [
 ("Elena codziennie ____ w pamiętniku.", ["pisze", "piszę", "pisać"], 0,
  [("Так! Вона (ona) → pisze. Дієслово pisać: piszę, piszesz, pisze.", "Tak! Ona → pisze. Odmiana: piszę, piszesz, pisze.", "Yes! Ona (she) → pisze. Pisać: piszę, piszesz, pisze."),
   ("Piszę — це «я пишу», а тут вона.", "Piszę to forma „ja”, a tu chodzi o nią.", "Piszę is the “I” form; here it's “she”."),
   ("Pisać — інфінітив, потрібна особова форма.", "Pisać to bezokolicznik — potrzebna forma osobowa.", "Pisać is the infinitive; you need a person form.")],
  ("Pisać — дієслово з чергуванням s → sz: piszę, piszesz.", "Pisać ma wymianę s → sz: piszę, piszesz.", "Pisać changes s → sz: piszę, piszesz.")),
 ("Bonnie: — Patrz! Nowy na ciebie ____!", ["patrzy", "patrzę", "patrzą"], 0,
  [("Так! Він (on) → patrzy.", "Tak! On → patrzy.", "Yes! He → patrzy."),
   ("Patrzę — «я дивлюся».", "Patrzę to „ja patrzę”.", "Patrzę means “I look”."),
   ("Patrzą — «вони дивляться», а новенький один.", "Patrzą to „oni”, a nowy jest jeden.", "Patrzą is “they”, but the new guy is one person.")],
  ("Польська не має окремого «тривалого» часу: patrzy = дивиться / дивиться зараз.", "Polski nie ma osobnego czasu „ciągłego”: patrzy = patrzy teraz albo zawsze.", "Polish has no separate continuous tense: patrzy = looks / is looking.")),
]
D[1] = ("Napisz wpis Eleny wieczorem po pierwszym dniu szkoły (40+ słów). Użyj czasu teraźniejszego: co robisz, co czujesz, kim jest nowy chłopak.", 40,
 ("Пиши від імені Олени. Почни з «Drogi pamiętniku, dziś…».", "Pisz jako Elena. Zacznij od „Drogi pamiętniku, dziś…”.", "Write as Elena. Start with “Drogi pamiętniku, dziś…”."))

T[2] = ("Минулий час і рід: był / była", "Czas przeszły i rodzaj: był / była", "Past tense and gender: był / była")
G[2] = [
 ("Wczoraj Elena ____ w szpitalu u Vicki.", ["była", "był", "było"], 0,
  [("Так! Олена — жінка → była.", "Tak! Elena to kobieta → była.", "Yes! Elena is female → była."),
   ("Był — чоловічий рід.", "Był to rodzaj męski.", "Był is masculine."),
   ("Było — середній рід (np. dziecko było).", "Było to rodzaj nijaki (np. dziecko było).", "Było is neuter (e.g. dziecko było).")],
  ("У минулому часі польське дієслово змінюється за родом: był / była / było.", "W czasie przeszłym czasownik zmienia się według rodzaju: był / była / było.", "In the past tense Polish verbs change by gender: był / była / było.")),
 ("Damon: — Stefan ____ zawsze nudnym bratem.", ["był", "była", "byli"], 0,
  [("Так! Стефан — він → był.", "Tak! Stefan → był.", "Yes! Stefan → był."),
   ("Była — для жінок.", "Była — dla kobiet.", "Była is for women."),
   ("Byli — множина.", "Byli to liczba mnoga.", "Byli is plural.")],
  ("Запам'ятай: on był, ona była, oni byli, one były.", "Zapamiętaj: on był, ona była, oni byli, one były.", "Remember: on był, ona była, oni byli, one były.")),
]
D[2] = ("Opisz noc komety (45+ słów) w czasie przeszłym. Kto gdzie był, co robił? Pamiętaj o rodzaju: Elena była, Damon był.", 45,
 ("Стеж за закінченнями роду: -ł / -ła.", "Pilnuj końcówek rodzaju: -ł / -ła.", "Watch the gender endings: -ł / -ła."))

T[3] = ("Вид дієслова: robić / zrobić", "Aspekt: robić / zrobić", "Verb aspect: robić / zrobić")
G[3] = [
 ("Stefan ____ Elenie wisiorek z werbeną. (jeden raz, skończone)", ["dał", "dawał", "daje"], 0,
  [("Так! Одна завершена дія → доконаний вид: dał.", "Tak! Jednorazowa, skończona czynność → aspekt dokonany: dał.", "Yes! A single finished action → perfective: dał."),
   ("Dawał — процес або повторення («давав»).", "Dawał to proces albo powtarzanie.", "Dawał is a process or repetition."),
   ("Daje — теперішній час.", "Daje to czas teraźniejszy.", "Daje is present tense.")],
  ("Пара видів: dawać (недоконаний) / dać (доконаний).", "Para aspektowa: dawać (niedokonany) / dać (dokonany).", "Aspect pair: dawać (imperfective) / dać (perfective).")),
 ("Elena ____ cheerleading po śmierci rodziców i już nie wróciła.", ["rzuciła", "rzucała", "rzuca"], 0,
  [("Так! Результат: кинула і не повернулася → rzuciła.", "Tak! Rezultat: rzuciła i nie wróciła.", "Yes! A result: she quit and didn't return → rzuciła."),
   ("Rzucała — «кидала» багато разів або довго.", "Rzucała — wiele razy albo długo.", "Rzucała means many times or for a while."),
   ("Rzuca — теперішній час.", "Rzuca to czas teraźniejszy.", "Rzuca is present tense.")],
  ("Доконаний вид часто відповідає англійському Present Perfect / результату.", "Aspekt dokonany często wyraża rezultat.", "The perfective often expresses a result, like the English Present Perfect.")),
]
D[3] = ("Napisz pamiętnik Stefana po meczu (45+ słów). Użyj co najmniej trzech czasowników dokonanych (zrobił, dał, zabił…) i dwóch niedokonanych.", 45,
 ("Доконаний — результат, недоконаний — процес.", "Dokonany — rezultat, niedokonany — proces.", "Perfective = result, imperfective = process."))

T[4] = ("Strona bierna: zostać + дієприкметник", "Strona bierna: zostać / być + imiesłów", "Passive: zostać / być + participle")
G[4] = [
 ("Miasto ____ założone w latach 60. XIX wieku.", ["zostało", "został", "założyło"], 0,
  [("Так! Miasto — середній рід → zostało założone.", "Tak! Miasto — rodzaj nijaki → zostało założone.", "Yes! Miasto is neuter → zostało założone."),
   ("Został — чоловічий рід (np. dom został zbudowany).", "Został to rodzaj męski (np. dom został zbudowany).", "Został is masculine (e.g. dom został zbudowany)."),
   ("Założyło — активний стан: місто когось заснувало.", "Założyło to strona czynna: miasto coś założyło.", "Założyło is active: the town founded something.")],
  ("Пасив: zostać + дієприкметник, узгоджений за родом.", "Strona bierna: zostać + imiesłów zgodny z rodzajem.", "Passive: zostać + participle agreeing in gender.")),
 ("W zeszłym miesiącu dwie osoby ____ zabite.", ["zostały", "został", "zostało"], 0,
  [("Так! Osoby — множина жіночого роду → zostały zabite.", "Tak! Osoby — liczba mnoga → zostały zabite.", "Yes! Osoby is plural → zostały zabite."),
   ("Został — однина.", "Został — liczba pojedyncza.", "Został is singular."),
   ("Zostało — однина середнього роду.", "Zostało — rodzaj nijaki, liczba pojedyncza.", "Zostało is neuter singular.")],
  ("Мова протоколу і Ради засновників любить пасив.", "Język protokołu i Rady Założycieli lubi stronę bierną.", "The Council's official language loves the passive.")),
]
D[4] = ("Napisz krótką historię Mystic Falls do programu balu założycieli (45+ słów). Użyj strony biernej co najmniej trzy razy: zostało założone, zostały zbudowane…", 45,
 ("Важливо, що сталося, а не хто зробив.", "Ważne jest, co się stało, a nie kto to zrobił.", "What happened matters more than who did it."))

T[6] = ("Модальні: musieć / nie wolno / nie trzeba", "Czasowniki modalne: musieć / nie wolno / nie trzeba", "Modals: musieć / nie wolno / nie trzeba")
G[6] = [
 ("Stefan: — Damonowi ____ wychodzić z piwnicy. To zbyt niebezpieczne.", ["nie wolno", "nie trzeba", "musi"], 0,
  [("Так! Nie wolno = заборона.", "Tak! Nie wolno = zakaz.", "Yes! Nie wolno = forbidden."),
   ("Nie trzeba = не обов'язково, а тут заборона.", "Nie trzeba = nie ma potrzeby, a tu jest zakaz.", "Nie trzeba = not necessary, but this is a ban."),
   ("Musi — «мусить вийти», протилежний зміст.", "Musi — odwrotne znaczenie.", "Musi means he has to — the opposite.")],
  ("nie wolno = не можна; nie trzeba = не треба (але можна).", "nie wolno = zakaz; nie trzeba = brak obowiązku.", "nie wolno = not allowed; nie trzeba = not necessary.")),
 ("Na myjni ____ płacić gotówką — można też kartą.", ["nie trzeba", "nie wolno", "trzeba"], 0,
  [("Так! Є інший варіант → nie trzeba.", "Tak! Jest inna opcja → nie trzeba.", "Yes! There's another option → nie trzeba."),
   ("Ніхто не забороняє готівку.", "Nikt nie zabrania gotówki.", "Nobody bans cash."),
   ("Trzeba — обов'язково, протилежне.", "Trzeba — obowiązek, odwrotnie.", "Trzeba means obligatory — the opposite.")],
  ("Після «trzeba / nie wolno» — інфінітив.", "Po „trzeba / nie wolno” — bezokolicznik.", "After trzeba / nie wolno use the infinitive.")),
]
D[6] = ("Napisz zasady domu Salvatore'ów dla gościa (45+ słów): co trzeba, czego nie wolno, czego nie trzeba robić. Np. Nie wolno schodzić do piwnicy.", 45,
 ("Додай 1–2 правила про вербену!", "Dodaj 1–2 zasady o werbenie!", "Add 1–2 rules about vervain!"))

T[7] = ("Послідовність у минулому: zanim / kiedy", "Kolejność w przeszłości: zanim / kiedy + aspekt", "Order of past events: zanim / kiedy + aspect")
G[7] = [
 ("Zanim Katherine ____ do Mystic Falls, bracia byli przyjaciółmi.", ["przyjechała", "przyjeżdżała", "przyjedzie"], 0,
  [("Так! Одна завершена подія → доконаний вид.", "Tak! Jedno zakończone wydarzenie → aspekt dokonany.", "Yes! One finished event → perfective."),
   ("Przyjeżdżała — багато разів.", "Przyjeżdżała — wiele razy.", "Przyjeżdżała means many times."),
   ("Przyjedzie — майбутнє.", "Przyjedzie — przyszłość.", "Przyjedzie is future.")],
  ("Польська не має Past Perfect: порядок показують zanim / kiedy і вид.", "Polski nie ma Past Perfect: kolejność pokazują zanim / kiedy i aspekt.", "Polish has no Past Perfect: zanim / kiedy and aspect show the order.")),
 ("Kiedy Stefan ____ prawdę, Elena już znalazła zdjęcie.", ["powiedział", "mówił", "powie"], 0,
  [("Так! Завершена подія → powiedział.", "Tak! Zakończone wydarzenie → powiedział.", "Yes! A finished event → powiedział."),
   ("Mówił — процес «говорив».", "Mówił — proces.", "Mówił is a process."),
   ("Powie — майбутнє.", "Powie — przyszłość.", "Powie is future.")],
  ("Слово «już» підказує, що одна дія відбулася раніше.", "Słowo „już” podpowiada, że jedna czynność była wcześniej.", "“Już” shows one action came earlier.")),
]
D[7] = ("Opowiedz historię z 1864 roku tak, jak usłyszała ją Elena (50+ słów). Użyj zanim, kiedy, potem i czasowników dokonanych.", 50,
 ("Модель: Zanim przyjechała, byli… Potem…", "Model: Zanim przyjechała, byli… Potem…", "Pattern: Zanim przyjechała, byli… Potem…"))

T[8] = ("Реальна умова: jeśli + майбутній час", "Warunek realny: jeśli + czas przyszły", "Real condition: jeśli + future")
G[8] = [
 ("Jeśli Vicki ____ blisko ludzi, straci kontrolę.", ["zostanie", "zostaje", "zostałaby"], 0,
  [("Так! Jeśli + майбутній доконаний: zostanie.", "Tak! Jeśli + czas przyszły dokonany: zostanie.", "Yes! Jeśli + perfective future: zostanie."),
   ("Zostaje — теперішній, звучить як звичка.", "Zostaje — teraźniejszy, brzmi jak nawyk.", "Zostaje is present; it sounds like a habit."),
   ("Zostałaby — умовний спосіб, для нереального.", "Zostałaby — tryb przypuszczający, dla nierealnych sytuacji.", "Zostałaby is conditional — for unreal situations.")],
  ("На відміну від англійської, після jeśli вживаємо майбутній час.", "Inaczej niż w angielskim: po jeśli używamy czasu przyszłego.", "Unlike English, Polish uses the future after jeśli.")),
 ("Jeśli się ____, ktoś zginie.", ["pośliźniesz", "pośliznąłeś", "poślizgnąć"], 0,
  [("Так! Jeśli + майбутній: pośliźniesz.", "Tak! Jeśli + przyszły: pośliźniesz.", "Yes! Jeśli + future: pośliźniesz."),
   ("Минулий час тут не пасує.", "Czas przeszły nie pasuje.", "The past doesn't fit."),
   ("Інфінітив — неповне речення.", "Bezokolicznik — zdanie niepełne.", "The infinitive leaves the sentence incomplete.")],
  ("Обидві частини — у майбутньому часі.", "Obie części — w czasie przyszłym.", "Both parts are in the future.")),
]
D[8] = ("Napisz pamiętnik Eleny po Halloween (50+ słów). Użyj co najmniej trzech zdań z jeśli: Jeśli Jeremy sobie przypomni…, Jeśli powiem Mattowi…", 50,
 ("Реальні наслідки: що буде, якщо правда випливе.", "Realne skutki: co będzie, jeśli prawda wyjdzie na jaw.", "Real consequences: what happens if the truth comes out."))

T[9] = ("Умовний спосіб: gdybym był…, byłbym…", "Tryb przypuszczający: gdybym był…, byłbym…", "Conditional mood: gdybym był…, byłbym…")
G[9] = [
 ("Stefan marzy: — Gdybym znowu ____ człowiekiem, zestarzałbym się z tobą.", ["był", "jestem", "będę"], 0,
  [("Так! Gdybym + минулий час: gdybym był.", "Tak! Gdybym + forma przeszła: gdybym był.", "Yes! Gdybym + past form: gdybym był."),
   ("Jestem — реальність, а Стефан мріє.", "Jestem — rzeczywistość, a Stefan marzy.", "Jestem is reality, but Stefan is dreaming."),
   ("Будущий час після gdyby не вживається.", "Po gdyby nie używa się czasu przyszłego.", "The future isn't used after gdyby.")],
  ("gdy + by + особа: gdybym, gdybyś, gdyby.", "gdy + by + końcówka osoby: gdybym, gdybyś, gdyby.", "gdy + by + person ending: gdybym, gdybyś, gdyby.")),
 ("Gdybym żyła wiecznie, ____ cały świat.", ["zwiedziłabym", "zwiedzę", "zwiedzałam"], 0,
  [("Так! Наслідок: -łabym (жіночий рід).", "Tak! Skutek: -łabym (forma żeńska).", "Yes! The result: -łabym (feminine)."),
   ("Zwiedzę — реальне майбутнє.", "Zwiedzę — realna przyszłość.", "Zwiedzę is a real future."),
   ("Zwiedzałam — минуле.", "Zwiedzałam — przeszłość.", "Zwiedzałam is past.")],
  ("Жінка: byłabym, zrobiłabym; чоловік: byłbym, zrobiłbym.", "Kobieta: byłabym, zrobiłabym; mężczyzna: byłbym, zrobiłbym.", "Female: byłabym; male: byłbym.")),
]
D[9] = ("Lexi pyta: „Gdybyś była nieśmiertelna, co byś robiła?” Odpowiedz w pamiętniku (50+ słów). Użyj trybu przypuszczającego co najmniej cztery razy.", 50,
 ("Gdybym był(a)… / Zrobił(a)bym… — мрій сміливо.", "Gdybym był(a)… / Zrobił(a)bym… — marz odważnie.", "Gdybym był(a)… / Zrobił(a)bym… — dream boldly."))

T[10] = ("Непряма мова: powiedział, że…", "Mowa zależna: powiedział, że…", "Reported speech: powiedział, że…")
G[10] = [
 ("Alaric: „Jestem waszym nowym nauczycielem.” → Alaric powiedział, że ____ naszym nowym nauczycielem.", ["jest", "był", "będzie"], 0,
  [("Так! У польській час не зсувається: mówi, że jest.", "Tak! W polskim czas się nie przesuwa: powiedział, że jest.", "Yes! Polish doesn't shift tense: powiedział, że jest."),
   ("Był — означало б, що вже не вчитель.", "Był — znaczyłoby, że już nim nie jest.", "Był would mean he isn't anymore."),
   ("Будущий час змінює зміст.", "Czas przyszły zmienia sens.", "The future changes the meaning.")],
  ("На відміну від англійської: без зсуву часів, змінюються лише особи.", "Inaczej niż w angielskim: bez przesunięcia czasów, zmieniają się tylko osoby.", "Unlike English: no tense shift, only the person changes.")),
 ("Bonnie: „Ciągle śni mi się ten sen.” → Bonnie powiedziała, że ciągle ____ się jej ten sen.", ["śni", "śnił", "śniła"], 0,
  [("Так! Той самий час: śni.", "Tak! Ten sam czas: śni.", "Yes! Same tense: śni."),
   ("Śnił — минуле, не потрібно.", "Śnił — przeszły, niepotrzebny.", "Śnił is past — not needed."),
   ("Śniła — ще й не той рід (sen — чоловічий).", "Śniła — do tego zły rodzaj (sen jest męski).", "Śniła also has the wrong gender (sen is masculine).")],
  ("Змінюй особу: mi → jej, mój → jej.", "Zmieniaj osobę: mi → jej, mój → jej.", "Change the person: mi → jej, mój → jej.")),
]
D[10] = ("Opowiedz, co różne osoby powiedziały w tym tygodniu (50+ słów): Alaric powiedział, że…, Bonnie powiedziała mi, że…, Damon przyznał, że…", 50,
 ("Пам'ятай: у польській час після że не зсувається.", "Pamiętaj: po że czas się nie przesuwa.", "Remember: no tense shift after że."))

T[12] = ("Припущення: na pewno / chyba / nie może być", "Przypuszczenia: na pewno / chyba / to nie może być", "Guessing: na pewno / chyba / to nie może być")
G[12] = [
 ("Ofiary nie mają krwi, a Logan zaginął. To ____ Logan.", ["na pewno", "na pewno nie", "nigdy"], 0,
  [("Так! Сильні докази → na pewno (напевно).", "Tak! Mocne dowody → na pewno.", "Yes! Strong evidence → na pewno."),
   ("Na pewno nie — протилежний висновок.", "Na pewno nie — odwrotny wniosek.", "Na pewno nie is the opposite conclusion."),
   ("Nigdy — «ніколи», не про припущення.", "Nigdy nie wyraża przypuszczenia.", "Nigdy isn't a guess.")],
  ("na pewno = напевно; chyba = мабуть; to nie może być = не може бути.", "na pewno = pewność; chyba = przypuszczenie; to nie może być = niemożliwe.", "na pewno = surely; chyba = probably; to nie może być = impossible.")),
 ("Jenna widziała Logana. „To nie ____ być on! On nie żyje!”", ["może", "musi", "chce"], 0,
  [("Так! Nie może być = неможливо.", "Tak! Nie może być = to niemożliwe.", "Yes! Nie może być = impossible."),
   ("Nie musi — «не обов'язково».", "Nie musi — nie ma obowiązku.", "Nie musi means not necessarily."),
   ("Chce — «хоче», не той зміст.", "Chce — inne znaczenie.", "Chce means wants — wrong meaning.")],
  ("«To nie może być prawda!» — фраза шокованої людини.", "„To nie może być prawda!” — zdanie zszokowanej osoby.", "“To nie może być prawda!” — a shocked person's line.")),
]
D[12] = ("Napisz pamiętnik Eleny po znalezieniu zdjęcia (50+ słów). Użyj na pewno, chyba, może i to nie może być co najmniej cztery razy.", 50,
 ("Мова детектива і мова сумнівів.", "Język detektywa i język wątpliwości.", "The language of detectives and doubt."))

T[13] = ("Непрямі питання: czy / gdzie / dlaczego", "Pytania zależne: czy / gdzie / dlaczego", "Indirect questions: czy / gdzie / dlaczego")
G[13] = [
 ("Elena: „Dokąd jedziemy?” → Możesz mi powiedzieć, ____ jedziemy?", ["dokąd", "czy", "że"], 0,
  [("Так! Питальне слово зберігається: dokąd.", "Tak! Słowo pytające zostaje: dokąd.", "Yes! The question word stays: dokąd."),
   ("Czy — для питань так/ні.", "Czy — dla pytań tak/nie.", "Czy is for yes/no questions."),
   ("Że — для тверджень, не для питань.", "Że — dla twierdzeń, nie pytań.", "Że is for statements, not questions.")],
  ("Порядок слів у польській не змінюється — лише сполучник.", "Szyk w polskim się nie zmienia — tylko spójnik.", "Polish word order doesn't change — only the linking word.")),
 ("„Czy jestem adoptowana?” → Chcę wiedzieć, ____ jestem adoptowana.", ["czy", "że", "co"], 0,
  [("Так! Питання так/ні → czy.", "Tak! Pytanie tak/nie → czy.", "Yes! A yes/no question → czy."),
   ("Że — тоді це твердження, а не питання.", "Że — wtedy to stwierdzenie.", "Że turns it into a statement."),
   ("Co — «що», не той тип питання.", "Co — inne pytanie.", "Co is a different kind of question.")],
  ("czy = англійське if/whether, українське «чи».", "czy = angielskie if/whether.", "czy = English if/whether.")),
]
D[13] = ("Napisz listę pytań, które Elena chce zadać rodzinie (50+ słów). Użyj pytań zależnych: Chcę wiedzieć, kto…, Zastanawiam się, dlaczego…, Czy ktoś mi powie, gdzie…", 50,
 ("Непрямі питання звучать м'якше.", "Pytania zależne brzmią łagodniej.", "Indirect questions sound softer."))

T[14] = ("Звички минулого: kiedyś + недоконаний вид", "Nawyki z przeszłości: kiedyś + aspekt niedokonany", "Past habits: kiedyś + imperfective")
G[14] = [
 ("Stefan: — W latach 50. co sobotę ____ do tej muzyki.", ["tańczyłem", "zatańczyłem", "zatańczę"], 0,
  [("Так! Повторювана дія → недоконаний: tańczyłem.", "Tak! Powtarzana czynność → niedokonany: tańczyłem.", "Yes! A repeated action → imperfective: tańczyłem."),
   ("Zatańczyłem — один раз.", "Zatańczyłem — jeden raz.", "Zatańczyłem means once."),
   ("Zatańczę — майбутнє.", "Zatańczę — przyszłość.", "Zatańczę is future.")],
  ("«co sobotę, zawsze, kiedyś» → недоконаний вид.", "„co sobotę, zawsze, kiedyś” → aspekt niedokonany.", "“every Saturday, always, used to” → imperfective.")),
 ("Kiedyś ludzie ____ się co tydzień na tańce.", ["stroili", "wystroili", "wystroją"], 0,
  [("Так! Звичка → stroili.", "Tak! Nawyk → stroili.", "Yes! A habit → stroili."),
   ("Wystroili — один випадок.", "Wystroili — jeden raz.", "Wystroili is one occasion."),
   ("Wystroją — майбутнє.", "Wystroją — przyszłość.", "Wystroją is future.")],
  ("Kiedyś = англійське used to.", "Kiedyś = angielskie used to.", "Kiedyś works like English used to.")),
]
D[14] = ("Napisz wspomnienie Stefana o latach 50. (50+ słów). Użyj kiedyś, zawsze, co tydzień i czasowników niedokonanych.", 50,
 ("Недоконаний вид — серце спогадів.", "Aspekt niedokonany to serce wspomnień.", "The imperfective is the heart of memories."))

T[15] = ("Умовний минулий: gdyby nie…, nie byłoby…", "Tryb przypuszczający o przeszłości: gdyby nie…", "Past unreal: gdyby nie…")
G[15] = [
 ("Gdyby założyciele nie ____ planu, wampiry nie zostałyby złapane.", ["odkryli", "odkrywają", "odkryją"], 0,
  [("Так! Gdyby + минулий час: odkryli.", "Tak! Gdyby + czas przeszły: odkryli.", "Yes! Gdyby + past form: odkryli."),
   ("Теперішній після gdyby не вживається.", "Po gdyby nie ma czasu teraźniejszego.", "No present after gdyby."),
   ("Майбутній після gdyby не вживається.", "Po gdyby nie ma czasu przyszłego.", "No future after gdyby.")],
  ("Польська часто використовує ту саму форму для теперішньої і минулої нереальності; контекст робить решту.", "Polski używa tej samej formy dla nierealnej teraźniejszości i przeszłości; resztę mówi kontekst.", "Polish uses one form for unreal present and past; context does the rest.")),
 ("Gdyby Katherine nie przyjechała, bracia ____ normalnie.", ["żyliby", "żyją", "będą żyć"], 0,
  [("Так! Наслідок: -liby.", "Tak! Skutek: -liby.", "Yes! The result: -liby."),
   ("Żyją — реальність.", "Żyją — rzeczywistość.", "Żyją is reality."),
   ("Майбутнє не пасує.", "Przyszłość nie pasuje.", "The future doesn't fit.")],
  ("Граматика жалю: gdyby nie… — якби не…", "Gramatyka żalu: gdyby nie…", "The grammar of regret: gdyby nie…")),
]
D[15] = ("Napisz o roku 1864 i o dziś (50+ słów). Użyj gdyby co najmniej trzy razy: Gdyby założyciele nie…, Gdyby Katherine…, Damon by…", 50,
 ("У Містик Фоллс жалю вистачає.", "W Mystic Falls żalu nie brakuje.", "Mystic Falls has plenty of regret."))

T[17] = ("Майбутній: zrobię / będę robić / zaraz", "Czas przyszły: zrobię / będę robić / zaraz", "Future: zrobię / będę robić / zaraz")
G[17] = [
 ("Damon: — Dziś w nocy ____ Katherine z grobowca.", ["wyciągnę", "będę wyciągać", "wyciągałem"], 0,
  [("Так! Одна завершена дія в майбутньому → доконаний: wyciągnę.", "Tak! Jedna zakończona czynność → dokonany: wyciągnę.", "Yes! One completed future action → perfective: wyciągnę."),
   ("Będę wyciągać — процес, без результату.", "Będę wyciągać — proces, bez rezultatu.", "Będę wyciągać is a process without a result."),
   ("Wyciągałem — минуле.", "Wyciągałem — przeszłość.", "Wyciągałem is past.")],
  ("Доконане майбутнє — простою формою: zrobię.", "Przyszły dokonany — forma prosta: zrobię.", "Perfective future is one word: zrobię.")),
 ("Grobowiec ____ się otworzy!", ["zaraz", "wczoraj", "kiedyś"], 0,
  [("Так! Zaraz = от-от.", "Tak! Zaraz = za chwilę.", "Yes! Zaraz = any moment."),
   ("Wczoraj — минуле.", "Wczoraj — przeszłość.", "Wczoraj is past."),
   ("Kiedyś — колись (невизначено).", "Kiedyś — nieokreślona przyszłość lub przeszłość.", "Kiedyś is vague.")],
  ("zaraz + майбутній = англійське be about to.", "zaraz + czas przyszły = angielskie be about to.", "zaraz + future = English be about to.")),
]
D[17] = ("Napisz pamiętnik Bonnie po pogrzebie (50+ słów). Użyj czasu przyszłego dokonanego i niedokonanego: czego nigdy więcej nie zrobi, co będzie robić teraz, co zaraz się zmieni.", 50,
 ("Три відтінки майбутнього.", "Trzy odcienie przyszłości.", "Three shades of the future."))

T[18] = ("Підрядні означальні: który / która / którego", "Zdania względne: który / która / którego", "Relative clauses: który / która / którego")
G[18] = [
 ("Isobel była badaczką, ____ badała miejscowy folklor.", ["która", "który", "które"], 0,
  [("Так! Badaczka — жіночий рід → która.", "Tak! Badaczka — rodzaj żeński → która.", "Yes! Badaczka is feminine → która."),
   ("Który — чоловічий рід.", "Który — rodzaj męski.", "Który is masculine."),
   ("Które — середній рід або множина.", "Które — rodzaj nijaki albo liczba mnoga.", "Które is neuter or plural.")],
  ("Który узгоджується з іменником за родом і числом.", "Który zgadza się z rzeczownikiem w rodzaju i liczbie.", "Który agrees with its noun in gender and number.")),
 ("Alaric to mężczyzna, ____ żona zaginęła.", ["którego", "który", "której"], 0,
  [("Так! «чия дружина» → którego (родовий відмінок).", "Tak! „czyja żona” → którego (dopełniacz).", "Yes! “whose wife” → którego (genitive)."),
   ("Który — називний, тут не пасує.", "Który — mianownik, nie pasuje.", "Który is nominative — doesn't fit."),
   ("Której — жіночий рід.", "Której — rodzaj żeński.", "Której is feminine.")],
  ("którego żona = чия дружина (англ. whose).", "którego żona = angielskie whose wife.", "którego żona = whose wife.")),
]
D[18] = ("Opisz trzy osoby z Mystic Falls, używając zdań względnych (50+ słów): Damon to mężczyzna, który…, Isobel była kobietą, której…, Mystic Falls to miasto, w którym…", 50,
 ("Який / яка / чий — роблять опис багатим.", "Który / która / którego wzbogacają opis.", "Który / która / którego make descriptions rich."))

T[19] = ("Після дієслів: chcieć + інфінітив, unikać + родовий", "Po czasownikach: chcieć + bezokolicznik, unikać + dopełniacz", "After verbs: chcieć + infinitive, unikać + genitive")
G[19] = [
 ("Jeremy chce ____ z Anną na zawsze.", ["zostać", "zostanie", "został"], 0,
  [("Так! Chcieć + інфінітив.", "Tak! Chcieć + bezokolicznik.", "Yes! Chcieć + infinitive."),
   ("Zostanie — майбутній, після chce не вживається.", "Zostanie — przyszły, nie po chce.", "Zostanie is future — not after chce."),
   ("Został — минулий.", "Został — przeszły.", "Został is past.")],
  ("Після chcieć, musieć, móc, lubić — інфінітив.", "Po chcieć, musieć, móc, lubić — bezokolicznik.", "After chcieć, musieć, móc, lubić use the infinitive.")),
 ("Elena unika ____ o wampirach.", ["rozmów", "rozmowy", "rozmowom"], 0,
  [("Так! Unikać + родовий відмінок: rozmów.", "Tak! Unikać + dopełniacz: rozmów.", "Yes! Unikać + genitive: rozmów."),
   ("Rozmowy — називний/знахідний множини.", "Rozmowy — mianownik/biernik.", "Rozmowy is nominative/accusative."),
   ("Rozmowom — давальний.", "Rozmowom — celownik.", "Rozmowom is dative.")],
  ("Unikać czego? — родовий відмінок.", "Unikać czego? — dopełniacz.", "Unikać czego? — genitive.")),
]
D[19] = ("Napisz pamiętnik Jeremy'ego (50+ słów). Użyj chcieć / musieć / lubić + bezokolicznik oraz unikać / bać się + dopełniacz.", 50,
 ("Запам'ятовуй дієслова разом із відмінком.", "Zapamiętuj czasowniki razem z przypadkiem.", "Learn verbs together with their case."))

T[20] = ("Пасив: został porwany, jest przetrzymywany", "Strona bierna: został porwany, jest przetrzymywany", "Passive: został porwany, jest przetrzymywany")
G[20] = [
 ("Stefan ____ porwany przez wampiry z grobowca!", ["został", "została", "porwał"], 0,
  [("Так! Стефан → został porwany.", "Tak! Stefan → został porwany.", "Yes! Stefan → został porwany."),
   ("Została — жіночий рід.", "Została — rodzaj żeński.", "Została is feminine."),
   ("Porwał — активний: це Стефан когось викрав.", "Porwał — strona czynna: to Stefan kogoś porwał.", "Porwał is active: Stefan kidnapped someone.")],
  ("zostać + дієприкметник = подія; być + дієприкметник = стан.", "zostać + imiesłów = wydarzenie; być + imiesłów = stan.", "zostać + participle = event; być + participle = state.")),
 ("Wampir musi ____ zaproszony przez właściciela.", ["zostać", "zaprosić", "zapraszał"], 0,
  [("Так! Musi + zostać + дієприкметник.", "Tak! Musi + zostać + imiesłów.", "Yes! Musi + zostać + participle."),
   ("Zaprosić — активний: вампір сам запрошує.", "Zaprosić — strona czynna.", "Zaprosić is active."),
   ("Zapraszał — минулий, не після musi.", "Zapraszał — przeszły, nie po musi.", "Zapraszał is past — not after musi.")],
  ("Пасив із модальними: musi zostać zaproszony.", "Strona bierna z modalnymi: musi zostać zaproszony.", "Modal passive: musi zostać zaproszony.")),
]
D[20] = ("Napisz raport policyjny z nocy ratunku (50+ słów). Użyj strony biernej: Stefan został znaleziony…, był przetrzymywany…, dom został…", 50,
 ("Мова офіційних звітів.", "Język oficjalnych raportów.", "The language of official reports."))

T[21] = ("Дієслова з się і прийменником: przyzwyczaić się do", "Czasowniki z się i przyimkiem: przyzwyczaić się do", "Reflexive verbs with prepositions: przyzwyczaić się do")
G[21] = [
 ("Stefan nie jest przyzwyczajony ____ ludzkiej krwi.", ["do", "na", "z"], 0,
  [("Так! przyzwyczaić się do + родовий.", "Tak! przyzwyczaić się do + dopełniacz.", "Yes! przyzwyczaić się do + genitive."),
   ("Na — інший прийменник.", "Na — inny przyimek.", "Na is the wrong preposition."),
   ("Z — інший прийменник.", "Z — inny przyimek.", "Z is the wrong preposition.")],
  ("być przyzwyczajonym do = be used to.", "być przyzwyczajonym do = angielskie be used to.", "być przyzwyczajonym do = be used to.")),
 ("Tyler znowu ____ panowanie nad sobą.", ["stracił", "tracić", "straci"], 0,
  [("Так! Подія в минулому: stracił.", "Tak! Wydarzenie w przeszłości: stracił.", "Yes! A past event: stracił."),
   ("Інфінітив — неповне речення.", "Bezokolicznik — zdanie niepełne.", "The infinitive is incomplete."),
   ("Straci — майбутнє, а «znowu» про те, що вже сталося.", "Straci — przyszłość, a „znowu” mówi o tym, co już się stało.", "Straci is future, but “znowu” refers to what already happened.")],
  ("stracić panowanie nad sobą = вийти з себе.", "stracić panowanie nad sobą = lose one's temper.", "stracić panowanie nad sobą = lose one's temper.")),
]
D[21] = ("Napisz pamiętnik Eleny o zmianach Stefana (55+ słów). Użyj przyzwyczaić się do, uspokoić się, poddać się i ograniczyć.", 55,
 ("Дієслова з się — серце живої польської.", "Czasowniki z się to serce żywej polszczyzny.", "Reflexive verbs are the heart of living Polish."))

T[23] = ("Бажання: szkoda, że / gdyby tylko", "Życzenia: szkoda, że / gdyby tylko", "Wishes: szkoda, że / gdyby tylko")
G[23] = [
 ("Elena: — ____ Stefana tu teraz nie ma.", ["Szkoda, że", "Gdyby", "Jeśli"], 0,
  [("Так! Жаль про реальну ситуацію → Szkoda, że + дійсний спосіб.", "Tak! Żal o rzeczywistą sytuację → Szkoda, że + tryb oznajmujący.", "Yes! Regret about reality → Szkoda, że + indicative."),
   ("Gdyby — потребує форми з by.", "Gdyby wymaga formy z by.", "Gdyby needs a form with by."),
   ("Jeśli — умова, не жаль.", "Jeśli — warunek, nie żal.", "Jeśli is a condition, not regret.")],
  ("Szkoda, że = I wish / шкода, що.", "Szkoda, że = angielskie I wish.", "Szkoda, że = I wish.")),
 ("Stefan: — Gdybym tylko nie ____ tej krwi!", ["pił", "piję", "wypiję"], 0,
  [("Так! Gdybym tylko + минулий: pił.", "Tak! Gdybym tylko + forma przeszła: pił.", "Yes! Gdybym tylko + past form: pił."),
   ("Piję — теперішній.", "Piję — teraźniejszy.", "Piję is present."),
   ("Wypiję — майбутній.", "Wypiję — przyszły.", "Wypiję is future.")],
  ("Gdyby tylko… — якби ж тільки…", "Gdyby tylko… = if only…", "Gdyby tylko… = if only…")),
]
D[23] = ("Napisz pamiętnik Eleny po konkursie (55+ słów). Użyj szkoda, że i gdyby tylko co najmniej cztery razy.", 55,
 ("Жаль про теперішнє і про минуле.", "Żal o teraźniejszość i o przeszłość.", "Regret about the present and the past."))

T[24] = ("Минулі модальні: powinienem był / mogłem", "Modalne o przeszłości: powinienem był / mogłem", "Past modals: powinienem był / mogłem")
G[24] = [
 ("Stefan: — Nie ____ namawiać Damona. Zniszczyłem mu życie.", ["powinienem był", "musiałem", "mogę"], 0,
  [("Так! Жаль про минуле: nie powinienem był.", "Tak! Żal o przeszłość: nie powinienem był.", "Yes! Regret about the past: nie powinienem był."),
   ("Musiałem — «мусив», без жалю.", "Musiałem — przymus, bez żalu.", "Musiałem means had to — no regret."),
   ("Mogę — теперішній.", "Mogę — teraźniejszy.", "Mogę is present.")],
  ("powinienem był + інфінітив = should have.", "powinienem był + bezokolicznik = should have.", "powinienem był + infinitive = should have.")),
 ("Damon początkowo odmówił. To ____ być dla niego straszny wybór.", ["musiał", "powinien", "mógłby"], 0,
  [("Так! Впевнене припущення про минуле: musiał być.", "Tak! Pewne przypuszczenie o przeszłości: musiał być.", "Yes! A confident guess about the past: musiał być."),
   ("Powinien — «повинен», не припущення.", "Powinien — powinność, nie przypuszczenie.", "Powinien is duty, not a guess."),
   ("Mógłby — умовний.", "Mógłby — tryb przypuszczający.", "Mógłby is conditional.")],
  ("musiał być = must have been.", "musiał być = angielskie must have been.", "musiał być = must have been.")),
]
D[24] = ("Napisz tajny pamiętnik Damona o 1864 roku (55+ słów). Użyj powinienem był, mogłem, musiał i nie powinien był.", 55,
 ("Граматика каяття і здогадок.", "Gramatyka skruchy i domysłów.", "The grammar of remorse and guesses."))

T[25] = ("Змішані умовні: gdyby nie odeszła, byłaby…", "Mieszane warunki: gdyby nie odeszła, byłaby teraz…", "Mixed conditionals: gdyby nie odeszła, byłaby teraz…")
G[25] = [
 ("Gdyby Isobel nie odeszła, Elena ____ teraz kimś innym.", ["byłaby", "jest", "będzie"], 0,
  [("Так! Минула причина → теперішній наслідок: byłaby teraz.", "Tak! Przeszła przyczyna → skutek teraz: byłaby.", "Yes! A past cause → a present result: byłaby teraz."),
   ("Jest — реальність.", "Jest — rzeczywistość.", "Jest is reality."),
   ("Będzie — реальне майбутнє.", "Będzie — realna przyszłość.", "Będzie is a real future.")],
  ("Слово «teraz» підказує теперішній наслідок.", "Słowo „teraz” podpowiada skutek w teraźniejszości.", "“Teraz” signals a present result.")),
 ("Gdyby John nie kłamał, Elena by mu teraz ____.", ["ufała", "ufa", "zaufa"], 0,
  [("Так! by + минула форма: ufała.", "Tak! by + forma przeszła: ufała.", "Yes! by + past form: ufała."),
   ("Ufa — реальність.", "Ufa — rzeczywistość.", "Ufa is reality."),
   ("Zaufa — майбутній.", "Zaufa — przyszłość.", "Zaufa is future.")],
  ("Частка «by» може стояти окремо: by mu ufała.", "Partykuła „by” może stać osobno: by mu ufała.", "“By” can stand apart: by mu ufała.")),
]
D[25] = ("Napisz pamiętnik Eleny po spotkaniu z Isobel (55+ słów). Użyj co najmniej trzech mieszanych zdań z gdyby: Gdyby nie odeszła, byłabym teraz…", 55,
 ("Минуле і теперішнє в одному реченні.", "Przeszłość i teraźniejszość w jednym zdaniu.", "Past and present in one sentence."))

T[26] = ("Час оповіді: вид у розповіді", "Czasy narracji: aspekt w opowiadaniu", "Narrative: aspect in storytelling")
G[26] = [
 ("Kiedy fajerwerki ____, John włączył urządzenie.", ["wybuchały", "wybuchły", "wybuchną"], 0,
  [("Так! Тло (процес) → недоконаний: wybuchały.", "Tak! Tło (proces) → niedokonany: wybuchały.", "Yes! Background (process) → imperfective: wybuchały."),
   ("Wybuchły — одна подія, тло втрачено.", "Wybuchły — jedno wydarzenie, tło znika.", "Wybuchły is one event; the background is lost."),
   ("Wybuchną — майбутнє.", "Wybuchną — przyszłość.", "Wybuchną is future.")],
  ("Недоконаний — тло, доконаний — події.", "Niedokonany — tło, dokonany — wydarzenia.", "Imperfective = background, perfective = events.")),
 ("Gdy Stefan dobiegł do piwnicy, ogień już ____.", ["się rozprzestrzenił", "się rozprzestrzeniał", "się rozprzestrzeni"], 0,
  [("Так! «już» + доконаний: результат раніше.", "Tak! „już” + dokonany: rezultat wcześniej.", "Yes! “już” + perfective: an earlier result."),
   ("Процес — менш точно після «już».", "Proces — mniej precyzyjnie po „już”.", "A process is less precise after “już”."),
   ("Майбутнє не пасує.", "Przyszłość nie pasuje.", "The future doesn't fit.")],
  ("Польська передає Past Perfect видом і словом «już».", "Polski oddaje Past Perfect aspektem i słowem „już”.", "Polish expresses Past Perfect with aspect and “już”.")),
]
D[26] = ("Napisz ostatni wpis Eleny w tym sezonie (60+ słów). Użyj aspektu niedokonanego dla tła i dokonanego dla wydarzeń. Zakończ tym, co twoim zdaniem wydarzy się dalej.", 60,
 ("Фінальний щоденник — твоя власна серія.", "Ostatni wpis — twój własny odcinek.", "The final entry is your own episode."))

# Bossowie i finał — powtórka gramatyki
for b, src in ((5, (1, 2, 3, 4)), (11, (6, 7, 8, 9, 10)), (16, (12, 13, 14, 15)), (22, (17, 18, 19, 20, 21)), (27, (23, 24, 25, 26))):
    G[b] = [G[i][0] for i in src]
    T[b] = ("Повторення граматики арки", "Powtórka gramatyki łuku", "Arc grammar review")
G[28] = [G[i][1] for i in (1, 2, 3, 4, 6, 8, 9, 13, 18, 20, 24, 25)]
T[28] = ("Уся граматика сезону", "Cała gramatyka sezonu", "All the season's grammar")
D[28] = ("Napisz własną ostatnią stronę sezonu (70+ słów): czego nauczyłeś(-aś) się w Mystic Falls, która postać zmieniła się najbardziej i czego oczekujesz od drugiego sezonu.", 70,
 ("Вітаємо! Твій щоденник польською — найкращий доказ.", "Gratulacje! Twój pamiętnik po polsku to najlepszy dowód.", "Congratulations! Your Polish diary is the best proof."))
