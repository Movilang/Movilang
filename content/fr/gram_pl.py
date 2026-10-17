# Wersja kursu „Przyjaciele” dla uczących się POLSKIEGO (A2–B1). Gramatyka + wiadomość.
# Zadanie: (pytanie, [opcje], poprawna, [(uk, pl, en) dla każdej opcji], (tip uk, pl, en))
G = {}
D = {}
T = {}

# ---- Арка 1
T[1] = ("Теперішній час: mieszkam, piję, pracuję", "Czas teraźniejszy: mieszkam, piję, pracuję", "Present tense: mieszkam, piję, pracuję")
G[1] = [
 ("Codziennie rano przyjaciele ____ kawę w Central Perk.", ["piją", "pije", "pijemy"], 0,
  [("Так! Вони (oni) → piją.", "Tak! Oni → piją.", "Yes! Oni (they) → piją."),
   ("Pije — він/вона.", "„Pije” — on/ona.", "Pije is he/she."),
   ("Pijemy — ми.", "„Pijemy” — my.", "Pijemy is we.")],
  ("Pić: piję, pijesz, pije, pijemy, pijecie, piją.", "Pić: piję, pijesz, pije, pijemy, pijecie, piją.", "Pić: piję, pijesz, pije, pijemy, pijecie, piją.")),
 ("Rachel: — Teraz ____ u Moniki.", ["mieszkam", "mieszka", "mieszkasz"], 0,
  [("Так! Я (ja) → mieszkam.", "Tak! Ja → mieszkam.", "Yes! Ja (I) → mieszkam."),
   ("Mieszka — вона.", "„Mieszka” — ona.", "Mieszka is she."),
   ("Mieszkasz — ти.", "„Mieszkasz” — ty.", "Mieszkasz is you.")],
  ("Польська не має окремої форми «зараз»: teraz mieszkam = I'm living now.", "Polski nie ma osobnej formy „teraz”: teraz mieszkam.", "Polish has one present tense: teraz mieszkam = I'm living now.")),
]
D[1] = ("Jesteś Rachel. Napisz wiadomość do starych przyjaciół (35+ słów): co robisz codziennie i co robisz teraz w Nowym Jorku.", 35,
 ("Codziennie… Teraz mieszkam… Pracuję…", "Codziennie… Teraz mieszkam… Pracuję…", "Codziennie… Teraz mieszkam… Pracuję…"))

T[2] = ("lubić / uwielbiać / nienawidzić + інфінітив", "lubić / uwielbiać / nienawidzić + bezokolicznik", "lubić / uwielbiać / nienawidzić + infinitive")
G[2] = [
 ("Rachel bardzo lubi ____ na zakupy.", ["chodzić", "chodzi", "chodzenie"], 0,
  [("Так! Lubić + інфінітив: lubi chodzić.", "Tak! Lubić + bezokolicznik.", "Yes! Lubić + infinitive."),
   ("Chodzi — особова форма, а потрібен інфінітив.", "„Chodzi” — forma osobowa, potrzebny bezokolicznik.", "Chodzi is a personal form; you need the infinitive."),
   ("Chodzenie — іменник; так буває, але тут природніше інфінітив.", "„Chodzenie” to rzeczownik; tu naturalniej bezokolicznik.", "Chodzenie is a noun; the infinitive sounds more natural.")],
  ("Lubię gotować, uwielbiam tańczyć, nienawidzę sprzątać.", "Lubię gotować, uwielbiam tańczyć, nienawidzę sprzątać.", "Lubię gotować, uwielbiam tańczyć, nienawidzę sprzątać.")),
 ("Rachel nie ma pieniędzy. Musi ____ pracę.", ["znaleźć", "znajduje", "znalazła"], 0,
  [("Так! Musieć + інфінітив.", "Tak! Musieć + bezokolicznik.", "Yes! Musieć + infinitive."),
   ("Znajduje — особова форма.", "„Znajduje” — forma osobowa.", "Znajduje is a personal form."),
   ("Znalazła — минулий час.", "„Znalazła” — czas przeszły.", "Znalazła is past tense.")],
  ("Muszę, chcę, potrzebuję + bezokolicznik.", "Muszę, chcę, potrzebuję + bezokolicznik.", "Muszę, chcę, potrzebuję + infinitive.")),
]
D[2] = ("Jesteś Rachel. Napisz wiadomość do taty (35+ słów): co lubisz robić, czego nienawidzisz w pracy i czego musisz się nauczyć.", 35,
 ("Lubię… Nienawidzę… Muszę… Chcę…", "Lubię… Nienawidzę… Muszę… Chcę…", "Lubię… Nienawidzę… Muszę… Chcę…"))

