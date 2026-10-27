# MoviLang — «Тачки» (Cars), рівень A1 (підходить і дітям). Хелпери для опису уроків.
# Мова завдань: англійська. Пояснення пишемо одразу трьома мовами: (uk, pl, en).
# Переклади реєструються в X і підставляються збиральником у поля *_pl / *_en.
# Репліки з фільму — лише короткі фрази (≤10 слів), решта — власні речення.

L = []    # усі уроки курсу
X = {}    # uk → (pl, en)
GL = {}   # англійське слово → {"pl": {...}, "uk": {...}} для польської / української версій

def u(s):
    """(uk, pl, en) → uk (і реєстрація перекладу); рядок повертається як є."""
    if isinstance(s, tuple):
        assert len(s) == 3 and all(isinstance(x, str) for x in s), s
        X[s[0]] = (s[1], s[2])
        return s[0]
    return s

def us(lst): return [u(x) for x in lst]

def lesson(num, title, grammar, scene, arc, badge, tasks, cert=None):
    v = {"arc": u(arc), "badge": {"icon": badge[0], "name": u(badge[1]), "text": u(badge[2])}}
    if cert: v["cert"] = u(cert)
    L.append({"num": num, "title": u(title), "grammar": grammar, "scene": u(scene), "tasks": tasks, "variants": v})

def cards(recap, people, label=("Раніше у фільмі…", "Wcześniej w filmie…", "Previously in Cars…")):
    """people: [(uk, en, role3) | (uk, en, role3, 'upd')]"""
    return {"type": "cards", "label": u(label), "q": u(recap), "img": None,
            "cards": [{"uk": p[0], "en": p[1], "role": u(p[2]), **({"upd": True} if len(p) > 3 else {})} for p in people]}

def gloss(title, raw, img=None):
    """Рядок: word|ipa|pos|lvl|uk|pl|who_uk|who_pl|who_en|line|ex|pl_line|pl_ex|uk_line|uk_ex"""
    items = []
    for line in raw.strip().split("\n"):
        line = line.strip()
        if not line: continue
        p = [x.strip() for x in line.split("|")]
        assert len(p) == 15, (len(p), line[:80])
        w, ipa, pos, lvl, uk, pl, who, who_pl, who_en, ln, ex, pl_line, pl_ex, uk_line, uk_ex = p
        X[uk] = (pl, w)
        X[who] = (who_pl, who_en)
        uk_word = uk.split(",")[0].split("(")[0].strip()
        g = {"pl": {"w": pl.split(",")[0].split("(")[0].strip(), "line": pl_line, "ex": pl_ex},
             "uk": {"w": uk_word, "line": uk_line, "ex": uk_ex}}
        items.append({"w": w, "ipa": ipa, "pos": pos, "lvl": lvl, "uk": uk, "who": who, "line": ln, "ex": ex, "_g": g})
        GL.setdefault(w, g)
    d = {"type": "glossary", "label": u(title), "q": u(("Відкривай слова і читай, хто і де це каже.", "Otwieraj słowa i czytaj, kto i gdzie to mówi.", "Open the words and read who says them and where.")), "items": items}
    if img: d["img"] = img
    return d

def boss_gloss(title, nums, per=9):
    """Повторення арки: по `per` слів з кожного уроку арки (уже описаних вище)."""
    items, seen = [], set()
    for l in L:
        if l["num"] not in nums: continue
        k = 0
        for t in l["tasks"]:
            if t["type"] != "glossary": continue
            for it in t["items"]:
                if k >= per or it["w"] in seen: continue
                seen.add(it["w"]); items.append(dict(it)); k += 1
    return {"type": "glossary", "label": u(title), "q": u(("Повтори ключові слова арки.", "Powtórz kluczowe słowa łuku.", "Review the arc's key words.")), "items": items}

def _mc(kind, label, q, opts, ans, why, tip="", scene=None, img=None, ins=None, say=None, qt=None):
    assert len(why) == len(opts), q
    d = {"type": kind, "label": u(label), "q": u(q), "options": opts, "answer": ans, "why": us(why), "tip": u(tip)}
    if scene: d["scene"] = u(scene)
    if img: d["img"] = img
    if ins: d["ins"] = u(ins)
    if say: d["say"] = say
    if qt: d["qt_uk"] = u(qt)
    return d

