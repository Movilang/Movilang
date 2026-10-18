# Wersja kursu „Zwierzogród” dla uczących się POLSKIEGO (A1–A2).
G = {}
D = {}
T = {}

# ---- Арка 1
T[1] = ("Być: jestem / jesteś / jest", "Być: jestem / jesteś / jest", "To be: jestem / jesteś / jest")
G[1] = [
 ("Judy: „____ króliczką i jestem odważna!”", ["Jestem", "Jest", "Jesteś"], 0,
  [("Так! Я → jestem.", "Tak! Ja → jestem.", "Yes! I → jestem."),
   ("Jest — він/вона.", "„Jest” — on/ona.", "Jest is he/she."),
   ("Jesteś — ти.", "„Jesteś” — ty.", "Jesteś is you.")],
  ("Ja jestem, ty jesteś, on/ona jest, my jesteśmy, wy jesteście, oni są.", "Ja jestem, ty jesteś, on jest, my jesteśmy, wy jesteście, oni są.", "Ja jestem, ty jesteś, on jest, my jesteśmy, wy jesteście, oni są.")),
 ("Mama: „Tata i ja ____ rolnikami.”", ["jesteśmy", "są", "jestem"], 0,
  [("Так! Ми → jesteśmy.", "Tak! My → jesteśmy.", "Yes! We → jesteśmy."),
   ("Są — вони.", "„Są” — oni.", "Są is they."),
   ("Jestem — я.", "„Jestem” — ja.", "Jestem is I.")],
  ("Після być — орудний відмінок: jestem rolnikiem.", "Po być — narzędnik: jestem rolnikiem.", "After być use the instrumental: jestem rolnikiem.")),
]
D[1] = ("Napisz o sobie (30+ słów). Kim jesteś? Ile masz lat? Skąd jesteś? Jakie jest twoje marzenie?", 30,
 ("Jestem… Mam … lat. Jestem z… Moje marzenie to…", "Jestem… Mam … lat. Jestem z… Moje marzenie to…", "Jestem… Mam … lat. Jestem z… Moje marzenie to…"))

T[2] = ("Umiem / mogę / nie umiem", "Umiem / mogę / nie umiem", "Umiem / mogę / nie umiem (can / can't)")
G[2] = [
 ("Judy jest mała, ale ____ wysoko skakać.", ["umie", "umiem", "umiesz"], 0,
  [("Так! Вона → umie.", "Tak! Ona → umie.", "Yes! She → umie."),
   ("Umiem — я.", "„Umiem” — ja.", "Umiem is I."),
   ("Umiesz — ти.", "„Umiesz” — ty.", "Umiesz is you.")],
  ("Umieć + інфінітив: umiem pływać.", "Umieć + bezokolicznik: umiem pływać.", "Umieć + infinitive: umiem pływać.")),
 ("Instruktorka: „Nie ____ wejść na tę ścianę!”", ["dasz rady", "dajesz rady", "dać rady"], 0,
  [("Так! Не впораєшся → nie dasz rady.", "Tak! Nie dasz rady.", "Yes! Nie dasz rady = you can't do it."),
   ("Dajesz — теперішній, не той зміст.", "„Dajesz” — inny sens.", "Different meaning."),
   ("Dać — інфінітив.", "„Dać” — bezokolicznik.", "Dać is the infinitive.")],
  ("Can't = nie umiem / nie mogę / nie dam rady.", "Can't = nie umiem / nie mogę / nie dam rady.", "Can't = nie umiem / nie mogę / nie dam rady.")),
]
D[2] = ("Jesteś Judy w akademii. Napisz do rodziców (30+ słów): co umiesz, czego jeszcze nie umiesz.", 30,
 ("Umiem… Jeszcze nie umiem… Mogę… Nie mogę…", "Umiem… Jeszcze nie umiem… Mogę… Nie mogę…", "Umiem… Jeszcze nie umiem… Mogę… Nie mogę…"))

T[3] = ("Mam / masz / ma", "Mam / masz / ma", "Mieć: mam / masz / ma (have got)")
G[3] = [
 ("Judy ____ walizkę, bilet i telefon.", ["ma", "mam", "mają"], 0,
  [("Так! Вона → ma.", "Tak! Ona → ma.", "Yes! She → ma."),
   ("Mam — я.", "„Mam” — ja.", "Mam is I."),
   ("Mają — вони.", "„Mają” — oni.", "Mają is they.")],
  ("Mieć: mam, masz, ma, mamy, macie, mają.", "Mieć: mam, masz, ma, mamy, macie, mają.", "Mieć: mam, masz, ma, mamy, macie, mają.")),
 ("Mama: „Czy ____ telefon, Judy?”", ["masz", "ma", "mam"], 0,
  [("Так! Ти → masz.", "Tak! Ty → masz.", "Yes! You → masz."),
   ("Ma — він/вона.", "„Ma” — on/ona.", "Ma is he/she."),
   ("Mam — я.", "„Mam” — ja.", "Mam is I.")],
  ("Питання: Czy masz…?", "Pytanie: Czy masz…?", "Question: Czy masz…?")),
]
D[3] = ("Napisz o swojej torbie (30+ słów). Co w niej masz? Czego nie masz? (Po „nie mam” — dopełniacz: nie mam telefonu.)", 30,
 ("W torbie mam… Nie mam… Mój przyjaciel ma…", "W torbie mam… Nie mam… Mój przyjaciel ma…", "W torbie mam… Nie mam… Mój przyjaciel ma…"))

T[4] = ("Jest / są + w / na / pod / obok", "Jest / są + w / na / pod / obok", "Jest / są + w / na / pod / obok (there is / are)")
G[4] = [
 ("W pokoju Judy ____ łóżko i mały stolik.", ["jest", "są", "ma"], 0,
  [("Так! Перед łóżko (однина) → jest.", "Tak! Przed „łóżko” → jest.", "Yes! Before łóżko (singular) → jest."),
   ("Są — для множини.", "„Są” — dla l. mnogiej.", "Są is plural."),
   ("Ma — «має».", "„Ma” — posiadanie.", "Ma means has.")],
  ("There is = jest, there are = są.", "There is = jest, there are = są.", "There is = jest, there are = są.")),
 ("Walizka jest pod ____.", ["łóżkiem", "łóżko", "łóżka"], 0,
  [("Так! Pod + орудний → łóżkiem.", "Tak! Pod + narzędnik → łóżkiem.", "Yes! Pod + instrumental → łóżkiem."),
   ("Łóżko — називний.", "„Łóżko” — mianownik.", "Łóżko is nominative."),
   ("Łóżka — родовий.", "„Łóżka” — dopełniacz.", "Łóżka is genitive.")],
  ("Pod / nad / za / przed + narzędnik; w / na + miejscownik.", "Pod / nad / za / przed + narzędnik; w / na + miejscownik.", "Pod / nad / za / przed + instrumental; w / na + locative.")),
]
D[4] = ("Opisz swój pokój (30+ słów). Co jest w pokoju? Gdzie to jest? Użyj: jest, są, w, na, pod, obok.", 30,
 ("W moim pokoju jest… Są… … jest obok… … jest pod…", "W moim pokoju jest… Są… … jest obok… … jest pod…", "W moim pokoju jest… Są… … jest obok… … jest pod…"))

