# Збирає курс «Гаррі Поттер і філософський камінь» в hp.json і перевіряє якість (самоперевірка з промту).
import json, os, re, sys, importlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import common
ARCS = [a for a in ("arc1", "arc2", "arc3", "arc4", "arc5", "arc6", "final") if os.path.exists(os.path.join(HERE, a + ".py"))]
for a in ARCS: importlib.import_module(a)
import repeat
L = sorted(common.L, key=lambda l: l["num"])

# Перемішуємо варіанти (детерміновано), щоб правильна відповідь не була завжди першою
import random
for l in L:
    rnd = random.Random(1000 + l["num"])
    for t in l["tasks"]:
        if t["type"] in ("quiz", "grammar", "vocabulary", "listening") and len(t["options"]) > 1:
            idx = list(range(len(t["options"]))); rnd.shuffle(idx)
            t["options"] = [t["options"][i] for i in idx]
            if "why" in t: t["why"] = [t["why"][i] for i in idx]
            t["answer"] = idx.index(t["answer"])
        if t["type"] == "quest":
            for st in t["steps"].values():
                rnd.shuffle(st["choices"])

INFO = {"intro", "cards", "glossary"}
# Спойлери: слово/ім'я не може з'являтися раніше вказаного уроку (наскрізна нумерація 1–36)
SPOIL = {r"Flamel|Фламел": 24, r"Elixir of Life|еліксир\w* життя": 24, r"Norbert|Норберт": 25, r"dragon egg|яйц\w* дракона": 25,
         r"Erised|Еїналеж": 22, r"invisibility cloak|манті\w*-невидимк": 21, r"Fluffy|Пушок|Пушк|three-headed|триголов": 16,
         r"Devil's Snare|сильц": 30, r"unicorn|єдиноро": 27, r"Firenze|Фіренце|centaur|кентавр": 27,
         r"back of (his|the) head|потилиц": 32, r"Quirrell.{0,40}(Voldemort|serves|lied)|Квірел.{0,40}(Волдеморт|служ|бреш)": 32,
         r"Snape.{0,40}(protect|sav)|Снейп.{0,40}(захищ|рятува)": 32, r"Seeker|ловц|ловець|ловця": 15, r"Nimbus|Німбус": 16}
NAMES_BAD = [r"Хогвартс", r"Гогвортс", r"Гермиона", r"Грейнджер", r"Хагрід", r"Гагрід", r"Хаґрід", r"Гегрід", r"Малфой", r"Макгонагал", r"Макґонагал",
             r"Макгонеґел", r"Квіррел", r"Грифіндор", r"Слізерин", r"Квідіч", r"Гринготс", r"Ґринґотс", r"Візлі", r"Гедвіга", r"Дамбладор", r"Петуния", r"Олливандер"]

def words(s): return len(re.findall(r"[A-Za-z']+", s))
def strings(o):
    if isinstance(o, str): yield o
    elif isinstance(o, dict):
        for v in o.values(): yield from strings(v)
    elif isinstance(o, list):
        for v in o: yield from strings(v)

# ---- Переклади пояснень (PL / EN) з i18n/*.tsv
SRC = {}
for line in open(os.path.join(HERE, "i18n", "src.txt"), encoding="utf-8"):
    i, t = line.rstrip("\n").split("\t", 1); SRC[t] = int(i)
TR = {}
for f in sorted(os.listdir(os.path.join(HERE, "i18n"))):
    if not (f.startswith("t0") and f.endswith(".tsv")): continue
    for line in open(os.path.join(HERE, "i18n", f), encoding="utf-8"):
        if not line.strip(): continue
        i, pl, en = line.rstrip("\n").split("\t")
        TR[int(i)] = (pl, en)
CYR = re.compile("[а-яіїєґА-ЯІЇЄҐ]")
missing = set()
def tr2(s):
    i = SRC.get(s)
    if i is None or i not in TR: missing.add(s[:70]); return (s, s)
    return TR[i]
def loc(o):
    if isinstance(o, list):
        for v in o: loc(v)
        return
    if not isinstance(o, dict): return
    for k in list(o.keys()):
        v = o[k]
        if k.endswith("_pl") or k.endswith("_en"): continue
        if isinstance(v, str) and CYR.search(v):
            if k == "uk" and "role" in o: continue
            o[k + "_pl"], o[k + "_en"] = tr2(v)
        elif isinstance(v, list) and v and all(isinstance(x, str) for x in v) and any(CYR.search(x) for x in v):
            o[k + "_pl"] = [tr2(x)[0] if CYR.search(x) else x for x in v]
            o[k + "_en"] = [tr2(x)[1] if CYR.search(x) else x for x in v]
        else: loc(v)
for l in L: loc(l)
for l in L:
    for k in ("pl", "en"):
        if l.get("grammar_" + k): l["variants"]["grammar_" + k] = l.pop("grammar_" + k)

import variants, drills
ONLY_EN = "--en" in sys.argv
if ONLY_EN:
    drills.apply_en(L) if os.path.exists(os.path.join(HERE, "drills_en.py")) else None
    for l in L: l["variants"].setdefault("pl", []); l["variants"].setdefault("uk", [])
variants.prepare(L) if not ONLY_EN else None
vmiss = variants.build(L, repeat.R, None) if not ONLY_EN else None
def _words_of(l, T):
    ws = []
    for t in l["tasks"]:
        if t["type"] != "glossary": continue
        for it in t["items"]:
            for w in variants.GLALL[T]:
                if w[2]["w"] == it["w"]: ws.append(w); break
    return ws
if not ONLY_EN:
    drills.apply_en(L)
    drills.apply_target(L, "pl", _words_of)
    drills.apply_target(L, "uk", _words_of)

