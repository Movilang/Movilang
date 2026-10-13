# Інтервальне повторення: у кожному звичайному уроці — пари зі слів, що з'являлися 2–4 уроки тому.
# Визначення беремо з уже написаних завдань «Слово з Дірявого Казана» (match).
import random
from common import L, cauldron, BOSS, FINAL

def _defs():
    D, where = {}, {}
    for l in L:
        gl = {it["w"] for t in l["tasks"] if t["type"] == "glossary" for it in t["items"]}
        for t in l["tasks"]:
            if t["type"] == "match" and t.get("label") == "СЛОВО З ДІРЯВОГО КАЗАНА":
                for o in t["options"]:
                    w, d = o.split("=", 1)
                    if w in gl and w not in D: D[w] = d; where[w] = l["num"]
    return D, where

D, WHERE = _defs()
R = {}
for l in L:
    n = l["num"]
    if n in BOSS or n == FINAL or n < 3: continue
    cand = [w for w, k in WHERE.items() if n - 4 <= k <= n - 2 and k not in BOSS]
    if len(cand) < 5: cand = [w for w, k in WHERE.items() if k < n and k not in BOSS]
    rnd = random.Random(500 + n)
    ws = rnd.sample(sorted(cand), 5)
    R[n] = ws
    t = cauldron([(w, D[w]) for w in ws], "Інтервальне повторення: ці слова ти вже зустрічав(ла) кілька уроків тому.",
                 q="Do you still remember these words?")
    t["label"] = "ПОВТОРЕННЯ"
    t["ins"] = "Згадай значення слів з попередніх уроків"
    l["tasks"].insert(len(l["tasks"]) - 1, t)
