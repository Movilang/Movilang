# HIMYM S1 (B1–B2).
G = {}
D = {}
T = {}

# ---- Łuk 1
T[1] = ("Минулий час: доконаний і недоконаний вид", "Czas przeszły: aspekt dokonany i niedokonany", "Past tense: perfective vs imperfective")
G[1] = [
 ("Kiedy Ted ____ do baru, Robin siedziała przy stoliku.", ["wszedł", "wchodził", "wejdzie"], 0,
  [("Так! Коротка завершена дія → доконаний вид.", "Tak! Krótka, zakończona czynność → dokonany.", "Yes! A short completed action → perfective."),
   ("Wchodził — процес, а тут подія.", "„Wchodził” — proces, a tu wydarzenie.", "Wchodził is a process; here it's an event."),
   ("Wejdzie — майбутнє.", "„Wejdzie” — przyszłość.", "Wejdzie is future.")],
  ("Фон — недоконаний (siedziała), подія — доконаний (wszedł).", "Tło — niedokonany, wydarzenie — dokonany.", "Background — imperfective, event — perfective.")),
 ("Marshall ____ się Lily wczoraj wieczorem.", ["oświadczył", "oświadczał", "oświadcza"], 0,
  [("Так! Один раз, результат → oświadczył.", "Tak! Jednorazowo, z rezultatem.", "Yes! Once, with a result → oświadczył."),
   ("Oświadczał — неодноразово або процес.", "„Oświadczał” — wielokrotnie lub proces.", "Oświadczał is repeated or ongoing."),
   ("Oświadcza — теперішній.", "„Oświadcza” — teraźniejszy.", "Oświadcza is present.")],
  ("Доконаний вид = результат.", "Aspekt dokonany = rezultat.", "Perfective = result.")),
]
D[1] = ("Opisz wieczór, kiedy poznałeś(-aś) kogoś ważnego (50+ słów). Użyj aspektu dokonanego i niedokonanego.", 50,
 ("Siedziałem w barze, kiedy… Rozmawialiśmy… Potem…", "Siedziałem w barze, kiedy… Rozmawialiśmy… Potem…", "Siedziałem w barze, kiedy… Rozmawialiśmy… Potem…"))

T[2] = ("już / jeszcze nie + вид дієслова", "już / jeszcze nie + aspekt", "już / jeszcze nie + aspect")
G[2] = [
 ("Robin jeszcze nie ____.", ["przyszła", "przychodzi", "przyjdzie"], 0,
  [("Так! Jeszcze nie + доконаний минулий.", "Tak! Jeszcze nie + dokonany.", "Yes! Jeszcze nie + perfective past."),
   ("Теперішній тут не пасує.", "Teraźniejszy nie pasuje.", "Present doesn't fit."),
   ("Майбутнє — інший зміст.", "Przyszłość — inny sens.", "Future changes the meaning.")],
  ("Англ. haven't … yet ≈ jeszcze nie + минулий доконаний.", "Haven't … yet ≈ jeszcze nie + dokonany.", "Haven't … yet ≈ jeszcze nie + perfective past.")),
 ("Ted ____ imprezy od tygodnia.", ["urządza", "urządził", "urządzi"], 0,
  [("Так! Od tygodnia + теперішній = have been doing.", "Tak! Od tygodnia + teraźniejszy.", "Yes! Od tygodnia + present = have been doing."),
   ("Минулий не показує, що дія триває.", "Przeszły nie pokazuje trwania.", "Past doesn't show it's ongoing."),
   ("Майбутнє — ні.", "Przyszłość — nie.", "Not future.")],
  ("Польська: od + теперішній час.", "Polski: od + czas teraźniejszy.", "Polish: od + present tense.")),
]
D[2] = ("Napisz wiadomość do przyjaciela (50+ słów): co już zrobiłeś(-aś) w tym miesiącu, a czego jeszcze nie.", 50,
 ("Już… Jeszcze nie… Od tygodnia…", "Już… Jeszcze nie… Od tygodnia…", "Już… Jeszcze nie… Od tygodnia…"))

