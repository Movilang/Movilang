# Trening gramatyczny (6 zdań) — wersja polska.
D = {}
D[1] = [
 ("Kevin ____ najmłodszy.", ["jest", "są", "jestem"], 0, ("Він → jest.", "On → jest.", "He → jest.")),
 ("My ____ dużą rodziną.", ["jesteśmy", "są", "jest"], 0, ("Ми → jesteśmy.", "My → jesteśmy.", "We → jesteśmy.")),
 ("Buzz ____ pająka.", ["ma", "mam", "mają"], 0, ("Він → ma.", "On → ma.", "He → ma.")),
 ("Ja ____ dwóch kuzynów.", ["mam", "ma", "mamy"], 0, ("Я → mam.", "Ja → mam.", "I → mam.")),
 ("Bilety ____ na stole.", ["są", "jest", "jestem"], 0, ("Множина → są.", "Liczba mnoga → są.", "Plural → są.")),
 ("Czy ____ paszport?", ["masz", "ma", "mam"], 0, ("Ти → masz.", "Ty → masz.", "You → masz.")),
]
D[2] = [
 ("Kevin ____ pizzę z serem.", ["lubi", "lubię", "lubią"], 0, ("Він → lubi.", "On → lubi.", "He → lubi.")),
 ("Buzz nie ____ Kevina.", ["lubi", "lubią", "lubisz"], 0, ("Він → lubi.", "On → lubi.", "He → lubi.")),
 ("Czy ty ____ ryby?", ["lubisz", "lubi", "lubię"], 0, ("Ти → lubisz.", "Ty → lubisz.", "You → lubisz.")),
 ("Kuzyni ____ dużo napojów.", ["piją", "pije", "piję"], 0, ("Вони → piją.", "Oni → piją.", "They → piją.")),
 ("Mama ____ kolację o siódmej.", ["robi", "robię", "robią"], 0, ("Вона → robi.", "Ona → robi.", "She → robi.")),
 ("Ja nie ____ pizzy z rybą.", ["jem", "je", "jedzą"], 0, ("Я → jem.", "Ja → jem.", "I → jem.")),
]
D[3] = [
 ("W pokoju ____ lampa.", ["jest", "są", "jesteś"], 0, ("Однина → jest.", "L. poj. → jest.", "Singular → jest.")),
 ("W pokoju ____ dwa okna.", ["są", "jest", "jestem"], 0, ("Множина → są.", "L. mn. → są.", "Plural → są.")),
 ("Czy pod łóżkiem ____ potwór?", ["jest", "są", "ma"], 0, ("Jest.", "Jest.", "Jest.")),
 ("Piwnica jest pod ____.", ["domem", "dom", "domu"], 0, ("Pod + орудний.", "Pod + narzędnik.", "Pod + instrumental.")),
 ("Bus stoi przed ____.", ["domem", "dom", "domy"], 0, ("Przed + орудний.", "Przed + narzędnik.", "Przed + instrumental.")),
 ("Na strychu nie ma ____.", ["światła", "światło", "światłem"], 0, ("Nie ma + родовий.", "Nie ma + dopełniacz.", "Nie ma + genitive.")),
]
D[4] = [
 ("Burza ____ straszna.", ["była", "był", "byli"], 0, ("Жін. рід → była.", "R. ż. → była.", "Feminine → była.")),
 ("My ____ spóźnieni.", ["byliśmy", "byli", "była"], 0, ("Ми → byliśmy.", "My → byliśmy.", "We → byliśmy.")),
 ("Światła nie ____ włączone.", ["były", "byli", "był"], 0, ("Речі → były.", "Rzeczy → były.", "Things → były.")),
 ("Czy Kevin ____ w busie?", ["był", "była", "było"], 0, ("Він → był.", "On → był.", "He → był.")),
 ("Ja ____ na trzecim piętrze.", ["byłem", "był", "byli"], 0, ("Я (чол.) → byłem.", "Ja (m.) → byłem.", "I (m.) → byłem.")),
 ("Już ____ dziewiąta!", ["była", "był", "byli"], 0, ("Godzina → była.", "Godzina → była.", "Godzina → była.")),
]
D[5] = [
 ("____ za mną, dzieci!", ["Chodźcie", "Chodzić", "Chodzą"], 0, ("Ви → chodźcie.", "Wy → chodźcie.", "You (pl.) → chodźcie.")),
 ("Nie ____ paszportu!", ["zapomnij", "zapominać", "zapomina"], 0, ("Ти → zapomnij.", "Ty → zapomnij.", "You → zapomnij.")),
 ("Proszę ____.", ["usiąść", "usiądź", "siedzą"], 0, ("Proszę + інфінітив.", "Proszę + bezokolicznik.", "Proszę + infinitive.")),
 ("____ pasy!", ["Zapnijcie", "Zapinać", "Zapinają"], 0, ("Ви → zapnijcie.", "Wy → zapnijcie.", "You (pl.) → zapnijcie.")),
 ("Nie ____ na lotnisku!", ["krzycz", "krzyczeć", "krzyczy"], 0, ("Nie + наказ.", "Nie + rozkaz.", "Nie + imperative.")),
 ("____ dzieci przed wyjazdem!", ["Policz", "Liczyć", "Liczy"], 0, ("Ти → policz.", "Ty → policz.", "You → policz.")),
]
D[7] = [
 ("Kevin ____ rodziny.", ["szukał", "szukała", "szukali"], 0, ("Він → -ł.", "On → -ł.", "He → -ł.")),
 ("Ja ____ mamę.", ["wołałem", "wołał", "wołali"], 0, ("Я (ч.) → -łem.", "Ja (m.) → -łem.", "I (m.) → -łem.")),
 ("Kevin ____ na łóżku.", ["skakał", "skakała", "skakali"], 0, ("Він → -ł.", "On → -ł.", "He → -ł.")),
 ("Czekał ____ godzinę.", ["przez", "od", "na"], 0, ("Przez godzinę.", "Przez godzinę.", "Przez godzinę.")),
 ("Nikt nie ____.", ["odpowiedział", "odpowiedzieli", "odpowiedziała"], 0, ("Nikt → він.", "Nikt → on.", "Nikt takes the he form.")),
 ("Kevin nikogo nie ____.", ["zobaczył", "zobaczyła", "zobaczyli"], 0, ("Він → -ł.", "On → -ł.", "He → -ł.")),
]
D[8] = [
 ("Kevin ____ jeść lody.", ["może", "mogę", "mogą"], 0, ("Він → może.", "On → może.", "He → może.")),
 ("Nie ____ znaleźć pilota!", ["mogę", "może", "mogą"], 0, ("Я → mogę.", "Ja → mogę.", "I → mogę.")),
 ("Czy ____ obejrzeć ten film?", ["mogę", "umiem", "muszę"], 0, ("Дозвіл → mogę.", "Pozwolenie → mogę.", "Permission → mogę.")),
 ("Kevinowi nie ____ skakać po łóżku.", ["wolno", "może", "umie"], 0, ("Wolno.", "Wolno.", "Wolno.")),
 ("Kevin ____ jeździć na sankach.", ["umie", "wolno", "może być"], 0, ("Навичка → umie.", "Umiejętność → umie.", "Skill → umie.")),
 ("Nie ____ mnie zatrzymać!", ["możecie", "może", "mogę"], 0, ("Ви → możecie.", "Wy → możecie.", "You (pl.) → możecie.")),
]
D[9] = [
 ("To pokój ____.", ["Buzza", "Buzz", "Buzzowi"], 0, ("Родовий: Buzza.", "Dopełniacz: Buzza.", "Genitive: Buzza.")),
 ("Czyj to ____?", ["pająk", "pająka", "pająkiem"], 0, ("Називний.", "Mianownik.", "Nominative.")),
 ("To są ____ pieniądze.", ["jego", "go", "on"], 0, ("Jego — його.", "Jego.", "Jego = his.")),
 ("Kevin się ____ nie boi.", ["go", "jego", "on"], 0, ("Об'єкт: go.", "Dopełnienie: go.", "Object: go.")),
 ("Ten pokój jest teraz ____!", ["mój", "moja", "moje"], 0, ("Pokój → mój.", "Pokój → mój.", "Pokój → mój.")),
 ("Nie potrzebuję ____!", ["ich", "oni", "im"], 0, ("Родовий: ich.", "Dopełniacz: ich.", "Genitive: ich.")),
]
D[10] = [
 ("Kevin ____ film gangsterski.", ["obejrzał", "obejrzała", "obejrzeli"], 0, ("Він → -ł.", "On → -ł.", "He → -ł.")),
 ("Dostawca ____ pod drzwi.", ["przyszedł", "przyszła", "przyszli"], 0, ("Przyjść → przyszedł.", "Przyjść → przyszedł.", "Przyjść → przyszedł.")),
 ("On ____.", ["uciekł", "uciekła", "uciekli"], 0, ("Uciec → uciekł.", "Uciec → uciekł.", "Uciec → uciekł.")),
 ("Kevin ____ całą pizzę.", ["zjadł", "zjadła", "zjedli"], 0, ("Zjeść → zjadł.", "Zjeść → zjadł.", "Zjeść → zjadł.")),
 ("Dostawca ____, że ktoś strzela.", ["pomyślał", "pomyślała", "pomyśleli"], 0, ("Він → -ł.", "On → -ł.", "He → -ł.")),
 ("Kevin ____ pieniędzmi Buzza.", ["zapłacił", "zapłaciła", "zapłacili"], 0, ("Він → -ł.", "On → -ł.", "He → -ł.")),
]
D[11] = [
 ("____ jest ten człowiek?", ["Kim", "Co", "Gdzie"], 0, ("Kim jest…?", "Kim jest…?", "Kim jest…?")),
 ("____ on mieszka?", ["Gdzie", "Kto", "Co"], 0, ("Місце → gdzie.", "Miejsce → gdzie.", "Place → gdzie.")),
 ("____ mieszka sam?", ["Dlaczego", "Kto", "Który"], 0, ("Причина → dlaczego.", "Przyczyna → dlaczego.", "Reason → dlaczego.")),
 ("____ wychodzi z domu?", ["Kiedy", "Kto", "Co"], 0, ("Час → kiedy.", "Czas → kiedy.", "Time → kiedy.")),
 ("Czego on ____?", ["chce", "chcę", "chcą"], 0, ("Він → chce.", "On → chce.", "He → chce.")),
 ("____ się masz?", ["Jak", "Kto", "Dlaczego"], 0, ("Jak się masz?", "Jak się masz?", "Jak się masz?")),
]
D[13] = [
 ("Patrz! Kevin ____ pod prysznicem.", ["śpiewa", "śpiewam", "śpiewają"], 0, ("Він → śpiewa.", "On → śpiewa.", "He → śpiewa.")),
 ("Teraz ____ zęby.", ["myję", "myje", "myją"], 0, ("Я → myję.", "Ja → myję.", "I → myję.")),
 ("On ____ włosy.", ["czesze", "czeszę", "czeszą"], 0, ("Він → czesze.", "On → czesze.", "He → czesze.")),
 ("Kevin ____ przed lustrem.", ["tańczy", "tańczę", "tańczą"], 0, ("Він → tańczy.", "On → tańczy.", "He → tańczy.")),
 ("Co ____?", ["robisz", "robię", "robi ty"], 0, ("Ти → robisz.", "Ty → robisz.", "You → robisz.")),
 ("On nie ____ płaszcza.", ["ma", "mam", "mają"], 0, ("Він → ma.", "On → ma.", "He → ma.")),
]
D[14] = [
 ("Ile ____ mam?", ["pieniędzy", "pieniądze", "pieniądzom"], 0, ("Ile + родовий.", "Ile + dopełniacz.", "Ile + genitive.")),
 ("Ile ____ potrzebujemy?", ["jajek", "jajka", "jajkami"], 0, ("Ile + родовий.", "Ile + dopełniacz.", "Ile + genitive.")),
 ("Potrzebuję trochę ____.", ["chleba", "chleb", "chlebem"], 0, ("Trochę + родовий.", "Trochę + dopełniacz.", "Trochę + genitive.")),
 ("Nie ma ____.", ["mleka", "mleko", "mlekiem"], 0, ("Nie ma + родовий.", "Nie ma + dopełniacz.", "Nie ma + genitive.")),
 ("Czy jest ____ sok?", ["jakiś", "jakaś", "jakieś"], 0, ("Sok — ч.р.", "Sok — r. męski.", "Sok is masculine.")),
 ("Ile to ____?", ["kosztuje", "kosztuję", "kosztują"], 0, ("To → kosztuje.", "To → kosztuje.", "It → kosztuje.")),
]
D[15] = [
 ("____ zapłaciłeś?", ["Czy", "Co", "Kto"], 0, ("Так/ні → czy.", "Tak/nie → czy.", "Yes/no → czy.")),
 ("Gdzie on ____?", ["poszedł", "poszła", "poszli"], 0, ("Він → poszedł.", "On → poszedł.", "He → poszedł.")),
 ("Co ____? (ty, m.)", ["kupiłeś", "kupiłem", "kupił"], 0, ("Ти → -łeś.", "Ty → -łeś.", "You → -łeś.")),
 ("Czy ktoś mnie ____?", ["widział", "widziałem", "widzieli"], 0, ("Ktoś → він.", "Ktoś → on.", "Ktoś takes he.")),
 ("Dlaczego ____? (ty, m.)", ["uciekłeś", "uciekłem", "uciekł"], 0, ("Ти → -łeś.", "Ty → -łeś.", "You → -łeś.")),
 ("Nie, nie ____. (ja, m.)", ["zapłaciłem", "zapłaciłeś", "zapłacił"], 0, ("Я → -łem.", "Ja → -łem.", "I → -łem.")),
]
D[16] = [
 ("Choinka jest ____ od Kevina.", ["wyższa", "wysoka", "najwyższa"], 0, ("Вищий ступінь.", "Stopień wyższy.", "Comparative.")),
 ("Ta jest ____ niż tamta.", ["tańsza", "tania", "najtańsza"], 0, ("Tani → tańszy.", "Tani → tańszy.", "Tani → tańszy.")),
 ("Choinka jest ____ niż torby.", ["cięższa", "ciężka", "najcięższa"], 0, ("Ciężki → cięższy.", "Ciężki → cięższy.", "Ciężki → cięższy.")),
 ("Teraz jest ____.", ["piękniejsza", "piękna", "najpiękniej"], 0, ("Вищий ступінь.", "Stopień wyższy.", "Comparative.")),
 ("Ta choinka jest ____.", ["lepsza", "dobrsza", "dobra niż"], 0, ("Dobry → lepszy.", "Dobry → lepszy.", "Dobry → lepszy.")),
 ("Większa ____ mnie!", ["ode", "niż od", "z"], 0, ("Od(e) + родовий.", "Od(e) + dopełniacz.", "Od(e) + genitive.")),
]
D[17] = [
 ("To ____ kolacja!", ["najlepsza", "lepsza", "dobra"], 0, ("Najlepszy.", "Najlepszy.", "Najlepszy.")),
 ("To ____ szklanka.", ["największa", "większa", "duża"], 0, ("Największy.", "Największy.", "Największy.")),
 ("Rodzina jest ____.", ["najważniejsza", "ważniejsza", "ważna niż"], 0, ("Naj-.", "Naj-.", "Naj-.")),
 ("To ____ pokój.", ["najprzytulniejszy", "przytulniejszy", "przytulny niż"], 0, ("Naj-.", "Naj-.", "Naj-.")),
 ("____ jest cisza.", ["Najgorsza", "Gorsza", "Zła"], 0, ("Zły → najgorszy.", "Zły → najgorszy.", "Zły → najgorszy.")),
 ("Najlepsza na ____.", ["świecie", "świat", "świata"], 0, ("Na + місцевий.", "Na + miejscownik.", "Na + locative.")),
]
D[19] = [
 ("Jutro ____ padać śnieg.", ["będzie", "będę", "będą"], 0, ("Śnieg → będzie.", "Śnieg → będzie.", "Śnieg → będzie.")),
 ("Bandyci ____ obserwować dom.", ["będą", "będzie", "będziemy"], 0, ("Oni → będą.", "Oni → będą.", "Oni → będą.")),
 ("Ja ____ czekać.", ["będę", "będzie", "będziesz"], 0, ("Ja → będę.", "Ja → będę.", "Ja → będę.")),
 ("Co ____ robić wieczorem, Kevin?", ["będziesz", "będę", "będzie"], 0, ("Ty → będziesz.", "Ty → będziesz.", "Ty → będziesz.")),
 ("My ____ oglądać film.", ["będziemy", "będą", "będę"], 0, ("My → będziemy.", "My → będziemy.", "My → będziemy.")),
 ("Kevin będzie ____ domu.", ["pilnować", "pilnuje", "pilnowali"], 0, ("Będzie + інфінітив.", "Będzie + bezokolicznik.", "Będzie + infinitive.")),
]
D[20] = [
 ("Kevin ____ to zrobić sam.", ["musi", "muszę", "musisz"], 0, ("On → musi.", "On → musi.", "On → musi.")),
 ("Ja ____ włączyć światło.", ["muszę", "musi", "musimy"], 0, ("Ja → muszę.", "Ja → muszę.", "Ja → muszę.")),
 ("Tu ____ wyłączać muzyki!", ["nie wolno", "nie wolna", "nie wolni"], 0, ("Nie wolno + інфінітив.", "Nie wolno + bezokolicznik.", "Nie wolno + infinitive.")),
 ("My ____ udawać.", ["musimy", "muszą", "muszę"], 0, ("My → musimy.", "My → musimy.", "My → musimy.")),
 ("Bandyci ____ uwierzyć.", ["muszą", "musi", "musimy"], 0, ("Oni → muszą.", "Oni → muszą.", "Oni → muszą.")),
 ("Trzeba ____ manekiny.", ["przesunąć", "przesuwa", "przesunął"], 0, ("Trzeba + інфінітив.", "Trzeba + bezokolicznik.", "Trzeba + infinitive.")),
]
D[21] = [
 ("Kiedy Harry ____ biżuterii, Marv odkręcał kran.", ["szukał", "znalazł", "szuka"], 0, ("Фон → недоконаний.", "Tło → niedokonany.", "Background → imperfective.")),
 ("Nagle Kevin ____ światło.", ["zobaczył", "widywał", "widzi"], 0, ("Nagle → доконаний.", "Nagle → dokonany.", "Nagle → perfective.")),
 ("Woda ____ przez całą noc.", ["leciała", "poleciała", "poleci"], 0, ("Całą noc → процес.", "Całą noc → proces.", "All night → a process.")),
 ("Marv ____ kran i wyszedł.", ["odkręcił", "odkręcał", "odkręca"], 0, ("Дві послідовні події.", "Dwa wydarzenia po kolei.", "Two events in a row.")),
 ("Kiedy oni kradli, Kevin ____.", ["patrzył", "popatrzy", "patrzy"], 0, ("Дві тривалі дії.", "Dwie czynności trwające.", "Two ongoing actions.")),
 ("Bandyci ____ przez płot i uciekli.", ["przeszli", "przechodzili", "przechodzą"], 0, ("Події по черзі.", "Wydarzenia po kolei.", "Events in order.")),
]
D[22] = [
 ("Marley nigdy ____ nie widział.", ["jej", "ją", "ona"], 0, ("Після заперечення — родовий: jej.", "Po przeczeniu — dopełniacz: jej.", "After a negative — genitive: jej.")),
 ("Czy ____ byłeś w kościele w nocy?", ["kiedyś", "nigdy", "nic"], 0, ("Питання → kiedyś.", "Pytanie → kiedyś.", "Question → kiedyś.")),
 ("Ja nigdy nie ____ w Paryżu.", ["byłem", "był", "byli"], 0, ("Ja → byłem.", "Ja → byłem.", "Ja → byłem.")),
 ("Marley nigdy nie ____ z synem.", ["rozmawia", "rozmawiam", "rozmawiasz"], 0, ("On → rozmawia.", "On → rozmawia.", "On → rozmawia.")),
 ("Kevin nigdy ____ nie spotkał.", ["go", "on", "jego"], 0, ("Nigdy go nie…", "Nigdy go nie…", "Nigdy go nie…")),
 ("Czy kiedyś ____ kolędy?", ["śpiewałeś", "śpiewany", "śpiewać"], 0, ("Ty → śpiewałeś.", "Ty → śpiewałeś.", "Ty → śpiewałeś.")),
]
D[23] = [
 ("Nie ____! To mój dom!", ["ucieknę", "uciekam", "uciekłem"], 0, ("Майбутнє: ucieknę.", "Przyszłość: ucieknę.", "Future: ucieknę.")),
 ("Obronię ____ dom.", ["swój", "swoja", "swoje"], 0, ("Dom — чол. рід: swój.", "Dom — r. męski: swój.", "Dom is masculine: swój.")),
 ("Obiecuję, że ____ odważny.", ["będę", "byłem", "jestem"], 0, ("Обіцянка → майбутнє.", "Obietnica → przyszłość.", "Promise → future.")),
 ("Bandyci ____ o dziewiątej.", ["przyjdą", "przyszli", "przyszedł"], 0, ("Майбутнє: przyjdą.", "Przyszłość: przyjdą.", "Future: przyjdą.")),
 ("Jutro ____ do mamy.", ["zadzwonię", "dzwoniłem", "zadzwonił"], 0, ("Я + майбутнє.", "Ja + przyszłość.", "I + future.")),
 ("Kevin nie ____ się.", ["podda", "poddałem", "poddadzą"], 0, ("Він → podda.", "On → podda.", "He → podda.")),
]
