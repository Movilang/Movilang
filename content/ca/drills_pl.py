# Trening (6 zdań) — wersja polska „Aut”.
D = {}
def r(q, opts, e):
    p = e.split("|"); p = p if len(p) == 3 else [e, e, e]
    return (q, opts, 0, tuple(p))
D[1] = [r("Ja ____ Zygzak.", ["jestem", "jest", "są"], "Ja → jestem."), r("On ____ szybki.", ["jest", "jestem", "są"], "On → jest."),
        r("My ____ fanami.", ["jesteśmy", "są", "jest"], "My → jesteśmy."), r("Maniek jest ____.", ["ciężarówką", "ciężarówka", "ciężarówki"], "Narzędnik."),
        r("Ty ____ moim przyjacielem.", ["jesteś", "jest", "jestem"], "Ty → jesteś."), r("Oni ____ kierowcami.", ["są", "jest", "jesteśmy"], "Oni → są.")]
D[2] = [r("Nie ____ zmęczony.", ["jestem", "jest", "są"], "Ja → nie jestem."), r("On ____ jest szczęśliwy.", ["nie", "ni", "nic"], "Nie + czasownik."),
        r("____ jesteś gotowy?", ["Czy", "Co", "Kto"], "Czy…?"), r("Czy on ____ gwiazdą?", ["jest", "są", "jestem"], "On → jest."),
        r("Oni nie ____ tutaj.", ["są", "jest", "jesteś"], "Oni → są."), r("Czy ____ spóźniony?", ["jestem", "są", "jest się"], "Ja → jestem.")]
D[3] = [r("To jest ____ przyczepa.", ["moja", "mój", "moje"], "Żeński → moja."), r("To ____ samochód.", ["mój", "moja", "moje"], "Męski → mój."),
        r("To jest auto ____.", ["Zygzaka", "Zygzak", "Zygzakiem"], "Dopełniacz."), r("Czy to ____ puchar?", ["twój", "twoja", "twoje"], "Męski → twój."),
        r("Sally kocha ____ motel.", ["swój", "swoja", "swoje"], "Swój (męski)."), r("Doc i ____ garaż.", ["jego", "jej", "mój"], "On → jego.")]
D[4] = [r("____ auto jest czerwone.", ["To", "Ten", "Ta"], "Nijaki → to."), r("____ opony są nowe.", ["Te", "Ten", "Ta"], "L. mnoga → te."),
        r("____ góra jest daleko.", ["Ta", "Ten", "To"], "Żeński → ta."), r("Patrz na ____ gwiazdy!", ["te", "ten", "ta"], "L. mnoga → te."),
        r("Dwa ____.", ["auta", "auto", "aut"], "2–4 → auta."), r("Trzy ____.", ["opony", "opona", "opon"], "2–4 → opony.")]
D[5] = [r("Ja ____ sponsora.", ["mam", "ma", "mają"], "Ja → mam."), r("On ____ przyczepę.", ["ma", "mam", "masz"], "On → ma."),
        r("Ona nie ma ____.", ["auta", "auto", "autem"], "Nie ma + dopełniacz."), r("Czy ____ przyjaciela?", ["masz", "ma", "mam"], "Ty → masz."),
        r("My ____ fanów.", ["mamy", "mają", "macie"], "My → mamy."), r("Oni nie ____ pieniędzy.", ["mają", "ma", "mamy"], "Oni → mają.")]
D[7] = [r("Tu ____ kawiarnia.", ["jest", "są", "ma"], "Jedna → jest."), r("Tu ____ dwa sklepy.", ["są", "jest", "jestem"], "Kilka → są."),
        r("Nie ma ____.", ["hotelu", "hotel", "hotelem"], "Nie ma + dopełniacz."), r("Czy jest tu ____?", ["droga", "drogi", "drogą"], "Mianownik."),
        r("Nie ma tu ____.", ["aut", "auta", "auto"], "Dopełniacz l. mn."), r("Czy są tu ____?", ["turyści", "turystów", "turysta"], "Mianownik l. mn.")]
