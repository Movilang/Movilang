# Wersja kursu „Auta” dla uczących się POLSKIEGO (A1).
G = {}
D = {}
T = {}
def W(*s): return [tuple(x.split("|")) for x in s]
def P(s): return tuple(s.split("|"))
def g(q, opts, whys, tip): return (q, opts, 0, W(*whys), P(tip))
def d(q, n, tip): return (q, n, P(tip + "|" + tip + "|" + tip))

# ---- Łuk 1
T[1] = P("Być: jestem / jesteś / jest|Być: jestem / jesteś / jest|To be: jestem / jesteś / jest")
G[1] = [
 g("Zygzak: „____ szybki! Jestem gwiazdą!”", ["Jestem", "Jest", "Są"],
   ["Так! Я → jestem.|Tak! Ja → jestem.|Yes! I → jestem.", "Jest — він/вона.|„Jest” — on/ona.|Jest is he/she.", "Są — вони.|„Są” — oni.|Są is they."],
   "Ja jestem, ty jesteś, on jest, my jesteśmy, wy jesteście, oni są.|Ja jestem, ty jesteś, on jest, my jesteśmy, wy jesteście, oni są.|Ja jestem, ty jesteś, on jest, my jesteśmy, wy jesteście, oni są."),
 g("Fani: „My ____ twoimi fanami!”", ["jesteśmy", "jesteście", "jest"],
   ["Так! Ми → jesteśmy.|Tak! My → jesteśmy.|Yes! We → jesteśmy.", "Jesteście — ви.|„Jesteście” — wy.|Jesteście is you (plural).", "Jest — він.|„Jest” — on.|Jest is he."],
   "Після być — орудний: jestem gwiazdą.|Po być — narzędnik: jestem gwiazdą.|After być use the instrumental: jestem gwiazdą."),
]
D[1] = d("Napisz o sobie (30+ słów). Kim jesteś? Ile masz lat? Skąd jesteś? Jaki jesteś?", 30, "Jestem… Mam … lat. Jestem z… Jestem…")

T[2] = P("Przeczenie i pytanie: nie jestem / czy jesteś?|Przeczenie i pytanie: nie jestem / czy jesteś?|Negatives and questions: nie jestem / czy jesteś?")
G[2] = [
 g("Zygzak: „Nie ____ zmęczony!”", ["jestem", "jest", "jesteś"],
   ["Так! Nie + jestem.|Tak! Nie + jestem.|Yes! Nie + jestem.", "Jest — він.|„Jest” — on.|Jest is he.", "Jesteś — ти.|„Jesteś” — ty.|Jesteś is you."],
   "Заперечення: nie + дієслово.|Przeczenie: nie + czasownik.|Negative: nie + verb."),
 g("Maniek: „____ jesteś gotowy, młody?”", ["Czy", "Co", "Nie"],
   ["Так! Питання так/ні → czy.|Tak! Pytanie tak/nie → czy.|Yes! Yes/no question → czy.", "Co — що.|„Co” = what.|Co means what.", "Nie — заперечення.|„Nie” — przeczenie.|Nie is negative."],
   "Czy + речення = питання.|Czy + zdanie = pytanie.|Czy + sentence = a question."),
]
D[2] = d("Napisz 3 zdania „nie jestem” i 3 pytania „czy jesteś…?” (30+ słów).", 30, "Nie jestem… Czy jesteś…? Tak, jestem. / Nie, nie jestem.")

T[3] = P("Mój / twój / jego|Mój / twój / jego|Possessives: mój / twój / jego")
G[3] = [
 g("Zygzak: „To ____ przyczepa!”", ["moja", "mój", "moje"],
   ["Так! Przyczepa — жін. рід → moja.|Tak! Przyczepa — r. żeński → moja.|Yes! Feminine → moja.", "Mój — чол. рід.|„Mój” — męski.|Mój is masculine.", "Moje — сер. рід.|„Moje” — nijaki.|Moje is neuter."],
   "mój (on) · moja (ona) · moje (ono).|mój · moja · moje.|mój (m) · moja (f) · moje (n)."),
 g("To jest Maniek. To ____ ciężarówka.", ["jego", "jej", "mój"],
   ["Так! Maniek → він → jego.|Tak! Maniek → on → jego.|Yes! He → jego.", "Jej — її.|„Jej” — ona.|Jej is her.", "Mój — мій.|„Mój” — ja.|Mój is my."],
   "jego / jej не змінюються.|jego / jej się nie odmieniają.|jego / jej don't change."),
]
D[3] = d("Opisz swoje rzeczy (30+ słów): mój telefon, moja torba, moje łóżko…", 30, "To jest mój… Moja… jest… Moje…")

