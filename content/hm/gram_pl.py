# HIMYM S1 (B1–B2).
G = {}
D = {}
T = {}

# ---- Łuk 1
T[1] = ("Минулий час: доконаний і недоконаний вид", "Czas przeszły: aspekt dokonany i niedokonany", "Past tense: perfective vs imperfective")
G[1] = [
 ("Kiedy Ted ____ do baru, Robin siedziała przy stoliku.", ["wszedł", "wchodził", "wejdzie"], 0,
  [("Так! Коротка завершена дія → доконаний вид.", "Tak! Krótka, zakończona czynność → dokonany.", "Yes! A short completed action → perfective."),
   ("Wchodził — процес, а тут подія.", "„Wchodził” — proces, a tu wydarzenie.", "Wchodził is a process; here it's an event."),
   ("Wejdzie — майбутнє.", "„Wejdzie” — przyszłość.", "Wejdzie is future.")],
  ("Фон — недоконаний (siedziała), подія — доконаний (wszedł).", "Tło — niedokonany, wydarzenie — dokonany.", "Background — imperfective, event — perfective.")),
 ("Marshall ____ się Lily wczoraj wieczorem.", ["oświadczył", "oświadczał", "oświadcza"], 0,
  [("Так! Один раз, результат → oświadczył.", "Tak! Jednorazowo, z rezultatem.", "Yes! Once, with a result → oświadczył."),
   ("Oświadczał — неодноразово або процес.", "„Oświadczał” — wielokrotnie lub proces.", "Oświadczał is repeated or ongoing."),
   ("Oświadcza — теперішній.", "„Oświadcza” — teraźniejszy.", "Oświadcza is present.")],
  ("Доконаний вид = результат.", "Aspekt dokonany = rezultat.", "Perfective = result.")),
]
D[1] = ("Opisz wieczór, kiedy poznałeś(-aś) kogoś ważnego (50+ słów). Użyj aspektu dokonanego i niedokonanego.", 50,
 ("Siedziałem w barze, kiedy… Rozmawialiśmy… Potem…", "Siedziałem w barze, kiedy… Rozmawialiśmy… Potem…", "Siedziałem w barze, kiedy… Rozmawialiśmy… Potem…"))

T[2] = ("już / jeszcze nie + вид дієслова", "już / jeszcze nie + aspekt", "już / jeszcze nie + aspect")
G[2] = [
 ("Robin jeszcze nie ____.", ["przyszła", "przychodzi", "przyjdzie"], 0,
  [("Так! Jeszcze nie + доконаний минулий.", "Tak! Jeszcze nie + dokonany.", "Yes! Jeszcze nie + perfective past."),
   ("Теперішній тут не пасує.", "Teraźniejszy nie pasuje.", "Present doesn't fit."),
   ("Майбутнє — інший зміст.", "Przyszłość — inny sens.", "Future changes the meaning.")],
  ("Англ. haven't … yet ≈ jeszcze nie + минулий доконаний.", "Haven't … yet ≈ jeszcze nie + dokonany.", "Haven't … yet ≈ jeszcze nie + perfective past.")),
 ("Ted ____ imprezy od tygodnia.", ["urządza", "urządził", "urządzi"], 0,
  [("Так! Od tygodnia + теперішній = have been doing.", "Tak! Od tygodnia + teraźniejszy.", "Yes! Od tygodnia + present = have been doing."),
   ("Минулий не показує, що дія триває.", "Przeszły nie pokazuje trwania.", "Past doesn't show it's ongoing."),
   ("Майбутнє — ні.", "Przyszłość — nie.", "Not future.")],
  ("Польська: od + теперішній час.", "Polski: od + czas teraźniejszy.", "Polish: od + present tense.")),
]
D[2] = ("Napisz wiadomość do przyjaciela (50+ słów): co już zrobiłeś(-aś) w tym miesiącu, a czego jeszcze nie.", 50,
 ("Już… Jeszcze nie… Od tygodnia…", "Już… Jeszcze nie… Od tygodnia…", "Już… Jeszcze nie… Od tygodnia…"))

