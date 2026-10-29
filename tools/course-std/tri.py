# Generator trójjęzyczny: jedna specyfikacja -> lekcje uk/pl/en.
import re, random, sys
sys.path.insert(0, '/home/claude/work/std'); from lib import *
IDS = [l.strip().split(':')[-1] for l in open('/home/claude/work/std/cars_ids.txt') if l.strip()]
I = {'uk': 0, 'pl': 1, 'en': 2}
M = re.compile(r'\[([^\]]+)\]')

def sp(t): a = [x.strip() for x in t.split('|')]; assert len(a) == 3, t; return a
def clean(s): return M.sub(lambda m: m.group(1).split('/')[0], s)
def hint(tri, tg):
    h = [clean(x) for x in tri]; h[I[tg]] = h[2] if tg != 'en' else h[0]; return '|'.join(h)

def gapitem(tri, tg, pool, rnd, tag='line'):
    a = sp(tri); s = a[I[tg]]; m = M.search(s)
    if not m: return None
    ops = m.group(1).split('/')
    if len(ops) == 1:
        c = list({w.lower(): w for w in pool if w.lower() != ops[0].lower()}.values()); rnd.shuffle(c); ops = ops + c[:2]
    q = s[:m.start()] + '____' + s[m.end():]; q = clean(q)
    full = clean(s); h = hint(a, tg).split('|')
    o = ops[:]; rnd.shuffle(o)
    return mc(q, o, o.index(ops[0]), '%s — %s|%s — %s|%s — %s' % (full, h[0], full, h[1], full, h[2]), '|'.join(h), tag)