D[8] = [r("Auto jest ____ garażu.", ["w", "na", "pod"], "W garażu."), r("Pachołek jest ____ drodze.", ["na", "w", "pod"], "Na drodze."),
        r("Złomek śpi pod ____.", ["znakiem", "znak", "znaku"], "Pod + narzędnik."), r("Kawiarnia jest obok ____.", ["motelu", "motel", "motelem"], "Obok + dopełniacz."),
        r("Garaż jest ____ sądem.", ["za", "zza", "przy za"], "Za + narzędnik."), r("Miasteczko jest ____ górami.", ["między", "mięczy", "przy między"], "Między.")]
D[9] = [r("____ auto!", ["Zatrzymaj", "Zatrzymuje", "Zatrzymać"], "Rozkaz."), r("Nie ____ tak szybko!", ["jedź", "jedzie", "jechać"], "Nie + rozkaz."),
        r("____!", ["Jedźmy", "Jedziemy by", "Jechać my"], "Jedźmy = let's go."), r("Proszę, ____ wolniej.", ["jedź", "jedzie", "jadę"], "Rozkaz."),
        r("Nie ____!", ["krzycz", "krzyczy", "krzyczeć"], "Rozkaz."), r("Naprawmy ____!", ["drogę", "droga", "drogą"], "Biernik.")]
D[10] = [r("Złomek ____ jeździć do tyłu.", ["umie", "umiem", "umieją"], "On → umie."), r("Nie ____ ciągnąć Bessie.", ["mogę", "może", "mogą"], "Ja → mogę."),
         r("Czy ____ mi pomóc?", ["możesz", "może", "mogę"], "Ty → możesz."), r("On nie ____ pływać.", ["umie", "umiem", "umieć"], "On → umie."),
         r("Ona umie dobrze ____.", ["jeździć", "jeździ", "jeżdżę"], "Bezokolicznik."), r("Czy oni ____ się ścigać?", ["mogą", "może", "mogę"], "Oni → mogą.")]
D[11] = [r("Złomek ____ na złomowisku.", ["mieszka", "mieszkam", "mieszkają"], "On → mieszka."), r("Codziennie ____ auta.", ["holuję", "holuje", "holują"], "Ja → holuję."),
         r("Flo ____ paliwo.", ["sprzedaje", "sprzedaję", "sprzedają"], "Ona → sprzedaje."), r("Oni ____ w miasteczku.", ["pracują", "pracuje", "pracuję"], "Oni → pracują."),
         r("Doc ____ na miasto.", ["patrzy", "patrzę", "patrzą"], "On → patrzy."), r("On dużo ____.", ["mówi", "mówię", "mówią"], "On → mówi.")]
D[13] = [r("Czy ____ mój motel?", ["lubisz", "lubi", "lubię"], "Ty → lubisz."), r("Czy Doc ____ wyścigi?", ["lubi", "lubisz", "lubią"], "On → lubi."),
         r("On tu nie ____.", ["mieszka", "mieszkam", "mieszkać"], "On → mieszka."), r("Nie ____ czekać.", ["lubię", "lubi", "lubią"], "Ja → lubię."),
         r("Czy ona ____ auto?", ["ma", "mam", "mają"], "Ona → ma."), r("Oni nie ____.", ["wiedzą", "wie", "wiem"], "Oni → wiedzą.")]
D[14] = [r("Sierżant ____ wstaje wcześnie.", ["zawsze", "nigdy", "wczoraj"], "Zawsze."), r("Flo jest ____ zajęta.", ["często", "częsty", "czasy"], "Często."),
         r("Nigdy ____ piję kawy.", ["nie", "ni", "nic"], "Nigdy nie…"), r("On ____ się spóźnia.", ["nigdy nie", "nigdy", "nie nigdy"], "Nigdy nie…"),
         r("____ gramy.", ["Czasem", "Czasy", "Czas"], "Czasem."), r("Red ____ płacze.", ["często", "częściej nie", "nigdy"], "Często.")]
