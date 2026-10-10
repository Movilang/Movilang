# MovieLang — "Harry Potter and the Philosopher's Stone": 16-lesson B1–B2 marathon.
# All sentences are original teaching material; scenes are described, not quoted.
import json

def intro(q, goals, img, btn="Start the lesson"):
    return {"type": "intro", "q": q, "options": goals, "img": img, "tip": btn}
def mc(kind, q, opts, ans, tip, img=None, scene=None, say=None):
    d = {"type": kind, "q": q, "options": opts, "answer": ans, "tip": tip}
    if img: d["img"] = img
    if scene: d["scene"] = scene
    if say: d["say"] = say
    return d
def match(q, pairs, tip, img=None):
    d = {"type": "match", "q": q, "options": [a + "=" + b for a, b in pairs], "tip": tip}
    if img: d["img"] = img
    return d
def order(q, sentence, tip):
    return {"type": "order", "q": q, "options": sentence.split(), "tip": tip}
def typ(q, answers, tip, scene=None, say=None):
    d = {"type": "type", "q": q, "options": answers, "tip": tip}
    if scene: d["scene"] = scene
    if say: d["say"] = say
    return d
def tf(q, true, tip, scene=None):
    d = {"type": "tf", "q": q, "options": ["True", "False"], "answer": 0 if true else 1, "tip": tip}
    if scene: d["scene"] = scene
    return d
def speak(q, line, tip):
    return {"type": "speaking", "q": q, "say": line, "tip": tip}
def final(q, minw, tip):
    return {"type": "final", "q": q, "answer": minw, "tip": tip}

L = []
def lesson(num, title, title_pl, grammar, scene, scene_pl, tasks):
    L.append({"num": num, "title": title, "title_pl": title_pl, "grammar": grammar, "scene": scene, "scene_pl": scene_pl, "tasks": tasks})

# ---------------------------------------------------------------- 1 (free trial)
lesson(1, "Хлопчик під сходами", "Chłopiec pod schodami", "Present Simple vs Present Continuous",
 "Звичайний будинок у передмісті. Хлопчик живе в комірчині під сходами, а родина святкує день народження кузена.",
 "Zwyczajny dom na przedmieściach. Chłopiec mieszka w komórce pod schodami, a rodzina świętuje urodziny kuzyna.",
 [
  intro("Welcome to your first MovieLang lesson! In 10 minutes you will step into the opening scenes of the story.",
        ["Learn 8 words for family life and feelings", "Hear real-speed English and catch key phrases",
         "Master Present Simple vs Present Continuous in context", "Say your first lines out loud like the characters"],
        "stairs", "Start the free lesson"),
  match("Match the words from the scene with their meanings.",
        [("cupboard", "a small room for storing things"), ("cousin", "your aunt's or uncle's child"),
         ("spoiled", "given too much, so behaves badly"), ("ordinary", "normal, nothing special"),
         ("chores", "boring jobs in the house")],
        "These five words describe the world Harry lives in before the magic starts.", "stairs"),
  mc("vocabulary", "The family wants to look <b>perfectly normal</b>. Which word means the same?",
     ["ordinary", "strange", "magical", "famous"], 0,
     "'Ordinary' = normal, typical. The opposite in this story is 'extraordinary'."),
  mc("listening", "Listen. What is the aunt asking Harry to do?",
     ["Wake up and make breakfast", "Go to school early", "Clean his cousin's room", "Open the presents"], 0,
     "'Get up' and 'cook' are typical morning chores. Notice how fast the order sounds!",
     say="Up! Get up now and come and cook the breakfast. And don't burn anything today."),
  mc("grammar", "Every morning Harry ____ breakfast for the whole family.",
     ["makes", "is making", "make", "made"], 0,
     "A routine or habit → Present Simple: he makes. Signal words: every morning, usually, always."),
  mc("grammar", "Look! Dudley ____ his birthday presents and he isn't happy.",
     ["counts", "is counting", "count", "has count"], 1,
     "'Look!' shows an action happening right now → Present Continuous: is counting."),
  order("Put the words in the right order to describe Harry's life.",
        "Harry doesn't have a real bedroom", "Negative Present Simple: subject + doesn't + base verb."),
  typ("Type the missing word: Harry sleeps in a small cupboard ____ the stairs.",
      ["under", "beneath", "below"], "Preposition of place: under / beneath the stairs."),
  tf("Harry's cousin gets fewer presents this year than last year, and he is angry about it.", True,
     "He counts them and finds there are fewer than last year, so he complains loudly.",
     scene="At breakfast, the cousin counts a big pile of presents."),
  speak("Repeat the sentence with natural rhythm. Stress the words in CAPITALS: I'm NOT ALLOWED to ask QUESTIONS here.",
        "I'm not allowed to ask questions here.",
        "'Not allowed to' = it is forbidden. Great phrase for talking about rules."),
 ])