T[5] = ("Czas teraźniejszy: pracuję / pracuje / nie pracuje", "Czas teraźniejszy: pracuję / pracuje / nie pracuje", "Present tense: pracuję / pracuje / nie pracuje")
G[5] = [
 ("Clawhauser ____ pączki każdego ranka.", ["je", "jem", "jedzą"], 0,
  [("Так! Він → je.", "Tak! On → je.", "Yes! He → je."),
   ("Jem — я.", "„Jem” — ja.", "Jem is I."),
   ("Jedzą — вони.", "„Jedzą” — oni.", "Jedzą is they.")],
  ("Jeść: jem, jesz, je, jemy, jecie, jedzą.", "Jeść: jem, jesz, je, jemy, jecie, jedzą.", "Jeść: jem, jesz, je, jemy, jecie, jedzą.")),
 ("Komendant Bogo ____ daje Judy sprawy.", ["nie", "nic", "nigdy nie nie"], 0,
  [("Так! Заперечення: nie + дієслово.", "Tak! Przeczenie: nie + czasownik.", "Yes! Negative: nie + verb."),
   ("Nic — «нічого».", "„Nic” — rzecz.", "Nic means nothing."),
   ("Неправильно.", "Błąd.", "Wrong.")],
  ("У польській: просто nie перед дієсловом.", "Po polsku: nie przed czasownikiem.", "Polish: just nie before the verb.")),
]
D[5] = ("Napisz o swoim dniu (30+ słów). O której wstajesz? Co robisz? Co robi twoja mama lub przyjaciel?", 30,
 ("Wstaję o… Idę do… Moja mama pracuje… Ona nie… Zwykle…", "Wstaję o… Idę do… Moja mama pracuje… Ona nie… Zwykle…", "Wstaję o… Idę do… Moja mama pracuje… Ona nie… Zwykle…"))

# ---- Арка 2
T[7] = ("Teraz: co robisz? — kupuję", "Teraz: co robisz? — kupuję", "Right now: co robisz? — kupuję")
G[7] = [
 ("Patrz! Lis ____ do lodziarni.", ["wchodzi", "wchodził", "wejdzie"], 0,
  [("Так! Зараз → теперішній час.", "Tak! Teraz → czas teraźniejszy.", "Yes! Now → present tense."),
   ("Wchodził — минуле.", "„Wchodził” — przeszłość.", "Wchodził is past."),
   ("Wejdzie — майбутнє.", "„Wejdzie” — przyszłość.", "Wejdzie is future.")],
  ("У польській немає окремого -ing: «зараз» і «завжди» — один теперішній час.", "Po polsku jeden czas teraźniejszy: teraz i zawsze.", "Polish has one present tense for “now” and “always”.")),
 ("Judy: „Co tu ____?” Nick: „Kupuję lody.”", ["robisz", "robi", "robię"], 0,
  [("Так! Ти → robisz.", "Tak! Ty → robisz.", "Yes! You → robisz."),
   ("Robi — він.", "„Robi” — on.", "Robi is he."),
   ("Robię — я.", "„Robię” — ja.", "Robię is I.")],
  ("What are you doing? = Co robisz?", "What are you doing? = Co robisz?", "What are you doing? = Co robisz?")),
]
D[7] = ("Rozejrzyj się. Napisz (30+ słów): co teraz robisz? Co robią ludzie lub zwierzęta obok ciebie?", 30,
 ("Teraz piszę… Mama gotuje… Kot śpi… Na ulicy ludzie…", "Teraz piszę… Mama gotuje… Kot śpi… Na ulicy ludzie…", "Teraz piszę… Mama gotuje… Kot śpi… Na ulicy ludzie…"))

T[8] = ("Trochę / kilka / żadnego + dopełniacz", "Trochę / kilka / żadnego + dopełniacz", "Trochę / kilka / żadnego + genitive (some / any)")
G[8] = [
 ("Nick potrzebuje trochę ____.", ["soku", "sok", "sokiem"], 0,
  [("Так! Trochę + родовий → soku.", "Tak! Trochę + dopełniacz → soku.", "Yes! Trochę + genitive → soku."),
   ("Sok — називний.", "„Sok” — mianownik.", "Sok is nominative."),
   ("Sokiem — орудний.", "„Sokiem” — narzędnik.", "Sokiem is instrumental.")],
  ("Trochę wody, trochę soku, kilka wiader.", "Trochę wody, trochę soku, kilka wiader.", "Trochę wody, trochę soku, kilka wiader.")),
 ("Judy nie ma żadnych ____.", ["dowodów", "dowody", "dowodami"], 0,
  [("Так! Nie ma + родовий → dowodów.", "Tak! Nie ma + dopełniacz → dowodów.", "Yes! Nie ma + genitive → dowodów."),
   ("Dowody — називний.", "„Dowody” — mianownik.", "Dowody is nominative."),
   ("Dowodami — орудний.", "„Dowodami” — narzędnik.", "Dowodami is instrumental.")],
  ("Any у запереченні = żaden / żadnych + dopełniacz.", "Any w przeczeniu = żaden + dopełniacz.", "Any in negatives = żaden + genitive.")),
]
D[8] = ("Napisz listę zakupów na przyjęcie (30+ słów). Co masz? Czego nie masz? Czego potrzebujesz? Użyj: trochę, kilka, nie mam…", 30,
 ("Mam trochę… Nie mam… Potrzebuję kilka… Czy mamy…?", "Mam trochę… Nie mam… Potrzebuję kilka… Czy mamy…?", "Mam trochę… Nie mam… Potrzebuję kilka… Czy mamy…?"))

T[9] = ("Tryb rozkazujący: znajdź! nie płacz! chodźmy!", "Tryb rozkazujący: znajdź! nie płacz! chodźmy!", "Imperative: znajdź! nie płacz! chodźmy!")
G[9] = [
 ("Pani Otterton: „Proszę, ____ mojego męża!”", ["znajdźcie", "znaleźć", "znajduje"], 0,
  [("Так! Наказ для кількох → znajdźcie.", "Tak! Rozkaz do kilku osób → znajdźcie.", "Yes! Imperative to several people → znajdźcie."),
   ("Znaleźć — інфінітив.", "„Znaleźć” — bezokolicznik.", "Znaleźć is the infinitive."),
   ("Znajduje — він.", "„Znajduje” — on.", "Znajduje is he.")],
  ("Ty: znajdź! · wy: znajdźcie! · my: znajdźmy!", "Ty: znajdź! · wy: znajdźcie! · my: znajdźmy!", "Ty: znajdź! · wy: znajdźcie! · my: znajdźmy!")),
 ("Judy: „____ zaczynać! Mamy tylko 48 godzin.”", ["Zacznijmy", "Zaczynam", "Zaczął"], 0,
  [("Так! Let's start = zacznijmy.", "Tak! Let's start = zacznijmy.", "Yes! Let's start = zacznijmy."),
   ("Zaczynam — я.", "„Zaczynam” — ja.", "Zaczynam is I."),
   ("Zaczął — минуле.", "„Zaczął” — przeszłość.", "Zaczął is past.")],
  ("Let's = форма «my» з -my: chodźmy, zróbmy.", "Let's = forma z -my: chodźmy, zróbmy.", "Let's = the -my form: chodźmy, zróbmy.")),
]
D[9] = ("Napisz 6 zasad dla nowego policjanta w Zwierzogrodzie (30+ słów). Użyj trybu rozkazującego: Bądź…, Nie…, Zawsze…, Pomagaj…, Chodźmy…", 30,
 ("Bądź… Nie… Zawsze… Pomagaj… Chodźmy…", "Bądź… Nie… Zawsze… Pomagaj… Chodźmy…", "Bądź… Nie… Zawsze… Pomagaj… Chodźmy…"))

