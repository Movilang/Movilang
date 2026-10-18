# Інтервальне повторення: у кожному звичайному уроці — 5 слів з уроку, що був 2–3 уроки тому.
import random
from common import L, u

BOSSES = {6, 12, 18, 24, 30, 35, 36}
BYNUM = {l["num"]: l for l in L}
R = {}

def words(n):
    l = BYNUM.get(n)
    if not l: return []
    return [it for t in l["tasks"] if t["type"] == "glossary" for it in t["items"]]

for l in L:
    n = l["num"]
    if n in BOSSES or n < 3: continue
    src = n - 2
    while src in BOSSES and src > 1: src -= 1
    pool = words(src)
    if len(pool) < 5: continue
    pick = random.Random(500 + n).sample(pool, 5)
    R[n] = [it["w"] for it in pick]
    import common
    t = {"type": "match", "label": u(("ПОВТОРЕННЯ", "POWTÓRKA", "REVIEW")),
         "ins": u(("З'єднай слово з перекладом", "Połącz słowo z tłumaczeniem", "Match each word with its meaning")),
         "q": "Do you still remember these words?",
         "tip": u(("Інтервальне повторення: ці слова були 2–3 уроки тому.", "Powtórka z odstępami: te słowa były 2–3 lekcje temu.", "Spaced review: you met these words 2–3 lessons ago."))}
    t["options_uk"] = ["%s=%s" % (it["w"], it["uk"].split(",")[0].split("(")[0].strip()) for it in pick]
    t["options_pl"] = ["%s=%s" % (it["w"], common.X[it["uk"]][0].split(",")[0].split("(")[0].strip()) for it in pick]
    t["options_en"] = ["%s=%s" % (it["w"], it["line"]) for it in pick]
    t["options"] = t["options_en"]
    l["tasks"].insert(len(l["tasks"]) - 1, t)
