export CSLUG=himym-s1 CIMG=ring CWORDS=70
for f in "$@"; do python3 $f >/dev/null || exit 1; done
python3 validate.py /home/claude/movilang/content/std/himym-s1/*.json 2>&1 | grep -B1 -E "BŁĄD|uwaga" | head -30