# ---------------------------------------------------------------- 2
lesson(2, "Пригода в зоопарку", "Przygoda w zoo", "Past Simple vs Past Continuous",
 "Родина бере хлопчика до зоопарку. Біля скла з великою змією стається щось дивне: скло раптом зникає.",
 "Rodzina zabiera chłopca do zoo. Przy szybie z wielkim wężem dzieje się coś dziwnego: szkło nagle znika.",
 [
  match("Match the zoo words.", [("reptile house", "building for snakes and lizards"), ("glass", "the clear wall of a tank"),
        ("to hiss", "to make a long 'sss' sound"), ("to vanish", "to disappear suddenly"), ("to escape", "to get free")],
        "You need these to retell the zoo scene.", "snake"),
  mc("grammar", "Harry ____ to the snake when the glass suddenly disappeared.",
     ["talked", "was talking", "talks", "has talked"], 1,
     "Longer background action (was talking) interrupted by a short event (disappeared).", img="snake"),
  mc("grammar", "While Dudley was pressing his face to the glass, the snake ____ out.",
     ["was sliding", "slid", "slides", "has slid"], 1, "Short completed event in the past → Past Simple: slid."),
  mc("listening", "Listen. Where is the snake originally from, according to the sign?",
     ["Brazil", "Egypt", "Australia", "India"], 0, "The sign says it was bred in the zoo, but the species comes from Brazil.",
     say="This snake was born here at the zoo, but its family originally comes from Brazil."),
  typ("Past Simple of 'fall': Dudley ____ into the water.", ["fell"], "fall → fell → fallen (irregular)."),
  tf("Harry knew he had magic powers at the zoo.", False, "He had no idea. He only realised later that strange things happened around him."),
  order("Order the words to make a Past Continuous question.", "What were you doing when it happened", "Question: What + were/was + subject + -ing?"),
  speak("Tell it like a story. Repeat: I was just standing there when the glass disappeared!",
        "I was just standing there when the glass disappeared!", "Past Continuous + when + Past Simple = perfect storytelling pattern."),
 ])

# ---------------------------------------------------------------- 3
lesson(3, "Листи нізвідки", "Listy znikąd", "Passive voice (past)",
 "Хлопчику починають приходити листи. Дядько їх знищує, але наступного дня листів стає дедалі більше.",
 "Do chłopca zaczynają przychodzić listy. Wuj je niszczy, ale następnego dnia listów jest coraz więcej.",
 [
  mc("vocabulary", "A letter is closed with red wax. What is the wax called?",
     ["a seal", "a stamp", "a ribbon", "a label"], 0, "A seal is wax pressed with a symbol. A stamp is what you pay postage with.", img="letter"),
  match("Match the verbs.", [("to deliver", "to bring post to a place"), ("to tear up", "to rip into pieces"),
        ("to hide", "to put where no one can see"), ("to board up", "to cover with wooden planks"), ("to flood", "to fill completely")],
        "Uncle tries everything: he hides, tears up and even boards up the letterbox.", "letter"),
  mc("grammar", "Hundreds of letters ____ through the chimney.",
     ["were sent", "sent", "was sent", "are send"], 0, "Passive, past, plural: were + past participle (sent)."),
  mc("grammar", "The first letter ____ by Uncle Vernon before Harry could read it.",
     ["was taken", "took", "was took", "is taken"], 0, "was + past participle. Take → took → taken."),
  typ("Make it passive: Someone delivered the letters by owl. → The letters were ____ by owl.",
      ["delivered"], "were + delivered (past participle)."),
  order("Order the words (passive).", "The house was filled with letters", "Subject + was + past participle + with..."),
  mc("listening", "Listen. Where is the letter addressed to?",
     ["The cupboard under the stairs", "The smallest bedroom", "The kitchen", "The garden shed"], 0,
     "The address is so exact that it shows someone knows where Harry sleeps.",
     say="Mr H. Potter, The Cupboard under the Stairs, Number Four."),
  tf("The family stayed at home until the letters stopped.", False, "They ran away to a hotel and then to a tiny house on a rock in the sea."),
 ])

