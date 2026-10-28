# MoviLang — standard lekcji „15 minut” (specyfikacja dla autorów)

Platforma: https://movilang.pages.dev. Kurs = film/serial, 36 lekcji. Każda lekcja istnieje w 3 wersjach
**języka nauki (tg)**: `en` (lekcje w kolumnie `lessons.tasks`), `pl` (`lessons.variants->'pl'`), `uk` (`lessons.variants->'uk'`).
Uczeń wybiera też **język interfejsu/wskazówek** (uk / pl / en). Dlatego KAŻDY tekst pomocniczy podajesz w 3 wersjach:
pole bazowe po **ukraińsku**, `_pl` po polsku, `_en` po angielsku (np. `label`, `label_pl`, `label_en`).
Treść w języku nauki (kwestie, warianty odpowiedzi, słowa do wpisania) NIE jest tłumaczona — tłumaczenie idzie do `tr`/`tr_pl`/`tr_en`.

Wzorzec do skopiowania stylu i struktury: `tools/course-std/EXAMPLE_cars_01_uk.json` (Auta, lekcja 1, nauka ukraińskiego). Przeczytaj go w całości zanim zaczniesz.

## Cel jakości
- Lekcja trwa ~15 minut: **11–15 zadań punktowanych**, łącznie **55–75 odpowiedzi**. Zadanie = karta z zestawem 5–12 pytań, nie jedno pytanie.
- **Wszystko o tej scenie filmu.** Żadnych losowych zdań typu „Мак — вантажівка”. Kwestie bohaterów, sytuacje z fabuły, decyzje ucznia w tej scenie.
- **Uczeń jest w środku historii** (rola w świecie filmu — patrz tabela ról). Pisz „ty” — ty w boksie, ty w Hogwarcie, ty przy stoliku w MacLaren's.
- **Poziom CEFR kursu** (tabela) — długość zdań, czasy, słownictwo. A1: zdania 3–8 słów, czas teraźniejszy; B1–B2: dłuższe zdania, czasy z gramatyki lekcji, idiomy z serialu.
- Gramatyka lekcji = pole `grammar` lekcji (EN) lub `variants.<tg>_grammar` (PL/UA). Zestaw gramatyczny ćwiczy DOKŁADNIE ten temat, w kwestiach bohaterów.
- Nie cytuj długich fragmentów scenariusza: kwestie do ~10 słów, reszta własnymi słowami.
- Poprawny, naturalny język docelowy. Tłumaczenia PL/EN/UA naturalne, nie dosłowne kalki.
- Błędne opcje wiarygodne, ale jednoznacznie błędne (bez dwóch poprawnych odpowiedzi). Pozycja poprawnej odpowiedzi różna (nie zawsze pierwsza).

## Układ zwykłej lekcji (kolejność)
1. `{"ref": i}` — karta bohaterów (cards) z obecnej wersji lekcji (zachowaj).
2. `intro` „TWOJA ROLA” — 2–3 zdania: gdzie jesteś i co robisz w tej scenie (u, pl, en).
3. Dla KAŻDEJ sceny (zwykle 3 słowniczki = 3 sceny):
   a. `{"ref": i}` — słowniczek sceny z obecnej wersji (glossary) — zachowaj, nie przepisuj;
   b. `match` — 5 par słowo sceny = tłumaczenie (`options` z tłumaczeniem EN, `options_pl`, `options_en`; dla tg=en daj `options` z tłumaczeniem UA, `options_pl`, `options_en`… patrz uwaga niżej);
   c. `drill` `kind:"set"` — 6–9 pytań o tę scenę: kwestie z luką (`tag` „Репліка”), prawda/fałsz (opcje w języku nauki: Правда/Неправда, Prawda/Fałsz, True/False), pytania o fabułę/emocje/„co robisz?”.
4. `intro` „ПРАВИЛО” — krótka zasada gramatyczna lekcji z 3–4 przykładami z filmu.
5. `drill` `kind:"set"` gramatyka — **10–15 pytań**, wszystkie to kwestie bohaterów/sytuacje lekcji.
6. `reading` — **artykuł/list/raport z świata filmu**: `title` (+_pl/_en), 14–20 zdań w `items`; w ≥10 zdaniach luka `____` z 3 opcjami (`options`, `answer`), pozostałe zdania bez `options` (zwykły tekst). Opowiada scenę lekcji.
7. `drill` `kind:"set"` „ROZUMIENIE TEKSTU” — 5 pytań MC do artykułu.
8. `quest` — 3–5 kroków z rozgałęzieniem, 2–3 zakończenia (`end_good`, `end_mid`, `end_bad`), wybory w języku nauki, ćwiczą słowa+gramatykę lekcji.
9. `drill` `kind:"set"` „PISZ I UKŁADAJ” — 8 pozycji: połowa `k:"type"` (napisz kwestię/słowo w języku nauki z tłumaczenia), połowa `k:"order"` (ułóż kwestię; `options` = słowa w POPRAWNEJ kolejności, gracz je tasuje).
10. `speaking` × 2 — kwestie z lekcji do powiedzenia na głos (`say` w języku nauki, `tip` z tłumaczeniem).
11. `drill` `kind:"set"` „PO SCENIE / SŁOWNICTWO” — 8–10 pytań na słowa lekcji w nowych kontekstach.
12. `final` — wypracowanie w świecie filmu (`answer`: min. słów — A1:25, A2:35, B1:60, B2:90), z `tip` = szkielet startowy w języku nauki.

