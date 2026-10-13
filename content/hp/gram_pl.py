# Wersja kursu dla uczących się POLSKIEGO. Gramatyka B1→B2 + list (zadanie pisemne).
# g(pytanie, [poprawna, zła, zła], [(uk,pl,en) ×3], (tip uk,pl,en)) — poprawna zawsze pierwsza (tasowane w variants).
G, D, T = {}, {}, {}
def g(q, opts, whys, tip): return (q, opts, 0, whys, tip)
def letter(uk, pl, en, mw=45): return None

T[1] = ("Теперішній час: -ę/-esz, -am/-asz", "Czas teraźniejszy: koniugacje", "Present tense: conjugations")
G[1] = [
 g("Harry codziennie ____ śniadanie dla Dursleyów.", ["robi", "robię", "robią"],
   [("Так! Він → robi.", "Tak! On → robi.", "Yes! He → robi."), ("Robię — «я».", "Robię to forma „ja”.", "Robię is the “I” form."), ("Robią — «вони».", "Robią — „oni”.", "Robią is “they”.")],
   ("Robić: robię, robisz, robi, robimy, robicie, robią.", "Robić: robię, robisz, robi…", "Robić: robię, robisz, robi…")),
 g("Ciocia Petunia właśnie ____ do drzwi komórki.", ["puka", "pukam", "pukają"],
   [("Так! Вона → puka. Польська не має окремого тривалого часу.", "Tak! Ona → puka.", "Yes! She → puka. Polish has no separate continuous tense."), ("Pukam — «я».", "Pukam — „ja”.", "Pukam is “I”."), ("Pukają — «вони».", "Pukają — „oni”.", "Pukają is “they”.")],
   ("Właśnie + теперішній час = «саме зараз».", "Właśnie + czas teraźniejszy = teraz.", "Właśnie + present = right now.")),
]
D[1] = ("Napisz krótki liścik jako Harry (40+ słów): gdzie mieszkasz, co robisz codziennie i co dzieje się teraz.", 40,
 ("Почни з «Mieszkam z ciocią i wujkiem…».", "Zacznij od „Mieszkam z ciocią i wujkiem…”.", "Start with “Mieszkam z ciocią i wujkiem…”."))

T[2] = ("Минулий час і рід: był / była", "Czas przeszły i rodzaj", "Past tense and gender")
G[2] = [
 g("Ciocia Petunia ____ w zoo bardzo zdenerwowana.", ["była", "był", "było"],
   [("Так! Жінка → była.", "Tak! Kobieta → była.", "Yes! A woman → była."), ("Był — чоловічий рід.", "Był — rodzaj męski.", "Był is masculine."), ("Było — середній рід.", "Było — rodzaj nijaki.", "Było is neuter.")],
   ("Минулий час змінюється за родом.", "Czas przeszły zmienia się według rodzaju.", "The past tense changes by gender.")),
 g("Wąż ____ do Harry'ego.", ["mrugnął", "mrugnęła", "mrugnęło"],
   [("Так! Wąż — ч.р. → -ął.", "Tak! Wąż — m. → -ął.", "Yes! Wąż is masculine → -ął."), ("-ęła — для жіночого.", "-ęła — żeński.", "-ęła is feminine."), ("-ęło — для середнього.", "-ęło — nijaki.", "-ęło is neuter.")],
   ("Рід іменника визначає закінчення.", "Rodzaj rzeczownika decyduje o końcówce.", "The noun's gender decides the ending.")),
]
D[2] = ("Opisz dzień w zoo (45+ słów) w czasie przeszłym. Uważaj na rodzaj: Harry był, Petunia była.", 45,
 ("Закінчення -ł / -ła.", "Końcówki -ł / -ła.", "Endings -ł / -ła."))

T[3] = ("Вид дієслова: pisać / napisać", "Aspekt: pisać / napisać", "Verb aspect: pisać / napisać")
G[3] = [
 g("Wuj Vernon ____ list i wrzucił go do ognia.", ["przeczytał", "czytał", "czyta"],
   [("Так! Одна завершена дія → доконаний вид.", "Tak! Jedna zakończona czynność → dokonany.", "Yes! One finished action → perfective."), ("Czytał — процес, без результату.", "Czytał — proces.", "Czytał is a process."), ("Czyta — теперішній.", "Czyta — teraźniejszy.", "Czyta is present.")],
   ("Доконаний вид = результат.", "Aspekt dokonany = rezultat.", "Perfective = result.")),
 g("Przez cały tydzień sowy ____ listy.", ["przynosiły", "przyniosły", "przyniesie"],
   [("Так! Повторювана дія → недоконаний.", "Tak! Powtarzana czynność → niedokonany.", "Yes! Repeated action → imperfective."), ("Przyniosły — один раз.", "Przyniosły — jeden raz.", "Przyniosły means once."), ("Przyniesie — майбутнє.", "Przyniesie — przyszłość.", "Przyniesie is future.")],
   ("Przez cały… → недоконаний.", "Przez cały… → niedokonany.", "Przez cały… → imperfective.")),
]
D[3] = ("Opisz historię z listami (45+ słów). Użyj par aspektowych: pisać/napisać, palić/spalić.", 45,
 ("Процес і результат.", "Proces i rezultat.", "Process and result."))

T[4] = ("Пасив: został / była + дієприкметник", "Strona bierna: zostać / być + imiesłów", "Passive: zostać / być + participle")
G[4] = [
 g("Rodzice Harry'ego ____ zamordowani.", ["zostali", "został", "została"],
   [("Так! Множина, чоловічоособовий → zostali.", "Tak! Liczba mnoga męskoosobowa → zostali.", "Yes! Masculine-personal plural → zostali."), ("Został — однина.", "Został — liczba pojedyncza.", "Został is singular."), ("Została — жін. однина.", "Została — żeńska.", "Została is feminine singular.")],
   ("Zostać + imiesłów = пасив події.", "Zostać + imiesłów = strona bierna.", "Zostać + participle = passive.")),
 g("Harry ____ przyjęty do Hogwartu.", ["został", "zostali", "została"],
   [("Так! Гаррі → został.", "Tak! Harry → został.", "Yes! Harry → został."), ("Zostali — множина.", "Zostali — mnoga.", "Zostali is plural."), ("Została — жін.", "Została — żeńska.", "Została is feminine.")],
   ("Узгодження за родом і числом.", "Zgoda w rodzaju i liczbie.", "Agree in gender and number.")),
]
D[4] = ("Napisz list Harry'ego do Hagrida (45+ słów). Użyj strony biernej: zostałem przyjęty, list został wysłany.", 45,
 ("Zostać + -ny / -ty.", "Zostać + -ny / -ty.", "Zostać + -ny / -ty."))

