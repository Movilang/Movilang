# Wersja kursu dla uczących się POLSKIEGO (A2). Gramatyka + list.
# Zadanie: (pytanie, [opcje], poprawna, [(uk, pl, en) dla każdej opcji], (tip uk, pl, en))
G = {}
D = {}
T = {}

T[1] = ("Być і mieć: jestem, mam", "Być i mieć: jestem, mam", "Być and mieć: to be and to have")
G[1] = [
 ("Kevin ____ osiem lat.", ["ma", "jest", "mam"], 0,
  [("Так! Про вік поляки кажуть «мати»: Kevin ma osiem lat.", "Tak! O wieku mówimy „mieć”: Kevin ma osiem lat.", "Yes! Polish uses mieć (to have) for age: Kevin ma osiem lat."),
   ("Jest — «є», але вік — через ma.", "„Jest” nie mówimy o wieku.", "Jest is not used for age."),
   ("Mam — «я маю».", "„Mam” — forma „ja”.", "Mam is the “I” form.")],
  ("Ile masz lat? — Mam osiem lat.", "Ile masz lat? — Mam osiem lat.", "Ile masz lat? — Mam osiem lat.")),
 ("Ja ____ najmłodszy w rodzinie.", ["jestem", "jest", "są"], 0,
  [("Так! Ja → jestem.", "Tak! Ja → jestem.", "Yes! Ja → jestem."),
   ("Jest — він/вона.", "„Jest” — on/ona.", "Jest is he/she."),
   ("Są — вони.", "„Są” — oni.", "Są is they.")],
  ("Być: jestem, jesteś, jest, jesteśmy, jesteście, są.", "Być: jestem, jesteś, jest, jesteśmy, jesteście, są.", "Być: jestem, jesteś, jest, jesteśmy, jesteście, są.")),
]
D[1] = ("Napisz o swojej rodzinie (35+ słów). Ile masz lat? Ilu masz braci i siostry? Kto jest najmłodszy?", 35,
 ("Використай jestem / mam.", "Użyj „jestem” i „mam”.", "Use jestem / mam."))

T[2] = ("Czas teraźniejszy: lubię, jem", "Czas teraźniejszy: lubię, jem", "Present tense: lubię, jem")
G[2] = [
 ("Kevin ____ tylko pizzę z serem.", ["lubi", "lubię", "lubią"], 0,
  [("Так! Він → lubi.", "Tak! On → lubi.", "Yes! He → lubi."),
   ("Lubię — «я люблю».", "„Lubię” — forma „ja”.", "Lubię is the “I” form."),
   ("Lubią — «вони люблять».", "„Lubią” — oni.", "Lubią is “they”.")],
  ("Lubić: lubię, lubisz, lubi, lubimy, lubicie, lubią.", "Lubić: lubię, lubisz, lubi, lubimy, lubicie, lubią.", "Lubić: lubię, lubisz, lubi, lubimy, lubicie, lubią.")),
 ("Buzz ____ pizzę Kevina.", ["je", "jem", "jedzą"], 0,
  [("Так! Він → je.", "Tak! On → je.", "Yes! He → je."),
   ("Jem — «я їм».", "„Jem” — ja.", "Jem is “I eat”."),
   ("Jedzą — «вони їдять».", "„Jedzą” — oni.", "Jedzą is “they eat”.")],
  ("Jeść: jem, jesz, je, jemy, jecie, jedzą.", "Jeść: jem, jesz, je, jemy, jecie, jedzą.", "Jeść: jem, jesz, je, jemy, jecie, jedzą.")),
]
D[2] = ("Napisz złą kartkę Kevina (35+ słów). Co lubi, a czego nie lubi w swojej rodzinie? Użyj: lubię, nie lubię, je, krzyczy.", 35,
 ("Заперечення: nie + дієслово.", "Przeczenie: nie + czasownik.", "Negative: nie + verb."))