T[4] = P("Ten / ta / to · liczba mnoga|Ten / ta / to · liczba mnoga|This / that: ten / ta / to + plurals")
G[4] = [
 g("Zygzak: „____ puchar jest mój!”", ["Ten", "Ta", "To"],
   ["Так! Puchar — чол. рід → ten.|Tak! Puchar — męski → ten.|Yes! Masculine → ten.", "Ta — жін. рід.|„Ta” — żeński.|Ta is feminine.", "To — сер. рід.|„To” — nijaki.|To is neuter."],
   "ten (m) · ta (f) · to (n) · te (мн.)|ten · ta · to · te|ten · ta · to · te (plural)"),
 g("Te ____ są szybkie.", ["auta", "auto", "aut"],
   ["Так! Множина: auta.|Tak! L. mnoga: auta.|Yes! Plural: auta.", "Auto — однина.|„Auto” — l. poj.|Auto is singular.", "Aut — родовий.|„Aut” — dopełniacz.|Aut is genitive."],
   "auto → auta, opona → opony.|auto → auta, opona → opony.|auto → auta, opona → opony."),
]
D[4] = d("Opisz swój pokój (30+ słów): ten stół, ta lampa, te książki…", 30, "Ten… jest… Ta… jest… Te… są…")

T[5] = P("Mieć: mam / masz / ma|Mieć: mam / masz / ma|Have got: mam / masz / ma")
G[5] = [
 g("Zygzak: „____ nowego sponsora!”", ["Mam", "Ma", "Mamy"],
   ["Так! Я → mam.|Tak! Ja → mam.|Yes! I → mam.", "Ma — він.|„Ma” — on.|Ma is he.", "Mamy — ми.|„Mamy” — my.|Mamy is we."],
   "mam, masz, ma, mamy, macie, mają.|mam, masz, ma, mamy, macie, mają.|mam, masz, ma, mamy, macie, mają."),
 g("Zygzak nie ma ____.", ["przyjaciół", "przyjaciele", "przyjaciel"],
   ["Так! Після nie ma → родовий.|Tak! Po nie ma → dopełniacz.|Yes! After nie ma → genitive.", "Називний — ні.|Mianownik — nie.|Not nominative.", "Однина, називний.|L. poj., mianownik.|Singular nominative."],
   "Nie mam + dopełniacz: nie mam czasu.|Nie mam + dopełniacz: nie mam czasu.|Nie mam + genitive: nie mam czasu."),
]
D[5] = d("Co masz? (30+ słów). Mam… Nie mam… Mój przyjaciel ma…", 30, "Mam… Nie mam… Mój przyjaciel ma…")

# ---- Łuk 2
T[7] = P("Jest / są (there is / are)|Jest / są|There is / are: jest / są")
G[7] = [
 g("W miasteczku ____ kawiarnia.", ["jest", "są", "ma"],
   ["Так! Одна річ → jest.|Tak! Jedna rzecz → jest.|Yes! One thing → jest.", "Są — кілька.|„Są” — kilka.|Są is for many.", "Ma — мати.|„Ma” — mieć.|Ma means has."],
   "Jest + однина · są + множина.|Jest + l. poj. · są + l. mnoga.|Jest + singular · są + plural."),
 g("Tu ____ dwa sklepy.", ["są", "jest", "jestem"],
   ["Так! Кілька → są.|Tak! Kilka → są.|Yes! Many → są.", "Jest — одне.|„Jest” — jedno.|Jest is one.", "Jestem — я.|„Jestem” — ja.|Jestem is I."],
   "Tu jest… / Tu są…|Tu jest… / Tu są…|Tu jest… / Tu są…"),
]
D[7] = d("Opisz swoje miasto (30+ słów): Jest… Są… Nie ma…", 30, "W moim mieście jest… Są… Nie ma…")

T[8] = P("W / na / pod / obok|W / na / pod / obok|Prepositions: w / na / pod / obok")
G[8] = [
 g("Zygzak jest ____ parkingu.", ["na", "pod", "obok"],
   ["Так! Na parkingu.|Tak! Na parkingu.|Yes! Na parkingu.", "Pod — під.|„Pod” = under.|Pod = under.", "Obok — поруч.|„Obok” = next to.|Obok = next to."],
   "w / na + miejscownik: w sklepie, na drodze.|w / na + miejscownik.|w / na + locative."),
 g("Złomek śpi ____ znakiem.", ["pod", "na", "w"],
   ["Так! Pod + орудний.|Tak! Pod + narzędnik.|Yes! Pod + instrumental.", "Na — на.|„Na” = on.|Na = on.", "W — в.|„W” = in.|W = in."],
   "pod / nad / obok.|pod / nad / obok.|pod (under) / nad (above) / obok (next to)."),
]
D[8] = d("Gdzie są twoje rzeczy? (30+ słów): Telefon jest na stole. Kot jest pod łóżkiem.", 30, "…jest na… …jest pod… …jest obok…")

