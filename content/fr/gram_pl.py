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

# ---- Арка 3
T[13] = ("Обов'язок: muszę / nie muszę / nie wolno", "Obowiązek: muszę / nie muszę / nie wolno", "Obligation: muszę / nie muszę / nie wolno")
G[13] = [
 ("Ross ____ karmić Marcela trzy razy dziennie.", ["musi", "muszę", "musimy"], 0,
  [("Так! Він → musi.", "Tak! On → musi.", "Yes! He → musi."),
   ("Muszę — я.", "„Muszę” — ja.", "Muszę is I."),
   ("Musimy — ми.", "„Musimy” — my.", "Musimy is we.")],
  ("Muszę, musisz, musi, musimy, musicie, muszą.", "Muszę, musisz, musi, musimy, musicie, muszą.", "Muszę, musisz, musi, musimy, musicie, muszą.")),
 ("Marcela ____ wyprowadzać na spacer — to nie pies.", ["nie trzeba", "nie wolno", "trzeba"], 0,
  [("Так! Nie trzeba = не обов'язково.", "Tak! Nie trzeba = don't have to.", "Yes! Nie trzeba = don't have to."),
   ("Nie wolno — заборона, інший зміст.", "„Nie wolno” — zakaz, inny sens.", "Nie wolno is a ban — different meaning."),
   ("Trzeba — обов'язково, протилежне.", "„Trzeba” — odwrotnie.", "Trzeba means you have to — the opposite.")],
  ("Nie musisz / nie trzeba ≠ nie wolno.", "Nie musisz / nie trzeba ≠ nie wolno.", "Nie musisz / nie trzeba (not necessary) ≠ nie wolno (not allowed).")),
]
D[13] = ("Jesteś Rossem. Napisz zasady dla opiekunki Marcela (35+ słów): co musi robić, czego nie musi robić i czego nie wolno jej robić.", 35,
 ("Musisz… Nie musisz… Nie wolno…", "Musisz… Nie musisz… Nie wolno…", "Musisz… Nie musisz… Nie wolno…"))

T[14] = ("Непряма мова: powiedział, że jest… (час не змінюється)", "Mowa zależna: powiedział, że jest…", "Reported speech: powiedział, że jest… (no tense shift)")
G[14] = [
 ("Joey: „Przepraszam”. → Joey powiedział, że ____.", ["przeprasza", "przepraszał", "przeprosi"], 0,
  [("Так! У польській час у непрямій мові не змінюється.", "Tak! W mowie zależnej czas się nie zmienia.", "Yes! In Polish the tense doesn't change in reported speech."),
   ("Przepraszał — інший зміст.", "„Przepraszał” — inny sens.", "Przepraszał changes the meaning."),
   ("Przeprosi — майбутнє.", "„Przeprosi” — przyszłość.", "Przeprosi is future.")],
  ("Англійська: am → was. Польська: jestem → że jest.", "Angielski: am → was. Polski: jestem → że jest.", "English: am → was. Polish: jestem → że jest.")),
 ("Ross ____ Chandlerowi, że widział pocałunek.", ["powiedział", "mówił do", "rozmawiał"], 0,
  [("Так! Powiedzieć komuś (давальний), że…", "Tak! Powiedzieć komuś, że…", "Yes! Powiedzieć komuś (dative), że…"),
   ("Mówił do — без że так не кажуть.", "„Mówił do” — z że tak się nie mówi.", "Mówił do doesn't go with że."),
   ("Rozmawiał — «розмовляв», без że.", "„Rozmawiał” — bez że.", "Rozmawiał doesn't take że.")],
  ("Powiedzieć komu? co? → Chandlerowi, że…", "Powiedzieć komu? co?", "Powiedzieć + dative + że…")),
]
D[14] = ("Jesteś Rossem. Opowiedz Monice, co się stało w restauracji (35+ słów): co powiedziała Nora, co powiedział Joey i co powiedział ci Chandler.", 35,
 ("Nora powiedziała, że… Joey powiedział mi, że…", "Nora powiedziała, że… Joey powiedział mi, że…", "Nora powiedziała, że… Joey powiedział mi, że…"))