T[3] = ("Jest / są + miejscownik: w pokoju, na łóżku", "Jest / są + miejscownik: w pokoju, na łóżku", "Jest / są + locative: w pokoju, na łóżku")
G[3] = [
 ("W pokoju ____ tylko jedno łóżko.", ["jest", "są", "jestem"], 0,
  [("Так! Один предмет → jest.", "Tak! Jedna rzecz → jest.", "Yes! One thing → jest."),
   ("Są — для множини.", "„Są” — liczba mnoga.", "Są is plural."),
   ("Jestem — «я є».", "„Jestem” — ja.", "Jestem means “I am”.")],
  ("Jest + однина, są + множина.", "Jest + liczba pojedyncza, są + mnoga.", "Jest + singular, są + plural.")),
 ("Lampa stoi obok ____.", ["łóżka", "łóżko", "łóżku"], 0,
  [("Так! Obok + родовий відмінок: łóżka.", "Tak! Obok + dopełniacz: łóżka.", "Yes! Obok + genitive: łóżka."),
   ("Łóżko — називний.", "„Łóżko” — mianownik.", "Łóżko is nominative."),
   ("Łóżku — місцевий (na łóżku).", "„Łóżku” — miejscownik (na łóżku).", "Łóżku is locative (na łóżku).")],
  ("Obok, koło, za + родовий; w, na + місцевий.", "Obok, koło + dopełniacz; w, na + miejscownik.", "Obok + genitive; w, na + locative.")),
]
D[3] = ("Opisz swój pokój (35+ słów). Co jest w pokoju? Gdzie stoi łóżko? Użyj: jest, są, obok, pod, na.", 35,
 ("W pokoju jest…, obok łóżka jest…", "W pokoju jest…, obok łóżka jest…", "W pokoju jest…, obok łóżka jest…"))

T[4] = ("Czas przeszły: był / była / byli", "Czas przeszły: był / była / byli", "Past tense: był / była / byli")
G[4] = [
 ("Wczoraj ____ wielka burza.", ["była", "był", "było"], 0,
  [("Так! Burza — жіночий рід → była.", "Tak! Burza (r. żeński) → była.", "Yes! Burza is feminine → była."),
   ("Był — чоловічий рід.", "„Był” — rodzaj męski.", "Był is masculine."),
   ("Było — середній рід.", "„Było” — rodzaj nijaki.", "Było is neuter.")],
  ("Минулий час змінюється за родом.", "Czas przeszły zmienia się według rodzaju.", "The past tense changes by gender.")),
 ("Dzieci nie ____ gotowe.", ["były", "byli", "była"], 0,
  [("Так! Dzieci → były (не чоловічо-особова форма).", "Tak! Dzieci → były (forma niemęskoosobowa).", "Yes! Dzieci → były (non-masculine-personal form)."),
   ("Byli — тільки якщо є чоловіки.", "„Byli” — gdy w grupie są mężczyźni.", "Byli is for groups with men."),
   ("Była — однина.", "„Była” — liczba pojedyncza.", "Była is singular.")],
  ("Byli (чоловіки), były (жінки, діти, речі).", "Byli (mężczyźni), były (kobiety, dzieci, rzeczy).", "Byli (men), były (women, children, things).")),
]
D[4] = ("Opisz zły poranek (35+ słów). Gdzie byłeś? Która była godzina? Kto się spóźnił? Użyj: byłem/byłam, był, była, byli.", 35,
 ("Стеж за родом: był / była.", "Pilnuj rodzaju: był / była.", "Watch the gender: był / była."))

T[5] = ("Tryb rozkazujący: biegnij! nie zatrzymuj się!", "Tryb rozkazujący: biegnij! nie zatrzymuj się!", "Imperative: biegnij! nie zatrzymuj się!")
G[5] = [
 ("Tata krzyczy: — ____ za mną!", ["Chodźcie", "Chodzić", "Chodzą"], 0,
  [("Так! Наказ для кількох: chodźcie.", "Tak! Rozkaz do kilku osób: chodźcie.", "Yes! An order to several people: chodźcie."),
   ("Chodzić — інфінітив.", "„Chodzić” — bezokolicznik.", "Chodzić is the infinitive."),
   ("Chodzą — «вони ходять».", "„Chodzą” — oni chodzą.", "Chodzą means “they walk”.")],
  ("Ty: chodź! Wy: chodźcie!", "Ty: chodź! Wy: chodźcie!", "Ty: chodź! Wy: chodźcie!")),
 ("— Nie ____ się! Jesteśmy spóźnieni!", ["zatrzymujcie", "zatrzymajcie", "zatrzymać"], 0,
  [("Так! Заборона: nie + недоконаний вид.", "Tak! Zakaz: nie + aspekt niedokonany.", "Yes! A ban: nie + imperfective."),
   ("Доконаний вид у забороні звучить неприродно.", "Aspekt dokonany w zakazie brzmi nienaturalnie.", "The perfective sounds unnatural in a ban."),
   ("Інфінітив — не наказ.", "Bezokolicznik to nie rozkaz.", "The infinitive is not an order.")],
  ("Nie + rozkaz niedokonany: nie biegnij, nie krzycz.", "Nie + rozkaz niedokonany: nie biegnij, nie krzycz.", "Nie + imperfective imperative: nie biegnij, nie krzycz.")),
]
D[5] = ("Napisz zasady rodzinnej podróży (35+ słów). Użyj trybu rozkazującego: spakuj…, nie zapomnij…, sprawdź…, policz dzieci!", 35,
 ("Ty: sprawdź! Wy: sprawdźcie!", "Ty: sprawdź! Wy: sprawdźcie!", "Ty: sprawdź! Wy: sprawdźcie!"))

