from common import *

# =====================================================================  17 · Fool Me Once
lesson(17, "Обдури мене раз", "Future forms: will / be going to / be about to",
 "Склеп нарешті відкривають. Бонні та її бабуся тримають заклинання, Деймон спускається вниз до тієї, на кого чекав 145 років, — а платити за магію доведеться дуже дорого.",
 A4, ("🕯️", "Свічка Шейли", "Ти пам'ятатимеш ціну, яку платять за магію."),
 [
  cards("Попередньо в Містик Фоллс… Флешбеки показали 1864 рік: засновники з компасом Джонатана Гілберта переловлювали вампірів. Стефан і Олена знайшли гримуар Емілі, а Деймон запропонував угоду. Склеп під церквою от-от відчинять.",
   [("Шейла Беннет", "Sheila Bennett", "«Грамс», бабуся Бонні. Сильна відьма, не довіряє Сальваторе — але допомагає онуці."),
    ("Перл", "Pearl", "Мама Анни. Була замкнена в склепі з 1864 року.", "upd"),
    ("Анна", "Anna", "Готова на все, щоб звільнити маму.", "upd"),
    ("Бонні Беннет", "Bonnie Bennett", "Мусить відчинити склеп разом з бабусею.", "upd")]),
  gloss("Сцена 1 · Підготовка до заклинання", """
spell|/spel/|noun|B1|заклинання|Бонні і бабуся готують ритуал.|We need the spell.|The witch cast a spell.
to cast a spell|/kɑːst ə spel/|phrase|B2|накласти заклинання|Відьми вимовляють заклинання разом.|Cast the spell.|She cast a spell on the prince.
torch|/tɔːtʃ/|noun|B1|смолоскип, ліхтарик|Біля склепу горять вогні.|Light the torches.|Take a torch, it's dark.
to be about to|/biː əˈbaʊt tə/|phrase|B1|от-от, збиратися щойно|Склеп ось-ось відчиниться.|It's about to open.|The film is about to start.
to hold|/həʊld/|verb|A2|тримати (заклинання)|Відьми мусять утримати двері відчиненими.|I can't hold it much longer.|Hold my hand.
power|/ˈpaʊə/|noun|B1|сила|Магія забирає сили відьом.|It takes a lot of power.|The storm knocked out the power.
to warn|/wɔːn/|verb|B1|попереджати|Бабуся попереджає про наслідки.|I'm warning you.|They warned us about the danger.
promise|/ˈprɒmɪs/|noun|A2|обіцянка|Бабуся вимагає від Сальваторе обіцянки.|Promise me.|I'll keep my promise.
price|/praɪs/|noun|A2|ціна|Магія має ціну.|There's always a price.|The price is too high.
"""),
  gloss("Сцена 2 · У склепі", """
the tomb|/tuːm/|noun|B2|склеп|Нарешті двері відчинено.|The tomb is open.|They opened the ancient tomb.
to go down|/ɡəʊ ˈdaʊn/|phrasal verb|A2|спуститися|Деймон спускається в темряву.|I'm going down.|Go down the stairs.
darkness|/ˈdɑːknəs/|noun|B1|темрява|Усередині — лише темрява і пил.|Total darkness.|The house was in darkness.
dried-up|/draɪd ˈʌp/|adjective|B2|висохлий|Вампіри в склепі за 145 років висохли без крові.|They're all dried up.|The river was dried up.
empty|/ˈempti/|adjective|A2|порожній|Деймон шукає одне місце — і знаходить порожнечу.|It's empty.|The fridge is empty.
to be gone|/ɡɒn/|phrase|B1|зникнути, не бути на місці|Кетрін немає в склепі.|She's gone.|My keys are gone!
to fool someone|/fuːl/|verb|B2|обдурити|Назва серії — про обман, що тривав роками.|She fooled us.|Don't let him fool you.
heartbroken|/ˈhɑːtbrəʊkən/|adjective|B2|з розбитим серцем|Деймон уперше не ховає біль.|He's heartbroken.|She was heartbroken after the breakup.
to be stuck|/stʌk/|adjective|B1|застрягти|Хтось може залишитися всередині назавжди.|I'm stuck!|We were stuck in traffic.
"""),
  gloss("Сцена 3 · Ціна магії", """
exhausted|/ɪɡˈzɔːstɪd/|adjective|B2|виснажений|Бабуся після заклинання ледь тримається.|I'm exhausted.|I was exhausted after work.
to rest|/rest/|verb|A2|відпочити|Бабуся просить дати їй відпочити.|I need to rest.|Sit down and rest.
to pass away|/pɑːs əˈweɪ/|phrasal verb|B2|відійти, померти (м'яко)|Найсумніша новина серії.|She passed away.|My grandfather passed away last year.
grief|/ɡriːf/|noun|B2|горе|Бонні в горі.|Her grief.|Grief takes time.
to blame|/bleɪm/|verb|B1|звинувачувати|Бонні звинувачує вампірів у смерті бабусі.|I blame you.|Don't blame yourself.
funeral|/ˈfjuːnərəl/|noun|B1|похорон|Сумна подія, що об'єднує друзів.|At the funeral.|The funeral is on Friday.
to comfort|/ˈkʌmfət/|verb|B2|утішати|Олена намагається втішити подругу.|Let me comfort you.|She comforted the crying child.
to be sorry for your loss|/lɒs/|phrase|B1|співчуваю вашій втраті|Формула співчуття.|I'm so sorry for your loss.|I'm sorry for your loss.
never again|/ˈnevər əˈɡen/|phrase|A2|ніколи більше|Бонні клянеться більше не допомагати вампірам.|Never again.|Never again, I promise.
"""),
  gram("Look at the door! It ____ open!", ["is about to", "will", "is going", "about to"], 0,
       ["Так! Be about to = от-от, через секунду.",
        "Will open — просто майбутнє, без відчуття «зараз-зараз».",
        "Is going open — бракує to.",
        "Без is речення неповне."],
       "be about to + verb = за мить. be going to = план або очевидний наслідок. will = рішення в моменті/прогноз.", img="tomb", label="ГРИМУАР"),
  gram("Damon has a plan: “I ____ bring Katherine out tonight.”", ["am going to", "will be", "am about", "going to"], 0,
       ["Так! Be going to — заздалегідь вирішений план.",
        "Will be bring — неграматично.",
        "Am about — без to і без сенсу «плану».",
        "Без am речення неповне."],
       "План на 145 років — точно going to.", label="ГРАМАТИКА СЦЕНИ"),
  choice("Grams is exhausted. Bonnie decides on the spot to help her. What does Bonnie say?",
         ["I'll help you, Grams.", "I'm going to help you, Grams, since last year.", "I help you, Grams."], 0,
         ["Так! Рішення в моменті → will: I'll help.",
          "Since last year — безглуздо з майбутнім.",
          "Present Simple тут звучить як звичка, а не рішення."],
         scene="Біля склепу. Руки бабусі тремтять."),
  who("“She's gone.” Who realises this inside the tomb?", ["Damon", "Stefan", "Anna", "Grams"], 0,
      ["Так — Деймон розуміє, що Кетрін немає. Найболючіша мить сезону для нього.",
       "Стефан теж у склепі, але для нього ця новина значить інше.",
       "Анна шукає маму, а не Кетрін.",
       "Бабуся залишається нагорі, тримаючи заклинання."],
      "Be gone — зникнути, не бути на місці. Звучить сильніше, ніж «she isn't here»."),
  sarcasm("After the tomb, Damon smiles too widely: “I'm fine. Never better.” What does he really feel?",
          ["He's devastated and hiding it", "He's truly relaxed", "He's hungry", "He's excited about the future"], 0,
          ["Так — «never better» після такої ночі звучить як крик болю.",
           "Ні, це маска.",
           "Голод тут ні до чого.",
           "Майбутнє його зараз не цікавить."],
          "Never better = «ще ніколи не було так добре». Коли все погано — це сарказм над собою."),
  grill([("to cast a spell", "to use magic words"), ("exhausted", "extremely tired"), ("heartbroken", "very sad because of love"),
         ("to pass away", "to die (polite)"), ("to be stuck", "unable to get out")],
        "Найсумніша серія сезону — у п'яти словах."),
  compel("Hold the door open until we come out",
         "Наказ + until + Present Simple (не will!): until we come out.",
         scene="Склеп відкритий. Стефан і Олена всередині. Час іде."),
  lie_tf("Bonnie: “I'm never going to help vampires again.” Does she mean it right now?",
         True,
         ["Так, зараз вона говорить щиро — горе робить її рішення твердим. Чи дотримає вона слова — інше питання.",
          "Насправді це правда для неї в цю мить. Відповідь «True» правильна."],
         "Тест на вербену перевіряє не майбутнє, а щирість у момент мовлення."),
  page("Dear Diary, tomorrow Bonnie ____ (bury) her grandmother. (заплановано)", ["is going to bury", "will bury", "is burying"],
       "Запланована подія: is going to bury або is burying (домовленість). Will теж приймаємо."),
  audio("I'm so sorry for your loss.", ["i'm so sorry for your loss", "i am so sorry for your loss"],
        "Формула співчуття. Говорять тихо, без поспіху."),
  word("Grams says magic always comes with a ____.", ["price", "prize", "present", "party"], 0,
       ["Так! Price — ціна. Головний урок серії.", "Prize — приз, нагорода. Схоже, але протилежне.",
        "Present — подарунок.", "Party — вечірка."],
       "price /praɪs/ ≠ prize /praɪz/. Одна літера — і ціна стає нагородою."),
  speak("I'm going to help you.", "Going to часто звучить як «gonna» в розмові, але тут вимовляй повністю."),
  diary_final("Write Bonnie's diary after the funeral (50+ words). Use will, be going to and be about to: what she will never do again, what she is going to do now, what is about to change.",
              50, "Три способи говорити про майбутнє — три різні відтінки рішучості."),
 ])

