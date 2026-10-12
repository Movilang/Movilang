# Будує версії курсу для тих, хто вчить ПОЛЬСЬКУ (variants.pl) і УКРАЇНСЬКУ (variants.uk).
# Основа: ті самі сцени, картки, словник (польський/український відповідник + репліки цільовою мовою),
# власна граматика (gram_pl.py / gram_uk.py) і щоденник.
import os, re, random, importlib

HERE = os.path.dirname(os.path.abspath(__file__))
SUP = ("uk", "pl", "en")

LAB = {
 "match": ("СЛОВО З МІСТИК ҐРИЛЛЯ", "SŁOWO Z MYSTIC GRILL", "A WORD FROM THE MYSTIC GRILL"),
 "vocab": ("СЛОВНИК СЦЕНИ", "SŁOWNIK SCENY", "SCENE VOCABULARY"),
 "order": ("НАВІЮВАННЯ", "PERSWAZJA", "COMPULSION"),
 "audio": ("АУДІОСЦЕНА", "SCENA AUDIO", "AUDIO SCENE"),
 "speak": ("ГОВОРІННЯ", "MÓWIENIE", "SPEAKING"),
 "gram": ("ГРАМАТИКА СЦЕНИ", "GRAMATYKA SCENY", "SCENE GRAMMAR"),
 "repeat": ("ПОВТОРЕННЯ", "POWTÓRKA", "REVIEW"),
 "final": ("ЩОДЕННИК ОЛЕНИ", "PAMIĘTNIK ELENY", "ELENA'S DIARY"),
}
INS = {
 "match": ("З'єднай слово з перекладом", "Połącz słowo z tłumaczeniem", "Match each word with its translation"),
 "vocab": ("Обери правильне слово", "Wybierz właściwe słowo", "Choose the right word"),
 "order": ("Склади фразу, яку ти навіюєш", "Ułóż zdanie, które wmawiasz", "Build the sentence you compel"),
 "audio": ("Послухай і запиши почуте", "Posłuchaj i zapisz, co słyszysz", "Listen and type what you hear"),
 "speak": ("Послухай і повтори вголос", "Posłuchaj i powtórz na głos", "Listen and repeat aloud"),
 "gram": ("Обери правильну форму", "Wybierz poprawną formę", "Choose the correct form"),
 "final": ("Напиши запис у щоденник", "Napisz wpis do pamiętnika", "Write a diary entry"),
}
LANGNAME = {"pl": ("польське", "polskie", "Polish"), "uk": ("українське", "ukraińskie", "Ukrainian")}
Q = {  # тексти питань цільовою мовою
 "pl": {"match": "Połącz słowa ze sceny z tłumaczeniem.", "order": "Ułóż zdanie we właściwej kolejności.",
        "audio": "Posłuchaj i zapisz, co słyszysz.", "speak": "Powiedz to na głos.", "repeat": "Pamiętasz te słowa?"},
 "uk": {"match": "З'єднай слова зі сцени з перекладом.", "order": "Склади речення в правильному порядку.",
        "audio": "Послухай і запиши почуте.", "speak": "Скажи це вголос.", "repeat": "Пам'ятаєш ці слова?"},
}
QT = {
 "match": ("З'єднай слова зі сцени з перекладом.", "Połącz słowa ze sceny z tłumaczeniem.", "Match the words from the scene with their translations."),
 "order": ("Склади речення в правильному порядку.", "Ułóż zdanie we właściwej kolejności.", "Put the words in the right order."),
 "audio": ("Послухай і запиши почуте.", "Posłuchaj i zapisz, co słyszysz.", "Listen and type what you hear."),
 "speak": ("Скажи це вголос.", "Powiedz to na głos.", "Say it out loud."),
 "repeat": ("Пам'ятаєш ці слова?", "Pamiętasz te słowa?", "Do you still remember these words?"),
}