D[15] = [r("____ jest Doc?", ["Gdzie", "Kto", "Kiedy"], "Miejsce → gdzie."), r("____ to jest?", ["Kto", "Gdzie", "Jak"], "Osoba → kto."),
         r("____ się ścigasz?", ["Dlaczego", "Kto", "Który"], "Przyczyna → dlaczego."), r("____ jest wyścig?", ["Kiedy", "Kto", "Co"], "Czas → kiedy."),
         r("____ się masz?", ["Jak", "Co", "Kto"], "Jak się masz?"), r("____ masz na imię?", ["Jak", "Co", "Gdzie"], "Jak masz na imię?")]
D[16] = [r("Złomek lubi ____ do tyłu.", ["jeździć", "jeździ", "jeżdżę"], "Lubić + bezokolicznik."), r("Nie znoszę ____.", ["czekać", "czekam", "czeka"], "Bezokolicznik."),
         r("Ona lubi ____ auta.", ["naprawiać", "naprawia", "naprawiam"], "Bezokolicznik."), r("Czy lubisz ____?", ["się ścigać", "ścigasz się", "ściga"], "Bezokolicznik."),
         r("On nie lubi ____.", ["biegać", "biega", "biegam"], "Bezokolicznik."), r("Uwielbiamy ____.", ["tańczyć", "tańczymy", "tańczy"], "Bezokolicznik.")]
D[17] = [r("Teraz Zygzak ____ drogę.", ["naprawia", "naprawiał", "naprawiać"], "Teraz → teraźniejszy."), r("Ja teraz ____.", ["pracuję", "pracuje", "pracował"], "Ja → pracuję."),
         r("Oni się ____.", ["śmieją", "śmieje", "śmieję"], "Oni → śmieją."), r("Czy ty ____?", ["słuchasz", "słucha", "słucham"], "Ty → słuchasz."),
         r("Ona nie ____.", ["śpi", "śpię", "spać"], "Ona → śpi."), r("Patrz! On ____!", ["jedzie", "jadę", "jechać"], "On → jedzie.")]
D[19] = [r("Doc ____ codziennie w garażu.", ["pracuje", "pracował", "pracować"], "Codziennie → teraźniejszy."), r("Patrz! Doc teraz ____!", ["jedzie", "jechał", "jechać"], "Teraz."),
         r("Zwykle ____ herbatę.", ["piję", "pije", "pić"], "Ja → piję."), r("Słuchaj! Ona ____.", ["śpiewa", "śpiewam", "śpiewała"], "Ona → śpiewa."),
         r("Oni teraz ____ telewizję.", ["oglądają", "ogląda", "oglądał"], "Oni → oglądają."), r("On często się ____.", ["spóźnia", "spóźniam", "spóźniał"], "On → spóźnia.")]
D[20] = [r("Chcę trochę ____.", ["wody", "woda", "wodą"], "Trochę + dopełniacz."), r("Jest trochę ____.", ["paliwa", "paliwo", "paliwem"], "Dopełniacz."),
         r("Czy jest jakiś ____?", ["olej", "oleju", "olejem"], "Mianownik."), r("Nie mam żadnych ____.", ["opon", "opony", "opona"], "Dopełniacz l. mn."),
         r("Mam kilka ____.", ["aut", "auta", "auto"], "Kilka + dopełniacz."), r("Chcesz trochę ____?", ["chleba", "chleb", "chlebem"], "Dopełniacz.")]
