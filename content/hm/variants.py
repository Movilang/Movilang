# Будує версії курсу для тих, хто вчить ПОЛЬСЬКУ (variants.pl) і УКРАЇНСЬКУ (variants.uk).
# Основа: ті самі сцени, картки, словник (польський/український відповідник + репліки цільовою мовою),
# власна граматика (gram_pl.py / gram_uk.py) і щоденник.
import os, re, random, importlib

HERE = os.path.dirname(os.path.abspath(__file__))
SUP = ("uk", "pl", "en")

LAB = {
 "match": ("СЛОВО З MACLAREN'S", "SŁOWO Z MACLAREN'S", "A WORD FROM MACLAREN'S"),
 "vocab": ("СЛОВНИК СЦЕНИ", "SŁOWNIK SCENY", "SCENE VOCABULARY"),
 "order": ("ІСТОРІЯ ДЛЯ ДІТЕЙ", "HISTORIA DLA DZIECI", "A STORY FOR THE KIDS"),
 "audio": ("АУДІОСЦЕНА", "SCENA AUDIO", "AUDIO SCENE"),
 "speak": ("ГОВОРІННЯ", "MÓWIENIE", "SPEAKING"),
 "gram": ("ГРАМАТИКА СЦЕНИ", "GRAMATYKA SCENY", "SCENE GRAMMAR"),
 "repeat": ("ПОВТОРЕННЯ", "POWTÓRKA", "REVIEW"),
 "gap": ("СЦЕНА З ФІЛЬМУ", "SCENA Z FILMU", "SCENE FROM THE FILM"),
 "final": ("ЛИСТ ДІТЯМ ІЗ МАЙБУТНЬОГО", "LIST DO DZIECI Z PRZYSZŁOŚCI", "A LETTER TO THE KIDS"),
}
INS = {
 "match": ("З'єднай слово з перекладом", "Połącz słowo z tłumaczeniem", "Match each word with its translation"),
 "vocab": ("Обери правильне слово", "Wybierz właściwe słowo", "Choose the right word"),
 "order": ("Склади репліку з частин", "Ułóż kwestię z części", "Build the line from the pieces"),
 "audio": ("Послухай і запиши почуте", "Posłuchaj i zapisz, co słyszysz", "Listen and type what you hear"),
 "speak": ("Прочитай і скажи вголос", "Przeczytaj i powiedz na głos", "Read it and say it aloud"),
 "gram": ("Обери правильну форму", "Wybierz poprawną formę", "Choose the correct form"),
 "gap": ("Встав пропущене слово в репліку", "Wstaw brakujące słowo w kwestię", "Fill the gap in the line"),
 "final": ("Напиши текст", "Napisz tekst", "Write a text"),
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
    import common
    return common.GL

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
                        if gt.get("line") and not gt["line"].startswith("—"): sentences.append((gt["line"], g, it))
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
                d["tip_uk"] = "Переклад: " + (g["uk"]["line"] if T == "pl" else it["line"])
                d["tip_pl"] = "Tłumaczenie: " + (g["pl"]["line"] if T == "uk" else it["line"])
                d["tip_en"] = "Translation: " + it["line"]
                d["tip"] = d["tip_uk"]
                return d
            def mk_audio(sent):
                txt, g, it = sent
                d = {"type": "type", "q": Q[T]["audio"], "say": txt, "options": [txt, re.sub(r"[.!?…]+$", "", txt)]}
                lab(d, "audio"); tri(QT["audio"], "qt", d); d.pop("qt")
                d["tip_uk"] = "Переклад: " + (g["uk"]["line"] if T == "pl" else it["line"])
                d["tip_pl"] = "Tłumaczenie: " + (g["pl"]["line"] if T == "uk" else it["line"])
                d["tip_en"] = "Translation: " + it["line"]; d["tip"] = d["tip_uk"]
                return d
            def mk_speak(sent):
                txt, g, it = sent
                d = {"type": "speaking", "q": Q[T]["speak"], "say": txt}
                lab(d, "speak"); tri(QT["speak"], "qt", d); d.pop("qt")
                d["tip_uk"] = "Переклад: " + (g["uk"]["line"] if T == "pl" else it["line"])
                d["tip_pl"] = "Tłumaczenie: " + (g["pl"]["line"] if T == "uk" else it["line"])
                d["tip_en"] = "Translation: " + it["line"]; d["tip"] = d["tip_uk"]
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
            used = set()
            def add(fn, cands, mn=1, mx=99):
                for s in cands:
                    k = s[0].strip().lower()
                    if k in used or not (mn <= len(s[0].split()) <= mx): continue
                    used.add(k); return fn(s)
                return None
            def mk_gap(sent, pool):
                txt, g, it = sent; w = g[T]["w"]
                m = re.search(r"(?i)(?<!\w)" + re.escape(w) + r"(?!\w)", txt)
                if not m or len(txt.split()) < 3: return None
                same = [x[0] for x in pool if x[0].lower() != w.lower() and x[2].get("pos") == it.get("pos") and x[0].lower() not in txt.lower()]
                other = [x[0] for x in pool if x[0].lower() != w.lower() and x[0].lower() not in txt.lower()]
                src = same if len(set(same)) >= 3 else other
                src = list(dict.fromkeys(src))
                if len(src) < 3: return None
                right = txt[m.start():m.end()]
                opts = [right] + rnd.sample(src, 3); rnd.shuffle(opts)
                d = {"type": "vocabulary", "q": txt[:m.start()] + "____" + txt[m.end():], "options": opts, "answer": opts.index(right)}
                lab(d, "gap")
                tr_uk = g["uk"]["line"] if T == "pl" else it["line"]
                tr_pl = g["pl"]["line"] if T == "uk" else it["line"]
                d["q_uk"] = "Встав слово, якого бракує в репліці. (" + tr_uk + ")"
                d["q_pl"] = "Wstaw brakujące słowo w kwestii. (" + tr_pl + ")"
                d["q_en"] = "Fill in the missing word in the line. (" + it["line"] + ")"
                d["tip"] = it["who"]; d["tip_uk"] = it["who"]; d["tip_pl"] = it.get("who_pl", it["who"]); d["tip_en"] = it.get("who_en", it["who"])
                d["why_uk"] = [("Так! Саме так звучить репліка." if o == right else "Ні — «%s» тут не пасує." % o) for o in opts]
                d["why_pl"] = [("Tak! Tak brzmi ta kwestia." if o == right else "Nie — „%s” tu nie pasuje." % o) for o in opts]
                d["why_en"] = [("Yes! That's the line." if o == right else "No — “%s” doesn't fit here." % o) for o in opts]
                d["why"] = d["why_uk"]
                return d
            def add_gap(cands, pool):
                for s in cands:
                    k = s[0].strip().lower()
                    if k in used: continue
                    d = mk_gap(s, pool)
                    if d: used.add(k); tasks.append(d); return d
                return None
            single = len(sentences) and len(words) >= 8
            scenes = [w for w in words]
            boss = n in (6, 12, 18, 24, 30, 35)
            final = n == 36
            if final:
                pool = [w for w in GLALL[T]]
                picks = rnd.sample(pool, 10)
                tasks += [mk_match(picks[:5]), mk_match(picks[5:10])]
                for w in rnd.sample(pool, 4): tasks.append(mk_vocab(w, pool))
                tasks += [mk_gram(g) for g in gm.G[n]]
                allss = list(SENTALL[T]); rnd.shuffle(allss)
                for _ in range(6):
                    x = add_gap(allss, pool)
                tasks += [x for x in (add(mk_order, allss, 3), add(mk_order, allss, 3), add(mk_order, allss, 3), add(mk_audio, allss), add(mk_speak, allss, 2, 9)) if x]
            elif boss:
                pool = words
                tasks += [mk_match(words[0:5]), mk_match(words[5:10]), mk_match(words[10:15])]
                tasks.append(mk_vocab(rnd.choice(pool[15:] or pool), pool))
                ss = list(sentences); rnd.shuffle(ss)
                add_gap(ss, pool); add_gap(ss, pool)
                tasks += [mk_gram(g) for g in gm.G[n]]
                tasks += [x for x in (add(mk_order, ss, 3), add(mk_audio, ss), add(mk_speak, ss, 2, 9)) if x]
            else:
                per = max(1, len(words) // 3)
                sc = [words[i * per:(i + 1) * per] for i in range(3)]
                ssc = [[s for s in sentences if any(s[2] is w[2] for w in part)] for part in sc]
                for part in ssc: rnd.shuffle(part)
                tasks.append(mk_match(sc[0][:5]))
                if not add_gap(ssc[0], words): tasks.append(mk_vocab(rnd.choice(sc[0][5:] or sc[0]), words))
                x = add(mk_order, ssc[0], 3); x and tasks.append(x)
                tasks.append(mk_gram(gm.G[n][0]))
                tasks.append(mk_match(sc[1][:5]))
                if not add_gap(ssc[1], words): tasks.append(mk_vocab(rnd.choice(sc[1][5:] or sc[1]), words))
                x = add(mk_order, ssc[1], 3); x and tasks.append(x)
                tasks.append(mk_gram(gm.G[n][1]))
                tasks.append(mk_vocab(rnd.choice(sc[2]), words))
                x = add(mk_audio, ssc[2]); x and tasks.append(x)
                add_gap(ssc[2], words)
                x = add(mk_speak, ssc[2], 2, 9) or add(mk_speak, sentences, 2, 9); x and tasks.append(x)
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
                    if g[T].get("line") and not g[T]["line"].startswith("—"): ss.append((g[T]["line"], g, it))
        GLALL[T] = ws; SENTALL[T] = ss; WORDALL[T] = ws