LB = {
 "who": ("ХТО ЦЕ СКАЗАВ?", "KTO TO POWIEDZIAŁ?", "WHO SAID IT?"),
 "choice": ("ЩО СКАЗАТИ?", "CO POWIEDZIEĆ?", "WHAT TO SAY?"),
 "doc": ("ПОРАДА ДОКА", "RADA DOCA", "DOC'S TIP"),
 "bandits": ("ЩО МАВ НА УВАЗІ МЕТР?", "CO MIAŁ NA MYŚLI ZŁOMEK?", "WHAT DOES MATER MEAN?"),
 "lie": ("ПРАВДА ЧИ НІ?", "PRAWDA CZY NIE?", "TRUE OR FALSE?"),
 "police": ("СПРАВА ШЕРИФА", "SPRAWA SZERYFA", "THE SHERIFF'S CASE"),
 "trap": ("ЯК ЦЕ ЗРОЗУМІВ ГВІДО?", "JAK ZROZUMIAŁ TO GUIDO?", "HOW DID GUIDO GET IT?"),
 "gram": ("ГРАМАТИКА СЦЕНИ", "GRAMATYKA SCENY", "SCENE GRAMMAR"),
 "word": ("СЛОВО З РАДІАТОР-СПРІНГС", "SŁOWO Z CHŁODNICY GÓRSKIEJ", "A WORD FROM RADIATOR SPRINGS"),
 "order": ("РАДІО КОМАНДИ", "RADIO ZESPOŁU", "TEAM RADIO"),
 "time": ("ЩО СТАЛОСЯ?", "CO SIĘ STAŁO?", "WHAT HAPPENED?"),
 "note": ("ТАБЛО ГОНКИ", "TABLICA WYNIKÓW", "RACE BOARD"),
 "list": ("МЕНЮ ФЛО", "MENU FLO", "FLO'S MENU"),
 "kitchen": ("СЛОВА І ЗНАЧЕННЯ", "SŁOWA I ZNACZENIA", "WORDS AND MEANINGS"),
 "profile": ("ХТО Є ХТО", "KTO JEST KIM", "WHO'S WHO"),
 "speak": ("ГОВОРІННЯ", "MÓWIENIE", "SPEAKING"),
 "final": ("ЛИСТ ДРУГОВІ", "LIST DO PRZYJACIELA", "LETTER TO A FRIEND"),
 "quest": ("КВЕСТ", "QUEST", "QUEST"),
 "announce": ("КОМЕНТАТОР ГОНКИ", "KOMENTATOR WYŚCIGU", "RACE COMMENTATOR"),
 "phone": ("ДЗВІНОК АГЕНТА", "TELEFON OD AGENTA", "CALL FROM THE AGENT"),
 "map": ("КАРТА ДОРОГИ 66", "MAPA DROGI 66", "ROUTE 66 MAP"),
 "walkie": ("РАЦІЯ МАКА", "KRÓTKOFALÓWKA MAŃKA", "MACK'S CB RADIO"),
 "news": ("НОВИНИ ГОНОК", "WIADOMOŚCI WYŚCIGOWE", "RACING NEWS"),
}
INS = {
 "who": ("Хто з героїв каже цю фразу?", "Która postać mówi to zdanie?", "Which character says this line?"),
 "choice": ("Обери найкращу відповідь англійською", "Wybierz najlepszą odpowiedź po angielsku", "Choose the best answer in English"),
 "bandits": ("Метр каже по-своєму. Що він насправді має на увазі?", "Złomek mówi po swojemu. Co naprawdę ma na myśli?", "Mater says it his way. What does he really mean?"),
 "lie": ("Хто каже неправду? Шукай підказки", "Kto mówi nieprawdę? Szukaj wskazówek", "Who isn't telling the truth? Look for clues"),
 "lie_tf": ("Правда чи ні?", "Prawda czy nie?", "True or false?"),
 "police": ("Прочитай докази і зроби висновок", "Przeczytaj dowody i wyciągnij wniosek", "Read the clues and solve the case"),
 "trap": ("Гвідо ще погано знає англійську й зрозумів усе буквально. Що фраза означає насправді?", "Guido słabo zna angielski i zrozumiał wszystko dosłownie. Co to naprawdę znaczy?", "Guido doesn't know much English and took it literally. What does it really mean?"),
 "gram": ("Обери правильну форму", "Wybierz poprawną formę", "Choose the correct form"),
 "word": ("Обери слово, яке підходить", "Wybierz pasujące słowo", "Choose the word that fits"),
 "order": ("Склади речення для радіо команди", "Ułóż zdanie do radia zespołu", "Build the sentence for the team radio"),
 "time": ("Розстав події в правильному порядку", "Ułóż wydarzenia we właściwej kolejności", "Put the events in the right order"),
 "note": ("Впиши слово в правильній формі", "Wpisz słowo w poprawnej formie", "Write the word in the correct form"),
 "list": ("Впиши пропущене слово", "Wpisz brakujące słowo", "Write the missing word"),
 "kitchen": ("З'єднай пари", "Połącz pary", "Match the pairs"),
 "profile": ("З'єднай героя з описом", "Połącz postać z opisem", "Match each character with a description"),
 "final": ("Напиши текст англійською", "Napisz tekst po angielsku", "Write a text in English"),
 "quest": ("Кожен вибір веде далі. Обирай уважно — англійською", "Każdy wybór prowadzi dalej. Wybieraj uważnie — po angielsku", "Every choice leads on. Choose carefully — in English"),
 "announce": ("Прочитай, що каже коментатор, і дай відповідь", "Przeczytaj, co mówi komentator, i odpowiedz", "Read what the commentator says and answer"),
 "phone": ("Прочитай, що каже агент Гарв, і обери відповідь", "Przeczytaj, co mówi agent Harv, i wybierz odpowiedź", "Read what Harv the agent says and choose the answer"),
 "map": ("Подивись на карту і подумай, куди їхати", "Spójrz na mapę i pomyśl, dokąd jechać", "Look at the map and work out where to drive"),
 "walkie": ("Мак говорить по рації. Що це означає?", "Maniek mówi przez krótkofalówkę. Co to znaczy?", "Mack is on the CB radio. What does it mean?"),
 "news": ("Прочитай новину і знайди, що вона означає", "Przeczytaj wiadomość i znajdź, co znaczy", "Read the news and find what it means"),
}

