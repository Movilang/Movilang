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
 x('Hagrid ____ want a dragon as a boy.', ['used to', 'uses to', 'use to'], ('Минула звичка.', 'Nawyk z przeszłości.', 'Past habit.')),
 x('Harry ____ live with the Dursleys.', ['used to', 'use to', 'using to'], ('Used to + V.', 'Used to + V.', 'Used to + V.')),
 x("Hagrid didn't ____ have a dragon.", ['use to', 'used to', 'using to'], ("Didn't + use to.", "Didn't + use to.", "Didn't + use to.")),
 x('Did you ____ have pets?', ['use to', 'used to', 'using to'], ('Did + use to.', 'Did + use to.', 'Did + use to.')),
 x('Every night Hagrid ____ read about dragons.', ['would', 'will', 'is'], ('Would для звичок.', 'Would — nawyki.', 'Would for past habits.')),
 x('Hagrid ____ tell everyone about dragons.', ['would', 'was used', 'is use'], ('Would для звичок.', 'Would — nawyki.', 'Would for past habits.')),
]
D[26] = [
 x('When Malfoy ____ the dragon, he told McGonagall.', ['saw', 'sees', 'has seen'], ('Past Simple.', 'Past Simple.', 'Past Simple.')),
 x("As soon as Hagrid ____, we'll ask him.", ['arrives', 'will arrive', 'arrived'], ('Після as soon as — без will.', 'Bez will.', 'No will after as soon as.')),
 x('Wait here ____ I come back.', ['until', 'while', 'since'], ('Until — доки не.', 'Until — aż.', 'Until.')),
 x("We'll go to bed after we ____.", ['finish', 'will finish', 'finished'], ('Після after — без will.', 'Bez will.', "No will after 'after'.")),
 x('Neville waited ____ midnight.', ['until', 'when', 'as soon as'], ('Until.', 'Until.', 'Until.')),
 x('____ they left the tower, Filch caught them.', ['When', 'Until', 'Yet'], ('When.', 'When.', 'When.')),
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
 x('Harry was scared ____ the forest was dark.', ['because', 'so', 'however'], ('Причина.', 'Przyczyna.', 'Reason.')),
 x('The forest was dark, ____ Harry held the lantern.', ['so', 'because', 'although'], ('Наслідок.', 'Skutek.', 'Result.')),
 x('____ he was afraid, Harry went on.', ['Although', 'However', 'So'], ('Хоча.', 'Chociaż.', 'Although.')),
 x('Draco ran away. ____, Harry stayed.', ['However', 'Although', 'Because'], ('Однак.', 'Jednak.', 'However.')),
 x('The stranger drank unicorn blood ____ he was weak.', ['because', 'although', 'so'], ('Причина.', 'Przyczyna.', 'Reason.')),
 x('Firenze saved Harry, ____ Bane was angry.', ['but', 'because', 'until'], ('Протиставлення.', 'Kontrast.', 'Contrast.')),
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
 x('Ron ____ play chess very well.', ['can', 'cans', 'can to'], ('Can + V.', 'Can + V.', 'Can + V.')),
 x('Harry ____ fly when he was eleven.', ['could', 'can', 'could to'], ('Минуле вміння.', 'Umiejętność w przeszłości.', 'Past ability.')),
 x('Harry was able ____ the key.', ['to catch', 'catch', 'catching'], ('Be able to + V.', 'Be able to + V.', 'Be able to + V.')),
 x("Without Ron, we won't ____ cross the board.", ['be able to', 'can', 'could'], ('Will be able to.', 'Will be able to.', 'Will be able to.')),
 x('Hermione ____ play chess as a child.', ["couldn't", "can't to", "wasn't able"], ("Couldn't.", "Couldn't.", "Couldn't.")),
 x('After a long chase, Harry ____ catch the key.', ['was able to', 'can', 'is able'], ('Одна вдала дія.', 'Udało się.', 'Managed once.')),
]
D[32] = [
 x('Quirrell was ____ nervous that nobody suspected him.', ['so', 'such', 'too'], ('So + adj.', 'So + adj.', 'So + adj.')),
 x('It was ____ a strange night.', ['such', 'so', 'too'], ('Such a + noun.', 'Such a + noun.', 'Such a + noun.')),
 x('Harry was ____ young to fight Voldemort.', ['too', 'so', 'enough'], ('Too + adj + to.', 'Too + adj + to.', 'Too + adj + to.')),
 x('Harry was brave ____ to face Quirrell.', ['enough', 'too', 'so'], ('Adj + enough.', 'Adj + enough.', 'Adj + enough.')),
 x('The Mirror was ____ beautiful that Harry stared.', ['so', 'such', 'enough'], ('So… that.', 'So… that.', 'So… that.')),
 x('Quirrell was ____ a good actor!', ['such', 'so', 'too'], ('Such a.', 'Such a.', 'Such a.')),
]
D[33] = [
 x('Harry has ____ woken up.', ['just', 'yet', 'ever'], ('Щойно.', 'Właśnie.', 'Just.')),
 x('Have you eaten your sweets ____?', ['yet', 'already', 'just'], ('Yet у питаннях.', 'Yet w pytaniach.', 'Yet in questions.')),
 x('The Stone has ____ been destroyed.', ['already', 'yet', 'still'], ('Вже.', 'Już.', 'Already.')),
 x("Ron hasn't visited ____.", ['yet', 'already', 'just'], ('Not… yet.', 'Not… yet.', 'Not… yet.')),
 x("Harry ____ doesn't understand everything.", ['still', 'yet', 'already'], ('Досі.', 'Wciąż.', 'Still.')),
 x('Dumbledore ____ just come in.', ['has', 'have', 'is'], ('Has + V3.', 'Has + V3.', 'Has + V3.')),
]
D[34] = [
 x("By the time Dumbledore ____, Gryffindor had won.", ["finished", "had finished", "was finish"], ("Past Simple.", "Past Simple.", "Past Simple.")),
 x("Slytherin ____ the cup many times before.", ["had won", "has won", "were win"], ("Past Perfect.", "Past Perfect.", "Past Perfect.")),
 x("Students ____ when the banners changed.", ["were cheering", "cheered had", "cheers"], ("Тло.", "Tło.", "Background.")),
 x("Harry ____ never felt so happy.", ["had", "has", "was"], ("Past Perfect.", "Past Perfect.", "Past Perfect.")),
 x("Neville ____ ten points.", ["got", "had getting", "gets"], ("Подія.", "Zdarzenie.", "Event.")),
 x("Harry ____ under the stairs when Hagrid came.", ["was living", "lived has", "is living"], ("Тло.", "Tło.", "Background.")),
]
