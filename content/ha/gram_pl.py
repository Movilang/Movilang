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

T[13] = ("Czas teraźniejszy: teraz robię", "Czas teraźniejszy: teraz robię", "Present tense: what I'm doing now")
G[13] = [
 ("Patrz! Kevin ____ zęby.", ["myje", "myję", "myją"], 0,
  [("Так! Він → myje.", "Tak! On → myje.", "Yes! He → myje."), ("Myję — я.", "„Myję” — ja.", "Myję is “I”."), ("Myją — вони.", "„Myją” — oni.", "Myją is “they”.")],
  ("У польській один теперішній час: myje = миє / is washing.", "Po polsku jeden czas teraźniejszy: myje = is washing / washes.", "Polish has one present tense: myje = washes / is washing.")),
 ("— Co robisz? — ____ włosy.", ["Myję", "Myje", "Myjemy"], 0,
  [("Так! Я → myję.", "Tak! Ja → myję.", "Yes! I → myję."), ("Myje — він.", "„Myje” — on.", "Myje is “he”."), ("Myjemy — ми.", "„Myjemy” — my.", "Myjemy is “we”.")],
  ("Ja myję, ty myjesz, on myje.", "Ja myję, ty myjesz, on myje.", "Ja myję, ty myjesz, on myje.")),
]
D[13] = ("Opisz, co Kevin robi teraz w łazience (35+ słów). Użyj: bierze prysznic, śpiewa, myje, czesze się, krzyczy.", 35,
 ("Теперішній час: -e / -ę.", "Czas teraźniejszy.", "Present tense."))

T[14] = ("Ile? Trochę / żaden", "Ile? Trochę / żaden", "Ile? Some / no")
G[14] = [
 ("____ pieniędzy ma Kevin?", ["Ile", "Ilu", "Jak"], 0,
  [("Так! Ile + родовий відмінок.", "Tak! Ile + dopełniacz.", "Yes! Ile + genitive."), ("Ilu — про людей-чоловіків.", "„Ilu” — o osobach (m.).", "Ilu is for male persons."), ("Jak — як.", "„Jak” — sposób.", "Jak means how.")],
  ("Ile + родовий: ile mleka, ile jajek.", "Ile + dopełniacz: ile mleka, ile jajek.", "Ile + genitive: ile mleka, ile jajek.")),
 ("W lodówce nie ma ____.", ["mleka", "mleko", "mlekiem"], 0,
  [("Так! Nie ma + родовий.", "Tak! Nie ma + dopełniacz.", "Yes! Nie ma + genitive."), ("Називний — помилка після nie ma.", "Mianownik po „nie ma” — błąd.", "Nominative after nie ma is wrong."), ("Орудний — помилка.", "Narzędnik — błąd.", "Instrumental is wrong.")],
  ("Nie ma + родовий: nie ma chleba, mleka.", "Nie ma + dopełniacz: nie ma chleba, mleka.", "Nie ma + genitive.")),
]
D[14] = ("Napisz listę zakupów Kevina i krótko opisz zakupy (35+ słów). Użyj: ile, trochę, kilka, nie ma.", 35,
 ("Trochę mleka, kilka jajek, nie ma chleba.", "Trochę mleka, kilka jajek, nie ma chleba.", "Trochę mleka, kilka jajek, nie ma chleba."))

T[15] = ("Pytania w czasie przeszłym: Czy zapłaciłeś?", "Pytania w czasie przeszłym: Czy zapłaciłeś?", "Past questions: Czy zapłaciłeś?")
G[15] = [
 ("____ Kevin zapłacił za szczoteczkę?", ["Czy", "Co", "Kto"], 0,
  [("Так! Так/ні питання → czy.", "Tak! Pytanie tak/nie → czy.", "Yes! Yes/no question → czy."), ("Co — що.", "„Co” — rzecz.", "Co means what."), ("Kto — хто.", "„Kto” — osoba.", "Kto means who.")],
  ("Czy + речення = питання так/ні.", "Czy + zdanie = pytanie tak/nie.", "Czy + sentence = yes/no question.")),
 ("Co ____ w aptece? (ty, chłopiec)", ["kupiłeś", "kupił", "kupiłam"], 0,
  [("Так! Ти (хлопчик) → -łeś.", "Tak! Ty (chłopiec) → -łeś.", "Yes! You (boy) → -łeś."), ("Kupił — він.", "„Kupił” — on.", "Kupił is “he”."), ("Kupiłam — я (жін.).", "„Kupiłam” — ja (ż.).", "Kupiłam is “I” (female).")],
  ("Ти: -łeś (ч.), -łaś (ж.).", "Ty: -łeś, -łaś.", "You: -łeś (m.), -łaś (f.).")),
]
D[15] = ("Jesteś policjantem. Napisz sześć pytań do Kevina o wczoraj (35+ słów). Użyj: czy…?, gdzie byłeś?, co kupiłeś?, dlaczego uciekłeś?", 35,
 ("Czy + минулий час.", "Czy + czas przeszły.", "Czy + past tense."))

