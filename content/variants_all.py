# Lessons 2–16 written natively for Polish and Ukrainian as target languages.
# Base fields (q, options, say) are in the TARGET language; *_en/_uk/_pl are the support language.
import json, importlib.util, os

HERE = os.path.dirname(os.path.abspath(__file__))

TITLE_EN = {1:"The Boy Under the Stairs",2:"Trouble at the Zoo",3:"Letters from Nowhere",4:"The Keeper of Keys",5:"The Magic Shopping Street",6:"The Wand Chooses the Wizard",7:"Platform Nine and Three-Quarters",8:"The Sorting Hat",9:"The Potions Lesson",10:"The First Flying Lesson",11:"A Troll in the Dungeons",12:"The First Match",13:"The Mirror of Desire",14:"The Forbidden Forest",15:"Through the Trapdoor",16:"Finale: the Stone and Your Story"}
SCENE_EN = {1:"An ordinary suburban house. A boy lives in the cupboard under the stairs while the family celebrates his cousin's birthday.",2:"The family takes the boy to the zoo. At the glass of a huge snake something strange happens: the glass suddenly vanishes.",3:"Letters start arriving for the boy. His uncle destroys them, but the next day there are even more.",4:"A stormy night on an island. A giant breaks down the door, brings a cake and tells the boy the truth about his parents.",5:"The giant leads the boy to a hidden street of shops: a bank, robes, books, cauldrons.",6:"An old wand shop. The boy tries several wands until one chooses him.",7:"A London station. The boy looks for a platform that doesn't exist, then meets a new friend on the train.",8:"A great hall with candles under the ceiling. An old hat decides which house each student joins.",9:"Cold dungeons and a strict teacher who asks the boy hard questions in the first lesson.",10:"Students hold broomsticks for the first time. One boy falls, another grabs his thing and soars high.",11:"Halloween. A troll has got into the school and a girl is alone in the bathroom.",12:"A pitch with hoops on tall posts and fans in the stands. The boy plays his first match as Seeker.",13:"An empty room at night. The boy finds a mirror that shows not a reflection but his deepest wish.",14:"A night detention in a dark forest. The boys see something terrible and a centaur saves them.",15:"Three friends pass tests under the school: giant chess, a potion riddle and fire.",16:"A last meeting at the mirror, a red stone in a pocket and the farewell feast. You tell the story yourself."}

def W(word, en, uk, pl):
    return (word, en, uk, pl)

def lesson(lang, num, gram, words, voc, lis, gr1, gr2, order, typ, tf, speak):
    """gram: dict en/uk/pl grammar label. Each task arg is a tuple, tips are (en, uk, pl)."""
    same = lang  # support language equal to target -> definition column
    tasks = []
    WEL = {"pl": ("Lekcja %d. Wchodzimy do kolejnej sceny!", "Lesson %d. Into the next scene!", "Урок %d. Вирушаємо в наступну сцену!", "Lekcja %d. Wchodzimy do kolejnej sceny!"),
           "uk": ("Урок %d. Вирушаємо в наступну сцену!", "Lesson %d. Into the next scene!", "Урок %d. Вирушаємо в наступну сцену!", "Lekcja %d. Wchodzimy do kolejnej sceny!")}[lang]
    LN = {"pl": {"en":"Polish","uk":"польських","pl":""}, "uk": {"en":"Ukrainian","uk":"","pl":"ukraińskich"}}[lang]
    tasks.append({"type":"intro","img":None,
        "q":WEL[0] % num, "q_en":WEL[1] % num, "q_uk":WEL[2] % num, "q_pl":WEL[3] % num,
        "options_en":["%d new %s words from the scene" % (len(words), LN["en"]), "Listening at natural speed", "Grammar: " + gram["en"], "Speaking: say a line from the scene"],
        "options_uk":["%d нових %sслів зі сцени" % (len(words), (LN["uk"] + " ") if LN["uk"] else ""), "Аудіювання в природному темпі", "Граматика: " + gram["uk"], "Говоріння: скажи фразу зі сцени"],
        "options_pl":["%d nowych %ssłów ze sceny" % (len(words), (LN["pl"] + " ") if LN["pl"] else ""), "Słuchanie w naturalnym tempie", "Gramatyka: " + gram["pl"], "Mówienie: powiedz kwestię ze sceny"],
        "tip":"Start","tip_en":"Start the lesson","tip_uk":"Почати урок","tip_pl":"Zacznij lekcję"})
    MQ = {"pl":"Połącz słowa ze sceny z ich znaczeniem.","uk":"З'єднай слова зі сцени з їхнім значенням."}[lang]
    m = {"type":"match","q":MQ}
    for s in ("en","uk","pl"):
        idx = {"en":1,"uk":2,"pl":3}[s]
        m["options_" + s] = ["%s=%s" % (w[0], w[idx]) for w in words]
    m["tip_en"], m["tip_uk"], m["tip_pl"] = voc[3]
    m["tip_en"] = words_tip(lang, "en"); m["tip_uk"] = words_tip(lang, "uk"); m["tip_pl"] = words_tip(lang, "pl")
    tasks.append(m)
    def mc(type_, t, extra=None):
        d = {"type":type_, "q":t[0], "options":t[1], "answer":t[2], "tip_en":t[3][0], "tip_uk":t[3][1], "tip_pl":t[3][2]}
        if extra: d.update(extra)
        return d
    tasks.append(mc("vocabulary", voc))
    tasks.append(mc("listening", lis[:4], {"say": lis[4]}))
    tasks.append(mc("grammar", gr1))
    tasks.append(mc("grammar", gr2))
    OQ = {"pl":"Ułóż zdanie.","uk":"Склади речення."}[lang]
    BUILD = {"en":"Build the sentence: “%s”","uk":"Склади речення: «%s»","pl":"Ułóż zdanie: „%s”"}
    o = {"type":"order","q":OQ,"options":order[0],"tip_en":order[2][0],"tip_uk":order[2][1],"tip_pl":order[2][2]}
    for s in ("en","uk","pl"):
        o["q_" + s] = BUILD[s] % (" ".join(order[0]) if s == lang else order[1][s])
    tasks.append(o)
    ty = {"type":"type","q":typ[0],"options":typ[1],"tip_en":typ[3][0],"tip_uk":typ[3][1],"tip_pl":typ[3][2]}
    for s in ("en","uk","pl"):
        ty["q_" + s] = "%s (%s)" % (typ[0], typ[2][s])
    tasks.append(ty)
    tasks.append({"type":"tf","q":tf[0],"options":["True","False"],"answer":tf[1],"tip_en":tf[2][0],"tip_uk":tf[2][1],"tip_pl":tf[2][2]})
    SQ = {"pl":"Powiedz na głos: <i>„%s”</i>","uk":"Скажи вголос: <i>«%s»</i>"}[lang]
    tasks.append({"type":"speaking","q":SQ % speak[0],"say":speak[0],"tip_en":speak[1][0],"tip_uk":speak[1][1],"tip_pl":speak[1][2]})
    for tk in tasks:
        if tk.get("img") is None: tk.pop("img", None)
    return tasks

def words_tip(lang, s):
    return {"en":"Say each new word out loud as you match it: it sticks better.",
            "uk":"Промовляй кожне нове слово вголос, коли з'єднуєш: так воно краще запам'ятовується.",
            "pl":"Wypowiadaj każde nowe słowo na głos, gdy je łączysz: lepiej zostaje w pamięci."}[s]

X = ("", "", "")  # placeholder tip (unused)

PL, UK, GR = {}, {}, {}

# ---------------- 2 ----------------
GR[2] = {"pl":{"en":"Past tense: -łem / -łam / -ł / -ła","uk":"Минулий час: -łem / -łam / -ł / -ła","pl":"Czas przeszły: -łem / -łam / -ł / -ła"},
         "uk":{"en":"Past tense: -в / -ла / -ли","uk":"Минулий час: -в / -ла / -ли","pl":"Czas przeszły: -в / -ла / -ли"}}
PL[2] = lesson("pl", 2, GR[2]["pl"],
 [W("wąż","snake","змія","długie zwierzę bez nóg"), W("szyba","glass pane","скло, шибка","szkło w oknie lub w terrarium"), W("zniknąć","to vanish","зникнути","przestać być widocznym"), W("krzyczeć","to scream","кричати","mówić bardzo głośno ze strachu"), W("uciec","to escape","втекти","szybko się wydostać")],
 ("Szkło nagle <b>zniknęło</b>. Co to znaczy?", ["Szkło się stłukło", "Szkła już nie było", "Szkło było brudne", "Szkło było grube"], 1,
  ("Zniknąć = to vanish: it was there, then it wasn't.", "Zniknąć = зникнути: було — і раптом немає.", "Zniknąć = przestać być widocznym, jakby się rozpłynęło.")),
 ("Posłuchaj. Co zrobił wąż?", ["Zasnął", "Uciekł z terrarium", "Zjadł obiad", "Ugryzł kuzyna"], 1,
  ("The snake slid out and escaped. Listen for wypełzł and uciekł.", "Змія виповзла й утекла. Шукай на слух wypełzł і uciekł.", "Wąż wypełzł i uciekł. Wsłuchaj się w czasowniki."),
  "Szyba zniknęła, a wąż wypełzł i uciekł. Kuzyn krzyczał bardzo głośno."),
 ("Wczoraj Harry ____ w zoo. (on)", ["był", "była", "byłem", "byli"], 0,
  ("Past tense of być for on (he): był. Ona była, ja byłem, oni byli.", "Минулий час від być для on (він): był. Ona była, ja byłem, oni byli.", "On był, ona była, ja byłem (mężczyzna), oni byli.")),
 ("Ciocia Petunia ____ bardzo zła.", ["była", "był", "byłam", "było"], 0,
  ("Feminine 3rd person: -ła. Ciocia → ona → była.", "Жіночий рід, 3-тя особа: -ła. Ciocia → ona → była, як і в нас «була».", "Rodzaj żeński: ona była, ona krzyczała.")),
 (["Wąż", "nagle", "wypełzł", "z", "terrarium"], {"en":"The snake suddenly crawled out of the terrarium.","uk":"Змія раптом виповзла з тераріуму.","pl":""},
  ("Z (out of) + genitive: z terrarium, z domu, z zoo.", "Z (з) + родовий відмінок: z terrarium, z domu.", "Z + dopełniacz: z terrarium, z domu.")),
 ("Harry ____ z wężem. (rozmawiać, on)", ["rozmawiał"], {"en":"talked","uk":"розмовляв","pl":"rozmawiać, on"},
  ("Past tense, masculine: take the stem rozmawia- and add -ł.", "Минулий час, чоловічий рід: основа rozmawia- + -ł, як «розмовля-в».", "Czas przeszły: rozmawia- + -ł = rozmawiał.")),
 ("Prawda czy fałsz? Wąż był w zoo bardzo szczęśliwy.", 1,
  ("False: the snake had never seen Brazil and was bored behind the glass.", "Неправда: змія нудьгувала за склом і ніколи не бачила Бразилії.", "Fałsz: wąż nudził się za szybą i nigdy nie widział Brazylii.")),
 ("Szyba zniknęła i wąż uciekł.", ("ę in zniknęła sounds like a nasal 'en'. Keep ł soft, like English 'w'.", "ę у zniknęła — носове «ен», ł звучить як українське «в» в кінці «був».", "Uważaj na ę i ł: zniknęła, uciekł.")))