# =====================================================================  18 · A Few Good Men
lesson(18, "Кілька хороших людей", "Relative clauses: who / which / that / whose / where",
 "Деймон топить горе після склепу. Олена шукає жінку, яка її народила, і слід веде до людини, що стоїть зовсім поруч. Аларік нарешті дізнається, хто винен у зникненні його дружини.",
 A4, ("🥃", "Келих бурбону", "Ти бачив(ла) Деймона без маски."),
 [
  cards("Попередньо в Містик Фоллс… Бонні і її бабуся відчинили склеп. Кетрін там не виявилося — Деймон чекав 145 років даремно. Анна визволила свою маму Перл. Бабуся Бонні не пережила тієї ночі.",
   [("Деймон Сальваторе", "Damon Salvatore", "Розбитий. П'є, грубіянить і вперше показує людям свій біль.", "upd"),
    ("Аларік Зальцман", "Alaric Saltzman", "Учитель історії і мисливець на вампірів. Шукає того, хто забрав його дружину.", "upd"),
    ("Ізобел", "Isobel", "Дружина Аларіка, що зникла. Дослідниця паранормального. Олена дізнається, що Ізобел — її біологічна мати.", "upd"),
    ("Перл", "Pearl", "Вийшла зі склепу і вчиться жити в XXI столітті.", "upd")]),
  gloss("Сцена 1 · Горе Деймона · Як говорить Деймон", """
bourbon|/ˈbɜːbən/|noun|B2|бурбон (віскі)|Улюблений напій Деймона цієї серії.|Pour me a bourbon.|He ordered a glass of bourbon.
to drown one's sorrows|/draʊn ˈsɒrəʊz/|idiom|C1|заливати горе (алкоголем)|Деймон намагається забути Кетрін.|Drowning my sorrows.|After the breakup he drowned his sorrows.
to get drunk|/ɡet drʌŋk/|phrase|B1|напитися|Деймон п'яний і небезпечний.|He's drunk.|Don't get drunk at the party.
to lash out|/læʃ ˈaʊt/|phrasal verb|C1|зриватися на когось|Біль Деймона виливається на інших.|Don't lash out at me.|He lashed out at his friends.
to care|/keə/|verb|A2|піклуватися, перейматися|Деймон кричить, що йому байдуже.|I don't care.|I care about you.
pathetic|/pəˈθetɪk/|adjective|B2|жалюгідний|Так Деймон називає себе чи інших.|Pathetic.|That's a pathetic excuse.
to move on|/muːv ɒn/|phrasal verb|B1|жити далі|Тепер Деймону треба відпустити минуле.|Time to move on.|It's time to move on.
to be over|/ˈəʊvə/|phrase|A2|закінчитися|Деймон визнає, що з Кетрін усе скінчено.|It's over.|The party is over.
lonely|/ˈləʊnli/|adjective|A2|самотній|Під сарказмом — самотність.|I'm not lonely.|She felt lonely in the new city.
"""),
  gloss("Сцена 2 · Пошуки матері", """
birth mother|/bɜːθ ˈmʌðə/|noun|B2|біологічна мати|Олена шукає жінку, яка її народила.|I want to find my birth mother.|She met her birth mother at 30.
to track down|/træk ˈdaʊn/|phrasal verb|B2|розшукати|Олена йде слідом за записами.|I tracked her down.|The police tracked down the car.
researcher|/rɪˈsɜːtʃə/|noun|B1|дослідниця|Ізобел вивчала паранормальні явища.|She was a researcher.|She works as a cancer researcher.
paranormal|/ˌpærəˈnɔːml/|adjective|C1|паранормальний|Предмет досліджень Ізобел.|Paranormal research.|He studies paranormal activity.
folklore|/ˈfəʊklɔː/|noun|C1|фольклор|Ізобел цікавилася легендами Містик Фоллс.|Local folklore.|Vampires are part of European folklore.
to be related|/rɪˈleɪtɪd/|adjective|B1|бути родичем|Олена дізнається, з ким пов'язана кров'ю.|We're related.|Are you two related?
to match|/mætʃ/|verb|B1|збігатися|Дати і імена збігаються.|Everything matches.|Your shoes match your bag.
small world|/smɔːl wɜːld/|idiom|B1|світ тісний|Олена шокована збігом.|Small world.|You know him too? Small world!
whose|/huːz/|pronoun|B1|чий, чия|Олена питає, чия це фотографія.|Whose photo is this?|Whose bag is this?
"""),
  gloss("Сцена 3 · Аларік і правда", """
hunter|/ˈhʌntə/|noun|B1|мисливець|Аларік полює на вампірів.|A vampire hunter.|The hunter came back with nothing.
to avenge|/əˈvendʒ/|verb|C1|помститися (за когось)|Аларік хоче помститися за дружину.|I'll avenge her.|He swore to avenge his father.
revenge|/rɪˈvendʒ/|noun|B2|помста|Двигун Аларіка весь цей час.|This is about revenge.|He wanted revenge.
to hold a grudge|/həʊld ə ɡrʌdʒ/|idiom|C1|тримати образу|Аларік не може відпустити.|He holds a grudge.|She never holds a grudge.
to confess|/kənˈfes/|verb|B2|зізнатися|Деймон розповідає свою версію подій.|I confess.|He confessed to the crime.
to ask for something|/ɑːsk fɔː/|phrase|A2|просити про щось|Деймон стверджує, що Ізобел сама цього хотіла.|She asked for it.|She asked for help.
to make amends|/meɪk əˈmendz/|idiom|C1|загладити провину|Чи може Деймон колись виправити скоєне?|I want to make amends.|He tried to make amends for his mistake.
weapon|/ˈwepən/|noun|B1|зброя|Аларік приходить підготовленим.|Your weapon.|The police found the weapon.
to stand a chance|/stænd ə tʃɑːns/|idiom|B2|мати шанс|Людина проти вампіра — нерівна битва.|You don't stand a chance.|We don't stand a chance against them.
"""),
  gram("Isobel was a researcher ____ studied local folklore.", ["who", "which", "whose", "where"], 0,
       ["Так! Who — для людей.", "Which — для речей і тварин.", "Whose — «чий», тут не пасує.", "Where — для місць."],
       "who/that — люди; which/that — речі; whose — чий; where — місце.", label="ГРАМАТИКА СЦЕНИ"),
  gram("Elena found the town ____ her birth mother had lived.", ["where", "which", "who", "whose"], 0,
       ["Так! Місце → where.", "Which можна лише з прийменником: the town in which… Без нього — where.",
        "Who — для людей.", "Whose — «чий»."],
       "Where = in which.", label="ВИБІР ОЛЕНИ"),
  page("Alaric is the man ____ wife disappeared.", ["whose"],
       "Whose = чий. The man whose wife… — чоловік, чия дружина…"),
  who("“I don't care.” Who keeps saying this in this episode — and doesn't mean it?", ["Damon", "Alaric", "Elena", "Pearl"], 0,
      ["Так — Деймон повторює «мені байдуже», бо надто болить.",
       "Аларікові якраз зовсім не байдуже.",
       "Олена переймається всім.",
       "Перл перейматися має чим."],
      "Коли людина повторює «I don't care» тричі — їй не байдуже."),
  sarcasm("Elena tries to talk to Damon. He says: “Oh, the Elena Gilbert support group. How lovely.” What does he mean?",
          ["Leave me alone, I don't want pity", "Thank you, I needed a friend", "Let's start a club", "You look lovely today"], 0,
          ["Так — «how lovely» тут означає «тільки цього бракувало».",
           "Можливо, глибоко в душі. Але слова кажуть протилежне.",
           "Клубів він не планує.",
           "Це не комплімент."],
          "Support group — група підтримки. Деймон глузує, бо не вміє приймати допомогу."),
  grill([("birth mother", "the woman who gave birth to you"), ("to track down", "to find after searching"),
         ("to hold a grudge", "to stay angry for a long time"), ("to make amends", "to try to fix a past wrong"),
         ("pathetic", "very weak and sad")],
        "Пошуки, образи і спроби виправити минуле."),
  council("Clues: (1) Isobel studied Mystic Falls folklore; (2) she visited the town years ago; (3) the dates in Elena's adoption file match; (4) Alaric has a photo of Isobel. Who is Isobel?",
          ["Elena's birth mother", "Jenna's sister", "Katherine's daughter", "Alaric's student"], 0,
          ["Так — і світ раптом стає дуже тісним.",
           "Дженна — сестра прийомної мами Олени, а не Ізобел.",
           "Нічого не вказує на Кетрін.",
           "Ізобел була дружиною Аларіка, а не студенткою."],
          "Who is…? — визначення людини через relative clause: the woman who…", img="diary"),
  compel("Tell me the name of the woman who gave birth to me",
         "Relative clause з who: the woman who gave birth to me. Без коми — це визначальна частина.",
         scene="Архів старої лікарні. Олена тримає папку з печаткою."),
  lie("Who is NOT fully honest? Damon: “I don't care about anyone.” Alaric: “I came here to find answers.” Elena: “I want to know who my mother is.”",
      ["Damon", "Alaric", "Elena"], 0,
      ["Так — Деймон захищається байдужістю, але не він не переймається.",
       "Аларік справді шукає відповіді.",
       "Олена щира."],
      "Самообман — теж брехня, яку виявляє тест на вербену."),
  audio("You don't stand a chance.", ["you don't stand a chance", "you do not stand a chance"],
        "Stand a chance — мати шанс. Don't — злито: /dəʊnt/."),
  speak("I want to make amends.", "Make amends — офіційно і серйозно. Говори повільно."),
  diary_final("Write about three people in Mystic Falls using relative clauses (50+ words): Damon is a man who…, Isobel was a woman whose…, Mystic Falls is a town where…",
              50, "Relative clauses роблять опис багатим. Використай who, which, whose, where."),
 ])