T[3] = ("Плани: Jutro idę do lekarza", "Plany: Jutro idę do lekarza", "Plans: Jutro idę do lekarza")
G[3] = [
 ("W czwartek Ross ____ z Carol do lekarza.", ["idzie", "szedł", "chodzi"], 0,
  [("Так! Теперішній час + час у майбутньому = план.", "Tak! Czas teraźniejszy + określenie przyszłości = plan.", "Yes! Present tense + a future time = a plan."),
   ("Szedł — минуле.", "„Szedł” — przeszłość.", "Szedł is past."),
   ("Chodzi — регулярно, звичка.", "„Chodzi” — regularnie, nawyk.", "Chodzi means regularly, a habit.")],
  ("Iść (один раз, у напрямку) vs chodzić (регулярно).", "Iść (raz, w jedną stronę) vs chodzić (regularnie).", "Iść (once, in one direction) vs chodzić (regularly).")),
 ("Co ____ dziś wieczorem?", ["robisz", "zrobiłeś", "robiłeś"], 0,
  [("Так! Co robisz dziś wieczorem? — питання про плани.", "Tak! Pytanie o plany.", "Yes! A question about plans."),
   ("Zrobiłeś — минуле.", "„Zrobiłeś” — przeszłość.", "Zrobiłeś is past."),
   ("Robiłeś — минуле.", "„Robiłeś” — przeszłość.", "Robiłeś is past.")],
  ("Co robisz jutro / w piątek / dziś wieczorem?", "Co robisz jutro / w piątek / dziś wieczorem?", "Co robisz jutro / w piątek / dziś wieczorem?")),
]
D[3] = ("Jesteś Rossem. Napisz plan na przyszły tydzień (35+ słów): co robisz w poniedziałek, w czwartek i w weekend, z kim się spotykasz.", 35,
 ("W poniedziałek idę… W czwartek spotykam się… W weekend…", "W poniedziałek idę… W czwartek spotykam się… W weekend…", "W poniedziałek idę… W czwartek spotykam się… W weekend…"))

T[4] = ("Dużo / wiele / kilka / trochę + родовий відмінок", "Dużo / wiele / kilka / trochę + dopełniacz", "Dużo / wiele / kilka / trochę + genitive")
G[4] = [
 ("Phoebe ma teraz dużo ____.", ["pieniędzy", "pieniądze", "pieniądzach"], 0,
  [("Так! Dużo + родовий: pieniędzy.", "Tak! Dużo + dopełniacz: pieniędzy.", "Yes! Dużo + genitive: pieniędzy."),
   ("Pieniądze — називний відмінок.", "„Pieniądze” — mianownik.", "Pieniądze is nominative."),
   ("Pieniądzach — місцевий.", "„Pieniądzach” — miejscownik.", "Pieniądzach is locative.")],
  ("Dużo / mało / trochę / ile + dopełniacz.", "Dużo / mało / trochę / ile + dopełniacz.", "Dużo / mało / trochę / ile + genitive.")),
 ("Chandler wypalił ____ papierosów.", ["kilka", "trochę", "mało czasu"], 0,
  [("Так! Kilka + злічуване: kilka papierosów.", "Tak! Kilka + policzalne.", "Yes! Kilka + countable."),
   ("Trochę — з незлічуваними: trochę mleka.", "„Trochę” — z niepoliczalnymi.", "Trochę goes with uncountables."),
   ("Mało czasu — про час, інший зміст.", "„Mało czasu” — o czasie.", "Mało czasu is about time.")],
  ("Kilka papierosów, trochę cukru, wiele osób.", "Kilka papierosów, trochę cukru, wiele osób.", "Kilka papierosów, trochę cukru, wiele osób.")),
]
D[4] = ("Jesteś Phoebe. Napisz list do firmy produkującej napoje (35+ słów): co znalazłaś, ile pieniędzy dostałaś i co chcesz z nimi zrobić. Użyj: dużo, kilka, trochę, ile.", 35,
 ("Dostałam dużo pieniędzy… Potrzebuję tylko trochę…", "Dostałam dużo pieniędzy… Potrzebuję tylko trochę…", "Dostałam dużo pieniędzy… Potrzebuję tylko trochę…"))