T[10] = ("Był / była / byli / były", "Był / była / byli / były", "Past of być: był / była / byli")
G[10] = [
 ("Wydra ____ klientem Nicka.", ["była", "był", "byli"], 0,
  [("Так! Wydra — жіночий рід → była.", "Tak! Wydra (ż.) → była.", "Yes! Wydra is feminine → była."),
   ("Był — чоловічий.", "„Był” — r. męski.", "Był is masculine."),
   ("Byli — множина.", "„Byli” — l. mnoga.", "Byli is plural.")],
  ("Він був, вона була, воно було, вони були/były.", "On był, ona była, ono było, oni byli, one były.", "On był, ona była, ono było, oni byli, one były.")),
 ("Judy: „Gdzie ____ wczoraj, Nick?”", ["byłeś", "byłam", "był"], 0,
  [("Так! Ти (чол.) → byłeś.", "Tak! Ty (m.) → byłeś.", "Yes! You (male) → byłeś."),
   ("Byłam — я (жін.).", "„Byłam” — ja (ż.).", "Byłam is I (female)."),
   ("Był — він.", "„Był” — on.", "Był is he.")],
  ("Byłem / byłam, byłeś / byłaś, był / była.", "Byłem / byłam, byłeś / byłaś, był / była.", "Byłem / byłam, byłeś / byłaś, był / była.")),
]
D[10] = ("Napisz o wczorajszym dniu (30+ słów). Gdzie byłeś/byłaś? Z kim? Czy było fajnie? Użyj: byłem/byłam, był, była, byli, nie było.", 30,
 ("Wczoraj byłam… Moi przyjaciele byli… Było… Nie byłam…", "Wczoraj byłam… Moi przyjaciele byli… Było… Nie byłam…", "Wczoraj byłam… Moi przyjaciele byli… Było… Nie byłam…"))

T[11] = ("Czas przeszły: rozmawiałem / zapytała / zatrzymał się", "Czas przeszły: rozmawiałem / zapytała", "Past tense: rozmawiałem / zapytała")
G[11] = [
 ("Yax: „Wydra ____ tu co wtorek.”", ["przychodziła", "przychodzi", "przyjdzie"], 0,
  [("Так! Минуле, жін. рід → -ła.", "Tak! Przeszłość, r. ż. → -ła.", "Yes! Past, feminine → -ła."),
   ("Przychodzi — теперішній.", "„Przychodzi” — teraźniejszy.", "Przychodzi is present."),
   ("Przyjdzie — майбутнє.", "„Przyjdzie” — przyszłość.", "Przyjdzie is future.")],
  ("Минуле: -łem/-łam (я), -ł/-ła (він/вона), -li/-ły (вони).", "Przeszły: -łem/-łam, -ł/-ła, -li/-ły.", "Past: -łem/-łam (I), -ł/-ła (he/she), -li/-ły (they).")),
 ("Judy ____ Yaxa o samochód.", ["zapytała", "zapytał", "zapytałem"], 0,
  [("Так! Judy (вона) → zapytała.", "Tak! Judy (ona) → zapytała.", "Yes! Judy (she) → zapytała."),
   ("Zapytał — він.", "„Zapytał” — on.", "Zapytał is he."),
   ("Zapytałem — я (чол.).", "„Zapytałem” — ja (m.).", "Zapytałem is I (male).")],
  ("Рід важливий у минулому часі!", "Rodzaj jest ważny w czasie przeszłym!", "Gender matters in the past tense!")),
]
D[11] = ("Napisz o zeszłym weekendzie (30+ słów). Co robiłeś/robiłaś? Użyj: grałem/grałam, oglądałem/oglądałam, odwiedziłem/odwiedziłam, nie…", 30,
 ("W weekend grałam… Oglądałam… Odwiedziłam… Nie…", "W weekend grałam… Oglądałam… Odwiedziłam… Nie…", "W weekend grałam… Oglądałam… Odwiedziłam… Nie…"))

# ---- Арка 3
T[13] = ("Przeszłość: poszedł, zobaczył, wziął, przyszedł", "Przeszłość: poszedł, zobaczył, wziął", "Past: poszedł, zobaczył, wziął")
G[13] = [
 ("Nick i Judy ____ do urzędu.", ["poszli", "poszedł", "poszła"], 0,
  [("Так! Вони (чол. + жін.) → poszli.", "Tak! Oni → poszli.", "Yes! They (mixed) → poszli."),
   ("Poszedł — він.", "„Poszedł” — on.", "Poszedł is he."),
   ("Poszła — вона.", "„Poszła” — ona.", "Poszła is she.")],
  ("Iść: poszedłem/poszłam, poszedł/poszła, poszli/poszły.", "Iść: poszedłem/poszłam, poszedł/poszła, poszli/poszły.", "Iść: poszedłem/poszłam, poszedł/poszła, poszli/poszły.")),
 ("Flash w końcu ____ nazwę firmy.", ["znalazł", "znalazła", "znajdzie"], 0,
  [("Так! Флеш (він) → znalazł.", "Tak! Flash (on) → znalazł.", "Yes! Flash (he) → znalazł."),
   ("Znalazła — вона.", "„Znalazła” — ona.", "Znalazła is she."),
   ("Znajdzie — майбутнє.", "„Znajdzie” — przyszłość.", "Znajdzie is future.")],
  ("Znaleźć → znalazł, znalazła.", "Znaleźć → znalazł, znalazła.", "Znaleźć → znalazł, znalazła.")),
]
D[13] = ("Opisz dzień, kiedy coś trwało wieki (30+ słów). Dokąd poszedłeś/poszłaś? Co zobaczyłeś/zobaczyłaś? Co dostałeś/dostałaś?", 30,
 ("W zeszłym miesiącu poszłam… Zobaczyłam… To trwało… W końcu dostałam…", "W zeszłym miesiącu poszłam… Zobaczyłam… To trwało… W końcu dostałam…", "W zeszłym miesiącu poszłam… Zobaczyłam… To trwało… W końcu dostałam…"))