T[9] = P("Tryb rozkazujący: jedź! stój!|Tryb rozkazujący: jedź! stój!|Imperatives: jedź! stój!")
G[9] = [
 g("Szeryf: „____!” — Zygzak musi się zatrzymać.", ["Stój", "Stoję", "Stoi"],
   ["Так! Наказ → stój!|Tak! Rozkaz → stój!|Yes! Command → stój!", "Stoję — я стою.|„Stoję” = I stand.|Stoję = I stand.", "Stoi — він стоїть.|„Stoi” = he stands.|Stoi = he stands."],
   "Rozkaz: jedź! stój! patrz!|Rozkaz: jedź! stój! patrz!|Command: jedź! stój! patrz!"),
 g("Doc: „Nie ____ tak szybko!”", ["jedź", "jedzie", "jadę"],
   ["Так! Nie + jedź.|Tak! Nie + jedź.|Yes! Nie + jedź.", "Jedzie — він.|„Jedzie” — on.|Jedzie is he.", "Jadę — я.|„Jadę” — ja.|Jadę is I."],
   "Chodźmy! / Jedźmy! = Let's go!|Chodźmy! / Jedźmy!|Chodźmy! / Jedźmy! = Let's go!"),
]
D[9] = d("Zasady w twoim domu (30+ słów): Myj ręce! Nie biegaj! Chodźmy…", 30, "Myj… Nie… Zawsze… Chodźmy…")

T[10] = P("Umiem / mogę|Umiem / mogę|Can: umiem / mogę")
G[10] = [
 g("Złomek ____ jeździć do tyłu.", ["umie", "umiem", "umiesz"],
   ["Так! Він → umie.|Tak! On → umie.|Yes! He → umie.", "Umiem — я.|„Umiem” — ja.|Umiem is I.", "Umiesz — ти.|„Umiesz” — ty.|Umiesz is you."],
   "Umieć + bezokolicznik.|Umieć + bezokolicznik.|Umieć + infinitive."),
 g("Zygzak: „Nie ____ jechać, Bessie jest ciężka!”", ["mogę", "może", "możesz"],
   ["Так! Я → mogę.|Tak! Ja → mogę.|Yes! I → mogę.", "Może — він.|„Może” — on.|Może is he.", "Możesz — ти.|„Możesz” — ty.|Możesz is you."],
   "umiem = вмію · mogę = можу.|umiem = skill · mogę = possibility.|umiem = know how · mogę = be able."),
]
D[10] = d("Co umiesz robić? (30+ słów): Umiem… Nie umiem… Mogę…", 30, "Umiem… Nie umiem… Mogę…")

T[11] = P("Czas teraźniejszy: pracuję / pracuje|Czas teraźniejszy|Present tense: pracuję / pracuje")
G[11] = [
 g("Złomek ____ na złomowisku.", ["mieszka", "mieszkam", "mieszkają"],
   ["Так! Він → mieszka.|Tak! On → mieszka.|Yes! He → mieszka.", "Mieszkam — я.|„Mieszkam” — ja.|Mieszkam is I.", "Mieszkają — вони.|„Mieszkają” — oni.|Mieszkają is they."],
   "mieszkam, mieszkasz, mieszka…|mieszkam, mieszkasz, mieszka…|mieszkam, mieszkasz, mieszka…"),
 g("Codziennie ____ auta.", ["holuję", "holuje", "holujesz"],
   ["Так! Я → holuję.|Tak! Ja → holuję.|Yes! I → holuję.", "Holuje — він.|„Holuje” — on.|Holuje is he.", "Holujesz — ти.|„Holujesz” — ty.|Holujesz is you."],
   "Закінчення показує особу.|Końcówka pokazuje osobę.|The ending shows the person."),
]
D[11] = d("Twój dzień (30+ słów): Wstaję o… Jem… Idę do…", 30, "Wstaję… Jem… Idę… Wracam…")

# ---- Łuk 3
T[13] = P("Pytania: czy? / nie + czasownik|Pytania i przeczenia|Questions and negatives")
G[13] = [
 g("Sally: „____ lubisz mój motel?” — „Tak!”", ["Czy", "Gdzie", "Nie"],
   ["Так! Так/ні → czy.|Tak! Tak/nie → czy.|Yes! Yes/no → czy.", "Gdzie — де.|„Gdzie” = where.|Gdzie = where.", "Nie — заперечення.|„Nie” — przeczenie.|Nie is negative."],
   "Czy + zdanie?|Czy + zdanie?|Czy + sentence?"),
 g("Zygzak nie ____ tu mieszkać.", ["chce", "chcę", "chcesz"],
   ["Так! Він → nie chce.|Tak! On → nie chce.|Yes! He → nie chce.", "Chcę — я.|„Chcę” — ja.|Chcę is I.", "Chcesz — ти.|„Chcesz” — ty.|Chcesz is you."],
   "nie стоїть перед дієсловом.|nie przed czasownikiem.|nie goes before the verb."),
]
D[13] = d("Zadaj przyjacielowi 5 pytań z „czy” i odpowiedz (30+ słów).", 30, "Czy lubisz…? Tak, lubię. Czy masz…? Nie, nie mam.")

