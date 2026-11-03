export CSLUG=friends-s1 CIMG=letter CWORDS=50
for f in "$@"; do python3 $f >/dev/null || exit 1; done
python3 validate.py /home/claude/movilang/content/std/friends-s1/*.json 2>&1 | grep -B1 -E "BŁĄD|uwaga" | head -30