Lekcje „BOSS ARC” (Auta: 6, 12, 18, 24, 30, 35 — tytuł zaczyna się od „Бос арки”/„Boss”): przegląd całego łuku: rola, 3 zestawy po 8–10 pytań (słowa łuku, gramatyka łuku, fabuła łuku), czytanie 18–22 zdań streszczające łuk, quest 6–8 kroków, pisz-i-układaj 10, final. Lekcja 36 (egzamin końcowy): 4 zestawy po 10 (słownictwo, gramatyka, fabuła, pisanie), czytanie 20 zdań o całym filmie, final 1.5× dłuższy. Słowniczki w bossach/egzaminie zachowaj przez `ref`, jeśli są.

## Format pozycji w zestawie (`drill` `kind:"set"`, pole `items`)
- MC (domyślnie): `{"q": "...", "options": [3–4], "answer": n, "exp": "...", "exp_pl", "exp_en", "tr", "tr_pl", "tr_en", "tag", "tag_pl", "tag_en"}`
  - `q` w języku nauki (z luką `____` jeśli to kwestia). Gdy `q` jest pytaniem o fabułę, możesz zapisać je w języku nauki (A2+), a `tr*` = tłumaczenie.
- Wpisz: `{"k": "type", "q": "...", "q_pl": "...", "q_en": "...", "options": [akceptowane odpowiedzi], "exp"...}` — tu `q` jest poleceniem w języku wskazówek (base=ua, _pl, _en), np. „Napisz po angielsku: „Jestem szybki.””. Akceptuj warianty bez kropki / z małej litery.
- Ułóż: `{"k": "order", "q": ..., "q_pl", "q_en", "options": [słowa w poprawnej kolejności], "exp"...}`.
Karta zestawu: `{"type":"drill","kind":"set","label*","q*" (krótki opis sytuacji),"ins*","tip*":"Потрібно 70%+." ...,"items":[...]}`.

## Inne typy (dokładne pola — zobacz przykład)
- `intro`: `label*`, `q*`.
- `match`: `options` = „słowo=tłumaczenie” (tłumaczenie w języku… patrz niżej), `options_pl`, `options_en`, `label*`, `q*`, `qt_pl`, `qt_en`, `ins*`, `tip*`.
  - Tłumaczenia w match: `options_pl` po polsku, `options_en` po angielsku, `options` (bazowe, dla interfejsu UA) po ukraińsku. Gdy tg=uk, bazowe `options` daj po angielsku (jak w przykładzie), bo uczący się ukraińskiego nie ma ukraińskiego interfejsu.
- `reading`: `title*`, `label*`, `q*`, `tip*`, `items`.
- `quest`: `start`, `steps{ id: {q, q_pl, q_en, scene*, choices:[{t, ok, next, fb, fb_pl, fb_en}]}}`, `endings{ end_x: {good, title*, text*}}`, `label*`, `q*`, `ins*`, `tip*`, `img` (jedno z: castle stairs snake letter cake alley wand train hat potion broom troll pitch mirror forest chess stone owl tomb crow ring vervain diary candles manor comet).
- `speaking`: `say`, `label*`, `q*`, `qt_pl`, `qt_en`, `ins*`, `tip*`.
- `final`: `answer` (min. słów), `img`, `label*`, `q*`, `ins*`, `tip*`.
(`*` = pole bazowe + `_pl` + `_en`.)

## Role ucznia (pierwsza osoba) i poziomy
| kurs (slug) | poziom | rola ucznia |
|---|---|---|
| cars | A1 | nowicjusz w ekipie mechaników (pit crew) Zygzaka McQueena |
| zootopia | A1–A2 | rekrut ZPD z tej samej akademii co Judy |
| home-alone | A2 | przyjaciel Kevina z domu obok, też został w mieście |
| friends-s1 | A2–B1 | siódmy przyjaciel z kanapy w Central Perk |
| harry-potter-1 | B1 | pierwszoroczny, przyjaciel Harry'ego |
| vampire-diaries-1 | B1–B2 | nowy uczeń w liceum Mystic Falls, w klasie Eleny |
| himym-s1 | B1–B2 | stały bywalec MacLaren's, przyjaciel paczki |

## Pliki i wgrywanie
1. Zanim napiszesz lekcję, pobierz jej dane: `select num,title,title_en,scene,scene_en,grammar,variants - 'pl' - 'uk' - 'en' as meta, <zestaw> from lessons where id='<id>'` gdzie `<zestaw>` = `tasks` (tg=en) albo `variants->'pl'` / `variants->'uk'`. Przeczytaj słowniczki (glossary: słowa, kwestie `line`, `who`) — na nich budujesz lekcję. Zanotuj indeksy kart `cards`/`glossary` do `ref`.
2. Zapisz plik `tools/course-std/<slug>/<NN>_<tg>.json`: `{"lesson_id": "...", "tg": "uk|pl|en", "tasks": [...]}` (NN = numer lekcji, dwie cyfry).
3. Sprawdź: `python3 tools/course-std/validate.py <plik>` — popraw wszystkie BŁĘDY.
4. Zbuduj SQL: `python3 tools/course-std/build_sql.py <plik> > /tmp/x.sql`, wyświetl go i wykonaj w Supabase (`execute_sql`, project_id `pybzpbkmdupvtsmxlqvr`). Skrypt sam robi kopię zapasową (tabela `lesson_backups`) i jest bezpieczny do ponownego uruchomienia. Odpowiedź SQL pokaże liczbę kart — sprawdź.
5. NIE zmieniaj kodu strony ani innych lekcji/kursów niż przydzielone.