T[5] = ("Повторення арки 1", "Powtórka łuku 1", "Arc 1 review")
G[5] = [
 g("Teraz Dudley ____ prezenty.", ["liczy", "liczył", "policzy"], [("Так — teraz.", "Tak — teraz.", "Yes — now."), ("Минуле.", "Przeszłość.", "Past."), ("Майбутнє.", "Przyszłość.", "Future.")], ("Урок 1.", "Lekcja 1.", "Lesson 1.")),
 g("Hermiona ____ bardzo zdziwiona.", ["była", "był", "byli"], [("Так — вона.", "Tak — ona.", "Yes — she."), ("Він.", "On.", "He."), ("Вони.", "Oni.", "They.")], ("Урок 2.", "Lekcja 2.", "Lesson 2.")),
 g("Hagrid w końcu ____ tort.", ["upiekł", "piekł", "piecze"], [("Так — результат.", "Tak — rezultat.", "Yes — result."), ("Процес.", "Proces.", "Process."), ("Теперішній.", "Teraźniejszy.", "Present.")], ("Урок 3.", "Lekcja 3.", "Lesson 3.")),
 g("Drzwi ____ wyważone.", ["zostały", "został", "zostali"], [("Так — drzwi (мн.).", "Tak — drzwi (lm).", "Yes — drzwi is plural."), ("Однина.", "Pojedyncza.", "Singular."), ("Чоловічоособова.", "Męskoosobowa.", "Masculine-personal.")], ("Урок 4.", "Lekcja 4.", "Lesson 4.")),
]

T[6] = ("Ступені порівняння", "Stopniowanie przymiotników", "Comparison of adjectives")
G[6] = [
 g("Gringott to ____ miejsce na świecie.", ["najbezpieczniejsze", "bezpieczniejsze", "bezpieczne"],
   [("Так! Найвищий ступінь: naj- + -sze.", "Tak! Stopień najwyższy.", "Yes! Superlative: naj- + -sze."), ("Вищий ступінь.", "Stopień wyższy.", "Comparative."), ("Звичайний.", "Równy.", "Basic form.")],
   ("bezpieczny → bezpieczniejszy → najbezpieczniejszy.", "bezpieczny → bezpieczniejszy → najbezpieczniejszy.", "bezpieczny → bezpieczniejszy → najbezpieczniejszy.")),
 g("Hogwart jest jeszcze ____ niż bank.", ["bezpieczniejszy", "najbezpieczniejszy", "bezpieczny"],
   [("Так! Niż → вищий ступінь.", "Tak! Niż → stopień wyższy.", "Yes! Niż → comparative."), ("Найвищий — без niż.", "Najwyższy — bez niż.", "Superlative doesn't take niż."), ("Без ступеня.", "Bez stopnia.", "No comparison.")],
   ("Порівняння: niż / od + родовий.", "Porównanie: niż / od + dopełniacz.", "Compare with niż / od + genitive.")),
]
D[6] = ("Napisz pocztówkę z ulicy Pokątnej (40+ słów). Porównaj: większy, dziwniejszy, najbezpieczniejszy.", 40,
 ("Мінімум два вищі й два найвищі.", "Minimum dwa stopnie wyższe i dwa najwyższe.", "At least two comparatives and two superlatives."))

T[7] = ("Кількість: dużo / mało / kilka + родовий", "Ilość: dużo / mało / kilka + dopełniacz", "Quantity: dużo / mało / kilka + genitive")
G[7] = [
 g("Harry ma dużo ____.", ["pieniędzy", "pieniądze", "pieniądzami"],
   [("Так! Dużo + родовий відмінок.", "Tak! Dużo + dopełniacz.", "Yes! Dużo + genitive."), ("Називний — помилка.", "Mianownik — błąd.", "Nominative is wrong."), ("Орудний — помилка.", "Narzędnik — błąd.", "Instrumental is wrong.")],
   ("Dużo, mało, kilka, pięć + родовий.", "Dużo, mało, kilka, pięć + dopełniacz.", "Dużo, mało, kilka, pięć + genitive.")),
 g("Na ulicy było pięć ____.", ["sklepów", "sklepy", "sklep"],
   [("Так! П'ять + родовий множини.", "Tak! Pięć + dopełniacz lm.", "Yes! Pięć + genitive plural."), ("Sklepy — після 2–4.", "Sklepy — po 2–4.", "Sklepy follows 2–4."), ("Однина — помилка.", "Pojedyncza — błąd.", "Singular is wrong.")],
   ("2–4 sklepy, 5+ sklepów.", "2–4 sklepy, 5+ sklepów.", "2–4 sklepy, 5+ sklepów.")),
]
D[7] = ("Napisz listę zakupów i myśli Harry'ego (40+ słów): dużo, mało, kilka, za dużo, wystarczająco.", 40,
 ("Після кількості — родовий.", "Po ilości — dopełniacz.", "After quantities — genitive."))

T[8] = ("Підрядні з który / która / które", "Zdania względne: który / która / które", "Relative clauses: który / która / które")
G[8] = [
 g("To różdżka, ____ wybrała Harry'ego.", ["która", "który", "które"],
   [("Так! Różdżka — жін. → która.", "Tak! Różdżka — ż. → która.", "Yes! Różdżka is feminine → która."), ("Który — чол.", "Który — m.", "Który is masculine."), ("Które — сер./мн.", "Które — n./lm.", "Które is neuter/plural.")],
   ("Który узгоджується з іменником.", "Który zgadza się z rzeczownikiem.", "Który agrees with the noun.")),
 g("Ollivander to człowiek, ____ pamięta każdą różdżkę.", ["który", "która", "którego"],
   [("Так! Człowiek — чол., підмет → który.", "Tak! Człowiek — m., podmiot → który.", "Yes! Człowiek, subject → który."), ("Która — жін.", "Która — ż.", "Która is feminine."), ("Którego — знахідний/родовий.", "Którego — biernik/dopełniacz.", "Którego is accusative/genitive.")],
   ("Відмінок який — залежить від ролі в підрядному.", "Przypadek zależy od roli w zdaniu podrzędnym.", "The case depends on its role in the clause.")),
]
D[8] = ("Opisz swoją wymarzoną różdżkę w liście do Ollivandera (40+ słów). Użyj który / która / które.", 40,
 ("Три підрядних мінімум.", "Minimum trzy zdania względne.", "At least three relative clauses."))

T[9] = ("Майбутній час: zrobię / będę robić", "Czas przyszły: zrobię / będę robić", "Future: zrobię / będę robić")
G[9] = [
 g("Jutro Harry ____ do Hogwartu.", ["pojedzie", "jechał", "jedzie wczoraj"],
   [("Так! Майбутній доконаний.", "Tak! Przyszły dokonany.", "Yes! Perfective future."), ("Минулий.", "Przeszły.", "Past."), ("Неможливе поєднання.", "Niemożliwe połączenie.", "Impossible combination.")],
   ("Доконаний вид у теперішній формі = майбутнє.", "Forma teraźniejsza czasownika dokonanego = przyszłość.", "A perfective verb in present form = future.")),
 g("Przez całą drogę Ron ____ jeść słodycze.", ["będzie", "był", "jest"],
   [("Так! Będzie + інфінітив — процес у майбутньому.", "Tak! Będzie + bezokolicznik — proces w przyszłości.", "Yes! Będzie + infinitive = a future process."), ("Минулий.", "Przeszły.", "Past."), ("Теперішній.", "Teraźniejszy.", "Present.")],
   ("Będę robić — тривала дія в майбутньому.", "Będę robić — czynność ciągła w przyszłości.", "Będę robić — an ongoing future action.")),
]
D[9] = ("Napisz notatkę z pociągu (45+ słów): co zrobisz w Hogwarcie, co będziesz robić wieczorem.", 45,
 ("Обидві форми майбутнього.", "Obie formy przyszłe.", "Both future forms."))