T[16] = ("Stopień wyższy: większy, ładniejszy, lepszy", "Stopień wyższy: większy, ładniejszy, lepszy", "Comparatives: większy, ładniejszy, lepszy")
G[16] = [
 ("Ta choinka jest ____ od Kevina.", ["wyższa", "wysoka", "najwyższa"], 0,
  [("Так! Wysoki → wyższy (ж. wyższa).", "Tak! Wysoki → wyższy (wyższa).", "Yes! Wysoki → wyższy (fem. wyższa)."), ("Звичайний ступінь.", "Stopień równy.", "Base form."), ("Найвищий ступінь.", "Stopień najwyższy.", "Superlative.")],
  ("Порівняння: od + родовий або niż.", "Porównanie: od + dopełniacz albo niż.", "Compare: od + genitive or niż.")),
 ("Z lampkami choinka jest ____.", ["ładniejsza", "bardziej ładna", "najładniej"], 0,
  [("Так! Ładny → ładniejszy.", "Tak! Ładny → ładniejszy.", "Yes! Ładny → ładniejszy."), ("Можливо, але природніше -iejsza.", "Możliwe, ale naturalniej -iejsza.", "Possible, but -iejsza is more natural."), ("Прислівник.", "Przysłówek.", "An adverb.")],
  ("Dobry → lepszy, zły → gorszy.", "Dobry → lepszy, zły → gorszy.", "Dobry → lepszy, zły → gorszy.")),
]
D[16] = ("Porównaj dwie choinki (35+ słów). Użyj: wyższa, mniejsza, ładniejsza, lepsza, niż.", 35,
 ("-szy / -ejszy + niż.", "-szy / -ejszy + niż.", "-szy / -ejszy + niż."))

T[17] = ("Stopień najwyższy: najlepszy, największy", "Stopień najwyższy: najlepszy, największy", "Superlatives: najlepszy, największy")
G[17] = [
 ("To ____ kolacja w moim życiu!", ["najlepsza", "najdobrsza", "lepsza"], 0,
  [("Так! Dobry → najlepszy.", "Tak! Dobry → najlepszy.", "Yes! Dobry → najlepszy."), ("Такого слова немає.", "Nie ma takiego słowa.", "Not a word."), ("Lepsza — вищий ступінь.", "„Lepsza” — stopień wyższy.", "Lepsza is the comparative.")],
  ("Naj- + вищий ступінь.", "Naj- + stopień wyższy.", "Naj- + comparative.")),
 ("To ____ szklanka w domu.", ["największa", "najbardziej duża", "większa"], 0,
  [("Так! Duży → największy.", "Tak! Duży → największy.", "Yes! Duży → największy."), ("Неприродно.", "Nienaturalnie.", "Unnatural."), ("Вищий ступінь.", "Stopień wyższy.", "Comparative.")],
  ("Duży → większy → największy.", "Duży → większy → największy.", "Duży → większy → największy.")),
]
D[17] = ("Opisz najlepszą albo najgorszą kolację w swoim życiu (35+ słów). Użyj: najlepszy, największy, najsmaczniejszy, najważniejszy.", 35,
 ("Naj- + -szy.", "Naj- + -szy.", "Naj- + -szy."))