T[15] = ("Пасив: zostały zrobione (przez)", "Strona bierna: zostały zrobione (przez)", "Passive: zostały zrobione (przez)")
G[15] = [
 ("Wszystkie lasagne zostały ____ przez Monicę.", ["zrobione", "zrobiła", "robią"], 0,
  [("Так! Zostać + дієприкметник: zostały zrobione.", "Tak! Zostać + imiesłów: zostały zrobione.", "Yes! Zostać + participle: zostały zrobione."),
   ("Zrobiła — активна форма.", "„Zrobiła” — strona czynna.", "Zrobiła is active."),
   ("Robią — теперішній, активний.", "„Robią” — teraźniejszy, czynny.", "Robią is active present.")],
  ("Został / została / zostało / zostały + imiesłów (+ przez kogo).", "Został / została / zostały + imiesłów.", "Został / została / zostały + participle (+ przez).")),
 ("Stół został dostarczony ____ kuriera.", ["przez", "od", "z"], 0,
  [("Так! У пасиві — przez + знахідний.", "Tak! W stronie biernej — przez + biernik.", "Yes! In the passive — przez + accusative."),
   ("Od — «від», інший зміст.", "„Od” — inny sens.", "Od changes the meaning."),
   ("Z — «з», не для виконавця.", "„Z” — nie dla wykonawcy.", "Z doesn't show who did it.")],
  ("Zrobione przez Monicę = made by Monica.", "Zrobione przez Monicę.", "Zrobione przez Monicę = made by Monica.")),
]
D[15] = ("Opisz kawiarnię, którą lubisz (35+ słów), używając strony biernej: co jest podawane, kiedy jest otwierana, co zostało tam zrobione.", 35,
 ("Kawa jest podawana… Ciasta są pieczone… Kawiarnia została otwarta…", "Kawa jest podawana… Ciasta są pieczone… Kawiarnia została otwarta…", "Kawa jest podawana… Ciasta są pieczone… Kawiarnia została otwarta…"))

T[16] = ("Умовний спосіб: gdybym był…, zrobiłbym…", "Tryb przypuszczający: gdybym był…, zrobiłbym…", "Conditional mood: gdybym był…, zrobiłbym…")
G[16] = [
 ("Gdyby Ross był odważniejszy, ____ Rachel prawdę.", ["powiedziałby", "powie", "powiedział"], 0,
  [("Так! Уявна ситуація → форма з -by.", "Tak! Sytuacja wyobrażona → forma z -by.", "Yes! Imaginary situation → the -by form."),
   ("Powie — реальне майбутнє.", "„Powie” — realna przyszłość.", "Powie is real future."),
   ("Powiedział — минуле.", "„Powiedział” — przeszłość.", "Powiedział is past.")],
  ("Gdyby + -by: gdybym miał…, kupiłbym…", "Gdyby + -by.", "Gdyby + -by: gdybym miał…, kupiłbym…")),
 ("Phoebe: „Na twoim miejscu ____ wszystko!”", ["spaliłabym", "spalę", "spaliłam"], 0,
  [("Так! Фібі (жінка, я) → spaliłabym.", "Tak! Phoebe (kobieta, ja) → spaliłabym.", "Yes! Phoebe (a woman, I) → spaliłabym."),
   ("Spalę — реальний план.", "„Spalę” — realny plan.", "Spalę is a real plan."),
   ("Spaliłam — минуле.", "„Spaliłam” — przeszłość.", "Spaliłam is past.")],
  ("Na twoim miejscu = If I were you.", "Na twoim miejscu = If I were you.", "Na twoim miejscu = If I were you.")),
]
D[16] = ("Co byś zrobił(a) w walentynki, gdybyś był(a) jednym z przyjaciół? (35+ słów). Użyj: gdybym…, -bym, na twoim miejscu.", 35,
 ("Gdybym był Rossem, … Na miejscu Moniki…", "Gdybym był Rossem, … Na miejscu Moniki…", "Gdybym był Rossem, … Na miejscu Moniki…"))