T[10] = ("Припущення: na pewno / chyba / nie może", "Przypuszczenia: na pewno / chyba / nie może być", "Guessing: na pewno / chyba / nie może być")
G[10] = [
 g("Hermiona zna wszystkie zaklęcia. ____ jest bardzo mądra.", ["Na pewno", "Chyba nie", "Nie może"],
   [("Так! Упевнений висновок.", "Tak! Pewny wniosek.", "Yes! A confident guess."), ("Суперечить фактам.", "Przeczy faktom.", "Contradicts the facts."), ("Протилежне.", "Odwrotnie.", "The opposite.")],
   ("Na pewno — 95%, chyba — 50%, nie może być — 5%.", "Na pewno, chyba, nie może być.", "Na pewno ≈ must, chyba ≈ might, nie może być ≈ can't.")),
 g("Ron ma stare ubrania. Jego rodzina ____ być bogata.", ["nie może", "na pewno", "musi"],
   [("Так! Nie może być = точно ні.", "Tak! Nie może być = na pewno nie.", "Yes! Nie może być = can't be."), ("Протилежне.", "Odwrotnie.", "The opposite."), ("Musi być — точно так.", "Musi być — na pewno tak.", "Musi być = must be.")],
   ("Musi być / nie może być — логічні висновки.", "Musi być / nie może być — wnioski.", "Musi być / nie może być — deductions.")),
]
D[10] = ("Napisz list Rona do mamy (45+ słów) z przypuszczeniami: na pewno, chyba, nie może być.", 45,
 ("Три висновки мінімум.", "Minimum trzy przypuszczenia.", "At least three guesses."))

T[11] = ("Повторення арки 2", "Powtórka łuku 2", "Arc 2 review")
G[11] = [
 g("Hogwart jest ____ niż Gringott.", ["bezpieczniejszy", "najbezpieczniejszy", "bezpieczny"], [("Так — niż.", "Tak — niż.", "Yes — niż."), ("Найвищий.", "Najwyższy.", "Superlative."), ("Без ступеня.", "Bez stopnia.", "No degree.")], ("Урок 6.", "Lekcja 6.", "Lesson 6.")),
 g("W pociągu było dużo ____.", ["uczniów", "uczniowie", "uczeń"], [("Так — родовий.", "Tak — dopełniacz.", "Yes — genitive."), ("Називний.", "Mianownik.", "Nominative."), ("Однина.", "Pojedyncza.", "Singular.")], ("Урок 7.", "Lekcja 7.", "Lesson 7.")),
 g("To sowa, ____ dostał Harry.", ["którą", "który", "która"], [("Так — знахідний жін.", "Tak — biernik ż.", "Yes — feminine accusative."), ("Чол.", "Męski.", "Masculine."), ("Називний.", "Mianownik.", "Nominative.")], ("Урок 8.", "Lekcja 8.", "Lesson 8.")),
 g("Jutro ____ na peron 9¾.", ["pójdziemy", "poszliśmy", "idziemy wczoraj"], [("Так — майбутнє.", "Tak — przyszłość.", "Yes — future."), ("Минуле.", "Przeszłość.", "Past."), ("Неможливо.", "Niemożliwe.", "Impossible.")], ("Урок 9.", "Lekcja 9.", "Lesson 9.")),
 g("To ____ być prawdziwe zaklęcie!", ["nie może", "na pewno", "musi"], [("Так — точно ні.", "Tak — na pewno nie.", "Yes — can't be."), ("Протилежне.", "Odwrotnie.", "Opposite."), ("Протилежне.", "Odwrotnie.", "Opposite.")], ("Урок 10.", "Lekcja 10.", "Lesson 10.")),
]

T[12] = ("Реальна умова: jeśli + майбутній", "Warunek realny: jeśli + czas przyszły", "Real condition: jeśli + future")
G[12] = [
 g("Jeśli złamiesz zasady, ____ punkty.", ["stracisz", "traciłeś", "straciłbyś"],
   [("Так! Jeśli + майбутній → майбутній.", "Tak! Jeśli + przyszły → przyszły.", "Yes! Jeśli + future → future."), ("Минулий.", "Przeszły.", "Past."), ("Умовний — для нереального.", "Tryb przypuszczający — nierealne.", "Conditional mood is for unreal.")],
   ("Jeśli + przyszły, przyszły.", "Jeśli + przyszły, przyszły.", "Jeśli + future, future.")),
 g("Jeśli ____ Tiarę, ona wybierze dom.", ["założysz", "zakładałeś", "założyłbyś"],
   [("Так! Майбутній доконаний після jeśli.", "Tak! Przyszły dokonany po jeśli.", "Yes! Perfective future after jeśli."), ("Минулий.", "Przeszły.", "Past."), ("Нереальна умова.", "Warunek nierealny.", "Unreal condition.")],
   ("На відміну від англійської, після jeśli — майбутній час!", "Inaczej niż po angielsku: po jeśli — przyszły!", "Unlike English, Polish uses the future after jeśli!")),
]
D[12] = ("Napisz list do Hagrida po Ceremonii Przydziału (45+ słów). Użyj trzech zdań z jeśli.", 45,
 ("Jeśli + майбутній.", "Jeśli + przyszły.", "Jeśli + future."))

T[13] = ("Модальні: musieć / nie wolno / nie trzeba", "Modalne: musieć / nie wolno / nie trzeba", "Modals: musieć / nie wolno / nie trzeba")
G[13] = [
 g("Uczniom ____ wchodzić do Zakazanego Lasu.", ["nie wolno", "nie trzeba", "trzeba"],
   [("Так! Заборона.", "Tak! Zakaz.", "Yes! A prohibition."), ("Не обов'язково — інше значення.", "Nie trzeba — brak obowiązku.", "Nie trzeba = not necessary."), ("Треба — протилежне.", "Trzeba — odwrotnie.", "Trzeba is the opposite.")],
   ("Nie wolno = заборонено; nie trzeba = не обов'язково.", "Nie wolno ≠ nie trzeba.", "Nie wolno = mustn't; nie trzeba = don't have to.")),
 g("W sobotę ____ iść na lekcje.", ["nie trzeba", "nie wolno", "musi"],
   [("Так! Немає обов'язку.", "Tak! Brak obowiązku.", "Yes! No obligation."), ("Заборона — неправда.", "Zakaz — nieprawda.", "A ban isn't true here."), ("Musi без підмета — помилка.", "Musi bez podmiotu — błąd.", "Musi needs a subject.")],
   ("Trzeba / nie trzeba — безособові.", "Trzeba / nie trzeba — bezosobowe.", "Trzeba / nie trzeba are impersonal.")),
]
D[13] = ("Napisz zasady Hogwartu dla nowego ucznia (45+ słów): musisz, nie wolno, nie trzeba.", 45,
 ("Кожен модальний хоча б раз.", "Każdy czasownik modalny co najmniej raz.", "Each modal at least once."))

