# Тренування (6 речень) — англійська версія «Тачок».
D = {}
def r(q, opts, e):
    p = e.split("|"); p = p if len(p) == 3 else [e, e, e]
    return (q, opts, 0, tuple(p))
D[1] = [r("I ____ McQueen.", ["am", "is", "are"], "I → am."), r("He ____ fast.", ["is", "are", "am"], "He → is."),
        r("We ____ fans.", ["are", "is", "am"], "We → are."), r("Mack ____ a truck.", ["is", "are", "am"], "He → is."),
        r("You ____ my friend.", ["are", "is", "am"], "You → are."), r("They ____ racers.", ["are", "is", "am"], "They → are.")]
D[2] = [r("I ____ tired.", ["am not", "not am", "isn't"], "I'm not."), r("He ____ happy.", ["isn't", "aren't", "not"], "He isn't."),
        r("____ you ready?", ["Are", "Is", "Am"], "Are you…?"), r("____ he a star?", ["Is", "Are", "Am"], "Is he…?"),
        r("They ____ here.", ["aren't", "isn't", "not"], "They aren't."), r("____ I late?", ["Am", "Is", "Are"], "Am I…?")]
D[3] = [r("This is ____ trailer.", ["my", "me", "I"], "My + noun."), r("McQueen is ____ star.", ["our", "us", "we"], "Our + noun."),
        r("Mack is ____ truck.", ["McQueen's", "McQueen", "McQueens"], "'s = whose."), r("Is this ____ cup?", ["your", "you", "yours"], "Your + noun."),
        r("Sally loves ____ motel.", ["her", "she", "his"], "She → her."), r("Doc and ____ garage.", ["his", "he", "her"], "He → his.")]
D[4] = [r("____ car is red.", ["This", "These", "Those"], "One, near → this."), r("____ tires are new.", ["These", "This", "That"], "Many, near → these."),
        r("____ mountain is far.", ["That", "Those", "These"], "One, far → that."), r("Look at ____ stars!", ["those", "that", "this"], "Many, far → those."),
        r("Two ____.", ["cars", "car", "cares"], "Plural + -s."), r("Three ____.", ["boxes", "boxs", "box"], "-x → -es.")]
D[5] = [r("I ____ got a sponsor.", ["have", "has", "am"], "I → have."), r("He ____ got a trailer.", ["has", "have", "is"], "He → has."),
        r("She hasn't ____ a car.", ["got", "get", "gets"], "Hasn't got."), r("____ you got a friend?", ["Have", "Has", "Do"], "Have you got…?"),
        r("We've got ____ fans.", ["many", "much", "a"], "Many + plural."), r("They ____ got any money.", ["haven't", "hasn't", "don't"], "They haven't.")]
D[7] = [r("There ____ a café.", ["is", "are", "be"], "One → is."), r("There ____ two shops.", ["are", "is", "am"], "Many → are."),
        r("There isn't ____ hotel.", ["a", "some", "many"], "Isn't a."), r("____ there a road?", ["Is", "Are", "Do"], "Is there…?"),
        r("There aren't ____ cars.", ["any", "a", "some"], "Aren't any."), r("Are there ____ tourists?", ["any", "a", "much"], "Any in questions.")]
D[8] = [r("The car is ____ the garage.", ["in", "on", "at"], "In = inside."), r("The cone is ____ the road.", ["on", "in", "under"], "On = on top."),
        r("Mater sleeps ____ the sign.", ["under", "in", "on"], "Under."), r("The café is ____ the motel.", ["next to", "next", "near to"], "Next to."),
        r("Doc's garage is ____ the court.", ["behind", "behind of", "back"], "Behind."), r("The town is ____ the mountains.", ["between", "among of", "at"], "Between.")]
D[9] = [r("____ the car!", ["Stop", "Stops", "Stopping"], "Imperative = base verb."), r("____ go so fast!", ["Don't", "No", "Not"], "Don't + verb."),
        r("____ go!", ["Let's", "Let", "Lets"], "Let's + verb."), r("Please ____ down.", ["slow", "slows", "to slow"], "Base verb."),
        r("Don't ____!", ["shout", "shouts", "shouting"], "Don't + verb."), r("Let's ____ the road.", ["fix", "fixing", "to fix"], "Let's + verb.")]
D[10] = [r("Mater ____ drive backwards.", ["can", "cans", "can to"], "Can + verb."), r("I can't ____ Bessie.", ["pull", "pulls", "to pull"], "Can't + verb."),
         r("____ you help me?", ["Can", "Do", "Are"], "Can you…?"), r("He ____ swim.", ["can't", "don't can", "not can"], "Can't."),
         r("She can ____ well.", ["drive", "drives", "driving"], "No -s."), r("Can they ____?", ["race", "races", "to race"], "Can + verb.")]
D[11] = [r("Mater ____ in a junkyard.", ["lives", "live", "living"], "He → -s."), r("I ____ cars every day.", ["tow", "tows", "towing"], "I → no -s."),
         r("Flo ____ fuel.", ["sells", "sell", "selling"], "She → -s."), r("They ____ in town.", ["work", "works", "working"], "They → no -s."),
         r("Doc ____ the town.", ["watches", "watchs", "watch"], "-ch → -es."), r("He ____ a lot.", ["talks", "talk", "talking"], "He → -s.")]
