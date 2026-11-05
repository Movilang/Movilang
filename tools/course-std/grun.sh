export CMODE=b CSLUG=game-of-thrones-1 CIMG=crow CWORDS=90
for f in "$@"; do python3 $f >/dev/null || exit 1; done
python3 validate.py /home/claude/movilang/content/std/game-of-thrones-1/*.json 2>&1 | grep -B1 -E "BŁĄD|uwaga" | head -30
