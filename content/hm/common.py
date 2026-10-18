# MoviLang — «Як я познайомився з вашою мамою. Сезон 1» (HIMYM), рівень B1–B2. Хелпери для опису уроків.
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

def cards(recap, people, label=("Діти, раніше в серіалі…", "Dzieciaki, w poprzednich odcinkach…", "Kids, previously…")):
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
        items.append({"w": w, "ipa": ipa, "pos": pos, "lvl": lvl, "uk": uk, "who": who, "line": ln, "ex": ex})
        uk_word = uk.split(",")[0].split("(")[0].strip()
        GL.setdefault(w, {"pl": {"w": pl.split(",")[0].split("(")[0].strip(), "line": pl_line, "ex": pl_ex},
                          "uk": {"w": uk_word, "line": uk_line, "ex": uk_ex}})
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
 "choice": ("ПОРАДА В БАРІ MACLAREN'S", "PORADA W BARZE MACLAREN'S", "ADVICE AT MACLAREN'S"),
 "bandits": ("ПРАВИЛО БАРНІ", "ZASADA BARNEYA", "BARNEY'S RULE"),
 "lie": ("ДЕТЕКТОР БРЕХНІ", "WYKRYWACZ KŁAMSTW", "LIE DETECTOR"),
 "police": ("ЛЕКЦІЯ ТЕДА", "WYKŁAD TEDA", "TED'S LECTURE"),
 "trap": ("ЯК ЦЕ ЗРОЗУМІЛА РОБІН?", "JAK ZROZUMIAŁA TO ROBIN?", "HOW DID ROBIN GET IT?"),
 "gram": ("ГРАМАТИКА СЦЕНИ", "GRAMATYKA SCENY", "SCENE GRAMMAR"),
 "word": ("СЛОВО З MACLAREN'S", "SŁOWO Z MACLAREN'S", "A WORD FROM MACLAREN'S"),
 "order": ("ІСТОРІЯ ДЛЯ ДІТЕЙ", "HISTORIA DLA DZIECI", "A STORY FOR THE KIDS"),
 "time": ("ЩО БУЛО НАСПРАВДІ?", "CO BYŁO NAPRAWDĘ?", "WHAT REALLY HAPPENED?"),
 "note": ("СЕРВЕТКА ТЕДА", "SERWETKA TEDA", "TED'S NAPKIN"),
 "list": ("ПЛЕЙБУК БАРНІ", "PLAYBOOK BARNEYA", "BARNEY'S PLAYBOOK"),
 "kitchen": ("СЛОВА І ЗНАЧЕННЯ", "SŁOWA I ZNACZENIA", "WORDS AND MEANINGS"),
 "profile": ("ХТО Є ХТО", "KTO JEST KIM", "WHO'S WHO"),
 "speak": ("ГОВОРІННЯ", "MÓWIENIE", "SPEAKING"),
 "final": ("ЛИСТ ДІТЯМ ІЗ МАЙБУТНЬОГО", "LIST DO DZIECI Z PRZYSZŁOŚCI", "A LETTER TO THE KIDS"),
 "quest": ("КВЕСТ", "QUEST", "QUEST"),
 "announce": ("НОВИНИ МЕТРО-НЬЮЗ 1", "WIADOMOŚCI METRO NEWS 1", "METRO NEWS 1"),
 "phone": ("ГОЛОСОВЕ ПОВІДОМЛЕННЯ", "WIADOMOŚĆ GŁOSOWA", "VOICEMAIL"),
 "map": ("ПЛАН ВЕЧОРА", "PLAN NA WIECZÓR", "THE PLAN FOR TONIGHT"),
 "walkie": ("ЕСЕМЕСКА", "SMS", "TEXT MESSAGE"),
 "news": ("ОГОЛОШЕННЯ", "OGŁOSZENIE", "THE AD"),
}
INS = {
 "who": ("Хто з п'ятірки каже цю фразу?", "Kto z piątki mówi to zdanie?", "Which of the five says this line?"),
 "choice": ("Обери найкращу відповідь англійською", "Wybierz najlepszą odpowiedź po angielsku", "Choose the best answer in English"),
 "bandits": ("Що Барні насправді має на увазі?", "Co Barney naprawdę ma na myśli?", "What does Barney really mean?"),
 "lie": ("Хто каже неправду? Шукай мовні підказки", "Kto mówi nieprawdę? Szukaj wskazówek w języku", "Who isn't telling the truth? Look for language clues"),
 "lie_tf": ("Правда чи ні?", "Prawda czy nie?", "True or false?"),
 "police": ("Тед читає лекцію. Зроби висновок із фактів", "Ted robi wykład. Wyciągnij wniosek z faktów", "Ted is lecturing. Draw a conclusion from the facts"),
 "trap": ("Робін — канадка й не знає цієї ідіоми. Що вона означає?", "Robin jest Kanadyjką i nie zna tego idiomu. Co on znaczy?", "Robin is Canadian and doesn't know this idiom. What does it mean?"),
 "gram": ("Обери правильну форму", "Wybierz poprawną formę", "Choose the correct form"),
 "word": ("Обери слово, яке підходить", "Wybierz pasujące słowo", "Choose the word that fits"),
 "order": ("Склади речення — так Тед розповідає дітям", "Ułóż zdanie — tak Ted opowiada dzieciom", "Build the sentence — the way Ted tells it to his kids"),
 "time": ("Розстав події в правильному порядку", "Ułóż wydarzenia we właściwej kolejności", "Put the events in the right order"),
 "note": ("Впиши слово в правильній формі", "Wpisz słowo w poprawnej formie", "Write the word in the correct form"),
 "list": ("Впиши пропущене слово", "Wpisz brakujące słowo", "Write the missing word"),
 "kitchen": ("З'єднай пари", "Połącz pary", "Match the pairs"),
 "profile": ("З'єднай персонажа з описом", "Połącz postać z opisem", "Match each character with a description"),
 "final": ("Напиши текст англійською", "Napisz tekst po angielsku", "Write a text in English"),
 "quest": ("Кожен вибір веде далі. Обирай уважно — англійською", "Każdy wybór prowadzi dalej. Wybieraj uważnie — po angielsku", "Every choice leads on. Choose carefully — in English"),
 "announce": ("Прочитай новину Робін і дай відповідь", "Przeczytaj wiadomość Robin i odpowiedz", "Read Robin's news report and answer"),
 "phone": ("Прочитай голосове повідомлення й обери відповідь", "Przeczytaj wiadomość głosową i wybierz odpowiedź", "Read the voicemail and choose the answer"),
 "map": ("Подивись на план і подумай, що станеться", "Spójrz na plan i pomyśl, co się stanie", "Look at the plan and work out what will happen"),
 "walkie": ("Прочитай есемеску. Що вона означає?", "Przeczytaj SMS. Co on znaczy?", "Read the text message. What does it mean?"),
 "news": ("Прочитай оголошення і знайди, що воно означає", "Przeczytaj ogłoszenie i znajdź, co znaczy", "Read the ad and find what it means"),
}

def who(q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("quiz", LB["who"], q, opts, ans, why, tip, scene, img, INS["who"])
def choice(q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("quiz", LB["choice"], q, opts, ans, why, tip, scene, img, INS["choice"])
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

A1 = ("Арка 1 · Синій валторн", "Łuk 1 · Niebieski róg", "Arc 1 · The Blue French Horn")
A2 = ("Арка 2 · Правила гри", "Łuk 2 · Zasady gry", "Arc 2 · Rules of the Game")
A3 = ("Арка 3 · Вікторія", "Łuk 3 · Victoria", "Arc 3 · Victoria")
A4 = ("Арка 4 · Після другої ночі", "Łuk 4 · Po drugiej w nocy", "Arc 4 · After 2 A.M.")
A5 = ("Арка 5 · Танець дощу", "Łuk 5 · Taniec deszczu", "Arc 5 · The Rain Dance")
A6 = ("Арка 6 · Сан-Франциско", "Łuk 6 · San Francisco", "Arc 6 · San Francisco")

# Псевдоніми з назвами HIMYM
barney, robin, lecture, news1, voicemail, plan, text, ad = bandits, trap, police, announce, phone, trapmap, walkie, news
tale, events, napkin, playbook = trapline, timeline, note, shoplist
