# Grammar drill — 6 sentences per regular lesson (English target). Correct option first.
D = {}
def x(q, o, e): return (q, o, 0, e)

D[1] = [
 x("Harry ____ breakfast every morning.", ["cooks", "is cooking", "cook"], ("Звичка → cooks.", "Nawyk → cooks.", "Habit → cooks.")),
 x("Listen! Dudley ____ down the stairs.", ["is running", "runs", "run"], ("Listen! → зараз.", "Listen! → teraz.", "Listen! → now.")),
 x("The Dursleys ____ magic.", ["hate", "are hating", "hates"], ("Hate — дієслово стану.", "Hate — czasownik stanu.", "Hate is a state verb.")),
 x("Look! Aunt Petunia ____ the cake.", ["is decorating", "decorates", "decorate"], ("Look! → Continuous.", "Look! → Continuous.", "Look! → Continuous.")),
 x("Harry ____ in a cupboard under the stairs.", ["lives", "is living", "live"], ("Постійна ситуація.", "Stała sytuacja.", "Permanent situation.")),
 x("Right now, Dudley ____ his presents.", ["is counting", "counts", "count"], ("Right now → Continuous.", "Right now → Continuous.", "Right now → Continuous.")),
]
D[2] = [
 x("Harry ____ at the snake when it winked.", ["was looking", "looked", "looks"], ("Тло → Past Continuous.", "Tło → Past Continuous.", "Background → Past Continuous.")),
 x("The glass ____ suddenly.", ["disappeared", "was disappearing", "disappears"], ("Коротка подія.", "Krótkie zdarzenie.", "A short event.")),
 x("While Dudley ____, Harry talked to the snake.", ["was complaining", "complained", "complains"], ("While + Continuous.", "While + Continuous.", "While + Continuous.")),
 x("The family ____ to the zoo on Dudley's birthday.", ["went", "was going", "goes"], ("Завершена подія.", "Zdarzenie.", "Finished event.")),
 x("Visitors ____ when the snake escaped.", ["were screaming", "screamed at", "scream"], ("Тло в момент події.", "Tło.", "Background at that moment.")),
 x("Uncle Vernon ____ Harry in the cupboard again.", ["locked", "was locking", "locks"], ("Подія.", "Zdarzenie.", "Event.")),
]
D[3] = [
 x("The letter ____ to “The Cupboard under the Stairs”.", ["was addressed", "addressed", "is addressing"], ("Past passive.", "Strona bierna.", "Past passive.")),
 x("Letters ____ by owls.", ["are delivered", "deliver", "are delivering"], ("Present passive.", "Strona bierna.", "Present passive.")),
 x("The letterbox ____ shut by Vernon.", ["was nailed", "nailed", "has nail"], ("Was + V3.", "Was + V3.", "Was + V3.")),
 x("Hundreds of letters ____ through the chimney.", ["were sent", "sent", "was sent"], ("Множина → were.", "Lm → were.", "Plural → were.")),
 x("The first letter ____ in the fire.", ["was burned", "burned itself", "is burn"], ("Пасив.", "Strona bierna.", "Passive.")),
 x("The hut ____ on a rock in the sea.", ["was built", "built", "is building"], ("Пасив.", "Strona bierna.", "Passive.")),
]
D[4] = [
 x("I ____ you since you were a baby.", ["haven't seen", "didn't see", "don't see"], ("Since → Present Perfect.", "Since → Present Perfect.", "Since → Present Perfect.")),
 x("Hagrid ____ Harry to Privet Drive ten years ago.", ["brought", "has brought", "brings"], ("Ago → Past Simple.", "Ago → Past Simple.", "Ago → Past Simple.")),
 x("Harry ____ never ____ of Hogwarts.", ["has / heard", "did / hear", "is / hearing"], ("Never + Present Perfect.", "Never + Present Perfect.", "Never + Present Perfect.")),
 x("“You've just ____ eleven, Harry!”", ["turned", "turn", "turning"], ("Just + V3.", "Just + V3.", "Just + V3.")),
 x("Hagrid ____ the cake himself last week.", ["baked", "has baked", "bakes"], ("Last week → Past Simple.", "Last week → Past.", "Last week → Past Simple.")),
 x("“Have you ever ____ magic?” — “I don't know.”", ["done", "did", "do"], ("Ever + V3.", "Ever + V3.", "Ever + V3.")),
]
D[6] = [
 x("Gringotts is ____ than any Muggle bank.", ["safer", "safest", "more safe"], ("Than → comparative.", "Than → wyższy.", "Than → comparative.")),
 x("It's the ____ street Harry has ever seen.", ["strangest", "stranger", "most strange"], ("Superlative.", "Najwyższy.", "Superlative.")),
 x("The cart ride was ____ than Hagrid remembered.", ["worse", "badder", "worst"], ("Bad → worse.", "Bad → worse.", "Bad → worse.")),
 x("Goblins are not the ____ creatures.", ["friendliest", "friendlier", "most friend"], ("-y → -iest.", "-y → -iest.", "-y → -iest.")),
 x("Vault 713 was ____ than Harry's vault.", ["smaller", "smallest", "more small"], ("Comparative.", "Wyższy.", "Comparative.")),
 x("Hogwarts is the ____ place of all.", ["most magical", "magicalest", "more magical"], ("Довгий прикм. → most.", "Długi → most.", "Long adjective → most.")),
]
D[7] = [
 x("Harry hasn't got ____ time.", ["much", "many", "a few"], ("Time — незлічуване.", "Niepoliczalne.", "Uncountable.")),
 x("There are ____ shops in Diagon Alley.", ["a lot of", "much", "a little"], ("A lot of — для всіх.", "A lot of — dla wszystkich.", "A lot of works for both.")),
 x("He bought ____ books.", ["a few", "a little", "much"], ("Злічуване.", "Policzalne.", "Countable.")),
 x("Is there ____ money for a wand?", ["enough", "too", "many"], ("Enough + іменник.", "Enough + rzeczownik.", "Enough + noun.")),
 x("There were too ____ people in the shop.", ["many", "much", "little"], ("People → many.", "People → many.", "People → many.")),
 x("Can I have ____ milk, please?", ["a little", "a few", "many"], ("Незлічуване.", "Niepoliczalne.", "Uncountable.")),
]
D[8] = [
 x("The wand ____ chose Harry has a phoenix feather.", ["that", "who", "whose"], ("Речі → that/which.", "Rzeczy → that/which.", "Things → that/which.")),
 x("Ollivander is the man ____ sells wands.", ["who", "which", "where"], ("Люди → who.", "Ludzie → who.", "People → who.")),
 x("This is the shop ____ Harry bought his wand.", ["where", "which", "who"], ("Місце → where.", "Miejsce → where.", "Place → where.")),
 x("The wizard ____ wand is the brother of Harry's…", ["whose", "who", "which"], ("Приналежність.", "Przynależność.", "Possession.")),
 x("The phoenix ____ gave the feather belongs to Dumbledore.", ["which", "who", "where"], ("Тварина → which.", "Zwierzę → which.", "Animal → which.")),
 x("Hagrid told Harry about the night ____ his parents died.", ["when", "which", "who"], ("Час → when.", "Czas → when.", "Time → when.")),
]
D[9] = [
 x("Look at those clouds — it ____ rain.", ["is going to", "will to", "goes to"], ("Прогноз за ознаками.", "Prognoza.", "Prediction from evidence.")),
 x("“My bag is heavy!” — “I ____ help you.”", ["'ll", "am going to", "help"], ("Спонтанне рішення.", "Spontaniczna decyzja.", "Instant decision.")),
 x("We ____ to Hogwarts on the first of September.", ["are going", "go to will", "will going"], ("План.", "Plan.", "Arrangement.")),
 x("The train ____ at eleven o'clock.", ["leaves", "is leave", "will leaving"], ("Розклад → Present Simple.", "Rozkład.", "Timetable → Present Simple.")),
 x("I think Harry ____ like Hogwarts.", ["will", "is going", "goes"], ("Думка → will.", "Opinia → will.", "Opinion → will.")),
 x("Ron ____ his brothers on the train.", ["is meeting", "meet", "will meeting"], ("Домовленість.", "Ustalenie.", "Arrangement.")),
]
D[10] = [
 x("Hermione ____ be very clever.", ["must", "can't", "mustn't"], ("Висновок «так».", "Wniosek.", "Deduction — yes.")),
 x("That ____ be a real spell — nothing happened!", ["can't", "must", "should"], ("Висновок «ні».", "Wniosek „nie”.", "Deduction — no.")),
 x("Neville's toad ____ be somewhere on the train.", ["might", "can't", "mustn't"], ("Можливо.", "Możliwe.", "Possibly.")),
 x("Ron ____ be hungry — he hasn't eaten.", ["must", "can't", "might not"], ("Висновок.", "Wniosek.", "Deduction.")),
 x("Dumbledore ____ be anywhere now.", ["could", "must", "can't"], ("Можливо.", "Możliwe.", "Possibly.")),
 x("Scabbers ____ be dangerous — he just sleeps.", ["can't", "must", "has to"], ("Точно ні.", "Na pewno nie.", "Certainly not.")),
]
D[12] = [
 x("If you break the rules, you ____ points.", ["will lose", "lose will", "would lose"], ("First Conditional.", "First Conditional.", "First Conditional.")),
 x("If you heat ice, it ____.", ["melts", "will melting", "melted"], ("Zero Conditional.", "Zero Conditional.", "Zero Conditional.")),
 x("If Harry ____ hard, he'll do well.", ["works", "will work", "worked"], ("If + Present.", "If + Present.", "If + Present.")),
 x("The Hat ____ you if you put it on.", ["will sort", "sorts will", "would sorting"], ("Will + V.", "Will + V.", "Will + V.")),
 x("If you ____ late, McGonagall will be angry.", ["are", "will be", "were"], ("If + Present.", "If + Present.", "If + Present.")),
 x("If you mix red and blue, you ____ purple.", ["get", "will got", "got"], ("Zero.", "Zero.", "Zero.")),
]
D[13] = [
 x("You ____ go into the Forbidden Forest.", ["mustn't", "don't have to", "have to"], ("Заборона.", "Zakaz.", "Prohibition.")),
 x("Students ____ wear robes to class.", ["have to", "mustn't", "don't have to"], ("Правило.", "Zasada.", "Rule.")),
 x("It's Sunday — we ____ go to lessons.", ["don't have to", "mustn't", "must"], ("Немає потреби.", "Nie trzeba.", "Not necessary.")),
 x("You ____ say the password to enter.", ["must", "mustn't", "don't have to"], ("Обов'язок.", "Obowiązek.", "Obligation.")),
 x("First years ____ bring brooms.", ["aren't allowed to", "don't have to", "must"], ("Заборона.", "Zakaz.", "Not allowed.")),
 x("I ____ study more — Snape's test is tomorrow.", ["must", "mustn't", "needn't to"], ("Внутрішній обов'язок.", "Obowiązek.", "Personal obligation.")),
]
D[14] = [
 x("You haven't read the book, ____ you?", ["have", "haven't", "did"], ("Заперечення → позитивний хвостик.", "Przeczenie → twierdząca końcówka.", "Negative → positive tag.")),
 x("Hermione is clever, ____ she?", ["isn't", "is", "doesn't"], ("Is → isn't.", "Is → isn't.", "Is → isn't.")),
 x("____ you know what a bezoar is?", ["Do", "Are", "Have"], ("Do + V.", "Do + V.", "Do + V.")),
 x("Where ____ you find a bezoar?", ["would", "will you", "do would"], ("Where + would.", "Where + would.", "Where + would.")),
 x("Snape doesn't like Harry, ____ he?", ["does", "doesn't", "is"], ("Doesn't → does.", "Doesn't → does.", "Doesn't → does.")),
 x("____ Hagrid take the package?", ["Did", "Was", "Has took"], ("Past question → did.", "Did.", "Past question → did.")),
]
D[15] = [
 x("By the time Hooch returned, Harry ____ the ball.", ["had caught", "has caught", "caught had"], ("Past Perfect.", "Past Perfect.", "Past Perfect.")),
 x("Neville cried because he ____ his wrist.", ["had broken", "has broken", "breaks"], ("Раніше → Past Perfect.", "Wcześniej → Past Perfect.", "Earlier → Past Perfect.")),
 x("Harry ____ never flown before that day.", ["had", "has", "was"], ("Had + never + V3.", "Had + V3.", "Had + V3.")),
 x("Malfoy ____ the Remembrall before Harry took off.", ["had thrown", "has thrown", "throws"], ("Раніше.", "Wcześniej.", "Earlier.")),
 x("When McGonagall arrived, Harry ____ already landed.", ["had", "has", "did"], ("Already + Past Perfect.", "Already + Past Perfect.", "Already + Past Perfect.")),
 x("Neville ____ forgotten something again.", ["had", "has had", "was"], ("Past Perfect.", "Past Perfect.", "Past Perfect.")),
]
D[16] = [
 x("Hermione said the dog ____ guarding something.", ["was", "is being", "will"], ("Is → was.", "Is → was.", "Is → was.")),
 x("Ron said he ____ never seen a dog like that.", ["had", "has", "was"], ("Has → had.", "Has → had.", "Has → had.")),
 x("Hermione said she ____ going to bed.", ["was", "is", "will"], ("Am → was.", "Am → was.", "Am → was.")),
 x("Wood told Harry that his father ____ a great player.", ["had been", "has been", "is"], ("Was → had been.", "Was → had been.", "Was → had been.")),
 x("Harry said he ____ catch the Snitch.", ["would", "will", "can will"], ("Will → would.", "Will → would.", "Will → would.")),
 x("Ron said they ____ run.", ["could", "can", "will can"], ("Can → could.", "Can → could.", "Can → could.")),
]
D[18] = [
 x("Hermione is good at ____ spells.", ["doing", "to do", "do"], ("Прийменник + -ing.", "Przyimek + -ing.", "Preposition + -ing.")),
 x("Ron wanted ____ the feather fly.", ["to make", "making", "make"], ("Want + to.", "Want + to.", "Want + to.")),
 x("Stop ____ your wand like that!", ["waving", "to wave", "wave"], ("Stop + -ing.", "Stop + -ing.", "Stop + -ing.")),
 x("Seamus kept ____ his feather.", ["exploding", "to explode", "explode"], ("Keep + -ing.", "Keep + -ing.", "Keep + -ing.")),
 x("Harry decided ____ Hermione.", ["to find", "finding", "find"], ("Decide + to.", "Decide + to.", "Decide + to.")),
 x("Hermione enjoys ____.", ["reading", "to read", "read"], ("Enjoy + -ing.", "Enjoy + -ing.", "Enjoy + -ing.")),
]
D[19] = [
 x("If I ____ a troll, I would run.", ["saw", "see", "would see"], ("Second Conditional.", "Second Conditional.", "Second Conditional.")),
 x("If I were you, I ____ apologise.", ["would", "will", "am"], ("Would + V.", "Would + V.", "Would + V.")),
 x("If Ron ____ braver, he'd say sorry.", ["were", "is", "will be"], ("If + were.", "If + were.", "If + were.")),
 x("What ____ you do if you met a troll?", ["would", "will", "did"], ("Would.", "Would.", "Would.")),
 x("If Hermione ____ the boys, they'd be in trouble.", ["didn't help", "doesn't help", "won't help"], ("If + Past.", "If + Past.", "If + Past.")),
 x("If I had a wand, I ____ magic every day.", ["would do", "will do", "do"], ("Would + V.", "Would + V.", "Would + V.")),
]
D[20] = [
 x("Harry flew ____ than anyone.", ["faster", "more fast", "fastly"], ("Fast → faster.", "Fast → faster.", "Fast → faster.")),
 x("Slytherin played very ____.", ["badly", "bad", "worse"], ("Bad → badly.", "Bad → badly.", "Bad → badly.")),
 x("Hermione watched ____.", ["carefully", "careful", "care"], ("Прислівник.", "Przysłówek.", "Adverb.")),
 x("The broom moved ____.", ["strangely", "strange", "stranger"], ("-ly.", "-ly.", "-ly.")),
 x("Gryffindor played ____ in the second half.", ["better", "gooder", "well better"], ("Well → better.", "Well → better.", "Well → better.")),
 x("The Snitch flew ____.", ["fast", "fastly", "faster than"], ("Fast без -ly.", "Fast bez -ly.", "Fast has no -ly.")),
]
D[21] = [
 x("Ron asked Harry who ____ him the cloak.", ["had sent", "did send", "has sent"], ("Непряме питання + зсув.", "Pytanie zależne.", "Reported question + backshift.")),
 x("Filch asked who ____ there.", ["was", "is", "were"], ("Is → was.", "Is → was.", "Is → was.")),
 x("Ron told Harry ____ it on.", ["to put", "put", "putting"], ("Told + to.", "Told + to.", "Told + to.")),
 x("Dumbledore told Harry ____ look for the mirror.", ["not to", "don't", "to not"], ("Not to.", "Not to.", "Not to.")),
 x("Harry asked ____ the cloak was his father's.", ["if", "that", "what if"], ("Так/ні → if.", "Tak/nie → if.", "Yes/no → if.")),
 x("Ron asked what Harry ____ in the mirror.", ["saw", "did see", "does see"], ("Без did.", "Bez did.", "No did.")),
]
D[22] = [
 x("I wish my parents ____ here.", ["were", "are", "will be"], ("Wish + Past.", "Wish + Past.", "Wish + Past.")),
 x("If only I ____ see them every day!", ["could", "can", "will"], ("Can → could.", "Can → could.", "Can → could.")),
 x("Ron wishes he ____ Head Boy.", ["was", "is", "will be"], ("Wish + Past.", "Wish + Past.", "Wish + Past.")),
 x("I wish I ____ more money.", ["had", "have", "will have"], ("Have → had.", "Have → had.", "Have → had.")),
 x("If only Hermione ____ here now!", ["were", "is", "be"], ("If only + were.", "If only + were.", "If only + were.")),
 x("Harry wishes he ____ about his family.", ["knew", "knows", "will know"], ("Wish + Past.", "Wish + Past.", "Wish + Past.")),
]
D[24] = [
 x("The Stone ____ hidden in the castle.", ["has been", "has", "is been"], ("Present Perfect Passive.", "PP Passive.", "Present Perfect Passive.")),
 x("The Stone can ____ to make gold.", ["be used", "use", "been used"], ("Can + be + V3.", "Can + be + V3.", "Can + be + V3.")),
 x("It must ____ at all costs.", ["be protected", "protect", "protected be"], ("Must + be + V3.", "Must + be + V3.", "Must + be + V3.")),
 x("Flamel's name ____ in an old book.", ["was found", "found", "was find"], ("Past passive.", "Strona bierna.", "Past passive.")),
 x("The Elixir ____ drunk regularly.", ["must be", "must", "must been"], ("Must be + V3.", "Must be + V3.", "Must be + V3.")),
 x("The Stone will ____ soon.", ["be destroyed", "destroyed", "destroy be"], ("Will be + V3.", "Will be + V3.", "Will be + V3.")),
]
D[25] = [
 x("Hagrid ____ want a dragon as a boy.", ["used to", "is used to", "use to"], ("Минула звичка.", "Nawyk z przeszłości.", "Past habit.")),
 x("Hagrid ____ dangerous animals.", ["is used to", "used to", "uses to"], ("Звик до.", "Przyzwyczajony.", "Accustomed to.")),
 x("You'll get used to ____ with a dragon.", ["living", "live", "lived"], ("To + -ing.", "To + -ing.", "To + -ing.")),
 x("Did you ____ have pets?", ["use to", "used to", "using to"], ("Did + use to.", "Did + use to.", "Did + use to.")),
 x("Norbert will soon ____ to Romania.", ["get used", "used", "use"], ("Get used to.", "Get used to.", "Get used to.")),
 x("Hagrid ____ tell everyone about dragons.", ["would", "was used", "is use"], ("Would для звичок.", "Would — nawyki.", "Would for past habits.")),
]
D[26] = [
 x("If Malfoy hadn't seen us, we ____ caught.", ["wouldn't have been", "won't be", "wouldn't be"], ("Third Conditional.", "Third Conditional.", "Third Conditional.")),
 x("If we ____ in bed, we'd have kept our points.", ["had stayed", "stayed", "would stay"], ("If + had + V3.", "If + had + V3.", "If + had + V3.")),
 x("If Neville hadn't gone out, he ____ detention.", ["wouldn't have got", "won't get", "didn't get"], ("Would have + V3.", "Would have + V3.", "Would have + V3.")),
 x("We would have been fine if we ____ more careful.", ["had been", "were", "have been"], ("Past Perfect.", "Past Perfect.", "Past Perfect.")),
 x("If Harry had known, he ____ have gone.", ["wouldn't", "won't", "didn't"], ("Wouldn't have.", "Wouldn't have.", "Wouldn't have.")),
 x("If Hagrid ____ the egg, there'd have been no dragon.", ["hadn't won", "didn't win", "won't win"], ("Had + V3.", "Had + V3.", "Had + V3.")),
]
D[27] = [
 x("Fang, ____ is Hagrid's dog, is a coward.", ["who", "that", "whose"], ("Між комами — не that.", "Bez that.", "No that between commas.")),
 x("Unicorn blood, ____ is silver, keeps you alive.", ["which", "that", "who"], ("Which.", "Which.", "Which.")),
 x("The forest, ____ students mustn't go, is dark.", ["where", "which", "that"], ("Місце → where.", "Miejsce → where.", "Place → where.")),
 x("Hagrid, ____ was carrying a lantern, led the way.", ["who", "which", "that"], ("Людина → who.", "Osoba → who.", "Person → who.")),
 x("Firenze, ____ hooves we heard, saved Harry.", ["whose", "who", "which"], ("Приналежність.", "Przynależność.", "Possession.")),
 x("Draco, ____ was terrified, ran away.", ["who", "that", "which"], ("Who.", "Who.", "Who.")),
]
D[28] = [
 x("The figure ____ Voldemort.", ["must have been", "must be", "can't have been"], ("Висновок про минуле.", "Wniosek o przeszłości.", "Past deduction.")),
 x("The stranger ____ a normal person.", ["can't have been", "must have been", "should be"], ("Точно ні.", "Na pewno nie.", "Certainly not.")),
 x("Hagrid ____ told him — he was drunk.", ["might have", "must", "can't"], ("Можливо.", "Możliwe.", "Possibly.")),
 x("Snape ____ wanted the Stone, Harry thought.", ["must have", "can't have", "mustn't"], ("Так думає Гаррі.", "Tak myśli Harry.", "Harry's deduction.")),
 x("The stranger ____ planned it all.", ["must have", "can't", "should"], ("Must have + V3.", "Must have + V3.", "Must have + V3.")),
 x("Harry's scar ____ hurt for a reason.", ["must have", "can't have", "won't"], ("Висновок.", "Wniosek.", "Deduction.")),
]
D[30] = [
 x("You ____ relax, or it'll kill you!", ["have to", "mustn't", "don't have to"], ("Необхідність.", "Konieczność.", "Necessity.")),
 x("You'd better ____ to bed.", ["go", "to go", "going"], ("Had better + V.", "Had better + V.", "Had better + V.")),
 x("You ____ tell a teacher.", ["should", "should to", "ought"], ("Should + V.", "Should + V.", "Should + V.")),
 x("____ wake the dog!", ["Don't", "Not", "No"], ("Заперечний наказ.", "Rozkaz przeczący.", "Negative imperative.")),
 x("We ought ____ hurry.", ["to", "for", "at"], ("Ought to.", "Ought to.", "Ought to.")),
 x("You'd better not ____.", ["panic", "to panic", "panicking"], ("Had better not + V.", "Had better not + V.", "Had better not + V.")),
]
D[31] = [
 x("If Ron weren't good at chess, they ____ across.", ["wouldn't have got", "won't get", "didn't get"], ("Mixed.", "Mixed.", "Mixed.")),
 x("If Harry hadn't caught the key, he ____ in that room now.", ["would still be", "will still be", "is still"], ("Минуле → зараз.", "Przeszłość → teraz.", "Past → present.")),
 x("If Ron hadn't sacrificed himself, Harry ____ here now.", ["wouldn't be", "won't be", "isn't"], ("Mixed.", "Mixed.", "Mixed.")),
 x("If I ____ a better flyer, I'd have caught it faster.", ["were", "am", "will be"], ("Теперішня риса.", "Cecha teraz.", "Present quality.")),
 x("If Hermione hadn't helped, they ____ trapped now.", ["would be", "will be", "are"], ("Mixed.", "Mixed.", "Mixed.")),
 x("If Ron weren't brave, he ____ that move.", ["wouldn't have made", "won't make", "doesn't make"], ("Mixed.", "Mixed.", "Mixed.")),
]
D[32] = [
 x("It ____ Quirrell who let the troll in.", ["was", "were", "is been"], ("It was… who.", "It was… who.", "It was… who.")),
 x("It was Snape ____ saved Harry.", ["who", "which", "what"], ("Who для людей.", "Who.", "Who for people.")),
 x("____ Voldemort wanted was the Stone.", ["What", "That", "Which"], ("Wh-cleft.", "Wh-cleft.", "Wh-cleft.")),
 x("It wasn't Snape ____ wanted the Stone.", ["who", "whom which", "what"], ("Who.", "Who.", "Who.")),
 x("What Harry saw ____ himself with the Stone.", ["was", "were", "is been"], ("Was.", "Was.", "Was.")),
 x("Severus ____ seem the type, doesn't he?", ["does", "do", "is"], ("Емфатичне do.", "Emfatyczne do.", "Emphatic do.")),
]
D[33] = [
 x("I ____ told someone!", ["should have", "should", "must have"], ("Жаль.", "Żal.", "Regret.")),
 x("You ____ been killed!", ["could have", "should have", "must"], ("Можливість у минулому.", "Możliwość.", "Past possibility.")),
 x("Hagrid ____ have told the stranger.", ["shouldn't", "couldn't", "mustn't"], ("Не треба було.", "Nie powinien był.", "Shouldn't have.")),
 x("You ____ have worried — the Stone is safe.", ["needn't", "mustn't", "can't"], ("Даремно.", "Niepotrzebnie.", "Needn't have.")),
 x("We ____ have gone without a teacher.", ["shouldn't", "needn't", "couldn't to"], ("Жаль.", "Żal.", "Regret.")),
 x("Harry ____ have died, but his mother's love saved him.", ["could", "should", "must"], ("Could have.", "Could have.", "Could have.")),
]
D[34] = [
 x("By the time Dumbledore ____, Gryffindor had won.", ["finished", "had finished", "was finish"], ("Past Simple.", "Past Simple.", "Past Simple.")),
 x("Slytherin ____ the cup for years.", ["had been winning", "has won", "were win"], ("Past Perfect Continuous.", "PPC.", "Past Perfect Continuous.")),
 x("Students ____ when the banners changed.", ["were cheering", "cheered had", "cheers"], ("Тло.", "Tło.", "Background.")),
 x("Harry ____ never felt so happy.", ["had", "has", "was"], ("Past Perfect.", "Past Perfect.", "Past Perfect.")),
 x("Neville ____ ten points.", ["got", "had getting", "gets"], ("Подія.", "Zdarzenie.", "Event.")),
 x("Harry ____ under the stairs for ten years when Hagrid came.", ["had been living", "lived has", "is living"], ("PPC.", "PPC.", "Past Perfect Continuous.")),
]