T[5] = ("Вид дієслова: oglądał (тривало) / trafił (одна подія)", "Aspekt: oglądał (trwało) / trafił (jedno zdarzenie)", "Aspect: oglądał (ongoing) / trafił (one event)")
G[5] = [
 ("Ross ____ mecz, kiedy krążek trafił go w twarz.", ["oglądał", "obejrzał", "ogląda"], 0,
  [("Так! Недоконаний вид = дія тривала (фон).", "Tak! Aspekt niedokonany = czynność trwała (tło).", "Yes! Imperfective = the action was ongoing (background)."),
   ("Obejrzał — уже закінчив, тоді шайба не перервала б.", "„Obejrzał” — skończył oglądać.", "Obejrzał means he finished watching."),
   ("Ogląda — теперішній час.", "„Ogląda” — czas teraźniejszy.", "Ogląda is present.")],
  ("Oglądał (фон) + trafił (подія) — як Past Continuous + Past Simple.", "Oglądał (tło) + trafił (wydarzenie).", "Oglądał (background) + trafił (event) — like Past Continuous + Past Simple.")),
 ("Dziewczyny jadły pizzę, kiedy ktoś ____ do drzwi.", ["zadzwonił", "dzwonił", "dzwoni"], 0,
  [("Так! Одна коротка подія → доконаний вид.", "Tak! Jedno krótkie zdarzenie → aspekt dokonany.", "Yes! One short event → perfective."),
   ("Dzwonił — тривало або багато разів.", "„Dzwonił” — długo albo wiele razy.", "Dzwonił means for a long time or many times."),
   ("Dzwoni — теперішній.", "„Dzwoni” — teraźniejszy.", "Dzwoni is present.")],
  ("Dzwonić (недоконаний) → zadzwonić (доконаний).", "Dzwonić → zadzwonić.", "Dzwonić (imperfective) → zadzwonić (perfective).")),
]
D[5] = ("Opowiedz o tamtym wieczorze (35+ słów): co robili chłopaki, kiedy krążek trafił Rossa? Co robiły dziewczyny, kiedy przyszła pizza?", 35,
 ("Chłopaki oglądali…, kiedy… Dziewczyny…, kiedy…", "Chłopaki oglądali…, kiedy… Dziewczyny…, kiedy…", "Chłopaki oglądali…, kiedy… Dziewczyny…, kiedy…"))

# ---- Арка 2
T[7] = ("Як часто? zawsze, zwykle, czasami, nigdy (nie)", "Jak często? zawsze, zwykle, czasami, nigdy (nie)", "How often? zawsze, zwykle, czasami, nigdy (nie)")
G[7] = [
 ("Rachel ____ nie robiła prania sama.", ["nigdy", "zawsze", "często"], 0,
  [("Так! Nigdy + nie — у польській подвійне заперечення.", "Tak! Nigdy + nie — podwójne przeczenie.", "Yes! Nigdy + nie — Polish uses a double negative."),
   ("Zawsze nie — так не кажуть.", "„Zawsze nie” — tak się nie mówi.", "We don't say zawsze nie."),
   ("Często nie — можливо, але сенс інший.", "„Często nie” — możliwe, ale inny sens.", "Często nie is possible, but means something else.")],
  ("Nigdy nie, nikt nie, nic nie — заперечення подвійне.", "Nigdy nie, nikt nie, nic nie.", "Nigdy nie, nikt nie, nic nie — double negatives.")),
 ("Ross ____ oddziela białe rzeczy od kolorowych.", ["zawsze", "nigdy", "wcale"], 0,
  [("Так! Росс завжди розділяє речі.", "Tak! Ross zawsze to robi.", "Yes! Ross always does it."),
   ("Nigdy — тоді потрібне nie.", "„Nigdy” wymagałoby nie.", "Nigdy would need nie."),
   ("Wcale — тільки з запереченням.", "„Wcale” — tylko z przeczeniem.", "Wcale only works with a negative.")],
  ("Прислівник частоти зазвичай перед дієсловом.", "Przysłówek częstotliwości zwykle stoi przed czasownikiem.", "The frequency adverb usually goes before the verb.")),
]
D[7] = ("Jesteś Rachel. Opisz swój nowy rytm dnia (35+ słów): co robisz zawsze, zwykle, czasami, rzadko i czego nigdy nie robisz.", 35,
 ("Zawsze… Zwykle… Czasami… Nigdy nie…", "Zawsze… Zwykle… Czasami… Nigdy nie…", "Zawsze… Zwykle… Czasami… Nigdy nie…"))