def load_gl():
    src = {}
    for line in open(os.path.join(HERE, "i18n", "gl_src.txt"), encoding="utf-8"):
        p = line.rstrip("\n").split("\t"); src[int(p[0])] = p[1]
    G = {}
    for f in sorted(os.listdir(os.path.join(HERE, "i18n"))):
        if not (f.startswith("g0") and f.endswith(".tsv")): continue
        for line in open(os.path.join(HERE, "i18n", f), encoding="utf-8"):
            if not line.strip(): continue
            p = line.rstrip("\n").split("\t")
            assert len(p) == 7, (f, line[:60])
            i = int(p[0])
            G[src[i]] = {"pl": {"w": p[1], "line": p[3], "ex": p[4]}, "uk": {"w": p[2], "line": p[5], "ex": p[6]}}
    return G

def tri(t3, prefix, d):
    d[prefix + "_uk"], d[prefix + "_pl"], d[prefix + "_en"] = t3
    d[prefix] = t3[0]

def lab(d, key):
    d["label"], d["label_pl"], d["label_en"] = LAB[key]
    if key in INS: d["ins"], d["ins_pl"], d["ins_en"] = INS[key]

def build(L, R, D_def):
    GL = load_gl()
    miss = set()
    for T in ("pl", "uk"):
        gm = importlib.import_module("gram_" + T)
        for l in L:
            n = l["num"]; rnd = random.Random(7000 + n + (0 if T == "pl" else 500))
            out, words, sentences = [], [], []
            for t in l["tasks"]:
                if t["type"] == "cards":
                    out.append(t)
                elif t["type"] == "glossary":
                    items = []
                    for it in t["items"]:
                        g = GL.get(it["w"])
                        if not g: miss.add(it["w"]); continue
                        gt = g[T]
                        ni = {"w": gt["w"], "ipa": "", "pos": it["pos"], "lvl": it["lvl"], "line": gt["line"], "ex": gt["ex"],
                              "who": it["who"], "who_pl": it.get("who_pl", it["who"]), "who_en": it.get("who_en", it["who"])}
                        # переклад слова мовою підказок
                        if T == "pl":
                            ni["uk"] = it["uk"]; ni["uk_uk"] = it["uk"]; ni["uk_en"] = it["w"]; ni["uk_pl"] = it["w"]
                        else:
                            ni["uk"] = it["w"]; ni["uk_uk"] = it["w"]; ni["uk_en"] = it["w"]; ni["uk_pl"] = it.get("uk_pl", it["w"])
                        items.append(ni)
                        words.append((gt["w"], {"uk": it["uk"].split(",")[0].split("(")[0].strip() if T == "pl" else it["w"],
                                                "pl": it.get("uk_pl", "").split(",")[0].split("(")[0].strip() if T == "uk" else it["w"],
                                                "en": it["w"]}, it))
                        if not gt["ex"].startswith("—"): sentences.append((gt["ex"], g, it))
                    nt = dict(t); nt["items"] = items
                    out.append(nt)
            # ---- завдання
            tasks = []
            def mk_match(ws, key="match", qk="match"):
                d = {"type": "match", "q": Q[T][qk]}
                lab(d, key)
                for s in SUP:
                    other = s if s != T else "en"
                    d["options_" + s] = ["%s=%s" % (w[0], w[1][other]) for w in ws]
                d["options"] = d["options_en"]
                tri(QT[qk], "qt", d); d.pop("qt")
                d["tip"], d["tip_pl"], d["tip_en"] = ("Ці слова звучать у сцені — повертайся до словника, якщо сумніваєшся.",
                    "Te słowa padają w scenie — wróć do słownika, jeśli masz wątpliwości.", "These words appear in the scene — go back to the glossary if unsure.")
                d["tip_uk"] = d["tip"]
                return d
            def mk_vocab(w, pool):
                opts = [w[0]] + rnd.sample([x[0] for x in pool if x[0] != w[0]], 3)
                rnd.shuffle(opts)
                d = {"type": "vocabulary", "options": opts, "answer": opts.index(w[0])}
                lab(d, "vocab")
                ln = LANGNAME[T]
                d["q"] = {"pl": "Które słowo znaczy „%s”?" % w[1]["en"], "uk": "Яке слово означає «%s»?" % w[1]["en"]}[T]
                d["q_uk"] = "Обери %s слово: «%s»" % (ln[0], w[1]["uk"] if T == "pl" else w[1]["en"])
                d["q_pl"] = "Wybierz %s słowo: „%s”" % (ln[1], w[1]["pl"] if T == "uk" else w[1]["en"])
                d["q_en"] = "Choose the %s word for “%s”" % (ln[2], w[1]["en"])
                it = w[2]
                d["tip"] = it["who"]; d["tip_uk"] = it["who"]; d["tip_pl"] = it.get("who_pl", it["who"]); d["tip_en"] = it.get("who_en", it["who"])
                wrong = ("Ні — «%s» тут не пасує.", "Nie — „%s” tu nie pasuje.", "No — “%s” doesn't fit here.")
                d["why_uk"] = [("Так!" if o == w[0] else wrong[0] % o) for o in opts]
                d["why_pl"] = [("Tak!" if o == w[0] else wrong[1] % o) for o in opts]
                d["why_en"] = [("Yes!" if o == w[0] else wrong[2] % o) for o in opts]
                d["why"] = d["why_uk"]
                return d
            def mk_order(sent):
                txt, g, it = sent
                d = {"type": "order", "q": Q[T]["order"], "options": txt.split()}
                lab(d, "order"); tri(QT["order"], "qt", d); d.pop("qt")
                o = "pl" if T == "uk" else "uk"
                d["tip_uk"] = "Переклад: " + (g["uk"]["ex"] if T == "pl" else it["ex"])
                d["tip_pl"] = "Tłumaczenie: " + (g["pl"]["ex"] if T == "uk" else it["ex"])
                d["tip_en"] = "Translation: " + it["ex"]
                d["tip"] = d["tip_uk"]
                return d
            def mk_audio(sent):
                txt, g, it = sent
                d = {"type": "type", "q": Q[T]["audio"], "say": txt, "options": [txt, re.sub(r"[.!?…]+$", "", txt)]}
                lab(d, "audio"); tri(QT["audio"], "qt", d); d.pop("qt")
                d["tip_uk"] = "Переклад: " + (g["uk"]["ex"] if T == "pl" else it["ex"])
                d["tip_pl"] = "Tłumaczenie: " + (g["pl"]["ex"] if T == "uk" else it["ex"])
                d["tip_en"] = "Translation: " + it["ex"]; d["tip"] = d["tip_uk"]
                return d
            def mk_speak(sent):
                txt, g, it = sent
                d = {"type": "speaking", "q": Q[T]["speak"], "say": txt}
                lab(d, "speak"); tri(QT["speak"], "qt", d); d.pop("qt")
                d["tip_uk"] = "Переклад: " + (g["uk"]["ex"] if T == "pl" else it["ex"])
                d["tip_pl"] = "Tłumaczenie: " + (g["pl"]["ex"] if T == "uk" else it["ex"])
                d["tip_en"] = "Translation: " + it["ex"]; d["tip"] = d["tip_uk"]
                return d
            def mk_gram(gt):
                q, opts, ans, whys, tip = gt
                idx = list(range(len(opts))); rnd.shuffle(idx)
                d = {"type": "grammar", "q": q, "options": [opts[i] for i in idx], "answer": idx.index(ans)}
                lab(d, "gram")
                d["why_uk"] = [whys[i][0] for i in idx]; d["why_pl"] = [whys[i][1] for i in idx]; d["why_en"] = [whys[i][2] for i in idx]
                d["why"] = d["why_uk"]
                d["tip"], d["tip_pl"], d["tip_en"] = tip; d["tip_uk"] = tip[0]
                return d
            single = len(sentences) and len(words) >= 8
            scenes = [w for w in words]
            boss = n in (5, 11, 16, 22, 27)
            final = n == 28
            if final:
                pool = [w for w in GLALL[T]]
                picks = rnd.sample(pool, 10)
                tasks += [mk_match(picks[:5]), mk_match(picks[5:10])]
                for w in rnd.sample(pool, 10): tasks.append(mk_vocab(w, pool))
                tasks += [mk_gram(g) for g in gm.G[28]]
                ss = rnd.sample(SENTALL[T], 5)
                tasks += [mk_order(ss[0]), mk_order(ss[1]), mk_audio(ss[2]), mk_audio(ss[3]), mk_speak(ss[4])]
            elif boss:
                pool = words
                tasks += [mk_match(words[0:5]), mk_match(words[5:10]), mk_match(words[10:15])]
                for w in rnd.sample(pool[15:], 3): tasks.append(mk_vocab(w, pool))
                tasks += [mk_gram(g) for g in gm.G[n]]
                ss = rnd.sample(sentences, 2)
                tasks += [mk_order(ss[0]), mk_audio(ss[1])]
            else:
                per = max(1, len(words) // 3)
                sc = [words[i * per:(i + 1) * per] for i in range(3)]
                ssc = [[s for s in sentences if any(s[2] is w[2] for w in part)] for part in sc]
                tasks.append(mk_match(sc[0][:5]))
                tasks.append(mk_vocab(rnd.choice(sc[0][5:] or sc[0]), words))
                tasks.append(mk_order(rnd.choice(ssc[0])))
                tasks.append(mk_gram(gm.G[n][0]))
                tasks.append(mk_match(sc[1][:5]))
                tasks.append(mk_vocab(rnd.choice(sc[1][5:] or sc[1]), words))
                tasks.append(mk_audio(rnd.choice(ssc[1])))
                tasks.append(mk_gram(gm.G[n][1]))
                tasks.append(mk_vocab(rnd.choice(sc[2]), words))
                tasks.append(mk_order(rnd.choice(ssc[2])))
                tasks.append(mk_speak(rnd.choice([s for s in ssc[2] if len(s[0].split()) <= 9] or ssc[2])))
                if R.get(n):
                    ws = [x for x in WORDALL[T] if x[1]["en"] in R[n]][:5]
                    if len(ws) >= 4: tasks.append(mk_match(ws, "repeat", "repeat"))
            if n in gm.D:
                q, mw, tip = gm.D[n]
                d = {"type": "final", "q": q, "answer": mw, "img": "diary"}
                lab(d, "final")
                d["tip"], d["tip_pl"], d["tip_en"] = tip; d["tip_uk"] = tip[0]
                tasks.append(d)
            l["variants"][T] = out + tasks
            gl = gm.T[n]
            l["variants"][T + "_grammar"] = gl[1] if T == "pl" else gl[0]
            l["variants"][T + "_grammar_uk"], l["variants"][T + "_grammar_pl"], l["variants"][T + "_grammar_en"] = gl
    return miss

GLALL, SENTALL, WORDALL = {}, {}, {}
def prepare(L):
    """Зібрати глобальні пули слів і речень для фіналу та повторення."""
    GL = load_gl()
    for T in ("pl", "uk"):
        ws, ss = [], []
        for l in L:
            for t in l["tasks"]:
                if t["type"] != "glossary": continue
                for it in t["items"]:
                    g = GL.get(it["w"])
                    if not g: continue
                    w = (g[T]["w"], {"uk": it["uk"].split(",")[0].split("(")[0].strip() if T == "pl" else it["w"],
                                     "pl": it.get("uk_pl", "").split(",")[0].split("(")[0].strip() if T == "uk" else it["w"],
                                     "en": it["w"]}, it)
                    if all(x[0] != w[0] for x in ws): ws.append(w)
                    if not g[T]["ex"].startswith("—"): ss.append((g[T]["ex"], g, it))
        GLALL[T] = ws; SENTALL[T] = ss; WORDALL[T] = ws