T[7] = ("Czas przeszły: szukałem, szukałam", "Czas przeszły: szukałem, szukałam", "Past tense: szukałem, szukałam")
G[7] = [
 ("Kevin ____ rodziny w całym domu.", ["szukał", "szukała", "szukali"], 0,
  [("Так! Він → szukał.", "Tak! On → szukał.", "Yes! He → szukał."),
   ("Szukała — вона.", "„Szukała” — ona.", "Szukała is “she”."),
   ("Szukali — вони.", "„Szukali” — oni.", "Szukali is “they”.")],
  ("Минулий: -ł (він), -ła (вона), -li/-ły (вони).", "Przeszły: -ł (on), -ła (ona), -li/-ły (oni/one).", "Past: -ł (he), -ła (she), -li/-ły (they).")),
 ("Kevin: — Ja ____ do mamy, ale nikt nie odpowiedział.", ["wołałem", "wołał", "wołałam"], 0,
  [("Так! Я (чоловік) → wołałem.", "Tak! Ja (mężczyzna) → wołałem.", "Yes! I (male) → wołałem."),
   ("Wołał — він.", "„Wołał” — on.", "Wołał is “he”."),
   ("Wołałam — я (жінка).", "„Wołałam” — ja (kobieta).", "Wołałam is “I” (female).")],
  ("Я: -łem (чол.), -łam (жін.).", "Ja: -łem (m.), -łam (ż.).", "I: -łem (male), -łam (female).")),
]
D[7] = ("Opisz pierwszy poranek Kevina samego w domu (35+ słów). Użyj czasu przeszłego: obudziłem się, szukałem, wołałem, czekałem.", 35,
 ("Від імені Кевіна: -łem.", "Jako Kevin: -łem.", "As Kevin: -łem."))

T[8] = ("Móc / umieć / wolno", "Móc / umieć / wolno", "Móc / umieć / wolno (can, know how, be allowed)")
G[8] = [
 ("Dziś Kevin ____ jeść lody na śniadanie.", ["może", "umie", "musi"], 0,
  [("Так! Може = є можливість / дозвіл.", "Tak! Może = ma możliwość / pozwolenie.", "Yes! Może = he is able/allowed."),
   ("Umie — вміє (навичка).", "„Umie” — umiejętność.", "Umie = knows how (a skill)."),
   ("Musi — мусить.", "„Musi” — obowiązek.", "Musi = must.")],
  ("Móc — можливість, umieć — навичка.", "Móc — możliwość, umieć — umiejętność.", "Móc = possibility, umieć = skill.")),
 ("Wcześniej Kevinowi nie ____ oglądać tego filmu.", ["wolno było", "mógł było", "umiał"], 0,
  [("Так! Wolno = дозволено; минуле: wolno było.", "Tak! Wolno = dozwolone; przeszłość: wolno było.", "Yes! Wolno = allowed; past: wolno było."),
   ("Неграматичне поєднання.", "Niegramatyczne połączenie.", "Ungrammatical."),
   ("Umiał — вмів, інший зміст.", "„Umiał” — inny sens.", "Umiał means knew how.")],
  ("Komuś wolno / nie wolno + інфінітив.", "Komuś wolno / nie wolno + bezokolicznik.", "Komuś wolno / nie wolno + infinitive.")),
]
D[8] = ("Napisz, co możesz, a czego nie możesz robić, kiedy jesteś sam w domu (35+ słów). Użyj: mogę, nie mogę, umiem, wolno mi.", 35,
 ("Mogę…, nie wolno mi…", "Mogę…, nie wolno mi…", "Mogę…, nie wolno mi…"))