T[3] = ("Майбутній час: zrobię / będę robić", "Czas przyszły: zrobię / będę robić", "Future: zrobię / będę robić")
G[3] = [
 ("Dziś wieczorem ____ do Filadelfii!", ["polecimy", "lecieliśmy", "latamy"], 0,
  [("Так! Один конкретний рейс → доконаний майбутній.", "Tak! Konkretny lot → dokonany.", "Yes! A single trip → perfective future."),
   ("Минулий.", "Przeszły.", "Past."),
   ("Latamy — регулярно.", "„Latamy” — regularnie.", "Latamy means regularly.")],
  ("Доконаний вид у теперішній формі = майбутнє.", "Dokonany w formie teraźniejszej = przyszłość.", "Perfective present form = future.")),
 ("Całą noc ____ się bawić!", ["będziemy", "będą", "byliśmy"], 0,
  [("Так! Będziemy + інфінітив = процес у майбутньому.", "Tak! Będziemy + bezokolicznik.", "Yes! Będziemy + infinitive = ongoing future."),
   ("Będą — вони.", "„Będą” — oni.", "Będą is they."),
   ("Минулий.", "Przeszły.", "Past.")],
  ("Будемо робити = być + недоконаний.", "Będę robić = być + niedokonany.", "Będę robić = być + imperfective.")),
]
D[3] = ("Zaplanuj idealny weekend (50+ słów). Co zrobisz? Co będziesz robić całą sobotę?", 50,
 ("W sobotę pojedziemy… Będziemy… Na pewno zobaczymy…", "W sobotę pojedziemy… Będziemy… Na pewno zobaczymy…", "W sobotę pojedziemy… Będziemy… Na pewno zobaczymy…"))

T[4] = ("Висновки: musi być / może być / nie może być", "Wnioskowanie: musi być / może być / nie może być", "Deduction: musi być / może być / nie może być")
G[4] = [
 ("Ted ciągle wzdycha. On ____ być nieszczęśliwy.", ["musi", "może nie", "nie musi"], 0,
  [("Так! Упевнений висновок → musi.", "Tak! Pewny wniosek → musi.", "Yes! A confident deduction → musi."),
   ("Це сумнів, а докази сильні.", "To wątpliwość, a dowody są mocne.", "That's doubt, but the evidence is strong."),
   ("Nie musi = не обов'язково.", "„Nie musi” = nie trzeba.", "Nie musi = doesn't have to.")],
  ("Musi być = must be; nie może być = can't be.", "Musi być = must be; nie może być = can't be.", "Musi być = must be; nie może być = can't be.")),
 ("To ____ być znak. Kto wie?", ["może", "musi", "nie może"], 0,
  [("Так! Можливо → może.", "Tak! Możliwe → może.", "Yes! Possibly → może."),
   ("Musi — надто впевнено.", "„Musi” — za pewne.", "Musi is too certain."),
   ("Nie może — протилежне.", "„Nie może” — odwrotnie.", "Nie może is the opposite.")],
  ("Może być = might be.", "Może być = might be.", "Może być = might be.")),
]
D[4] = ("Opisz nieznajomych na zdjęciu (50+ słów) i zgadnij, kim są. Użyj: musi być, może być, nie może być.", 50,
 ("Oni muszą być… Ona może być… On nie może być…", "Oni muszą być… Ona może być… On nie może być…", "Oni muszą być… Ona może być… On nie może być…"))

T[5] = ("Kiedyś + недоконаний; przyzwyczaić się do", "Kiedyś + niedokonany; przyzwyczaić się do", "Kiedyś + imperfective; przyzwyczaić się do")
G[5] = [
 ("Kiedyś Ted co roku ____ na dachu do rana.", ["czekał", "poczekał", "czeka"], 0,
  [("Так! Повторювана дія → недоконаний.", "Tak! Powtarzana czynność → niedokonany.", "Yes! A repeated action → imperfective."),
   ("Poczekał — один раз.", "„Poczekał” — raz.", "Poczekał means once."),
   ("Теперішній.", "Teraźniejszy.", "Present.")],
  ("Used to / would ≈ kiedyś + недоконаний вид.", "Used to / would ≈ kiedyś + niedokonany.", "Used to / would ≈ kiedyś + imperfective.")),
 ("Ted jest przyzwyczajony do ____ w samotności.", ["czekania", "czekać", "czeka"], 0,
  [("Так! Do + віддієслівний іменник у родовому.", "Tak! Do + rzeczownik odczasownikowy w dopełniaczu.", "Yes! Do + verbal noun in the genitive."),
   ("Після do — не інфінітив.", "Po „do” — nie bezokolicznik.", "No infinitive after do."),
   ("Особова форма — ні.", "Forma osobowa — nie.", "Not a personal form.")],
  ("Be used to + -ing = przyzwyczajony do + -ania.", "Be used to + -ing = przyzwyczajony do + -ania.", "Be used to + -ing = przyzwyczajony do + -ania.")),
]
D[5] = ("Opisz swoje dzieciństwo (50+ słów): co kiedyś robiłeś(-aś), do czego się przyzwyczaiłeś(-aś).", 50,
 ("Kiedyś co lato… Codziennie chodziłem… Teraz jestem przyzwyczajony do…", "Kiedyś co lato… Codziennie chodziłem… Teraz jestem przyzwyczajony do…", "Kiedyś co lato… Codziennie chodziłem… Teraz jestem przyzwyczajony do…"))