T[14] = ("Питання: czy, wh-слова, prawda?", "Pytania: czy, zaimki pytajne, prawda?", "Questions: czy, question words, prawda?")
G[14] = [
 g("____ przeczytałeś podręcznik przed lekcją?", ["Czy", "Co", "Gdzie"],
   [("Так! Так/ні-питання → czy.", "Tak! Pytanie tak/nie → czy.", "Yes! Yes/no question → czy."), ("Co — «що».", "Co — o rzecz.", "Co means “what”."), ("Gdzie — «де».", "Gdzie — o miejsce.", "Gdzie means “where”.")],
   ("Czy відкриває загальне питання.", "Czy otwiera pytanie ogólne.", "Czy opens a yes/no question.")),
 g("Nie znasz odpowiedzi, ____?", ["prawda", "czy", "co"],
   [("Так! …, prawda? — польський «хвостик».", "Tak! …, prawda?", "Yes! …, prawda? is the Polish tag."), ("Czy — на початку.", "Czy — na początku.", "Czy goes at the start."), ("Co — не хвостик.", "Co — nie końcówka.", "Co isn't a tag.")],
   ("Prawda? / tak? / nie? — для підтвердження.", "Prawda? / tak? — potwierdzenie.", "Prawda? / tak? — to confirm.")),
]
D[14] = ("Napisz pięć pytań do Hagrida o skrytkę 713 (45+ słów). Użyj czy i prawda?", 45,
 ("Різні типи питань.", "Różne typy pytań.", "Different question types."))

T[15] = ("Послідовність: zanim / kiedy / po tym, jak", "Kolejność: zanim / kiedy / po tym, jak", "Sequence: zanim / kiedy / po tym, jak")
G[15] = [
 g("____ pani Hooch wróciła, Harry już złapał kulkę.", ["Zanim", "Po tym, jak", "Dlatego"],
   [("Так! Zanim = до того як.", "Tak! Zanim = przed.", "Yes! Zanim = before."), ("Після — інша послідовність.", "Po tym, jak — odwrotna kolejność.", "Po tym, jak = after — wrong order."), ("Dlatego — причина.", "Dlatego — skutek.", "Dlatego means “so”.")],
   ("У польській немає Past Perfect — порядок показують сполучники.", "Kolejność pokazują spójniki.", "Polish has no Past Perfect — conjunctions show the order.")),
 g("Neville płakał, bo ____ nadgarstek.", ["złamał", "łamał", "złamie"],
   [("Так! Завершена дія раніше → доконаний.", "Tak! Wcześniejsza zakończona czynność → dokonany.", "Yes! An earlier finished action → perfective."), ("Процес.", "Proces.", "Process."), ("Майбутнє.", "Przyszłość.", "Future.")],
   ("Доконаний вид показує завершене раніше.", "Dokonany pokazuje to, co zakończyło się wcześniej.", "Perfective shows what was finished earlier.")),
]
D[15] = ("Napisz list Neville'a do babci ze skrzydła szpitalnego (45+ słów). Użyj zanim i po tym, jak.", 45,
 ("Покажи порядок подій.", "Pokaż kolejność zdarzeń.", "Show the order of events."))

T[16] = ("Непряма мова: powiedziała, że…", "Mowa zależna: powiedziała, że…", "Reported speech: powiedziała, że…")
G[16] = [
 g("Hermiona powiedziała, że pies ____ czegoś.", ["pilnuje", "pilnował", "pilnowałby"],
   [("Так! У польській час зазвичай не зсувається.", "Tak! W polskim czas się nie zmienia.", "Yes! Polish usually keeps the original tense."), ("Можливо, але природніше теперішній.", "Możliwe, ale naturalniej teraźniejszy.", "Possible, but the present is more natural."), ("Умовний — інший зміст.", "Tryb przypuszczający — inny sens.", "Conditional changes the meaning.")],
   ("Нема зсуву часів, як в англійській!", "Bez cofania czasu, inaczej niż po angielsku!", "No backshift, unlike English!")),
 g("Ron powiedział, ____ nigdy nie widział takiego psa.", ["że", "czy", "żeby"],
   [("Так! Ствердження → że.", "Tak! Twierdzenie → że.", "Yes! A statement → że."), ("Czy — для питань.", "Czy — pytania.", "Czy is for questions."), ("Żeby — для прохань.", "Żeby — prośby.", "Żeby is for requests.")],
   ("Powiedział, że… / zapytał, czy… / kazał, żeby…", "Powiedział, że… / zapytał, czy… / kazał, żeby…", "Powiedział, że… / zapytał, czy… / kazał, żeby…")),
]
D[16] = ("Opowiedz, co kto powiedział tamtej nocy (45+ słów): powiedział, że…, Hermiona powiedziała, że…", 45,
 ("Що + теперішній/минулий як в оригіналі.", "Że + czas jak w oryginale.", "Że + the original tense."))

T[17] = ("Повторення арки 3", "Powtórka łuku 3", "Arc 3 review")
G[17] = [
 g("Jeśli ____ znicza, wygramy.", ["złapiesz", "złapałeś", "złapałbyś"], [("Так.", "Tak.", "Yes."), ("Минуле.", "Przeszłość.", "Past."), ("Нереальне.", "Nierealne.", "Unreal.")], ("Урок 12.", "Lekcja 12.", "Lesson 12.")),
 g("Na trzecie piętro ____ chodzić!", ["nie wolno", "nie trzeba", "trzeba"], [("Так.", "Tak.", "Yes."), ("Не обов'язково.", "Nie ma obowiązku.", "Not necessary."), ("Протилежне.", "Odwrotnie.", "Opposite.")], ("Урок 13.", "Lekcja 13.", "Lesson 13.")),
 g("Snape jest surowy, ____?", ["prawda", "czy", "co"], [("Так.", "Tak.", "Yes."), ("На початку.", "Na początku.", "At the start."), ("Ні.", "Nie.", "No.")], ("Урок 14.", "Lekcja 14.", "Lesson 14.")),
 g("Hermiona powiedziała, ____ idzie spać.", ["że", "czy", "żeby"], [("Так.", "Tak.", "Yes."), ("Питання.", "Pytanie.", "Question."), ("Прохання.", "Prośba.", "Request.")], ("Урок 16.", "Lekcja 16.", "Lesson 16.")),
]