# =====================================================================  19 · There Goes the Neighborhood
lesson(19, "Нові сусіди", "Gerund vs infinitive",
 "Вампіри зі склепу оселилися в місті — і пам'ятають, хто їх туди замкнув. Джеремі закохується в Анну і просить про неможливе. Олена намагається жити звичайним життям і хоч на вечір забути про таємниці.",
 A4, ("📌", "Шпилька Анни", "Ти знаєш, що вампіри зі склепу живуть поруч."),
 [
  cards("Попередньо в Містик Фоллс… Деймон топив горе після склепу. Олена дізналася, що її біологічна мати — Ізобел, зникла дружина Аларіка. Деймон зізнався Аларікові у своїй версії правди.",
   [("Анна", "Anna", "Закохана в Джеремі. Але вона вампірка — і Джеремі це знає.", "upd"),
    ("Джеремі Гілберт", "Jeremy Gilbert", "Втомився від втрат. Хоче, щоб Анна зробила його таким, як вона.", "upd"),
    ("Перл", "Pearl", "Ватажок вампірів зі склепу. Хоче повернути собі місто — по-своєму.", "upd")]),
  gloss("Сцена 1 · Звичайний вечір", """
double date|/ˈdʌbl deɪt/|noun|B2|подвійне побачення|Друзі вирішують провести вечір парами.|Let's go on a double date.|We went on a double date with our friends.
to hang out|/hæŋ ˈaʊt/|phrasal verb|B1|проводити час|Олена хоче просто провести час з друзями.|We should hang out more.|We hang out after school.
normal|/ˈnɔːml/|adjective|A2|нормальний, звичайний|Олена мріє про звичайний вечір.|I want one normal night.|It was a normal day.
to enjoy|/ɪnˈdʒɔɪ/|verb|A2|насолоджуватися|Олена намагається насолодитися вечором.|Enjoy yourself.|I enjoy reading.
to avoid|/əˈvɔɪd/|verb|B1|уникати|Олена уникає розмов про вампірів.|Avoid talking about it.|Avoid eating late.
small talk|/smɔːl tɔːk/|noun|B1|світська розмова|Розмови ні про що за столом.|Just small talk.|I'm not good at small talk.
to get to know|/ɡet tə nəʊ/|phrase|B1|познайомитися ближче|Друзі пізнають одне одного по-новому.|I want to get to know you.|Let's get to know each other.
to look forward to|/lʊk ˈfɔːwəd tə/|phrasal verb|B2|чекати з нетерпінням|Хтось чекає вечора, хтось боїться.|I'm looking forward to it.|I look forward to seeing you.
awkward silence|/ˈɔːkwəd ˈsaɪləns/|noun|B1|ніякова тиша|Пауза, яку ніхто не знає, як заповнити.|Awkward silence.|There was an awkward silence.
"""),
  gloss("Сцена 2 · Джеремі і Анна", """
to turn someone|/tɜːn/|verb|C1|перетворити на вампіра|Джеремі просить Анну перетворити його.|Turn me.|— (термін серіалу)
forever|/fərˈevə/|adverb|A2|назавжди|Джеремі хоче бути з Анною назавжди.|Forever.|I'll love you forever.
to stop feeling|/stɒp ˈfiːlɪŋ/|phrase|B1|перестати відчувати|Джеремі хоче перестати відчувати біль.|I want to stop feeling this.|Stop worrying!
to risk|/rɪsk/|verb|B1|ризикувати|Джеремі готовий ризикнути всім.|I'll risk it.|Don't risk your life.
to regret|/rɪˈɡret/|verb|B2|шкодувати|Анна попереджає, що він пошкодує.|You'll regret it.|I regret saying that.
to refuse|/rɪˈfjuːz/|verb|B1|відмовитися|Анна спершу відмовляє.|I refuse to do it.|He refused to answer.
to pretend|/prɪˈtend/|verb|B1|вдавати|Джеремі вдає, що все гаразд.|Stop pretending.|She pretended to be ill.
to give up|/ɡɪv ˈʌp/|phrasal verb|B1|відмовитися від|Ціна безсмертя — відмовитися від людського життя.|You'd give up everything.|He gave up smoking.
to deserve|/dɪˈzɜːv/|verb|B2|заслуговувати|Анна каже, що Джеремі заслуговує на справжнє життя.|You deserve a real life.|You deserve a break.
"""),
  gloss("Сцена 3 · Сусіди зі склепу", """
neighborhood|/ˈneɪbəhʊd/|noun|B1|район, околиця|Вампіри зі склепу оселилися поряд.|There goes the neighborhood.|We live in a quiet neighborhood.
to settle in|/setl ˈɪn/|phrasal verb|B2|облаштуватися|Перл обживається в новому столітті.|We're settling in.|Are you settling in well?
to adjust|/əˈdʒʌst/|verb|B2|пристосуватися|Як звикнути до XXI століття після 1864 року?|It's hard to adjust.|It takes time to adjust to a new job.
technology|/tekˈnɒlədʒi/|noun|B1|технології|Перл вивчає світ телефонів і комп'ютерів.|So much technology.|Technology changes fast.
to take revenge on|/teɪk rɪˈvendʒ/|phrase|B2|помститися комусь|Вампіри зі склепу не забули засновників.|They want revenge on the founders.|He took revenge on his enemies.
founding families|/ˈfaʊndɪŋ ˈfæməliz/|noun|B2|родини-засновниці|Список імен, якого бояться в місті.|The founding families.|The founding families built the town.
to keep a low profile|/ləʊ ˈprəʊfaɪl/|idiom|C1|не висовуватися|Перл радить своїм поводитися тихо.|Keep a low profile.|After the scandal, he kept a low profile.
threat|/θret/|noun|B2|загроза|Для міста — нова небезпека.|They're a threat.|The storm is a threat to farmers.
to make a move|/meɪk ə muːv/|idiom|B2|почати діяти|Вампіри чекають слушного моменту.|When will they make a move?|Don't make a move yet.
"""),
  gram("Jeremy wants ____ forever with Anna.", ["to stay", "staying", "stay", "to staying"], 0,
       ["Так! Want + to-infinitive.", "Want не вживається з -ing.", "Бракує to.", "To staying — помилка."],
       "Після want, decide, refuse, promise, hope — to + verb.", label="ГРАМАТИКА СЦЕНИ"),
  gram("Elena tries to avoid ____ about vampires tonight.", ["talking", "to talk", "talk", "talked"], 0,
       ["Так! Avoid + -ing.", "Avoid не вживається з to.", "Потрібна форма -ing.", "Минулий час тут не пасує."],
       "Після avoid, enjoy, stop, mind, keep, finish — -ing.", label="ВИБІР ОЛЕНИ"),
  page("Anna: “I refuse ____ (turn) you. You deserve a real life.”", ["to turn"],
       "Refuse + to + verb: refuse to turn."),
  grimoire("I'm looking forward to ____ (бачити) you. (-ing!)", ["seeing"],
           "Look forward to + -ing! «To» тут — прийменник, а не частина інфінітива."),
  word("Stop ____ ! (stop + -ing = перестати робити) Choose the correct form.", ["pretending", "to pretend", "pretend", "pretended"], 0,
       ["Так! Stop + -ing = перестати робити.",
        "Stop to pretend = зупинитися, щоб удати. Зовсім інший зміст!",
        "Потрібна форма -ing.",
        "Минулий час тут не пасує."],
       "stop doing = перестати; stop to do = зупинитися з метою."),
  who("“Turn me.” Who asks this, and whom?", ["Jeremy asks Anna", "Elena asks Stefan", "Caroline asks Damon", "Matt asks Pearl"], 0,
      ["Так — Джеремі хоче перестати відчувати біль.",
       "Олена ніколи цього не просила.",
       "Керолайн у цій серії так не говорить.",
       "Метт нічого не знає про вампірів."],
      "Turn someone — перетворити на вампіра. Наказовий спосіб — коротко і страшно."),
  sarcasm("Damon about the tomb vampires moving into town: “There goes the neighborhood.” What does he mean?",
          ["The town is about to become much more dangerous", "He likes his new neighbours", "He's moving to another neighborhood", "The houses are too expensive"], 0,
          ["Так! Ідіома «there goes the neighborhood» — іронічно: «ну все, району кінець».",
           "Навпаки, вони йому не до вподоби.",
           "Переїжджати він не збирається.",
           "Мова не про ціни."],
          "Назва серії — ідіома. Її кажуть, коли «не ті» люди переїжджають по сусідству."),
  grill([("to settle in", "to get comfortable in a new place"), ("to adjust", "to change to fit something new"),
         ("to keep a low profile", "to avoid attention"), ("to deserve", "to have earned something"), ("double date", "two couples going out together")],
        "Сусіди, побачення і звикання."),
  compel("Promise me to stop thinking about it",
         "Promise + to + verb; stop + -ing — обидва правила в одному реченні.",
         scene="Кімната Джеремі. Анна сидить на краю ліжка."),
  lie_tf("Jeremy tells Elena: “I'm fine, I'm just tired.” Is he telling the truth?",
         False,
         ["Ні — «just tired» прикриває глибокий біль і небезпечне рішення.",
          "Так, це неправда. Відповідь «False» правильна."],
         "Just + легке пояснення = класичний маркер прихованої проблеми."),
  audio("I'm looking forward to it.", ["i'm looking forward to it", "i am looking forward to it"],
        "Look forward to — чекати з нетерпінням. Звучить ввічливо і тепло."),
  speak("I want one normal night.", "Наголос на normal. Втомлена, але тепла інтонація."),
  diary_final("Write Jeremy's diary (50+ words). Use verbs + infinitive (want to, decide to, refuse to) and verbs + -ing (avoid, enjoy, stop, keep). What does he want, and what does he try to avoid?",
              50, "Gerund vs infinitive — запам'ятовуй дієслова групами."),
 ])

