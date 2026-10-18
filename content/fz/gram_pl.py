# Міні-курс «Крижане серце».
G = {}
D = {}
T = {}
T[1] = ("Jestem / mam", "Jestem / mam", "Być i mieć: jestem / mam")
G[1] = [
 ("Elsa ____ starszą siostrą.", ["jest", "są", "jestem"], 0,
  [("Так! Вона → jest.", "Tak! Ona → jest.", "Yes! She → jest."),
   ("Są — вони.", "„Są” — oni.", "Są is they."),
   ("Jestem — я.", "„Jestem” — ja.", "Jestem is I.")],
  ("Ja jestem, ona jest, one są.", "Ja jestem, ona jest, one są.", "Ja jestem, ona jest, one są.")),
 ("Elsa ____ magię w rękach.", ["ma", "mam", "mają"], 0,
  [("Так! Вона → ma.", "Tak! Ona → ma.", "Yes! She → ma."),
   ("Mam — я.", "„Mam” — ja.", "Mam is I."),
   ("Mają — вони.", "„Mają” — oni.", "Mają is they.")],
  ("Mieć: mam, masz, ma, mamy, macie, mają.", "Mieć: mam, masz, ma…", "Mieć: mam, masz, ma, mamy, macie, mają.")),
]
D[1] = ("Napisz o swojej rodzinie (30+ słów). Kto w niej jest? Ile mają lat? Co mają?", 30,
 ("Mam… Moja siostra jest… Ona ma… Jesteśmy…", "Mam… Moja siostra jest… Ona ma… Jesteśmy…", "Mam… Moja siostra jest… Ona ma… Jesteśmy…"))
T[2] = ("Teraz: co się dzieje?", "Teraz: co się dzieje?", "Right now: co się dzieje?")
G[2] = [
 ("Patrz! Brama się ____!", ["otwiera", "otwierała", "otworzy"], 0,
  [("Так! Зараз → теперішній.", "Tak! Teraz → teraźniejszy.", "Yes! Now → present."),
   ("Минуле.", "Przeszłość.", "Past."),
   ("Майбутнє.", "Przyszłość.", "Future.")],
  ("Польська: один теперішній час для «зараз».", "Jeden czas teraźniejszy.", "Polish: one present tense for “now”.")),
 ("Hans i ja ____!", ["tańczymy", "tańczą", "tańczę"], 0,
  [("Так! Ми → tańczymy.", "Tak! My → tańczymy.", "Yes! We → tańczymy."),
   ("Tańczą — вони.", "„Tańczą” — oni.", "Tańczą is they."),
   ("Tańczę — я.", "„Tańczę” — ja.", "Tańczę is I.")],
  ("Tańczyć: tańczę, tańczysz, tańczy, tańczymy…", "Tańczyć: tańczę, tańczymy…", "Tańczyć: tańczę, tańczysz, tańczy, tańczymy…")),
]
D[2] = ("Wyobraź sobie wielkie przyjęcie. Napisz, co się teraz dzieje (30+ słów). Kto tańczy? Kto śpiewa? Co robisz?", 30,
 ("Stoję… Moi przyjaciele tańczą… Gra muzyka… Mama…", "Stoję… Moi przyjaciele tańczą… Gra muzyka… Mama…", "Stoję… Moi przyjaciele tańczą… Gra muzyka… Mama…"))
T[3] = ("Umie / może / nie może", "Umie / może / nie może", "Can = umie / może")
G[3] = [
 ("Elsa ____ robić lód.", ["umie", "umiem", "umieją"], 0,
  [("Так! Вона → umie.", "Tak! Ona → umie.", "Yes! She → umie."),
   ("Umiem — я.", "„Umiem” — ja.", "Umiem is I."),
   ("Umieją — вони.", "„Umieją” — oni.", "Umieją is they.")],
  ("Umieć + bezokolicznik.", "Umieć + bezokolicznik.", "Umieć + infinitive.")),
 ("Elsa: „Nie ____ tego zatrzymać!”", ["mogę", "może", "możesz"], 0,
  [("Так! Я → mogę.", "Tak! Ja → mogę.", "Yes! I → mogę."),
   ("Może — вона.", "„Może” — ona.", "Może is she."),
   ("Możesz — ти.", "„Możesz” — ty.", "Możesz is you.")],
  ("Can't = nie mogę / nie umiem.", "Can't = nie mogę.", "Can't = nie mogę / nie umiem.")),
]
D[3] = ("Wyobraź sobie, że masz magiczną moc (30+ słów). Co umiesz? Czego nie umiesz?", 30,
 ("Umiem… Mogę też… Ale nie umiem… Nie mogę…", "Umiem… Mogę też… Ale nie umiem… Nie mogę…", "Umiem… Mogę też… Ale nie umiem… Nie mogę…"))