UK[2] = lesson("uk", 2, GR[2]["uk"],
 [W("змія","snake","długie zwierzę bez nóg → ","wąż"), W("скло","glass","прозорий матеріал у вікні","szkło, szyba"), W("зникнути","to vanish","перестати бути видимим","zniknąć"), W("кричати","to scream","голосно говорити від страху","krzyczeć"), W("втекти","to escape","швидко вибратися","uciec")],
 ("Скло раптом <b>зникло</b>. Що це означає?", ["Скло розбилося", "Скла більше не було", "Скло було брудне", "Скло було товсте"], 1,
  ("Зникнути = to vanish: it was there, then it wasn't.", "Зникнути — перестати бути видимим, ніби розтанути.", "Зникнути = zniknąć: było i nagle nie ma.")),
 ("Послухай. Що зробила змія?", ["Заснула", "Втекла з тераріуму", "Пообідала", "Вкусила кузена"], 1,
  ("The snake crawled out and escaped. Listen for виповзла and втекла.", "Змія виповзла і втекла. Слухай дієслова.", "Wąż wypełzł i uciekł. Słuchaj: виповзла, втекла."),
  "Скло зникло, а змія виповзла і втекла. Кузен дуже голосно кричав."),
 ("Учора Гаррі ____ в зоопарку.", ["був", "була", "були", "було"], 0,
  ("Past tense of бути for він (he): був. Вона була, вони були.", "Він був, вона була, воно було, вони були.", "Czas przeszły od бути dla він (on): був = był. Вона була = była.")),
 ("Тітка Петунія ____ дуже сердита.", ["була", "був", "було", "були"], 0,
  ("Feminine past ends in -ла: вона була, вона кричала.", "Жіночий рід у минулому: -ла: була, кричала.", "Rodzaj żeński: -ла, jak polskie -ła: була = była.")),
 (["Змія", "раптом", "виповзла", "з", "тераріуму"], {"en":"The snake suddenly crawled out of the terrarium.","uk":"","pl":"Wąż nagle wypełzł z terrarium."},
  ("З (out of) + genitive: з тераріуму, з дому.", "З + родовий відмінок: з тераріуму, з дому.", "З + dopełniacz, jak po polsku: з тераріуму = z terrarium.")),
 ("Гаррі ____ зі змією. (розмовляти, він)", ["розмовляв"], {"en":"talked","uk":"розмовляти, він","pl":"rozmawiał"},
  ("Masculine past: stem розмовля- + -в.", "Чоловічий рід, минулий час: розмовля- + -в = розмовляв.", "Czas przeszły, rodzaj męski: -в, jak polskie -ł: розмовляв = rozmawiał.")),
 ("Правда чи неправда? Змії в зоопарку було дуже весело.", 1,
  ("False: the snake was bored behind the glass and had never seen Brazil.", "Неправда: змія нудьгувала за склом і ніколи не бачила Бразилії.", "Fałsz: wąż nudził się za szybą i nigdy nie widział Brazylii.")),
 ("Скло зникло, і змія втекла.", ("Ukrainian г is a soft breathy 'h'; и is a short 'i' as in 'sit'.", "Чітко вимовляй «зникло» і «втекла».", "Ukraińskie и brzmi jak polskie y: зникло ≈ znykło.")))
# fix match word 1 for UK (uk definition)
UK[2][1]["options_uk"][0] = "змія=довга тварина без ніг"

# ---------------- 3 ----------------
GR[3] = {"pl":{"en":"Verb aspect: pisać / napisać","uk":"Вид дієслова: pisać / napisać","pl":"Aspekt: pisać / napisać"},
         "uk":{"en":"Verb aspect: писати / написати","uk":"Вид дієслова: писати / написати","pl":"Aspekt: писати / написати"}}
PL[3] = lesson("pl", 3, GR[3]["pl"],
 [W("list","letter","лист","wiadomość na papierze"), W("koperta","envelope","конверт","papier, w którym jest list"), W("wujek","uncle","дядько","brat mamy lub taty"), W("spalić","to burn","спалити","zniszczyć ogniem"), W("komin","chimney","комин","przez niego wychodzi dym")],
 ("Na kopercie jest <b>adres</b>. Co to jest?", ["Imię kota", "Miejsce, gdzie ktoś mieszka", "Data urodzin", "Cena znaczka"], 1,
  ("Adres = address: the place where someone lives.", "Adres = адреса: місце, де хтось живе.", "Adres to miejsce zamieszkania: ulica, dom, miasto.")),
 ("Posłuchaj. Skąd wpadają listy?", ["Przez okno", "Przez komin", "Pod drzwiami", "Z lodówki"], 1,
  ("Przez komin = through the chimney. Hundreds of letters fly in!", "Przez komin = через комин. Сотні листів!", "Listy wlatują przez komin, setki listów!"),
  "Setki listów wlatują przez komin! Wujek jest wściekły."),
 ("Wujek ____ wszystkie listy i wyrzucił je do ognia. (finished action)", ["zebrał", "zbierał", "zbiera", "zbierać"], 0,
  ("Perfective zebrał = he gathered them (done, result). Imperfective zbierał = was gathering.", "Доконаний вид zebrał = зібрав (результат). Недоконаний zbierał = збирав.", "Aspekt dokonany: zebrał (skończone). Niedokonany: zbierał (proces).")),
 ("Każdego dnia sowy ____ nowe listy. (repeated action)", ["przynosiły", "przyniosły", "przyniosą", "przynieść"], 0,
  ("Repeated action → imperfective: przynosiły (used to bring, every day).", "Повторювана дія → недоконаний вид: przynosiły (приносили щодня).", "Czynność powtarzana → aspekt niedokonany: przynosiły.")),
 (["Harry", "w końcu", "przeczytał", "swój", "list"], {"en":"Harry finally read his letter.","uk":"Гаррі нарешті прочитав свій лист.","pl":""},
  ("Przeczytał (perfective): he read it to the end. W końcu = finally.", "Przeczytał (доконаний) — прочитав до кінця. W końcu = нарешті.", "Przeczytał: czynność zakończona. W końcu = nareszcie.")),
 ("Wujek ____ list, zanim Harry go otworzył. (spalić, on)", ["spalił"], {"en":"burned","uk":"спалив","pl":"spalić, on"},
  ("Spalić is perfective: spalił = burned (completely).", "Spalić — доконаний вид: spalił = спалив.", "Spalić (dokonany) → spalił.")),
 ("Prawda czy fałsz? Wujek chętnie dał Harry'emu list.", 1,
  ("False: he tore up and burned the letters and even moved the family to an island.", "Неправда: він рвав і палив листи й навіть утік з родиною на острів.", "Fałsz: darł i palił listy, a nawet uciekł z rodziną na wyspę.")),
 ("Setki listów wlatują przez komin!", ("Setki and listów: the genitive plural after numbers like setki.", "Setki listów — «сотні листів», родовий після числівника.", "Setki + dopełniacz: setki listów.")))
UK[3] = lesson("uk", 3, GR[3]["uk"],
 [W("лист","letter","повідомлення на папері","list"), W("конверт","envelope","папір, у якому лежить лист","koperta"), W("дядько","uncle","брат мами чи тата","wujek"), W("спалити","to burn","знищити вогнем","spalić"), W("комин","chimney","через нього виходить дим","komin")],
 ("На конверті є <b>адреса</b>. Що це?", ["Ім'я кота", "Місце, де хтось живе", "Дата народження", "Ціна марки"], 1,
  ("Адреса = address: the place where someone lives.", "Адреса — місце проживання: вулиця, будинок, місто.", "Адреса = adres: miejsce zamieszkania.")),
 ("Послухай. Звідки летять листи?", ["Через вікно", "Через комин", "З-під дверей", "З холодильника"], 1,
  ("Через комин = through the chimney. Hundreds of letters!", "Сотні листів летять через комин!", "Через комин = przez komin. Setki listów!"),
  "Сотні листів летять через комин! Дядько страшенно злий."),
 ("Дядько ____ всі листи і кинув їх у вогонь. (завершена дія)", ["зібрав", "збирав", "збирає", "збирати"], 0,
  ("Perfective зібрав = gathered (done, result). Imperfective збирав = was gathering.", "Доконаний вид «зібрав» — дію завершено, є результат.", "Aspekt dokonany: зібрав = zebrał. Niedokonany: збирав = zbierał.")),
 ("Щодня сови ____ нові листи. (повторювана дія)", ["приносили", "принесли", "принесуть", "принести"], 0,
  ("Repeated action → imperfective: приносили (brought every day).", "Повторювана дія → недоконаний вид: приносили.", "Czynność powtarzana → niedokonany: приносили = przynosiły.")),
 (["Гаррі", "нарешті", "прочитав", "свій", "лист"], {"en":"Harry finally read his letter.","uk":"","pl":"Harry w końcu przeczytał swój list."},
  ("Прочитав (perfective): read to the end. Нарешті = finally.", "Прочитав — доконаний вид. Нарешті — після довгого чекання.", "Прочитав = przeczytał (dokonany). Нарешті = w końcu.")),
 ("Дядько ____ лист, перш ніж Гаррі його відкрив. (спалити, він)", ["спалив"], {"en":"burned","uk":"спалити, він","pl":"spalił"},
  ("Спалити is perfective: спалив = burned completely.", "Спалити — доконаний вид: спалив.", "Спалити (dokonany) → спалив = spalił.")),
 ("Правда чи неправда? Дядько охоче віддав Гаррі лист.", 1,
  ("False: he tore up and burned the letters and even fled to an island.", "Неправда: він рвав і палив листи й навіть утік на острів.", "Fałsz: darł i palił listy, a nawet uciekł na wyspę.")),
 ("Сотні листів летять через комин!", ("Ukrainian и in листів sounds like a short 'i' in 'sit'.", "Чітко вимовляй «сотні листів».", "и w листів brzmi jak polskie y.")))

# ---------------- 4 ----------------
GR[4] = {"pl":{"en":"Reported speech: powiedział, że…","uk":"Непряма мова: powiedział, że…","pl":"Mowa zależna: powiedział, że…"},
         "uk":{"en":"Reported speech: сказав, що…","uk":"Непряма мова: сказав, що…","pl":"Mowa zależna: сказав, що…"}}
PL[4] = lesson("pl", 4, GR[4]["pl"],
 [W("olbrzym","giant","велетень","bardzo, bardzo duży człowiek"), W("burza","storm","буря","silny wiatr, deszcz i grzmoty"), W("drzwi","door","двері","przez nie wchodzisz do domu"), W("tort","cake","торт","słodkie ciasto na urodziny"), W("czarodziej","wizard","чарівник","ktoś, kto umie czarować")],
 ("Olbrzym <b>wyważył</b> drzwi. Co zrobił?", ["Pomalował je", "Otworzył je siłą", "Zamknął na klucz", "Zapukał cicho"], 1,
  ("Wyważyć drzwi = to break the door down by force.", "Wyważyć drzwi = вибити двері силою.", "Wyważyć drzwi = otworzyć je siłą.")),
 ("Posłuchaj. Co Hagrid przyniósł Harry'emu?", ["Książkę", "Tort urodzinowy", "Miotłę", "Sowę"], 1,
  ("Tort urodzinowy = birthday cake. Wszystkiego najlepszego = happy birthday.", "Tort urodzinowy = торт на день народження.", "Tort urodzinowy i życzenia: wszystkiego najlepszego!"),
  "Wszystkiego najlepszego, Harry! Przyniosłem ci tort urodzinowy."),
 ("Hagrid: „Jesteś czarodziejem.” → Hagrid powiedział, że Harry ____ czarodziejem.", ["jest", "był", "będzie", "jestem"], 0,
  ("Polish keeps the original tense after że: powiedział, że jest (no backshift!).", "У польській після że час не змінюється: powiedział, że jest — як і в українській.", "Po że zostaje ten sam czas: powiedział, że jest.")),
 ("Harry zapytał, ____ jego rodzice byli czarodziejami.", ["czy", "że", "co", "gdzie"], 0,
  ("Reported yes/no question: zapytał, czy… (asked whether…).", "Непряме загальне питання: zapytał, czy… (спитав, чи…).", "Pytanie zależne tak/nie: zapytał, czy…")),
 (["Hagrid", "powiedział", "że", "Harry", "jest", "sławny"], {"en":"Hagrid said that Harry is famous.","uk":"Хагрід сказав, що Гаррі відомий.","pl":""},
  ("Że = that. A comma always goes before że in Polish.", "Że = що. Перед że завжди кома.", "Przed że zawsze stawiamy przecinek.")),
 ("Wujek krzyknął, ____ Harry nigdzie nie pojedzie.", ["że"], {"en":"that","uk":"що","pl":"spójnik"},
  ("Że introduces reported statements: krzyknął, że…", "Że вводить непряму мову: krzyknął, że… (крикнув, що…).", "Że wprowadza mowę zależną.")),
 ("Prawda czy fałsz? Harry od zawsze wiedział, że jest czarodziejem.", 1,
  ("False: he learned it from Hagrid on his 11th birthday.", "Неправда: він дізнався про це від Хагріда на 11-й день народження.", "Fałsz: dowiedział się od Hagrida w swoje 11. urodziny.")),
 ("Hagrid powiedział, że jestem czarodziejem.", ("rz in powiedział? No: it's ie + dz. Say it smoothly: po-wie-dział.", "Powiedział читається «по-вє-джяв».", "Powiedział: wymawiaj płynnie, ł jak u.")))
