# MovieLang — «Щоденники вампіра: Сезон 1». Хелпери для опису уроків.
# Мова завдань: англійська. Пояснення (tip / why / label / scene / ins): українською.
# Репліки з серіалу — лише короткі фрази (≤10 слів), решта — власні речення.

L = []  # усі уроки курсу

def lesson(num, title, grammar, scene, arc, badge, tasks, cert=None):
    v = {"arc": arc, "badge": {"icon": badge[0], "name": badge[1], "text": badge[2]}}
    if cert: v["cert"] = cert
    L.append({"num": num, "title": title, "grammar": grammar, "scene": scene, "tasks": tasks, "variants": v})

def cards(recap, people, label="Попередньо в Містик Фоллс…"):
    """people: [(uk, en, role) | (uk, en, role, 'upd')]"""
    return {"type": "cards", "label": label, "q": recap, "img": None,
            "cards": [{"uk": p[0], "en": p[1], "role": p[2], **({"upd": True} if len(p) > 3 else {})} for p in people]}

def gloss(title, raw, img=None):
    """raw: рядки 'word|ipa|pos|lvl|uk|who|line|ex'"""
    items = []
    for line in raw.strip().split("\n"):
        line = line.strip()
        if not line: continue
        p = [x.strip() for x in line.split("|")]
        assert len(p) == 8, line
        items.append(dict(zip(("w", "ipa", "pos", "lvl", "uk", "who", "line", "ex"), p)))
    d = {"type": "glossary", "label": title, "q": "Відкривай слова, слухай вимову 🔊 і читай, хто і де це каже.", "items": items}
    if img: d["img"] = img
    return d

def _mc(kind, label, q, opts, ans, why, tip="", scene=None, img=None, ins=None, say=None, qt=None):
    assert len(why) == len(opts), q
    d = {"type": kind, "label": label, "q": q, "options": opts, "answer": ans, "why": why, "tip": tip}
    if scene: d["scene"] = scene
    if img: d["img"] = img
    if ins: d["ins"] = ins
    if say: d["say"] = say
    if qt: d["qt_uk"] = qt
    return d

def who(q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("quiz", "ХТО ЦЕ СКАЗАВ?", q, opts, ans, why, tip, scene, img, "Хто вимовляє цю фразу?")
def choice(q, opts, ans, why, tip="", scene=None, img=None, qt=None):
    return _mc("quiz", "ВИБІР ОЛЕНИ", q, opts, ans, why, tip, scene, img, "Обери найкращу відповідь англійською", qt=qt)
def sarcasm(q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("quiz", "САРКАЗМ ДЕЙМОНА", q, opts, ans, why, tip, scene, img, "Що Деймон насправді має на увазі?")
def lie(q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("quiz", "ТЕСТ НА ВЕРБЕНУ", q, opts, ans, why, tip, scene, img, "Хто бреше? Шукай мовні маркери")
def lie_tf(q, true, why, tip="", scene=None, img=None):
    return _mc("tf", "ТЕСТ НА ВЕРБЕНУ", q, ["True", "False"], 0 if true else 1, why, tip, scene, img, "Правда чи брехня?")
def council(q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("quiz", "РОЗСЛІДУВАННЯ РАДИ", q, opts, ans, why, tip, scene, img, "Прочитай підказки і зроби висновок")
def gram(q, opts, ans, why, tip="", scene=None, img=None, label="ГРАМАТИКА СЦЕНИ"):
    return _mc("grammar", label, q, opts, ans, why, tip, scene, img, "Обери правильну форму")
def word(q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("vocabulary", "СЛОВО З МІСТИК ҐРИЛЛЯ", q, opts, ans, why, tip, scene, img, "Обери слово, яке підходить")

def compel(sentence, tip, scene=None, q="Compel them: put the words in the right order."):
    d = {"type": "order", "label": "НАВІЮВАННЯ", "ins": "Склади фразу, яку ти навіюєш", "q": q, "options": sentence.split(), "tip": tip}
    if scene: d["scene"] = scene
    return d
def grimoire(q, answers, tip, scene=None, img=None):
    d = {"type": "type", "label": "ГРИМУАР", "ins": "Впиши пропущене слово", "q": q, "options": answers, "tip": tip}
    if scene: d["scene"] = scene
    if img: d["img"] = img
    return d
def page(q, answers, tip, scene=None, img="diary"):
    d = {"type": "type", "label": "СТОРІНКА ЩОДЕННИКА", "ins": "Впиши дієслово в правильній формі", "q": q, "options": answers, "tip": tip}
    if scene: d["scene"] = scene
    if img: d["img"] = img
    return d
def audio(say, answers, tip, scene=None):
    d = {"type": "type", "label": "АУДІОСЦЕНА", "ins": "Послухай і запиши почуте англійською", "q": "Listen and type what you hear.", "say": say, "options": answers, "tip": tip}
    if scene: d["scene"] = scene
    return d
def grill(pairs, tip, scene=None, q="Match the words with their meanings."):
    d = {"type": "match", "label": "СЛОВО З МІСТИК ҐРИЛЛЯ", "ins": "З'єднай пари", "q": q, "options": [a + "=" + b for a, b in pairs], "tip": tip}
    if scene: d["scene"] = scene
    return d
def profile(pairs, tip, scene=None):
    d = {"type": "match", "label": "СКЛАДИ ПРОФІЛЬ", "ins": "З'єднай персонажа з описом", "q": "Who is who in Mystic Falls right now?", "options": [a + "=" + b for a, b in pairs], "tip": tip}
    if scene: d["scene"] = scene
    return d
def speak(line, tip, scene=None):
    d = {"type": "speaking", "label": "ГОВОРІННЯ", "q": "Say it out loud.", "say": line, "tip": tip}
    if scene: d["scene"] = scene
    return d
def diary_final(q, minw, tip, scene=None):
    d = {"type": "final", "label": "ЩОДЕННИК ОЛЕНИ", "ins": "Напиши запис у щоденник англійською", "q": q, "answer": minw, "tip": tip, "img": "diary"}
    if scene: d["scene"] = scene
    return d

def quest(q, start, steps, endings, tip, scene=None, img=None):
    """steps: {id: (q, scene, [(text, next, ok, fb), ...])}; endings: {id: (title, text, good)}"""
    d = {"type": "quest", "label": "КВЕСТ", "ins": "Кожен вибір веде далі. Обирай уважно — англійською", "q": q, "start": start,
         "steps": {k: {"q": v[0], "scene": v[1], "choices": [{"t": c[0], "next": c[1], "ok": c[2], "fb": c[3]} for c in v[2]]} for k, v in steps.items()},
         "endings": {k: {"title": v[0], "text": v[1], "good": v[2]} for k, v in endings.items()}, "tip": tip}
    if scene: d["scene"] = scene
    if img: d["img"] = img
    return d

A1 = "Арка 1 · Новенький у місті"
A2 = "Арка 2 · Таємниці Сальваторе"
A3 = "Арка 3 · Кров і родовід"
A4 = "Арка 4 · Склеп"
A5 = "Арка 5 · День засновників"
