# Adds question translations (qt_en / qt_uk / qt_pl) to every task in hp1.json, from qtr.txt.
import json, os
H = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(H, "hp1.json"), encoding="utf-8"))
seen, order = {}, []
for l in d:
    for src, tasks in (("en", l["tasks"]), ("pl", l["variants"]["pl"]), ("uk", l["variants"]["uk"])):
        for t in tasks:
            if t["type"] == "intro" or t["q"] in seen: continue
            seen[t["q"]] = len(order); order.append(src)
tr = {}
for line in open(os.path.join(H, "qtr.txt"), encoding="utf-8"):
    if not line.strip() or line.startswith("#"): continue
    i, a, b = line.rstrip("\n").split("|")
    tr[int(i)] = (a, b)
OTHER = {"en": ("uk", "pl"), "pl": ("en", "uk"), "uk": ("en", "pl")}
miss = 0
for l in d:
    for src, tasks in (("en", l["tasks"]), ("pl", l["variants"]["pl"]), ("uk", l["variants"]["uk"])):
        for t in tasks:
            if t["type"] == "intro": continue
            i = seen[t["q"]]
            if i not in tr: miss += 1; continue
            a, b = OTHER[src]
            t["qt_" + a], t["qt_" + b] = tr[i]
json.dump(d, open(os.path.join(H, "hp1.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok, missing", miss, "of", len(order))