UK[4] = lesson("uk", 4, GR[4]["uk"],
 [W("велетень","giant","дуже-дуже велика людина","olbrzym"), W("буря","storm","сильний вітер, дощ і грім","burza"), W("двері","door","через них заходиш у дім","drzwi"), W("торт","cake","солодкий пиріг на свято","tort"), W("чарівник","wizard","той, хто вміє чаклувати","czarodziej")],
 ("Велетень <b>вибив</b> двері. Що він зробив?", ["Пофарбував їх", "Відчинив силою", "Замкнув на ключ", "Тихо постукав"], 1,
  ("Вибити двері = to break the door down.", "Вибити двері — відчинити їх силою.", "Вибити двері = wyważyć drzwi.")),
 ("Послухай. Що Хагрід приніс Гаррі?", ["Книжку", "Торт на день народження", "Мітлу", "Сову"], 1,
  ("Торт = cake. З днем народження = happy birthday.", "Торт на день народження і привітання.", "Торт = tort. З днем народження = wszystkiego najlepszego."),
  "З днем народження, Гаррі! Я приніс тобі торт."),
 ("Хагрід: «Я приніс торт». → Хагрід сказав, що він ____ торт.", ["приніс", "приносить", "принесе", "принести"], 0,
  ("Ukrainian keeps the original tense after що: no backshift.", "Після «що» час не змінюється: сказав, що приніс.", "Po що czas się nie zmienia, jak po polsku po że.")),
 ("Гаррі спитав, ____ його батьки були чарівниками.", ["чи", "що", "де", "коли"], 0,
  ("Reported yes/no question: спитав, чи… (asked whether…).", "Непряме загальне питання: спитав, чи…", "Pytanie zależne: спитав, чи… = zapytał, czy…")),
 (["Хагрід", "сказав", "що", "Гаррі", "дуже", "відомий"], {"en":"Hagrid said that Harry is very famous.","uk":"","pl":"Hagrid powiedział, że Harry jest bardzo sławny."},
  ("Що = that. Put a comma before що.", "Перед «що» ставимо кому.", "Що = że. Przed що przecinek.")),
 ("Дядько крикнув, ____ Гаррі нікуди не поїде.", ["що"], {"en":"that","uk":"сполучник","pl":"że"},
  ("Що introduces reported statements.", "«Що» вводить непряму мову.", "Що = że: krzyknął, że…")),
 ("Правда чи неправда? Гаррі завжди знав, що він чарівник.", 1,
  ("False: he learned it from Hagrid on his 11th birthday.", "Неправда: дізнався від Хагріда на свій 11-й день народження.", "Fałsz: dowiedział się od Hagrida w 11. urodziny.")),
 ("Хагрід сказав, що я чарівник.", ("ч is 'ch', р is rolled.", "Чітко: чарівник, сказав.", "ч = cz, р wibrujące jak polskie r.")))

# ---------------- 5 ----------------
GR[5] = {"pl":{"en":"Quantities: dużo / mało / kilka + genitive","uk":"Кількість: dużo / mało / kilka + родовий","pl":"Ilość: dużo / mało / kilka + dopełniacz"},
         "uk":{"en":"Quantities: багато / мало / кілька + genitive","uk":"Кількість: багато / мало / кілька + родовий","pl":"Ilość: багато / мало / кілька + dopełniacz"}}
PL[5] = lesson("pl", 5, GR[5]["pl"],
 [W("sklep","shop","крамниця","miejsce, gdzie się coś kupuje"), W("bank","bank","банк","tu trzyma się pieniądze"), W("kociołek","cauldron","казанок","garnek do eliksirów"), W("szata","robe","мантія","długie ubranie czarodzieja"), W("pieniądze","money","гроші","tym płacisz w sklepie")],
 ("Harry ma <b>za mało</b> pieniędzy? Nie! W banku ma ich…", ["bardzo dużo", "zero", "trochę za mało", "tylko jedną monetę"], 0,
  ("Za mało = too little; bardzo dużo = very much. His parents left him gold.", "Za mało = замало; bardzo dużo = дуже багато. Батьки залишили йому золото.", "Za mało ≠ bardzo dużo. Rodzice zostawili mu złoto.")),
 ("Posłuchaj. Ile kosztuje różdżka?", ["Siedem galeonów", "Dwa sykle", "Sto galeonów", "Nic"], 0,
  ("Siedem galeonów: after 5+ the noun is genitive plural.", "Siedem galeonów: після 5+ іменник у родовому множини.", "Siedem + dopełniacz l.mn.: siedem galeonów."),
  "Ta różdżka kosztuje siedem galeonów. To niedużo za tak dobrą różdżkę."),
 ("Na ulicy było dużo ____.", ["sklepów", "sklepy", "sklep", "sklepami"], 0,
  ("Dużo + genitive plural: dużo sklepów.", "Dużo + родовий множини: dużo sklepów (багато крамниць).", "Dużo + dopełniacz: dużo sklepów.")),
 ("Harry kupił trzy ____.", ["książki", "książek", "książka", "książkami"], 0,
  ("2, 3, 4 take nominative plural: trzy książki. 5+ takes genitive: pięć książek.", "2, 3, 4 + називний множини: trzy książki; 5+ — родовий: pięć książek. Як у нас: три книжки, п'ять книжок.", "2–4 + mianownik: trzy książki; 5+ dopełniacz: pięć książek.")),
 (["Na", "ulicy", "jest", "mnóstwo", "czarodziejów"], {"en":"There are loads of wizards on the street.","uk":"На вулиці безліч чарівників.","pl":""},
  ("Mnóstwo = loads of, + genitive plural.", "Mnóstwo = безліч, + родовий множини.", "Mnóstwo + dopełniacz l.mn.")),
 ("Harry nie ma ani jednej ____. (sowa)", ["sowy"], {"en":"owl","uk":"сова","pl":"sowa"},
  ("After negation (nie ma) Polish uses genitive: nie ma sowy.", "Після заперечення nie ma — родовий: nie ma sowy (немає сови).", "Po przeczeniu dopełniacz: nie ma sowy.")),
 ("Prawda czy fałsz? Harry kupił sowę.", 1,
  ("False: Hagrid bought him the owl as a birthday present.", "Неправда: сову йому подарував Хагрід.", "Fałsz: sowę kupił mu Hagrid w prezencie.")),
 ("Ile kosztuje ten kociołek?", ("Ile = how much/many. ó in kociołek? No: o + ł.", "Ile kosztuje — скільки коштує.", "Pytanie o cenę: ile kosztuje…?")))
UK[5] = lesson("uk", 5, GR[5]["uk"],
 [W("крамниця","shop","місце, де щось купують","sklep"), W("банк","bank","тут зберігають гроші","bank"), W("казанок","cauldron","горщик для зілля","kociołek"), W("мантія","robe","довгий одяг чарівника","szata"), W("гроші","money","ними платять у крамниці","pieniądze")],
 ("У Гаррі <b>замало</b> грошей? Ні! У банку їх…", ["дуже багато", "нуль", "трохи замало", "лише одна монета"], 0,
  ("Замало = too little; дуже багато = very much.", "Замало ≠ дуже багато. Батьки залишили йому золото.", "Замало = za mało; дуже багато = bardzo dużo.")),
 ("Послухай. Скільки коштує паличка?", ["Сім галеонів", "Два серпики", "Сто галеонів", "Нічого"], 0,
  ("Сім галеонів: after 5+ the noun is genitive plural.", "Сім + родовий множини: сім галеонів.", "Сім галеонів = siedem galeonów (dopełniacz)."),
  "Ця паличка коштує сім галеонів. Це небагато за таку гарну паличку."),
 ("На вулиці було багато ____.", ["крамниць", "крамниці", "крамниця", "крамницями"], 0,
  ("Багато + genitive plural: багато крамниць.", "Багато + родовий множини: багато крамниць.", "Багато + dopełniacz: багато крамниць = dużo sklepów.")),
 ("Гаррі купив три ____.", ["книжки", "книжок", "книжка", "книжками"], 0,
  ("2, 3, 4 take nominative plural (три книжки); 5+ genitive (п'ять книжок).", "2–4: три книжки; 5+: п'ять книжок.", "2–4 + mianownik: три книжки; 5+ dopełniacz: п'ять книжок.")),
 (["На", "вулиці", "безліч", "різних", "чарівників"], {"en":"There are loads of different wizards on the street.","uk":"","pl":"Na ulicy jest mnóstwo różnych czarodziejów."},
  ("Безліч = loads of, + genitive plural.", "Безліч + родовий множини.", "Безліч = mnóstwo, + dopełniacz.")),
 ("У Гаррі немає жодної ____. (сова)", ["сови"], {"en":"owl","uk":"сова","pl":"sowa"},
  ("After немає Ukrainian uses genitive: немає сови.", "Після «немає» — родовий: немає сови.", "Po немає dopełniacz, jak po polsku: nie ma sowy.")),
 ("Правда чи неправда? Гаррі сам купив собі сову.", 1,
  ("False: Hagrid gave him the owl as a birthday present.", "Неправда: сову подарував Хагрід.", "Fałsz: sowę dał mu Hagrid w prezencie.")),
 ("Скільки коштує цей казанок?", ("Stress: СКІЛЬки, КОШтує, казаНОК.", "Наголоси: скільки, коштує, казанок.", "Akcent: СКІЛЬки, КОШтує, казаНОК.")))

# ---------------- 6 ----------------
GR[6] = {"pl":{"en":"Relative clauses: który / która / które","uk":"Підрядні: który / która / które","pl":"Zdania względne: który / która / które"},
         "uk":{"en":"Relative clauses: який / яка / яке","uk":"Підрядні: який / яка / яке","pl":"Zdania względne: який / яка / яке"}}
PL[6] = lesson("pl", 6, GR[6]["pl"],
 [W("różdżka","wand","чарівна паличка","patyk do czarowania"), W("sprzedawca","seller","продавець","osoba, która sprzedaje"), W("pudełko","box","коробка","w nim coś leży"), W("pióro","feather","перо","rośnie ptakom"), W("wybierać","to choose","обирати","decydować, co wziąć")],
 ("Różdżka <b>wybiera</b> czarodzieja. Co to znaczy?", ["Czarodziej jej szuka", "Różdżka decyduje", "Różdżka się psuje", "Różdżka jest tania"], 1,
  ("Wybierać = to choose. Here the wand decides!", "Wybierać = обирати. Тут вирішує паличка!", "Wybierać = decydować. Tu decyduje różdżka.")),
 ("Posłuchaj. Co jest w środku różdżki Harry'ego?", ["Włos jednorożca", "Pióro feniksa", "Smocze serce", "Złoto"], 1,
  ("Pióro feniksa = phoenix feather.", "Pióro feniksa = перо фенікса.", "Pióro feniksa — jak różdżka Voldemorta!"),
  "Ta różdżka ma w środku pióro feniksa. Ten sam feniks dał jeszcze jedno pióro."),
 ("To jest sprzedawca, ____ zna każdą różdżkę.", ["który", "która", "które", "których"], 0,
  ("Sprzedawca is masculine → który.", "Sprzedawca — чоловічий рід → który (який).", "Rodzaj męski → który.")),
 ("To różdżka, ____ wybrała Harry'ego.", ["która", "który", "które", "którą"], 0,
  ("Różdżka is feminine and it's the subject → która.", "Różdżka — жіночий рід і підмет → która (яка).", "Rodzaj żeński, podmiot → która.")),
 (["To", "sklep", "w", "którym", "kupuje", "się", "różdżki"], {"en":"This is the shop where you buy wands.","uk":"Це крамниця, в якій купують палички.","pl":""},
  ("W którym = in which (locative). Kupuje się = one buys.", "W którym = в якому (місцевий відмінок). Kupuje się = купують.", "W + miejscownik: w którym.")),
 ("To pudełko, ____ leży na półce, jest bardzo stare.", ["które"], {"en":"which","uk":"яке","pl":"zaimek względny"},
  ("Pudełko is neuter → które.", "Pudełko — середній рід → które (яке).", "Rodzaj nijaki → które.")),
 ("Prawda czy fałsz? Pierwsza różdżka od razu pasowała do Harry'ego.", 1,
  ("False: he tried several wands before the right one chose him.", "Неправда: він спробував кілька паличок, поки одна не обрала його.", "Fałsz: próbował kilku, zanim właściwa go wybrała.")),
 ("To różdżka, która wybrała mnie.", ("ó in która sounds like 'u'.", "ó в która читається як «у».", "ó = u: która.")))
