# Збирає курс міні-курс «Крижане серце» у fz1.json і перевіряє якість.
import json, os, re, sys, importlib, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import common
ARCS = [a for a in ("arc1", "arc2", "arc3", "arc4", "arc5", "arc6") if os.path.exists(os.path.join(HERE, a + ".py"))]
for a in ARCS: importlib.import_module(a)
L = sorted(common.L, key=lambda l: l["num"])
import repeat  # noqa: додає завдання на повторення

for l in L:
    rnd = random.Random(3000 + l["num"])
    for t in l["tasks"]:
        if t["type"] in ("quiz", "grammar", "vocabulary") and len(t["options"]) > 1:
            idx = list(range(len(t["options"]))); rnd.shuffle(idx)
            t["options"] = [t["options"][i] for i in idx]
            if "why" in t: t["why"] = [t["why"][i] for i in idx]
            t["answer"] = idx.index(t["answer"])
        if t["type"] == "quest":
            for st in t["steps"].values(): rnd.shuffle(st["choices"])

INFO = {"intro", "cards", "glossary"}
CYR = re.compile("[а-яіїєґА-ЯІЇЄҐ]")
missing = set()
def tr2(s):
    if s in common.X: return common.X[s]
    missing.add(s[:80]); return (s, s)
def loc(o):
    if isinstance(o, list):
        for v in o: loc(v)
        return
    if not isinstance(o, dict): return
    for k in list(o.keys()):
        v = o[k]
        if k.endswith("_pl") or k.endswith("_en") or k.startswith("options_"): continue
        if isinstance(v, str) and CYR.search(v):
            if k == "uk" and "role" in o: continue
            o[k + "_pl"], o[k + "_en"] = tr2(v)
        elif isinstance(v, list) and v and all(isinstance(x, str) for x in v) and any(CYR.search(x) for x in v):
            o[k + "_pl"] = [tr2(x)[0] if CYR.search(x) else x for x in v]
            o[k + "_en"] = [tr2(x)[1] if CYR.search(x) else x for x in v]
        else: loc(v)
for l in L: loc(l)