D[13] = [r("____ you like my motel?", ["Do", "Does", "Are"], "You → do."), r("____ Doc like racing?", ["Does", "Do", "Is"], "He → does."),
         r("He doesn't ____ here.", ["live", "lives", "living"], "Doesn't + verb."), r("I ____ like waiting.", ["don't", "doesn't", "not"], "I → don't."),
         r("Does she ____ a car?", ["have", "has", "having"], "Does + base verb."), r("They ____ know.", ["don't", "doesn't", "aren't"], "They → don't.")]
D[14] = [r("Sarge ____ gets up early.", ["always", "always is", "is always"], "Adverb before verb."), r("Flo is ____ busy.", ["often", "often is", "oftens"], "After be."),
         r("I ____ drink tea.", ["never", "never don't", "not never"], "Never + verb."), r("He ____ late.", ["is never", "never is", "never are"], "Be + never."),
         r("We ____ play.", ["sometimes", "sometime", "some times"], "Sometimes."), r("Red ____ cries.", ["often", "oftenly", "is often cries"], "Often + verb.")]
D[15] = [r("____ is Doc?", ["Where", "Who", "When"], "Place → where."), r("____ is that car?", ["Who", "Where", "How"], "Person → who."),
         r("____ do you race?", ["Why", "Who", "Which"], "Reason → why."), r("____ is the race?", ["When", "Who", "What"], "Time → when."),
         r("____ are you?", ["How", "What", "Who's"], "How are you?"), r("____ is your name?", ["What", "Who", "Where"], "What's your name?")]
D[16] = [r("Mater loves ____ backwards.", ["driving", "drive", "drives"], "Love + -ing."), r("I hate ____.", ["waiting", "wait", "waits"], "Hate + -ing."),
         r("She likes ____ cars.", ["fixing", "fix", "fixes"], "Like + -ing."), r("Do you enjoy ____?", ["racing", "race", "to racing"], "Enjoy + -ing."),
         r("He doesn't like ____.", ["running", "runing", "run"], "Double n."), r("We love ____.", ["dancing", "danceing", "dance"], "Drop -e.")]
D[17] = [r("McQueen ____ the road now.", ["is fixing", "fixes", "fixing"], "Is + -ing."), r("I ____ working.", ["am", "is", "are"], "I am."),
         r("They are ____.", ["laughing", "laugh", "laughs"], "Are + -ing."), r("____ you listening?", ["Are", "Do", "Is"], "Are you…?"),
         r("She isn't ____.", ["sleeping", "sleep", "sleeps"], "Isn't + -ing."), r("Look! He's ____!", ["driving", "driveing", "drive"], "Drop -e.")]
D[19] = [r("Doc ____ in his garage every day.", ["works", "is working", "work"], "Every day → Simple."), r("Look! Doc ____ now!", ["is racing", "races", "race"], "Now → Continuous."),
         r("I usually ____ tea.", ["drink", "am drinking", "drinks"], "Usually → Simple."), r("Listen! She ____.", ["is singing", "sings", "sing"], "Listen! → Continuous."),
         r("They ____ TV right now.", ["are watching", "watch", "watches"], "Right now → Continuous."), r("He often ____ late.", ["comes", "is coming", "come"], "Often → Simple.")]
D[20] = [r("I'd like ____ apple.", ["an", "a", "some"], "Vowel → an."), r("There's ____ fuel.", ["some", "a", "an"], "Uncountable → some."),
         r("Is there ____ oil?", ["any", "a", "an"], "Questions → any."), r("I haven't got ____ tires.", ["any", "some", "a"], "Negative → any."),
         r("She's got ____ car.", ["a", "an", "any"], "Consonant → a."), r("Would you like ____ water?", ["some", "any", "a"], "Offers → some.")]
D[21] = [r("How ____ tires?", ["many", "much", "lot"], "Countable → many."), r("How ____ fuel?", ["much", "many", "lots"], "Uncountable → much."),
         r("How much ____ it?", ["is", "are", "does"], "How much is it?"), r("How many cars ____ there?", ["are", "is", "be"], "Plural → are."),
         r("I haven't got ____ money.", ["much", "many", "a"], "Uncountable → much."), r("There are ____ shops.", ["many", "much", "a lot"], "Countable → many.")]
D[22] = [r("Sally likes ____.", ["him", "he", "his"], "Object → him."), r("I can see ____.", ["you", "your", "yours"], "Object → you."),
         r("Call ____!", ["me", "I", "my"], "Object → me."), r("He loves ____.", ["her", "she", "hers"], "Object → her."),
         r("Help ____!", ["us", "we", "our"], "Object → us."), r("I know ____.", ["them", "they", "their"], "Object → them.")]
