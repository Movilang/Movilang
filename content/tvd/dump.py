# Вивантажує всі українські рядки курсу в i18n/src.txt (id \t text), зберігаючи наявні id.
import os, re, sys, importlib, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import common
for a in ("arc1", "arc2", "arc3", "arc4", "arc5", "extra"): importlib.import_module(a)
import repeat
CYR = re.compile("[а-яіїєґА-ЯІЇЄҐ]")
seen, order = set(), []
def add(s):
    if s not in seen: seen.add(s); order.append(s)
def walk(o):
    if isinstance(o, list):
        for v in o: walk(v)
        return
    if not isinstance(o, dict): return
    for k, v in o.items():
        if k.endswith("_pl") or k.endswith("_en"): continue
        if isinstance(v, str) and CYR.search(v):
            if k == "uk" and "role" in o: continue
            add(v)
        elif isinstance(v, list) and v and all(isinstance(x, str) for x in v):
            for x in v:
                if CYR.search(x): add(x)
        else: walk(v)
for l in sorted(common.L, key=lambda l: l["num"]): walk(l)
p = os.path.join(HERE, "i18n", "src.txt")
old = {}
if os.path.exists(p):
    for line in open(p, encoding="utf-8"):
        if line.strip():
            i, t = line.rstrip("\n").split("\t", 1); old[t] = int(i)
nxt = max(old.values(), default=-1) + 1
for s in order:
    if s not in old: old[s] = nxt; nxt += 1
with open(p, "w", encoding="utf-8") as f:
    for t, i in sorted(old.items(), key=lambda x: x[1]): f.write(f"{i}\t{t.replace(chr(10), ' ')}\n")
# список нерозкладених (без перекладу)
TR = set()
for fn in os.listdir(os.path.join(HERE, "i18n")):
    if fn.startswith("t0") and fn.endswith(".tsv"):
        for line in open(os.path.join(HERE, "i18n", fn), encoding="utf-8"):
            if line.strip(): TR.add(int(line.split("\t", 1)[0]))
todo = [i for t, i in old.items() if t in seen and i not in TR]
print("рядків:", len(seen), "без перекладу:", len(todo), "діапазон:", min(todo, default=None), max(todo, default=None))