UK[6] = lesson("uk", 6, GR[6]["uk"],
 [W("паличка","wand","нею чаклують","różdżka"), W("продавець","seller","людина, яка продає","sprzedawca"), W("коробка","box","у ній щось лежить","pudełko"), W("перо","feather","росте в птахів","pióro"), W("обирати","to choose","вирішувати, що взяти","wybierać")],
 ("Паличка <b>обирає</b> чарівника. Що це означає?", ["Чарівник її шукає", "Паличка вирішує", "Паличка ламається", "Паличка дешева"], 1,
  ("Обирати = to choose. Here the wand decides!", "Тут вирішує саме паличка!", "Обирати = wybierać. Decyduje różdżka.")),
 ("Послухай. Що всередині палички Гаррі?", ["Волосина єдинорога", "Перо фенікса", "Серце дракона", "Золото"], 1,
  ("Перо фенікса = phoenix feather.", "Перо фенікса — як у паличці Волдеморта!", "Перо фенікса = pióro feniksa."),
  "У цій паличці перо фенікса. Той самий фенікс дав ще одне перо."),
 ("Це продавець, ____ знає кожну паличку.", ["який", "яка", "яке", "які"], 0,
  ("Продавець is masculine → який.", "Чоловічий рід → який.", "Rodzaj męski → який = który.")),
 ("Це паличка, ____ обрала Гаррі.", ["яка", "який", "яке", "яку"], 0,
  ("Паличка is feminine and the subject → яка.", "Жіночий рід, підмет → яка.", "Rodzaj żeński, podmiot → яка = która.")),
 (["Це", "крамниця", "в", "якій", "продають", "палички"], {"en":"This is the shop where they sell wands.","uk":"","pl":"To sklep, w którym sprzedają różdżki."},
  ("В якій = in which (locative).", "В якій — місцевий відмінок.", "В якій = w którym (miejscownik).")),
 ("Ця коробка, ____ лежить на полиці, дуже стара.", ["яка"], {"en":"which","uk":"займенник","pl":"który/która"},
  ("Коробка is feminine → яка.", "Коробка — жіночий рід → яка.", "Коробка jest rodzaju żeńskiego → яка (choć pudełko jest nijakie!).")),
 ("Правда чи неправда? Перша паличка одразу підійшла Гаррі.", 1,
  ("False: he tried several before the right one chose him.", "Неправда: він пробував кілька паличок.", "Fałsz: próbował kilku różdżek.")),
 ("Це паличка, яка обрала мене.", ("я is 'ya': яка = 'yaka'.", "Чітко: яка обрала мене.", "я = ja: яка ≈ jaka.")))

# ---------------- 7 ----------------
GR[7] = {"pl":{"en":"Guessing: musi / może / nie może być","uk":"Припущення: musi / może / nie może być","pl":"Przypuszczenia: musi / może / nie może być"},
         "uk":{"en":"Guessing: мабуть / напевно / не може бути","uk":"Припущення: мабуть / напевно / не може бути","pl":"Przypuszczenia: мабуть / напевно / не може бути"}}
PL[7] = lesson("pl", 7, GR[7]["pl"],
 [W("peron","platform","перон, платформа","miejsce, gdzie staje pociąg"), W("dworzec","station","вокзал","budynek, z którego jadą pociągi"), W("pociąg","train","потяг","jedzie po torach"), W("ściana","wall","стіна","część pokoju lub budynku"), W("przyjaciel","friend","друг","ktoś bliski, kogo lubisz")],
 ("Peronu 9 i ¾ <b>nie ma</b> na tablicy. Harry myśli, że…", ["to musi być żart", "to musi być bank", "to łatwe", "pociąg już jest"], 0,
  ("To musi być żart = it must be a joke (strong guess).", "To musi być żart = це, мабуть, жарт.", "Musi być = jestem prawie pewien.")),
 ("Posłuchaj. Jak dostać się na peron?", ["Przejść przez ścianę", "Pojechać taksówką", "Zapytać konduktora", "Wspiąć się na dach"], 0,
  ("Przejść przez ścianę = go through the wall.", "Przejść przez ścianę = пройти крізь стіну.", "Trzeba przejść przez ścianę!"),
  "Po prostu przejdź przez ścianę między peronem dziewiątym a dziesiątym. Nie bój się."),
 ("Rudzi chłopcy mają kufry i sowę. To ____ być czarodzieje!", ["muszą", "nie mogą", "mogę", "musi"], 0,
  ("Strong guess, plural → muszą być.", "Сильне припущення, множина → muszą być (мабуть, вони).", "Prawie pewność, l.mn. → muszą być.")),
 ("Ron ma brudny nos. On ____ być zmęczony, bo jedzie długo.", ["może", "musisz", "mogą", "muszę"], 0,
  ("Possibility → może być (he may be).", "Можливість → może być (може бути).", "Możliwość → może być.")),
 (["To", "nie", "może", "być", "prawdziwy", "peron"], {"en":"That can't be a real platform.","uk":"Це не може бути справжній перон.","pl":""},
  ("Nie może być = can't be (sure it's not true).", "Nie może być = не може бути.", "Nie może być = jestem pewien, że nie.")),
 ("Ta ściana ____ być magiczna! (musieć, ona)", ["musi"], {"en":"must","uk":"мусить, мабуть","pl":"musieć, ona"},
  ("Musieć → ona musi.", "Musieć → ona musi (вона мусить).", "Ona musi.")),
 ("Prawda czy fałsz? W pociągu Harry poznał Rona.", 0,
  ("True: they shared sweets and became friends on the train.", "Правда: у потязі вони поділилися солодощами й потоваришували.", "Prawda: w pociągu dzielili się słodyczami.")),
 ("To musi być peron dziewięć i trzy czwarte.", ("ć in być is a soft 'ch'; trzy starts with 'tsh'.", "być — м'яке «чь», trzy — «тши».", "Uważaj: być, trzy czwarte.")))
UK[7] = lesson("uk", 7, GR[7]["uk"],
 [W("перон","platform","місце, де зупиняється потяг","peron"), W("вокзал","station","будівля, звідки їдуть потяги","dworzec"), W("потяг","train","їде по рейках","pociąg"), W("стіна","wall","частина кімнати чи будинку","ściana"), W("друг","friend","близька людина","przyjaciel")],
 ("Перону 9¾ <b>немає</b> на табло. Гаррі думає, що…", ["це, мабуть, жарт", "це, мабуть, банк", "це легко", "потяг уже тут"], 0,
  ("Мабуть = probably/must be.", "Мабуть — майже впевнене припущення.", "Мабуть = chyba, pewnie.")),
 ("Послухай. Як потрапити на перон?", ["Пройти крізь стіну", "Поїхати таксі", "Спитати кондуктора", "Вилізти на дах"], 0,
  ("Крізь стіну = through the wall.", "Треба пройти крізь стіну!", "Крізь стіну = przez ścianę."),
  "Просто пройди крізь стіну між дев'ятим і десятим пероном. Не бійся."),
 ("Руді хлопці мають валізи й сову. Вони, ____, чарівники!", ["напевно", "ніколи", "вчора", "далеко"], 0,
  ("Напевно = surely, must be.", "Напевно — сильне припущення.", "Напевно = na pewno, chyba.")),
 ("У Рона брудний ніс. Він ____ бути втомлений.", ["може", "мусиш", "можу", "можемо"], 0,
  ("Може бути = may be.", "Може бути — можливість.", "Може бути = może być.")),
 (["Це", "не", "може", "бути", "справжній", "перон"], {"en":"That can't be a real platform.","uk":"","pl":"To nie może być prawdziwy peron."},
  ("Не може бути = can't be.", "Не може бути — впевненість, що ні.", "Не може бути = nie może być.")),
 ("Ця стіна, ____, чарівна! (probably)", ["мабуть","напевно"], {"en":"probably","uk":"слово-припущення","pl":"chyba, pewnie"},
  ("Мабуть is set off by commas.", "«Мабуть» виділяємо комами.", "Мабуть oddzielamy przecinkami.")),
 ("Правда чи неправда? У потязі Гаррі познайомився з Роном.", 0,
  ("True: they shared sweets and became friends.", "Правда: вони поділилися солодощами.", "Prawda: dzielili się słodyczami.")),
 ("Це, мабуть, перон дев'ять і три чверті.", ("Apostrophe in дев'ять: a tiny pause before я.", "Апостроф: дев'ять — «дев-ять».", "Apostrof: дев'ять ≈ dew-jat'.")))

# ---------------- 8 ----------------
GR[8] = {"pl":{"en":"Conditional: gdybym…, -bym","uk":"Умовний спосіб: gdybym…, -bym","pl":"Tryb przypuszczający: gdybym…, -bym"},
         "uk":{"en":"Conditional: якби…, би","uk":"Умовний спосіб: якби…, би","pl":"Tryb przypuszczający: якби…, би"}}
PL[8] = lesson("pl", 8, GR[8]["pl"],
 [W("tiara","hat","капелюх","stary kapelusz, który mówi"), W("dom","house (school team)","гуртожиток, дім","drużyna w szkole"), W("świeca","candle","свічка","daje światło, gdy się pali"), W("odważny","brave","сміливий","nie boi się"), W("sufit","ceiling","стеля","góra pokoju")],
 ("Świece wiszą pod <b>sufitem</b>. Gdzie to jest?", ["Na podłodze", "Na górze sali", "Za oknem", "W szafie"], 1,
  ("Sufit = ceiling. Pod sufitem: under the ceiling (instrumental again!).", "Sufit = стеля. Pod sufitem — орудний, як pod schodami.", "Pod + narzędnik: pod sufitem.")),
 ("Posłuchaj. Gdzie tiara wysyła Harry'ego?", ["Do Slytherinu", "Do Gryffindoru", "Do Hufflepuffu", "Do domu"], 1,
  ("Gryffindor! The house of the brave.", "Гріфіндор! Дім сміливих.", "Gryffindor: dom odważnych."),
  "Hm, trudne… Odwagi ci nie brakuje. Skoro nie Slytherin, to… Gryffindor!"),
 ("Gdybym był w Slytherinie, ____ smutny.", ["byłbym", "jestem", "będę", "byłem"], 0,
  ("Conditional: gdybym…, byłbym (I would be).", "Умовний: gdybym…, byłbym (я був би).", "Gdybym…, byłbym.")),
 ("Gdyby Ron ____ odważny, poszedłby do Gryffindoru.", ["był", "jest", "będzie", "bądź"], 0,
  ("After gdyby use the past form: gdyby był.", "Після gdyby — форма минулого: gdyby był (якби був).", "Gdyby + forma przeszła: gdyby był.")),
 (["Gdybym", "miał", "wybór", "wybrałbym", "Gryffindor"], {"en":"If I had a choice, I would choose Gryffindor.","uk":"Якби я мав вибір, я обрав би Гріфіндор.","pl":""},
  ("-bym sticks to the verb: wybrałbym.", "-bym приєднується до дієслова: wybrałbym (обрав би).", "Końcówka -bym: wybrałbym.")),
 ("Gdybyś mógł, ____ (pojechać) do domu? (ty)", ["pojechałbyś"], {"en":"would you go","uk":"ти поїхав би","pl":"pojechać, ty"},
  ("You (ty) → -łbyś: pojechałbyś.", "Ти → -łbyś: pojechałbyś (поїхав би).", "Ty → -łbyś.")),
 ("Prawda czy fałsz? Tiara od razu wiedziała, gdzie wysłać Harry'ego.", 1,
  ("False: she hesitated and thought about Slytherin.", "Неправда: капелюх вагався і думав про Слизерин.", "Fałsz: tiara wahała się i myślała o Slytherinie.")),
 ("Gdybym mógł wybrać, wybrałbym Gryffindor.", ("Gdybym: say 'g-dy-bym' clearly.", "Gdybym читається «гдибим».", "Wymawiaj wyraźnie: gdybym, wybrałbym.")))