D[23] = [r("The race is ____ Sunday.", ["on", "in", "at"], "Days → on."), r("I get up ____ seven.", ["at", "on", "in"], "Times → at."),
         r("It's hot ____ July.", ["in", "on", "at"], "Months → in."), r("____ the morning.", ["In", "On", "At"], "In the morning."),
         r("____ night.", ["At", "In", "On"], "At night."), r("____ the weekend.", ["At", "In the", "On in"], "At the weekend (UK).")]
D[25] = [r("Doc ____ a champion.", ["was", "were", "is"], "He → was."), r("The fans ____ there.", ["were", "was", "are"], "They → were."),
         r("I ____ in hospital.", ["was", "were", "am"], "I → was."), r("It ____ fair.", ["wasn't", "weren't", "didn't"], "It wasn't."),
         r("____ you surprised?", ["Were", "Was", "Did"], "Were you…?"), r("We ____ tired.", ["were", "was", "are"], "We → were.")]
D[26] = [r("He ____ all night.", ["worked", "work", "works"], "Past → -ed."), r("I ____ the job.", ["finished", "finish", "finishing"], "Past → -ed."),
         r("She ____ at me.", ["smiled", "smileed", "smile"], "-e → -d."), r("They ____ with joy.", ["jumped", "jump", "jumps"], "Past → -ed."),
         r("He didn't ____.", ["stop", "stopped", "stops"], "Didn't + base."), r("We ____ the town.", ["visited", "visit", "visitted"], "Visited.")]
D[27] = [r("He ____ to every shop.", ["went", "goed", "go"], "Go → went."), r("I ____ some fuel.", ["bought", "buyed", "buy"], "Buy → bought."),
         r("She ____ the lights.", ["saw", "seed", "see"], "See → saw."), r("He ____ a surprise.", ["made", "maked", "make"], "Make → made."),
         r("Ramone ____ him paint.", ["gave", "gived", "give"], "Give → gave."), r("We ____ a great time.", ["had", "haved", "have"], "Have → had.")]
D[28] = [r("____ you call them?", ["Did", "Do", "Were"], "Did + you…?"), r("He didn't ____ goodbye.", ["say", "said", "says"], "Didn't + base."),
         r("Did she ____ the news?", ["see", "saw", "sees"], "Did + base."), r("Yes, I ____.", ["did", "do", "was"], "Yes, I did."),
         r("I ____ know.", ["didn't", "don't did", "wasn't"], "Didn't + know."), r("Did they ____ him?", ["find", "found", "finds"], "Did + base.")]
D[29] = [r("I'd like ____ go back.", ["to", "—", "for"], "Would like to + verb."), r("Would you ____ some water?", ["like", "likes", "to like"], "Would you like…?"),
         r("I want ____ win.", ["to", "for", "—"], "Want to + verb."), r("She'd like ____ coffee.", ["a", "to", "an"], "Would like + noun."),
         r("Do you ____ a new car?", ["want", "would", "wants"], "Do you want…?"), r("He ____ like to stay.", ["would", "will", "do"], "He would like.")]
D[31] = [r("The stadium is ____ than the town.", ["bigger", "more big", "biggest"], "Big → bigger."), r("Chick is ____ than McQueen? No!", ["faster", "more fast", "fastest"], "-er."),
         r("The King is ____ experienced.", ["more", "most", "much"], "Long → more."), r("Friends are ____ than fame.", ["better", "gooder", "more good"], "Good → better."),
         r("The town is ____ than the city.", ["quieter", "more quiet er", "quietest"], "-er."), r("It's ____ than yesterday.", ["worse", "badder", "more bad"], "Bad → worse.")]
D[32] = [r("We ____ going to help.", ["are", "is", "am"], "We → are."), r("He's going ____ change the tires.", ["to", "for", "—"], "Going to."),
         r("I'm going to ____.", ["win", "winning", "wins"], "Going to + base."), r("Is it going to ____?", ["rain", "rains", "raining"], "Base verb."),
         r("They ____ going to lose.", ["aren't", "isn't", "don't"], "They aren't."), r("____ you going to race?", ["Are", "Do", "Will"], "Are you going to…?")]
D[33] = [r("I stopped ____ he crashed.", ["because", "so", "but"], "Reason → because."), r("He was angry, ____ he pushed.", ["so", "because", "but"], "Result → so."),
         r("He won, ____ nobody clapped.", ["but", "so", "because"], "Contrast → but."), r("I was tired, ____ I slept.", ["so", "but", "because"], "Result → so."),
         r("I like tea ____ coffee.", ["and", "so", "because"], "Adding → and."), r("She smiled ____ she was happy.", ["because", "so", "but"], "Reason → because.")]
D[34] = [r("____, wake up.", ["First", "Finally", "After"], "Start → First."), r("____ have breakfast.", ["Then", "First then", "Finally first"], "Next → Then."),
         r("After ____, go to school.", ["that", "this then", "it then"], "After that."), r("____, go to bed.", ["Finally", "First", "Then first"], "End → Finally."),
         r("First the race, ____ the party.", ["then", "first", "finally first"], "Then."), r("____ of all, say thank you.", ["First", "Finally", "Then"], "First of all.")]