T[17] = ("Припущення: na pewno / chyba / może / nie może być", "Przypuszczenia: na pewno / chyba / może / nie może być", "Deduction: na pewno / chyba / może / nie może być")
G[17] = [
 ("Zjadł dwanaście taco. ____ jest bardzo głodny!", ["Na pewno", "Na pewno nie", "Wcale"], 0,
  [("Так! Упевнений висновок → na pewno.", "Tak! Pewny wniosek → na pewno.", "Yes! A confident conclusion → na pewno."),
   ("Na pewno nie — протилежне.", "„Na pewno nie” — odwrotnie.", "Na pewno nie is the opposite."),
   ("Wcale — лише із запереченням.", "„Wcale” — tylko z przeczeniem.", "Wcale only works with a negative.")],
  ("Na pewno ≈ must; może ≈ might; to nie może być ≈ can't be.", "Na pewno ≈ must; może ≈ might.", "Na pewno ≈ must; może ≈ might; nie może być ≈ can't be.")),
 ("Śmieje się z zupy. To ____ być poważny gość.", ["nie może", "musi", "powinien"], 0,
  [("Так! «Точно ні» → nie może być.", "Tak! „Na pewno nie” → nie może być.", "Yes! “Surely not” → nie może być."),
   ("Musi — упевнене «так».", "„Musi” — pewne „tak”.", "Musi is a confident yes."),
   ("Powinien — порада.", "„Powinien” — rada.", "Powinien is advice.")],
  ("To nie może być prawda! = That can't be true!", "To nie może być prawda!", "To nie może być prawda! = That can't be true!")),
]
D[17] = ("Jesteś Rachel. Napisz do Phoebe o dziwnym gościu (35+ słów): co na pewno jest prawdą, co może być powodem, a co nie może być prawdą.", 35,
 ("Na pewno… Może… To nie może być…", "Na pewno… Może… To nie może być…", "Na pewno… Może… To nie może być…"))

# ---- Арка 4
T[19] = ("Питання-підтвердження: …, prawda? / …, nie?", "Pytania potwierdzające: …, prawda? / …, nie?", "Tag questions: …, prawda? / …, nie?")
G[19] = [
 ("Phoebe: „Spotykasz się z moją siostrą, ____?”", ["prawda", "czy", "co"], 0,
  [("Так! «…, prawda?» — польський хвостик, який ніколи не змінюється.", "Tak! „…, prawda?” — dopisek, który się nie zmienia.", "Yes! “…, prawda?” — the Polish tag never changes."),
   ("Czy ставиться на початку питання.", "„Czy” stoi na początku pytania.", "Czy goes at the start of a question."),
   ("Co — «що», не підтвердження.", "„Co” to pytanie o rzecz.", "Co means “what”.")],
  ("Англійська змінює хвостик (aren't you / do you), польська — ні.", "Angielski zmienia dopisek, polski — nie.", "English tags change (aren't you / do you); Polish ones don't.")),
 ("Ursula: „Nie lubisz mnie, ____?”", ["co", "czy", "jak"], 0,
  [("Так! «…, co?» — розмовний хвостик.", "Tak! „…, co?” — potoczny dopisek.", "Yes! “…, co?” is an informal tag."),
   ("Czy — на початку питання.", "„Czy” — na początku pytania.", "Czy goes at the start."),
   ("Jak — «як», інше питання.", "„Jak” — inne pytanie.", "Jak means “how”.")],
  ("…, prawda? (нейтрально), …, nie? / …, co? (розмовно).", "…, prawda? (neutralnie), …, nie? / …, co? (potocznie).", "…, prawda? (neutral), …, nie? / …, co? (informal).")),
]
D[19] = ("Napisz krótką rozmowę Phoebe i Joeya o Ursuli (35+ słów). Użyj co najmniej pięciu pytań z „prawda?”, „nie?” albo „co?”.", 35,
 ("Lubisz ją, prawda? Nie gniewasz się, co?", "Lubisz ją, prawda? Nie gniewasz się, co?", "Lubisz ją, prawda? Nie gniewasz się, co?"))