T[14] = P("Zawsze / często / nigdy|Zawsze / często / nigdy|Frequency: zawsze / często / nigdy")
G[14] = [
 g("Sierżant ____ wstaje wcześnie.", ["zawsze", "nigdy nie", "wczoraj"],
   ["Так! Zawsze = завжди.|Tak! Zawsze = always.|Yes! Zawsze = always.", "Сардж рано встає.|Sierżant wstaje wcześnie.|He does get up early.", "Wczoraj — минуле.|„Wczoraj” — przeszłość.|Wczoraj is past."],
   "zawsze · często · czasem · rzadko · nigdy.|zawsze · często · czasem · rzadko · nigdy.|always · often · sometimes · rarely · never."),
 g("Fillmore ____ pije zwykłego paliwa.", ["nigdy nie", "nigdy", "zawsze nie"],
   ["Так! Nigdy + nie (подвійне заперечення).|Tak! Nigdy + nie.|Yes! Nigdy + nie (double negative).", "Бракує nie.|Brakuje nie.|Nie is missing.", "Так не кажуть.|Tak się nie mówi.|Not Polish."],
   "У польській: nigdy nie…|Po polsku: nigdy nie…|Polish: nigdy nie…"),
]
D[14] = d("Jak często? (30+ słów): Zawsze… Często… Czasem… Nigdy nie…", 30, "Zawsze… Często… Czasem… Nigdy nie…")

T[15] = P("Kto? Co? Gdzie? Kiedy? Dlaczego?|Słowa pytające|Question words: kto / co / gdzie")
G[15] = [
 g("„____ jest Doc?” — „Jest w garażu.”", ["Gdzie", "Kto", "Kiedy"],
   ["Так! Місце → gdzie.|Tak! Miejsce → gdzie.|Yes! Place → gdzie.", "Kto — хто.|„Kto” = who.|Kto = who.", "Kiedy — коли.|„Kiedy” = when.|Kiedy = when."],
   "kto · co · gdzie · kiedy · dlaczego · jak.|kto · co · gdzie · kiedy · dlaczego · jak.|who · what · where · when · why · how."),
 g("„____ jedziesz tak szybko?” — „Bo chcę wygrać.”", ["Dlaczego", "Gdzie", "Co"],
   ["Так! Причина → dlaczego.|Tak! Przyczyna → dlaczego.|Yes! Reason → dlaczego.", "Gdzie — місце.|„Gdzie” — miejsce.|Gdzie is place.", "Co — що.|„Co” = what.|Co = what."],
   "Dlaczego…? — Bo…|Dlaczego…? — Bo…|Dlaczego…? — Bo…"),
]
D[15] = d("Wywiad z bohaterem filmu: 6 pytań (kto, co, gdzie, kiedy, dlaczego, jak) i odpowiedzi (30+ słów).", 30, "Kto…? Gdzie…? Dlaczego…? Bo…")

T[16] = P("Lubię / kocham / nie znoszę + bezokolicznik|Lubię + bezokolicznik|Like / love / hate + infinitive")
G[16] = [
 g("Złomek ____ jeździć do tyłu.", ["lubi", "lubię", "lubią"],
   ["Так! Він → lubi.|Tak! On → lubi.|Yes! He → lubi.", "Lubię — я.|„Lubię” — ja.|Lubię is I.", "Lubią — вони.|„Lubią” — oni.|Lubią is they."],
   "Lubić + bezokolicznik: lubię pływać.|Lubić + bezokolicznik.|Lubić + infinitive."),
 g("Zygzak nie lubi ____.", ["czekać", "czeka", "czekam"],
   ["Так! Після lubi — інфінітив.|Tak! Po lubi — bezokolicznik.|Yes! Infinitive after lubi.", "Czeka — він чекає.|„Czeka” — forma osobowa.|Czeka is conjugated.", "Czekam — я.|„Czekam” — ja.|Czekam is I."],
   "Bezokolicznik: -ć: czekać, jechać, spać.|Bezokolicznik kończy się na -ć.|Infinitive ends in -ć."),
]
D[16] = d("Co lubisz robić? (30+ słów): Lubię… Uwielbiam… Nie lubię…", 30, "Lubię… Uwielbiam… Nie znoszę…")