T[8] = ("Досвід: Byłeś kiedyś…? Nigdy nie grałem…", "Doświadczenie: Byłeś kiedyś…? Nigdy nie grałem…", "Experience: Byłeś kiedyś…? Nigdy nie grałem…")
G[8] = [
 ("Joey, ____ kiedyś na prawdziwym planie filmowym?", ["byłeś", "jesteś", "będziesz"], 0,
  [("Так! Досвід — минулий час + kiedyś.", "Tak! Doświadczenie — czas przeszły + kiedyś.", "Yes! Experience — past tense + kiedyś."),
   ("Jesteś — зараз.", "„Jesteś” — teraz.", "Jesteś is now."),
   ("Będziesz — майбутнє.", "„Będziesz” — przyszłość.", "Będziesz is future.")],
  ("Польська не має Present Perfect: Byłeś kiedyś…? = Have you ever been…?", "Polski nie ma Present Perfect: Byłeś kiedyś…?", "Polish has no Present Perfect: Byłeś kiedyś…? = Have you ever been…?")),
 ("Wczoraj Joey ____ swoją pierwszą scenę.", ["zagrał", "grał kiedyś", "zagra"], 0,
  [("Так! Одна завершена дія вчора → доконаний вид.", "Tak! Jedna zakończona czynność → aspekt dokonany.", "Yes! One finished action yesterday → perfective."),
   ("Kiedyś не поєднується з wczoraj.", "„Kiedyś” nie pasuje do wczoraj.", "Kiedyś doesn't go with wczoraj."),
   ("Zagra — майбутнє.", "„Zagra” — przyszłość.", "Zagra is future.")],
  ("Wczoraj / w zeszłym tygodniu + dokonany: zagrał, zrobił.", "Wczoraj + dokonany.", "Wczoraj + perfective: zagrał, zrobił.")),
]
D[8] = ("Jesteś Joeyem. Napisz krótki profil dla agentki (35+ słów): co już robiłeś w życiu, czego nigdy nie robiłeś i co zrobiłeś w zeszłym tygodniu.", 35,
 ("Grałem w… Nigdy nie… W zeszłym tygodniu zagrałem…", "Grałem w… Nigdy nie… W zeszłym tygodniu zagrałem…", "Grałem w… Nigdy nie… W zeszłym tygodniu zagrałem…"))

T[9] = ("Майбутнє: zamierzam powiedzieć (план) / zaraz przyniosę (рішення)", "Przyszłość: zamierzam powiedzieć / zaraz przyniosę", "Future: zamierzam powiedzieć (plan) / zaraz przyniosę (decision)")
G[9] = [
 ("Ross postanowił: dziś wieczorem ____ powiedzieć Rachel o uczuciach.", ["zamierza", "przyniesie", "powiedział"], 0,
  [("Так! Zamierzać + інфінітив = план.", "Tak! Zamierzać + bezokolicznik = plan.", "Yes! Zamierzać + infinitive = a plan."),
   ("Przyniesie — інше дієслово.", "„Przyniesie” — inny czasownik.", "Przyniesie is a different verb."),
   ("Powiedział — минуле.", "„Powiedział” — przeszłość.", "Powiedział is past.")],
  ("Zamierzam / mam zamiar + bezokolicznik = be going to.", "Zamierzam / mam zamiar + bezokolicznik.", "Zamierzam / mam zamiar + infinitive = be going to.")),
 ("Zgasło światło! Monica: — Spokojnie, zaraz ____ świece.", ["przyniosę", "przynoszę codziennie", "przyniosłam"], 0,
  [("Так! Доконаний вид у теперішній формі = майбутня дія.", "Tak! Aspekt dokonany w formie teraźniejszej = przyszłość.", "Yes! A perfective verb in present form = future."),
   ("Codziennie — звичка.", "„Codziennie” — nawyk.", "Codziennie is a habit."),
   ("Przyniosłam — минуле.", "„Przyniosłam” — przeszłość.", "Przyniosłam is past.")],
  ("Przyniosę, zrobię, zadzwonię = I'll bring / do / call.", "Przyniosę, zrobię, zadzwonię.", "Przyniosę, zrobię, zadzwonię = I'll bring / do / call.")),
]
D[9] = ("Jesteś Rossem. Napisz w pamiętniku po awarii prądu (35+ słów): co zamierzałeś zrobić, co zamierzasz zrobić następnym razem i co sobie obiecujesz.", 35,
 ("Zamierzałem… Następnym razem zamierzam… Obiecuję, że…", "Zamierzałem… Następnym razem zamierzam… Obiecuję, że…", "Zamierzałem… Następnym razem zamierzam… Obiecuję, że…"))

