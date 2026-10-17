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