T[4] = ("Lubię / kocham / nie znoszę + bezokolicznik", "Lubię + bezokolicznik", "Like = lubię + infinitive")
G[4] = [
 ("Olaf uwielbia ciepłe ____.", ["przytulasy", "przytulasów", "przytulasami"], 0,
  [("Так! Uwielbiać + знахідний.", "Tak! Uwielbiać + biernik.", "Yes! Uwielbiać + accusative."),
   ("Родовий — ні.", "Dopełniacz — nie.", "Not genitive."),
   ("Орудний — ні.", "Narzędnik — nie.", "Not instrumental.")],
  ("Lubię / kocham + biernik; nie lubię + dopełniacz.", "Lubię + biernik; nie lubię + dopełniacz.", "Lubię + accusative; nie lubię + genitive.")),
 ("Kristoff: „Nie znoszę ____.”", ["czekać", "czekam", "czekanie się"], 0,
  [("Так! Nie znoszę + інфінітив.", "Tak! Nie znoszę + bezokolicznik.", "Yes! Nie znoszę + infinitive."),
   ("Czekam — «я чекаю».", "„Czekam” — ja czekam.", "Czekam means I wait."),
   ("Неправильно.", "Błąd.", "Wrong.")],
  ("Like + -ing = lubię + bezokolicznik.", "Like + -ing = lubię + bezokolicznik.", "Like + -ing = lubię + infinitive.")),
]
D[4] = ("Napisz, co lubisz, kochasz i czego nie znosisz (30+ słów). Opisz też ulubione miejsce: co tam jest?", 30,
 ("Uwielbiam pływać. Lubię czytać. Nie znoszę… W moim ulubionym miejscu jest… są…", "Uwielbiam pływać. Lubię czytać. Nie znoszę… W moim ulubionym miejscu jest… są…", "Uwielbiam pływać. Lubię czytać. Nie znoszę… W moim ulubionym miejscu jest… są…"))
T[5] = ("Czas przeszły: poszła, znalazła, uratowała", "Czas przeszły", "Past: poszła, znalazła, uratowała")
G[5] = [
 ("Anna ____ do pałacu i znalazła siostrę.", ["poszła", "poszedł", "pójdzie"], 0,
  [("Так! Анна (жін.) → poszła.", "Tak! Anna (ż.) → poszła.", "Yes! Anna (f.) → poszła."),
   ("Poszedł — чоловічий.", "„Poszedł” — r. męski.", "Poszedł is masculine."),
   ("Майбутнє.", "Przyszłość.", "Future.")],
  ("Минуле: -ł (він), -ła (вона), -li (вони).", "Przeszły: -ł, -ła, -li.", "Past: -ł (he), -ła (she), -li (they).")),
 ("Hans nie ____ Anny.", ["kochał", "kochała", "kocha"], 0,
  [("Так! Ганс (чол.) → kochał.", "Tak! Hans (m.) → kochał.", "Yes! Hans (m.) → kochał."),
   ("Kochała — жіночий.", "„Kochała” — r. żeński.", "Kochała is feminine."),
   ("Kocha — теперішній.", "„Kocha” — teraźniejszy.", "Kocha is present.")],
  ("Didn't = nie + минулий час.", "Didn't = nie + przeszły.", "Didn't = nie + past.")),
]
D[5] = ("Napisz krótką bajkę o dwóch przyjaciołach (30+ słów). Co się stało? Dokąd poszli? Co znaleźli? Jak się skończyło?", 30,
 ("Dawno temu były dwie przyjaciółki. Pewnego dnia poszły… Znalazły… Na końcu…", "Dawno temu były dwie przyjaciółki. Pewnego dnia poszły… Znalazły… Na końcu…", "Dawno temu były dwie przyjaciółki. Pewnego dnia poszły… Znalazły… Na końcu…"))