# ---- Łuk 2
T[7] = ("Умовний спосіб: gdybym był…, byłbym…", "Tryb przypuszczający: gdybym był…, byłbym…", "Conditional: gdybym był…, byłbym…")
G[7] = [
 ("Gdybyśmy ____ w klubie, nudzilibyśmy się.", ["byli", "jesteśmy", "będziemy"], 0,
  [("Так! Gdyby + минула форма.", "Tak! Gdyby + forma przeszła.", "Yes! Gdyby + past form."),
   ("Теперішній — ні.", "Nie.", "No."),
   ("Майбутній — ні.", "Nie.", "No.")],
  ("Gdyby + -śmy/-m + минула форма.", "Gdyby + forma przeszła.", "Gdyby + past form.")),
 ("Na twoim miejscu ____ do domu.", ["poszedłbym", "pójdę", "szedłem"], 0,
  [("Так! -bym = would.", "Tak! -bym.", "Yes! -bym = would."),
   ("Майбутній.", "Przyszły.", "Future."),
   ("Минулий.", "Przeszły.", "Past.")],
  ("Poszedłbym = I would go.", "Poszedłbym = I would go.", "Poszedłbym = I would go.")),
]
D[7] = ("Co byś zrobił(a), gdybyś miał(a) jeden wolny dzień (50+ słów)? Użyj trybu przypuszczającego.", 50,
 ("Gdybym miał wolny dzień, pojechałbym… Spotkałbym… Nie robiłbym…", "Gdybym miał wolny dzień, pojechałbym… Spotkałbym… Nie robiłbym…", "Gdybym miał wolny dzień, pojechałbym… Spotkałbym… Nie robiłbym…"))

T[8] = ("Нереальне минуле: gdybym wiedział, nie przyszedłbym", "Nierealna przeszłość: gdybym wiedział, nie przyszedłbym", "Unreal past: gdybym wiedział, nie przyszedłbym")
G[8] = [
 ("Gdybyś nie był taki wybredny, już ____ kogoś znaleźli.", ["byśmy", "będziemy", "jesteśmy"], 0,
  [("Так! Znaleźlibyśmy = znaleźli + byśmy.", "Tak! Byśmy.", "Yes! Byśmy = we would."),
   ("Майбутній.", "Przyszły.", "Future."),
   ("Теперішній.", "Teraźniejszy.", "Present.")],
  ("У польській той самий умовний для теперішнього й минулого.", "Ten sam tryb dla teraźniejszości i przeszłości.", "Polish uses the same conditional for present and past.")),
 ("Gdybym ____, że to takie drogie, nie przyszedłbym.", ["wiedział", "wiem", "będę wiedział"], 0,
  [("Так!", "Tak!", "Yes!"),
   ("Теперішній.", "Teraźniejszy.", "Present."),
   ("Майбутній.", "Przyszły.", "Future.")],
  ("Минулий контекст видно зі змісту.", "Przeszłość wynika z kontekstu.", "The past comes from context.")),
]
D[8] = ("Opisz chwilę, która zmieniła twoje życie (50+ słów). Co by było, gdyby się nie wydarzyła?", 50,
 ("Gdybym wtedy nie…, nigdy bym nie… Gdybym…, mógłbym…", "Gdybym wtedy nie…, nigdy bym nie… Gdybym…, mógłbym…", "Gdybym wtedy nie…, nigdy bym nie… Gdybym…, mógłbym…"))

