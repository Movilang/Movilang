import json, html, os
E = html.escape
B = "https://movilang.pages.dev"
C = json.load(open('tools/courses_seo.json'))
os.makedirs('kursy', exist_ok=True)
CSS = """:root{--bg:#F7F6F3;--paper:#fff;--fg:#17161A;--mu:#5F5B68;--line:#E6E3DD;--ac:#C2391C;--acb:#E5482F}
@media(prefers-color-scheme:dark){:root{--bg:#111014;--paper:#19181D;--fg:#F2F0F5;--mu:#A7A2B0;--line:#2C2A31;--ac:#FF7456;--acb:#FF5B40}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.65 Figtree,system-ui,sans-serif}a{color:var(--ac)}
.w{max-width:980px;margin:auto;padding:22px 18px 70px}header{display:flex;justify-content:space-between;align-items:center;gap:12px}
header a{color:var(--fg);text-decoration:none;font-weight:700}.top{display:grid;grid-template-columns:240px 1fr;gap:34px;margin:34px 0;align-items:start}
.pst{aspect-ratio:2/3;border-radius:16px;background:#2a1d52 center/cover;max-width:100%}
h1{font:800 clamp(32px,5vw,50px)/1.03 "Bricolage Grotesque",system-ui,sans-serif;letter-spacing:-.03em;margin:8px 0 14px}
h2{font:800 26px "Bricolage Grotesque",system-ui,sans-serif;letter-spacing:-.02em;margin:44px 0 14px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0}.chips span{border:1px solid var(--line);background:var(--paper);border-radius:999px;padding:4px 12px;font-size:14px;font-weight:600}
.btn{display:inline-flex;align-items:center;height:50px;padding:0 24px;border-radius:999px;background:var(--acb);color:#fff;text-decoration:none;font-weight:700;margin:6px 8px 0 0}
.btn.o{background:transparent;color:var(--fg);border:1px solid var(--line)}.mu{color:var(--mu)}
ol{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:6px 24px;padding-left:22px}li{font-size:15px}li small{color:var(--mu)}li.b{font-weight:700}
.f{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}.f div{background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:16px;font-size:15px}.f b{display:block;font-size:16px}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:14px}.card{display:block;background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:16px;text-decoration:none;color:var(--fg)}
footer{margin-top:60px;color:var(--mu);font-size:13px;border-top:1px solid var(--line);padding-top:18px}
@media(max-width:700px){.top{grid-template-columns:1fr}.pst{width:160px}ol,.f{grid-template-columns:1fr}}"""
HEAD = '<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,800&family=Figtree:wght@400;600;700&display=swap"><style>' + CSS + '</style>'
HDR = '<header><a href="/">▶ MoviLang</a><nav><a href="/kursy/">Kursy</a> · <a href="/blog/">Blog</a></nav></header>'
FTR = '<footer>© 2026 MoviLang · Języki przez kino · <a href="/privacy.html">Polityka prywatności</a> · <a href="/terms.html">Regulamin</a><br>Tytuły filmów i seriali służą wyłącznie opisowi treści kursów; MoviLang nie jest powiązany z właścicielami praw.</footer>'
FEAT = '<div class="f"><div><b>Tłumaczenie każdego słowa</b>Dotknij słowa w zdaniu, a zobaczysz tłumaczenie w kontekście. Działa też dla całego zdania.</div><div><b>Mówienie od pierwszej lekcji</b>Powtarzasz kwestie bohaterów, a mikrofon sprawdza wymowę.</div><div><b>Wyjaśnienia po polsku lub ukraińsku</b>Gramatyka bez wkuwania, z przykładami ze scen.</div><div><b>Questy i powtórki</b>Co 6 lekcji „boss” łuku, a słówka wracają w powtórce dnia.</div><div><b>Certyfikat</b>Egzamin końcowy kursu i certyfikat z imieniem.</div><div><b>Płacisz raz</b>Bez subskrypcji, dostęp na zawsze. BLIK, Przelewy24, karta.</div></div>'
def page(c):
    url = f"{B}/kursy/{c['url']}.html"; kind = 'serialu' if c['k']=='series' else 'filmu'
    title = f"Angielski z {kind} „{c['t']}” — kurs {c['lv']} online | MoviLang"
    desc = c['d'][:155]
    lis = ''.join(f'<li class="b">{E(t)}</li>' if t.startswith(('Boss','Egzamin')) else f'<li>{E(t)}{" <small>· "+E(g)+"</small>" if g else ""}</li>' for t,g in (x.split('|',1) for x in c['ls']))
    gram = sorted({g for g in (x.split('|',1)[1] for x in c['ls']) if g})[:10]
    ld = {"@context":"https://schema.org","@graph":[{"@type":"Course","name":f"{c['t']} — angielski {c['lv']}","description":c['d'],"url":url,"inLanguage":"en","educationalLevel":c['lv'],"numberOfCredits":36,
      "provider":{"@type":"Organization","name":"MoviLang","url":B+"/"},"offers":{"@type":"Offer","category":"Paid","price":c['p'],"priceCurrency":"PLN","url":url},
      "hasCourseInstance":{"@type":"CourseInstance","courseMode":"online","courseWorkload":"PT6H"}, **({"image":c['img']} if c['img'] else {})},
      {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"MoviLang","item":B+"/"},{"@type":"ListItem","position":2,"name":"Kursy","item":B+"/kursy/"},{"@type":"ListItem","position":3,"name":c['t'],"item":url}]}]}
    others = ''.join(f'<a class="card" href="/kursy/{o["url"]}.html"><b>{E(o["t"])}</b><span class="mu">{o["lv"]} · {o["p"]} zł</span></a>' for o in C if o is not c)
    pst = f' style="background-image:url({c["img"]})"' if c['img'] else ''
    return f'''<!doctype html><html lang="pl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{url}">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{url}"><meta property="og:type" content="website"><meta property="og:image" content="{c['img'] or B+'/assets/og.png'}">
{HEAD}<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script></head><body><div class="w">{HDR}
<div class="top"><div class="pst" role="img" aria-label="Okładka kursu {E(c['t'])}"{pst}></div><div>
<span class="mu">Kurs angielskiego · {'serial' if c['k']=='series' else 'film'}</span><h1>Angielski z {kind} „{E(c['t'])}”</h1><p>{E(c['d'])}</p>
<div class="chips"><span>Poziom {c['lv']}</span><span>36 lekcji</span><span>ok. 6 godzin</span><span>certyfikat</span><span>{c['p']} zł jednorazowo</span></div>
<a class="btn" href="/#/course/{c['id']}">Zobacz kurs i zacznij</a><a class="btn o" href="/#/trial">Darmowa lekcja próbna</a>
<p class="mu" style="font-size:14px;margin-top:10px">Pierwsza lekcja za darmo, bez karty. Nie znasz poziomu? <a href="/#/test">Test w 2 minuty</a>.</p></div></div>
<h2>Jak wygląda nauka</h2>{FEAT}
<h2>Program: 36 lekcji</h2><ol>{lis}</ol>
<h2>Gramatyka w kursie</h2><p class="mu">{E(' · '.join(gram))} i więcej.</p>
<h2>Inne kursy</h2><div class="cards">{others}</div>
<p style="margin-top:34px"><a class="btn" href="/#/course/{c['id']}">Zacznij kurs „{E(c['t'])}”</a></p>{FTR}</div></body></html>'''
for c in C: open(f"kursy/{c['url']}.html",'w').write(page(c))
cards = ''.join(f'<a class="card" href="/kursy/{c["url"]}.html"><b>{E(c["t"])}</b><span class="mu">{"Serial" if c["k"]=="series" else "Film"} · {c["lv"]} · 36 lekcji · {c["p"]} zł</span></a>' for c in sorted(C, key=lambda c:c['lv']))
ld = {"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"url":f"{B}/kursy/{c['url']}.html","name":c['t']} for i,c in enumerate(C)]}
open('kursy/index.html','w').write(f'''<!doctype html><html lang="pl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Kursy angielskiego z filmów i seriali (A1–B2) | MoviLang</title><meta name="description" content="Kursy angielskiego online na podstawie filmów i seriali: Harry Potter, Przyjaciele, Gra o tron, Auta i inne. Poziomy A1–B2, 36 lekcji, płacisz raz."><link rel="canonical" href="{B}/kursy/">
{HEAD}<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script></head><body><div class="w">{HDR}
<h1 style="margin-top:34px">Kursy angielskiego z filmów i seriali</h1><p class="mu">Wybierz film lub serial na swoim poziomie. Każdy kurs ma 36 interaktywnych lekcji, questy, mówienie i certyfikat. Płacisz raz, bez subskrypcji.</p>
<p><a class="btn" href="/#/trial">Darmowa lekcja próbna</a><a class="btn o" href="/#/test">Sprawdź poziom</a></p>
<h2>Wszystkie kursy</h2><div class="cards">{cards}</div>{FTR}</div></body></html>''')
# sitemap
sm = open('sitemap.xml').read()
add = ''.join(f'  <url><loc>{B}/kursy/{u}</loc><lastmod>2026-11-07</lastmod></url>\n' for u in [''] + [c['url']+'.html' for c in C] if f'/kursy/{u}<' not in sm)
open('sitemap.xml','w').write(sm.replace('</urlset>', add + '</urlset>'))
print('ok', len(C))