T[19] = ("Czas przyszły: będę + bezokolicznik", "Czas przyszły: będę + bezokolicznik", "Future tense: będę + infinitive")
G[19] = [
 ("Dziś wieczorem bandyci ____ obserwować dom.", ["będą", "będzie", "są"], 0,
  [("Так! Вони → będą + інфінітив.", "Tak! Oni → będą + bezokolicznik.", "Yes! They → będą + infinitive."),
   ("Będzie — він/вона.", "„Będzie” — on/ona.", "Będzie is he/she."),
   ("Są — теперішній час.", "„Są” — czas teraźniejszy.", "Są is present tense.")],
  ("Być у майбутньому: będę, będziesz, będzie, będziemy, będziecie, będą.", "Być w przyszłości: będę, będziesz, będzie, będziemy, będziecie, będą.", "Być in the future: będę, będziesz, będzie, będziemy, będziecie, będą.")),
 ("Ja ____ czekać w furgonetce — mówi Marv.", ["będę", "będziesz", "jestem"], 0,
  [("Так! Я → będę.", "Tak! Ja → będę.", "Yes! Ja → będę."),
   ("Będziesz — ти.", "„Będziesz” — ty.", "Będziesz is “you”."),
   ("Jestem czekać — помилка.", "„Jestem czekać” — błąd.", "Jestem czekać is wrong.")],
  ("Będę + інфінітив = тривала дія в майбутньому.", "Będę + bezokolicznik = czynność trwająca w przyszłości.", "Będę + infinitive = an ongoing action in the future.")),
]
D[19] = ("Napisz, co będziesz robić w święta (35+ słów). Użyj: będę, będziemy, będzie + bezokolicznik.", 35,
 ("Будь-яка особа: będę czytać, będziemy jeść…", "Np.: będę czytać, będziemy jeść…", "E.g. będę czytać, będziemy jeść…"))

T[20] = ("Musieć / trzeba / nie wolno", "Musieć / trzeba / nie wolno", "Musieć / trzeba / nie wolno (must, it's necessary, it's forbidden)")
G[20] = [
 ("Kevin jest sam, więc ____ wszystko zrobić sam.", ["musi", "muszę", "musisz"], 0,
  [("Так! Він → musi.", "Tak! On → musi.", "Yes! On → musi."),
   ("Muszę — я.", "„Muszę” — ja.", "Muszę is “I”."),
   ("Musisz — ти.", "„Musisz” — ty.", "Musisz is “you”.")],
  ("Musieć: muszę, musisz, musi, musimy, musicie, muszą.", "Musieć: muszę, musisz, musi, musimy, musicie, muszą.", "Musieć: muszę, musisz, musi, musimy, musicie, muszą.")),
 ("W domu ____ zjeżdżać na sankach po schodach!", ["nie wolno", "nie wolny", "nie wolna"], 0,
  [("Так! Nie wolno = заборонено (безособово).", "Tak! „Nie wolno” = zakaz (bezosobowo).", "Yes! Nie wolno = it's forbidden (impersonal)."),
   ("Wolny — прикметник «вільний».", "„Wolny” to przymiotnik.", "Wolny is an adjective (free)."),
   ("Wolna — теж прикметник.", "„Wolna” to też przymiotnik.", "Wolna is also an adjective.")],
  ("Nie wolno + інфінітив = не можна.", "Nie wolno + bezokolicznik.", "Nie wolno + infinitive = you mustn't.")),
]
D[20] = ("Napisz zasady udawanej imprezy Kevina (35+ słów). Użyj: musi, muszę, trzeba, nie wolno.", 35,
 ("Trzeba / nie wolno + інфінітив.", "Trzeba / nie wolno + bezokolicznik.", "Trzeba / nie wolno + infinitive."))

T[21] = ("Aspekt w przeszłości: szukał / znalazł", "Aspekt w przeszłości: szukał / znalazł", "Aspect in the past: szukał / znalazł")
G[21] = [
 ("Kiedy Harry ____ biżuterii, Marv odkręcał krany.", ["szukał", "znalazł", "szuka"], 0,
  [("Так! Тривала дія (фон) → недоконаний вид.", "Tak! Czynność trwająca (tło) → aspekt niedokonany.", "Yes! An ongoing action (background) → imperfective."),
   ("Znalazł — одна завершена подія.", "„Znalazł” — jedno zakończone wydarzenie.", "Znalazł is one finished event."),
   ("Szuka — теперішній час.", "„Szuka” — czas teraźniejszy.", "Szuka is present tense.")],
  ("Niedokonany = процес (англ. Past Continuous).", "Niedokonany = proces (ang. Past Continuous).", "Imperfective = a process (like Past Continuous).")),
 ("Nagle Kevin ____ latarkę w oknie.", ["zobaczył", "widywał", "widzi"], 0,
  [("Так! Nagle + доконаний вид.", "Tak! Nagle + aspekt dokonany.", "Yes! Nagle + perfective."),
   ("Widywał — «бачив часто».", "„Widywał” — często.", "Widywał means “used to see often”."),
   ("Widzi — теперішній час.", "„Widzi” — teraźniejszy.", "Widzi is present.")],
  ("Dokonany = результат, одна подія.", "Dokonany = rezultat, jedno wydarzenie.", "Perfective = a result, one event.")),
]
D[21] = ("Napisz krótki artykuł o Mokrych Bandytach (35+ słów). Co robili? Co się nagle stało? Użyj: kradli, odkręcił, leciała, zobaczył.", 35,
 ("Фон — недоконаний, подія — доконаний.", "Tło — niedokonany, wydarzenie — dokonany.", "Background — imperfective, event — perfective."))