import variants, drills
# Боси і фінал: повторення граматики (перше питання з кожного уроку арки)
BOSSES = {6: (1, 2, 3, 4, 5), 12: (7, 8, 9, 10, 11), 18: (13, 14, 15, 16, 17), 24: (19, 20, 21, 22, 23), 30: (25, 26, 27, 28, 29), 35: (31, 32, 33, 34)}
for _m in ("gram_pl", "gram_uk"):
    gm = importlib.import_module(_m)
    for b, src in BOSSES.items():
        if all(i in gm.G for i in src):
            gm.G[b] = [gm.G[i][0] for i in src]
            gm.T[b] = ("Повторення граматики арки", "Powtórka gramatyki łuku", "Arc grammar review")
    reg = [i for i in range(1, 35) if i in gm.G and i not in BOSSES]
    if len(reg) >= 12:
        pick = reg[::max(1, len(reg) // 12)][:12]
        gm.G[36] = [gm.G[i][1] for i in pick]
        gm.T[36] = ("Уся граматика курсу", "Cała gramatyka kursu", "All the course grammar")
variants.prepare(L)
vmiss = variants.build(L, repeat.R, None)
def _words_of(l, T):
    ws = []
    for t in l["tasks"]:
        if t["type"] != "glossary": continue
        for it in t["items"]:
            for w in variants.GLALL[T]:
                if w[2]["w"] == it["w"]: ws.append(w); break
    return ws
drills.apply_en(L)
drills.apply_target(L, "pl", _words_of)
drills.apply_target(L, "uk", _words_of)

def words(s): return len(re.findall(r"[A-Za-z']+", s))
def strings(o):
    if isinstance(o, str): yield o
    elif isinstance(o, dict):
        for v in o.values(): yield from strings(v)
    elif isinstance(o, list):
        for v in o: yield from strings(v)

errs = []
if vmiss: errs.append(f"варіанти: немає перекладу слів: {list(vmiss)[:5]}")
if missing: errs.append(f"без перекладу: {len(missing)} → " + " | ".join(list(missing)[:6]))
for l in L:
    for T in ("pl", "uk"):
        vt = l["variants"].get(T) or []
        sc = [t for t in vt if t["type"] not in INFO]
        if len(sc) < 9: errs.append(f"#{l['num']} {T}: лише {len(sc)} завдань")
        for t in sc:
            for o in (t.get("options") or []) + [t.get("say") or ""]:
                if t["type"] == "match": continue
                if T == "pl" and CYR.search(o): errs.append(f"#{l['num']} pl: кирилиця «{o[:40]}»")
                if T == "uk" and re.search(r"[a-z]{3}", o) and not o.startswith("("): errs.append(f"#{l['num']} uk: латиниця «{o[:40]}»")
for l in L:
    n, ts = l["num"], l["tasks"]
    boss = "Бос" in l["title"] or "іспит" in l["title"].lower()
    scored = [t for t in ts if t["type"] not in INFO]
    gl = sum(len(t["items"]) for t in ts if t["type"] == "glossary")
    labels = {t.get("label", t["type"]) for t in scored}
    if not boss:
        if not 25 <= gl <= 40: errs.append(f"#{n}: словник {gl} (треба 25–40)")
        if not 10 <= len(scored) <= 17: errs.append(f"#{n}: завдань {len(scored)} (треба 10–17)")
        if len(labels) < 7: errs.append(f"#{n}: лише {len(labels)} типів")
        if ts[-1]["type"] != "final": errs.append(f"#{n}: останнє завдання не лист")
        if ts[0]["type"] != "cards": errs.append(f"#{n}: немає карток на початку")
    if "іспит" in l["title"].lower() and len(scored) != 30: errs.append(f"#{n}: в іспиті {len(scored)} завдань (треба 30)")
    if "Бос" in l["title"] and not 36 <= gl <= 60: errs.append(f"#{n}: у босі {gl} слів (треба 36–60)")
    seenw = set()
    for t in ts:
        if t["type"] == "glossary":
            for it in t["items"]:
                if it["w"] in seenw and not boss: errs.append(f"#{n}: слово двічі «{it['w']}»")
                seenw.add(it["w"])
    for i, t in enumerate(ts):
        tag = f"#{n}.{i+1} {t['type']}"
        if t["type"] in ("quiz", "grammar", "vocabulary", "tf"):
            if not 0 <= t["answer"] < len(t["options"]): errs.append(tag + ": answer поза межами")
            if len(t.get("why", [])) != len(t["options"]): errs.append(tag + ": why ≠ options")
            if len(set(t["options"])) != len(t["options"]): errs.append(tag + ": дубль варіанта")
        if t["type"] == "match" and any(o.count("=") != 1 for o in t["options"]): errs.append(tag + ": пара без '='")
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
                if words(q) > 12: errs.append(tag + f": цитата >12 слів «{q[:50]}»")

json.dump(L, open(os.path.join(HERE, "fz1.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print("уроків:", len(L), "| арки:", ARCS)
for l in L:
    ts = l["tasks"]; sc = [t for t in ts if t["type"] not in INFO]
    vp = len([t for t in l["variants"]["pl"] if t["type"] not in INFO]); vu = len([t for t in l["variants"]["uk"] if t["type"] not in INFO])
    print(f"  {l['num']:>2}. pl {vp:>2} · uk {vu:>2} · {l['title'][:30]:<30} словник {sum(len(t['items']) for t in ts if t['type']=='glossary'):>2} · завдань {len(sc):>2} · типів {len({t.get('label') for t in sc})}")
print("\n".join(errs[:60]) if errs else "✓ помилок немає")
sys.exit(1 if errs else 0)