UK[8] = lesson("uk", 8, GR[8]["uk"],
 [W("капелюх","hat","головний убір, що говорить","tiara, kapelusz"), W("гуртожиток","house (school team)","команда у школі","dom"), W("свічка","candle","дає світло, коли горить","świeca"), W("сміливий","brave","не боїться","odważny"), W("стеля","ceiling","верх кімнати","sufit")],
 ("Свічки висять під <b>стелею</b>. Де це?", ["На підлозі", "Угорі зали", "За вікном", "У шафі"], 1,
  ("Стеля = ceiling. Під стелею: instrumental again!", "Під + орудний: під стелею.", "Під стелею = pod sufitem.")),
 ("Послухай. Куди капелюх відправляє Гаррі?", ["У Слизерин", "У Гріфіндор", "У Гафелпаф", "Додому"], 1,
  ("Gryffindor, the house of the brave.", "Гріфіндор — дім сміливих.", "Gryffindor: dom odważnych."),
  "Гм, складно… Сміливості тобі не бракує. Якщо не Слизерин, то… Гріфіндор!"),
 ("Якби я був у Слизерині, я ____ сумний.", ["був би", "є", "буду", "був"], 0,
  ("Conditional: якби…, був би.", "Умовний спосіб: якби…, був би.", "Якби…, був би = gdybym…, byłbym.")),
 ("Якби Рон ____ сміливий, він пішов би в Гріфіндор.", ["був", "є", "буде", "будь"], 0,
  ("After якби use the past form: якби був.", "Після «якби» — минула форма.", "Po якби forma przeszła: якби був = gdyby był.")),
 (["Якби", "я", "мав", "вибір", "обрав", "би", "Гріфіндор"], {"en":"If I had a choice, I would choose Gryffindor.","uk":"","pl":"Gdybym miał wybór, wybrałbym Gryffindor."},
  ("Би is a separate word in Ukrainian (би / б).", "«Би» пишемо окремо.", "Po ukraińsku би piszemy osobno, po polsku -bym razem.")),
 ("Якби ти міг, ти ____ поїхав додому?", ["би"], {"en":"would","uk":"частка","pl":"-byś"},
  ("Би marks the conditional.", "Частка «би» — ознака умовного способу.", "Би = -by/-byś.")),
 ("Правда чи неправда? Капелюх одразу знав, куди відправити Гаррі.", 1,
  ("False: it hesitated and thought of Slytherin.", "Неправда: капелюх вагався.", "Fałsz: tiara się wahała.")),
 ("Якби я міг обрати, я обрав би Гріфіндор.", ("и in якби is short, like 'i' in 'sit'.", "Чітко: якби, обрав би.", "и w якби = polskie y.")))

# ---------------- 9 ----------------
GR[9] = {"pl":{"en":"Imperative: dodaj! mieszaj! nie dotykaj!","uk":"Наказовий спосіб: dodaj! mieszaj! nie dotykaj!","pl":"Tryb rozkazujący: dodaj! mieszaj! nie dotykaj!"},
         "uk":{"en":"Imperative: додай! мішай! не чіпай!","uk":"Наказовий спосіб: додай! мішай! не чіпай!","pl":"Tryb rozkazujący: додай! мішай! не чіпай!"}}
PL[9] = lesson("pl", 9, GR[9]["pl"],
 [W("eliksir","potion","зілля","magiczny napój"), W("lochy","dungeons","підземелля","zimne sale pod zamkiem"), W("surowy","strict","суворий","wymaga dużo, rzadko się uśmiecha"), W("mieszać","to stir","мішати","kręcić łyżką w garnku"), W("składnik","ingredient","інгредієнт","część przepisu")],
 ("Nauczyciel jest bardzo <b>surowy</b>. Jaki jest?", ["Wesoły i miły", "Wymagający i zimny", "Młody i nowy", "Zmęczony"], 1,
  ("Surowy = strict (also: raw, for food!).", "Surowy = суворий (а про їжу — сирий!).", "Surowy = wymagający.")),
 ("Posłuchaj. Co trzeba zrobić najpierw?", ["Dodać korzeń", "Wymieszać siedem razy", "Wypić eliksir", "Wyjść z klasy"], 0,
  ("Najpierw dodaj = first add.", "Najpierw dodaj = спочатку додай.", "Najpierw dodaj, potem mieszaj."),
  "Najpierw dodaj korzeń, potem mieszaj siedem razy. I niczego nie dotykaj!"),
 ("____ eliksir powoli! (mieszać, ty)", ["Mieszaj", "Mieszać", "Mieszam", "Miesza"], 0,
  ("Imperative of mieszać for ty: mieszaj!", "Наказовий для ty: mieszaj! (мішай!)", "Ty → mieszaj!")),
 ("Nie ____ tego kociołka! (dotykać, ty)", ["dotykaj", "dotknąć", "dotykam", "dotyka"], 0,
  ("Negative orders use the imperfective: nie dotykaj!", "Заборона — недоконаний вид: nie dotykaj! (не чіпай!)", "Zakaz: nie + niedokonany: nie dotykaj!")),
 (["Otwórzcie", "książki", "na", "stronie", "dziesiątej"], {"en":"Open your books at page ten.","uk":"Відкрийте книжки на десятій сторінці.","pl":""},
  ("Otwórzcie = open (you all). -cie = plural imperative.", "Otwórzcie = відкрийте (ви). -cie — множина.", "-cie: rozkaz do wielu osób.")),
 ("____ ten składnik do kociołka! (dodać, ty)", ["Dodaj"], {"en":"add","uk":"додай","pl":"dodać, ty"},
  ("Dodać → dodaj!", "Dodać → dodaj! (додай!)", "Dodać → dodaj!")),
 ("Prawda czy fałsz? Snape lubi Harry'ego od pierwszej lekcji.", 1,
  ("False: he asks Harry hard questions to embarrass him.", "Неправда: він ставить Гаррі важкі питання, щоб присоромити.", "Fałsz: zadaje mu trudne pytania, żeby go zawstydzić.")),
 ("Mieszaj powoli i niczego nie dotykaj!", ("sz in mieszaj = 'sh'.", "sz = «ш»: mieszaj.", "sz: mieszaj.")))
UK[9] = lesson("uk", 9, GR[9]["uk"],
 [W("зілля","potion","чарівний напій","eliksir"), W("підземелля","dungeons","холодні зали під замком","lochy"), W("суворий","strict","вимогливий, рідко всміхається","surowy"), W("мішати","to stir","крутити ложкою в горщику","mieszać"), W("інгредієнт","ingredient","частина рецепта","składnik")],
 ("Учитель дуже <b>суворий</b>. Який він?", ["Веселий і милий", "Вимогливий і холодний", "Молодий і новий", "Втомлений"], 1,
  ("Суворий = strict.", "Суворий — вимогливий.", "Суворий = surowy (ale nie o jedzeniu!).")),
 ("Послухай. Що треба зробити спочатку?", ["Додати корінь", "Помішати сім разів", "Випити зілля", "Вийти з класу"], 0,
  ("Спочатку додай = first add.", "Спочатку додай, потім мішай.", "Спочатку додай = najpierw dodaj."),
  "Спочатку додай корінь, потім помішай сім разів. І нічого не чіпай!"),
 ("____ зілля повільно! (мішати, ти)", ["Мішай", "Мішати", "Мішаю", "Мішає"], 0,
  ("Imperative for ти: мішай!", "Наказовий для «ти»: мішай!", "Ty → мішай! = mieszaj!")),
 ("Не ____ цього казанка! (чіпати, ти)", ["чіпай", "чіпати", "чіпаю", "чіпає"], 0,
  ("Negative order: не чіпай!", "Заборона: не чіпай!", "Zakaz: не чіпай! = nie dotykaj!")),
 (["Відкрийте", "книжки", "на", "десятій", "сторінці"], {"en":"Open your books at page ten.","uk":"","pl":"Otwórzcie książki na stronie dziesiątej."},
  ("-те = plural/polite imperative: відкрийте.", "-те — звертання до багатьох: відкрийте.", "-те = -cie: відкрийте = otwórzcie.")),
 ("____ цей інгредієнт у казанок! (додати, ти)", ["Додай"], {"en":"add","uk":"додати, ти","pl":"dodaj"},
  ("Додати → додай!", "Додати → додай!", "Додати → додай = dodaj.")),
 ("Правда чи неправда? Снейп любить Гаррі з першого уроку.", 1,
  ("False: he asks Harry hard questions to embarrass him.", "Неправда: він ставить важкі питання, щоб присоромити.", "Fałsz: zadaje mu trudne pytania.")),
 ("Мішай повільно і нічого не чіпай!", ("ш = 'sh', ч = 'ch', і = 'ee'.", "Чітко: мішай, нічого, чіпай.", "ш = sz, ч = cz.")))

# ---------------- 10 ----------------
GR[10] = {"pl":{"en":"Obligation: muszę / trzeba / nie wolno","uk":"Обов'язок: muszę / trzeba / nie wolno","pl":"Obowiązek: muszę / trzeba / nie wolno"},
          "uk":{"en":"Obligation: мушу / треба / не можна","uk":"Обов'язок: мушу / треба / не можна","pl":"Obowiązek: мушу / треба / не можна"}}
PL[10] = lesson("pl", 10, GR[10]["pl"],
 [W("miotła","broomstick","мітла","na niej latają czarodzieje"), W("latać","to fly","літати","poruszać się w powietrzu"), W("spaść","to fall","впасти","szybko polecieć w dół"), W("nadgarstek","wrist","зап'ястя","między ręką a dłonią"), W("przypominajka","remembrall","нагадайко","szklana kula, która przypomina")],
 ("Neville <b>spadł</b> z miotły. Co się stało?", ["Poleciał wysoko", "Upadł na ziemię", "Zasnął", "Wygrał"], 1,
  ("Spaść = to fall. He broke his wrist.", "Spaść = впасти. Він зламав зап'ястя.", "Spaść = upaść w dół.")),
 ("Posłuchaj. Czego nie wolno robić?", ["Wstawać z łóżek", "Latać, gdy nauczycielki nie ma", "Jeść obiadu", "Czytać"], 1,
  ("Nie wolno latać = flying is not allowed.", "Nie wolno latać = не можна літати.", "Nie wolno = zakaz."),
  "Kiedy mnie nie będzie, nikomu nie wolno latać. Kto wzleci, wyleci ze szkoły!"),
 ("Harry ____ oddać przypominajkę Neville'owi. (has to)", ["musi", "muszę", "musimy", "musieć"], 0,
  ("Musieć → on musi (he has to).", "Musieć → on musi (він мусить).", "On musi.")),
 ("W szkole ____ wolno chodzić nocą po korytarzach.", ["nie", "nic", "nikt", "trzeba"], 0,
  ("Nie wolno = it's forbidden.", "Nie wolno = не можна.", "Nie wolno = zakaz.")),
 (["Trzeba", "mocno", "trzymać", "miotłę", "obiema", "rękami"], {"en":"You have to hold the broom tightly with both hands.","uk":"Треба міцно тримати мітлу обома руками.","pl":""},
  ("Trzeba + infinitive = one has to.", "Trzeba + інфінітив = треба.", "Trzeba + bezokolicznik.")),
 ("Nie ____ się bać, to łatwe! (don't have to, ty)", ["musisz"], {"en":"you don't have to","uk":"не мусиш","pl":"musieć, ty"},
  ("Nie musisz = you don't have to (it's not necessary).", "Nie musisz = не мусиш (не обов'язково).", "Nie musisz ≠ nie wolno.")),
 ("Prawda czy fałsz? Za latanie Harry został wyrzucony ze szkoły.", 1,
  ("False: he was made Seeker of the house team!", "Неправда: його взяли ловцем у команду!", "Fałsz: został szukającym w drużynie!")),
 ("Nie wolno latać bez nauczyciela.", ("w in wolno sounds like 'v'.", "w = «в»: wolno.", "Wyraźnie: nie wolno.")))
