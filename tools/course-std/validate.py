#!/usr/bin/env python3
"""Walidator lekcji MoviLang (standard 15 minut). Użycie: python3 validate.py plik.json [...]"""
import json, re, sys

CYR = re.compile(r'[Ѐ-ӿ]')
TRI = ['label', 'q', 'ins', 'tip', 'title', 'text', 'exp', 'tr', 'tag', 'scene']
IMG = set('castle stairs snake letter cake alley wand train hat potion broom troll pitch mirror forest chess stone owl tomb crow ring vervain diary candles manor comet'.split())

def check(path):
    E, W = [], []
    d = json.load(open(path))
    tg = d.get('tg'); ts = d.get('tasks')
    if tg not in ('en', 'pl', 'uk'): E.append('tg musi być en/pl/uk')
    if not re.match(r'^[0-9a-f-]{36}$', d.get('lesson_id', '')): E.append('brak/zły lesson_id')
    if not isinstance(ts, list) or not ts: E.append('brak tasks'); return E, W
    def tri(o, where, keys=TRI):
        for k in keys:
            if k in o and isinstance(o[k], str):
                for s in ('_pl', '_en'):
                    if not str(o.get(k + s, '')).strip(): E.append('%s: brak %s%s' % (where, k, s))
    def opts_ok(o, where):
        op = o.get('options') or []
        if len([x for x in op if str(x).strip()]) != len(op): E.append(where + ': pusta opcja')
        if len(set(str(x).strip().lower() for x in op)) != len(op): E.append(where + ': zduplikowana opcja')
        a = o.get('answer')
        if not isinstance(a, int) or not (0 <= a < len(op)): E.append(where + ': answer poza zakresem')
        if tg == 'en' and any(CYR.search(str(x)) for x in op): E.append(where + ': cyrylica w opcjach (tg=en)')
    scored = answers = 0; types = []
    for i, t in enumerate(ts):
        w = 'zad.%d' % (i + 1)
        if 'ref' in t:
            if not isinstance(t['ref'], int): E.append(w + ': ref musi być liczbą')
            continue
        ty = t.get('type'); types.append(ty)
        if ty not in ('intro', 'cards', 'glossary', 'match', 'drill', 'reading', 'quest', 'speaking', 'final', 'vocabulary', 'grammar', 'quiz', 'tf', 'order', 'type'):
            E.append(w + ': nieznany typ ' + str(ty)); continue
        if t.get('img') and t['img'] not in IMG: E.append(w + ': nieznany img')
        tri(t, w + '(' + ty + ')')
        if ty in ('intro', 'cards', 'glossary'): continue
        scored += 1
        if ty == 'drill':
            its = t.get('items') or []
            if t.get('kind') != 'set': W.append(w + ': drill bez kind:"set"')
            if not 5 <= len(its) <= 16: E.append(w + ': zestaw musi mieć 5–16 pytań (ma %d)' % len(its))
            answers += len(its)
            for j, it in enumerate(its):
                ww = '%s.p%d' % (w, j + 1)
                k = it.get('k', 'mc')
                if not str(it.get('q', '')).strip(): E.append(ww + ': puste q')
                tri(it, ww, ['exp', 'tr', 'tag'])
                if not str(it.get('exp', '')).strip(): W.append(ww + ': brak exp')
                if k == 'mc':
                    opts_ok(it, ww)
                    if len(it.get('options') or []) < 2: E.append(ww + ': za mało opcji')
                elif k in ('type', 'order'):
                    if not it.get('options'): E.append(ww + ': brak options (odpowiedzi/słów)')
                    for s in ('q_pl', 'q_en'):
                        if not str(it.get(s, '')).strip(): E.append(ww + ': brak ' + s)
                else: E.append(ww + ': nieznane k')
        elif ty == 'match':
            op = t.get('options') or []
            if len(op) < 4: E.append(w + ': match min. 4 pary')
            for s in ('options_pl', 'options_en'):
                if len(t.get(s) or []) != len(op): E.append(w + ': ' + s + ' ≠ liczba par')
            if any('=' not in x for x in op): E.append(w + ': para bez „=”')
            answers += len(op)
        elif ty == 'reading':
            its = t.get('items') or []; gaps = [x for x in its if x.get('options')]
            if len(its) < 12: E.append(w + ': czytanie min. 12 zdań (ma %d)' % len(its))
            if len(gaps) < 8: E.append(w + ': czytanie min. 8 luk (ma %d)' % len(gaps))
            for j, it in enumerate(gaps):
                if str(it.get('q', '')).count('____') != 1: E.append('%s.z%d: zdanie z opcjami musi mieć dokładnie jedną lukę ____' % (w, j + 1))
                opts_ok(it, '%s.z%d' % (w, j + 1))
            if not t.get('title'): W.append(w + ': brak title artykułu')
            answers += len(gaps)
        elif ty == 'quest':
            st = t.get('steps') or {}; en = t.get('endings') or {}
            if t.get('start') not in st: E.append(w + ': start nie istnieje')
            for sid, s in st.items():
                tri(s, w + '.' + sid, ['scene'])
                for s2 in ('q_pl', 'q_en'):
                    if not s.get(s2): E.append(w + '.' + sid + ': brak ' + s2)
                for c in s.get('choices') or []:
                    if c.get('next') not in st and c.get('next') not in en: E.append(w + '.' + sid + ': next „%s” nie istnieje' % c.get('next'))
                    for s2 in ('fb_pl', 'fb_en'):
                        if not c.get(s2): E.append(w + '.' + sid + ': brak ' + s2)
            for eid, e in en.items(): tri(e, w + '.' + eid, ['title', 'text'])
            if len(en) < 2: E.append(w + ': min. 2 zakończenia')
            answers += max(3, len(st) - 1)
        elif ty == 'speaking':
            if not t.get('say'): E.append(w + ': brak say')
            answers += 1
        elif ty == 'final':
            if not isinstance(t.get('answer'), int): E.append(w + ': final.answer = min. słów')
            answers += 3
        else:
            answers += 1
            if t.get('options') and ty not in ('order', 'type'): opts_ok(t, w)
    if 'final' not in types: E.append('brak final')
    if 'reading' not in types: W.append('brak reading')
    if 'quest' not in types: W.append('brak quest')
    if not 10 <= scored <= 16: W.append('zadań punktowanych: %d (cel 11–15)' % scored)
    if answers < 50: E.append('za mało odpowiedzi: %d (cel 55–75)' % answers)
    return E, W, scored, answers

if __name__ == '__main__':
    bad = 0
    for p in sys.argv[1:]:
        r = check(p); E, W = r[0], r[1]
        print('==', p, '| zadania: %s, odpowiedzi: %s' % (r[2] if len(r) > 2 else '?', r[3] if len(r) > 3 else '?'))
        for e in E: print('  BŁĄD:', e)
        for x in W: print('  uwaga:', x)
        if E: bad += 1
        else: print('  OK')
    sys.exit(1 if bad else 0)
