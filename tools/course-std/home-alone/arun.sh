export CSLUG=home-alone CIMG=stairs CWORDS=40
for f in "$@"; do python3 $f >/dev/null || exit 1; done
python3 validate.py /home/claude/movilang/content/std/home-alone/*.json 2>&1 | grep -B1 -E "BŁĄD|uwaga" | head -30
