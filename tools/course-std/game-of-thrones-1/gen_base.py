# Базовий курс «Гра престолів»: картки героїв + 3 словники сцен з кожної специфікації gNN.py.
# Результат: content/got/got1.json (36 уроків, у тому ж форматі, що й інші курси).
import json, os, re, sys, glob, importlib.util, types
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
IDS = [l.strip() for l in open(os.path.join(HERE, '..', 'game-of-thrones-1_ids.txt')) if l.strip()]
M = re.compile(r'\[([^\]]+)\]')
I = {'uk': 0, 'pl': 1, 'en': 2}
ARCS = {1: ('Арка 1 · Зима близько|Łuk 1 · Zima nadchodzi|Arc 1 · Winter Is Coming', '🐺', 'Вовченя Старків|Szczenię Starków|The Stark Pup', 'Ти зустрів(ла) родину Старків і почув(ла) перші новини з півдня.|Poznałeś(-aś) Starków i usłyszałeś(-aś) pierwsze wieści z południa.|You met the Starks and heard the first news from the south.'),
        2: ('Арка 2 · Королівський тракт|Łuk 2 · Królewski Trakt|Arc 2 · The Kingsroad', '🗡', 'Валірійський кинджал|Valyriański sztylet|The Valyrian Dagger', 'Ти пройшов(ла) Королівським трактом до столиці.|Przeszedłeś(-aś) Królewskim Traktem do stolicy.|You travelled the Kingsroad to the capital.'),
        3: ('Арка 3 · Інтриги столиці|Łuk 3 · Intrygi stolicy|Arc 3 · Court Intrigue', '🕷', 'Павутина Павука|Sieć Pająka|The Spider\'s Web', 'Ти навчився(лася) слухати шепіт Королівської Гавані.|Nauczyłeś(-aś) się słuchać szeptów Królewskiej Przystani.|You learned to listen to the whispers of King\'s Landing.'),
        4: ('Арка 4 · Вовк і лев|Łuk 4 · Wilk i lew|Arc 4 · The Wolf and the Lion', '🦁', 'Ланністерський золотий|Złota moneta Lannisterów|A Lannister Gold Dragon', 'Ти пережив(ла) сутичку Старків і Ланністерів.|Przetrwałeś(-aś) starcie Starków z Lannisterami.|You survived the clash of Starks and Lannisters.'),
        5: ('Арка 5 · Гра престолів|Łuk 5 · Gra o tron|Arc 5 · The Game of Thrones', '👑', 'Зламана корона|Złamana korona|The Broken Crown', 'Ти побачив(ла), як у грі престолів виграють або помирають.|Zobaczyłeś(-aś), że w grze o tron się wygrywa albo umiera.|You saw that in the game of thrones you win or you die.'),
        6: ('Арка 6 · Вогонь і кров|Łuk 6 · Ogień i krew|Arc 6 · Fire and Blood', '🐉', 'Драконяче яйце|Smocze jajo|The Dragon Egg', 'Ти дійшов(ла) до кінця першого сезону.|Doszedłeś(-aś) do końca pierwszego sezonu.|You reached the end of the first season.')}

def sp(t): a = [x.strip() for x in t.split('|')]; assert len(a) == 3, t; return a
def clean(s): return M.sub(lambda m: m.group(1).split('/')[0], s)

captured = {}
fake = types.ModuleType('tri')
def _build(num, d, tgs, boss=False): captured[num] = (d, boss)
fake.build = _build; sys.modules['tri'] = fake
for f in sorted(glob.glob(os.path.join(HERE, 'g[0-9][0-9].py'))):
    spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

UI = {'uk': ('Відкривай слова, слухай вимову 🔊 і читай, хто і де це каже.', 'Otwieraj słowa, słuchaj wymowy 🔊 i czytaj, kto i gdzie to mówi.', 'Open the words, listen to the pronunciation 🔊 and read who says it and where.')}