T[18] = ("Після дієслів: lubić + інфінітив, uczyć się + родовий", "Po czasownikach: lubić + bezokolicznik, uczyć się + dopełniacz", "After verbs: lubić + infinitive, uczyć się + genitive")
G[18] = [
 g("Hermiona lubi ____ zaklęcia.", ["ćwiczyć", "ćwiczy", "ćwiczenie"],
   [("Так! Lubić + інфінітив.", "Tak! Lubić + bezokolicznik.", "Yes! Lubić + infinitive."), ("Особова форма — помилка.", "Forma osobowa — błąd.", "A finite form is wrong."), ("Іменник тут неприродний.", "Rzeczownik nienaturalny.", "A noun sounds unnatural here.")],
   ("Lubić, chcieć, umieć + інфінітив.", "Lubić, chcieć, umieć + bezokolicznik.", "Lubić, chcieć, umieć + infinitive.")),
 g("Ron uczy się ____.", ["zaklęć", "zaklęcia", "zaklęciami"],
   [("Так! Uczyć się + родовий.", "Tak! Uczyć się + dopełniacz.", "Yes! Uczyć się + genitive."), ("Знахідний — помилка.", "Biernik — błąd.", "Accusative is wrong."), ("Орудний — помилка.", "Narzędnik — błąd.", "Instrumental is wrong.")],
   ("Uczyć się, bać się, szukać + родовий.", "Uczyć się, bać się, szukać + dopełniacz.", "Uczyć się, bać się, szukać + genitive.")),
]
D[18] = ("Napisz list Hermiony do rodziców (45+ słów): co lubisz robić, czego się uczysz, czego się boisz.", 45,
 ("Інфінітив і родовий.", "Bezokolicznik i dopełniacz.", "Infinitive and genitive."))

T[19] = ("Умовний спосіб: gdybym…, -bym", "Tryb przypuszczający: gdybym…", "Conditional mood: gdybym…")
G[19] = [
 g("Gdybym spotkał trolla, ____.", ["uciekłbym", "ucieknę", "uciekłem"],
   [("Так! Gdyby + -bym.", "Tak! Gdyby + -bym.", "Yes! Gdyby + -bym."), ("Реальна умова.", "Warunek realny.", "Real condition."), ("Минуле.", "Przeszłość.", "Past.")],
   ("Gdybym + минулий, …-bym.", "Gdybym + forma przeszła, …-bym.", "Gdybym + past form, …-bym.")),
 g("Gdyby Ron ____ odważniejszy, przeprosiłby Hermionę.", ["był", "jest", "będzie"],
   [("Так! Gdyby + форма минулого.", "Tak! Gdyby + forma przeszła.", "Yes! Gdyby + past form."), ("Теперішній — помилка.", "Teraźniejszy — błąd.", "Present is wrong."), ("Майбутній — помилка.", "Przyszły — błąd.", "Future is wrong.")],
   ("Після gdyby — форма на -ł.", "Po gdyby — forma na -ł.", "After gdyby use the -ł form.")),
]
D[19] = ("Jesteś Ronem. Napisz liścik do Hermiony (45+ słów) z trzema zdaniami z gdyby.", 45,
 ("Gdybym był…, …bym.", "Gdybym był…, …bym.", "Gdybym był…, …bym."))

T[20] = ("Прислівники: szybko → szybciej → najszybciej", "Przysłówki i stopniowanie", "Adverbs and comparison")
G[20] = [
 g("Harry latał ____ niż inni.", ["szybciej", "najszybciej", "szybki"],
   [("Так! Niż → вищий ступінь прислівника.", "Tak! Niż → stopień wyższy.", "Yes! Niż → comparative adverb."), ("Найвищий.", "Najwyższy.", "Superlative."), ("Прикметник.", "Przymiotnik.", "Adjective.")],
   ("szybko → szybciej → najszybciej.", "szybko → szybciej → najszybciej.", "szybko → szybciej → najszybciej.")),
 g("Hermiona ____ obserwowała Snape'a.", ["uważnie", "uważna", "uważny"],
   [("Так! Як? → прислівник.", "Tak! Jak? → przysłówek.", "Yes! How? → adverb."), ("Прикметник жін.", "Przymiotnik ż.", "Feminine adjective."), ("Прикметник чол.", "Przymiotnik m.", "Masculine adjective.")],
   ("Прислівник на -e/-o відповідає на «як?».", "Przysłówek na -e/-o: jak?", "Adverbs in -e/-o answer “how?”.")),
]
D[20] = ("Napisz relację z meczu (45+ słów). Użyj pięciu przysłówków: szybko, źle, nagle, uważnie, lepiej.", 45,
 ("Як? — прислівник.", "Jak? — przysłówek.", "How? — an adverb."))

T[21] = ("Непрямі питання і накази: zapytał, czy… / kazał, żeby…", "Pytania i polecenia zależne", "Reported questions and commands")
G[21] = [
 g("Ron zapytał, ____ przysłał pelerynę.", ["kto", "że", "żeby"],
   [("Так! Питання про особу → kto.", "Tak! Pytanie o osobę → kto.", "Yes! A question about a person → kto."), ("Że — для тверджень.", "Że — twierdzenia.", "Że is for statements."), ("Żeby — для наказів.", "Żeby — polecenia.", "Żeby is for commands.")],
   ("Zapytał, kto / czy / gdzie…", "Zapytał, kto / czy / gdzie…", "Zapytał, kto / czy / gdzie…")),
 g("Dumbledore kazał Harry'emu, ____ nie szukał lustra.", ["żeby", "że", "czy"],
   [("Так! Наказ → żeby + форма на -ł.", "Tak! Polecenie → żeby + forma na -ł.", "Yes! A command → żeby + -ł form."), ("Що — для тверджень.", "Że — twierdzenia.", "Że is for statements."), ("Czy — для питань.", "Czy — pytania.", "Czy is for questions.")],
   ("Kazać / prosić, żeby…", "Kazać / prosić, żeby…", "Kazać / prosić, żeby…")),
]
D[21] = ("Opisz Boże Narodzenie (45+ słów): Ron zapytał, czy…, kazał mi, żebym…", 45,
 ("Czy, kto, żeby.", "Czy, kto, żeby.", "Czy, kto, żeby."))

T[22] = ("Бажання: szkoda, że / gdyby tylko", "Życzenia: szkoda, że / gdyby tylko", "Wishes: szkoda, że / gdyby tylko")
G[22] = [
 g("Gdyby tylko moi rodzice ____ tutaj!", ["byli", "są", "będą"],
   [("Так! Gdyby tylko + форма на -li.", "Tak! Gdyby tylko + forma na -li.", "Yes! Gdyby tylko + -li form."), ("Реальність.", "Rzeczywistość.", "Reality."), ("Майбутнє.", "Przyszłość.", "Future.")],
   ("Gdyby tylko… — «якби ж…».", "Gdyby tylko… = gdybym mógł…", "Gdyby tylko… = if only…")),
 g("Szkoda, ____ nie mogę ich zobaczyć.", ["że", "żeby", "czy"],
   [("Так! Szkoda, że + звичайне речення.", "Tak! Szkoda, że + zdanie.", "Yes! Szkoda, że + a clause."), ("Żeby — мета.", "Żeby — cel.", "Żeby shows purpose."), ("Czy — питання.", "Czy — pytanie.", "Czy is a question.")],
   ("Szkoda, że… — жаль про реальність.", "Szkoda, że… — żal.", "Szkoda, że… — regret about reality.")),
]
D[22] = ("Jesteś Harrym. Napisz, co widzisz w lustrze (45+ słów). Użyj gdyby tylko i szkoda, że.", 45,
 ("Мінімум чотири бажання.", "Minimum cztery życzenia.", "At least four wishes."))

