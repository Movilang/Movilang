# Trening gramatyczny (6 zdań) — wersja dla uczących się polskiego. Poprawna odpowiedź pierwsza.
D = {}
def x(q, o, e): return (q, o, 0, e)
U = lambda uk, pl, en: (uk, pl, en)

D[1] = [
 x("Harry codziennie ____ śniadanie.", ["robi", "robię", "robią"], U("Він → robi.", "On → robi.", "He → robi.")),
 x("Ja ____ w komórce pod schodami.", ["śpię", "śpi", "śpią"], U("Я → śpię.", "Ja → śpię.", "I → śpię.")),
 x("Ty zawsze ____ o prezenty!", ["prosisz", "prosi", "proszę"], U("Ти → prosisz.", "Ty → prosisz.", "You → prosisz.")),
 x("Dursleyowie ____ magii.", ["nienawidzą", "nienawidzi", "nienawidzę"], U("Вони → -ą.", "Oni → -ą.", "They → -ą.")),
 x("My ____ do zoo.", ["jedziemy", "jadą", "jedzie"], U("Ми → jedziemy.", "My → jedziemy.", "We → jedziemy.")),
 x("Czy wy ____ Harry'ego?", ["znacie", "znają", "znasz"], U("Ви → znacie.", "Wy → znacie.", "You (pl.) → znacie.")),
]
D[2] = [
 x("Petunia ____ bardzo zdenerwowana.", ["była", "był", "było"], U("Жін. → była.", "Ż. → była.", "Fem. → była.")),
 x("Dudley ____ do terrarium.", ["wpadł", "wpadła", "wpadło"], U("Чол. → -ł.", "M. → -ł.", "Masc. → -ł.")),
 x("Szkło nagle ____.", ["zniknęło", "zniknął", "zniknęła"], U("Сер. → -ło.", "N. → -ło.", "Neuter → -ło.")),
 x("Goście ____ ze strachu.", ["krzyczeli", "krzyczały", "krzyczał"], U("Чоловічоособові → -li.", "Męskoosob. → -li.", "Masc.-personal → -li.")),
 x("Ja (Harry) ____ z wężem.", ["rozmawiałem", "rozmawiałam", "rozmawiał"], U("Я, чол. → -łem.", "Ja, m. → -łem.", "I (male) → -łem.")),
 x("Ty (Petunia) ____ w zoo!", ["byłaś", "byłeś", "była"], U("Ти, жін. → -łaś.", "Ty, ż. → -łaś.", "You (female) → -łaś.")),
]
D[3] = [
 x("Vernon ____ list i spalił go.", ["przeczytał", "czytał", "czyta"], U("Результат.", "Rezultat.", "Result.")),
 x("Sowy codziennie ____ listy.", ["przynosiły", "przyniosły", "przyniesie"], U("Повторення.", "Powtarzanie.", "Repetition.")),
 x("Harry długo ____ list.", ["czytał", "przeczytał", "przeczyta"], U("Процес.", "Proces.", "Process.")),
 x("Wuj ____ wszystkie listy w kominku.", ["spalił", "palił", "pali"], U("Результат.", "Rezultat.", "Result.")),
 x("W nocy Harry ____ tort na podłodze.", ["narysował", "rysował", "rysuje"], U("Один раз.", "Raz.", "Once.")),
 x("Przez całą noc ____ burza.", ["szalała", "rozszalała", "szaleje"], U("Тривалість.", "Trwanie.", "Duration.")),
]
D[4] = [
 x("Harry ____ przyjęty do Hogwartu.", ["został", "zostali", "została"], U("Чол. однина.", "M. lp.", "Masc. sing.")),
 x("Drzwi ____ wyważone.", ["zostały", "został", "zostało"], U("Мн.", "Lm.", "Plural.")),
 x("List ____ napisany zielonym atramentem.", ["był", "była", "byli"], U("Чол.", "M.", "Masc.")),
 x("Rodzice Harry'ego ____ zamordowani.", ["zostali", "zostały", "został"], U("Чоловічоособові.", "Męskoosob.", "Masc.-personal.")),
 x("Tort ____ upieczony przez Hagrida.", ["został", "została", "zostało"], U("Tort — чол.", "Tort — m.", "Tort is masc.")),
 x("Ta szkoła ____ założona dawno temu.", ["została", "został", "zostały"], U("Жін.", "Ż.", "Fem.")),
]
D[6] = [
 x("Gringott jest ____ niż bank mugoli.", ["bezpieczniejszy", "najbezpieczniejszy", "bezpieczny"], U("Niż → вищий.", "Niż → wyższy.", "Niż → comparative.")),
 x("To ____ ulica w Londynie.", ["najdziwniejsza", "dziwniejsza", "dziwna"], U("Найвищий.", "Najwyższy.", "Superlative.")),
 x("Jazda była ____ niż pamiętał Hagrid.", ["gorsza", "złejsza", "najgorsza"], U("Zły → gorszy.", "Zły → gorszy.", "Zły → gorszy.")),
 x("Gobliny są ____ od ludzi.", ["mądrzejsze", "mądre", "najmądrzejsze"], U("Od → вищий.", "Od → wyższy.", "Od → comparative.")),
 x("Skrytka 713 była ____ niż skrytka Harry'ego.", ["mniejsza", "mała", "najmniejsza"], U("Mały → mniejszy.", "Mały → mniejszy.", "Mały → mniejszy.")),
 x("Hogwart to ____ miejsce.", ["najbardziej magiczne", "magiczniejsze", "bardziej magiczne niż"], U("Bardziej / najbardziej.", "Najbardziej.", "Najbardziej + adjective.")),
]
D[7] = [
 x("Harry ma dużo ____.", ["pieniędzy", "pieniądze", "pieniądzach"], U("Родовий.", "Dopełniacz.", "Genitive.")),
 x("Kupił pięć ____.", ["książek", "książki", "książka"], U("5+ → родовий мн.", "5+ → dop. lm.", "5+ → genitive pl.")),
 x("Kupił trzy ____.", ["książki", "książek", "książka"], U("2–4 → називний мн.", "2–4 → mianownik lm.", "2–4 → nominative pl.")),
 x("W sklepie było mało ____.", ["ludzi", "ludzie", "człowiek"], U("Родовий.", "Dopełniacz.", "Genitive.")),
 x("Mamy kilka ____ czasu? Nie — mamy trochę czasu.", ["minut", "minuty", "minuta"], U("Kilka + родовий мн.", "Kilka + dop. lm.", "Kilka + genitive pl.")),
 x("Za dużo ____ na ulicy!", ["czarodziejów", "czarodzieje", "czarodziej"], U("Родовий.", "Dopełniacz.", "Genitive.")),
]
D[8] = [
 x("To różdżka, ____ wybrała Harry'ego.", ["która", "który", "które"], U("Жін.", "Ż.", "Fem.")),
 x("Ollivander to człowiek, ____ sprzedaje różdżki.", ["który", "która", "którego"], U("Чол., підмет.", "M., podmiot.", "Masc. subject.")),
 x("To sklep, w ____ kupił różdżkę.", ["którym", "który", "którego"], U("W + місцевий.", "W + miejscownik.", "W + locative.")),
 x("Feniks, ____ pióro jest w różdżce, należy do Dumbledore'a.", ["którego", "który", "którym"], U("Родовий (чий).", "Dopełniacz.", "Genitive (whose).")),
 x("Pudełka, ____ stały na półkach, były zakurzone.", ["które", "który", "którzy"], U("Мн. неособові.", "Lm. niemęskoos.", "Non-personal plural.")),
 x("Czarodziej, ____ się wszyscy boją, zniknął.", ["którego", "który", "którym"], U("Bać się + родовий.", "Bać się + dopełniacz.", "Bać się + genitive.")),
]
D[9] = [
 x("Jutro Harry ____ do Hogwartu.", ["pojedzie", "jechał", "jeździł"], U("Майбутнє.", "Przyszłość.", "Future.")),
 x("Wieczorem ____ ucztę.", ["będziemy mieć", "mieliśmy", "mamy wczoraj"], U("Будемо + інфінітив.", "Będziemy + bezokol.", "Będziemy + infinitive.")),
 x("Pomogę ci z kufrem! Zaraz go ____.", ["podniosę", "podnosiłem", "podnoszę wczoraj"], U("Доконаний майбутній.", "Przyszły dokonany.", "Perfective future.")),
 x("Pociąg ____ o jedenastej.", ["odjeżdża", "odjechał", "odjeżdżał"], U("Розклад → теперішній.", "Rozkład → teraźniejszy.", "Timetable → present.")),
 x("Myślę, że Harry ____ Hogwart.", ["polubi", "lubił", "polubił"], U("Майбутнє.", "Przyszłość.", "Future.")),
 x("Ron całą drogę ____ jeść słodycze.", ["będzie", "był", "jest"], U("Будуть процес.", "Proces.", "Process.")),
]
D[10] = [
 x("Hermiona ____ być bardzo mądra.", ["musi", "nie może", "chce"], U("Висновок.", "Wniosek.", "Deduction.")),
 x("To ____ być prawdziwe zaklęcie!", ["nie może", "musi", "chce"], U("Точно ні.", "Na pewno nie.", "Certainly not.")),
 x("Ropucha jest ____ gdzieś w pociągu.", ["chyba", "nigdy", "musi"], U("Можливо.", "Możliwe.", "Maybe.")),
 x("Ron ____ jest głodny — nic nie jadł.", ["na pewno", "nie może", "chyba nie"], U("Упевнено.", "Pewnie.", "Surely.")),
 x("Dumbledore ____ być teraz wszędzie.", ["może", "musi", "nie może"], U("Можливо.", "Możliwe.", "Possibly.")),
 x("Parszywek ____ być groźny — tylko śpi.", ["nie może", "musi", "na pewno"], U("Точно ні.", "Na pewno nie.", "Certainly not.")),
]
D[12] = [
 x("Jeśli złamiesz zasady, ____ punkty.", ["stracisz", "traciłeś", "straciłbyś"], U("Jeśli + майбутній.", "Jeśli + przyszły.", "Jeśli + future.")),
 x("Jeśli ____ ciężko, zdasz egzaminy.", ["będziesz pracować", "pracowałeś", "pracowałbyś"], U("Майбутній.", "Przyszły.", "Future.")),
 x("Tiara cię ____, jeśli ją założysz.", ["przydzieli", "przydzielała", "przydzieliła"], U("Майбутній.", "Przyszły.", "Future.")),
 x("Jeśli się ____, McGonagall się zdenerwuje.", ["spóźnisz", "spóźniłeś", "spóźniałbyś"], U("Майбутній.", "Przyszły.", "Future.")),
 x("Jeśli podgrzejesz lód, ____.", ["stopi się", "stopił się", "stopiłby"], U("Загальна істина.", "Prawda ogólna.", "General truth.")),
 x("Jeśli wygramy, ____ puchar.", ["dostaniemy", "dostawaliśmy", "dostalibyśmy"], U("Майбутній.", "Przyszły.", "Future.")),
]
D[13] = [
 x("____ wchodzić do lasu!", ["Nie wolno", "Nie trzeba", "Trzeba"], U("Заборона.", "Zakaz.", "Prohibition.")),
 x("Uczniowie ____ nosić szaty.", ["muszą", "nie muszą", "nie wolno"], U("Обов'язок.", "Obowiązek.", "Obligation.")),
 x("W niedzielę ____ iść na lekcje.", ["nie trzeba", "nie wolno", "trzeba"], U("Не обов'язково.", "Nie trzeba.", "Not necessary.")),
 x("Musisz ____ hasło.", ["podać", "podajesz", "podał"], U("Musieć + інфінітив.", "Musieć + bezokol.", "Musieć + infinitive.")),
 x("Pierwszoroczniakom ____ mieć mioteł.", ["nie wolno", "nie trzeba", "muszą"], U("Заборона.", "Zakaz.", "Not allowed.")),
 x("Muszę się więcej ____.", ["uczyć", "uczę", "uczyłem"], U("Інфінітив.", "Bezokolicznik.", "Infinitive.")),
]
D[14] = [
 x("____ przeczytałeś podręcznik?", ["Czy", "Co", "Kto"], U("Так/ні.", "Tak/nie.", "Yes/no.")),
 x("Hermiona jest mądra, ____?", ["prawda", "czy", "co"], U("Хвостик.", "Końcówka.", "Tag.")),
 x("____ szukałbyś bezoaru?", ["Gdzie", "Czy", "Kto"], U("Місце.", "Miejsce.", "Place.")),
 x("____ to jest bezoar?", ["Co", "Kto", "Gdzie"], U("Що.", "Co.", "What.")),
 x("____ Snape nie lubi Harry'ego?", ["Dlaczego", "Gdzie", "Kto"], U("Причина.", "Przyczyna.", "Reason.")),
 x("____ Hagrid zabrał paczkę?", ["Kiedy", "Co", "Kto"], U("Час.", "Czas.", "Time.")),
]
D[15] = [
 x("____ pani Hooch wróciła, Harry złapał kulkę.", ["Zanim", "Dlatego", "Bo"], U("До того як.", "Przed.", "Before.")),
 x("Neville płakał, bo ____ nadgarstek.", ["złamał", "łamał", "złamie"], U("Доконаний.", "Dokonany.", "Perfective.")),
 x("____ Malfoy rzucił kulkę, Harry poleciał.", ["Kiedy", "Zanim", "Chociaż"], U("Коли.", "Kiedy.", "When.")),
 x("Po tym, jak Harry ____, wszyscy wiwatowali.", ["wylądował", "lądował", "wyląduje"], U("Доконаний.", "Dokonany.", "Perfective.")),
 x("Harry nigdy wcześniej nie ____.", ["latał", "poleciał", "lata"], U("Досвід → недоконаний.", "Doświadczenie → niedok.", "Experience → imperfective.")),
 x("Zanim McGonagall przyszła, Harry już ____.", ["wylądował", "lądował", "ląduje"], U("Вже → доконаний.", "Już → dokonany.", "Already → perfective.")),
]
D[16] = [
 x("Hermiona powiedziała, że pies ____ klapy.", ["pilnuje", "pilnowałby", "pilnujemy"], U("Без зсуву.", "Bez zmiany.", "No backshift.")),
 x("Ron powiedział, ____ jest zmęczony.", ["że", "czy", "żeby"], U("Ствердження.", "Twierdzenie.", "Statement.")),
 x("Hermiona powiedziała, że ____ spać.", ["idzie", "idę", "idziesz"], U("Вона → idzie.", "Ona → idzie.", "She → idzie.")),
 x("Wood powiedział, że ojciec Harry'ego ____ świetnym graczem.", ["był", "jest", "będzie"], U("Минуле в оригіналі.", "Przeszłość.", "Original past.")),
 x("Harry powiedział, że ____ znicza.", ["złapie", "złapię", "złapiesz"], U("Він → złapie.", "On → złapie.", "He → złapie.")),
 x("Ron powiedział, że muszą ____.", ["uciekać", "uciekają", "uciekali"], U("Інфінітив.", "Bezokolicznik.", "Infinitive.")),
]
D[18] = [
 x("Hermiona lubi ____.", ["czytać", "czyta", "czytanie się"], U("Інфінітив.", "Bezokolicznik.", "Infinitive.")),
 x("Ron chciał ____ piórko.", ["unieść", "unosi", "uniósł"], U("Інфінітив.", "Bezokolicznik.", "Infinitive.")),
 x("Neville boi się ____.", ["latania", "latanie", "lataniem"], U("Родовий.", "Dopełniacz.", "Genitive.")),
 x("Harry szuka ____.", ["Hermiony", "Hermionę", "Hermioną"], U("Szukać + родовий.", "Szukać + dop.", "Szukać + genitive.")),
 x("Seamus przestał ____ zaklęcia.", ["rzucać", "rzuca", "rzucał"], U("Інфінітив.", "Bezokolicznik.", "Infinitive.")),
 x("Ron uczy się ____.", ["zaklęć", "zaklęcia", "zaklęciami"], U("Родовий.", "Dopełniacz.", "Genitive.")),
]
D[19] = [
 x("Gdybym zobaczył trolla, ____.", ["uciekłbym", "ucieknę", "uciekłem"], U("-bym.", "-bym.", "-bym.")),
 x("Gdybym był tobą, ____ ją.", ["przeprosiłbym", "przeproszę", "przeprosiłem"], U("-bym.", "-bym.", "-bym.")),
 x("Gdyby Ron ____ odważniejszy, przeprosiłby.", ["był", "jest", "będzie"], U("Gdyby + -ł.", "Gdyby + -ł.", "Gdyby + -ł.")),
 x("Co ____ zrobił, gdybyś spotkał trolla?", ["byś", "będziesz", "bym"], U("Ти → byś.", "Ty → byś.", "You → byś.")),
 x("Gdyby Hermiona nie pomogła, chłopcy ____ kłopoty.", ["mieliby", "będą mieć", "mieli"], U("Вони → -liby.", "Oni → -liby.", "They → -liby.")),
 x("Gdybym miała różdżkę, ____ codziennie.", ["czarowałabym", "czaruję", "czarowałam"], U("Жін. → -łabym.", "Ż. → -łabym.", "Female → -łabym.")),
]
D[20] = [
 x("Harry latał ____ niż inni.", ["szybciej", "szybki", "najszybciej"], U("Вищий ступінь.", "Wyższy.", "Comparative.")),
 x("Ślizgoni grali bardzo ____.", ["źle", "zły", "gorszy"], U("Прислівник.", "Przysłówek.", "Adverb.")),
 x("Hermiona patrzyła ____.", ["uważnie", "uważna", "uważny"], U("Прислівник.", "Przysłówek.", "Adverb.")),
 x("Miotła ruszała się ____.", ["dziwnie", "dziwna", "dziwny"], U("Прислівник.", "Przysłówek.", "Adverb.")),
 x("Gryffindor grał ____ w drugiej połowie.", ["lepiej", "lepszy", "dobry"], U("Dobrze → lepiej.", "Dobrze → lepiej.", "Dobrze → lepiej.")),
 x("Znicz leciał ____ ze wszystkich.", ["najszybciej", "szybciej", "szybki"], U("Найвищий.", "Najwyższy.", "Superlative.")),
]
D[21] = [
 x("Ron zapytał, ____ przysłał pelerynę.", ["kto", "że", "żeby"], U("Хто.", "Kto.", "Who.")),
 x("Filch zapytał, ____ tam jest.", ["kto", "czy", "żeby"], U("Хто.", "Kto.", "Who.")),
 x("Ron kazał Harry'emu, ____ ją założył.", ["żeby", "że", "czy"], U("Наказ.", "Polecenie.", "Command.")),
 x("Dumbledore poprosił, żeby Harry nie ____ lustra.", ["szukał", "szuka", "szukać"], U("Żeby + -ł.", "Żeby + -ł.", "Żeby + -ł.")),
 x("Harry zapytał, ____ peleryna należała do ojca.", ["czy", "że", "kto"], U("Так/ні.", "Tak/nie.", "Yes/no.")),
 x("Ron zapytał, ____ Harry widzi w lustrze.", ["co", "czy", "żeby"], U("Що.", "Co.", "What.")),
]
D[22] = [
 x("Gdyby tylko rodzice ____ tutaj!", ["byli", "są", "będą"], U("Gdyby tylko + -li.", "Gdyby tylko + -li.", "Gdyby tylko + -li.")),
 x("Szkoda, ____ ich tu nie ma.", ["że", "żeby", "czy"], U("Szkoda, że.", "Szkoda, że.", "Szkoda, że.")),
 x("Gdybym tylko ____ ich widzieć codziennie!", ["mógł", "mogę", "będę mógł"], U("-ł.", "-ł.", "-ł.")),
 x("Ron chciałby, żeby ____ kapitanem.", ["był", "jest", "będzie"], U("Żeby + -ł.", "Żeby + -ł.", "Żeby + -ł.")),
 x("Szkoda, że nie ____ więcej pieniędzy.", ["mam", "miałbym", "mieć"], U("Реальність.", "Rzeczywistość.", "Reality.")),
 x("Gdyby tylko Hermiona ____ teraz z nami!", ["była", "jest", "będzie"], U("Жін. -ła.", "Ż. -ła.", "Fem. -ła.")),
]
D[24] = [
 x("Kamień ____ ukryty w zamku.", ["został", "została", "zostało"], U("Чол.", "M.", "Masc.")),
 x("Kamień może być ____ do robienia złota.", ["użyty", "użyć", "używa"], U("Дієприкметник.", "Imiesłów.", "Participle.")),
 x("Musi być ____ za wszelką cenę.", ["chroniony", "chronić", "chroni"], U("Дієприкметник.", "Imiesłów.", "Participle.")),
 x("Nazwisko Flamela ____ znalezione w starej księdze.", ["zostało", "został", "została"], U("Сер.", "N.", "Neuter.")),
 x("Eliksir ____ pity regularnie.", ["musi być", "musi", "musiał"], U("Musi być + -ty.", "Musi być + -ty.", "Musi być + -ty.")),
 x("Kamień wkrótce ____ zniszczony.", ["zostanie", "został", "zostaje"], U("Майбутній пасив.", "Przyszła bierna.", "Future passive.")),
]
D[25] = [
 x("Kiedyś Hagrid ____ o smoku.", ["marzył", "zamarzył", "marzy jutro"], U("Звичка.", "Nawyk.", "Habit.")),
 x("Hagrid przyzwyczaił się do ____.", ["smoków", "smoki", "smokami"], U("До + родовий.", "Do + dop.", "Do + genitive.")),
 x("Przyzwyczaisz się do ____ ze smokiem.", ["mieszkania", "mieszkanie", "mieszkać"], U("Родовий.", "Dopełniacz.", "Genitive.")),
 x("Czy ____ miałeś zwierzęta?", ["kiedyś", "jutro", "zaraz"], U("Колись.", "Kiedyś.", "Ever / used to.")),
 x("Norbert ____ do Rumunii.", ["przyzwyczai się", "przyzwyczaja się wczoraj", "przyzwyczaić"], U("Майбутній.", "Przyszły.", "Future.")),
 x("Hagrid codziennie ____ o smokach.", ["opowiadał", "opowiedział", "opowie"], U("Звичка.", "Nawyk.", "Habit.")),
]
D[26] = [
 x("Gdyby Malfoy nas nie zobaczył, nie ____ nas.", ["złapaliby", "złapią", "złapali"], U("-liby.", "-liby.", "-liby.")),
 x("Gdybyśmy ____ w łóżkach, mielibyśmy punkty.", ["zostali", "zostaniemy", "zostajemy"], U("Gdyby + -li.", "Gdyby + -li.", "Gdyby + -li.")),
 x("Gdyby Neville nie wyszedł, nie ____ szlabanu.", ["dostałby", "dostanie", "dostał"], U("-łby.", "-łby.", "-łby.")),
 x("Gdybyśmy ____ ostrożniejsi, nic by się nie stało.", ["byli", "będziemy", "jesteśmy"], U("-li.", "-li.", "-li.")),
 x("Gdyby Harry wiedział, nie ____.", ["poszedłby", "pójdzie", "poszedł"], U("-łby.", "-łby.", "-łby.")),
 x("Gdyby Hagrid nie wygrał jaja, nie ____ smoka.", ["byłoby", "będzie", "było"], U("Безособове.", "Bezosobowe.", "Impersonal.")),
]
D[27] = [
 x("Kieł, ____ jest psem Hagrida, to tchórz.", ["który", "którego", "którym"], U("Підмет.", "Podmiot.", "Subject.")),
 x("Krew, ____ jest srebrna, utrzymuje przy życiu.", ["która", "który", "które"], U("Жін.", "Ż.", "Fem.")),
 x("Las, do ____ nie wolno wchodzić, jest ciemny.", ["którego", "który", "którym"], U("Do + родовий.", "Do + dop.", "Do + genitive.")),
 x("Hagrid, ____ niósł latarnię, prowadził.", ["który", "którego", "którym"], U("Підмет.", "Podmiot.", "Subject.")),
 x("Firenzo, z ____ rozmawiał Harry, to centaur.", ["którym", "który", "którego"], U("З + орудний.", "Z + narzędnik.", "Z + instrumental.")),
 x("Draco, ____ się bał, uciekł.", ["który", "którego", "którym"], U("Підмет.", "Podmiot.", "Subject.")),
]
D[28] = [
 x("Postać ____ być Voldemortem.", ["musiała", "nie mogła", "chciała"], U("Висновок.", "Wniosek.", "Deduction.")),
 x("Nieznajomy nie ____ być zwykłym człowiekiem.", ["mógł", "musiał", "chciał"], U("Точно ні.", "Na pewno nie.", "Certainly not.")),
 x("Hagrid ____ mu powiedzieć — był pijany.", ["mógł", "musiał", "nie mógł"], U("Можливо.", "Możliwe.", "Possibly.")),
 x("Snape ____ chcieć kamienia, myślał Harry.", ["musiał", "nie mógł", "nie musiał"], U("Висновок Гаррі.", "Wniosek.", "Harry's deduction.")),
 x("Nieznajomy ____ wszystko zaplanować.", ["musiał", "nie mógł", "nie musiał"], U("Висновок.", "Wniosek.", "Deduction.")),
 x("Blizna nie ____ boleć bez powodu.", ["mogła", "musiała", "chciała"], U("Точно ні.", "Na pewno nie.", "Certainly not.")),
]
D[30] = [
 x("____ się, Ron!", ["Uspokój", "Uspokoić", "Uspokaja"], U("Наказовий.", "Rozkazujący.", "Imperative.")),
 x("Lepiej ____ do łóżka.", ["idź", "idziesz", "iść"], U("Наказовий.", "Rozkazujący.", "Imperative.")),
 x("____ powiedzieć nauczycielowi.", ["Powinieneś", "Powinna", "Powinniśmy był"], U("Порада.", "Rada.", "Advice.")),
 x("Nie ____ psa!", ["budź", "budzić", "budzisz"], U("Заперечний наказ.", "Przeczący rozkaz.", "Negative imperative.")),
 x("Powinniśmy się ____.", ["pospieszyć", "pospieszamy", "pospieszyli"], U("Інфінітив.", "Bezokolicznik.", "Infinitive.")),
 x("Lepiej nie ____!", ["panikuj", "panikować", "panikujesz"], U("Наказовий.", "Rozkazujący.", "Imperative.")),
]
D[31] = [
 x("Gdyby Ron nie grał dobrze w szachy, nie ____ dalej.", ["przeszlibyśmy", "przejdziemy", "przeszliśmy"], U("-libyśmy.", "-libyśmy.", "-libyśmy.")),
 x("Gdyby Harry nie złapał klucza, ____ teraz w tamtej sali.", ["byłby", "będzie", "był"], U("Зараз.", "Teraz.", "Now.")),
 x("Gdyby nie Ron, Harry nie ____ teraz tutaj.", ["byłby", "będzie", "jest"], U("-łby.", "-łby.", "-łby.")),
 x("Gdybym ____ lepiej latać, złapałbym go szybciej.", ["umiał", "umiem", "umiałbym"], U("Gdyby + -ł.", "Gdyby + -ł.", "Gdyby + -ł.")),
 x("Gdyby Hermiona nie pomogła, ____ teraz w sidłach.", ["bylibyśmy", "będziemy", "jesteśmy"], U("Ми → -libyśmy.", "My → -libyśmy.", "We → -libyśmy.")),
 x("Gdyby Ron nie był odważny, nie ____ tego ruchu.", ["zrobiłby", "zrobi", "zrobił"], U("-łby.", "-łby.", "-łby.")),
]
D[32] = [
 x("To ____ Quirrell wpuścił trolla.", ["właśnie", "chyba nie", "nigdy"], U("Підсилення.", "Wyróżnienie.", "Emphasis.")),
 x("To nie Snape, ____ Quirrell.", ["tylko", "ale też", "czy"], U("Не X, а Y.", "Nie X, tylko Y.", "Not X but Y.")),
 x("To ____ Snape ratował Harry'ego.", ["właśnie", "nigdy", "może nie"], U("Підсилення.", "Wyróżnienie.", "Emphasis.")),
 x("Najważniejszy ____ kamień.", ["był", "była", "byli"], U("Чол.", "M.", "Masc.")),
 x("To, co zobaczył Harry, ____ niezwykłe.", ["było", "był", "była"], U("Сер.", "N.", "Neuter.")),
 x("To nie Snape ____ wrogiem.", ["był", "była", "byli"], U("Чол.", "M.", "Masc.")),
]
D[33] = [
 x("____ komuś powiedzieć!", ["Powinienem był", "Powinienem będę", "Powinien"], U("Жаль.", "Żal.", "Regret.")),
 x("Mogłeś ____!", ["zginąć", "ginąć wczoraj", "zginął"], U("Інфінітив.", "Bezokolicznik.", "Infinitive.")),
 x("Nie ____ mu mówić!", ["powinienem był", "muszę", "mogę"], U("Жаль.", "Żal.", "Regret.")),
 x("Nie ____ się martwić — kamień jest bezpieczny.", ["musiałeś", "mogłeś", "chciałeś"], U("Не треба було.", "Nie trzeba było.", "Needn't have.")),
 x("Nie ____ iść bez nauczyciela.", ["powinniśmy byli", "powinniśmy będziemy", "musimy"], U("Жаль.", "Żal.", "Regret.")),
 x("Harry ____ zginąć, ale uratowała go miłość.", ["mógł", "musiał", "powinien"], U("Можливість.", "Możliwość.", "Possibility.")),
]
D[34] = [
 x("Kiedy Dumbledore ____, wszyscy słuchali.", ["mówił", "powiedział", "powie"], U("Тло.", "Tło.", "Background.")),
 x("Gryffindor ____ puchar.", ["wygrał", "wygrywał", "wygra"], U("Подія.", "Zdarzenie.", "Event.")),
 x("Uczniowie ____, gdy zmieniły się sztandary.", ["wiwatowali", "zawiwatują", "wiwatują"], U("Тло.", "Tło.", "Background.")),
 x("Neville ____ dziesięć punktów.", ["dostał", "dostawał", "dostanie"], U("Подія.", "Zdarzenie.", "Event.")),
 x("Przez dziesięć lat Harry ____ pod schodami.", ["mieszkał", "zamieszkał", "mieszka"], U("Тривалість.", "Trwanie.", "Duration.")),
 x("Kiedy Hagrid ____, Harry miał jedenaście lat.", ["przyszedł", "przychodził", "przyjdzie"], U("Подія.", "Zdarzenie.", "Event.")),
]