T[20] = ("Так / такий: tak bolesne, taki zły pomysł", "Tak / taki: tak bolesne, taki zły pomysł", "So / such: tak bolesne, taki zły pomysł")
G[20] = [
 ("Rachel tak ____ boli, że nie może chodzić.", ["bardzo", "taki", "taka"], 0,
  [("Так! Tak bardzo + дієслово.", "Tak! Tak bardzo + czasownik.", "Yes! Tak bardzo + verb."),
   ("Taki — з іменником (чол. рід).", "„Taki” — z rzeczownikiem (r. męski).", "Taki goes with a masculine noun."),
   ("Taka — з іменником (жін. рід).", "„Taka” — z rzeczownikiem (r. żeński).", "Taka goes with a feminine noun.")],
  ("Tak + прикметник/прислівник; taki/taka/takie + іменник.", "Tak + przymiotnik/przysłówek; taki/taka/takie + rzeczownik.", "Tak + adjective/adverb; taki/taka/takie + noun.")),
 ("Monica: „To ____ zły pomysł!”", ["taki", "tak", "taka"], 0,
  [("Так! Pomysł — чол. рід → taki.", "Tak! Pomysł (r. męski) → taki.", "Yes! Pomysł is masculine → taki."),
   ("Tak — перед прикметником без іменника.", "„Tak” — przed przymiotnikiem bez rzeczownika.", "Tak goes before an adjective with no noun."),
   ("Taka — жіночий рід.", "„Taka” — rodzaj żeński.", "Taka is feminine.")],
  ("Taki zły pomysł, taka trudna sytuacja, takie drogie.", "Taki zły pomysł, taka trudna sytuacja.", "Taki zły pomysł, taka trudna sytuacja, takie drogie.")),
]
D[20] = ("Jesteś Monicą. Opisz w pamiętniku podwójną randkę (35+ słów). Użyj: tak, taki/taka, tak… że.", 35,
 ("Lekarze byli tak… To był taki… Byłam tak zła, że…", "Lekarze byli tak… To był taki… Byłam tak zła, że…", "Lekarze byli tak… To był taki… Byłam tak zła, że…"))

T[21] = ("Ступені порівняння: lepszy, mądrzejszy, najlepszy, tak … jak", "Stopniowanie: lepszy, mądrzejszy, najlepszy, tak … jak", "Comparison: lepszy, mądrzejszy, najlepszy, tak … jak")
G[21] = [
 ("Na początku chłopaki grają ____ niż dziewczyny.", ["lepiej", "dobrzej", "najlepiej"], 0,
  [("Так! Dobrze → lepiej (прислівник).", "Tak! Dobrze → lepiej.", "Yes! Dobrze → lepiej (adverb)."),
   ("Dobrzej — такої форми немає.", "„Dobrzej” nie istnieje.", "Dobrzej doesn't exist."),
   ("Najlepiej — найвищий ступінь.", "„Najlepiej” — stopień najwyższy.", "Najlepiej is the superlative.")],
  ("Dobry → lepszy → najlepszy; dobrze → lepiej → najlepiej.", "Dobry → lepszy → najlepszy.", "Dobry → lepszy → najlepszy; dobrze → lepiej → najlepiej.")),
 ("Po lekcji Monica jest ____ graczką przy stole.", ["najlepszą", "lepszą", "dobrą"], 0,
  [("Так! Найвищий ступінь + орудний: najlepszą.", "Tak! Stopień najwyższy + narzędnik.", "Yes! Superlative + instrumental: najlepszą."),
   ("Lepszą — порівняння двох.", "„Lepszą” — porównanie dwóch.", "Lepszą compares two."),
   ("Dobrą — без порівняння.", "„Dobrą” — bez porównania.", "Dobrą doesn't compare.")],
  ("Jest najlepszą graczką = She's the best player.", "Jest najlepszą graczką.", "Jest najlepszą graczką = She's the best player.")),
]
D[21] = ("Porównaj szóstkę przyjaciół (35+ słów): kto jest najzabawniejszy, kto mądrzejszy od Joeya, kto lubi rywalizację tak jak Monica.", 35,
 ("Chandler jest najzabawniejszy… Ross jest mądrzejszy niż… Nikt nie jest tak … jak…", "Chandler jest najzabawniejszy… Ross jest mądrzejszy niż… Nikt nie jest tak … jak…", "Chandler jest najzabawniejszy… Ross jest mądrzejszy niż… Nikt nie jest tak … jak…"))