D[21] = [r("Ile ____?", ["opon", "opony", "opona"], "Ile + dopełniacz."), r("Ile ____?", ["paliwa", "paliwo", "paliwem"], "Ile + dopełniacz."),
         r("Ile to ____?", ["kosztuje", "kosztują", "koszt"], "Ile to kosztuje?"), r("Mam pięć ____.", ["opon", "opony", "opona"], "5+ → dopełniacz l. mn."),
         r("Mam dwie ____.", ["opony", "opon", "opona"], "2–4 → mianownik l. mn."), r("Jest tu wiele ____.", ["sklepów", "sklepy", "sklep"], "Wiele + dopełniacz.")]
D[22] = [r("Sally lubi ____.", ["go", "on", "jego"], "Biernik → go."), r("Widzę ____.", ["cię", "ty", "twój"], "Biernik → cię."),
         r("Zadzwoń do ____!", ["mnie", "ja", "mój"], "Do + mnie."), r("On ____ kocha.", ["ją", "ona", "jej"], "Biernik → ją."),
         r("Pomóż ____!", ["nam", "my", "nasz"], "Pomóc + celownik."), r("Znam ____.", ["ich", "oni", "ichni"], "Biernik → ich.")]
D[23] = [r("Wyścig jest ____ niedzielę.", ["w", "o", "na"], "Dni → w."), r("Wstaję ____ siódmej.", ["o", "w", "na"], "Godzina → o."),
         r("Jest gorąco ____ lipcu.", ["w", "o", "na"], "Miesiące → w."), r("____ rano.", ["Rano", "W rano", "O rano"], "Rano."),
         r("____ nocy.", ["W", "O", "Na"], "W nocy."), r("____ weekend.", ["W", "O", "Na w"], "W weekend.")]
D[25] = [r("Doc ____ mistrzem.", ["był", "była", "byli"], "On → był."), r("Fani ____ wszędzie.", ["byli", "był", "była"], "Oni → byli."),
         r("Ja (Doc) ____ w szpitalu.", ["byłem", "byłam", "był"], "Ja (m.) → byłem."), r("To nie ____ sprawiedliwe.", ["było", "był", "była"], "To → było."),
         r("Czy ____ zaskoczony?", ["byłeś", "byłem", "był"], "Ty (m.) → byłeś."), r("My ____ zmęczeni.", ["byliśmy", "byli", "był"], "My → byliśmy.")]
D[26] = [r("On ____ całą noc.", ["pracował", "pracuje", "pracowała"], "On → -ł."), r("Ja ____ pracę.", ["skończyłem", "skończył", "kończę"], "Ja (m.) → -łem."),
         r("Ona się ____.", ["uśmiechnęła", "uśmiechnął", "uśmiecha"], "Ona → -ła."), r("Oni ____ z radości.", ["skakali", "skakał", "skaczą"], "Oni → -li."),
         r("On nie ____.", ["spał", "śpi", "spała"], "On → spał."), r("My ____ miasteczko.", ["odwiedziliśmy", "odwiedził", "odwiedzamy"], "My → -liśmy.")]
D[27] = [r("On ____ do każdego sklepu.", ["pojechał", "pojedzie", "jedzie"], "Przeszłość."), r("Ja ____ paliwo.", ["kupiłem", "kupię", "kupuję"], "Przeszłość."),
         r("Ona ____ światła.", ["zobaczyła", "zobaczył", "zobaczy"], "Ona → -ła."), r("On ____ niespodziankę.", ["zrobił", "zrobi", "robi"], "Przeszłość."),
         r("Ramone ____ mu lakier.", ["dał", "da", "daje"], "Przeszłość."), r("Świetnie się ____.", ["bawiliśmy", "bawimy", "bawił"], "My → -liśmy.")]
D[28] = [r("Czy ____ do nich?", ["zadzwoniłeś", "zadzwonisz", "dzwonisz"], "Przeszłość."), r("On nie ____ do widzenia.", ["powiedział", "powie", "mówi"], "Przeszłość."),
         r("Czy ona ____ wiadomości?", ["widziała", "widzi", "zobaczy"], "Przeszłość."), r("Tak, ____.", ["zadzwoniłem", "zadzwonię", "dzwonię"], "Przeszłość."),
         r("Nie ____.", ["wiedziałem", "wiem", "wiedzieć"], "Przeszłość."), r("Czy oni go ____?", ["znaleźli", "znajdą", "znajdują"], "Przeszłość.")]