T[3] = ("Майбутній час: zrobię / będę robić", "Czas przyszły: zrobię / będę robić", "Future: zrobię / będę robić")
G[3] = [
 ("Dziś wieczorem ____ do Filadelfii!", ["polecimy", "lecieliśmy", "latamy"], 0,
  [("Так! Один конкретний рейс → доконаний майбутній.", "Tak! Konkretny lot → dokonany.", "Yes! A single trip → perfective future."),
   ("Минулий.", "Przeszły.", "Past."),
   ("Latamy — регулярно.", "„Latamy” — regularnie.", "Latamy means regularly.")],
  ("Доконаний вид у теперішній формі = майбутнє.", "Dokonany w formie teraźniejszej = przyszłość.", "Perfective present form = future.")),
 ("Całą noc ____ się bawić!", ["będziemy", "będą", "byliśmy"], 0,
  [("Так! Będziemy + інфінітив = процес у майбутньому.", "Tak! Będziemy + bezokolicznik.", "Yes! Będziemy + infinitive = ongoing future."),
   ("Będą — вони.", "„Będą” — oni.", "Będą is they."),
   ("Минулий.", "Przeszły.", "Past.")],
  ("Будемо робити = być + недоконаний.", "Będę robić = być + niedokonany.", "Będę robić = być + imperfective.")),
]
D[3] = ("Zaplanuj idealny weekend (50+ słów). Co zrobisz? Co będziesz robić całą sobotę?", 50,
 ("W sobotę pojedziemy… Będziemy… Na pewno zobaczymy…", "W sobotę pojedziemy… Będziemy… Na pewno zobaczymy…", "W sobotę pojedziemy… Będziemy… Na pewno zobaczymy…"))

T[4] = ("Висновки: musi być / może być / nie może być", "Wnioskowanie: musi być / może być / nie może być", "Deduction: musi być / może być / nie może być")
G[4] = [
 ("Ted ciągle wzdycha. On ____ być nieszczęśliwy.", ["musi", "może nie", "nie musi"], 0,
  [("Так! Упевнений висновок → musi.", "Tak! Pewny wniosek → musi.", "Yes! A confident deduction → musi."),
   ("Це сумнів, а докази сильні.", "To wątpliwość, a dowody są mocne.", "That's doubt, but the evidence is strong."),
   ("Nie musi = не обов'язково.", "„Nie musi” = nie trzeba.", "Nie musi = doesn't have to.")],
  ("Musi być = must be; nie może być = can't be.", "Musi być = must be; nie może być = can't be.", "Musi być = must be; nie może być = can't be.")),
 ("To ____ być znak. Kto wie?", ["może", "musi", "nie może"], 0,
  [("Так! Можливо → może.", "Tak! Możliwe → może.", "Yes! Possibly → może."),
   ("Musi — надто впевнено.", "„Musi” — za pewne.", "Musi is too certain."),
   ("Nie może — протилежне.", "„Nie może” — odwrotnie.", "Nie może is the opposite.")],
  ("Może być = might be.", "Może być = might be.", "Może być = might be.")),
]
D[4] = ("Opisz nieznajomych na zdjęciu (50+ słów) i zgadnij, kim są. Użyj: musi być, może być, nie może być.", 50,
 ("Oni muszą być… Ona może być… On nie może być…", "Oni muszą być… Ona może być… On nie może być…", "Oni muszą być… Ona może być… On nie może być…"))

T[5] = ("Kiedyś + недоконаний; przyzwyczaić się do", "Kiedyś + niedokonany; przyzwyczaić się do", "Kiedyś + imperfective; przyzwyczaić się do")
G[5] = [
 ("Kiedyś Ted co roku ____ na dachu do rana.", ["czekał", "poczekał", "czeka"], 0,
  [("Так! Повторювана дія → недоконаний.", "Tak! Powtarzana czynność → niedokonany.", "Yes! A repeated action → imperfective."),
   ("Poczekał — один раз.", "„Poczekał” — raz.", "Poczekał means once."),
   ("Теперішній.", "Teraźniejszy.", "Present.")],
  ("Used to / would ≈ kiedyś + недоконаний вид.", "Used to / would ≈ kiedyś + niedokonany.", "Used to / would ≈ kiedyś + imperfective.")),
 ("Ted jest przyzwyczajony do ____ w samotności.", ["czekania", "czekać", "czeka"], 0,
  [("Так! Do + віддієслівний іменник у родовому.", "Tak! Do + rzeczownik odczasownikowy w dopełniaczu.", "Yes! Do + verbal noun in the genitive."),
   ("Після do — не інфінітив.", "Po „do” — nie bezokolicznik.", "No infinitive after do."),
   ("Особова форма — ні.", "Forma osobowa — nie.", "Not a personal form.")],
  ("Be used to + -ing = przyzwyczajony do + -ania.", "Be used to + -ing = przyzwyczajony do + -ania.", "Be used to + -ing = przyzwyczajony do + -ania.")),
]
D[5] = ("Opisz swoje dzieciństwo (50+ słów): co kiedyś robiłeś(-aś), do czego się przyzwyczaiłeś(-aś).", 50,
 ("Kiedyś co lato… Codziennie chodziłem… Teraz jestem przyzwyczajony do…", "Kiedyś co lato… Codziennie chodziłem… Teraz jestem przyzwyczajony do…", "Kiedyś co lato… Codziennie chodziłem… Teraz jestem przyzwyczajony do…"))