# ---------------------------------------------------------------- 4
lesson(4, "Хранитель ключів", "Strażnik kluczy", "Reported speech",
 "Штормова ніч на острові. Велетень вибиває двері, приносить торт і розповідає хлопчику правду про його батьків.",
 "Burzowa noc na wyspie. Olbrzym wyważa drzwi, przynosi tort i opowiada chłopcu prawdę o jego rodzicach.",
 [
  intro("A giant knocks on the door at midnight. Today you learn to report what people said.",
        ["Report statements: he said that…", "Report questions: she asked if…", "Shift tenses back correctly"], "cake", "Let's go"),
  mc("grammar", "Hagrid: 'You are a wizard.' → Hagrid told Harry that he ____ a wizard.",
     ["is", "was", "were", "has been"], 1, "Reported speech: present → past (are → was).", img="cake"),
  mc("grammar", "Harry: 'Are you sure?' → Harry asked if Hagrid ____ sure.",
     ["is", "was", "were being", "be"], 1, "Yes/no questions: asked + if/whether + subject + past verb."),
  typ("Uncle: 'I won't pay for that school.' → Uncle said that he ____ pay for that school.",
      ["wouldn't", "would not"], "will → would; won't → wouldn't."),
  match("Match the reporting verbs.", [("to admit", "to agree something is true, unwillingly"), ("to promise", "to say you will surely do it"),
        ("to refuse", "to say you won't do it"), ("to explain", "to make something clear"), ("to warn", "to say something bad may happen")],
        "Better than just 'said' — these verbs make your stories vivid."),
  order("Order the reported question.", "He asked who his parents really were", "In reported questions, NO question word order: who + subject + verb."),
  mc("listening", "Listen. What did Hagrid bake for Harry?", ["A birthday cake", "Bread", "Cookies", "A pie"], 0,
     "It's a little squashed, but made with love.", say="I made you a birthday cake. It got a bit squashed on the way, but it should still taste good."),
  speak("Report it! Repeat: He told me that I had been famous all my life.", "He told me that I had been famous all my life.",
        "Past perfect in reported speech: had been."),
 ])

# ---------------------------------------------------------------- 5
lesson(5, "Чарівна вулиця покупок", "Magiczna ulica zakupów", "Quantifiers: too / enough / a lot of / few",
 "Велетень веде хлопчика на приховану вулицю з крамницями: банк, мантії, книги, котли.",
 "Olbrzym prowadzi chłopca na ukrytą ulicę ze sklepami: bank, szaty, książki, kociołki.",
 [
  mc("vocabulary", "A magical street full of shops. A place where money is kept safely is a…",
     ["bank", "market", "library", "pharmacy"], 0, "The bank is run by goblins and has very deep vaults.", img="alley"),
  match("Shopping list: match.", [("robes", "long clothes for school"), ("cauldron", "a big pot for potions"),
        ("quill", "a feather pen"), ("parchment", "old-style paper"), ("vault", "a safe room in a bank")], "You will see all of these at the school too."),
  mc("grammar", "Harry has never had ____ money to buy what he wants.",
     ["enough", "too", "too much", "a few"], 0, "enough + noun = the right amount. 'Too' needs an adjective: too expensive."),
  mc("grammar", "The robes were ____ long, so the tailor shortened them.",
     ["enough", "too", "much", "few"], 1, "too + adjective = more than needed."),
  typ("Complete: There were so ____ people in the street that Harry got lost for a moment.", ["many"], "many + countable plural (people)."),
  tf("Harry discovered that his parents had left him nothing.", False, "There was a vault full of gold coins waiting for him."),
  order("Order the words.", "We don't have enough time to buy everything", "enough + noun + to-infinitive."),
  speak("Shopping English. Repeat: Excuse me, how much is this? It's a bit too expensive for me.",
        "Excuse me, how much is this? It's a bit too expensive for me.", "A polite, useful phrase for real shops."),
 ])