T[14] = ("Pytania w przeszłości: Czy widziałeś? Gdzie poszedł?", "Pytania w przeszłości", "Past questions: Czy widziałeś? Gdzie poszedł?")
G[14] = [
 ("Pan Big: „____ przyszliście skrzywdzić moją rodzinę?”", ["Czy", "Co", "Gdzie"], 0,
  [("Так! Питання так/ні → Czy.", "Tak! Pytanie tak/nie → Czy.", "Yes! Yes/no question → Czy."),
   ("Co — «що».", "„Co” — rzecz.", "Co means what."),
   ("Gdzie — «де».", "„Gdzie” — miejsce.", "Gdzie means where.")],
  ("Did you…? = Czy + минулий час…?", "Did you…? = Czy + przeszły…?", "Did you…? = Czy + past…?")),
 ("Judy: „Dokąd ____ wydra po imprezie?”", ["pojechała", "pojedzie", "jedzie"], 0,
  [("Так! Минуле, видра (жін.) → pojechała.", "Tak! Przeszłość, wydra (ż.) → pojechała.", "Yes! Past, wydra (f.) → pojechała."),
   ("Pojedzie — майбутнє.", "„Pojedzie” — przyszłość.", "Pojedzie is future."),
   ("Jedzie — теперішній.", "„Jedzie” — teraźniejszy.", "Jedzie is present.")],
  ("У польській немає did: Dokąd pojechała?", "Po polsku nie ma did.", "Polish has no did: Dokąd pojechała?")),
]
D[14] = ("Przeprowadź wywiad z przyjacielem o weekendzie. Napisz 6 pytań i odpowiedzi (30+ słów). Użyj: Czy…? Gdzie…? Co…? Z kim…?", 30,
 ("Czy byłeś…? Tak. Gdzie poszedłeś? Poszedłem… Co jadłeś?", "Czy byłeś…? Tak. Gdzie poszedłeś? Poszedłem… Co jadłeś?", "Czy byłeś…? Tak. Gdzie poszedłeś? Poszedłem… Co jadłeś?"))

T[15] = ("Zaimki: mnie, go, ją, nas, ich", "Zaimki: mnie, go, ją, nas, ich", "Object pronouns: mnie, go, ją, nas, ich")
G[15] = [
 ("Nick spada! Judy: „Trzymaj się ____!”", ["mnie", "ja", "mój"], 0,
  [("Так! Trzymać się + родовий → mnie.", "Tak! Trzymać się + dopełniacz → mnie.", "Yes! Trzymać się + genitive → mnie."),
   ("Ja — підмет.", "„Ja” — podmiot.", "Ja is a subject."),
   ("Mój — «мій».", "„Mój” — dzierżawczy.", "Mój is possessive.")],
  ("Ja → mnie, ty → cię/ciebie, on → go/jego, ona → ją/jej, my → nas, oni → ich.", "Ja → mnie, on → go, ona → ją, my → nas, oni → ich.", "Ja → mnie, on → go, ona → ją, my → nas, oni → ich.")),
 ("Manchas biegnie za Judy i Nickiem. Widzi ____!", ["ich", "oni", "im"], 0,
  [("Так! Widzieć + знахідний → ich.", "Tak! Widzieć + biernik → ich.", "Yes! Widzieć + accusative → ich."),
   ("Oni — підмет.", "„Oni” — podmiot.", "Oni is a subject."),
   ("Im — давальний.", "„Im” — celownik.", "Im is dative.")],
  ("Widzę go / ją / ich. Daję mu / jej / im.", "Widzę go / ją / ich. Daję mu / jej / im.", "Widzę go / ją / ich. Daję mu / jej / im.")),
]
D[15] = ("Napisz o przyjacielu, który ci pomógł (30+ słów). Co się stało? Jak ci pomógł? Użyj: mnie, mi, go, mu, ją, jej, nas, ich.", 30,
 ("Mój przyjaciel pomógł mi, kiedy… Zadzwoniłam do niego… Dał mi… My…", "Mój przyjaciel pomógł mi, kiedy… Zadzwoniłam do niego… Dał mi… My…", "Mój przyjaciel pomógł mi, kiedy… Zadzwoniłam do niego… Dał mi… My…"))

T[16] = ("Stopień wyższy: większy, szybszy, bardziej niebezpieczny", "Stopień wyższy", "Comparatives: większy, szybszy, bardziej")
G[16] = [
 ("Komendant Bogo jest ____ niż Judy.", ["większy", "duży", "największy"], 0,
  [("Так! Порівняння → większy.", "Tak! Porównanie → większy.", "Yes! Comparison → większy."),
   ("Duży — звичайна форма.", "„Duży” — stopień równy.", "Duży is the base form."),
   ("Największy — найвищий ступінь.", "„Największy” — stopień najwyższy.", "Największy is the superlative.")],
  ("Duży → większy, dobry → lepszy, mały → mniejszy.", "Duży → większy, dobry → lepszy.", "Duży → większy, dobry → lepszy, mały → mniejszy.")),
 ("Manchas jest teraz ____ niebezpieczny niż zwykły jaguar.", ["bardziej", "więcej", "najbardziej"], 0,
  [("Так! Довгі прикметники → bardziej.", "Tak! Długie przymiotniki → bardziej.", "Yes! Long adjectives → bardziej."),
   ("Więcej — про кількість.", "„Więcej” — o ilości.", "Więcej is about amount."),
   ("Najbardziej — найвищий.", "„Najbardziej” — najwyższy.", "Najbardziej is the superlative.")],
  ("More dangerous = bardziej niebezpieczny.", "More dangerous = bardziej niebezpieczny.", "More dangerous = bardziej niebezpieczny.")),
]
D[16] = ("Porównaj dwie osoby lub dwa zwierzęta (30+ słów). Kto jest większy, szybszy, milszy, bardziej interesujący? Użyj: …-szy niż, bardziej … niż.", 30,
 ("Mój kot jest mniejszy niż pies. Pies jest szybszy… Siostra jest bardziej…", "Mój kot jest mniejszy niż pies. Pies jest szybszy… Siostra jest bardziej…", "Mój kot jest mniejszy niż pies. Pies jest szybszy… Siostra jest bardziej…"))

T[17] = ("Plany: zamierzam / będę + bezokolicznik", "Plany: zamierzam / będę + bezokolicznik", "Plans: zamierzam / będę + infinitive")
G[17] = [
 ("Judy: „Dziś wieczorem ____ śledzić wilki.”", ["będziemy", "byliśmy", "jesteśmy"], 0,
  [("Так! Майбутнє: będziemy + інфінітив.", "Tak! Przyszłość: będziemy + bezokolicznik.", "Yes! Future: będziemy + infinitive."),
   ("Byliśmy — минуле.", "„Byliśmy” — przeszłość.", "Byliśmy is past."),
   ("Jesteśmy — теперішній.", "„Jesteśmy” — teraźniejszy.", "Jesteśmy is present.")],
  ("Going to = zamierzam / będę + bezokolicznik.", "Going to = zamierzam / będę.", "Going to = zamierzam / będę + infinitive.")),
 ("Bellwether: „____ wam pomóc!”", ["Zamierzam", "Zamierzała", "Zamierzaliśmy"], 0,
  [("Так! Я → zamierzam.", "Tak! Ja → zamierzam.", "Yes! I → zamierzam."),
   ("Zamierzała — минуле.", "„Zamierzała” — przeszłość.", "Zamierzała is past."),
   ("Неправильна особа.", "Zła osoba.", "Wrong person.")],
  ("Zamierzam + bezokolicznik.", "Zamierzam + bezokolicznik.", "Zamierzam + infinitive.")),
]
D[17] = ("Napisz o planach na następny weekend (30+ słów). Co zamierzasz robić? Czego nie zamierzasz? Czy będzie padać?", 30,
 ("W weekend zamierzam… Moi przyjaciele będą… Nie zamierzam… Będzie…", "W weekend zamierzam… Moi przyjaciele będą… Nie zamierzam… Będzie…", "W weekend zamierzam… Moi przyjaciele będą… Nie zamierzam… Będzie…"))