T[9] = ("Zaimki dzierżawcze: mój, twój, jego", "Zaimki dzierżawcze: mój, twój, jego", "Possessives: mój, twój, jego")
G[9] = [
 ("To jest pokój Buzza. To ____ pokój.", ["jego", "jej", "mój"], 0,
  [("Так! Buzz — він → jego.", "Tak! Buzz → jego.", "Yes! Buzz → jego (his)."),
   ("Jej — її.", "„Jej” — ona.", "Jej means her."),
   ("Mój — мій.", "„Mój” — ja.", "Mój means my.")],
  ("Jego / jej / ich не змінюються.", "Jego / jej / ich się nie odmieniają.", "Jego / jej / ich never change.")),
 ("Kevin: — Teraz ten pokój jest ____!", ["mój", "moja", "moje"], 0,
  [("Так! Pokój — чоловічий рід → mój.", "Tak! Pokój (r. męski) → mój.", "Yes! Pokój is masculine → mój."),
   ("Moja — жіночий рід.", "„Moja” — r. żeński.", "Moja is feminine."),
   ("Moje — середній рід.", "„Moje” — r. nijaki.", "Moje is neuter.")],
  ("Mój (ч.), moja (ж.), moje (с.).", "Mój, moja, moje.", "Mój, moja, moje — by gender.")),
]
D[9] = ("Opisz pokój swojego brata, siostry albo przyjaciela (35+ słów). Użyj: jego, jej, mój, twój.", 35,
 ("Jego plakaty, jej łóżko, mój pokój.", "Jego plakaty, jej łóżko, mój pokój.", "Jego plakaty, jej łóżko, mój pokój."))

T[10] = ("Czas przeszły nieregularny: jadłem, poszedłem, widziałem", "Czas przeszły nieregularny: jadłem, poszedłem, widziałem", "Irregular past: jadłem, poszedłem, widziałem")
G[10] = [
 ("Dostawca ____ pod drzwi.", ["przyszedł", "przyszłem", "przychodził raz"], 0,
  [("Так! Przyjść → przyszedł.", "Tak! Przyjść → przyszedł.", "Yes! Przyjść → przyszedł."),
   ("Такої форми немає.", "Takiej formy nie ma.", "No such form."),
   ("Неприродно.", "Nienaturalnie.", "Unnatural.")],
  ("Iść → szedł, przyjść → przyszedł, jeść → jadł.", "Iść → szedł, przyjść → przyszedł, jeść → jadł.", "Iść → szedł, przyjść → przyszedł, jeść → jadł.")),
 ("Kevin ____ pizzę przed telewizorem.", ["zjadł", "zjedł", "zjadał raz"], 0,
  [("Так! Zjeść → zjadł.", "Tak! Zjeść → zjadł.", "Yes! Zjeść → zjadł."),
   ("Такої форми немає.", "Takiej formy nie ma.", "No such form."),
   ("Неприродно.", "Nienaturalnie.", "Unnatural.")],
  ("Jeść: jadł, jadła, jedli.", "Jeść: jadł, jadła, jedli.", "Jeść: jadł, jadła, jedli.")),
]
D[10] = ("Opisz swój wieczór jak Kevin (35+ słów). Użyj: zjadłem, widziałem, przyszedł, uciekł, pomyślał.", 35,
 ("Неправильні форми треба запам'ятати.", "Formy nieregularne trzeba zapamiętać.", "Irregular forms must be learnt."))

T[11] = ("Pytania: kto, co, gdzie, kiedy, dlaczego, jak", "Pytania: kto, co, gdzie, kiedy, dlaczego, jak", "Questions: kto, co, gdzie, kiedy, dlaczego, jak")
G[11] = [
 ("____ Marley mieszka sam?", ["Dlaczego", "Kto", "Gdzie"], 0,
  [("Так! Dlaczego = чому.", "Tak! Dlaczego = przyczyna.", "Yes! Dlaczego = why."),
   ("Kto — хто.", "„Kto” — osoba.", "Kto = who."),
   ("Gdzie — де.", "„Gdzie” — miejsce.", "Gdzie = where.")],
  ("Kto, co, gdzie, kiedy, dlaczego, jak.", "Kto, co, gdzie, kiedy, dlaczego, jak.", "Kto, co, gdzie, kiedy, dlaczego, jak.")),
 ("____ jest ten człowiek z łopatą?", ["Kim", "Kto", "Co"], 0,
  [("Так! Kim jest…? — про особу з «бути».", "Tak! Kim jest…? — z „być”.", "Yes! Kim jest…? — with “to be”."),
   ("Kto jest… — можливо, але «Kim jest» природніше.", "„Kto jest” — możliwe, ale „Kim jest” brzmi naturalniej.", "Kto jest is possible, but Kim jest is more natural."),
   ("Co — про речі.", "„Co” — o rzeczach.", "Co is for things.")],
  ("Kim jesteś? Kim on jest?", "Kim jesteś? Kim on jest?", "Kim jesteś? Kim on jest?")),
]
D[11] = ("Napisz sześć pytań do Marleya (35+ słów). Użyj: kto, co, gdzie, kiedy, dlaczego, jak.", 35,
 ("Dlaczego…? Gdzie…? Kiedy…?", "Dlaczego…? Gdzie…? Kiedy…?", "Dlaczego…? Gdzie…? Kiedy…?"))
