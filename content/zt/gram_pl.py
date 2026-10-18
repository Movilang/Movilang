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