T[22] = ("Що сталося раніше: już + доконаний, zanim", "Co stało się wcześniej: już + dokonany, zanim", "What happened earlier: już + perfective, zanim")
G[22] = [
 ("Kiedy Rachel wróciła, Marcel ____ uciekł.", ["już", "jeszcze", "zaraz"], 0,
  [("Так! Już + доконаний = дія завершилася раніше.", "Tak! Już + dokonany = czynność skończyła się wcześniej.", "Yes! Już + perfective = it was already finished."),
   ("Jeszcze — «ще», інший зміст.", "„Jeszcze” — inny sens.", "Jeszcze means “still/yet”."),
   ("Zaraz — «зараз, скоро».", "„Zaraz” — „za chwilę”.", "Zaraz means “in a moment”.")],
  ("Польська не має Past Perfect: już uciekł = had already escaped.", "Polski nie ma Past Perfect: już uciekł.", "Polish has no Past Perfect: już uciekł = had already escaped.")),
 ("____ Ross przyjechał, przyjaciele przeszukali cały budynek.", ["Zanim", "Kiedy już", "Po tym"], 0,
  [("Так! Zanim = by the time / before.", "Tak! Zanim = by the time.", "Yes! Zanim = by the time / before."),
   ("Kiedy już — неприродно тут.", "„Kiedy już” — tu nienaturalnie.", "Kiedy już sounds unnatural here."),
   ("Po tym — потрібне «jak».", "„Po tym” wymaga „jak”.", "Po tym needs “jak”.")],
  ("Zanim + доконаний вид.", "Zanim + aspekt dokonany.", "Zanim + perfective.")),
]
D[22] = ("Jesteś Rachel. Napisz do Rossa o tamtym popołudniu (35+ słów): co już się stało, zanim wróciłaś, i co zrobiliście, zanim przyjechał.", 35,
 ("Kiedy wróciłam, Marcel już… Zanim przyjechałeś, przeszukaliśmy…", "Kiedy wróciłam, Marcel już… Zanim przyjechałeś, przeszukaliśmy…", "Kiedy wróciłam, Marcel już… Zanim przyjechałeś, przeszukaliśmy…"))

T[23] = ("Тривалі дії: spotyka się od dwóch tygodni", "Czynności trwające: spotyka się od dwóch tygodni", "Ongoing actions: spotyka się od dwóch tygodni")
G[23] = [
 ("Rachel ____ się z Barrym od dwóch tygodni.", ["spotyka", "spotkała", "spotka"], 0,
  [("Так! Дія триває досі → теперішній час + od.", "Tak! Czynność trwa → czas teraźniejszy + od.", "Yes! Still going on → present tense + od."),
   ("Spotkała — один раз у минулому.", "„Spotkała” — raz w przeszłości.", "Spotkała is once in the past."),
   ("Spotka — майбутнє.", "„Spotka” — przyszłość.", "Spotka is future.")],
  ("Present Perfect Continuous → польський теперішній + od.", "Present Perfect Continuous → czas teraźniejszy + od.", "Present Perfect Continuous → Polish present + od.")),
 ("Chandler czeka przy telefonie ____ dziesiątej rano.", ["od", "przez", "za"], 0,
  [("Так! Od + родовий = з якогось моменту.", "Tak! Od + dopełniacz.", "Yes! Od + genitive = since."),
   ("Przez — «протягом», інша конструкція.", "„Przez” — inna konstrukcja.", "Przez is a different structure."),
   ("Za — у майбутньому.", "„Za” — w przyszłości.", "Za means “in” (future).")],
  ("Od dziesiątej, od wtorku, od dwóch tygodni.", "Od dziesiątej, od wtorku.", "Od dziesiątej, od wtorku, od dwóch tygodni.")),
]
D[23] = ("Jesteś Monicą. Napisz wiadomość do Rachel (35+ słów). Zapytaj, od jak dawna spotyka się z Barrym, i napisz, co ostatnio zauważasz.", 35,
 ("Od jak dawna się z nim spotykasz? Ostatnio ciągle… Martwię się od…", "Od jak dawna się z nim spotykasz? Ostatnio ciągle… Martwię się od…", "Od jak dawna się z nim spotykasz? Ostatnio ciągle… Martwię się od…"))