# ---------------------------------------------------------------- 6
lesson(6, "Паличка обирає чарівника", "Różdżka wybiera czarodzieja", "Relative clauses (who / which / where / whose)",
 "Старовинна крамниця паличок. Хлопчик пробує кілька, доки одна не обирає його.",
 "Stary sklep z różdżkami. Chłopiec próbuje kilku, aż jedna wybiera jego.",
 [
  mc("grammar", "This is the shop ____ every young wizard buys a wand.",
     ["which", "where", "who", "whose"], 1, "Place → where.", img="wand"),
  mc("grammar", "The wand ____ chose Harry has a very special core.",
     ["who", "which", "where", "whose"], 1, "Thing → which / that."),
  mc("grammar", "The old man ____ shop is full of boxes remembers every wand he has sold.",
     ["who", "which", "whose", "that"], 2, "Possession → whose (his shop → whose shop)."),
  typ("Complete with one word: Harry is the boy ____ survived.", ["who", "that"], "Person → who / that."),
  match("Match the descriptions.", [("wand-maker", "a person who makes wands"), ("dusty", "covered with fine dirt"),
        ("core", "the magic material inside"), ("curious", "strange, surprising"), ("brother wand", "a wand which shares the same core")],
        "Notice how definitions themselves use relative clauses!"),
  order("Make one sentence with a relative clause.", "The owl which Hagrid bought is snowy white", "Relative clause in the middle: The owl (which Hagrid bought) is…"),
  tf("The first wand Harry tried was perfect for him.", False, "Several wands caused chaos before the right one chose him."),
  speak("Describe like a pro: Repeat: It's the kind of place where you feel the magic in the air.",
        "It's the kind of place where you feel the magic in the air.", "'The kind of place where…' is a great B2 phrase."),
 ])

# ---------------------------------------------------------------- 7
lesson(7, "Платформа дев'ять і три чверті", "Peron dziewięć i trzy czwarte", "Modals of deduction: must / might / can't",
 "Вокзал у Лондоні. Хлопчик шукає неіснуючу платформу, а потім у поїзді знайомиться з новим другом.",
 "Dworzec w Londynie. Chłopiec szuka nieistniejącego peronu, a potem w pociągu poznaje nowego przyjaciela.",
 [
  intro("Platform nine and three-quarters doesn't exist… or does it? Today: guessing and deducing.",
        ["must = I'm almost sure it's true", "can't = I'm sure it's impossible", "might / could = maybe"], "train", "Board the train"),
  mc("grammar", "There's no platform between 9 and 10. It ____ be real!",
     ["must", "can't", "should", "has to"], 1, "Deduction that something is impossible → can't be.", img="train"),
  mc("grammar", "That family is pushing trolleys with owls. They ____ be going to the same school.",
     ["must", "can't", "mustn't", "needn't"], 0, "Strong evidence → must be."),
  mc("grammar", "Ron isn't sure about the sweets: 'This one ____ taste like earwax. Be careful!'",
     ["might", "must", "can't", "has"], 0, "Possibility → might."),
  typ("Complete: The trolley lady sells sweets, so she ____ be very popular with the students. (strong guess)",
      ["must"], "must = logical certainty."),
  match("Travel vocabulary.", [("platform", "where you get on a train"), ("trolley", "a cart for luggage"),
        ("compartment", "a small room in a train"), ("luggage", "bags and cases"), ("ticket inspector", "checks your ticket")], "Useful for real trips too!"),
  mc("listening", "Listen. What does Ron ask?", ["Is anyone sitting there?", "Where is the train?", "Do you have food?", "What time is it?"], 0,
     "Polite way to ask for a seat.", say="Excuse me, do you mind? Is anyone sitting there? Everywhere else is full."),
  speak("Deduce out loud. Repeat: You must be joking! That can't be the right platform.",
        "You must be joking! That can't be the right platform.", "Natural reaction + deduction."),
 ])