UK[10] = lesson("uk", 10, GR[10]["uk"],
 [W("мітла","broomstick","на ній літають чарівники","miotła"), W("літати","to fly","рухатися в повітрі","latać"), W("впасти","to fall","швидко полетіти вниз","spaść"), W("зап'ястя","wrist","між рукою і долонею","nadgarstek"), W("нагадайко","remembrall","скляна кулька, що нагадує","przypominajka")],
 ("Невіл <b>впав</b> з мітли. Що сталося?", ["Полетів високо", "Опинився на землі", "Заснув", "Виграв"], 1,
  ("Впасти = to fall. He broke his wrist.", "Він зламав зап'ястя.", "Впасти = spaść.")),
 ("Послухай. Чого не можна робити?", ["Вставати з ліжок", "Літати, поки вчительки немає", "Обідати", "Читати"], 1,
  ("Не можна літати = flying is not allowed.", "Не можна — заборона.", "Не можна = nie wolno."),
  "Поки мене не буде, нікому не можна літати. Хто злетить, вилетить зі школи!"),
 ("Гаррі ____ повернути нагадайко Невілу. (has to)", ["мусить", "мушу", "мусимо", "мусити"], 0,
  ("Мусити → він мусить.", "Він мусить.", "Мусити → мусить = musi.")),
 ("У школі ____ можна ходити вночі коридорами.", ["не", "ні", "ніхто", "треба"], 0,
  ("Не можна = it's forbidden.", "Не можна — заборона.", "Не можна = nie wolno.")),
 (["Треба", "міцно", "тримати", "мітлу", "обома", "руками"], {"en":"You have to hold the broom tightly with both hands.","uk":"","pl":"Trzeba mocno trzymać miotłę obiema rękami."},
  ("Треба + infinitive.", "Треба + інфінітив.", "Треба = trzeba.")),
 ("Ти не ____ боятися, це легко! (don't have to)", ["мусиш"], {"en":"don't have to","uk":"мусити, ти","pl":"musisz"},
  ("Не мусиш = you don't have to.", "Не мусиш — не обов'язково.", "Не мусиш = nie musisz.")),
 ("Правда чи неправда? За політ Гаррі вигнали зі школи.", 1,
  ("False: he became Seeker of the house team!", "Неправда: його взяли ловцем!", "Fałsz: został szukającym!")),
 ("Не можна літати без учителя.", ("Stress: ЛІтати, учиТЕля.", "Наголоси: літати, учителя.", "Akcent: ЛІтати.")))

# ---------------- 11 ----------------
GR[11] = {"pl":{"en":"Motion verbs with prefixes: wejść / wyjść / przyjść","uk":"Дієслова руху з префіксами: wejść / wyjść / przyjść","pl":"Czasowniki ruchu z przedrostkami: wejść / wyjść / przyjść"},
          "uk":{"en":"Motion verbs with prefixes: увійти / вийти / прийти","uk":"Дієслова руху з префіксами: увійти / вийти / прийти","pl":"Czasowniki ruchu z przedrostkami: увійти / вийти / прийти"}}
PL[11] = lesson("pl", 11, GR[11]["pl"],
 [W("troll","troll","троль","ogromny, głupi potwór"), W("łazienka","bathroom","ванна кімната","tu myjesz ręce"), W("maczuga","club","палиця, булава","ciężki kij"), W("ratować","to save","рятувати","pomagać komuś w niebezpieczeństwie"), W("bać się","to be afraid","боятися","czuć strach")],
 ("Hermiona <b>boi się</b> trolla. Co czuje?", ["Radość", "Strach", "Głód", "Nudę"], 1,
  ("Bać się = to be afraid. Boi się + genitive: trolla.", "Bać się = боятися. Boi się trolla — родовий, як «боїться троля».", "Bać się + dopełniacz.")),
 ("Posłuchaj. Co krzyczy profesor?", ["Troll w lochach!", "Obiad gotowy!", "Lekcja skończona!", "Wesołych świąt!"], 0,
  ("Troll w lochach = troll in the dungeons.", "Troll w lochach = троль у підземеллі!", "Troll w lochach!"),
  "Troll! Troll w lochach! Myślałem, że powinniście wiedzieć."),
 ("Troll ____ do łazienki. (went in)", ["wszedł", "wyszedł", "przyszedł", "odszedł"], 0,
  ("W- = in: wejść → wszedł (went in).", "W- = у: wszedł = увійшов.", "W- = do środka: wszedł.")),
 ("Harry i Ron szybko ____ z sali. (went out)", ["wyszli", "weszli", "przyszli", "zeszli"], 0,
  ("Wy- = out: wyszli.", "Wy- = ви-: wyszli = вийшли.", "Wy- = na zewnątrz: wyszli.")),
 (["Chłopcy", "przyszli", "Hermionie", "na", "ratunek"], {"en":"The boys came to Hermione's rescue.","uk":"Хлопці прийшли Герміоні на порятунок.","pl":""},
  ("Przy- = arrive: przyszli (came).", "Przy- = при-: przyszli = прийшли.", "Przy-: przybyć, przyjść.")),
 ("Troll ____ z łazienki? Nie, upadł! (wyjść, on)", ["wyszedł"], {"en":"went out","uk":"вийшов","pl":"wyjść, on"},
  ("Wyjść → wyszedł (irregular past!).", "Wyjść → wyszedł (неправильна форма).", "Wyjść → wyszedł.")),
 ("Prawda czy fałsz? Po tej nocy Hermiona została przyjaciółką chłopców.", 0,
  ("True: from then on they were three friends.", "Правда: відтоді їх було троє друзів.", "Prawda: od tej pory byli we trójkę.")),
 ("Troll wszedł do łazienki!", ("wszedł: 'fshedw', tricky cluster!", "wszedł ≈ «вшедв».", "Trudne: wszedł.")))
UK[11] = lesson("uk", 11, GR[11]["uk"],
 [W("троль","troll","величезне дурне чудовисько","troll"), W("вбиральня","bathroom","тут миють руки","łazienka"), W("палиця","club","важкий кийок","maczuga"), W("рятувати","to save","допомагати в небезпеці","ratować"), W("боятися","to be afraid","відчувати страх","bać się")],
 ("Герміона <b>боїться</b> троля. Що вона відчуває?", ["Радість", "Страх", "Голод", "Нудьгу"], 1,
  ("Боятися = to be afraid; боїться + genitive: троля.", "Боятися кого? — родовий: троля.", "Боятися + dopełniacz, jak bać się trolla.")),
 ("Послухай. Що кричить професор?", ["Троль у підземеллі!", "Обід готовий!", "Урок закінчено!", "Веселих свят!"], 0,
  ("Троль у підземеллі = troll in the dungeons.", "Троль у підземеллі!", "Троль у підземеллі = troll w lochach."),
  "Троль! Троль у підземеллі! Я подумав, що ви маєте знати."),
 ("Троль ____ у вбиральню. (went in)", ["увійшов", "вийшов", "прийшов", "пішов"], 0,
  ("У- = in: увійшов.", "У- = всередину.", "У- = w-: увійшов = wszedł.")),
 ("Гаррі й Рон швидко ____ із зали. (went out)", ["вийшли", "увійшли", "прийшли", "зійшли"], 0,
  ("Ви- = out: вийшли.", "Ви- = назовні.", "Ви- = wy-: вийшли = wyszli.")),
 (["Хлопці", "прийшли", "Герміоні", "на", "порятунок"], {"en":"The boys came to Hermione's rescue.","uk":"","pl":"Chłopcy przyszli Hermionie na ratunek."},
  ("При- = arrive: прийшли.", "При- = прибуття.", "При- = przy-.")),
 ("Троль ____ з вбиральні? Ні, він упав! (вийти, він)", ["вийшов"], {"en":"went out","uk":"вийти, він","pl":"wyszedł"},
  ("Вийти → вийшов.", "Вийти → вийшов.", "Вийти → вийшов = wyszedł.")),
 ("Правда чи неправда? Після тієї ночі Герміона стала подругою хлопців.", 0,
  ("True: from then on they were three friends.", "Правда: відтоді їх троє.", "Prawda: od tej pory we trójkę.")),
 ("Троль увійшов у вбиральню!", ("й is a short 'y' sound: увійшов.", "Чітко: увійшов.", "й = j: увійшов ≈ uwijszow.")))

# ---------------- 12 ----------------
GR[12] = {"pl":{"en":"Comparison: szybki → szybszy → najszybszy","uk":"Ступені порівняння: szybki → szybszy → najszybszy","pl":"Stopniowanie: szybki → szybszy → najszybszy"},
          "uk":{"en":"Comparison: швидкий → швидший → найшвидший","uk":"Ступені порівняння: швидкий → швидший → найшвидший","pl":"Stopniowanie: швидкий → швидший → найшвидший"}}
PL[12] = lesson("pl", 12, GR[12]["pl"],
 [W("mecz","match","матч","sportowa gra dwóch drużyn"), W("kibic","fan","вболівальник","ogląda i dopinguje"), W("szukający","Seeker","ловець","łapie złoty znicz"), W("złapać","to catch","спіймати","chwycić coś, co leci"), W("wygrać","to win","виграти","być pierwszym, zdobyć zwycięstwo")],
 ("Harry <b>złapał</b> znicz. Co zrobił?", ["Upuścił go", "Chwycił go", "Zgubił go", "Kupił go"], 1,
  ("Złapać = to catch. He nearly swallowed it!", "Złapać = спіймати. Він ледь його не проковтнув!", "Złapać = chwycić.")),
 ("Posłuchaj. Kto wygrał mecz?", ["Gryffindor", "Slytherin", "Nikt", "Nauczyciele"], 0,
  ("Gryffindor wygrywa = Gryffindor wins!", "Gryffindor wygrywa = Гріфіндор перемагає!", "Gryffindor wygrywa!"),
  "Potter ma znicz! Gryffindor wygrywa sto siedemdziesiąt do sześćdziesięciu!"),
 ("Nimbus jest ____ niż stara miotła.", ["szybszy", "szybki", "najszybszy", "szybko"], 0,
  ("Comparative: szybki → szybszy (+ niż = than).", "Вищий ступінь: szybszy niż… (швидший, ніж…).", "Stopień wyższy + niż.")),
 ("Harry jest ____ szukającym w historii szkoły. (the youngest)", ["najmłodszym", "młodszym", "młodym", "młodo"], 0,
  ("Superlative: naj- + comparative: najmłodszy (here instrumental after jest).", "Найвищий: naj- (як наш най-): najmłodszy.", "Stopień najwyższy: naj-.")),
 (["To", "był", "najlepszy", "mecz", "w", "roku"], {"en":"It was the best match of the year.","uk":"Це був найкращий матч року.","pl":""},
  ("Dobry → lepszy → najlepszy (irregular).", "Dobry → lepszy → najlepszy (неправильне, як добрий → кращий).", "Nieregularne: dobry, lepszy, najlepszy.")),
 ("Miotła leciała coraz ____. (wyżej/niżej → higher)", ["wyżej"], {"en":"higher","uk":"вище","pl":"wysoko → ?"},
  ("Adverb comparative: wysoko → wyżej.", "Прислівник: wysoko → wyżej (вище).", "Wysoko → wyżej.")),
 ("Prawda czy fałsz? Miotła Harry'ego w meczu zachowywała się normalnie.", 1,
  ("False: someone was jinxing it and it tried to throw him off.", "Неправда: хтось зачаровував мітлу, і вона намагалася його скинути.", "Fałsz: ktoś rzucał na nią urok.")),
 ("Gryffindor wygrywa! To najlepszy mecz!", ("rz in wygrywa? No: just 'gr'. Najlepszy: 'sh' sound in -szy.", "-szy читається як «ши».", "Wyraźnie: najlepszy.")))
UK[12] = lesson("uk", 12, GR[12]["uk"],
 [W("матч","match","спортивна гра двох команд","mecz"), W("вболівальник","fan","дивиться і підтримує","kibic"), W("ловець","Seeker","ловить золотий снич","szukający"), W("спіймати","to catch","схопити те, що летить","złapać"), W("виграти","to win","бути першим","wygrać")],
 ("Гаррі <b>спіймав</b> снич. Що він зробив?", ["Впустив", "Схопив", "Загубив", "Купив"], 1,
  ("Спіймати = to catch.", "Спіймати — схопити. Він мало не проковтнув снич!", "Спіймати = złapać.")),
 ("Послухай. Хто виграв матч?", ["Гріфіндор", "Слизерин", "Ніхто", "Учителі"], 0,
  ("Гріфіндор перемагає = Gryffindor wins!", "Гріфіндор перемагає!", "Гріфіндор перемагає = Gryffindor wygrywa."),
  "Поттер упіймав снича! Гріфіндор перемагає з рахунком сто сімдесят — шістдесят!"),
 ("Німбус ____ за стару мітлу.", ["швидший", "швидкий", "найшвидший", "швидко"], 0,
  ("Comparative: швидкий → швидший (за = than).", "Вищий ступінь: швидший за…", "Швидший за = szybszy niż.")),
 ("Гаррі — ____ ловець в історії школи. (the youngest)", ["наймолодший", "молодший", "молодий", "молодо"], 0,
  ("Superlative: най- + comparative.", "Найвищий ступінь: най-.", "Най- = naj-.")),
 (["Це", "був", "найкращий", "матч", "цього", "року"], {"en":"It was the best match of the year.","uk":"","pl":"To był najlepszy mecz w tym roku."},
  ("Добрий → кращий → найкращий (irregular).", "Добрий → кращий → найкращий.", "Добрий → кращий → найкращий = dobry → lepszy → najlepszy.")),
 ("Мітла летіла все ____. (higher)", ["вище"], {"en":"higher","uk":"високо → ?","pl":"wyżej"},
  ("Високо → вище.", "Прислівник: високо → вище.", "Високо → вище = wyżej.")),
 ("Правда чи неправда? Мітла Гаррі під час матчу поводилася звичайно.", 1,
  ("False: someone jinxed it.", "Неправда: хтось зачаровував мітлу.", "Fałsz: ktoś rzucił urok.")),
 ("Гріфіндор перемагає! Це найкращий матч!", ("г is a soft breathy 'h'.", "Чітко: Гріфіндор, найкращий.", "г ≈ polskie h.")))