# ---- Арка 4
T[19] = ("Stopień najwyższy: największy, najgorszy, najbardziej", "Stopień najwyższy", "Superlatives: największy, najgorszy, najbardziej")
G[19] = [
 ("To jest ____ klif za miastem.", ["najwyższy", "wyższy", "wysoki"], 0,
  [("Так! Найвищий ступінь → naj-.", "Tak! Stopień najwyższy → naj-.", "Yes! Superlative → naj-."),
   ("Wyższy — порівняння.", "„Wyższy” — stopień wyższy.", "Wyższy is a comparative."),
   ("Wysoki — звичайна форма.", "„Wysoki” — stopień równy.", "Wysoki is the base form.")],
  ("Naj- + stopień wyższy: wyższy → najwyższy, lepszy → najlepszy.", "Naj- + stopień wyższy.", "Naj- + comparative: wyższy → najwyższy.")),
 ("To są ____ niebezpieczne zwierzęta w mieście.", ["najbardziej", "bardziej", "bardzo bardzo"], 0,
  [("Так! Довгі → najbardziej.", "Tak! Długie → najbardziej.", "Yes! Long ones → najbardziej."),
   ("Bardziej — порівняння.", "„Bardziej” — stopień wyższy.", "Bardziej is a comparative."),
   ("Неправильно.", "Błąd.", "Wrong.")],
  ("The most dangerous = najbardziej niebezpieczny.", "The most dangerous = najbardziej niebezpieczny.", "The most dangerous = najbardziej niebezpieczny.")),
]
D[19] = ("Napisz o najlepszych i najgorszych miejscach w twoim mieście (30+ słów). Użyj: największy, najlepszy, najbardziej…, najgorszy.", 30,
 ("Największy budynek w moim mieście to… Najlepsza kawiarnia to… Najbardziej interesujące miejsce…", "Największy budynek w moim mieście to… Najlepsza kawiarnia to… Najbardziej interesujące miejsce…", "Największy budynek w moim mieście to… Najlepsza kawiarnia to… Najbardziej interesujące miejsce…"))

T[20] = ("Musieć / nie wolno / nie trzeba", "Musieć / nie wolno / nie trzeba", "Must = musieć, mustn't = nie wolno")
G[20] = [
 ("Judy: „____ zadzwonić do komendanta!”", ["Musimy", "Musimy się", "Musiał"], 0,
  [("Так! Ми → musimy + інфінітив.", "Tak! My → musimy + bezokolicznik.", "Yes! We → musimy + infinitive."),
   ("Się тут зайве.", "Zbędne się.", "No się here."),
   ("Musiał — минуле.", "„Musiał” — przeszłość.", "Musiał is past.")],
  ("Muszę, musisz, musi, musimy, musicie, muszą.", "Muszę, musisz, musi, musimy, musicie, muszą.", "Muszę, musisz, musi, musimy, musicie, muszą.")),
 ("Nick: „____ zgubić tego telefonu!”", ["Nie wolno ci", "Nie musisz", "Nie musi"], 0,
  [("Так! Mustn't = nie wolno.", "Tak! Mustn't = nie wolno.", "Yes! Mustn't = nie wolno."),
   ("Nie musisz = don't have to.", "„Nie musisz” = don't have to.", "Nie musisz = don't have to."),
   ("Nie musi — він.", "„Nie musi” — on.", "Nie musi is he.")],
  ("Mustn't = nie wolno · don't have to = nie musisz.", "Mustn't = nie wolno · don't have to = nie musisz.", "Mustn't = nie wolno · don't have to = nie musisz.")),
]
D[20] = ("Napisz zasady w domu lub w szkole (30+ słów). Co musisz robić? Czego nie wolno? Co musisz robić codziennie?", 30,
 ("W domu muszę… Nie wolno mi… Codziennie muszę… W szkole musimy…", "W domu muszę… Nie wolno mi… Codziennie muszę… W szkole musimy…", "W domu muszę… Nie wolno mi… Codziennie muszę… W szkole musimy…"))

T[21] = ("Rada: powinieneś / powinnaś / nie powinieneś", "Rada: powinieneś / powinnaś", "Advice: powinieneś / powinnaś")
G[21] = [
 ("Nick: „Nie ____ mówić za dużo, Carrots.”", ["powinnaś", "powinieneś", "powinna"], 0,
  [("Так! До Джуді (жін., ти) → powinnaś.", "Tak! Do Judy (ty, ż.) → powinnaś.", "Yes! To Judy (you, f.) → powinnaś."),
   ("Powinieneś — до чоловіка.", "„Powinieneś” — do mężczyzny.", "Powinieneś is to a male."),
   ("Powinna — вона.", "„Powinna” — ona.", "Powinna is she.")],
  ("Powinienem/powinnam, powinieneś/powinnaś, powinien/powinna.", "Powinienem/powinnam, powinieneś/powinnaś…", "Powinienem/powinnam, powinieneś/powinnaś, powinien/powinna.")),
 ("Judy: „Co ____ teraz powiedzieć Nickowi?”", ["powinnam", "powinna", "powinnaś"], 0,
  [("Так! Я (жін.) → powinnam.", "Tak! Ja (ż.) → powinnam.", "Yes! I (f.) → powinnam."),
   ("Powinna — вона.", "„Powinna” — ona.", "Powinna is she."),
   ("Powinnaś — ти.", "„Powinnaś” — ty.", "Powinnaś is you.")],
  ("Should I…? = Czy powinnam/powinienem…?", "Should I…? = Czy powinnam…?", "Should I…? = Czy powinnam/powinienem…?")),
]
D[21] = ("Daj radę Judy (30+ słów). Co powinna zrobić? Czego nie powinna? Użyj: powinnaś, nie powinnaś, Nick powinien…", 30,
 ("Judy, powinnaś… Nie powinnaś… Powinnaś powiedzieć… Nick powinien…", "Judy, powinnaś… Nie powinnaś… Powinnaś powiedzieć… Nick powinien…", "Judy, powinnaś… Nie powinnaś… Powinnaś powiedzieć… Nick powinien…"))