# ---------------------------------------------------------------- 8
lesson(8, "Капелюх розподілу", "Tiara przydziału", "Second conditional",
 "Великий зал зі свічками під стелею. Старий капелюх вирішує, до якого гуртожитку піде кожен учень.",
 "Wielka Sala ze świecami pod sufitem. Stara tiara decyduje, do którego domu trafi każdy uczeń.",
 [
  match("Personality adjectives.", [("brave", "not afraid of danger"), ("loyal", "always supports friends"),
        ("ambitious", "really wants to succeed"), ("wise", "clever and sensible"), ("cunning", "clever in a tricky way")],
        "Each school house values different qualities.", "hat"),
  mc("grammar", "If I ____ the Sorting Hat, I would put Harry in the bravest house.",
     ["am", "were", "will be", "had been"], 1, "Second conditional: If + past (were) + would.", img="hat"),
  mc("grammar", "If Harry ____ to the hat's first idea, he would join a different house.",
     ["listens", "listened", "will listen", "has listened"], 1, "Unreal present/future: If + Past Simple."),
  typ("Complete: What house would you choose if you ____ (can) choose?", ["could"], "can → could in second conditional."),
  order("Order the conditional sentence.", "I would feel nervous if everyone watched me", "would + verb … if + past."),
  tf("Hermione hopes to be in the house that values courage.", True, "She has read about the houses and has strong opinions."),
  mc("vocabulary", "The ceiling looks like the night sky. It is…", ["enchanted", "painted", "broken", "empty"], 0, "Enchanted = under a magic spell."),
  speak("Your turn. Repeat and then say it about yourself: If I were a student there, I would want to be brave.",
        "If I were a student there, I would want to be brave.", "Change the adjective to describe YOU."),
 ])

# ---------------------------------------------------------------- 9
lesson(9, "Урок зілля", "Lekcja eliksirów", "Phrasal verbs & instructions",
 "Холодний підвал, суворий учитель. Він ставить хлопчику складні питання на першому ж уроці.",
 "Zimne lochy, surowy nauczyciel. Na pierwszej lekcji zadaje chłopcu trudne pytania.",
 [
  mc("vocabulary", "A teacher who is very strict and unfriendly is…", ["harsh", "kind", "relaxed", "funny"], 0, "Harsh = severe, unkind.", img="potion"),
  match("Phrasal verbs from the classroom.", [("to pick on", "to treat someone unfairly"), ("to look up", "to find information"),
        ("to carry on", "to continue"), ("to point out", "to show or mention"), ("to put off", "to delay")],
        "Phrasal verbs are everywhere in natural English!"),
  mc("grammar", "Don't worry, just ____ with your potion. You're doing fine.", ["carry on", "put off", "pick on", "look up"], 0, "carry on = continue."),
  mc("grammar", "If you don't know the answer, ____ it ____ in the book.", ["look / up", "pick / on", "carry / on", "point / out"], 0, "Separable phrasal verb: look it up."),
  order("Instructions: order the words.", "Stir the potion slowly and then add the leaves", "Imperatives for instructions."),
  typ("Complete: Why does the teacher always pick ____ Harry?", ["on"], "pick on someone."),
  tf("Harry knew all the answers in his first potions lesson.", False, "He didn't — and Hermione's hand was up the whole time."),
  speak("Give an instruction. Repeat: First, read the instructions carefully. Then, add the ingredients one by one.",
        "First, read the instructions carefully. Then, add the ingredients one by one.", "Sequencers: first, then, after that, finally."),
 ])