D[29] = [r("____ wrócić. (Zygzak)", ["Chciałbym", "Chciałabym", "Chciałby"], "Ja (m.) → chciałbym."), r("Czy ____ wody? (do Zygzaka)", ["chciałbyś", "chciałbym", "chciałby"], "Ty (m.) → chciałbyś."),
         r("Chcę ____.", ["wygrać", "wygram", "wygrał"], "Chcieć + bezokolicznik."), r("Sally ____ kawę.", ["chciałaby", "chciałbym", "chciałby"], "Ona → chciałaby."),
         r("Czy ____ nowe auto?", ["chcesz", "chce", "chcę"], "Ty → chcesz."), r("On ____ zostać.", ["chciałby", "chciałbym", "chciałaby"], "On → chciałby.")]
D[31] = [r("Stadion jest ____ niż miasteczko.", ["większy", "duży", "największy"], "Duży → większy."), r("Kto jest ____?", ["szybszy", "szybki", "bardziej szybki"], "Szybki → szybszy."),
         r("Król jest bardziej ____.", ["doświadczony", "doświadczeńszy", "doświadczonym"], "Bardziej + przymiotnik."), r("Przyjaciele są ____ niż sława.", ["lepsi", "dobrzejsi", "dobrzy"], "Dobry → lepszy."),
         r("Miasteczko jest ____ niż miasto.", ["cichsze", "ciche", "najcichsze"], "Cichy → cichszy."), r("Jest ____ niż wczoraj.", ["gorzej", "źlej", "złej"], "Źle → gorzej.")]
D[32] = [r("____ ci pomóc.", ["Zamierzamy", "Zamierza", "Zamierzają"], "My → zamierzamy."), r("On ____ wymienić opony.", ["zamierza", "zamierzam", "zamierzają"], "On → zamierza."),
         r("Zamierzam ____.", ["wygrać", "wygram", "wygrał"], "Bezokolicznik."), r("Czy będzie ____?", ["padać", "pada", "padał"], "Będzie + bezokolicznik."),
         r("Oni nie ____ przegrać.", ["zamierzają", "zamierza", "zamierzam"], "Oni → zamierzają."), r("Czy ____ się ścigać?", ["będziesz", "będę", "będzie"], "Ty → będziesz.")]
D[33] = [r("Zatrzymałem się, ____ się rozbił.", ["bo", "więc", "ale"], "Przyczyna → bo."), r("Był zły, ____ popchnął.", ["więc", "bo", "ale"], "Skutek → więc."),
         r("Wygrał, ____ nikt nie klaskał.", ["ale", "więc", "bo"], "Kontrast → ale."), r("Byłem zmęczony, ____ spałem.", ["więc", "ale", "bo"], "Skutek → więc."),
         r("Lubię herbatę ____ kawę.", ["i", "więc", "bo"], "Dodawanie → i."), r("Uśmiechnęła się, ____ była szczęśliwa.", ["bo", "więc", "ale"], "Przyczyna → bo.")]
D[34] = [r("____ wstań.", ["Najpierw", "W końcu", "Następnie potem"], "Początek → najpierw."), r("____ zjedz śniadanie.", ["Potem", "Najpierw w końcu", "W końcu najpierw"], "Dalej → potem."),
         r("____ idź do szkoły.", ["Następnie", "Najpierw w końcu", "Bo"], "Następnie."), r("____ idź spać.", ["W końcu", "Najpierw", "Bo"], "Koniec → w końcu."),
         r("Najpierw wyścig, ____ impreza.", ["potem", "najpierw", "bo"], "Potem."), r("____ powiedz dziękuję.", ["Najpierw", "W końcu bo", "Więc najpierw"], "Najpierw.")]