def who(q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("quiz", LB["who"], q, opts, ans, why, tip, scene, img, INS["who"])
def choice(q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("quiz", LB["choice"], q, opts, ans, why, tip, scene, img, INS["choice"])
def doc(q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("quiz", LB["doc"], q, opts, ans, why, tip, scene, img, INS["choice"])
def bandits(q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("quiz", LB["bandits"], q, opts, ans, why, tip, scene, img, INS["bandits"])
def lie(q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("quiz", LB["lie"], q, opts, ans, why, tip, scene, img, INS["lie"])
def lie_tf(q, true, why, tip="", scene=None, img=None):
    return _mc("tf", LB["lie"], q, ["True", "False"], 0 if true else 1, why, tip, scene, img, INS["lie_tf"])
def police(q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("quiz", LB["police"], q, opts, ans, why, tip, scene, img, INS["police"])
def trap(q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("quiz", LB["trap"], q, opts, ans, why, tip, scene, img, INS["trap"])
def announce(q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("quiz", LB["announce"], q, opts, ans, why, tip, scene, img, INS["announce"])
def phone(q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("quiz", LB["phone"], q, opts, ans, why, tip, scene, img, INS["phone"])
def trapmap(q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("quiz", LB["map"], q, opts, ans, why, tip, scene, img, INS["map"])
def walkie(q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("quiz", LB["walkie"], q, opts, ans, why, tip, scene, img, INS["walkie"])
def news(q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("quiz", LB["news"], q, opts, ans, why, tip, scene, img, INS["news"])
def gram(q, opts, ans, why, tip="", scene=None, img=None, label=None):
    return _mc("grammar", label or LB["gram"], q, opts, ans, why, tip, scene, img, INS["gram"])
def word(q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("vocabulary", LB["word"], q, opts, ans, why, tip, scene, img, INS["word"])

def _base(kind, label, ins, q, extra, tip, scene=None, img=None):
    d = {"type": kind, "label": u(label), "ins": u(ins), "q": u(q), "tip": u(tip)}
    d.update(extra)
    if scene: d["scene"] = u(scene)
    if img: d["img"] = img
    return d

def trapline(sentence, tip, scene=None, q="Build the line: put the words in the right order."):
    return _base("order", LB["order"], INS["order"], q, {"options": sentence.split()}, tip, scene)
def timeline(events, tip, scene=None, q="What happened first? Put the events in order."):
    return _base("order", LB["time"], INS["time"], q, {"options": list(events)}, tip, scene)
def note(q, answers, tip, scene=None, img=None):
    return _base("type", LB["note"], INS["note"], q, {"options": answers}, tip, scene, img)
def shoplist(q, answers, tip, scene=None, img=None):
    return _base("type", LB["list"], INS["list"], q, {"options": answers}, tip, scene, img)
def kitchen(pairs, tip, scene=None, q="Match the words with their meanings."):
    return _base("match", LB["kitchen"], INS["kitchen"], q, {"options": [a + "=" + b for a, b in pairs]}, tip, scene)
def profile(pairs, tip, scene=None, q="Who is who in the group?"):
    return _base("match", LB["profile"], INS["profile"], q, {"options": [a + "=" + b for a, b in pairs]}, tip, scene)
def speak(line, tip, scene=None):
    d = {"type": "speaking", "label": u(LB["speak"]), "q": "Say it out loud.", "say": line, "tip": u(tip)}
    if scene: d["scene"] = u(scene)
    return d
def letter(q, minw, tip, scene=None, img="letter"):
    d = {"type": "final", "label": u(LB["final"]), "ins": u(INS["final"]), "q": q, "answer": minw, "tip": u(tip), "img": img}
    if scene: d["scene"] = u(scene)
    return d

def quest(q, start, steps, endings, tip, scene=None, img=None):
    """steps: {id: (q, scene3, [(text, next, ok, fb3), ...])}; endings: {id: (title3, text3, good)}"""
    d = {"type": "quest", "label": u(LB["quest"]), "ins": u(INS["quest"]), "q": q, "start": start,
         "steps": {k: {"q": v[0], "scene": u(v[1]), "choices": [{"t": c[0], "next": c[1], "ok": c[2], "fb": u(c[3])} for c in v[2]]} for k, v in steps.items()},
         "endings": {k: {"title": u(v[0]), "text": u(v[1]), "good": v[2]} for k, v in endings.items()}, "tip": u(tip)}
    if scene: d["scene"] = u(scene)
    if img: d["img"] = img
    return d

A1 = ("Арка 1 · Новачок-зірка", "Łuk 1 · Gwiazda-debiutant", "Arc 1 · The Rookie Star")
A2 = ("Арка 2 · Загублений на трасі 66", "Łuk 2 · Zagubiony na drodze 66", "Arc 2 · Lost on Route 66")
A3 = ("Арка 3 · Нові друзі", "Łuk 3 · Nowi przyjaciele", "Arc 3 · New Friends")
A4 = ("Арка 4 · Таємниця Дока", "Łuk 4 · Tajemnica Doca", "Arc 4 · Doc's Secret")
A5 = ("Арка 5 · Нова дорога", "Łuk 5 · Nowa droga", "Arc 5 · The New Road")
A6 = ("Арка 6 · Велика гонка", "Łuk 6 · Wielki wyścig", "Arc 6 · The Big Race")

# Псевдоніми з назвами «Тачок»
mater, guido, sheriff, sheriff_case, commentator, agent, routemap, cb, racenews = bandits, trap, lie, police, announce, phone, trapmap, walkie, news
report, events, board, menu = trapline, timeline, note, shoplist