T[22] = ("Szłam, kiedy… (aspekt niedokonany + dokonany)", "Szłam, kiedy… (aspekt)", "Was walking when… = szłam, kiedy…")
G[22] = [
 ("Kiedy Judy ____ ulicą, mama-królica odciągnęła dziecko.", ["szła", "poszła", "pójdzie"], 0,
  [("Так! Тривала дія → недоконаний: szła.", "Tak! Czynność trwająca → niedokonany: szła.", "Yes! An ongoing action → imperfective: szła."),
   ("Poszła — одна завершена дія.", "„Poszła” — czynność zakończona.", "Poszła is a finished action."),
   ("Pójdzie — майбутнє.", "„Pójdzie” — przyszłość.", "Pójdzie is future.")],
  ("Past Continuous = niedokonany (robiłam), Past Simple часто = dokonany (zrobiłam).", "Past Continuous = niedokonany; Past Simple = dokonany.", "Past Continuous ≈ imperfective; Past Simple ≈ perfective.")),
 ("Podczas gdy zwierzęta ____ w autobusie, nikt nic nie powiedział.", ["siedziały", "usiadły", "siądą"], 0,
  [("Так! Тривала дія → siedziały.", "Tak! Trwanie → siedziały.", "Yes! Ongoing → siedziały."),
   ("Usiadły — разова дія.", "„Usiadły” — jednorazowo.", "Usiadły is a single action."),
   ("Siądą — майбутнє.", "„Siądą” — przyszłość.", "Siądą is future.")],
  ("Podczas gdy + niedokonany.", "Podczas gdy + niedokonany.", "Podczas gdy + imperfective.")),
]
D[22] = ("Opisz chwilę, którą pamiętasz (30+ słów). Co robiłeś/robiłaś? Co robili ludzie obok? Co się wtedy stało?", 30,
 ("Szłam… kiedy… Moi przyjaciele siedzieli… Podczas gdy…, nagle…", "Szłam… kiedy… Moi przyjaciele siedzieli… Podczas gdy…, nagle…", "Szłam… kiedy… Moi przyjaciele siedzieli… Podczas gdy…, nagle…"))

T[23] = ("Przysłówki: smutno, cicho, dobrze, szybko", "Przysłówki: smutno, cicho, dobrze", "Adverbs: smutno, cicho, dobrze, szybko")
G[23] = [
 ("Judy patrzy ____ na pustą drogę.", ["smutno", "smutna", "smutny"], 0,
  [("Так! Як? → прислівник smutno.", "Tak! Jak? → przysłówek smutno.", "Yes! How? → adverb smutno."),
   ("Smutna — прикметник.", "„Smutna” — przymiotnik.", "Smutna is an adjective."),
   ("Smutny — прикметник.", "„Smutny” — przymiotnik.", "Smutny is an adjective.")],
  ("Przysłówek często na -o / -ie: smutno, cicho, dobrze, ładnie.", "Przysłówek na -o / -ie.", "Polish adverbs often end in -o / -ie.")),
 ("Gideon piecze bardzo ____.", ["dobrze", "dobry", "dobra"], 0,
  [("Так! Як? → dobrze.", "Tak! Jak? → dobrze.", "Yes! How? → dobrze."),
   ("Dobry — прикметник.", "„Dobry” — przymiotnik.", "Dobry is an adjective."),
   ("Dobra — прикметник.", "„Dobra” — przymiotnik.", "Dobra is an adjective.")],
  ("Well = dobrze.", "Well = dobrze.", "Well = dobrze.")),
]
D[23] = ("Napisz o kimś, kto się zmienił (30+ słów). Jak zachowywał się kiedyś? A jak teraz? Użyj: źle, miło, cicho, grzecznie, dobrze…", 30,
 ("Kiedyś mój brat mówił głośno i grał źle. Teraz mówi cicho i…", "Kiedyś mój brat mówił głośno i grał źle. Teraz mówi cicho i…", "Kiedyś mój brat mówił głośno i grał źle. Teraz mówi cicho i…"))

# ---- Арка 5
T[25] = ("Doświadczenie: już / jeszcze nie / nigdy / kiedyś", "Doświadczenie: już / jeszcze nie / nigdy", "Experience: już / jeszcze nie / nigdy / kiedyś")
G[25] = [
 ("Judy: „____ wszystko zrozumiałam!”", ["Właśnie", "Jeszcze", "Nigdy"], 0,
  [("Так! Just = właśnie.", "Tak! Just = właśnie.", "Yes! Just = właśnie."),
   ("Jeszcze — «ще».", "„Jeszcze” — inny sens.", "Jeszcze means still/yet."),
   ("Nigdy — «ніколи».", "„Nigdy” — inny sens.", "Nigdy means never.")],
  ("У польській Present Perfect = минулий час + właśnie / już / kiedyś / nigdy.", "Present Perfect = przeszły + właśnie / już / kiedyś.", "Polish uses the past tense + właśnie / już / kiedyś / nigdy.")),
 ("Tato, czy ____ jadłeś nocnego wyjca?", ["kiedyś", "wczoraj o piątej", "jutro"], 0,
  [("Так! Ever = kiedyś.", "Tak! Ever = kiedyś.", "Yes! Ever = kiedyś."),
   ("Конкретний час — не досвід.", "Konkretny czas — to nie doświadczenie.", "A specific time isn't experience."),
   ("Jutro — майбутнє.", "„Jutro” — przyszłość.", "Jutro is future.")],
  ("Have you ever…? = Czy kiedyś…?", "Have you ever…? = Czy kiedyś…?", "Have you ever…? = Czy kiedyś…?")),
]
D[25] = ("Napisz o swoich doświadczeniach (30+ słów). Co już robiłeś/robiłaś? Czego nigdy nie robiłeś/robiłaś? Czy kiedyś…?", 30,
 ("Byłam już w… Nigdy nie jadłam… Czy kiedyś…? Właśnie…", "Byłam już w… Nigdy nie jadłam… Czy kiedyś…? Właśnie…", "Byłam już w… Nigdy nie jadłam… Czy kiedyś…? Właśnie…"))

T[26] = ("Przyszłość: pomogę / nie powiem / będzie", "Przyszłość: pomogę / nie powiem", "Future: pomogę / nie powiem / będzie")
G[26] = [
 ("Judy: „Już nigdy tak nie ____. Obiecuję.”", ["powiem", "mówię", "powiedziałam"], 0,
  [("Так! Обіцянка → майбутній: powiem.", "Tak! Obietnica → przyszły: powiem.", "Yes! A promise → future: powiem."),
   ("Mówię — теперішній.", "„Mówię” — teraźniejszy.", "Mówię is present."),
   ("Powiedziałam — минуле.", "„Powiedziałam” — przeszłość.", "Powiedziałam is past.")],
  ("Доконаний вид у теперішній формі = майбутнє: powiem, pomogę, zrobię.", "Dokonany w formie teraźniejszej = przyszłość.", "Perfective in present form = future: powiem, pomogę.")),
 ("Judy: „____ mi, Nick?”", ["Pomożesz", "Pomagasz zawsze", "Pomogłeś"], 0,
  [("Так! Прохання → майбутній: Pomożesz?", "Tak! Prośba → Pomożesz?", "Yes! A request → Pomożesz?"),
   ("Інший зміст.", "Inny sens.", "Different meaning."),
   ("Pomogłeś — минуле.", "„Pomogłeś” — przeszłość.", "Pomogłeś is past.")],
  ("Will you help me? = Pomożesz mi?", "Will you help me? = Pomożesz mi?", "Will you help me? = Pomożesz mi?")),
]
D[26] = ("Napisz obietnicę dla przyjaciela (30+ słów). Co zrobisz? Czego nie zrobisz? Co będzie w przyszłym roku?", 30,
 ("Obiecuję, że… Nie… W przyszłym roku… Myślę, że będzie…", "Obiecuję, że… Nie… W przyszłym roku… Myślę, że będzie…", "Obiecuję, że… Nie… W przyszłym roku… Myślę, że będzie…"))