# ---------------- 13 ----------------
GR[13] = {"pl":{"en":"Wishes: chciałbym… / żeby…","uk":"Бажання: chciałbym… / żeby…","pl":"Życzenia: chciałbym… / żeby…"},
          "uk":{"en":"Wishes: хотів би… / якби ж…","uk":"Бажання: хотів би… / якби ж…","pl":"Życzenia: хотів би… / якби ж…"}}
PL[13] = lesson("pl", 13, GR[13]["pl"],
 [W("lustro","mirror","дзеркало","w nim widzisz siebie"), W("pragnienie","wish, desire","бажання","to, czego bardzo chcesz"), W("odbicie","reflection","відображення","obraz w lustrze"), W("tęsknić","to miss (someone)","сумувати","być smutnym bez kogoś"), W("peleryna","cloak","плащ","długie okrycie bez rękawów")],
 ("Harry <b>tęskni</b> za rodzicami. Co czuje?", ["Złość", "Smutek, bo ich nie ma", "Strach", "Radość"], 1,
  ("Tęsknić za kimś = to miss someone.", "Tęsknić za kimś = сумувати за кимось.", "Tęsknić za + narzędnik.")),
 ("Posłuchaj. Co pokazuje lustro?", ["Przyszłość", "Najgłębsze pragnienie", "Pogodę", "Twoje odbicie"], 1,
  ("The mirror shows your deepest wish, not the truth.", "Дзеркало показує найглибше бажання.", "Lustro pokazuje najgłębsze pragnienie."),
  "To lustro nie pokazuje przyszłości. Pokazuje tylko najgłębsze pragnienie naszego serca."),
 ("____ znowu zobaczyć mamę i tatę. (I would like)", ["Chciałbym", "Chcę by", "Chciałem", "Chcieć"], 0,
  ("Chciałbym = I would like (polite wish).", "Chciałbym = я хотів би.", "Chciałbym = życzenie.")),
 ("Ron marzy, ____ był kapitanem drużyny.", ["żeby", "że", "czy", "bo"], 0,
  ("Wish about something: żeby + past form.", "Бажання: żeby + форма минулого (щоб був).", "Marzyć, żeby…")),
 (["Chciałbym", "żeby", "moi", "rodzice", "żyli"], {"en":"I wish my parents were alive.","uk":"Я хотів би, щоб мої батьки були живі.","pl":""},
  ("Żeby + past tense form expresses a wish.", "Żeby + минулий час = щоб…", "Żeby + forma przeszła.")),
 ("Ron ____, żeby zdobyć puchar. (chcieć, on, conditional)", ["chciałby"], {"en":"would like","uk":"хотів би","pl":"chcieć, on, tryb przypuszczający"},
  ("Chcieć → chciałby (he would like).", "Chcieć → chciałby (хотів би).", "On chciałby.")),
 ("Prawda czy fałsz? Dumbledore radzi Harry'emu codziennie patrzeć w lustro.", 1,
  ("False: he says it's not good to live in dreams and forget to live.", "Неправда: він каже, що не можна жити мріями й забувати жити.", "Fałsz: mówi, że nie wolno żyć marzeniami.")),
 ("Chciałbym znowu zobaczyć rodziców.", ("ch is a breathy 'h'; ia is like 'ya'.", "ch = «х»: chciałbym ≈ «хцявбим».", "Wyraźnie: chciałbym.")))
UK[13] = lesson("uk", 13, GR[13]["uk"],
 [W("дзеркало","mirror","у ньому бачиш себе","lustro"), W("бажання","wish","те, чого дуже хочеш","pragnienie"), W("відображення","reflection","образ у дзеркалі","odbicie"), W("сумувати","to miss","бути сумним без когось","tęsknić"), W("плащ","cloak","довгий одяг без рукавів","peleryna")],
 ("Гаррі <b>сумує</b> за батьками. Що він відчуває?", ["Злість", "Смуток, бо їх немає", "Страх", "Радість"], 1,
  ("Сумувати за кимось = to miss someone.", "Сумувати за + орудний: за батьками.", "Сумувати за = tęsknić za.")),
 ("Послухай. Що показує дзеркало?", ["Майбутнє", "Найглибше бажання", "Погоду", "Твоє відображення"], 1,
  ("It shows your deepest wish.", "Дзеркало показує найглибше бажання серця.", "Najgłębsze pragnienie."),
  "Це дзеркало не показує майбутнього. Воно показує лише найглибше бажання нашого серця."),
 ("Я ____ знову побачити маму й тата. (would like)", ["хотів би", "хочу б", "хотів", "хотіти"], 0,
  ("Хотів би = I would like.", "Хотів би — бажання.", "Хотів би = chciałbym.")),
 ("Рон мріє, ____ стати капітаном команди.", ["щоб", "що", "чи", "бо"], 0,
  ("Wish: мріяти, щоб…", "Мріяти, щоб…", "Щоб = żeby.")),
 (["Якби", "ж", "мої", "батьки", "були", "живі"], {"en":"If only my parents were alive.","uk":"","pl":"Gdyby tylko moi rodzice żyli."},
  ("Якби ж = if only.", "«Якби ж» — сильне бажання.", "Якби ж = gdyby tylko.")),
 ("Рон ____ би здобути кубок. (хотіти, він)", ["хотів"], {"en":"would like","uk":"хотіти, він","pl":"chciałby"},
  ("Хотіти → хотів би.", "Він хотів би.", "Хотів би = chciałby.")),
 ("Правда чи неправда? Дамблдор радить Гаррі щодня дивитися в дзеркало.", 1,
  ("False: he warns against living in dreams.", "Неправда: не можна жити мріями.", "Fałsz: ostrzega przed życiem marzeniami.")),
 ("Я хотів би знову побачити батьків.", ("х is a rough 'h', like Scottish 'loch'.", "Чітко: хотів би.", "х = ch.")))

# ---------------- 14 ----------------
GR[14] = {"pl":{"en":"Past conditional: gdyby nie…, to by…","uk":"Нереальна умова в минулому: gdyby nie…, to by…","pl":"Warunek nierzeczywisty: gdyby nie…, to by…"},
          "uk":{"en":"Past conditional: якби не…, то б…","uk":"Нереальна умова: якби не…, то б…","pl":"Warunek nierzeczywisty: якби не…, то б…"}}
PL[14] = lesson("pl", 14, GR[14]["pl"],
 [W("las","forest","ліс","dużo drzew"), W("kara","punishment, detention","покарання","za złe zachowanie"), W("centaur","centaur","кентавр","pół człowiek, pół koń"), W("ciemny","dark","темний","bez światła"), W("jednorożec","unicorn","єдиноріг","biały koń z rogiem")],
 ("W lesie jest bardzo <b>ciemno</b>. Jak jest?", ["Jasno", "Bez światła", "Gorąco", "Głośno"], 1,
  ("Ciemno = dark.", "Ciemno = темно.", "Ciemno ≠ jasno.")),
 ("Posłuchaj. Kto uratował Harry'ego?", ["Centaur", "Troll", "Hagrid", "Sowa"], 0,
  ("Firenze the centaur saved him.", "Його врятував кентавр Флоренц.", "Uratował go centaur."),
  "Szybko, wsiadaj mi na grzbiet! Las nie jest bezpieczny w nocy."),
 ("Gdyby nie centaur, Harry ____ zginąć.", ["mógłby", "może", "mógł", "będzie mógł"], 0,
  ("Gdyby nie…, mógłby… = if it weren't for…, he could have…", "Gdyby nie…, mógłby… = якби не…, міг би…", "Gdyby nie…, mógłby…")),
 ("Gdyby chłopcy nie złamali zasad, nie ____ kary.", ["dostaliby", "dostali", "dostają", "dostaną"], 0,
  ("Conditional plural: -liby.", "Умовний, множина: dostaliby (отримали б).", "Oni → -liby.")),
 (["Gdyby", "nie", "Hagrid", "zgubiliby", "się", "w", "lesie"], {"en":"If it weren't for Hagrid, they would have got lost in the forest.","uk":"Якби не Хагрід, вони заблукали б у лісі.","pl":""},
  ("Zgubić się = to get lost.", "Zgubić się = заблукати.", "Zgubić się w lesie.")),
 ("Gdybym tam był, ____ się bał. (być, ja → would)", ["bym"], {"en":"would","uk":"б","pl":"cząstka"},
  ("Particle bym: ja bym się bał.", "Частка bym: ja bym się bał (я б боявся).", "Ja bym…")),
 ("Prawda czy fałsz? W lesie ktoś pił krew jednorożca.", 0,
  ("True: a hooded figure was drinking unicorn blood.", "Правда: постать у каптурі пила кров єдинорога.", "Prawda: postać w kapturze piła krew.")),
 ("Gdyby nie centaur, zgubiłbym się w lesie.", ("zgubiłbym: g-u-b, ł like 'w'.", "zgubiłbym ≈ «згубівбим».", "Wyraźnie: zgubiłbym.")))
UK[14] = lesson("uk", 14, GR[14]["uk"],
 [W("ліс","forest","багато дерев","las"), W("покарання","punishment","за погану поведінку","kara"), W("кентавр","centaur","наполовину людина, наполовину кінь","centaur"), W("темний","dark","без світла","ciemny"), W("єдиноріг","unicorn","білий кінь з рогом","jednorożec")],
 ("У лісі дуже <b>темно</b>. Як там?", ["Світло", "Без світла", "Жарко", "Гучно"], 1,
  ("Темно = dark.", "Темно — без світла.", "Темно = ciemno.")),
 ("Послухай. Хто врятував Гаррі?", ["Кентавр", "Троль", "Хагрід", "Сова"], 0,
  ("The centaur saved him.", "Кентавр Флоренц.", "Uratował go centaur."),
  "Швидко, сідай мені на спину! Ліс уночі небезпечний."),
 ("Якби не кентавр, Гаррі ____ загинути.", ["міг би", "може", "міг", "зможе"], 0,
  ("Якби не…, міг би…", "Якби не…, міг би…", "Якби не… = gdyby nie…")),
 ("Якби хлопці не порушили правил, вони не ____ покарання.", ["отримали б", "отримали", "отримують", "отримають"], 0,
  ("Conditional: past form + б.", "Минула форма + б.", "Отримали б = dostaliby.")),
 (["Якби", "не", "Хагрід", "вони", "заблукали", "б"], {"en":"If it weren't for Hagrid, they would have got lost.","uk":"","pl":"Gdyby nie Hagrid, zgubiliby się."},
  ("Заблукати = to get lost.", "Заблукати — загубити дорогу.", "Заблукати = zgubić się.")),
 ("Якби я там був, я ____ боявся.", ["б", "би"], {"en":"would","uk":"частка","pl":"bym"},
  ("Б / би marks the conditional.", "Частка б/би.", "Б = by.")),
 ("Правда чи неправда? У лісі хтось пив кров єдинорога.", 0,
  ("True: a hooded figure.", "Правда: постать у каптурі.", "Prawda: postać w kapturze.")),
 ("Якби не кентавр, я заблукав би в лісі.", ("є = 'ye'; ліс has a soft л.", "Чітко: заблукав би.", "л przed і miękkie.")))

# ---------------- 15 ----------------
GR[15] = {"pl":{"en":"Future: zrobię vs będę robić","uk":"Майбутній час: zrobię vs będę robić","pl":"Czas przyszły: zrobię vs będę robić"},
          "uk":{"en":"Future: зроблю vs буду робити","uk":"Майбутній час: зроблю vs буду робити","pl":"Czas przyszły: зроблю vs буду робити"}}