def build(num, d, tgs, boss=False):
    lid = IDS[num - 1]
    for tg in tgs:
        rnd = random.Random(num * 7 + I[tg]); L = Lesson(lid, tg); k = I[tg]
        allm = [x for sc in d['sc'] for x in sc[2]] + d['read']
        pool = list(dict.fromkeys(m.split('/')[0] for t in allm for m in M.findall(sp(t)[k]) if '/' not in m))
        if not boss: L.ref(0)
        L.intro('ТВОЯ РОЛЬ|TWOJA ROLA|YOUR ROLE', d['role'])
        for n, (lab, voc, sents) in enumerate(d['sc']):
            if not boss: L.ref(n + 1)
            pr = []
            for v in voc.split(';'):
                a = sp(v); pr.append(a[k] + '=' + '/'.join(a))
            L.match('СЦЕНА %d · СЛОВА|SCENA %d · SŁOWA|SCENE %d · WORDS' % (n + 1, n + 1, n + 1), pr)
            its = [gapitem(t, tg, pool, rnd) for t in sents]
            l3 = sp(lab)
            L.set('СЦЕНА %d · %s|SCENA %d · %s|SCENE %d · %s' % (n + 1, l3[0].upper(), n + 1, l3[1].upper(), n + 1, l3[2].upper()),
                  d['where'], 'Встав слово в репліку|Wstaw słowo do kwestii|Put the word into the line', [x for x in its if x])
        r = d['rule'][tg]; L.intro('ПРАВИЛО|ZASADA|RULE', r + '|' + r + '|' + r)
        L.set('ГРАМАТИКА|GRAMATYKA|GRAMMAR', d['where'], 'Обери правильну форму|Wybierz poprawną formę|Choose the correct form',
              [gapitem(t, tg, pool, rnd, 'gram') for t in d['gram']])
        rs = []
        for t in d['read']:
            a = sp(t); s = a[k]; m = M.search(s)
            if not m: rs.append(S(s)); continue
            g = gapitem(t, tg, pool, rnd); rs.append(S(g['q'], g['options'], g['answer']))
        L.reading(d['rt'], 'ЧИТАННЯ|CZYTANIE|READING', 'Прочитай текст і обери слова.|Przeczytaj tekst i wybierz słowa.|Read the text and choose the words.', rs,
                  'Читай усе речення, не лише пропуск.|Czytaj całe zdanie, nie tylko lukę.|Read the whole sentence, not just the gap.')
        cs = []
        for q, opts in d['chk']:
            o = [sp(x)[k] for x in opts]; c = o[0]; rnd.shuffle(o); qa = sp(q)
            cs.append(mc(qa[k], o, o.index(c), c + '|' + c + '|' + c, hint(qa, tg)))
        L.set('РОЗУМІННЯ ТЕКСТУ|ROZUMIENIE TEKSTU|READING CHECK', 'Питання до тексту.|Pytania do tekstu.|Questions about the text.', 'П\'ять питань|Pięć pytań|Five questions', cs)
        st = {}; qs = d['quest']
        for n, (line, good, bad) in enumerate(qs):
            la, ga, ba = sp(line), sp(good), sp(bad); nx = 's%d' % (n + 2) if n < len(qs) - 1 else 'end_good'
            c = [ch(ga[k], True, nx, 'Так!|Tak!|Yes!'), ch(ba[k], False, nx if n < len(qs) - 1 else 'end_bad', 'Краще: %s|Lepiej: %s|Better: %s' % (ga[k], ga[k], ga[k]))]
            if n % 2: c.reverse()
            h = hint(la, tg).split('|'); st['s%d' % (n + 1)] = step(la[k], '|'.join(h), d['where'], c)
        L.quest('КВЕСТ|QUEST|QUEST', d['qq'], 'alley', st, {'end_good': end(True, 'Місію виконано!|Misja wykonana!|Mission complete!', d['qend']),
                 'end_bad': end(False, 'Спробуй ще|Spróbuj jeszcze|Try again', 'Майже! Пройди квест ще раз.|Prawie! Przejdź quest jeszcze raz.|Almost! Play the quest again.')})
        ss = [sp(t) for sc in d['sc'] for t in sc[2]] + [sp(t) for t in d['read'][:6]]
        ws = []
        sh = sorted(ss, key=lambda a: len(clean(a[k])))
        for a in sh[:4]: ws.append(typ(tg, clean(a[k]), hint(a, tg)))
        for a in [x for x in sh[4:] if 3 <= len(clean(x[k]).split()) <= 7 and len(set(clean(x[k]).split())) == len(clean(x[k]).split())][:4]: ws.append(order(tg, clean(a[k]).split(), hint(a, tg)))
        L.set('ПИШИ Й СКЛАДАЙ|PISZ I UKŁADAJ|WRITE AND BUILD', d['where'], 'Впиши й склади|Wpisz i ułóż|Type and build', ws)
        for t in d['speak']: a = sp(t); L.speak(a[k], hint(a, tg))
        vs = [sp(v) for sc in d['sc'] for v in sc[1].split(';')]; rnd.shuffle(vs); wi = []
        mi = 2 if tg != 'en' else 0
        for a in vs[:8]:
            o = [a[mi]] + [b[mi] for b in vs if b[mi] != a[mi]][:0]
            oth = [b[mi] for b in vs if b[mi] != a[mi]]; rnd.shuffle(oth); o = [a[mi]] + oth[:2]; rnd.shuffle(o)
            if tg != 'en': wi.append(mc('«%s» = ?' % a[k], o, o.index(a[mi]), '%s = %s' % (a[k], a[mi]), None, 'word'))
            else:
                o = [a[2]] + [b[2] for b in vs if b[2] != a[2]]; o = o[:1] + rnd.sample(o[1:], 2); rnd.shuffle(o)
                it = mc('«%s» = ?' % a[0], o, o.index(a[2]), a[0] + ' = ' + a[2], None, 'word'); it['q_pl'] = '«%s» = ?' % a[1]; it['q_en'] = it['q']; wi.append(it)
        L.set('СЛОВА УРОКУ|SŁOWA LEKCJI|LESSON WORDS', 'Що означає слово?|Co znaczy słowo?|What does the word mean?', 'Вісім слів|Osiem słów|Eight words', wi)
        f = sp(d['fin'][1])
        L.final('ФІНАЛ|FINAŁ|FINAL', d['fin'][0], f[k], 25)
        print(L.save('cars', num))