# ---------------------------------------------------------------- 10
lesson(10, "Перший урок польотів", "Pierwsza lekcja latania", "Obligation: must / have to / mustn't / don't have to",
 "Учні вперше тримають мітли. Один хлопчик падає, а інший забирає його річ і злітає високо в небо.",
 "Uczniowie pierwszy raz trzymają miotły. Jeden chłopiec spada, a drugi zabiera jego rzecz i wzlatuje wysoko.",
 [
  mc("grammar", "Students ____ fly while the teacher is away. It's against the rules!",
     ["mustn't", "don't have to", "must", "needn't"], 0, "mustn't = it is forbidden.", img="broom"),
  mc("grammar", "You ____ be an expert on your first day. Just try your best.",
     ["mustn't", "don't have to", "have to", "must"], 1, "don't have to = it's not necessary."),
  mc("grammar", "Yesterday, Neville ____ go to the hospital wing after his fall.",
     ["must", "had to", "has to", "mustn't"], 1, "Past obligation → had to (must has no past form)."),
  typ("Complete: Everyone ____ to hold the broom with their right hand. (obligation, present)", ["has", "needs"], "has to = rule/obligation."),
  match("Flying words.", [("to hover", "to stay in the air in one place"), ("to dive", "to go down fast"),
        ("to grab", "to take quickly"), ("to land", "to come back to the ground"), ("a natural", "someone born with a talent")],
        "Harry turns out to be a natural!"),
  tf("Harry caught a glass ball after a long dive, and a teacher saw it.", True, "Instead of punishment, he got a place on the team."),
  order("Order the rule.", "You must keep your feet on the ground", "must + base verb."),
  speak("Talk about rules in your life. Repeat: At my school we had to wear a uniform, but we didn't have to stand up.",
        "At my school we had to wear a uniform, but we didn't have to stand up.", "Past obligation vs no obligation."),
 ])

# ---------------------------------------------------------------- 11
lesson(11, "Троль у підземеллі", "Troll w lochach", "Past Perfect",
 "Свято Гелловіну. У школу пробрався троль, а одна учениця залишилася сама у вбиральні.",
 "Halloween. Do szkoły dostał się troll, a jedna uczennica została sama w łazience.",
 [
  intro("Halloween night — and something huge is in the castle. Today: the tense of 'what had already happened'.",
        ["Past Perfect: had + past participle", "Order two past events clearly", "Tell a dramatic story in English"], "troll", "Enter the castle"),
  mc("grammar", "When the boys arrived, the troll ____ already ____ into the bathroom.",
     ["had / gone", "has / gone", "was / going", "did / go"], 0, "The earlier action → had gone.", img="troll"),
  mc("grammar", "Hermione was crying because Ron ____ something unkind earlier that day.",
     ["said", "had said", "has said", "was saying"], 1, "Earlier past → Past Perfect: had said."),
  typ("Complete: By the time the teachers came, the boys ____ already defeated the troll. (have)", ["had"], "had + defeated."),
  match("Halloween vocabulary.", [("feast", "a big special meal"), ("dungeon", "an underground room"),
        ("to faint", "to suddenly lose consciousness"), ("club", "a heavy wooden weapon"), ("to knock out", "to make unconscious")],
        "Useful for retelling the scene."),
  order("Order the sentence.", "They became friends after they had faced the troll together", "after + Past Perfect."),
  tf("After that night, Hermione became friends with Harry and Ron.", True, "Facing danger together changed everything."),
  speak("Dramatic storytelling. Repeat: I had never seen anything so big in my whole life!",
        "I had never seen anything so big in my whole life!", "had never + past participle = strong emotion."),
 ])

# ---------------------------------------------------------------- 12
lesson(12, "Перший матч", "Pierwszy mecz", "Comparatives, superlatives & adverbs",
 "Стадіон, обручі на високих стовпах, глядачі на трибунах. Хлопчик грає свій перший матч у ролі ловця.",
 "Stadion, obręcze na wysokich słupach, kibice na trybunach. Chłopiec gra swój pierwszy mecz jako szukający.",
 [
  mc("grammar", "Harry is the ____ Seeker the team has had in a century.", ["youngest", "younger", "most young", "young"], 0, "One-syllable adjective → -est.", img="pitch"),
  mc("grammar", "The golden ball moves ____ than any other ball.", ["fast", "faster", "fastest", "more fast"], 1, "Comparative + than."),
  mc("grammar", "His broom started to shake ____ during the match.", ["dangerous", "dangerously", "danger", "more dangerous"], 1, "Adverb describes HOW it shook."),
  typ("Complete: This was the ____ (exciting) match of the season.", ["most exciting"], "Long adjective → the most + adj."),
  match("Sports vocabulary.", [("pitch", "the field where you play"), ("score", "to get points"),
        ("referee", "the person who controls the game"), ("crowd", "the people watching"), ("cheat", "to break rules to win")],
        "Works for football too!"),
  tf("Harry caught the golden ball with his hands.", False, "He almost swallowed it — and it still counted!"),
  order("Order the sentence.", "It was the best day of his life so far", "the best = superlative of good."),
  speak("Commentate! Repeat: He's flying faster and faster — what an incredible catch!",
        "He's flying faster and faster — what an incredible catch!", "faster and faster = increasing speed."),
 ])