T[9] = ("Бажання: szkoda, że… / chciałbym, żeby… / gdyby tylko", "Życzenia: szkoda, że… / chciałbym, żeby… / gdyby tylko", "Wishes: szkoda, że… / chciałbym, żeby… / gdyby tylko")
G[9] = [
 ("Szkoda, że nie ____ wyższa.", ["jestem", "byłabym", "będę"], 0,
  [("Так! Szkoda, że + звичайний час.", "Tak! Szkoda, że + zwykły czas.", "Yes! Szkoda, że + normal tense."),
   ("Умовний тут не потрібен.", "Bez trybu przypuszczającego.", "No conditional here."),
   ("Майбутній.", "Przyszły.", "Future.")],
  ("I wish I were = szkoda, że nie jestem.", "I wish I were = szkoda, że nie jestem.", "I wish I were = szkoda, że nie jestem.")),
 ("Chciałbym, żeby bracia przestali ____ ze mną droczyć.", ["się", "sobie", "siebie"], 0,
  [("Так! Droczyć się.", "Tak! Droczyć się.", "Yes! Droczyć się."),
   ("Ні.", "Nie.", "No."),
   ("Ні.", "Nie.", "No.")],
  ("Chciałbym, żeby + минула форма.", "Chciałbym, żeby + forma przeszła.", "Chciałbym, żeby + past form.")),
]
D[9] = ("Napisz o trzech życzeniach (50+ słów). Użyj: szkoda, że…; chciałbym, żeby…; gdyby tylko…", 50,
 ("Szkoda, że nie… Chciałbym, żeby… Gdyby tylko…", "Szkoda, że nie… Chciałbym, żeby… Gdyby tylko…", "Szkoda, że nie… Chciałbym, żeby… Gdyby tylko…"))

T[10] = ("Непряма мова: powiedział, że…", "Mowa zależna: powiedział, że…", "Reported speech: powiedział, że…")
G[10] = [
 ("Barney: „Możesz wypić pięć”. → Barney powiedział, że Ted ____ wypić pięć.", ["może", "mógł", "mógłby"], 0,
  [("Так! У польській час НЕ зсувається.", "Tak! Czas się nie zmienia.", "Yes! Polish doesn't backshift."),
   ("Англійська звичка — тут зайва.", "Angielski nawyk.", "An English habit — not needed."),
   ("Інший зміст.", "Inny sens.", "Different meaning.")],
  ("Польська: час залишається, як у прямій мові.", "Czas zostaje taki jak w mowie niezależnej.", "Polish keeps the original tense.")),
 ("Lily ____ Tedowi, że do niego zadzwoniła.", ["powiedziała", "mówiła się", "powiedziało"], 0,
  [("Так!", "Tak!", "Yes!"),
   ("Ні.", "Nie.", "No."),
   ("Рід!", "Rodzaj!", "Gender!")],
  ("Powiedzieć komuś (celownik), że…", "Powiedzieć komuś, że…", "Powiedzieć komuś (dative), że…")),
]
D[10] = ("Przekaż rozmowę, którą niedawno odbyłeś(-aś) (50+ słów). Co powiedział rozmówca? Co obiecałeś(-aś)?", 50,
 ("Kolega powiedział, że… Zapytał, czy… Obiecałem, że…", "Kolega powiedział, że… Zapytał, czy… Obiecałem, że…", "Kolega powiedział, że… Zapytał, czy… Obiecałem, że…"))

T[11] = ("Пасив: został zorganizowany / jest robiony", "Strona bierna: został zorganizowany / jest robiony", "Passive: został zorganizowany / jest robiony")
G[11] = [
 ("Impreza ____ odwołana.", ["została", "został", "zostało"], 0,
  [("Так! Impreza — жіночий рід.", "Tak! Rodzaj żeński.", "Yes! Impreza is feminine."),
   ("Чоловічий.", "Męski.", "Masculine."),
   ("Середній.", "Nijaki.", "Neuter.")],
  ("Zostać (минуле, результат) + дієприкметник.", "Zostać + imiesłów.", "Zostać + participle (completed).")),
 ("Limuzyna ____ prowadzona przez Ranjita.", ["była", "został", "jest być"], 0,
  [("Так! Być + дієприкметник — процес.", "Tak! Być + imiesłów.", "Yes! Być + participle — a process."),
   ("Рід.", "Rodzaj.", "Gender."),
   ("Ні.", "Nie.", "No.")],
  ("Być = стан/процес, zostać = результат.", "Być = proces, zostać = rezultat.", "Być = process, zostać = result.")),
]
D[11] = ("Opisz duże wydarzenie w twoim mieście (50+ słów). Jak jest organizowane? Co zostało zrobione w zeszłym roku?", 50,
 ("Festiwal jest organizowany przez… W zeszłym roku została zbudowana… Wszystko było…", "Festiwal jest organizowany przez… W zeszłym roku została zbudowana… Wszystko było…", "Festiwal jest organizowany przez… W zeszłym roku została zbudowana… Wszystko było…"))