T[27] = ("Za / zbyt / wystarczająco / dość", "Za / zbyt / wystarczająco", "Too = za / zbyt, enough = wystarczająco")
G[27] = [
 ("Duke jest ____ uparty, żeby mówić.", ["zbyt", "dość mało", "wystarczająco nie"], 0,
  [("Так! Too = zbyt / za.", "Tak! Too = zbyt / za.", "Yes! Too = zbyt / za."),
   ("Неправильно.", "Błąd.", "Wrong."),
   ("Неправильно.", "Błąd.", "Wrong.")],
  ("Za / zbyt + przymiotnik, żeby + bezokolicznik.", "Za / zbyt + przymiotnik, żeby…", "Za / zbyt + adjective, żeby + infinitive.")),
 ("Duke: „Nie jestem ____ odważny, żeby kłamać!”", ["wystarczająco", "zbyt", "bardzo za"], 0,
  [("Так! Enough = wystarczająco / dość.", "Tak! Enough = wystarczająco.", "Yes! Enough = wystarczająco."),
   ("Zbyt — «надто».", "„Zbyt” — za bardzo.", "Zbyt means too."),
   ("Неправильно.", "Błąd.", "Wrong.")],
  ("Brave enough = wystarczająco odważny / dość odważny.", "Brave enough = wystarczająco odważny.", "Brave enough = wystarczająco odważny.")),
]
D[27] = ("Napisz o rzeczach, które są dla ciebie za… albo nie dość… (30+ słów). Np.: Mój pokój jest za mały. Nie jestem wystarczająco wysoki, żeby…", 30,
 ("Moja torba jest za ciężka. Nie jestem wystarczająco… Film był zbyt… Nie jest dość ciepło…", "Moja torba jest za ciężka. Nie jestem wystarczająco… Film był zbyt… Nie jest dość ciepło…", "Moja torba jest za ciężka. Nie jestem wystarczająco… Film był zbyt… Nie jest dość ciepło…"))

T[28] = ("Jeśli + przyszły: Jeśli nas zobaczy, będzie kłopot", "Jeśli + czas przyszły", "If + future: Jeśli nas zobaczy…")
G[28] = [
 ("Nick: „Jeśli Doug nas ____, będziemy mieli kłopoty.”", ["zobaczy", "widzi", "zobaczył"], 0,
  [("Так! У польській після jeśli — майбутній час.", "Tak! Po jeśli — czas przyszły.", "Yes! In Polish, jeśli takes the future."),
   ("Widzi — теперішній.", "„Widzi” — teraźniejszy.", "Widzi is present."),
   ("Zobaczył — минуле.", "„Zobaczył” — przeszłość.", "Zobaczył is past.")],
  ("Англійська: If he sees (теп.). Польська: Jeśli zobaczy (майб.).", "Angielski: If he sees. Polski: Jeśli zobaczy.", "English: If he sees (present). Polish: Jeśli zobaczy (future).")),
 ("Uda się, ____ Doug się obudzi.", ["chyba że", "bo", "i"], 0,
  [("Так! Unless = chyba że.", "Tak! Unless = chyba że.", "Yes! Unless = chyba że."),
   ("Bo — причина.", "„Bo” — przyczyna.", "Bo is a reason."),
   ("I — «і».", "„I” — łączy.", "I means and.")],
  ("Unless = chyba że / jeśli nie.", "Unless = chyba że.", "Unless = chyba że / jeśli nie.")),
]
D[28] = ("Napisz pięć zdań z „jeśli” o swoim tygodniu (30+ słów). Jeśli będzie słońce, pójdę… Jeśli skończę lekcje, …", 30,
 ("Jeśli będzie słońce, pójdę… Jeśli będę mieć czas… Jeśli przyjaciel zadzwoni… Nie…, chyba że…", "Jeśli będzie słońce, pójdę… Jeśli będę mieć czas… Jeśli przyjaciel zadzwoni… Nie…, chyba że…", "Jeśli będzie słońce, pójdę… Jeśli będę mieć czas… Jeśli przyjaciel zadzwoni… Nie…, chyba że…"))

T[29] = ("Bo / więc / ale / i / albo", "Bo / więc / ale / i / albo", "Linking: bo / więc / ale / i / albo")
G[29] = [
 ("Biegną przez muzeum, ____ to najkrótsza droga.", ["bo", "więc", "ale"], 0,
  [("Так! Причина → bo / ponieważ.", "Tak! Przyczyna → bo.", "Yes! A reason → bo."),
   ("Więc — наслідок.", "„Więc” — skutek.", "Więc is a result."),
   ("Ale — протиставлення.", "„Ale” — przeciwieństwo.", "Ale is a contrast.")],
  ("Because = bo / ponieważ · so = więc · but = ale.", "Because = bo · so = więc · but = ale.", "Because = bo · so = więc · but = ale.")),
 ("Judy zraniła nogę, ____ kuleje.", ["więc", "bo", "albo"], 0,
  [("Так! Наслідок → więc.", "Tak! Skutek → więc.", "Yes! A result → więc."),
   ("Bo — причина.", "„Bo” — przyczyna.", "Bo is a reason."),
   ("Albo — вибір.", "„Albo” — wybór.", "Albo is a choice.")],
  ("Więc = тому.", "Więc = so.", "Więc = so.")),
]
D[29] = ("Opisz trudny dzień (30+ słów). Co się stało? Dlaczego? Co zrobiłeś/zrobiłaś? Użyj: i, ale, więc, bo, albo.", 30,
 ("Byłam zmęczona, bo… Było trudno, ale… więc… i potem…", "Byłam zmęczona, bo… Było trudno, ale… więc… i potem…", "Byłam zmęczona, bo… Było trudno, ale… więc… i potem…"))