T[17] = P("Teraz: właśnie robię|Teraz: właśnie robię|Present Continuous in Polish: teraz robię")
G[17] = [
 g("Patrz! Zygzak ____ drogę.", ["naprawia", "naprawiam", "naprawiał"],
   ["Так! Зараз → naprawia.|Tak! Teraz → naprawia.|Yes! Now → naprawia.", "Naprawiam — я.|„Naprawiam” — ja.|Naprawiam is I.", "Naprawiał — минуле.|„Naprawiał” — przeszłość.|Naprawiał is past."],
   "У польській немає -ing: teraz + звичайний теп. час.|Po polsku nie ma -ing: teraz + czas teraźniejszy.|Polish has no -ing: teraz + present tense."),
 g("Co teraz ____ ?", ["robisz", "robię", "robi się"],
   ["Так! Ти → robisz.|Tak! Ty → robisz.|Yes! You → robisz.", "Robię — я.|„Robię” — ja.|Robię is I.", "Не те значення.|Inne znaczenie.|Different meaning."],
   "Co robisz? — Jem. / Czytam.|Co robisz? — Jem.|Co robisz? — Jem."),
]
D[17] = d("Co teraz robią ludzie wokół ciebie? (30+ słów): Mama gotuje. Brat gra…", 30, "Teraz… Mama… Ja…")

# ---- Łuk 4
T[19] = P("Codziennie vs teraz|Codziennie vs teraz|Every day vs now")
G[19] = [
 g("Doc codziennie ____ w garażu, ale teraz jest na torze.", ["pracuje", "pracował", "pracować"],
   ["Так! Звичка → теп. час.|Tak! Nawyk → teraźniejszy.|Yes! Habit → present.", "Pracował — минуле.|„Pracował” — przeszłość.|Pracował is past.", "Інфінітив.|Bezokolicznik.|Infinitive."],
   "У польській обидва — теп. час.|Po polsku oba — czas teraźniejszy.|Polish uses the present for both."),
 g("____ Zygzak jedzie po torze.", ["Teraz", "Codziennie zawsze", "Wczoraj"],
   ["Так! Teraz = зараз.|Tak! Teraz = now.|Yes! Teraz = now.", "Зайве.|Zbędne.|Extra word.", "Wczoraj — минуле.|„Wczoraj” — przeszłość.|Wczoraj is past."],
   "codziennie (звичка) · teraz (зараз).|codziennie · teraz.|codziennie (habit) · teraz (now)."),
]
D[19] = d("Twój zwykły dzień i co robisz teraz (30+ słów).", 30, "Codziennie… Zwykle… Ale teraz…")

T[20] = P("Trochę / kilka + dopełniacz|Trochę / kilka + dopełniacz|Some / any: trochę + genitive")
G[20] = [
 g("Flo: „Chcesz trochę ____?”", ["paliwa", "paliwo", "paliwem"],
   ["Так! Trochę + родовий.|Tak! Trochę + dopełniacz.|Yes! Trochę + genitive.", "Називний.|Mianownik.|Nominative.", "Орудний.|Narzędnik.|Instrumental."],
   "trochę wody, trochę paliwa.|trochę wody, trochę paliwa.|trochę wody, trochę paliwa."),
 g("Nie ma ____ opon.", ["żadnych", "jakieś", "trochę"],
   ["Так! Nie ma żadnych = немає жодних.|Tak! Nie ma żadnych.|Yes! Nie ma żadnych = no… at all.", "Jakieś — у ствердженні.|„Jakieś” — w twierdzeniu.|Jakieś is positive.", "Trochę — для незлічуваних.|„Trochę” — niepoliczalne.|Trochę is uncountable."],
   "żaden / żadna / żadne + nie.|żaden + nie.|żaden (no/any) + nie."),
]
D[20] = d("Co jest w twojej lodówce? (30+ słów): Jest trochę… Są jakieś… Nie ma żadnych…", 30, "Jest trochę… Są… Nie ma…")

T[21] = P("Ile? + liczebniki|Ile? + liczebniki|How much / many: ile?")
G[21] = [
 g("„Ile ____ chcesz?” — „Cztery.”", ["opon", "opony", "opona"],
   ["Так! Ile + родовий мн.|Tak! Ile + dopełniacz l. mn.|Yes! Ile + genitive plural.", "Називний.|Mianownik.|Nominative.", "Однина.|L. poj.|Singular."],
   "Ile + dopełniacz: ile opon? ile wody?|Ile + dopełniacz.|Ile + genitive."),
 g("Luigi ma pięć ____.", ["opon", "opony", "opona"],
   ["Так! 5+ → родовий мн.|Tak! 5+ → dopełniacz l. mn.|Yes! 5+ → genitive plural.", "2–4 → opony.|2–4 → opony.|2–4 → opony.", "Однина.|L. poj.|Singular."],
   "1 opona · 2–4 opony · 5+ opon.|1 opona · 2–4 opony · 5+ opon.|1 opona · 2–4 opony · 5+ opon."),
]
D[21] = d("Ile? (30+ słów): Ile masz książek? Ile osób jest w twojej rodzinie?", 30, "Mam … książek. W rodzinie są … osoby…")