errs, warns = [], []
if vmiss: errs.append(f"варіанти: немає перекладу слів: {list(vmiss)[:5]}")
LAT = re.compile(r"[a-ząćęłńóśźż]", re.I)
for l in L:
    for T in ("pl", "uk"):
        vt = l["variants"].get(T) or []
        sc = [t for t in vt if t["type"] not in INFO]
        if ONLY_EN: continue
        if len(sc) < 9: errs.append(f"#{l['num']} {T}: лише {len(sc)} завдань")
        for t in sc:
            for o in (t.get("options") or []) + [t.get("say") or ""]:
                if t["type"] == "match": continue
                if T == "pl" and CYR.search(o): errs.append(f"#{l['num']} pl: кирилиця у варіанті «{o[:40]}»")
                if T == "uk" and t["type"] != "match" and re.search(r"[a-z]{3}", o) and not o.startswith("("): errs.append(f"#{l['num']} uk: латиниця «{o[:40]}»")
            if t["type"] in ("vocabulary", "grammar") and len(t.get("why_en", [])) != len(t["options"]): errs.append(f"#{l['num']} {T}: why")
if missing and not ONLY_EN: errs.append(f"без перекладу: {len(missing)} → " + " | ".join(list(missing)[:5]))
for l in L:
    n, ts = l["num"], l["tasks"]
    boss = "Бос" in l["title"] or "іспит" in l["title"].lower()
    scored = [t for t in ts if t["type"] not in INFO]
    gl = sum(len(t["items"]) for t in ts if t["type"] == "glossary")
    labels = {t.get("label", t["type"]) for t in scored}
    if not boss:
        if not 25 <= gl <= 30: errs.append(f"#{n}: словник {gl} (треба 25–30)")
        if not 12 <= len(scored) <= 15: errs.append(f"#{n}: завдань {len(scored)} (треба 12–15 з тренуваннями, урок 10–15 хв)")
        if len(labels) < 6: errs.append(f"#{n}: лише {len(labels)} типів")
        if ts[-1]["type"] != "final": errs.append(f"#{n}: останнє завдання не «Лист совою»")
        if ts[0]["type"] != "cards": errs.append(f"#{n}: немає карток/переказу на початку")
    for i, t in enumerate(ts):
        tag = f"#{n}.{i+1} {t['type']}"
        if t["type"] in ("quiz", "grammar", "vocabulary", "tf", "listening"):
            if not 0 <= t["answer"] < len(t["options"]): errs.append(tag + ": answer поза межами")
            if len(t.get("why", [])) != len(t["options"]): errs.append(tag + ": why ≠ options")
            if len(set(t["options"])) != len(t["options"]): errs.append(tag + ": дубль варіанта")
        if t["type"] == "match":
            if any(o.count("=") != 1 for o in t["options"]): errs.append(tag + ": пара без '='")
        if t["type"] == "type" and not t["options"]: errs.append(tag + ": немає відповідей")
        if t["type"] == "glossary":
            for it in t["items"]:
                if not all(it.values()): errs.append(tag + f": порожнє поле у «{it['w']}»")
                if words(it["line"]) > 10: errs.append(tag + f": репліка >10 слів «{it['line']}»")
        if t["type"] == "quest":
            ids = set(t["steps"]) | set(t["endings"])
            for k, st in t["steps"].items():
                for c in st["choices"]:
                    if c["next"] not in ids: errs.append(tag + f": квест {k} → {c['next']} не існує")
            if not any(e["good"] for e in t["endings"].values()): errs.append(tag + ": немає доброї кінцівки")
        for s in strings(t):
            for q in re.findall(r"“([^”]+)”", s):
                if words(q) > 10: errs.append(tag + f": цитата >10 слів «{q}»")
    if "іспит" in l["title"].lower() and len(scored) != 30: errs.append(f"#{n}: в іспиті {len(scored)} завдань (треба 30)")
    if boss and "Бос" in l["title"] and not 40 <= gl <= 60: errs.append(f"#{n}: у босі повторюється {gl} слів (треба 40–60)")
    for s in list(strings(l)):
        if s in ("ДЗЕРКАЛО ПРАВДИ", "LUSTRO PRAWDY", "MIRROR OF TRUTH"): continue
        for pat, first in SPOIL.items():
            if n < first and re.search(pat, s, re.I): errs.append(f"#{n}: спойлер /{pat}/ (дозволено з #{first}) → {s[:60]}")
        for pat in NAMES_BAD:
            if re.search(pat, s): errs.append(f"#{n}: глосарій — «{pat}» → {s[:60]}")

# Курс B1: слова B2 позначаємо як «B1+» (верхній B1), терміни світу ГП — «HP»
for l in L:
    for ts in [l["tasks"], l["variants"].get("pl") or [], l["variants"].get("uk") or []]:
        for t in ts:
            if t.get("type") == "glossary":
                for it in t["items"]:
                    if it.get("lvl") == "B2": it["lvl"] = "B1+"
json.dump(L, open(os.path.join(HERE, "hp.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print("уроків:", len(L), "| арки:", ARCS)
for l in L:
    ts = l["tasks"]; sc = [t for t in ts if t["type"] not in INFO]
    vp = len([t for t in l["variants"]["pl"] if t["type"] not in INFO]); vu = len([t for t in l["variants"]["uk"] if t["type"] not in INFO])
    print(f"  {l['num']:>2}. pl {vp:>2} · uk {vu:>2} · {l['title'][:30]:<30} словник {sum(len(t['items']) for t in ts if t['type']=='glossary'):>2} · завдань {len(sc):>2} · типів {len({t.get('label') for t in sc})}")
print("\n".join(errs) if errs else "✓ помилок немає")
sys.exit(1 if errs else 0)