# =====================================================================  20 · Let the Right One In
lesson(20, "Впусти мене", "Passive: Present Perfect & modal passive",
 "Буря відрізає місто, а Стефан зникає. Його схопили вампіри зі склепу. Олена, Деймон і Аларік мусять об'єднатися — і за порятунок Стефан заплатить тим, від чого втікав десятиліттями.",
 A4, ("🪵", "Дерев'яний кілок", "Ти брав(ла) участь у порятунку Стефана."),
 [
  cards("Попередньо в Містик Фоллс… Вампіри зі склепу оселилися в місті й хочуть помститися засновникам. Джеремі попросив Анну перетворити його. Олена мріяла про один нормальний вечір — і не отримала його.",
   [("Стефан Сальваторе", "Stefan Salvatore", "Схоплений вампірами зі склепу. Слабкий, бо харчується лише кров'ю тварин.", "upd"),
    ("Аларік Зальцман", "Alaric Saltzman", "Тепер союзник Олени й Деймона в боротьбі з вампірами зі склепу.", "upd"),
    ("Фредерік", "Frederick", "Вампір зі склепу. Ненавидить Стефана і засновників.")]),
  gloss("Сцена 1 · Буря і зникнення", """
storm|/stɔːm/|noun|A2|буря, гроза|Злива і вітер над Містик Фоллс.|There's a storm coming.|The storm knocked down trees.
to be taken|/ˈteɪkən/|passive|B1|бути схопленим|Стефан зник — його схопили.|He's been taken.|My bike has been taken!
to go missing|/ɡəʊ ˈmɪsɪŋ/|phrase|B1|зникнути безвісти|Стефан не відповідає на дзвінки.|He's gone missing.|Their cat has gone missing.
to be held|/held/|passive|B1|утримуватися (в полоні)|Стефан у полоні в старому будинку.|He's being held there.|The hostages were held for days.
to kidnap|/ˈkɪdnæp/|verb|B2|викрасти|Вампіри зі склепу викрадають Стефана.|They kidnapped him.|They kidnapped the dog for money.
power outage|/ˈpaʊər ˌaʊtɪdʒ/|noun|C1|відключення світла|Буря вимикає електрику.|The power's out.|We had a power outage last night.
to call for help|/kɔːl fə help/|phrase|A2|кликати на допомогу|Олена дзвонить усім, хто може допомогти.|Call for help.|She called for help.
to be soaked|/səʊkt/|adjective|B1|змокнути|Олена шукає Стефана під зливою.|I'm soaked.|We got soaked in the storm.
rescue|/ˈreskjuː/|noun, verb|B1|порятунок, рятувати|Олена планує порятунок.|We need a rescue plan.|The firemen rescued the boy.
"""),
  gloss("Сцена 2 · Будинок без господаря", """
invitation|/ˌɪnvɪˈteɪʃn/|noun|B1|запрошення|Правило, на якому все тримається.|No invitation needed.|Thanks for the invitation.
owner|/ˈəʊnə/|noun|B1|власник|Господар будинку мертвий — і правило не діє.|The owner is dead.|The owner of the shop is my friend.
to let in|/let ˈɪn/|phrasal verb|B1|впустити|Хто може впустити вампіра?|Let me in.|Don't let anyone in.
can't get in|/kɑːnt ɡet ɪn/|phrase|A2|не може увійти|Деймон зупиняється на порозі.|I can't get in.|I can't get in — I lost my key.
to be invited in|/ɪnˈvaɪtɪd ɪn/|passive|B1|бути запрошеним досередини|Деймонові потрібне запрошення.|I need to be invited in.|We were invited in for coffee.
basement|/ˈbeɪsmənt/|noun|B1|підвал|Стефана тримають унизу.|He's in the basement.|We keep bikes in the basement.
wooden|/ˈwʊdn/|adjective|A2|дерев'яний|Вампіри катують Стефана дерев'яними кілками.|Wooden stakes.|A wooden table.
to torture|/ˈtɔːtʃə/|verb|C1|катувати|Стефан страждає в полоні.|They're torturing him.|— (історичний контекст)
weak|/wiːk/|adjective|A2|слабкий|Через тваринну кров Стефан слабший за інших.|He's too weak.|I feel weak today.
"""),
  gloss("Сцена 3 · Кров Олени", """
human blood|/ˈhjuːmən blʌd/|noun|B1|людська кров|Стефанові потрібна сила, і є лише одне джерело.|He needs human blood.|— (термін серіалу)
to offer|/ˈɒfə/|verb|B1|пропонувати|Олена пропонує свою кров.|I'm offering.|She offered me a cup of tea.
strength|/streŋθ/|noun|B1|сила|Кров повертає Стефанові сили.|It'll give you strength.|You need strength for this job.
to crave|/kreɪv/|verb|C1|жадати, сильно хотіти|Після цієї ночі Стефан відчуває стару спрагу.|I crave it.|I'm craving pizza.
to recover|/rɪˈkʌvə/|verb|B2|одужати, відновитися|Стефан швидко відновлюється.|You'll recover.|She recovered after the operation.
to lose control|/luːz kənˈtrəʊl/|phrase|B1|втратити контроль|Найбільший страх Стефана.|I can't lose control.|He lost control of the car.
to be addicted|/əˈdɪktɪd/|adjective|B2|бути залежним|Стефан знає, чим це може закінчитися.|I was addicted once.|He's addicted to his phone.
cut|/kʌt/|noun|A2|поріз|Олена робить поріз на руці.|A small cut.|I have a cut on my finger.
to save someone's life|/seɪv laɪf/|phrase|B1|врятувати комусь життя|Олена рятує Стефана.|You saved my life.|The doctor saved his life.
"""),
  gram("Stefan ____ by the tomb vampires. Nobody knows where he is!", ["has been taken", "has taken", "is taking", "was take"], 0,
       ["Так! Present Perfect Passive: has been + 3-тя форма. Важливий результат зараз.",
        "Has taken — активний стан: це Стефан когось забрав.",
        "Is taking — теж активний.",
        "Was take — неправильна форма."],
       "Present Perfect Passive: has/have been + V3.", label="РОЗСЛІДУВАННЯ РАДИ"),
  gram("A vampire must ____ into a house by the owner.", ["be invited", "invite", "invited", "being invited"], 0,
       ["Так! Модальний пасив: must be + V3.", "Активна форма — вампір сам когось запрошує.",
        "Бракує be.", "Being — не після must."],
       "Модальний пасив: can/must/should + be + V3.", img="manor", label="ГРИМУАР"),
  page("He can't ____ (save) without human blood. (пасив: його не можна врятувати)", ["be saved"],
       "Can't + be + saved."),
  council("Clues: (1) the house's owner is dead; (2) the tomb vampires walked in freely; (3) Damon could also enter without an invitation; (4) Stefan is in the basement. Why could everyone get in?",
          ["Without a living owner, no invitation is needed", "The door was open", "Stefan invited them", "They used a spell"], 0,
          ["Так — правило запрошення діє, лише поки живий господар.",
           "Відчинені двері не скасовують вампірського правила.",
           "Стефан їх не запрошував.",
           "Заклинання тут не потрібне."],
          "Головна «юридична» деталь вампірських правил серіалу.", img="manor"),
  who("“You saved my life.” Who could say this at the end of the episode, and to whom?",
      ["Stefan to Elena", "Damon to Alaric", "Frederick to Pearl", "Jeremy to Anna"], 0,
      ["Так — кров Олени повернула Стефанові сили.",
       "Деймон і Аларік радше мовчки кивнули б одне одному.",
       "Фредерік — ворог Стефана.",
       "Джеремі в цій сцені немає."],
      "Save someone's life — врятувати комусь життя."),
  sarcasm("Damon to Alaric before the rescue: “Great. A history teacher. We're saved.” What does he mean?",
          ["He doubts a human can help, but he's grudgingly accepting it", "He's sure Alaric is the best fighter", "He wants a history lesson", "He's going to fire Alaric"], 0,
          ["Так — сарказм: «чудово, вчитель історії — ну все, ми врятовані». Але Деймон таки бере його з собою.",
           "Ні, він сумнівається.",
           "Уроки історії його не цікавлять.",
           "Звільнити Аларіка він не може."],
          "«We're saved» з іронією = «ну все, нам кінець»."),
  grill([("to go missing", "to disappear"), ("to crave", "to want very strongly"), ("to recover", "to get well again"),
         ("power outage", "when the electricity stops"), ("owner", "the person a house belongs to")],
        "Ніч бурі і порятунку."),
  compel("Let me in and don't say a word",
         "Наказ з let: Let + me + in. Друга частина — заперечний наказ.",
         scene="Поріг старого будинку. Зливу чути крізь двері."),
  lie_tf("After drinking Elena's blood, Stefan says: “I'm fine. It's under control.” Is this the full truth?",
         False,
         ["Ні — він уже відчуває стару спрагу. «Under control» ще повернеться в наступному уроці.",
          "Так, це не вся правда. «False» — правильно."],
         "Under control — фраза, яку кажуть саме тоді, коли контроль уже втрачено."),
  audio("He's been taken.", ["he's been taken", "he has been taken"],
        "He's = he has. Злито і швидко: /hiːz biːn ˈteɪkən/."),
  choice("Elena makes a decision in the basement. Which sentence fits?",
         ["Take my blood. I want you to live.", "Take my blood. I want that you live.", "Taking my blood. I want you living."], 0,
         ["Так! Наказ + want + object + to + verb.",
          "«Want that you live» — калька з української.",
          "Taking — не наказовий спосіб."],
         scene="Підвал, слабке світло ліхтарика. Стефан ледь дихає."),
  speak("You saved my life.", "Тиха, щира інтонація. Наголос на saved."),
  diary_final("Write a police-style report of the rescue night (50+ words). Use passive forms: Stefan has been found…, he was held…, the house can be entered…, nobody should be told…",
              50, "Пасив — мова офіційних звітів і таємних операцій."),
 ])