# ---------------------------------------------------------------- 13
lesson(13, "Дзеркало бажань", "Zwierciadło pragnień", "Wishes: I wish / If only",
 "Порожній клас уночі. Хлопчик знаходить дзеркало, яке показує не відображення, а найглибше бажання.",
 "Pusta sala w nocy. Chłopiec znajduje lustro, które pokazuje nie odbicie, lecz najgłębsze pragnienie.",
 [
  mc("grammar", "Harry wishes he ____ his parents.", ["knows", "knew", "will know", "has known"], 1, "Wish about the present → past simple.", img="mirror"),
  mc("grammar", "Ron wishes he ____ more successful than his brothers.", ["is", "were", "will be", "be"], 1, "wish + were (formal, correct for all persons)."),
  mc("grammar", "If only I ____ that mirror! Now I can't stop thinking about it. (regret about the past)", ["didn't find", "hadn't found", "don't find", "wouldn't find"], 1, "Regret about the past → If only + Past Perfect."),
  typ("Complete: I wish it ____ (be) Christmas every day.", ["were", "was"], "were is more formal; was is common in speech."),
  match("Feelings.", [("longing", "a strong wish for something"), ("lonely", "sad because alone"),
        ("obsessed", "can't stop thinking about something"), ("grateful", "thankful"), ("homesick", "missing home or family")],
        "Emotions make your English richer."),
  tf("The headmaster advises Harry to keep visiting the mirror every night.", False, "He warns that living in dreams means forgetting to live."),
  order("Order the advice from the headmaster (in our words).", "Real life is more important than dreams",
        "The idea of the scene: don't get lost in dreams."),
  speak("Make a wish. Repeat, then make your own: I wish I could speak English as fluently as a native speaker.",
        "I wish I could speak English as fluently as a native speaker.", "wish + could = ability you'd like to have."),
 ])

# ---------------------------------------------------------------- 14
lesson(14, "Заборонений ліс", "Zakazany Las", "Third conditional",
 "Покарання вночі в темному лісі. Хлопчики бачать щось страшне, і їх рятує кентавр.",
 "Kara w nocy w ciemnym lesie. Chłopcy widzą coś strasznego, a ratuje ich centaur.",
 [
  intro("A night in the Forbidden Forest. Today: imagining how the past could have been different.",
        ["Third conditional: If + had done, would have done", "Talk about regrets and lucky escapes", "Night & forest vocabulary"], "forest", "Into the forest"),
  mc("grammar", "If they ____ out after midnight, they wouldn't have got a detention.",
     ["didn't go", "hadn't gone", "wouldn't go", "haven't gone"], 1, "If + Past Perfect…", img="forest"),
  mc("grammar", "If the centaur hadn't arrived, something terrible ____.",
     ["would happen", "would have happened", "had happened", "will happen"], 1, "…would have + past participle."),
  typ("Complete: If Harry had stayed in bed, he ____ have seen the hooded figure.", ["wouldn't", "would not"], "wouldn't have seen."),
  match("Forest vocabulary.", [("detention", "a punishment at school"), ("lantern", "a lamp you carry"),
        ("hooded", "wearing a hood"), ("to creep", "to move slowly and quietly"), ("silver blood", "magic creature's blood (unicorn)")],
        "Atmosphere words for scary stories."),
  order("Order the third conditional.", "We would have been lost if you hadn't helped us", "would have + pp … if + had + pp."),
  tf("The boys were in the forest as a punishment.", True, "It was their detention."),
  speak("Regret and relief. Repeat: If you hadn't come, we would have been in serious trouble.",
        "If you hadn't come, we would have been in serious trouble.", "Very natural way to say thank you after help."),
 ])

