# Додає до кожного уроку «тренування»: граматичний блок (6 речень) і словниковий блок (6 речень).
import re, random, importlib

LAB = {"gram": ("ГРАМАТИЧНЕ ТРЕНУВАННЯ", "TRENING GRAMATYCZNY", "GRAMMAR DRILL"),
       "vocab": ("СЛОВНИКОВЕ ТРЕНУВАННЯ", "TRENING SŁOWNICTWA", "VOCABULARY DRILL")}
INS = {"gram": ("Шість речень на тему уроку. Потрібно 70%+", "Sześć zdań na temat lekcji. Potrzeba 70%+", "Six sentences on the lesson topic. You need 70%+"),
       "vocab": ("Шість слів зі сцен цього уроку", "Sześć słów ze scen tej lekcji", "Six words from this lesson's scenes")}
TIP = {"gram": ("Кожне речення тренує одну граматичну тему — так вона закріплюється.", "Każde zdanie ćwiczy ten sam temat — tak się utrwala.", "Each sentence practises the same point — that's how it sticks."),
       "vocab": ("Слова повертатимуться в наступних уроках.", "Słowa wrócą w kolejnych lekcjach.", "These words will come back in later lessons.")}
QG = {"en": "Complete the sentences.", "pl": "Uzupełnij zdania.", "uk": "Доповни речення."}
QV = {"en": "Fill each gap with a word from the scene.", "pl": "Wybierz słowo ze sceny.", "uk": "Обери слово зі сцени."}

def _base(kind, target, items):
    d = {"type": "drill", "q": QG[target] if kind == "gram" else QV[target], "items": items}
    Q = QG if kind == "gram" else QV
    d["q_uk"], d["q_pl"], d["q_en"] = Q["uk"], Q["pl"], Q["en"]
    d["label"], d["label_pl"], d["label_en"] = LAB[kind]
    d["ins"], d["ins_pl"], d["ins_en"] = INS[kind]
    d["tip"], d["tip_pl"], d["tip_en"] = TIP[kind]; d["tip_uk"] = TIP[kind][0]
    return d

def gram_drill(target, rows, seed):
    rnd = random.Random(seed); items = []
    for q, opts, ans, exp in rows:
        idx = list(range(len(opts))); rnd.shuffle(idx)
        it = {"q": q, "options": [opts[i] for i in idx], "answer": idx.index(ans)}
        it["exp"], it["exp_pl"], it["exp_en"] = exp; it["exp_uk"] = exp[0]
        items.append(it)
    return _base("gram", target, items)

def en_vocab_drill(gloss_items, pool, seed):
    """Англійська: речення-приклад із пропуском на місці слова."""
    rnd = random.Random(seed); items = []
    cands = []
    for it in gloss_items:
        w = re.sub(r"^to ", "", it["w"]); w = re.sub(r"\s*\(.*?\)", "", w).strip()
        if len(w) < 3 or it["ex"].startswith("—"): continue
        m = re.search(r"\b" + re.escape(w) + r"\b", it["ex"], re.I)
        if m: cands.append((it, w, m))
    rnd.shuffle(cands)
    words = [re.sub(r"\s*\(.*?\)", "", re.sub(r"^to ", "", x["w"])).strip() for x in pool]
    for it, w, m in cands[:6]:
        q = it["ex"][:m.start()] + "____" + it["ex"][m.end():]
        wrong = [x for x in words if x.lower() != w.lower() and len(x) > 2]
        opts = [m.group(0)] + rnd.sample(wrong, 2); rnd.shuffle(opts)
        d = {"q": q, "options": opts, "answer": opts.index(m.group(0))}
        d["exp"] = d["exp_uk"] = "%s — %s" % (it["w"], it["uk"]); d["exp_pl"] = "%s — %s" % (it["w"], it.get("uk_pl", it["uk"])); d["exp_en"] = "%s — %s" % (it["w"], it.get("uk_en", ""))
        items.append(d)
    return _base("vocab", "en", items) if len(items) >= 4 else None

def tgt_vocab_drill(target, words, seed):
    """Польська/українська: 6 слів — обери слово цільовою мовою за перекладом."""
    rnd = random.Random(seed); items = []
    pick = rnd.sample(words, min(6, len(words)))
    LN = {"pl": ("польське", "polskie", "Polish"), "uk": ("українське", "ukraińskie", "Ukrainian")}[target]
    for w in pick:
        opts = [w[0]] + rnd.sample([x[0] for x in words if x[0] != w[0]], 2); rnd.shuffle(opts)
        d = {"options": opts, "answer": opts.index(w[0])}
        d["q"] = "„%s”" % w[1]["en"]
        d["q_uk"] = "«%s» → %s слово?" % (w[1]["uk"] if target == "pl" else w[1]["en"], LN[0])
        d["q_pl"] = "„%s” → %s słowo?" % (w[1]["pl"] if target == "uk" else w[1]["en"], LN[1])
        d["q_en"] = "“%s” → the %s word?" % (w[1]["en"], LN[2])
        it = w[2]
        d["exp"] = d["exp_uk"] = it["who"]; d["exp_pl"] = it.get("who_pl", it["who"]); d["exp_en"] = it.get("who_en", it["who"])
        items.append(d)
    return _base("vocab", target, items)

BOSS = {6: (1, 2, 3, 4, 5), 14: (7, 8, 9, 10, 11, 12, 13), 21: (15, 16, 17, 18, 19, 20), 28: (22, 23, 24, 25, 26, 27), 35: (29, 30, 31, 32, 33, 34)}
def boss_rows(D, b):
    rows = []
    for n in BOSS[b]: rows += D[n][2:4]
    return rows[:8]

def insert_before_final(tasks, new):
    i = len(tasks)
    for k in range(len(tasks) - 1, -1, -1):
        if tasks[k]["type"] == "final": i = k; break
    for t in new:
        if t: tasks.insert(i, t); i += 1

def apply_en(L):
    import drills_en
    for l in L:
        n = l["num"]; new = []
        if n in drills_en.D: new.append(gram_drill("en", drills_en.D[n], 900 + n))
        elif n in BOSS: new.append(gram_drill("en", boss_rows(drills_en.D, n), 900 + n))
        gl = [it for t in l["tasks"] if t["type"] == "glossary" for it in t["items"]]
        if gl and n != 36: new.append(en_vocab_drill(gl, gl, 950 + n))
        insert_before_final(l["tasks"], new)

def apply_target(L, target, words_of):
    D = importlib.import_module("drills_" + target).D
    for l in L:
        n = l["num"]; vt = l["variants"][target]; new = []
        if n in D: new.append(gram_drill(target, D[n], 1900 + n))
        elif n in BOSS: new.append(gram_drill(target, boss_rows(D, n), 1900 + n))
        ws = words_of(l, target)
        if len(ws) >= 6 and n != 36: new.append(tgt_vocab_drill(target, ws, 1950 + n))
        insert_before_final(vt, new)