def glossary(tg, n, lab, voc, sents):
    k = I[tg]; L = sp(lab); items = []
    for v in voc.split(';'):
        a = sp(v); w = a[k]
        idx = None
        for kk in (2, k):  # спершу англійська (стабільні основи слів), потім мова уроку
            stem = re.sub(r'^to ', '', a[kk].lower())[:4]
            br = lambda s: [x.split('/')[0].lower() for x in M.findall(sp(s)[kk])]
            idx = next((i for i, s in enumerate(sents) if any(b.startswith(stem) for b in br(s))), None)
            if idx is None: idx = next((i for i, s in enumerate(sents) if stem in clean(sp(s)[kk]).lower()), None)
            if idx is not None: break
        line = sents[idx or 0]
        ls = sp(line); full = [clean(x) for x in ls]
        it = {'w': w, 'ipa': '', 'pos': '', 'lvl': 'B2', 'line': full[k], 'ex': full[k],
              'who': full[0], 'who_pl': full[1], 'who_en': full[2]}
        if tg == 'en':
            it.update({'uk': a[0], 'uk_pl': a[1], 'uk_en': a[2]})
        else:
            it.update({'uk': a[0] if tg != 'uk' else a[2], 'uk_uk': a[0], 'uk_pl': a[1], 'uk_en': a[2]})
        items.append(it)
    return {'type': 'glossary', 'label': 'Сцена %d · %s' % (n, L[0]), 'label_pl': 'Scena %d · %s' % (n, L[1]), 'label_en': 'Scene %d · %s' % (n, L[2]),
            'q': UI['uk'][0], 'q_pl': UI['uk'][1], 'q_en': UI['uk'][2], 'items': items}

def cards(d):
    p = sp(d['prev'])
    cs = [{'uk': a, 'en': b, 'role': sp(r)[0], 'role_pl': sp(r)[1], 'role_en': sp(r)[2]} for a, b, r in d['cards']]
    return {'type': 'cards', 'label': 'Раніше у Вестеросі…', 'label_pl': 'Wcześniej w Westeros…', 'label_en': 'Previously in Westeros…',
            'q': p[0], 'q_pl': p[1], 'q_en': p[2], 'img': None, 'cards': cs}

def arc_of(n): return min(6, (n - 1) // 6 + 1)

out = []
for n in range(1, 37):
    if n not in captured: continue
    d, boss = captured[n]
    t, s = sp(d['title']), sp(d['scene'])
    base = {'num': n, 'id': IDS[n - 1], 'title': t[0], 'title_pl': t[1], 'title_en': t[2], 'scene': s[0], 'scene_pl': s[1], 'scene_en': s[2],
            'grammar': sp(d['gname']['en'])[2]}
    per = {}
    for tg in ('en', 'pl', 'uk'):
        per[tg] = [cards(d)] + [glossary(tg, i + 1, lab, voc, sents) for i, (lab, voc, sents) in enumerate(d['sc'])]
    base['tasks'] = per['en']
    a = ARCS[arc_of(n)]; ar = sp(a[0]); bn = sp(a[2]); bt = sp(a[3])
    v = {'arc': ar[0], 'arc_pl': ar[1], 'arc_en': ar[2], 'badge': {'icon': a[1], 'name': bn[0], 'name_pl': bn[1], 'name_en': bn[2], 'text': bt[0], 'text_pl': bt[1], 'text_en': bt[2]},
         'pl': per['pl'], 'uk': per['uk']}
    for tg in ('pl', 'uk'):
        g = sp(d['gname'][tg]); v[tg + '_grammar'] = g[1] if tg == 'pl' else g[0]
        v[tg + '_grammar_uk'], v[tg + '_grammar_pl'], v[tg + '_grammar_en'] = g
    base['variants'] = v
    out.append(base)
os.makedirs(os.path.join(ROOT, 'content', 'got'), exist_ok=True)
json.dump(out, open(os.path.join(ROOT, 'content', 'got', 'got1.json'), 'w'), ensure_ascii=False)
print(len(out), 'lessons ->', os.path.join(ROOT, 'content', 'got', 'got1.json'))