PL[15] = lesson("pl", 15, GR[15]["pl"],
 [W("klapa","trapdoor","люк","drzwi w podłodze"), W("szachy","chess","шахи","gra z królem i wieżą"), W("zagadka","riddle","загадка","pytanie do rozwiązania"), W("ogień","fire","вогонь","pali się i grzeje"), W("poświęcić się","to sacrifice oneself","пожертвувати собою","oddać siebie dla innych")],
 ("Ron <b>poświęca się</b> w szachach. Co robi?", ["Ucieka", "Oddaje siebie, żeby inni wygrali", "Śpi", "Oszukuje"], 1,
  ("Poświęcić się = to sacrifice yourself.", "Poświęcić się = пожертвувати собою.", "Poświęcić się dla innych.")),
 ("Posłuchaj. Kto pójdzie dalej?", ["Harry", "Ron", "Hermiona", "Wszyscy"], 0,
  ("Harry pójdzie dalej sam.", "Гаррі піде далі сам.", "Harry pójdzie sam."),
  "Ten eliksir wystarczy tylko dla jednej osoby. Ty pójdziesz dalej, Harry. Ja wrócę po pomoc."),
 ("Jutro Harry ____ kamień. (once, result)", ["znajdzie", "będzie znajdować", "znalazł", "znajduje"], 0,
  ("Perfective future (one result): znajdzie.", "Доконаний майбутній: znajdzie (знайде).", "Dokonany: znajdzie.")),
 ("W wakacje Hermiona ____ się codziennie. (repeated)", ["będzie uczyć", "nauczy", "uczyła", "uczy się"], 0,
  ("Imperfective future = będę + infinitive: będzie się uczyć.", "Недоконаний майбутній: będzie się uczyć (буде вчитися).", "Będzie + bezokolicznik.")),
 (["Ja", "wrócę", "i", "sprowadzę", "pomoc"], {"en":"I'll go back and bring help.","uk":"Я повернуся і приведу допомогу.","pl":""},
  ("Wrócę, sprowadzę: perfective future.", "Wrócę, sprowadzę — доконаний майбутній.", "Dokonany: wrócę.")),
 ("Ty ____ dalej, Harry! (pójść, ty)", ["pójdziesz"], {"en":"will go","uk":"підеш","pl":"pójść, ty"},
  ("Pójść → ty pójdziesz.", "Pójść → pójdziesz (підеш).", "Ty pójdziesz.")),
 ("Prawda czy fałsz? Hermiona rozwiązała zagadkę z eliksirami.", 0,
  ("True: logic, not magic!", "Правда: логіка, а не магія!", "Prawda: logika, nie magia!")),
 ("Ja wrócę i sprowadzę pomoc!", ("ę at the end is nearly silent: wrócę ≈ 'vroo-tse'.", "ę в кінці майже не чути: wrócę.", "Końcowe ę wymawiamy słabo.")))
UK[15] = lesson("uk", 15, GR[15]["uk"],
 [W("люк","trapdoor","двері в підлозі","klapa"), W("шахи","chess","гра з королем і турою","szachy"), W("загадка","riddle","питання, яке треба розв'язати","zagadka"), W("вогонь","fire","горить і гріє","ogień"), W("пожертвувати","to sacrifice","віддати себе заради інших","poświęcić")],
 ("Рон <b>жертвує</b> собою в шахах. Що він робить?", ["Тікає", "Віддає себе, щоб інші перемогли", "Спить", "Шахраює"], 1,
  ("Жертвувати собою = to sacrifice yourself.", "Жертвувати собою заради інших.", "Жертвувати = poświęcać się.")),
 ("Послухай. Хто піде далі?", ["Гаррі", "Рон", "Герміона", "Усі"], 0,
  ("Harry will go on alone.", "Гаррі піде далі сам.", "Harry pójdzie sam."),
  "Цього зілля вистачить лише на одного. Ти підеш далі, Гаррі. Я повернуся по допомогу."),
 ("Завтра Гаррі ____ камінь. (результат)", ["знайде", "буде шукати", "знайшов", "знаходить"], 0,
  ("Perfective future: знайде.", "Доконаний майбутній: знайде.", "Знайде = znajdzie.")),
 ("На канікулах Герміона ____ щодня. (повторювано)", ["буде вчитися", "навчиться", "вчилася", "вчиться"], 0,
  ("Imperfective future: буде + infinitive.", "Недоконаний майбутній: буде вчитися (або вчитиметься).", "Буде вчитися = będzie się uczyć.")),
 (["Я", "повернуся", "і", "приведу", "допомогу"], {"en":"I'll go back and bring help.","uk":"","pl":"Wrócę i sprowadzę pomoc."},
  ("Perfective future forms.", "Доконаний майбутній.", "Повернуся = wrócę.")),
 ("Ти ____ далі, Гаррі! (піти, ти)", ["підеш"], {"en":"will go","uk":"піти, ти","pl":"pójdziesz"},
  ("Піти → ти підеш.", "Піти → підеш.", "Підеш = pójdziesz.")),
 ("Правда чи неправда? Герміона розв'язала загадку із зіллям.", 0,
  ("True: logic, not magic!", "Правда: логіка, а не магія!", "Prawda: logika!")),
 ("Я повернуся і приведу допомогу!", ("ся is 'sya': повернуся.", "Чітко: повернуся.", "-ся ≈ -sia.")))

# ---------------- 16 ----------------
GR[16] = {"pl":{"en":"Review: past, future, cases","uk":"Повторення: минулий, майбутній, відмінки","pl":"Powtórka: przeszły, przyszły, przypadki"},
          "uk":{"en":"Review: past, future, cases","uk":"Повторення: минулий, майбутній, відмінки","pl":"Powtórka: przeszły, przyszły, przypadki"}}
PL[16] = lesson("pl", 16, GR[16]["pl"],
 [W("kamień","stone","камінь","twarda rzecz z ziemi"), W("kieszeń","pocket","кишеня","w niej trzymasz rzeczy"), W("uczta","feast","бенкет","wielka, uroczysta kolacja"), W("puchar","cup (trophy)","кубок","nagroda dla zwycięzcy"), W("pożegnanie","farewell","прощання","gdy mówisz do widzenia")],
 ("Kamień nagle był w <b>kieszeni</b> Harry'ego. Gdzie?", ["W ręce", "W kieszeni", "W bucie", "W książce"], 1,
  ("W kieszeni = in the pocket (locative).", "W kieszeni = у кишені (місцевий).", "W + miejscownik: w kieszeni.")),
 ("Posłuchaj. Kto zdobył puchar domów?", ["Slytherin", "Gryffindor", "Ravenclaw", "Nikt"], 1,
  ("The last points went to Neville!", "Останні бали отримав Невіл!", "Ostatnie punkty dostał Neville!"),
  "Za odwagę wobec przyjaciół: dziesięć punktów dla Neville'a. Puchar zdobywa Gryffindor!"),
 ("Harry ____ w lustro i zobaczył siebie z kamieniem.", ["spojrzał", "spojrzy", "patrzy", "spojrzeć"], 0,
  ("Past, completed: spojrzał.", "Минулий доконаний: spojrzał (подивився).", "Przeszły dokonany.")),
 ("W przyszłym roku Harry ____ do Hogwartu.", ["wróci", "wrócił", "wraca", "wrócić"], 0,
  ("Future perfective: wróci.", "Майбутній: wróci (повернеться).", "Przyszły: wróci.")),
 (["Harry", "wrócił", "na", "wakacje", "do", "wujostwa"], {"en":"Harry went back to his aunt and uncle for the holidays.","uk":"Гаррі повернувся на канікули до дядька й тітки.","pl":""},
  ("Do + genitive: do wujostwa.", "Do + родовий: do wujostwa.", "Do + dopełniacz.")),
 ("Opowiedz: „W tym roku ____ wiele przygód.” (mieć, ja)", ["miałem","miałam"], {"en":"I had","uk":"я мав/мала","pl":"mieć, ja"},
  ("Past: miałem (male) / miałam (female).", "Минулий: miałem (ч.) / miałam (ж.).", "Miałem / miałam.")),
 ("Prawda czy fałsz? Na końcu kamień został zniszczony.", 0,
  ("True: Dumbledore and Flamel decided to destroy it.", "Правда: Дамблдор і Фламель вирішили його знищити.", "Prawda: zdecydowali go zniszczyć.")),
 ("W tym roku miałem wiele przygód, ale wrócę!", ("Tell your own story: past (miałem), future (wrócę).", "Розкажи свою історію: минулий + майбутній.", "Twoja historia: przeszły i przyszły.")))
UK[16] = lesson("uk", 16, GR[16]["uk"],
 [W("камінь","stone","тверда річ із землі","kamień"), W("кишеня","pocket","у ній тримаєш речі","kieszeń"), W("бенкет","feast","велика урочиста вечеря","uczta"), W("кубок","cup (trophy)","нагорода переможцю","puchar"), W("прощання","farewell","коли кажеш «до побачення»","pożegnanie")],
 ("Камінь раптом опинився в <b>кишені</b> Гаррі. Де?", ["У руці", "У кишені", "У черевику", "У книжці"], 1,
  ("У кишені = in the pocket (locative).", "У кишені — місцевий відмінок.", "У кишені = w kieszeni.")),
 ("Послухай. Хто здобув кубок гуртожитків?", ["Слизерин", "Гріфіндор", "Рейвенклов", "Ніхто"], 1,
  ("The last points went to Neville!", "Останні бали — Невілу!", "Ostatnie punkty dla Neville'a!"),
  "За сміливість перед друзями: десять балів Невілу Лонгботому. Кубок здобуває Гріфіндор!"),
 ("Гаррі ____ у дзеркало і побачив себе з каменем.", ["подивився", "подивиться", "дивиться", "подивитися"], 0,
  ("Past perfective: подивився.", "Минулий доконаний.", "Подивився = spojrzał.")),
 ("Наступного року Гаррі ____ до Гоґвортсу.", ["повернеться", "повернувся", "повертається", "повернутися"], 0,
  ("Future perfective: повернеться.", "Майбутній доконаний.", "Повернеться = wróci.")),
 (["Гаррі", "повернувся", "на", "канікули", "до", "дядька"], {"en":"Harry went back to his uncle for the holidays.","uk":"","pl":"Harry wrócił na wakacje do wujka."},
  ("До + genitive: до дядька.", "До + родовий.", "До + dopełniacz.")),
 ("Розкажи: «Цього року я ____ багато пригод.» (мати, я)", ["мав","мала"], {"en":"I had","uk":"мати, я","pl":"miałem/miałam"},
  ("Past: мав (male) / мала (female).", "Мав / мала.", "Мав = miałem, мала = miałam.")),
 ("Правда чи неправда? Наприкінці камінь знищили.", 0,
  ("True: Dumbledore and Flamel decided to destroy it.", "Правда.", "Prawda.")),
 ("Цього року я мав багато пригод, але я повернуся!", ("Tell your own story: past + future.", "Твоя історія: минулий і майбутній час.", "Twoja historia: przeszły i przyszły.")))

if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("l1", os.path.join(HERE, "l1_variants.py"))
    l1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(l1)
    p = os.path.join(HERE, "hp1.json")
    d = json.load(open(p, encoding="utf-8"))
    for l in d:
        n = l["num"]
        l["title_en"] = TITLE_EN[n]; l["scene_en"] = SCENE_EN[n]
        if n == 1:
            l["variants"] = {"pl": l1.PL, "uk": l1.UK, "pl_grammar": "Czas teraźniejszy · pod + narzędnik", "uk_grammar": "Теперішній час · під + орудний відмінок",
                "pl_grammar_en": "Present tense · pod + instrumental", "pl_grammar_uk": "Теперішній час · pod + орудний", "pl_grammar_pl": "Czas teraźniejszy · pod + narzędnik",
                "uk_grammar_en": "Present tense · під + instrumental", "uk_grammar_uk": "Теперішній час · під + орудний", "uk_grammar_pl": "Czas teraźniejszy · під + narzędnik"}
        else:
            l["variants"] = {"pl": PL[n], "uk": UK[n]}
            for tg in ("pl","uk"):
                for sp in ("en","uk","pl"):
                    l["variants"]["%s_grammar_%s" % (tg, sp)] = GR[n][tg][sp]
    json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("ok", sum(len(l["variants"]["pl"]) + len(l["variants"]["uk"]) for l in d))