# ---- Łuk 3
T[13] = ("Підрядні речення: który, która, które, którego", "Zdania względne: który, która, które, którego", "Relative clauses: który, która, które, którego")
G[13] = [
 ("Victoria to dziewczyna, ____ upiekła tort.", ["która", "który", "które"], 0,
  [("Так! Dziewczyna — жіночий рід.", "Tak! Rodzaj żeński.", "Yes! Feminine."),
   ("Чоловічий.", "Męski.", "Masculine."),
   ("Середній.", "Nijaki.", "Neuter.")],
  ("Który узгоджується з іменником у роді й числі.", "Który zgadza się z rzeczownikiem.", "Który agrees with the noun.")),
 ("To tort, ____ nigdy nie zapomnę.", ["którego", "który", "którym"], 0,
  [("Так! Zapomnieć + родовий.", "Tak! Zapomnieć + dopełniacz.", "Yes! Zapomnieć takes the genitive."),
   ("Називний — ні.", "Mianownik — nie.", "Not nominative."),
   ("Орудний — ні.", "Narzędnik — nie.", "Not instrumental.")],
  ("Відмінок który залежить від дієслова в підрядному.", "Przypadek zależy od czasownika.", "The case depends on the verb in the clause.")),
]
D[13] = ("Opisz osobę, którą spotkałeś(-aś) tylko raz (50+ słów). Użyj: który, która, którego, gdzie.", 50,
 ("Raz poznałem kobietę, która… To było w miejscu, gdzie… Miała psa, którego…", "Raz poznałem kobietę, która… To było w miejscu, gdzie… Miała psa, którego…", "Raz poznałem kobietę, która… To było w miejscu, gdzie… Miała psa, którego…"))

T[14] = ("Інфінітив чи віддієслівний іменник: lubię czytać / unikam czytania", "Bezokolicznik czy rzeczownik odczasownikowy", "Infinitive or verbal noun")
G[14] = [
 ("Ted nie może przestać ____ o Victorii.", ["myśleć", "myślenia", "myśli"], 0,
  [("Так! Przestać + інфінітив.", "Tak! Przestać + bezokolicznik.", "Yes! Przestać + infinitive."),
   ("Іменник тут не йде.", "Nie rzeczownik.", "Not a noun here."),
   ("Особова форма.", "Forma osobowa.", "A personal form.")],
  ("Przestać, chcieć, próbować + інфінітив.", "Przestać, chcieć, próbować + bezokolicznik.", "Przestać, chcieć, próbować + infinitive.")),
 ("Ted unika ____ na torty.", ["patrzenia", "patrzeć", "patrzy"], 0,
  [("Так! Unikać + родовий: patrzenia.", "Tak! Unikać + dopełniacz.", "Yes! Unikać + genitive."),
   ("Unikać не з інфінітивом.", "Nie z bezokolicznikiem.", "Not with an infinitive."),
   ("Ні.", "Nie.", "No.")],
  ("Unikać / bać się + -nia (родовий).", "Unikać / bać się + -nia.", "Unikać / bać się + -nia (genitive).")),
]
D[14] = ("Napisz o swoim hobby (50+ słów): co lubisz robić, czego unikasz, czego chcesz spróbować.", 50,
 ("Lubię… Unikam… Chcę spróbować… Nie mogę przestać…", "Lubię… Unikam… Chcę spróbować… Nie mogę przestać…", "Lubię… Unikam… Chcę spróbować… Nie mogę przestać…"))

