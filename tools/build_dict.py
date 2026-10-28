# Будує content/dict.json — словник для «натисни на слово» з глосаріїв усіх курсів.
# Запуск: python3 tools/build_dict.py   (після збирання курсів)
import json, glob, re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = {"en": {}, "pl": {}, "uk": {}}
def clean(s):
    s = re.sub(r"\([^)]*\)", "", str(s or "")).strip()
    return re.split(r"\s*[,;/]\s*", s)[0].strip(" .!?…—-") if s else ""
def full(s):
    return re.sub(r"\s+", " ", str(s or "")).strip()
def put(lang, key, tr):
    key = full(key).lower().strip(" .!?…")
    if not key or len(key) > 40: return
    keys = {key}
    if lang == "en" and key.startswith("to "): keys.add(key[3:])
    if lang == "pl" and key.endswith(" się"): keys.add(key[:-4])
    if lang == "uk" and key.endswith("ся") and " " not in key: pass
    for k in keys:
        cur = D[lang].setdefault(k, {})
        for l, v in tr.items():
            if v and l != lang and l not in cur: cur[l] = full(v)
files = [f for f in glob.glob(os.path.join(ROOT, "content", "**", "*.json"), recursive=True) if not re.search(r"defs_|dict\.json", f)]
n = 0
for f in files:
    try: ls = json.load(open(f))
    except Exception: continue
    if not isinstance(ls, list): continue
    for l in ls:
        sets = [("en", l.get("tasks") or [])] + [(k, (l.get("variants") or {}).get(k) or []) for k in ("pl", "uk")]
        for T, ts in sets:
            if not isinstance(ts, list): continue
            for t in ts:
                if not isinstance(t, dict) or t.get("type") != "glossary": continue
                for it in t.get("items") or []:
                    w = it.get("w")
                    if not w: continue
                    if T == "en": tr = {"uk": it.get("uk"), "pl": it.get("uk_pl")}
                    elif T == "pl": tr = {"uk": it.get("uk_uk") or it.get("uk"), "en": it.get("uk_en")}
                    else: tr = {"en": it.get("uk_en"), "pl": it.get("uk_pl")}
                    put(T, w, tr); n += 1
out = os.path.join(ROOT, "content", "dict.json")
json.dump(D, open(out, "w"), ensure_ascii=False, separators=(",", ":"))
print("items", n, "keys", {k: len(v) for k, v in D.items()}, "KB", os.path.getsize(out) // 1024)