T[22] = ("Czy kiedyś…? Nigdy nie…", "Czy kiedyś…? Nigdy nie…", "Czy kiedyś…? Nigdy nie… (ever / never)")
G[22] = [
 ("Marley ____ nie widział wnuczki z bliska.", ["nigdy", "kiedyś", "zawsze"], 0,
  [("Так! Nigdy + nie — подвійне заперечення.", "Tak! „Nigdy” + „nie” — podwójne przeczenie.", "Yes! Nigdy + nie — Polish uses double negation."),
   ("Kiedyś + nie — неприродно.", "„Kiedyś” + „nie” — nienaturalnie.", "Kiedyś + nie sounds wrong."),
   ("Zawsze nie — помилка.", "„Zawsze nie” — błąd.", "Zawsze nie is wrong.")],
  ("По-польськи: nigdy NIE widziałem (обидва заперечення).", "Po polsku: nigdy NIE widziałem.", "In Polish: nigdy NIE widziałem (both negatives).")),
 ("Czy ____ się bałeś?", ["kiedyś", "nigdy", "nic"], 0,
  [("Так! Kiedyś = колись (у житті).", "Tak! „Kiedyś” = w jakimś momencie życia.", "Yes! Kiedyś = ever."),
   ("Nigdy — для відповіді, не для питання.", "„Nigdy” — do odpowiedzi, nie do pytania.", "Nigdy is for answers, not questions."),
   ("Nic — «нічого».", "„Nic” = żadna rzecz.", "Nic means “nothing”.")],
  ("Польська не має Present Perfect: минулий час + kiedyś/nigdy.", "Polski nie ma Present Perfect: czas przeszły + kiedyś/nigdy.", "Polish has no Present Perfect: past tense + kiedyś/nigdy.")),
]
D[22] = ("Napisz pytania Kevina i odpowiedzi Marleya (35+ słów). Użyj: Czy kiedyś…? Nigdy nie…", 35,
 ("Nigdy + nie + дієслово.", "Nigdy + nie + czasownik.", "Nigdy + nie + verb."))

T[23] = ("Czas przyszły dokonany: obronię, nie ucieknę", "Czas przyszły dokonany: obronię, nie ucieknę", "Perfective future: obronię, nie ucieknę")
G[23] = [
 ("Nie ____! To mój dom!", ["ucieknę", "uciekam", "uciekłem"], 0,
  [("Так! Рішення на майбутнє → доконаний: ucieknę.", "Tak! Decyzja na przyszłość → dokonany: ucieknę.", "Yes! A decision about the future → perfective: ucieknę."),
   ("Uciekam — зараз.", "„Uciekam” — teraz.", "Uciekam is now."),
   ("Uciekłem — у минулому.", "„Uciekłem” — w przeszłości.", "Uciekłem is past.")],
  ("Доконане дієслово в теперішній формі = майбутнє.", "Czasownik dokonany w formie teraźniejszej = przyszłość.", "A perfective verb in present form = future.")),
 ("Obiecuję, że ____ odważny.", ["będę", "byłem", "jestem"], 0,
  [("Так! Обіцянка → będę.", "Tak! Obietnica → będę.", "Yes! A promise → będę."),
   ("Byłem — минуле.", "„Byłem” — przeszłość.", "Byłem is past."),
   ("Jestem — зараз.", "„Jestem” — teraz.", "Jestem is now.")],
  ("Obiecuję, że + майбутній час.", "Obiecuję, że + czas przyszły.", "Obiecuję, że + future tense.")),
]
D[23] = ("Napisz obietnice Kevina na ten wieczór (35+ słów). Użyj: obronię, nie ucieknę, zrobię, obiecuję, że…", 35,
 ("Доконані дієслова: zrobię, obronię, przygotuję.", "Dokonane: zrobię, obronię, przygotuję.", "Perfective: zrobię, obronię, przygotuję."))

