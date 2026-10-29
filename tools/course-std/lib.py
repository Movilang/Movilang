# Kompaktowy DSL do lekcji MoviLang. Teksty pomocnicze: "ua|pl|en".
import json, sys, os
def T(s):
    p = s.split('|'); p += [p[-1]] * (3 - len(p)); return p
def put(d, k, s):
    if s is None: return
    a = T(s); d[k], d[k + '_pl'], d[k + '_en'] = a
OK70 = 'Потрібно 70%+.|Potrzeba 70%+.|You need 70%+.'
LBL = {'line': 'Репліка|Kwestia|Line', 'tf': 'Правда чи ні?|Prawda czy nie?|True or false?', 'story': 'Сюжет|Fabuła|Story',
       'you': 'Твій вибір|Twój wybór|Your call', 'gram': 'Граматика|Gramatyka|Grammar', 'word': 'Слово|Słowo|Word',
       'write': 'Напиши|Napisz|Write', 'build': 'Склади|Ułóż|Build', 'text': 'Текст|Tekst|Text'}
TFW = {'uk': ['Правда', 'Неправда'], 'pl': ['Prawda', 'Fałsz'], 'en': ['True', 'False']}
LN = {'uk': ('українською', 'po ukraińsku', 'in Ukrainian'), 'pl': ('польською', 'po polsku', 'in Polish'), 'en': ('англійською', 'po angielsku', 'in English')}

class Lesson:
    def __init__(s, lid, tg): s.lid, s.tg, s.t = lid, tg, []
    def ref(s, i): s.t.append({'ref': i}); return s
    def intro(s, label, text): d = {'type': 'intro'}; put(d, 'label', label); put(d, 'q', text); s.t.append(d); return s
    def match(s, label, pairs):
        """pairs: 'słowo=ua/pl/en' list (tłumaczenia przez /)."""
        b, p, e = [], [], []
        for x in pairs:
            w, tr = x.split('=', 1); a = tr.split('/'); a += [a[-1]] * (3 - len(a))
            b.append(w + '=' + (a[2] if s.tg == 'uk' else a[0])); p.append(w + '=' + a[1]); e.append(w + '=' + a[2])
        d = {'type': 'match', 'options': b, 'options_pl': p, 'options_en': e}
        put(d, 'label', label); put(d, 'q', "З'єднай слова сцени з перекладом.|Połącz słowa sceny z tłumaczeniem.|Match the scene words with their translations.")
        d['qt_pl'], d['qt_en'] = d['q_pl'], d['q_en']
        put(d, 'ins', "П'ять пар зі сцени|Pięć par ze sceny|Five pairs from the scene"); put(d, 'tip', 'Повернись до словника сцени.|Wróć do słownika sceny.|Go back to the scene glossary.')
        s.t.append(d); return s
    def set(s, label, q, ins, items, tip=OK70):
        d = {'type': 'drill', 'kind': 'set', 'items': items}
        put(d, 'label', label); put(d, 'q', q); put(d, 'ins', ins); put(d, 'tip', tip); s.t.append(d); return s
    def reading(s, title, label, q, sents, tip):
        d = {'type': 'reading', 'items': sents}
        put(d, 'title', title); put(d, 'label', label); put(d, 'q', q); put(d, 'tip', tip); s.t.append(d); return s
    def quest(s, label, q, img, steps, endings, start='s1'):
        d = {'type': 'quest', 'img': img, 'start': start, 'steps': steps, 'endings': endings}
        put(d, 'label', label); put(d, 'q', q)
        put(d, 'ins', 'Кожен вибір веде далі. Обирай уважно|Każdy wybór prowadzi dalej. Wybieraj uważnie|Every choice leads on. Choose carefully')
        put(d, 'tip', 'Квест перевіряє слова й граматику уроку.|Quest sprawdza słowa i gramatykę lekcji.|The quest checks the lesson words and grammar.')
        s.t.append(d); return s
    def speak(s, line, tr):
        d = {'type': 'speaking', 'say': line}
        put(d, 'label', 'ГОВОРІННЯ|MÓWIENIE|SPEAKING'); put(d, 'q', 'Скажи це вголос.|Powiedz to na głos.|Say it out loud.')
        d['qt_pl'], d['qt_en'] = d['q_pl'], d['q_en']
        put(d, 'ins', 'Прочитай і скажи вголос|Przeczytaj i powiedz na głos|Read it and say it aloud')
        a = T(tr); put(d, 'tip', 'Переклад: %s|Tłumaczenie: %s|Translation: %s' % (a[2] if s.tg != 'en' else a[0], a[1], a[2])); s.t.append(d); return s
    def final(s, label, q, tip, words, img='diary'):
        d = {'type': 'final', 'img': img, 'answer': words}; put(d, 'label', label); put(d, 'q', q); put(d, 'ins', 'Напиши текст|Napisz tekst|Write a text')
        d['tip'] = d['tip_pl'] = d['tip_en'] = tip; s.t.append(d); return s
    def save(s, slug, num):
        os.makedirs('/home/claude/movilang/content/std/' + slug, exist_ok=True)
        p = '/home/claude/movilang/content/std/%s/%02d_%s.json' % (slug, num, s.tg)
        json.dump({'lesson_id': s.lid, 'tg': s.tg, 'tasks': s.t}, open(p, 'w'), ensure_ascii=False); return p

# --- pozycje zestawów ---
def mc(q, opts, ans, exp, tr=None, tag='story'):
    it = {'q': q, 'options': opts, 'answer': ans}; put(it, 'exp', exp); put(it, 'tag', LBL.get(tag, tag))
    if tr: put(it, 'tr', tr)
    return it
def gap(line, tr, opts, ans, exp): return mc(line, opts, ans, exp, tr, 'line')
def tf(tg, stmt, tr, true, exp): return mc(stmt, TFW[tg], 0 if true else 1, exp, tr, 'tf')
def typ(tg, ans, tr, alts=()):
    a = T(tr); l = LN[tg]
    it = {'k': 'type', 'q': 'Напиши %s: «%s»' % (l[0], a[2] if tg != 'en' else a[0]), 'q_pl': 'Napisz %s: „%s”' % (l[1], a[1]), 'q_en': 'Write %s: “%s”' % (l[2], a[2] if tg != 'en' else a[0]),
          'options': [ans] + [x for x in alts] + [ans.rstrip('.!?')]}
    it['options'] = list(dict.fromkeys(it['options'])); put(it, 'exp', ans); put(it, 'tag', LBL['write']); return it
def order(tg, words, tr):
    a = T(tr)
    it = {'k': 'order', 'q': 'Склади репліку: «%s»' % (a[2] if tg != 'en' else a[0]), 'q_pl': 'Ułóż kwestię: „%s”' % a[1], 'q_en': 'Build the line: “%s”' % (a[2] if tg != 'en' else a[0]), 'options': words}
    put(it, 'exp', ' '.join(words)); put(it, 'tag', LBL['build']); return it
def S(text, opts=None, ans=0):
    return {'q': text} if opts is None else {'q': text, 'options': opts, 'answer': ans}
def step(q, tr, scene, choices): d = {'q': q}; a = T(tr); d['q_pl'] = q + ' (' + a[1] + ')'; d['q_en'] = q + ' (' + a[2] + ')'; put(d, 'scene', scene); d['choices'] = choices; return d
def ch(t, ok, nxt, fb): d = {'t': t, 'ok': ok, 'next': nxt}; put(d, 'fb', fb); return d
def end(good, title, text): d = {'good': good}; put(d, 'title', title); put(d, 'text', text); return d