T[15] = ("Префікси дієслів: wymyślić, rozłożyć, zerwać, przebrać się", "Przedrostki: wymyślić, rozłożyć, zerwać, przebrać się", "Verb prefixes: wymyślić, rozłożyć, zerwać, przebrać się")
G[15] = [
 ("Lily ____ nową grę.", ["wymyśliła", "myślała", "pomyślała o"], 0,
  [("Так! Wy- + myślić = come up with.", "Tak! Wymyślić = come up with.", "Yes! Wy- + myślić = come up with."),
   ("Myśleć = просто думати.", "„Myśleć” = po prostu myśleć.", "Myśleć just means think."),
   ("Інший зміст.", "Inny sens.", "Different meaning.")],
  ("Префікс змінює зміст, як частинка у phrasal verb.", "Przedrostek zmienia znaczenie.", "The prefix changes the meaning, like a particle in a phrasal verb.")),
 ("Dziewczyna ____ z Barneyem.", ["zerwała", "rwała", "porwała"], 0,
  [("Так! Zerwać z = break up with.", "Tak!", "Yes! Zerwać z = break up with."),
   ("Rwać = рвати.", "„Rwać” = rwać.", "Rwać = tear."),
   ("Porwać = викрасти!", "„Porwać” = uprowadzić!", "Porwać = kidnap!")],
  ("Zerwać z kimś = розлучитися.", "Zerwać z kimś.", "Zerwać z kimś = break up with someone.")),
]
D[15] = ("Opisz zmianę w swoim życiu (50+ słów). Użyj co najmniej pięciu czasowników z przedrostkami.", 50,
 ("Kiedyś rzuciłem… Potem zacząłem… Wymyśliłem… Dowiedziałem się…", "Kiedyś rzuciłem… Potem zacząłem… Wymyśliłem… Dowiedziałem się…", "Kiedyś rzuciłem… Potem zacząłem… Wymyśliłem… Dowiedziałem się…"))

T[16] = ("Доручення: oddać do przeróbki, dać do naprawy, zamówić", "Zlecanie: oddać do przeróbki, dać do naprawy, zamówić", "Getting things done: oddać do przeróbki, dać do naprawy")
G[16] = [
 ("Lily oddała suknię do ____.", ["przeróbki", "przerobić", "przeróbka"], 0,
  [("Так! Do + родовий.", "Tak! Do + dopełniacz.", "Yes! Do + genitive."),
   ("Інфінітив — ні.", "Nie bezokolicznik.", "Not the infinitive."),
   ("Називний — ні.", "Nie mianownik.", "Not nominative.")],
  ("Have something altered ≈ oddać coś do przeróbki.", "Oddać do przeróbki.", "Have something altered ≈ oddać do przeróbki.")),
 ("Marshall ____ sobie garnitur na miarę.", ["uszył", "szył się", "uszyto"], 0,
  [("Так! Польська часто каже «uszył sobie», хоча шив кравець.", "Tak! Mówimy „uszył sobie”.", "Yes! Polish says uszył sobie even when a tailor did it."),
   ("Ні.", "Nie.", "No."),
   ("Безособова форма — без Маршалла.", "Forma bezosobowa.", "Impersonal — no Marshall.")],
  ("Obciąłem włosy = I had my hair cut.", "Obciąłem włosy u fryzjera.", "Obciąłem włosy = I had my hair cut.")),
]
D[16] = ("Napisz, co ostatnio oddałeś(-aś) do naprawy, przeróbki lub co zamówiłeś(-aś) (50+ słów).", 50,
 ("W zeszłym tygodniu oddałem… do naprawy. Obciąłem włosy… Zamówiłem…", "W zeszłym tygodniu oddałem… do naprawy. Obciąłem włosy… Zamówiłem…", "W zeszłym tygodniu oddałem… do naprawy. Obciąłem włosy… Zamówiłem…"))

T[17] = ("Змішані умовні: gdybym został, byłbym teraz bogaty", "Mieszane: gdybym został, byłbym teraz bogaty", "Mixed: gdybym został, byłbym teraz bogaty")
G[17] = [
 ("Gdybyś wtedy został, ____ teraz bogaty.", ["byłbyś", "będziesz", "jesteś"], 0,
  [("Так!", "Tak!", "Yes!"),
   ("Майбутній.", "Przyszły.", "Future."),
   ("Теперішній.", "Teraźniejszy.", "Present.")],
  ("Слова wtedy / teraz показують час.", "„Wtedy” i „teraz” pokazują czas.", "Wtedy / teraz show the time.")),
 ("Gdybym był taki jak oni, dawno ____ odszedł.", ["bym", "będę", "jestem"], 0,
  [("Так!", "Tak!", "Yes!"),
   ("Ні.", "Nie.", "No."),
   ("Ні.", "Nie.", "No.")],
  ("Odszedłbym = odszedł + bym.", "Odszedł + bym.", "Odszedł + bym.")),
]
D[17] = ("Pomyśl o decyzji z przeszłości (50+ słów). Jak wyglądałoby twoje życie teraz, gdybyś zdecydował(a) inaczej?", 50,
 ("Gdybym wtedy nie…, teraz byłbym… Gdybym był bardziej…, …", "Gdybym wtedy nie…, teraz byłbym… Gdybym był bardziej…, …", "Gdybym wtedy nie…, teraz byłbym… Gdybym był bardziej…, …"))