T[10] = ("Kiedyś + минулий недоконаний: babcia kiedyś mieszkała", "Kiedyś + przeszły niedokonany: babcia kiedyś mieszkała", "Kiedyś + past imperfective: babcia kiedyś mieszkała")
G[10] = [
 ("Babcia kiedyś ____ w tym mieszkaniu.", ["mieszkała", "zamieszkała", "mieszka"], 0,
  [("Так! Тривалий стан у минулому → недоконаний вид.", "Tak! Trwały stan w przeszłości → niedokonany.", "Yes! A long-lasting past state → imperfective."),
   ("Zamieszkała — момент переїзду.", "„Zamieszkała” — moment przeprowadzki.", "Zamieszkała is the moment of moving in."),
   ("Mieszka — теперішній.", "„Mieszka” — teraźniejszy.", "Mieszka is present.")],
  ("Kiedyś + niedokonany ≈ used to.", "Kiedyś + niedokonany ≈ used to.", "Kiedyś + imperfective ≈ used to.")),
 ("Jako dziecko Monica co niedzielę ____ babcię.", ["odwiedzała", "odwiedziła", "odwiedzi"], 0,
  [("Так! Повторювана дія в минулому → недоконаний.", "Tak! Powtarzana czynność → niedokonany.", "Yes! A repeated past action → imperfective."),
   ("Odwiedziła — один раз.", "„Odwiedziła” — raz.", "Odwiedziła is once."),
   ("Odwiedzi — майбутнє.", "„Odwiedzi” — przyszłość.", "Odwiedzi is future.")],
  ("Co niedzielę / zawsze + niedokonany.", "Co niedzielę + niedokonany.", "Co niedzielę + imperfective.")),
]
D[10] = ("Napisz o starszej osobie z twojej rodziny (35+ słów): co kiedyś robiła, co robiliście razem, czego nie lubiła.", 35,
 ("Babcia kiedyś… Razem często… Nie lubiła…", "Babcia kiedyś… Razem często… Nie lubiła…", "Babcia kiedyś… Razem często… Nie lubiła…"))

T[11] = ("Поради: powinieneś / powinnaś + інфінітив", "Rady: powinieneś / powinnaś + bezokolicznik", "Advice: powinieneś / powinnaś + infinitive")
G[11] = [
 ("Rachel spóźniła się na samolot. Monica: — ____ zostać z nami!", ["Powinnaś", "Powinieneś", "Powinna"], 0,
  [("Так! До жінки (ty) → powinnaś.", "Tak! Do kobiety (ty) → powinnaś.", "Yes! To a woman (you) → powinnaś."),
   ("Powinieneś — до чоловіка.", "„Powinieneś” — do mężczyzny.", "Powinieneś is for a man."),
   ("Powinna — про неї (вона).", "„Powinna” — o niej (ona).", "Powinna is she, not you.")],
  ("Powinienem/powinnam, powinieneś/powinnaś, powinien/powinna.", "Powinienem/powinnam, powinieneś/powinnaś, powinien/powinna.", "Powinienem/powinnam, powinieneś/powinnaś, powinien/powinna.")),
 ("Joey ____ jeździć metrem w tym tygodniu.", ["nie powinien", "powinien", "nie powinna"], 0,
  [("Так! Він → nie powinien.", "Tak! On → nie powinien.", "Yes! He → nie powinien."),
   ("Powinien — тоді всі витріщатимуться ще більше.", "„Powinien” — wtedy wszyscy będą się gapić.", "Powinien — then everyone will stare more."),
   ("Nie powinna — жіночий рід.", "„Nie powinna” — rodzaj żeński.", "Nie powinna is feminine.")],
  ("Nie powinieneś + bezokolicznik = shouldn't.", "Nie powinieneś + bezokolicznik.", "Nie powinieneś + infinitive = shouldn't.")),
]
D[11] = ("Napisz rady dla jednego z przyjaciół (35+ słów): dla Joeya z plakatem, dla Rachel, która spóźniła się na samolot, albo dla Moniki ze spalonym indykiem. Użyj: powinieneś / powinnaś, nie powinieneś.", 35,
 ("Powinieneś… Nie powinnaś… W przyszłym roku powinnaś…", "Powinieneś… Nie powinnaś… W przyszłym roku powinnaś…", "Powinieneś… Nie powinnaś… W przyszłym roku powinnaś…"))