# =====================================================================  21 · Under Control
lesson(21, "Під контролем", "Phrasal verbs + be used to / get used to",
 "У місто приїздить дядько Джон Гілберт, і він знає про вампірів більше, ніж мав би. Стефан після людської крові змінюється: забагато емоцій, забагато енергії і забагато таємниць. Тайлер дедалі частіше вибухає гнівом.",
 A4, ("🎤", "Мікрофон засновників", "Ти бачив(ла), як втрачають контроль — і як його приховують."),
 [
  cards("Попередньо в Містик Фоллс… Під час бурі вампіри зі склепу схопили Стефана. Олена, Деймон і Аларік врятували його, а Олена віддала Стефанові свою кров. Відтоді Стефан відчуває спрагу, якої не знав багато років.",
   [("Джон Гілберт", "John Gilbert", "Дядько Олени і Джеремі. Повертається до міста — і явно знає про вампірів."),
    ("Стефан Сальваторе", "Stefan Salvatore", "Знову п'є людську кров і стверджує, що все під контролем.", "upd"),
    ("Тайлер Локвуд", "Tyler Lockwood", "Дедалі важче стримує гнів. Сам не розуміє чому.", "upd")]),
  gloss("Сцена 1 · Дядько Джон", """
uncle|/ˈʌŋkl/|noun|A1|дядько|Брат батька Олени приїжджає без попередження.|Uncle John is here.|My uncle lives in Canada.
to show up|/ʃəʊ ˈʌp/|phrasal verb|B1|з'явитися (несподівано)|Джон з'являється на порозі.|He just showed up.|She showed up at midnight.
to stay with|/steɪ wɪð/|phrasal verb|A2|зупинитися в когось|Джон хоче пожити в Гілбертів.|He's staying with us.|I'm staying with my aunt.
to get along with|/ɡet əˈlɒŋ wɪð/|phrasal verb|B1|ладнати з|Дженна не ладнає з Джоном.|We don't get along.|I get along with my boss.
to look down on|/lʊk ˈdaʊn ɒn/|phrasal verb|B2|зверхньо ставитися|Джон поводиться зверхньо.|Don't look down on me.|He looks down on poor people.
to keep an eye on|/kiːp ən aɪ ɒn/|idiom|B2|стежити за|Джон стежить за всіма.|I'm keeping an eye on you.|Keep an eye on the soup.
to find out|/faɪnd aʊt/|phrasal verb|B1|дізнатися|Олена хоче дізнатися, що знає Джон.|What did he find out?|We found out the truth.
to bring up|/brɪŋ ˈʌp/|phrasal verb|B2|порушити (тему)|Джон підіймає теми, яких усі уникають.|Don't bring it up.|Don't bring up politics at dinner.
to be up to|/ʌp tuː/|idiom|B2|замишляти|Деймон питає, що задумав Джон.|What's he up to?|What are you up to?
"""),
  gloss("Сцена 2 · Стефан на межі", """
under control|/ˈʌndə kənˈtrəʊl/|phrase|B1|під контролем|Стефан повторює це надто часто.|It's under control.|Everything is under control.
addiction|/əˈdɪkʃn/|noun|B2|залежність|Людська кров для Стефана — залежність.|It's an addiction.|He fought his addiction for years.
to sneak|/sniːk/|verb|B2|робити щось крадькома|Стефан крадькома бере пакети крові.|He sneaks blood bags.|She sneaked into the kitchen.
blood bag|/blʌd bæɡ/|noun|C1|пакет крові (донорської)|Стефан ховає донорську кров.|Blood bags from the hospital.|The hospital needs more blood bags.
to cut back on|/kʌt ˈbæk ɒn/|phrasal verb|C1|зменшити (споживання)|Стефан обіцяє пити менше.|I'll cut back.|I'm cutting back on sugar.
to give in|/ɡɪv ˈɪn/|phrasal verb|B2|піддатися|Стефан піддається спразі.|Don't give in.|She finally gave in and said yes.
to be used to|/biː ˈjuːst tə/|phrase|B2|бути звиклим до|Стефан не звик до людської крові.|I'm not used to it.|I'm used to getting up early.
to get used to|/ɡet ˈjuːst tə/|phrase|B2|звикати до|Олена боїться, що він звикне.|You'll get used to it.|You'll get used to the cold.
mood swings|/muːd swɪŋz/|noun|B2|перепади настрою|Стефан то сміється, то злиться.|What's with the mood swings?|Teenagers have mood swings.
"""),
  gloss("Сцена 3 · Промова і бійка", """
speech|/spiːtʃ/|noun|B1|промова|Стефан виголошує промову на заході засновників.|Give a speech.|The president gave a speech.
to toast|/təʊst/|verb|B2|виголосити тост|Келихи догори на честь міста.|Let's toast to Mystic Falls.|They toasted the bride.
temper|/ˈtempə/|noun|B2|запальність|Тайлер ледве стримується.|Watch your temper.|He has a bad temper.
to lose one's temper|/luːz ˈtempə/|idiom|B2|вийти з себе|Тайлер вибухає на рівному місці.|He lost his temper.|Don't lose your temper with the kids.
to calm down|/kɑːm daʊn/|phrasal verb|B1|заспокоїтися|Друзі намагаються заспокоїти Тайлера.|Calm down, man.|Calm down and listen.
to break up (a fight)|/breɪk ʌp/|phrasal verb|B2|розборонити (бійку)|Хтось мусить розтягнути хлопців.|Break it up!|The teacher broke up the fight.
to blow up|/bləʊ ˈʌp/|phrasal verb|B2|вибухнути (від злості)|Тайлер вибухає гнівом.|He blew up at me.|Dad blew up when he saw my grades.
anger|/ˈæŋɡə/|noun|B1|гнів|Тайлер не розуміє, звідки береться його гнів.|So much anger.|She couldn't hide her anger.
to run in the family|/rʌn ɪn ðə ˈfæməli/|idiom|B2|передаватися в родині|Мер натякає, що запальність Локвудів — родинне.|It runs in the family.|Red hair runs in our family.
"""),
  gram("Stefan isn't ____ human blood. It's dangerous for him.", ["used to drinking", "used to drink", "use to drinking", "used drinking"], 0,
       ["Так! Be used to + -ing = звиклий до.", "Used to drink — колись пив (інше значення).",
        "Use to — без d тут неможливо.", "Бракує to."],
       "be used to + -ing ≠ used to + verb. Одна з найважливіших відмінностей B2.", label="ГРАМАТИКА СЦЕНИ"),
  gram("Don't worry, you'll ____ the new rules soon.", ["get used to", "used to", "be use to", "get use to"], 0,
       ["Так! Get used to = поступово звикати.", "Used to — про минулі звички.",
        "Be use to — неправильна форма.", "Use без -d — помилка."],
       "get used to = процес звикання; be used to = стан «звик».", label="ВИБІР ОЛЕНИ"),
  grimoire("Tyler ____ ____ his temper again. (вийшов із себе, Past)", ["lost his"],
           "Lose one's temper → he lost his temper. Присвійний займенник обов'язковий.", img="crow"),
  page("Dear Diary, Stefan keeps saying he will ____ ____ ____ (зменшить) human blood.", ["cut back on"],
       "Cut back on — фразове дієслово з трьох частин."),
  who("“It's under control.” Who says it — and why is it a red flag?",
      ["Stefan — because he's losing control", "Sheriff Forbes — about the town", "Uncle John — about his car", "Matt — about the Grill"], 0,
      ["Так — Стефан говорить це саме тоді, коли контроль утрачено.",
       "Шериф теж любить цю фразу, але в цій серії вона — Стефанова.",
       "Джон говорить про інше.",
       "Метт ні до чого."],
      "Under control — фраза-попередження, а не заспокоєння."),
  sarcasm("Damon about Uncle John: “Oh, I love family reunions.” What does he mean?",
          ["John's arrival is bad news and Damon is suspicious", "He wants to meet his own family", "He's excited about a party", "He likes John a lot"], 0,
          ["Так — Деймон відчуває загрозу і прикриває її сарказмом.",
           "Свою родину він бачить і так забагато.",
           "Вечірки тут ні до чого.",
           "Джон йому зовсім не подобається."],
          "Family reunion — зустріч родини. З вуст Деймона — тривожний дзвіночок."),
  grill([("to show up", "to arrive unexpectedly"), ("to give in", "to stop resisting"), ("to cut back on", "to use less of"),
         ("to blow up", "to suddenly become very angry"), ("to bring up", "to start talking about a topic")],
        "П'ять фразових дієслів цієї серії."),
  council("Clues: (1) Tyler gets angry very fast; (2) the Mayor says “it runs in the family”; (3) the Lockwood family keeps old secrets; (4) the anger feels stronger than normal. What's the best conclusion for now?",
          ["The Lockwoods might have a family secret of their own", "Tyler is a vampire", "Tyler is just tired", "The Mayor is lying about everything"], 0,
          ["Так — поки що лише підозра: у Локвудів є власна таємниця. Більше ми ще не знаємо.",
           "Ні, Тайлер ходить під сонцем і їсть звичайну їжу.",
           "Втома не пояснює родинну закономірність.",
           "«Про все» — занадто сильно. Мер щось приховує, але не все."],
          "Might have — обережний висновок. Детектив не поспішає з обвинуваченням."),
  compel("Calm down and give me the blood bags",
         "Два фразові накази: calm down + give me. Для тих, хто піддався спразі.",
         scene="Кухня Сальваторе. У холодильнику щось, чого там бути не мало."),
  lie("Who's lying? Stefan: “I'm cutting back.” Tyler: “I don't know why I'm so angry.” Jenna: “I don't trust John.”",
      ["Stefan", "Tyler", "Jenna"], 0,
      ["Так — Стефан не зменшує, а приховує.", "Тайлер справді не розуміє, що з ним.", "Дженна щира."],
      "Present Continuous «I'm cutting back» звучить як процес, якого насправді немає."),
  audio("It's under control.", ["it's under control", "it is under control"],
        "Under control: наголос на -trol: /kənˈtrəʊl/."),
  speak("Let's toast to Mystic Falls.", "Toast to — тост за щось. Підніми уявний келих!"),
  diary_final("Write Elena's diary about Stefan's changes (55+ words). Use at least five phrasal verbs (give in, cut back on, show up, find out, calm down) and both be used to and get used to.",
              55, "Фразові дієслова — серце живої англійської."),
 ])