T[23] = ("Повторення арки 4", "Powtórka łuku 4", "Arc 4 review")
G[23] = [
 g("Hermiona lubi ____.", ["czytać", "czyta", "czytanie się"], [("Так.", "Tak.", "Yes."), ("Особова.", "Osobowa.", "Finite."), ("Помилка.", "Błąd.", "Wrong.")], ("Урок 18.", "Lekcja 18.", "Lesson 18.")),
 g("Gdybym był niewidzialny, ____ do biblioteki.", ["poszedłbym", "pójdę", "poszedłem"], [("Так.", "Tak.", "Yes."), ("Реальне.", "Realne.", "Real."), ("Минуле.", "Przeszłość.", "Past.")], ("Урок 19.", "Lekcja 19.", "Lesson 19.")),
 g("Harry złapał znicza ____.", ["szybko", "szybki", "szybka"], [("Так.", "Tak.", "Yes."), ("Прикметник.", "Przymiotnik.", "Adjective."), ("Прикметник.", "Przymiotnik.", "Adjective.")], ("Урок 20.", "Lekcja 20.", "Lesson 20.")),
 g("Filch zapytał, ____ tam jest.", ["kto", "że", "żeby"], [("Так.", "Tak.", "Yes."), ("Твердження.", "Twierdzenie.", "Statement."), ("Наказ.", "Polecenie.", "Command.")], ("Урок 21.", "Lekcja 21.", "Lesson 21.")),
 g("Gdyby tylko Ron ____ kapitanem!", ["był", "jest", "będzie"], [("Так.", "Tak.", "Yes."), ("Реальність.", "Rzeczywistość.", "Reality."), ("Майбутнє.", "Przyszłość.", "Future.")], ("Урок 22.", "Lekcja 22.", "Lesson 22.")),
]

T[24] = ("Пасив з модальними: może być użyty", "Strona bierna z modalnymi", "Passive with modals")
G[24] = [
 g("Kamień ____ ukryty w zamku.", ["został", "zostały", "została"],
   [("Так! Kamień — чол. → został.", "Tak! Kamień — m. → został.", "Yes! Kamień is masculine → został."), ("Множина.", "Mnoga.", "Plural."), ("Жін.", "Żeńska.", "Feminine.")],
   ("Zostać + imiesłów.", "Zostać + imiesłów.", "Zostać + participle.")),
 g("Kamień musi być ____.", ["chroniony", "chronić", "chroni"],
   [("Так! Musi być + дієприкметник.", "Tak! Musi być + imiesłów.", "Yes! Musi być + participle."), ("Інфінітив — активний.", "Bezokolicznik — strona czynna.", "Infinitive is active."), ("Особова форма.", "Forma osobowa.", "Finite form.")],
   ("Może / musi / powinien być + -ny/-ty.", "Może / musi być + -ny/-ty.", "Może / musi być + -ny/-ty.")),
]
D[24] = ("Napisz tajny liścik do przyjaciół o kamieniu (45+ słów). Użyj strony biernej: został ukryty, musi być chroniony.", 45,
 ("Три пасивні форми.", "Trzy formy bierne.", "Three passive forms."))

T[25] = ("Звички минулого і przyzwyczaić się do", "Nawyki: kiedyś + niedokonany, przyzwyczaić się do", "Past habits & przyzwyczaić się do")
G[25] = [
 g("Kiedyś Hagrid często ____ o smokach.", ["opowiadał", "opowiedział", "opowie"],
   [("Так! Повторювана звичка → недоконаний.", "Tak! Nawyk → niedokonany.", "Yes! A habit → imperfective."), ("Один раз.", "Jeden raz.", "Once."), ("Майбутнє.", "Przyszłość.", "Future.")],
   ("Kiedyś + недоконаний = used to.", "Kiedyś + niedokonany = nawyk.", "Kiedyś + imperfective = used to.")),
 g("Hagrid przyzwyczaił się do ____ zwierząt.", ["niebezpiecznych", "niebezpieczne", "niebezpiecznymi"],
   [("Так! Do + родовий.", "Tak! Do + dopełniacz.", "Yes! Do + genitive."), ("Знахідний.", "Biernik.", "Accusative."), ("Орудний.", "Narzędnik.", "Instrumental.")],
   ("Przyzwyczaić się do + родовий.", "Przyzwyczaić się do + dopełniacz.", "Przyzwyczaić się do + genitive.")),
]
D[25] = ("Napisz list Hagrida do Charliego o Norbercie (45+ słów): kiedyś…, przyzwyczaiłem się do…", 45,
 ("Недоконаний + do + родовий.", "Niedokonany + do + dopełniacz.", "Imperfective + do + genitive."))

T[26] = ("Нереальне минуле: gdyby nie…", "Nierealna przeszłość: gdyby nie…", "Unreal past: gdyby nie…")
G[26] = [
 g("Gdyby Malfoy nie zobaczył smoka, nie ____ nas.", ["złapaliby", "złapią", "złapali"],
   [("Так! Gdyby + …, -by.", "Tak! Gdyby + …, -by.", "Yes! Gdyby + …, -by."), ("Майбутнє.", "Przyszłość.", "Future."), ("Без умовності.", "Bez trybu.", "No conditional.")],
   ("У польській одна форма для нереального теперішнього і минулого.", "Jedna forma dla nierealnej teraźniejszości i przeszłości.", "Polish uses one form for unreal present and past.")),
 g("Gdyby Neville ____ w łóżku, nie dostałby szlabanu.", ["został", "zostanie", "zostaje"],
   [("Так! Gdyby + форма на -ł.", "Tak! Gdyby + forma na -ł.", "Yes! Gdyby + -ł form."), ("Майбутнє.", "Przyszłość.", "Future."), ("Теперішній.", "Teraźniejszy.", "Present.")],
   ("Gdyby + -ł, …-by.", "Gdyby + -ł, …-by.", "Gdyby + -ł, …-by.")),
]
D[26] = ("Napisz w pamiętniku o tamtej nocy (45+ słów). Trzy zdania z gdyby nie…", 45,
 ("Gdyby nie…", "Gdyby nie…", "Gdyby nie…"))

