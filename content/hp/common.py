# MovieLang — «Гаррі Поттер і філософський камінь» (B1→B2). Хелпери для опису уроків.
# Мова завдань: англійська. Пояснення (tip / why / label / scene / ins): українською → перекладаються в i18n.
# Репліки з фільму — лише короткі фрази (≤10 слів), решта — власні речення.

L = []

def lesson(num, title, grammar, scene, arc, badge, tasks, cert=None):
    v = {"arc": arc, "badge": {"icon": badge[0], "name": badge[1], "text": badge[2]}}
    if cert: v["cert"] = cert
    L.append({"num": num, "title": title, "grammar": grammar, "scene": scene, "tasks": tasks, "variants": v})

def cards(recap, people, label="Раніше у світі чарівників…"):
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

def _mc(kind, label, q, opts, ans, why, tip="", scene=None, img=None, ins=None, say=None):
    assert len(why) == len(opts), q
    d = {"type": kind, "label": label, "q": q, "options": opts, "answer": ans, "why": why, "tip": tip}
    if scene: d["scene"] = scene
    if img: d["img"] = img
    if ins: d["ins"] = ins
    if say: d["say"] = say
    return d

def who(q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("quiz", "ХТО ЦЕ СКАЗАВ?", q, opts, ans, why, tip, scene, img, "Хто вимовляє цю фразу?")
def choice(q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("quiz", "ВИБІР ГАРРІ", q, opts, ans, why, tip, scene, img, "Обери найкращу відповідь англійською")
def subtext(q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("quiz", "ПІДТЕКСТ", q, opts, ans, why, tip, scene, img, "Що насправді мається на увазі?")
def truth(q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("quiz", "ДЗЕРКАЛО ПРАВДИ", q, opts, ans, why, tip, scene, img, "Хто каже неправду? Шукай мовні маркери")
def truth_tf(q, true, why, tip="", scene=None, img=None):
    return _mc("tf", "ДЗЕРКАЛО ПРАВДИ", q, ["True", "False"], 0 if true else 1, why, tip, scene, img, "Правда чи ні?")
def case(q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("quiz", "СПРАВА ДЛЯ ТРІЙКИ", q, opts, ans, why, tip, scene, img, "Прочитай підказки і зроби висновок")
def gram(q, opts, ans, why, tip="", scene=None, img=None, label="ГРАМАТИКА СЦЕНИ"):
    return _mc("grammar", label, q, opts, ans, why, tip, scene, img, "Обери правильну форму")
def word(q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("vocabulary", "СЛОВО З ДІРЯВОГО КАЗАНА", q, opts, ans, why, tip, scene, img, "Обери слово, яке підходить")
def listen(say, q, opts, ans, why, tip="", scene=None, img=None):
    return _mc("listening", "АУДІОСЦЕНА", q, opts, ans, why, tip, scene, img, "Послухай і обери відповідь", say=say)

def spell(sentence, tip, scene=None, q="Cast it right: put the words in the correct order."):
    d = {"type": "order", "label": "ЗАКЛИНАННЯ", "ins": "Склади речення — як заклинання, без жодної помилки", "q": q, "options": sentence.split(), "tip": tip}
    if scene: d["scene"] = scene
    return d
def book(q, answers, tip, scene=None, img=None):
    d = {"type": "type", "label": "КНИГА ЗАКЛИНАНЬ", "ins": "Впиши пропущене слово", "q": q, "options": answers, "tip": tip}
    if scene: d["scene"] = scene
    if img: d["img"] = img
    return d
def owl(q, answers, tip, scene=None, img="owl"):
    d = {"type": "type", "label": "СОВИНА ПОШТА", "ins": "Впиши дієслово в правильній формі", "q": q, "options": answers, "tip": tip}
    if scene: d["scene"] = scene
    if img: d["img"] = img
    return d
def audio(say, answers, tip, scene=None):
    d = {"type": "type", "label": "АУДІОСЦЕНА", "ins": "Послухай і запиши почуте англійською", "q": "Listen and type what you hear.", "say": say, "options": answers, "tip": tip}
    if scene: d["scene"] = scene
    return d
def cauldron(pairs, tip, scene=None, q="Match the words with their meanings."):
    d = {"type": "match", "label": "СЛОВО З ДІРЯВОГО КАЗАНА", "ins": "З'єднай пари", "q": q, "options": [a + "=" + b for a, b in pairs], "tip": tip}
    if scene: d["scene"] = scene
    return d
def frogcards(pairs, tip, scene=None):
    d = {"type": "match", "label": "КАРТКИ З ШОКОЛАДНИХ ЖАБ", "ins": "З'єднай персонажа з описом", "q": "Who is who right now?", "options": [a + "=" + b for a, b in pairs], "tip": tip}
    if scene: d["scene"] = scene
    return d
def speak(line, tip, scene=None):
    d = {"type": "speaking", "label": "ГОВОРІННЯ", "q": "Say it out loud.", "say": line, "tip": tip}
    if scene: d["scene"] = scene
    return d
def letter(q, minw, tip, scene=None):
    d = {"type": "final", "label": "ЛИСТ СОВОЮ", "ins": "Напиши лист англійською", "q": q, "answer": minw, "tip": tip, "img": "owl"}
    if scene: d["scene"] = scene
    return d

def quest(q, start, steps, endings, tip, scene=None, img=None):
    """steps: {id: (q, scene, [(text, next, ok, fb), ...])}; endings: {id: (title, text, good)}"""
    d = {"type": "quest", "label": "ПРИГОДА", "ins": "Кожен вибір веде далі. Обирай уважно — англійською", "q": q, "start": start,
         "steps": {k: {"q": v[0], "scene": v[1], "choices": [{"t": c[0], "next": c[1], "ok": c[2], "fb": c[3]} for c in v[2]]} for k, v in steps.items()},
         "endings": {k: {"title": v[0], "text": v[1], "good": v[2]} for k, v in endings.items()}, "tip": tip}
    if scene: d["scene"] = scene
    if img: d["img"] = img
    return d

A1 = "Арка 1 · Хлопчик, який вижив"
A2 = "Арка 2 · Світ чарівників"
A3 = "Арка 3 · Ласкаво просимо до Гоґвортсу"
A4 = "Арка 4 · Тролі, квідич і Різдво"
A5 = "Арка 5 · Таємниця третього поверху"
A6 = "Арка 6 · Крізь люк"
BOSS = {5: (1, 2, 3, 4), 11: (6, 7, 8, 9, 10), 17: (12, 13, 14, 15, 16), 23: (18, 19, 20, 21, 22), 29: (24, 25, 26, 27, 28), 35: (30, 31, 32, 33, 34)}
FINAL = 36