T[22] = P("Mnie / cię / go / ją|Zaimki: mnie / go / ją|Object pronouns: mnie / go / ją")
G[22] = [
 g("Sally: „Zygzak? Lubię ____.”", ["go", "ją", "mnie"],
   ["Так! Він → go.|Tak! On → go.|Yes! Him → go.", "Ją — її.|„Ją” — ona.|Ją is her.", "Mnie — мене.|„Mnie” — ja.|Mnie is me."],
   "mnie · cię · go · ją · nas · was · ich.|mnie · cię · go · ją · nas · was · ich.|me · you · him · her · us · you · them."),
 g("Zygzak: „Sally, widzę ____!”", ["cię", "go", "ich"],
   ["Так! Ти → cię.|Tak! Ty → cię.|Yes! You → cię.", "Go — його.|„Go” — on.|Go is him.", "Ich — їх.|„Ich” — oni.|Ich is them."],
   "Kocham cię. Widzę go.|Kocham cię. Widzę go.|Kocham cię. Widzę go."),
]
D[22] = d("Twoi przyjaciele (30+ słów): Lubię go, bo… Znam ją od… Często ich widzę…", 30, "Lubię go… Znam ją… Widzę ich…")

T[23] = P("O której? W poniedziałek, w lipcu|Czas: o której? w poniedziałek|Time: o której? / w poniedziałek")
G[23] = [
 g("Wyścig jest ____ niedzielę.", ["w", "o", "na"],
   ["Так! Дні → w.|Tak! Dni → w.|Yes! Days → w.", "O — години.|„O” — godziny.|O is for times.", "Не тут.|Nie tutaj.|Not here."],
   "w poniedziałek · w lipcu · o ósmej.|w poniedziałek · w lipcu · o ósmej.|w + day/month · o + time."),
 g("Wstaję ____ siódmej.", ["o", "w", "na"],
   ["Так! Година → o.|Tak! Godzina → o.|Yes! Time → o.", "W — дні, місяці.|„W” — dni, miesiące.|W is days, months.", "Не тут.|Nie tutaj.|Not here."],
   "O której? — O siódmej.|O której? — O siódmej.|O której? — O siódmej."),
]
D[23] = d("Twój tydzień (30+ słów): W poniedziałek… O ósmej… W weekend…", 30, "W poniedziałek… O… W sobotę…")

# ---- Łuk 5
T[25] = P("Był / była / było|Był / była / było|Past of być: był / była")
G[25] = [
 g("Doc ____ mistrzem.", ["był", "była", "byli"],
   ["Так! Він → był.|Tak! On → był.|Yes! He → był.", "Była — вона.|„Była” — ona.|Była is she.", "Byli — вони.|„Byli” — oni.|Byli is they."],
   "był (on) · była (ona) · było (ono) · byli/były.|był · była · było · byli · były.|był (m) · była (f) · było (n) · byli (pl)."),
 g("Ja ____ w szpitalu przez rok. (mówi Doc)", ["byłem", "byłam", "był"],
   ["Так! Я (чол.) → byłem.|Tak! Ja (m.) → byłem.|Yes! I (male) → byłem.", "Byłam — жінка.|„Byłam” — kobieta.|Byłam is female.", "Był — він.|„Był” — on.|Był is he."],
   "byłem / byłam · byłeś / byłaś.|byłem / byłam · byłeś / byłaś.|byłem (m) / byłam (f)."),
]
D[25] = d("Gdzie byłeś wczoraj? (30+ słów): Wczoraj byłem/byłam… To było… Moi przyjaciele byli…", 30, "Byłem/Byłam… Było… Byli…")

T[26] = P("Czas przeszły: pracował / skończył|Czas przeszły|Past tense: pracował / skończył")
G[26] = [
 g("Zygzak ____ całą noc.", ["pracował", "pracuje", "pracowała"],
   ["Так! Він, минуле → pracował.|Tak! On, przeszłość → pracował.|Yes! He, past → pracował.", "Теп. час.|Czas teraźniejszy.|Present.", "Pracowała — вона.|„Pracowała” — ona.|Pracowała is she."],
   "-ł (on) · -ła (ona) · -li (oni).|-ł · -ła · -li.|-ł (m) · -ła (f) · -li (pl)."),
 g("Mieszkańcy ____ nową drogę.", ["zobaczyli", "zobaczył", "zobaczą"],
   ["Так! Вони → -li.|Tak! Oni → -li.|Yes! They → -li.", "Він.|On.|He.", "Майбутнє.|Przyszłość.|Future."],
   "Zobaczyłem, zobaczyłaś, zobaczyli.|Zobaczyłem, zobaczyłaś, zobaczyli.|Zobaczyłem, zobaczyłaś, zobaczyli."),
]
D[26] = d("Co robiłeś wczoraj? (30+ słów): Wczoraj pracowałem… Oglądałem… Nie spałem…", 30, "Wczoraj… Potem… Wieczorem…")