T[25] = ("Grzeczne prośby: Poproszę… Chciałabym… Czy mógłby pan…?", "Grzeczne prośby: Poproszę… Chciałabym… Czy mógłby pan…?", "Polite requests: Poproszę… Chciałabym… Czy mógłby pan…?")
G[25] = [
 ("Kate przy okienku: — ____ bilet do Chicago.", ["Poproszę", "Proszę się", "Prosiłam"], 0,
  [("Так! Poproszę + іменник = «дайте, будь ласка».", "Tak! Poproszę + rzeczownik — grzeczna prośba.", "Yes! Poproszę + noun = “I'd like…, please”."),
   ("Proszę się — зворотне, тут не підходить.", "„Proszę się” — forma zwrotna, nie pasuje.", "Proszę się is reflexive and doesn't fit."),
   ("Prosiłam — минуле.", "„Prosiłam” — przeszłość.", "Prosiłam is past.")],
  ("У магазині й на касі: Poproszę kawę / bilet.", "W sklepie i przy kasie: Poproszę kawę / bilet.", "In shops and at desks: Poproszę kawę / bilet.")),
 ("Kate: — ____ wrócić do domu na święta.", ["Chciałabym", "Chciałbym", "Chcę by"], 0,
  [("Так! Кейт — жінка → chciałabym.", "Tak! Kate to kobieta → chciałabym.", "Yes! Kate is a woman → chciałabym."),
   ("Chciałbym — каже чоловік.", "„Chciałbym” mówi mężczyzna.", "Chciałbym is what a man says."),
   ("Chcę by — помилка.", "„Chcę by” — błąd.", "Chcę by is wrong.")],
  ("Умовний спосіб: chciałbym (чол.), chciałabym (жін.).", "Tryb przypuszczający: chciałbym / chciałabym.", "Conditional: chciałbym (male), chciałabym (female).")),
]
D[25] = ("Napisz grzeczną wiadomość do linii lotniczych (35+ słów). Użyj: Poproszę…, Chciałabym/Chciałbym…, Czy mógłby pan / mogłaby pani…?", 35,
 ("Proszę, dziękuję — ввічливі слова.", "Proszę, dziękuję — słowa grzecznościowe.", "Proszę, dziękuję — polite words."))

T[26] = ("Za / zbyt / wystarczająco", "Za / zbyt / wystarczająco", "Za / zbyt / wystarczająco (too / enough)")
G[26] = [
 ("Przykro mi, jest już ____ późno na lot.", ["za", "zbyt dużo", "wystarczająco"], 0,
  [("Так! Za + прикметник/прислівник = надто.", "Tak! Za + przymiotnik/przysłówek.", "Yes! Za + adjective/adverb = too."),
   ("Zbyt dużo — з іменником.", "„Zbyt dużo” — z rzeczownikiem.", "Zbyt dużo goes with nouns."),
   ("Wystarczająco późno — інший зміст.", "„Wystarczająco późno” — inny sens.", "Wystarczająco późno means “late enough”.")],
  ("Za późno, za drogo, za zimno.", "Za późno, za drogo, za zimno.", "Za późno, za drogo, za zimno.")),
 ("Nie ma ____ miejsc w samolocie.", ["wystarczająco", "za", "zbyt"], 0,
  [("Так! Wystarczająco + родовий: miejsc.", "Tak! Wystarczająco + dopełniacz: miejsc.", "Yes! Wystarczająco + genitive: miejsc."),
   ("Za + іменник — помилка.", "„Za” + rzeczownik — błąd.", "Za + noun is wrong."),
   ("Zbyt + іменник — помилка.", "„Zbyt” + rzeczownik — błąd.", "Zbyt + noun is wrong.")],
  ("Також: za mało miejsc = замало місць.", "Także: za mało miejsc.", "Also: za mało miejsc = not enough seats.")),
]
D[26] = ("Napisz wiadomość Kate do Petera ze Scranton (35+ słów). Użyj: za późno, za zimno, za mało miejsc, wystarczająco.", 35,
 ("Za + прикметник; za mało + родовий.", "Za + przymiotnik; za mało + dopełniacz.", "Za + adjective; za mało + genitive."))