# ---- Арка 6
T[31] = ("Który / która / które / gdzie", "Który / która / gdzie", "Relative: który / która / które / gdzie")
G[31] = [
 ("Bellwether to owca, ____ wszystko zaplanowała.", ["która", "który", "które"], 0,
  [("Так! Owca — жіночий рід → która.", "Tak! Owca (ż.) → która.", "Yes! Owca is feminine → która."),
   ("Który — чоловічий.", "„Który” — r. męski.", "Który is masculine."),
   ("Które — середній / множина.", "„Które” — r. nijaki / l. mnoga.", "Które is neuter / plural.")],
  ("Który / która / które узгоджуються з іменником (і про людей, і про речі).", "Który / która / które — zgoda z rzeczownikiem.", "Który / która / które agree with the noun (people and things).")),
 ("To sala, ____ wszystko się stało.", ["gdzie", "która", "kiedy"], 0,
  [("Так! Місце → gdzie (або w której).", "Tak! Miejsce → gdzie.", "Yes! A place → gdzie."),
   ("Która — без прийменника тут не підходить.", "„Która” — bez przyimka nie pasuje.", "Która doesn't fit without a preposition."),
   ("Kiedy — час.", "„Kiedy” — czas.", "Kiedy is time.")],
  ("Where = gdzie / w którym.", "Where = gdzie / w którym.", "Where = gdzie / w którym.")),
]
D[31] = ("Opisz trzy osoby, trzy rzeczy i dwa miejsca, które lubisz (30+ słów). Użyj: który, która, które, gdzie.", 30,
 ("Mój przyjaciel to chłopak, który… Moja ulubiona rzecz to rower, który… Park, gdzie…", "Mój przyjaciel to chłopak, który… Moja ulubiona rzecz to rower, który… Park, gdzie…", "Mój przyjaciel to chłopak, który… Moja ulubiona rzecz to rower, który… Park, gdzie…"))

T[32] = ("Mój / twój / jej / nasz / czyj", "Mój / twój / jej / nasz / czyj", "Possessives: mój / twój / jej / nasz / czyj")
G[32] = [
 ("Nick: „Długopis jest ____, Carrots.”", ["twój", "twoja", "twoje"], 0,
  [("Так! Długopis (чол. рід) → twój.", "Tak! Długopis (m.) → twój.", "Yes! Długopis is masculine → twój."),
   ("Twoja — жіночий.", "„Twoja” — r. żeński.", "Twoja is feminine."),
   ("Twoje — середній.", "„Twoje” — r. nijaki.", "Twoje is neuter.")],
  ("Польська: та сама форма з іменником і без: twój długopis / jest twój.", "Ta sama forma: twój długopis / jest twój.", "Polish uses the same form with or without a noun.")),
 ("Judy: „To nagranie jest teraz ____!”", ["nasze", "nasz", "nasza"], 0,
  [("Так! Nagranie (середній) → nasze.", "Tak! Nagranie (n.) → nasze.", "Yes! Nagranie is neuter → nasze."),
   ("Nasz — чоловічий.", "„Nasz” — r. męski.", "Nasz is masculine."),
   ("Nasza — жіночий.", "„Nasza” — r. żeński.", "Nasza is feminine.")],
  ("Mój/moja/moje, twój/twoja/twoje, nasz/nasza/nasze; jej, jego, ich — не змінюються.", "Jej, jego, ich — nieodmienne.", "Jej, jego, ich never change.")),
]
D[32] = ("Napisz o rzeczach w pokoju i rzeczach rodziny (30+ słów). Czyje są? Użyj: mój, twój, jego, jej, nasz, ich, czyj.", 30,
 ("Niebieska torba jest moja. Duży fotel jest taty — jest jego. Ogród jest nasz. Czyj jest…?", "Niebieska torba jest moja. Duży fotel jest taty — jest jego. Ogród jest nasz. Czyj jest…?", "Niebieska torba jest moja. Duży fotel jest taty — jest jego. Ogród jest nasz. Czyj jest…?"))

T[33] = ("Kiedyś (dawniej) + czas przeszły niedokonany", "Kiedyś + przeszły niedokonany", "Used to = kiedyś + imperfective past")
G[33] = [
 ("Miasto ____ się bało, ale teraz jest spokojne.", ["kiedyś", "jutro", "zaraz"], 0,
  [("Так! Used to = kiedyś.", "Tak! Used to = kiedyś.", "Yes! Used to = kiedyś."),
   ("Jutro — майбутнє.", "„Jutro” — przyszłość.", "Jutro is future."),
   ("Zaraz — «зараз же».", "„Zaraz” — za chwilę.", "Zaraz means soon.")],
  ("Used to = kiedyś + niedokonany: kiedyś mieszkałam, kiedyś grałam.", "Kiedyś + niedokonany.", "Kiedyś + imperfective past.")),
 ("Kiedyś Clawhauser ____ w archiwum.", ["pracował", "popracował", "pracuje"], 0,
  [("Так! Тривале в минулому → недоконаний.", "Tak! Niedokonany → pracował.", "Yes! Imperfective → pracował."),
   ("Popracował — коротко, разово.", "„Popracował” — krótko.", "Popracował means for a short while."),
   ("Pracuje — теперішній.", "„Pracuje” — teraźniejszy.", "Pracuje is present.")],
  ("Used to → недоконаний вид.", "Used to → niedokonany.", "Used to → imperfective.")),
]
D[33] = ("Napisz, jaki/jaka byłeś/byłaś, kiedy byłeś/byłaś mały/mała (30+ słów). Co kiedyś robiłeś/robiłaś? Czego kiedyś nie lubiłeś/lubiłaś? Co robisz teraz?", 30,
 ("Kiedy byłam mała, kiedyś… Kiedyś nie lubiłam… Teraz…", "Kiedy byłam mała, kiedyś… Kiedyś nie lubiłam… Teraz…", "Kiedy byłam mała, kiedyś… Kiedyś nie lubiłam… Teraz…"))

T[34] = ("Przyszłość: będę / zamierzam / spotykam się jutro", "Przyszłość: będę / zamierzam", "Future: będę / zamierzam / spotykam się jutro")
G[34] = [
 ("Judy: „____ najlepszymi partnerami!”", ["Będziemy", "Byliśmy", "Jesteśmy wczoraj"], 0,
  [("Так! Майбутнє → będziemy.", "Tak! Przyszłość → będziemy.", "Yes! Future → będziemy."),
   ("Byliśmy — минуле.", "„Byliśmy” — przeszłość.", "Byliśmy is past."),
   ("Неправильно.", "Błąd.", "Wrong.")],
  ("Будемо = будемо: będę, będziesz, będzie, będziemy…", "Być: będę, będziesz, będzie, będziemy…", "Future of być: będę, będziesz, będzie, będziemy…")),
 ("Nick: „Spokojnie, Carrots. ____ go!”", ["Zatrzymam", "Zatrzymuję wczoraj", "Zatrzymałem"], 0,
  [("Так! Рішення → доконаний майбутній.", "Tak! Decyzja → dokonany przyszły.", "Yes! A decision → perfective future."),
   ("Неправильно.", "Błąd.", "Wrong."),
   ("Zatrzymałem — минуле.", "„Zatrzymałem” — przeszłość.", "Zatrzymałem is past.")],
  ("I'll stop it = Zatrzymam go.", "I'll stop it = Zatrzymam go.", "I'll stop it = Zatrzymam go.")),
]
D[34] = ("Napisz o swojej przyszłości (30+ słów). Co zamierzasz robić w przyszłym roku? Co robisz w ten weekend? Co będzie za 10 lat?", 30,
 ("W przyszłym roku zamierzam… W weekend spotykam się z… Za dziesięć lat będę…", "W przyszłym roku zamierzam… W weekend spotykam się z… Za dziesięć lat będę…", "W przyszłym roku zamierzam… W weekend spotykam się z… Za dziesięć lat będę…"))