# =====================================================================  22 · BOSS 4
lesson(22, "Бос арки 4: Ніч біля склепу", "Повторення: майбутні форми, relative clauses, gerund/infinitive, пасив, фразові дієслова",
 "Підсумок арки «Склеп». Вампіри зі склепу планують помсту, Стефан бореться зі спрагою, а в місті з'явився дядько Джон. Тобі доведеться зробити вибір англійською, від якого залежать життя.",
 A4, ("🗝️", "Ключ склепу", "Ти пройшов(ла) четверту арку."),
 [
  gloss("Повторення арки 4 · ключові слова", """
to cast a spell|/kɑːst ə spel/|phrase|B2|накласти заклинання|Бонні і бабуся.|Cast the spell.|She cast a spell.
to be about to|/əˈbaʊt tə/|phrase|B1|от-от|Склеп.|It's about to open.|I'm about to leave.
price|/praɪs/|noun|A2|ціна|Магія.|There's always a price.|What's the price?
to be gone|/ɡɒn/|phrase|B1|зникнути|Кетрін.|She's gone.|The cake is gone!
to fool|/fuːl/|verb|B2|обдурити|Кетрін.|She fooled us.|You can't fool me.
heartbroken|/ˈhɑːtbrəʊkən/|adjective|B2|з розбитим серцем|Деймон.|He's heartbroken.|She was heartbroken.
exhausted|/ɪɡˈzɔːstɪd/|adjective|B2|виснажений|Бабуся.|I'm exhausted.|I'm exhausted after the trip.
to pass away|/pɑːs əˈweɪ/|phrasal verb|B2|відійти|Бабуся.|She passed away.|He passed away in May.
grief|/ɡriːf/|noun|B2|горе|Бонні.|Her grief.|Grief is natural.
to blame|/bleɪm/|verb|B1|звинувачувати|Бонні.|I blame you.|Don't blame me.
funeral|/ˈfjuːnərəl/|noun|B1|похорон|Бабуся.|At the funeral.|A small funeral.
to drown one's sorrows|/draʊn ˈsɒrəʊz/|idiom|C1|заливати горе|Деймон.|Drowning my sorrows.|He drowned his sorrows.
to lash out|/læʃ aʊt/|phrasal verb|C1|зриватися|Деймон.|Don't lash out at me.|She lashed out at me.
pathetic|/pəˈθetɪk/|adjective|B2|жалюгідний|Деймон.|Pathetic.|A pathetic attempt.
birth mother|/bɜːθ ˈmʌðə/|noun|B2|біологічна мати|Олена.|I want to find my birth mother.|She found her birth mother.
to track down|/træk daʊn/|phrasal verb|B2|розшукати|Олена.|I tracked her down.|We tracked him down.
folklore|/ˈfəʊklɔː/|noun|C1|фольклор|Ізобел.|Local folklore.|Irish folklore.
to avenge|/əˈvendʒ/|verb|C1|помститися за|Аларік.|I'll avenge her.|Avenge your family.
to hold a grudge|/həʊld ə ɡrʌdʒ/|idiom|C1|тримати образу|Аларік.|He holds a grudge.|Don't hold a grudge.
to make amends|/meɪk əˈmendz/|idiom|C1|загладити провину|Деймон.|I want to make amends.|Make amends with her.
to stand a chance|/stænd ə tʃɑːns/|idiom|B2|мати шанс|Деймон.|You don't stand a chance.|We stand a chance.
double date|/ˈdʌbl deɪt/|noun|B2|подвійне побачення|Друзі.|Let's go on a double date.|A fun double date.
to avoid|/əˈvɔɪd/|verb|B1|уникати|Олена.|Avoid talking about it.|Avoid the traffic.
to look forward to|/lʊk ˈfɔːwəd/|phrasal verb|B2|чекати з нетерпінням|Друзі.|I'm looking forward to it.|I look forward to it.
to refuse|/rɪˈfjuːz/|verb|B1|відмовитися|Анна.|I refuse to do it.|She refused to go.
to deserve|/dɪˈzɜːv/|verb|B2|заслуговувати|Анна.|You deserve a real life.|You deserve it.
to settle in|/setl ɪn/|phrasal verb|B2|облаштуватися|Перл.|We're settling in.|Settle in first.
to adjust|/əˈdʒʌst/|verb|B2|пристосуватися|Перл.|It's hard to adjust.|I adjusted quickly.
to keep a low profile|/ləʊ ˈprəʊfaɪl/|idiom|C1|не висовуватися|Перл.|Keep a low profile.|Keep a low profile for now.
threat|/θret/|noun|B2|загроза|Вампіри зі склепу.|They're a threat.|A real threat.
to go missing|/ɡəʊ ˈmɪsɪŋ/|phrase|B1|зникнути|Стефан.|He's gone missing.|My phone went missing.
to be held|/held/|passive|B1|утримуватися|Стефан.|He's being held there.|The meeting is held monthly.
owner|/ˈəʊnə/|noun|B1|власник|Правило запрошення.|The owner is dead.|The owner of the car.
to crave|/kreɪv/|verb|C1|жадати|Стефан.|I crave it.|I crave chocolate.
to recover|/rɪˈkʌvə/|verb|B2|відновитися|Стефан.|You'll recover.|He recovered fast.
under control|/ˈʌndə kənˈtrəʊl/|phrase|B1|під контролем|Стефан.|It's under control.|All under control.
addiction|/əˈdɪkʃn/|noun|B2|залежність|Стефан.|It's an addiction.|Internet addiction.
to give in|/ɡɪv ɪn/|phrasal verb|B2|піддатися|Стефан.|Don't give in.|Never give in.
to get used to|/ɡet juːst tə/|phrase|B2|звикати|Олена.|You'll get used to it.|I got used to it.
to lose one's temper|/luːz ˈtempə/|idiom|B2|вийти з себе|Тайлер.|He lost his temper.|I lost my temper.
to run in the family|/rʌn ɪn ðə ˈfæməli/|idiom|B2|передаватися в родині|Локвуди.|It runs in the family.|Music runs in the family.
to show up|/ʃəʊ ʌp/|phrasal verb|B1|з'явитися|Дядько Джон.|He just showed up.|She didn't show up.
"""),
  quest("The tomb vampires are planning something for Founder's Day. Stefan is struggling. Uncle John is watching. Make your choices — in English.", "s1",
   {"s1": ("Pearl asks you to deliver a message to Damon. She says: “We are going to ____ the founding families.” Which verb fits her plan?",
           "Аптека Перл. На полиці — старовинні пляшечки.",
           [("take revenge on", "s2", True, "Так — be going to + план помсти."),
            ("look forward to", "s1b", False, "Look forward to — чекати з нетерпінням. Не те.")]),
    "s1b": ("Pearl frowns. Try again: what do the tomb vampires want?", "Перл чекає.",
            [("Revenge.", "s2", True, "Так."),
             ("A double date.", "end_bad", False, "Перл не смішно.")]),
    "s2": ("You find Stefan with blood bags. He says: “I'm used to ____ it now.” Which form is correct?",
           "Кухня Сальваторе. Стефан ховає погляд.",
           [("drinking", "s3", True, "Be used to + -ing. Граматика правильна — але новина тривожна."),
            ("drink", "s2b", False, "Після be used to потрібне -ing.")]),
    "s2b": ("Correct the sentence: “I'm used to drink it.”", "Друга спроба.",
            [("I'm used to drinking it.", "s3", True, "Тепер правильно."),
             ("I used to drinking it.", "end_bad", False, "Знову помилка — і Стефан іде в ніч.")]),
    "s3": ("What should you say to Stefan?",
           "Ти бачиш, як тремтять його руки.",
           [("You need to stop drinking it. Let us help you.", "s4", True, "Need to + verb; stop + -ing. І турбота."),
            ("You need stop to drink it.", "end_mid", True, "Задум добрий, але граматика підвела. Стефан усе одно чує турботу.")]),
    "s4": ("Uncle John asks about the Salvatores. Describe Damon without telling the secret.",
           "Вітальня Гілбертів. Джон уважно слухає.",
           [("He's a man who loves bourbon and sarcasm.", "s5", True, "Relative clause з who — і нуль зайвої інформації."),
            ("He's a vampire which drinks blood.", "end_bad", False, "Ти видав(ла) таємницю. І which для людей — помилка.")]),
    "s5": ("Bonnie warns you: “Something terrible ____ happen.” Choose the strongest form for 'very soon'.",
           "Бонні тримає тебе за руку. Її долоні холодні.",
           [("is about to", "end_good", True, "Так — be about to: от-от."),
            ("is going", "end_mid", True, "Бракує to — але ти зрозумів(ла) сенс.")])},
   {"end_good": ("Кінцівка: Ти попереджений(а)", "Ти знаєш план Перл, підтримав(ла) Стефана і зберіг(ла) таємницю від дядька Джона. День засновників наближається — і ти до нього готовий(а).", True),
    "end_mid": ("Кінцівка: Майже", "Таємниці в безпеці, але граматика десь кульгала. Пройди ще раз, щоб отримати ідеальну кінцівку.", True),
    "end_bad": ("Кінцівка: Таємницю розкрито", "Через твою помилку хтось дізнався забагато. Спробуй інший шлях!", False)},
   "Квест перевіряє be going to / be about to, be used to + -ing, relative clauses і gerund/infinitive.", img="tomb"),
  grill([("heartbroken", "very sad because of lost love"), ("to avenge", "to punish someone for a wrong"),
         ("addiction", "a habit you can't stop"), ("owner", "the person a house belongs to"),
         ("threat", "something dangerous"), ("folklore", "old stories of a people")],
        "Ключові іменники та дієслова арки 4."),
  grill([("to pass away", "to die (polite)"), ("to track down", "to find after searching"), ("to settle in", "to get comfortable in a new place"),
         ("to give in", "to stop resisting"), ("to lash out", "to attack with words"), ("to show up", "to arrive")],
        "Фразові дієслова арки 4."),
  gram("Pearl is the woman ____ shop was the town's apothecary.", ["whose", "who", "which", "where"], 0,
       ["Так — whose: чия аптека.", "Who — не про приналежність.", "Which — для речей.", "Where — для місця."],
       "Повторення уроку 18.", label="ГРАМАТИКА СЦЕНИ"),
  page("Stefan ____ (find) by Elena, Damon and Alaric. (пасив, Past Simple)", ["was found"],
       "Повторення уроку 20: was + V3."),
  grimoire("Jeremy decided ____ ____ (попросити) Anna. (to + verb)", ["to ask"],
           "Decide + to + verb. Повторення уроку 19.", img="candles"),
  lie("Who is lying? Stefan: “I'm used to it, it's fine.” Bonnie: “I blame the vampires.” Alaric: “I'm here to help.”",
      ["Stefan", "Bonnie", "Alaric"], 0,
      ["Так — «it's fine» після тривожного зізнання видає його.",
       "Бонні справді звинувачує вампірів.",
       "Аларік справді прийшов допомогти — він ризикував життям заради Стефана."],
      "Повторення: fine/okay наприкінці тривожної фрази — маркер."),
  sarcasm("Damon: “Uncle John. My favourite person.” What does he mean?",
          ["He strongly dislikes and distrusts John", "John is his favourite", "He wants to adopt John", "John is a relative of Damon"], 0,
          ["Так — сарказм класичний: «улюблена людина» = найнеприємніша.", "Ні.", "Ні.", "Ні, Джон — родич Олени."],
          "Повторення: перебільшено позитивні слова = протилежний зміст."),
 ])
