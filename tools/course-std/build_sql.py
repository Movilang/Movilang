#!/usr/bin/env python3
"""Buduje SQL wgrywający lekcję (standard 15 minut). Użycie: python3 build_sql.py plik.json
- robi kopię zapasową oryginału (raz na lekcję i język: note = 'std-<tg>'),
- {"ref": i} = element i z ORYGINAŁU (kopii zapasowej), więc ponowne uruchomienie jest bezpieczne."""
import json, sys
d = json.load(open(sys.argv[1]))
lid, tg, ts = d['lesson_id'], d['tg'], d['tasks']
src = "b.tasks" if tg == 'en' else "b.variants->'%s'" % tg
parts, buf = [], []
def flush():
    if buf:
        parts.append("'" + json.dumps(buf, ensure_ascii=False).replace("'", "''") + "'::jsonb"); buf.clear()
for t in ts:
    if 'ref' in t:
        flush(); parts.append("jsonb_build_array(%s->%d)" % (src, int(t['ref'])))
    else:
        buf.append(t)
flush()
arr = ' || '.join(parts)
note = 'std-' + tg
print("insert into lesson_backups(lesson_id,tasks,variants,note) select id,tasks,variants,'%s' from lessons where id='%s' and not exists (select 1 from lesson_backups where lesson_id='%s' and note='%s');" % (note, lid, lid, note))
if tg == 'en':
    print("update lessons set tasks = (%s) from (select tasks, variants from lesson_backups where lesson_id='%s' and note='%s' order by id limit 1) b where lessons.id='%s';" % (arr, lid, note, lid))
    print("select num, jsonb_array_length(tasks) cards from lessons where id='%s';" % lid)
else:
    print("update lessons set variants = jsonb_set(coalesce(lessons.variants,'{}'::jsonb), '{%s}', (%s)) from (select tasks, variants from lesson_backups where lesson_id='%s' and note='%s' order by id limit 1) b where lessons.id='%s';" % (tg, arr, lid, note, lid))
    print("select num, jsonb_array_length(variants->'%s') cards from lessons where id='%s';" % (tg, lid))