# ---- Łuk 4
T[19] = ("Розділові питання: prawda?, nie?, co?", "Pytania rozłączne: prawda?, nie?", "Tags: prawda?, nie?")
G[19] = [
 ("Nie śpisz jeszcze, ____?", ["prawda", "czy", "co nie jest"], 0,
  [("Так! Польська має один хвостик: prawda? / nie?", "Tak! Prawda? / nie?", "Yes! Polish uses one tag: prawda? / nie?"),
   ("Czy — на початку питання.", "„Czy” — na początku.", "Czy goes at the start."),
   ("Ні.", "Nie.", "No.")],
  ("Prawda? — нейтрально; nie? — розмовно.", "Prawda? — neutralnie; nie? — potocznie.", "Prawda? — neutral; nie? — casual.")),
 ("Mama miała rację, ____?", ["nie", "tak nie", "czyż"], 0,
  [("Так! Розмовне «nie?».", "Tak!", "Yes! Casual nie?"),
   ("Ні.", "Nie.", "No."),
   ("Czyż — на початку і книжне.", "Książkowe.", "Bookish, and goes first.")],
  ("Без зміни дієслова, на відміну від англійської.", "Bez zmiany czasownika.", "No auxiliary changes, unlike English.")),
]
D[19] = ("Napisz krótki dialog dwóch przyjaciół (50+ słów). Użyj co najmniej pięciu pytań z „prawda?” lub „nie?”.", 50,
 ("— Będzie słonecznie, prawda? — Tak. Weźmiesz auto, nie?…", "— Będzie słonecznie, prawda? — Tak. Weźmiesz auto, nie?…", "— Będzie słonecznie, prawda? — Tak. Weźmiesz auto, nie?…"))

T[20] = ("Жаль про минуле: powinienem był, mogłem, niepotrzebnie", "Żal: powinienem był, mogłem, niepotrzebnie", "Regret: powinienem był, mogłem, niepotrzebnie")
G[20] = [
 ("____ z nią pojechać.", ["Powinienem był", "Powinienem jestem", "Powinien byłem"], 0,
  [("Так! Powinienem był = should have.", "Tak!", "Yes! Powinienem był = should have."),
   ("Ні.", "Nie.", "No."),
   ("Ні.", "Nie.", "No.")],
  ("Powinienem był + інфінітив.", "Powinienem był + bezokolicznik.", "Powinienem był + infinitive.")),
 ("____ kupiłeś ten bilet.", ["Niepotrzebnie", "Nie trzeba", "Nie musisz"], 0,
  [("Так! = you needn't have bought.", "Tak!", "Yes! = needn't have bought."),
   ("Теперішній зміст.", "Teraźniejsze.", "Present meaning."),
   ("Теперішній зміст.", "Teraźniejsze.", "Present meaning.")],
  ("Niepotrzebnie + минулий = needn't have.", "Niepotrzebnie + przeszły.", "Niepotrzebnie + past = needn't have.")),
]
D[20] = ("Opisz sytuację z przeszłości, którą zrobiłbyś(-abyś) dziś inaczej (50+ słów). Użyj: powinienem był, mogłem, niepotrzebnie.", 50,
 ("Powinienem był… Mogłem… Niepotrzebnie się martwiłem…", "Powinienem był… Mogłem… Niepotrzebnie się martwiłem…", "Powinienem był… Mogłem… Niepotrzebnie się martwiłem…"))