T[27] = P("Przeszłość: poszedł, pojechał, kupił, dał|Nieregularne formy przeszłe|Past: poszedł, kupił, dał")
G[27] = [
 g("Zygzak ____ do każdego sklepu.", ["pojechał", "pojedzie", "jechać"],
   ["Так! Минуле → pojechał.|Tak! Przeszłość → pojechał.|Yes! Past → pojechał.", "Майбутнє.|Przyszłość.|Future.", "Інфінітив.|Bezokolicznik.|Infinitive."],
   "iść → szedł/poszedł · jechać → jechał/pojechał.|iść → poszedł · jechać → pojechał.|iść → poszedł · jechać → pojechał."),
 g("Ramone ____ mu nowy lakier.", ["dał", "dała", "daje"],
   ["Так! Він → dał.|Tak! On → dał.|Yes! He → dał.", "Dała — вона.|„Dała” — ona.|Dała is she.", "Теп. час.|Teraźniejszy.|Present."],
   "dać → dał · zobaczyć → zobaczył.|dać → dał · zobaczyć → zobaczył.|dać → dał · zobaczyć → zobaczył."),
]
D[27] = d("Twój ostatni weekend (30+ słów): Pojechałem… Zobaczyłem… Kupiłem…", 30, "Pojechałem/Pojechałam… Zobaczyłem… Kupiłem…")

T[28] = P("Pytania i przeczenia w przeszłości|Pytania w przeszłości|Past questions and negatives")
G[28] = [
 g("Sally: „Czy ty ____ do dziennikarzy?”", ["zadzwoniłeś", "zadzwonisz", "dzwonisz"],
   ["Так! Минуле, ти (чол.) → zadzwoniłeś.|Tak! Przeszłość, ty (m.) → zadzwoniłeś.|Yes! Past, you (m) → zadzwoniłeś.", "Майбутнє.|Przyszłość.|Future.", "Теп. час.|Teraźniejszy.|Present."],
   "Czy + минуле: czy widziałeś?|Czy + przeszłość: czy widziałeś?|Czy + past: czy widziałeś?"),
 g("Zygzak nie ____ „do widzenia”.", ["powiedział", "powie", "mówi"],
   ["Так! Nie + минуле.|Tak! Nie + przeszłość.|Yes! Nie + past.", "Майбутнє.|Przyszłość.|Future.", "Теп. час.|Teraźniejszy.|Present."],
   "nie + czasownik w przeszłości.|nie + czas przeszły.|nie + past verb."),
]
D[28] = d("Wywiad o wczoraj: 5 pytań „Czy…?” i odpowiedzi (30+ słów).", 30, "Czy byłeś…? Tak, byłem. Czy widziałeś…? Nie, nie widziałem.")

T[29] = P("Chciałbym / chciałabym|Chciałbym / chciałabym|Would like: chciałbym")
G[29] = [
 g("Zygzak: „____ wrócić.”", ["Chciałbym", "Chciałabym", "Chcę by"],
   ["Так! Чоловік → chciałbym.|Tak! Mężczyzna → chciałbym.|Yes! Male → chciałbym.", "Chciałabym — жінка.|„Chciałabym” — kobieta.|Chciałabym is female.", "Так не кажуть.|Tak się nie mówi.|Not Polish."],
   "chciałbym (m) · chciałabym (f) + bezokolicznik.|chciałbym · chciałabym.|chciałbym (m) · chciałabym (f)."),
 g("Flo: „Czy ____ trochę paliwa?”", ["chciałbyś", "chciałbym", "chce"],
   ["Так! Ти → chciałbyś.|Tak! Ty → chciałbyś.|Yes! You → chciałbyś.", "Chciałbym — я.|„Chciałbym” — ja.|Chciałbym is I.", "Chce — він.|„Chce” — on.|Chce is he."],
   "Ввічливо: Czy chciałbyś…?|Uprzejmie: Czy chciałbyś…?|Polite: Czy chciałbyś…?"),
]
D[29] = d("Twoje marzenia (30+ słów): Chciałbym/Chciałabym… Chcę… Kiedyś chciałbym…", 30, "Chciałbym… Chcę… Kiedyś…")

