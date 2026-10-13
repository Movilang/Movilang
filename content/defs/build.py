# Builds content/defs_pl.json and content/defs_uk.json (monolingual definitions shown when
# the target language equals the hint language) from the pl_*.txt / uk_*.txt files ("word|definition").
import json, glob, os
H = os.path.dirname(os.path.abspath(__file__))
for lang in ("pl", "uk"):
    D = {}
    for f in sorted(glob.glob(os.path.join(H, lang + "_*.txt"))):
        for line in open(f, encoding="utf-8"):
            line = line.rstrip("\n")
            if "|" in line and not line.startswith("#"):
                k, v = line.split("|", 1); D[k.strip()] = v.strip()
    json.dump(D, open(os.path.join(os.path.dirname(H), "defs_%s.json" % lang), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    print(lang, len(D))