T[27] = ("Przysłówki: głośno, cicho, dobrze, źle", "Przysłówki: głośno, cicho, dobrze, źle", "Adverbs: głośno, cicho, dobrze, źle")
G[27] = [
 ("Zespół gra bardzo ____.", ["głośno", "głośny", "głośna"], 0,
  [("Так! Як грає? → прислівник на -o.", "Tak! Jak gra? → przysłówek na -o.", "Yes! How does it play? → adverb in -o."),
   ("Głośny — прикметник: głośny zespół.", "„Głośny” — przymiotnik.", "Głośny is an adjective."),
   ("Głośna — прикметник жін. роду.", "„Głośna” — przymiotnik.", "Głośna is an adjective.")],
  ("Прислівники: -o (głośno, cicho) або -e (dobrze, ładnie).", "Przysłówki: -o (głośno) lub -e (dobrze, ładnie).", "Adverbs end in -o (głośno) or -e (dobrze, ładnie).")),
 ("Gus gra ____ na akordeonie, ale śpiewa źle.", ["dobrze", "dobry", "dobra"], 0,
  [("Так! Dobry → dobrze.", "Tak! Dobry → dobrze.", "Yes! Dobry → dobrze."),
   ("Прикметник.", "Przymiotnik.", "Adjective."),
   ("Прикметник жін. роду.", "Przymiotnik r. żeńskiego.", "Feminine adjective.")],
  ("Dobry → dobrze, zły → źle.", "Dobry → dobrze, zły → źle.", "Dobry → dobrze, zły → źle.")),
]
D[27] = ("Opisz noc w furgonetce zespołu (35+ słów). Użyj: głośno, cicho, dobrze, źle, powoli, ostrożnie.", 35,
 ("Дієслово + прислівник.", "Czasownik + przysłówek.", "Verb + adverb."))

T[28] = ("Jeśli + czas przyszły", "Jeśli + czas przyszły", "Jeśli + future tense (First Conditional)")
G[28] = [
 ("Jeśli ____ całą noc, będziesz w domu rano.", ["pojedziemy", "pojechaliśmy", "pojechalibyśmy"], 0,
  [("Так! Jeśli + майбутній час, як і в другій частині.", "Tak! Jeśli + czas przyszły, jak w drugiej części.", "Yes! Jeśli + future, like the second half."),
   ("Минуле — інший зміст.", "Przeszłość — inny sens.", "The past changes the meaning."),
   ("Умовний спосіб — для нереальних ситуацій.", "Tryb przypuszczający — dla sytuacji nierealnych.", "The conditional mood is for unreal situations.")],
  ("На відміну від англійської: по-польськи після jeśli — майбутній час.", "Inaczej niż po angielsku: po jeśli jest czas przyszły.", "Unlike English, Polish uses the future after jeśli.")),
 ("Jeśli nikt nie otworzy, policjant ____.", ["odjedzie", "odjechał", "odjeżdżał"], 0,
  [("Так! Наслідок — майбутній час.", "Tak! Skutek — czas przyszły.", "Yes! The result — future tense."),
   ("Минуле.", "Przeszłość.", "Past."),
   ("Минуле, недоконаний вид.", "Przeszłość, niedokonany.", "Past imperfective.")],
  ("Jeśli + przyszły, przyszły.", "Jeśli + przyszły, przyszły.", "Jeśli + future, future.")),
]
D[28] = ("Napisz plan Kate na tę noc (35+ słów). Użyj trzech zdań z jeśli: Jeśli drogi będą…, Jeśli policja…, Jeśli dojadę…", 35,
 ("Jeśli + майбутній, майбутній.", "Jeśli + przyszły, przyszły.", "Jeśli + future, future."))

T[29] = ("Kiedy? w niedzielę, w grudniu, o siódmej", "Kiedy? w niedzielę, w grudniu, o siódmej", "When? w niedzielę, w grudniu, o siódmej")
G[29] = [
 ("Nasz lot jest ____ niedzielę.", ["w", "o", "na"], 0,
  [("Так! W + день тижня (знахідний): w niedzielę.", "Tak! W + dzień tygodnia (biernik).", "Yes! W + day of the week (accusative)."),
   ("O — для годин.", "„O” — dla godzin.", "O is for clock times."),
   ("Na niedzielę — «на неділю» (до неділі), інший зміст.", "„Na niedzielę” — inny sens.", "Na niedzielę means “for Sunday”.")],
  ("W poniedziałek, w niedzielę, w Wigilię.", "W poniedziałek, w niedzielę, w Wigilię.", "W poniedziałek, w niedzielę, w Wigilię.")),
 ("Samolot startuje ____ siódmej rano.", ["o", "w", "na"], 0,
  [("Так! O + година (місцевий): o siódmej.", "Tak! O + godzina (miejscownik).", "Yes! O + clock time (locative)."),
   ("W — для днів і місяців.", "„W” — dla dni i miesięcy.", "W is for days and months."),
   ("Na — не з годинами.", "„Na” — nie z godzinami.", "Na isn't used with clock times.")],
  ("O siódmej, o północy; w grudniu (місцевий).", "O siódmej, o północy; w grudniu.", "O siódmej, o północy; w grudniu (locative).")),
]
D[29] = ("Napisz pocztówkę z Paryża od Buzza do Kevina (35+ słów). Użyj: w niedzielę, o siódmej, w grudniu, rano, wieczorem.", 35,
 ("W + день/місяць, o + година.", "W + dzień/miesiąc, o + godzina.", "W + day/month, o + time."))