T[27] = ("Który у відмінках", "Który w przypadkach", "Który in different cases")
G[27] = [
 g("Las, ____ nie wolno wchodzić, jest pełen stworzeń.", ["do którego", "który", "którym"],
   [("Так! Wchodzić do + родовий.", "Tak! Wchodzić do + dopełniacz.", "Yes! Wchodzić do + genitive."), ("Називний — помилка.", "Mianownik — błąd.", "Nominative is wrong."), ("Без прийменника — помилка.", "Bez przyimka — błąd.", "Missing the preposition.")],
   ("Прийменник + który у потрібному відмінку.", "Przyimek + który w odpowiednim przypadku.", "Preposition + który in the right case.")),
 g("Hagrid, ____ niósł latarnię, prowadził grupę.", ["który", "którego", "którym"],
   [("Так! Підмет → називний.", "Tak! Podmiot → mianownik.", "Yes! Subject → nominative."), ("Знахідний.", "Biernik.", "Accusative."), ("Орудний.", "Narzędnik.", "Instrumental.")],
   ("Додаткова інформація — між комами.", "Informacja dodatkowa — w przecinkach.", "Extra information goes between commas.")),
]
D[27] = ("Opisz noc w lesie (45+ słów). Użyj który w różnych przypadkach: którego, w którym, z którym.", 45,
 ("Три відмінки.", "Trzy przypadki.", "Three cases."))

T[28] = ("Висновки про минуле: musiał / mógł / nie mógł", "Przypuszczenia o przeszłości: musiał / mógł / nie mógł", "Past deduction: musiał / mógł / nie mógł")
G[28] = [
 g("Postać w lesie ____ być Voldemortem.", ["musiała", "nie mogła", "powinna"],
   [("Так! Упевнений висновок.", "Tak! Pewny wniosek.", "Yes! A confident deduction."), ("Протилежне.", "Odwrotnie.", "Opposite."), ("Повинна — обов'язок.", "Powinna — powinność.", "Powinna = should.")],
   ("Musiał być — точно; mógł być — можливо; nie mógł być — точно ні.", "Musiał / mógł / nie mógł być.", "Musiał = must have; mógł = might have; nie mógł = can't have.")),
 g("Nieznajomy nie ____ być zwykłym człowiekiem.", ["mógł", "musiał", "chciał"],
   [("Так! Nie mógł = точно ні.", "Tak! Nie mógł = na pewno nie.", "Yes! Nie mógł = can't have."), ("Nie musiał — «не мусив».", "Nie musiał — brak konieczności.", "Nie musiał = didn't have to."), ("Не про бажання.", "Nie o chęć.", "Not about wanting.")],
   ("Nie mógł ≠ nie musiał!", "Nie mógł ≠ nie musiał!", "Nie mógł ≠ nie musiał!")),
]
D[28] = ("Napisz notatki Hermiony o zagadce (45+ słów): musiał, mógł, nie mógł.", 45,
 ("Три висновки.", "Trzy wnioski.", "Three deductions."))

T[29] = ("Повторення арки 5", "Powtórka łuku 5", "Arc 5 review")
G[29] = [
 g("Kamień został ____ w zamku.", ["ukryty", "ukryć", "ukrywa"], [("Так.", "Tak.", "Yes."), ("Інфінітив.", "Bezokolicznik.", "Infinitive."), ("Особова.", "Osobowa.", "Finite.")], ("Урок 24.", "Lekcja 24.", "Lesson 24.")),
 g("Hagrid przyzwyczaił się do ____.", ["smoków", "smoki", "smokami"], [("Так.", "Tak.", "Yes."), ("Знахідний.", "Biernik.", "Accusative."), ("Орудний.", "Narzędnik.", "Instrumental.")], ("Урок 25.", "Lekcja 25.", "Lesson 25.")),
 g("Gdyby Malfoy nie doniósł, nie ____ punktów.", ["stracilibyśmy", "stracimy", "straciliśmy"], [("Так.", "Tak.", "Yes."), ("Майбутнє.", "Przyszłość.", "Future."), ("Реальне.", "Realne.", "Real.")], ("Урок 26.", "Lekcja 26.", "Lesson 26.")),
 g("Firenzo, ____ uratował Harry'ego, jest centaurem.", ["który", "którego", "którym"], [("Так.", "Tak.", "Yes."), ("Знахідний.", "Biernik.", "Accusative."), ("Орудний.", "Narzędnik.", "Instrumental.")], ("Урок 27.", "Lekcja 27.", "Lesson 27.")),
 g("Nieznajomy ____ chcieć kamienia.", ["musiał", "nie musiał", "nie mógł"], [("Так.", "Tak.", "Yes."), ("Не мусив.", "Brak konieczności.", "Didn't have to."), ("Протилежне.", "Odwrotnie.", "Opposite.")], ("Урок 28.", "Lekcja 28.", "Lesson 28.")),
]

T[30] = ("Поради: powinieneś / lepiej / наказовий", "Rady: powinieneś / lepiej / tryb rozkazujący", "Advice: powinieneś / lepiej / imperative")
G[30] = [
 g("Ron, ____ się! Musisz się rozluźnić!", ["uspokój", "uspokoić", "uspokajasz"],
   [("Так! Наказовий спосіб.", "Tak! Tryb rozkazujący.", "Yes! Imperative."), ("Інфінітив.", "Bezokolicznik.", "Infinitive."), ("Теперішній.", "Teraźniejszy.", "Present.")],
   ("Наказовий: uspokój się, zrób, idź.", "Tryb rozkazujący: uspokój się, zrób, idź.", "Imperative: uspokój się, zrób, idź.")),
 g("Neville: „____ powiedzieć nauczycielowi!”", ["Powinieneś", "Powinna", "Powinniśmy był"],
   [("Так! Порада для «ти» (чол.).", "Tak! Rada dla „ty” (m.).", "Yes! Advice to “you” (male)."), ("Жін., 3 особа.", "Ż., 3 osoba.", "Feminine 3rd person."), ("Неіснуюча форма.", "Forma nie istnieje.", "Doesn't exist.")],
   ("Powinieneś / powinnaś + інфінітив.", "Powinieneś / powinnaś + bezokolicznik.", "Powinieneś / powinnaś + infinitive.")),
]
D[30] = ("Napisz rady dla kogoś, kto idzie przez klapę (45+ słów): tryb rozkazujący, powinieneś, lepiej.", 45,
 ("Мінімум п'ять порад.", "Minimum pięć rad.", "At least five tips."))

