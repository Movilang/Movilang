export CMODE=b CSLUG=harry-potter-1 CIMG=castle CWORDS=60
for f in "$@"; do python3 $f >/dev/null || exit 1; done
python3 validate.py /home/claude/movilang/content/std/harry-potter-1/*.json 2>&1 | grep -B1 -E "BŁĄD|uwaga" | head -30