# ---- Арка 6
T[31] = ("Порядок дій: najpierw, potem, następnie, na koniec", "Kolejność: najpierw, potem, następnie, na koniec", "Sequencing: najpierw, potem, następnie, na koniec")
G[31] = [
 ("____ Kevin polewa schody wodą, potem idzie do drzwi.", ["Najpierw", "Na koniec", "Wreszcie"], 0,
  [("Так! Najpierw = спочатку, перший крок.", "Tak! Najpierw — pierwszy krok.", "Yes! Najpierw = first."),
   ("Na koniec — останній крок.", "„Na koniec” to ostatni krok.", "Na koniec is the last step."),
   ("Wreszcie — «нарешті», після чекання.", "„Wreszcie” — po długim czekaniu.", "Wreszcie = at last, after waiting.")],
  ("Najpierw → potem → następnie → na koniec.", "Najpierw → potem → następnie → na koniec.", "Najpierw → potem → następnie → na koniec.")),
 ("Kevin wiesza puszki. ____ rozkłada zabawki na podłodze.", ["Następnie", "Najpierw", "Wcześniej"], 0,
  [("Так! Następnie = далі, наступним кроком.", "Tak! Następnie — kolejny krok.", "Yes! Następnie = next."),
   ("Najpierw — перший крок, а тут уже другий.", "„Najpierw” — pierwszy krok, a to już drugi.", "Najpierw is the first step."),
   ("Wcześniej — «раніше», назад у часі.", "„Wcześniej” cofa nas w czasie.", "Wcześniej means earlier.")],
  ("Następnie — книжне, potem — розмовне.", "„Następnie” — bardziej książkowe, „potem” — potoczne.", "Następnie is more formal than potem.")),
]
D[31] = ("Napisz plan Kevina jako instrukcję (35+ słów). Użyj: najpierw, potem, następnie, po tym, na koniec.", 35,
 ("Najpierw polej schody… Potem…", "Najpierw polej schody… Potem…", "Najpierw polej schody… Potem…"))

T[32] = ("Почуття і враження: zaskoczony / zaskakujący", "Uczucia i wrażenia: zaskoczony / zaskakujący", "Feelings and impressions: zaskoczony / zaskakujący")
G[32] = [
 ("Bandyci są ____: dom nie jest pusty!", ["zaskoczeni", "zaskakujący", "zaskoczony"], 0,
  [("Так! Що відчувають люди → -ony/-eni: zaskoczeni.", "Tak! Uczucie ludzi → zaskoczeni.", "Yes! How people feel → zaskoczeni."),
   ("Zaskakujący — про річ або ситуацію.", "„Zaskakujący” — o rzeczy lub sytuacji.", "Zaskakujący describes a thing or situation."),
   ("Zaskoczony — однина, а бандитів двоє.", "„Zaskoczony” — liczba pojedyncza.", "Zaskoczony is singular.")],
  ("Ktoś jest zaskoczony; coś jest zaskakujące.", "Ktoś jest zaskoczony; coś jest zaskakujące.", "Ktoś jest zaskoczony; coś jest zaskakujące.")),
 ("Ta noc jest naprawdę ____.", ["przerażająca", "przerażona", "przerażony"], 0,
  [("Так! Noc (річ) → -ąca: przerażająca.", "Tak! Noc (rzecz) → przerażająca.", "Yes! The night (a thing) → przerażająca."),
   ("Przerażona — про людину, яка боїться.", "„Przerażona” — o osobie, która się boi.", "Przerażona describes a frightened person."),
   ("Przerażony — чоловічий рід і про людину.", "„Przerażony” — o mężczyźnie, który się boi.", "Przerażony is about a frightened man.")],
  ("-ący/-ąca — викликає почуття; -ony/-ona — відчуває.", "-ący/-ąca wywołuje uczucie; -ony/-ona je odczuwa.", "-ący causes the feeling; -ony feels it.")),
]
D[32] = ("Opisz dziewiątą wieczorem z dwóch stron: bandytów i Kevina (35+ słów). Użyj par: zaskoczony / zaskakujący, przerażony / przerażający, zmęczony / męczący.", 35,
 ("Człowiek jest -ony, sytuacja jest -ąca.", "Człowiek jest -ony, sytuacja jest -ąca.", "A person is -ony, a situation is -ąca."))