T[31] = ("Змішані умовні: gdyby nie…, nie byłby teraz…", "Mieszane warunki: gdyby nie…, nie byłby teraz…", "Mixed conditionals")
G[31] = [
 g("Gdyby Ron się nie poświęcił, Harry nie ____ teraz tutaj.", ["byłby", "będzie", "był"],
   [("Так! Наслідок зараз → byłby teraz.", "Tak! Skutek teraz → byłby teraz.", "Yes! Present result → byłby teraz."), ("Майбутнє.", "Przyszłość.", "Future."), ("Минуле без -by.", "Przeszły bez -by.", "Past without -by.")],
   ("Teraz / wtedy показують час наслідку.", "Teraz / wtedy pokazują czas skutku.", "Teraz / wtedy show when the result is.")),
 g("Gdyby Ron nie grał tak dobrze w szachy, nie ____ wtedy przez szachownicę.", ["przeszlibyśmy", "przejdziemy", "przeszliśmy"],
   [("Так!", "Tak!", "Yes!"), ("Майбутнє.", "Przyszłość.", "Future."), ("Реальне.", "Realne.", "Real.")],
   ("Gdyby + -ł, …-by.", "Gdyby + -ł, …-by.", "Gdyby + -ł, …-by.")),
]
D[31] = ("Napisz list Hermiony do Rona w skrzydle szpitalnym (45+ słów). Trzy zdania z gdyby.", 45,
 ("Gdyby nie ty…", "Gdyby nie ty…", "Gdyby nie ty…"))

T[32] = ("Наголос: to właśnie… / to… był", "Wyróżnianie: to właśnie… / to… był", "Emphasis: to właśnie… / to… był")
G[32] = [
 g("To ____ Quirrell wpuścił trolla, nie Snape.", ["właśnie", "chyba nie", "nigdy"],
   [("Так! To właśnie — підсилення.", "Tak! To właśnie — wyróżnienie.", "Yes! To właśnie adds emphasis."), ("Заперечення.", "Przeczenie.", "Negation."), ("Неправильний сенс.", "Zły sens.", "Wrong meaning.")],
   ("To właśnie X… = саме X…", "To właśnie X… = to X, a nie ktoś inny.", "To właśnie X… = it was X who…")),
 g("To nie Snape ____ wrogiem, tylko Quirrell.", ["był", "była", "byli"],
   [("Так! Snape → był.", "Tak! Snape → był.", "Yes! Snape → był."), ("Жін.", "Ż.", "Feminine."), ("Мн.", "Mnoga.", "Plural.")],
   ("To nie X…, tylko Y.", "To nie X…, tylko Y.", "To nie X…, tylko Y.")),
]
D[32] = ("Wyjaśnij przyjaciołom prawdę (45+ słów): to nie Snape…, to właśnie Quirrell…", 45,
 ("To właśnie / to nie…, tylko…", "To właśnie / to nie…, tylko…", "To właśnie / to nie…, tylko…"))

T[33] = ("Жаль: powinienem był / mogłem / nie musiałem", "Żal: powinienem był / mogłem / nie musiałem", "Regret: powinienem był / mogłem / nie musiałem")
G[33] = [
 g("Harry: „____ komuś powiedzieć!”", ["Powinienem był", "Powinienem będę", "Powinien był"],
   [("Так! Powinienem był = треба було.", "Tak! Powinienem był = żal.", "Yes! Powinienem był = should have."), ("Неіснуюча форма.", "Forma nie istnieje.", "Doesn't exist."), ("3 особа.", "3 osoba.", "Third person.")],
   ("Powinienem był / powinnam była + інфінітив.", "Powinienem był + bezokolicznik.", "Powinienem był + infinitive.")),
 g("Hagrid: „Nie ____ mówić nieznajomemu o Puszku!”", ["powinienem był", "musiałem", "mogę"],
   [("Так! Жаль.", "Tak! Żal.", "Yes! Regret."), ("Обов'язок.", "Konieczność.", "Obligation."), ("Теперішній.", "Teraźniejszy.", "Present.")],
   ("Nie powinienem był… = не треба було.", "Nie powinienem był… = żal.", "Nie powinienem był… = shouldn't have.")),
]
D[33] = ("Napisz list Harry'ego do Hagrida (45+ słów): powinienem był, mogłem, nie musiałeś.", 45,
 ("Три форми жалю.", "Trzy formy żalu.", "Three forms of regret."))

T[34] = ("Розповідь: вид у минулому", "Narracja: aspekt w przeszłości", "Narrative: aspect in the past")
G[34] = [
 g("Kiedy Dumbledore ____ punkty, wszyscy wiwatowali.", ["ogłaszał", "ogłosi", "ogłasza"],
   [("Так! Тло → недоконаний.", "Tak! Tło → niedokonany.", "Yes! Background → imperfective."), ("Майбутнє.", "Przyszłość.", "Future."), ("Теперішній.", "Teraźniejszy.", "Present.")],
   ("Недоконаний — тло, доконаний — подія.", "Niedokonany — tło, dokonany — zdarzenie.", "Imperfective = background, perfective = event.")),
 g("Gryffindor ____ puchar dzięki Neville'owi.", ["wygrał", "wygrywał", "wygra"],
   [("Так! Подія з результатом → доконаний.", "Tak! Zdarzenie → dokonany.", "Yes! An event with a result → perfective."), ("Процес.", "Proces.", "Process."), ("Майбутнє.", "Przyszłość.", "Future.")],
   ("Результат → доконаний.", "Rezultat → dokonany.", "Result → perfective.")),
]
D[34] = ("Opowiedz historię pierwszego roku Harry'ego (60+ słów), mieszając aspekt dokonany i niedokonany.", 60,
 ("Тло + події.", "Tło + zdarzenia.", "Background + events."))

T[35] = ("Повторення арки 6", "Powtórka łuku 6", "Arc 6 review")
G[35] = [
 g("____ się, Ron!", ["Uspokój", "Uspokoić", "Uspokaja"], [("Так.", "Tak.", "Yes."), ("Інфінітив.", "Bezokolicznik.", "Infinitive."), ("Теперішній.", "Teraźniejszy.", "Present.")], ("Урок 30.", "Lekcja 30.", "Lesson 30.")),
 g("Gdyby nie Ron, Harry nie ____ teraz w zamku.", ["byłby", "będzie", "był"], [("Так.", "Tak.", "Yes."), ("Майбутнє.", "Przyszłość.", "Future."), ("Реальне.", "Realne.", "Real.")], ("Урок 31.", "Lekcja 31.", "Lesson 31.")),
 g("To ____ Quirrell chciał kamienia.", ["właśnie", "nigdy", "chyba nie"], [("Так.", "Tak.", "Yes."), ("Ні.", "Nie.", "No."), ("Ні.", "Nie.", "No.")], ("Урок 32.", "Lekcja 32.", "Lesson 32.")),
 g("Nie ____ mu mówić!", ["powinienem był", "muszę", "mogę"], [("Так.", "Tak.", "Yes."), ("Теперішнє.", "Teraźniejsze.", "Present."), ("Теперішнє.", "Teraźniejsze.", "Present.")], ("Урок 33.", "Lekcja 33.", "Lesson 33.")),
]

T[36] = ("Уся граматика курсу", "Cała gramatyka kursu", "All the course grammar")
G[36] = G[5][:2] + G[11][:2] + G[17][:2] + G[23][:2] + G[29][:2] + G[35][:2]
D[36] = ("Napisz list do przyszłego pierwszoroczniaka (70+ słów). Daj rady, opowiedz o swoim roku i napisz, czego żałujesz.", 70,
 ("Мінімум п'ять тем курсу.", "Co najmniej pięć tematów kursu.", "At least five course topics."))