# ---------------------------------------------------------------- 15
lesson(15, "Крізь люк", "Przez klapę", "Present Perfect vs Past Simple",
 "Троє друзів проходять випробування під школою: гігантські шахи, загадка з зіллям і вогонь.",
 "Trójka przyjaciół przechodzi próby pod szkołą: gigantyczne szachy, zagadka z eliksirami i ogień.",
 [
  mc("grammar", "Ron has played chess since he was a child, but he ____ a game like this before.",
     ["never played", "has never played", "had never play", "didn't ever"], 1, "Life experience up to now → Present Perfect.", img="chess"),
  mc("grammar", "Last night, the three friends ____ through the trapdoor.", ["have climbed", "climbed", "climb", "were climb"], 1, "Finished time (last night) → Past Simple."),
  mc("grammar", "Hermione: 'I ____ the riddle! It's the smallest bottle.'", ["solved", "have solved", "solve", "had solved"], 1, "Result now, no time given → Present Perfect."),
  typ("Complete: Have you ever ____ chess? (play)", ["played"], "Have you ever + past participle = experience question."),
  match("Challenge vocabulary.", [("trapdoor", "a door in the floor"), ("riddle", "a puzzle in words"),
        ("sacrifice", "giving something up for others"), ("to checkmate", "to win at chess"), ("flames", "fire")],
        "Words of the final adventure."),
  tf("Ron lets himself be taken in the chess game so Harry can go on.", True, "A real sacrifice for his friend."),
  order("Order the sentence.", "I have never been so scared in my life", "Present Perfect + never + superlative feeling."),
  speak("Your experience. Repeat, then make it true for you: I've been to London, but I've never seen a real castle.",
        "I've been to London, but I've never seen a real castle.", "been to = visited and came back."),
 ])

# ---------------------------------------------------------------- 16
lesson(16, "Фінал: камінь і твоя історія", "Finał: kamień i twoja historia", "Narrative tenses — review",
 "Остання зустріч біля дзеркала, червоний камінь у кишені і прощальне свято. Ти розповідаєш історію сам.",
 "Ostatnie spotkanie przy lustrze, czerwony kamień w kieszeni i pożegnalna uczta. Opowiadasz historię sam.",
 [
  intro("The final lesson! Put together everything you learned and tell the story in your own words.",
        ["Review narrative tenses", "Use 10+ words from the marathon", "Write and record your own retelling", "Get your MovieLang certificate"], "stone", "Begin the finale"),
  mc("grammar", "Harry looked in the mirror and suddenly felt that the stone ____ into his pocket.",
     ["dropped", "had dropped", "has dropped", "was drop"], 1, "Earlier past event → had dropped.", img="stone"),
  mc("grammar", "While the teacher ____, Harry was thinking about his mother.", ["talked", "was talking", "has talked", "talks"], 1, "Background action → Past Continuous."),
  match("Review: match the grammar to the example.", [("Past Perfect", "had already left"), ("Second conditional", "If I were you"),
        ("Passive", "was delivered by owl"), ("Reported speech", "He said he was tired"), ("Wish", "I wish I knew")], "Everything you practised in 16 lessons!"),
  mc("quiz", "Which school house wins the cup at the end?", ["The house of the brave", "The house of the wise", "The house of the loyal", "The house of the cunning"], 0,
     "Last-minute points for courage and friendship."),
  tf("Harry goes back to his aunt and uncle for the summer.", True, "But now he knows who he really is."),
  speak("Final speaking. Repeat: This story taught me that friendship and courage matter more than anything.",
        "This story taught me that friendship and courage matter more than anything.", "Use this as the last line of your retelling."),
  final("FINAL PROJECT: Write your favourite scene from the film (100–150 words). Use at least: 2 Past Perfect forms, 1 conditional, 1 passive, and 5 words from the marathon.",
        100, "Saved! Your teacher (or you) can review it in your account. Congratulations on finishing the marathon!"),
 ])

print(json.dumps(L, ensure_ascii=False))