T[21] = ("Майбутнє: będę tańczyć (процес) / zarezerwujemy do (результат)", "Przyszłość: będę tańczyć / zarezerwujemy do", "Future: będę tańczyć / zarezerwujemy do")
G[21] = [
 ("Za rok o tej porze ____ tańczyć na weselu.", ["będziemy", "zatańczymy", "tańczyliśmy"], 0,
  [("Так! Процес → będziemy + недоконаний.", "Tak! Proces.", "Yes! Process → będziemy + imperfective."),
   ("Доконаний — результат, не процес.", "Dokonany — rezultat.", "Perfective = result."),
   ("Минулий.", "Przeszły.", "Past.")],
  ("Will be doing ≈ będę + недоконаний.", "Will be doing ≈ będę + niedokonany.", "Will be doing ≈ będę + imperfective.")),
 ("Do czerwca ____ salę.", ["zarezerwujemy", "będziemy rezerwować", "rezerwujemy"], 0,
  [("Так! Результат до дати → доконаний майбутній.", "Tak! Dokonany.", "Yes! Result by a date → perfective future."),
   ("Процес — ні.", "Proces — nie.", "Not a process."),
   ("Теперішній.", "Teraźniejszy.", "Present.")],
  ("Will have done ≈ do + доконаний майбутній.", "Do + dokonany.", "Will have done ≈ do + perfective future.")),
]
D[21] = ("Wyobraź sobie swoje życie za dziesięć lat (50+ słów). Co będziesz robić? Co zrobisz do tego czasu?", 50,
 ("Za dziesięć lat będę mieszkać… Będę pracować… Do tego czasu zbuduję…", "Za dziesięć lat będę mieszkać… Będę pracować… Do tego czasu zbuduję…", "Za dziesięć lat będę mieszkać… Będę pracować… Do tego czasu zbuduję…"))

T[22] = ("Наголос: To Robin…, Właśnie tego chcę, Tym, czego chcę, jest…", "Akcent: To Robin…, Właśnie…, Tym, czego chcę, jest…", "Emphasis: To Robin…, Właśnie…")
G[22] = [
 ("____ Marshall kupił złe mleko!", ["To", "Co", "Ten"], 0,
  [("Так! To + особа = It was … who.", "Tak!", "Yes! To + person = It was … who."),
   ("Ні.", "Nie.", "No."),
   ("Ні.", "Nie.", "No.")],
  ("To X zrobił… = It was X who…", "To X zrobił…", "To X zrobił… = It was X who…")),
 ("Tym, czego chcę, ____ Robin.", ["jest", "są", "być"], 0,
  [("Так! = What I want is Robin.", "Tak!", "Yes! = What I want is Robin."),
   ("Однина.", "Liczba pojedyncza.", "Singular."),
   ("Ні.", "Nie.", "No.")],
  ("Tym, czego… jest… — орудний + jest.", "Tym, czego… jest…", "Tym, czego… jest… = What… is…")),
]
D[22] = ("Napisz, co jest dla ciebie naprawdę ważne (50+ słów). Użyj: To… zrobił; Właśnie…; Tym, czego chcę, jest…", 50,
 ("Tym, co kocham najbardziej, jest… To moja siostra… Właśnie rano…", "Tym, co kocham najbardziej, jest… To moja siostra… Właśnie rano…", "Tym, co kocham najbardziej, jest… To moja siostra… Właśnie rano…"))

T[23] = ("Протиставлення: chociaż, mimo że, mimo, jednak", "Kontrast: chociaż, mimo że, mimo, jednak", "Contrast: chociaż, mimo że, mimo, jednak")
G[23] = [
 ("____ Ted nie lubi psów, wyprowadza je codziennie.", ["Chociaż", "Mimo", "Jednak"], 0,
  [("Так! Chociaż + речення.", "Tak! Chociaż + zdanie.", "Yes! Chociaż + clause."),
   ("Mimo + родовий.", "Mimo + dopełniacz.", "Mimo + genitive."),
   ("Jednak — у другому реченні.", "„Jednak” — w drugim zdaniu.", "Jednak goes in the second sentence.")],
  ("Chociaż / mimo że + речення · mimo + родовий.", "Chociaż + zdanie · mimo + dopełniacz.", "Chociaż + clause · mimo + genitive.")),
 ("Mimo ____ są razem.", ["różnic", "różnice", "różnicami"], 0,
  [("Так! Mimo + родовий.", "Tak! Dopełniacz.", "Yes! Genitive."),
   ("Називний.", "Mianownik.", "Nominative."),
   ("Орудний.", "Narzędnik.", "Instrumental.")],
  ("Mimo deszczu, mimo wszystko.", "Mimo deszczu.", "Mimo deszczu = despite the rain.")),
]
D[23] = ("Porównaj dwie bardzo różne osoby (50+ słów). Użyj: chociaż, mimo że, mimo, jednak.", 50,
 ("Chociaż mój brat lubi…, ja… Mimo różnic… Jednak…", "Chociaż mój brat lubi…, ja… Mimo różnic… Jednak…", "Chociaż mój brat lubi…, ja… Mimo różnic… Jednak…"))