T[33] = ("Щойно, уже, ще не: właśnie, już, jeszcze nie", "Właśnie, już, jeszcze nie", "Just, already, not yet: właśnie, już, jeszcze nie")
G[33] = [
 ("Kevin ____ zadzwonił na policję.", ["właśnie", "jeszcze nie", "nigdy"], 0,
  [("Так! Właśnie + доконаний вид = щойно.", "Tak! Właśnie + aspekt dokonany = przed chwilą.", "Yes! Właśnie + perfective = just."),
   ("Jeszcze nie потребує заперечення: nie zadzwonił.", "„Jeszcze nie” wymaga przeczenia.", "Jeszcze nie needs a negative verb."),
   ("Nigdy — «ніколи», протилежне.", "„Nigdy” to przeciwieństwo.", "Nigdy means never.")],
  ("Польська не має Present Perfect: właśnie / już / jeszcze nie + минулий час.", "Polski nie ma Present Perfect: właśnie / już / jeszcze nie + czas przeszły.", "Polish has no Present Perfect: właśnie / już / jeszcze nie + past tense.")),
 ("Bandyci ____ nie złapali Kevina.", ["jeszcze", "już", "właśnie"], 0,
  [("Так! Jeszcze nie = ще не.", "Tak! Jeszcze nie.", "Yes! Jeszcze nie = not yet."),
   ("Już nie — «уже не» (більше не), інший зміст.", "„Już nie” znaczy „więcej nie”.", "Już nie means no longer."),
   ("Właśnie nie — неприродно.", "„Właśnie nie” brzmi nienaturalnie.", "Właśnie nie sounds unnatural.")],
  ("Już = уже; jeszcze nie = ще не.", "Już; jeszcze nie.", "Już = already; jeszcze nie = not yet.")),
]
D[33] = ("Jesteś Kevinem. Napisz krótkie zgłoszenie na policję (35+ słów): co się właśnie stało, co bandyci już zrobili, a czego jeszcze nie.", 35,
 ("Właśnie…, już…, jeszcze nie…", "Właśnie…, już…, jeszcze nie…", "Właśnie…, już…, jeszcze nie…"))

T[34] = ("Підрядні речення: który / która / które, gdzie", "Zdania względne: który / która / które, gdzie", "Relative clauses: który / która / które, gdzie")
G[34] = [
 ("Marley to sąsiad, ____ uratował Kevina.", ["który", "która", "gdzie"], 0,
  [("Так! Sąsiad — чоловічий рід → który.", "Tak! Sąsiad (r. męski) → który.", "Yes! Sąsiad is masculine → który."),
   ("Która — жіночий рід.", "„Która” — rodzaj żeński.", "Która is feminine."),
   ("Gdzie — про місце.", "„Gdzie” — o miejscu.", "Gdzie is for places.")],
  ("Który/która/które узгоджується з іменником за родом.", "Który/która/które zgadza się z rodzajem rzeczownika.", "Który/która/które agrees in gender with the noun.")),
 ("To jest dom, ____ bandyci złapali Kevina.", ["gdzie", "który", "kto"], 0,
  [("Так! Місце → gdzie.", "Tak! Miejsce → gdzie.", "Yes! A place → gdzie."),
   ("Który потребує прийменника: w którym.", "„Który” wymagałby przyimka: w którym.", "Który would need a preposition: w którym."),
   ("Kto — питання, не підрядне.", "„Kto” to pytanie.", "Kto is a question word.")],
  ("Gdzie = w którym.", "Gdzie = w którym.", "Gdzie = w którym.")),
]
D[34] = ("Napisz kartkę z podziękowaniem od Kevina dla Marleya (35+ słów). Użyj: który, która, które, gdzie.", 35,
 ("Jesteś człowiekiem, który… Dom, gdzie…", "Jesteś człowiekiem, który… Dom, gdzie…", "Jesteś człowiekiem, który… Dom, gdzie…"))