# ---- Łuk 6
T[31] = P("Stopień wyższy: szybszy, większy, lepszy|Stopień wyższy|Comparatives: szybszy / lepszy")
G[31] = [
 g("Stadion jest ____ niż miasteczko.", ["większy", "duży", "największy"],
   ["Так! Порівняння → większy niż.|Tak! Porównanie → większy niż.|Yes! Comparative → większy niż.", "Duży — без порівняння.|„Duży” — bez porównania.|Duży isn't comparative.", "Найвищий ступінь.|Stopień najwyższy.|Superlative."],
   "szybki → szybszy · duży → większy · dobry → lepszy.|szybki → szybszy · duży → większy · dobry → lepszy.|fast → szybszy · big → większy · good → lepszy."),
 g("Przyjaciele są ____ niż sława.", ["ważniejsi", "ważni", "ważniejszy"],
   ["Так! Ważny → ważniejsi (мн., особи).|Tak! Ważny → ważniejsi.|Yes! Ważniejsi (plural, people).", "Без порівняння.|Bez porównania.|Not comparative.", "Однина.|L. poj.|Singular."],
   "… niż … = … ніж …|… niż …|… niż … = … than …"),
]
D[31] = d("Porównaj dwa miejsca (30+ słów): Moje miasto jest mniejsze niż… Jest cichsze… Lepsze…", 30, "…jest większy niż… …jest lepsze…")

T[32] = P("Będę / zamierzam + bezokolicznik|Będę / zamierzam|Going to: będę / zamierzam")
G[32] = [
 g("Złomek: „____ ci pomóc!”", ["Zamierzamy", "Zamierzam", "Zamierzają"],
   ["Так! Ми → zamierzamy.|Tak! My → zamierzamy.|Yes! We → zamierzamy.", "Я.|Ja.|I.", "Вони.|Oni.|They."],
   "zamierzam + bezokolicznik = I'm going to.|zamierzam + bezokolicznik.|zamierzam + infinitive = I'm going to."),
 g("Doc: „____ szefem twojej ekipy.”", ["Będę", "Byłem", "Jestem być"],
   ["Так! Майбутнє → będę.|Tak! Przyszłość → będę.|Yes! Future → będę.", "Минуле.|Przeszłość.|Past.", "Так не кажуть.|Tak się nie mówi.|Not Polish."],
   "będę, będziesz, będzie, będziemy…|będę, będziesz, będzie…|będę, będziesz, będzie…"),
]
D[32] = d("Twoje plany (30+ słów): W weekend zamierzam… Latem będę… Mój przyjaciel będzie…", 30, "Zamierzam… Będę… Będziemy…")

T[33] = P("Bo / więc / ale|Bo / więc / ale|Linking words: bo / więc / ale")
G[33] = [
 g("Zygzak się zatrzymał, ____ Król miał wypadek.", ["bo", "więc", "ale"],
   ["Так! Причина → bo.|Tak! Przyczyna → bo.|Yes! Reason → bo.", "Więc — наслідок.|„Więc” — skutek.|Więc is result.", "Ale — протиставлення.|„Ale” — kontrast.|Ale is contrast."],
   "bo = тому що · więc = тому · ale = але.|bo · więc · ale.|bo = because · więc = so · ale = but."),
 g("Chick wygrał, ____ nikt nie klaskał.", ["ale", "bo", "więc"],
   ["Так! Протиставлення → ale.|Tak! Kontrast → ale.|Yes! Contrast → ale.", "Не причина.|Nie przyczyna.|Not a reason.", "Не наслідок.|Nie skutek.|Not a result."],
   "Перед bo / więc / ale — кома.|Przed bo / więc / ale — przecinek.|Comma before bo / więc / ale."),
]
D[33] = d("Trudny wybór (30+ słów). Użyj bo, więc, ale.", 30, "Chciałem…, ale… Pomogłem, bo… więc…")

T[34] = P("Najpierw / potem / następnie / w końcu|Najpierw / potem / w końcu|Sequencing: najpierw / potem / w końcu")
G[34] = [
 g("____ Zygzak odmówił Dinoco. Potem wrócił do domu.", ["Najpierw", "W końcu", "Potem"],
   ["Так! Najpierw = спочатку.|Tak! Najpierw = first.|Yes! Najpierw = first.", "W końcu — в кінці.|„W końcu” — na końcu.|W końcu is at the end.", "Potem уже далі.|„Potem” jest dalej.|Potem comes next."],
   "Najpierw → potem → następnie → w końcu.|Najpierw → potem → następnie → w końcu.|first → then → after that → finally."),
 g("Najpierw lot helikopterem, potem powrót, ____ wielkie święto.", ["w końcu", "najpierw", "bo"],
   ["Так! Останнє → w końcu.|Tak! Ostatnie → w końcu.|Yes! Last → w końcu.", "Najpierw уже було.|„Najpierw” już było.|Najpierw was used.", "Bo — причина.|„Bo” — przyczyna.|Bo is a reason."],
   "W końcu = нарешті.|W końcu = finally.|W końcu = finally."),
]
D[34] = d("Twój idealny dzień (30+ słów): Najpierw… Potem… Następnie… W końcu…", 30, "Najpierw… Potem… Następnie… W końcu…")
