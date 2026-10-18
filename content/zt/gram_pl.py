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
