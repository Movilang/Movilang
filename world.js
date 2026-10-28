// MoviLang — «Ігровий світ» курсів: фракції, ритуал входу, валюта, колекція, журнал.
// Кожен курс підключається за slug. Курс без запису тут працює як раніше.
// Як додати світ новому курсу — див. README, розділ «Ігровий світ».
// Тексти: {uk, pl, en}. Питання ритуалу — англійською (тренують лексику), підказка — мовою інтерфейсу.
window.MOVILANG_WORLDS = {

  'harry-potter-1': {
    theme: 'hp',
    points: {icon: '⭐', uk: 'бали факультету', pl: 'punkty domu', en: 'house points'},
    ritual: {
      icon: '🎩',
      title: {uk: 'Розподільчий капелюх', pl: 'Tiara Przydziału', en: 'The Sorting Hat'},
      intro: {uk: 'Капелюх ставить п\'ять питань англійською. Відповідай чесно — він бачить тебе наскрізь.', pl: 'Tiara zadaje pięć pytań po angielsku. Odpowiadaj szczerze — ona widzi cię na wylot.', en: 'The Hat asks five questions. Answer honestly: it sees right through you.'},
      reveal: {uk: 'Капелюх вигукує на всю Велику залу:', pl: 'Tiara woła na całą Wielką Salę:', en: 'The Hat shouts across the Great Hall:'},
      questions: [
        {q: 'A troll is loose in the dungeons. What do you do?', hint: {uk: 'Троль вирвався в підземелля. Що ти робиш?', pl: 'Troll uciekł do lochów. Co robisz?', en: ''},
          a: [['I run to help my friend, even without a plan.', 'gryffindor'], ['I find out where the troll is weak first.', 'ravenclaw'], ['I make sure everyone is safe and nobody is left behind.', 'hufflepuff'], ['I use the chaos to get what I need.', 'slytherin']]},
        {q: 'Which subject would you never skip?', hint: {uk: 'Який предмет ти ніколи не пропустиш?', pl: 'Którego przedmiotu nigdy nie opuścisz?', en: ''},
          a: [['Potions, because one drop can change everything.', 'slytherin'], ['Charms, I love learning new spells.', 'ravenclaw'], ['Herbology, plants need patience.', 'hufflepuff'], ['Flying lessons, of course!', 'gryffindor']]},
        {q: 'You find the Mirror of Erised. What do you see?', hint: {uk: 'Ти знайшов Дзеркало Єйналежу. Що ти бачиш?', pl: 'Znajdujesz Zwierciadło Ain Eingarp. Co widzisz?', en: ''},
          a: [['Myself, famous and powerful.', 'slytherin'], ['My family, happy and together.', 'hufflepuff'], ['Myself holding the House Cup.', 'gryffindor'], ['A library with every answer.', 'ravenclaw']]},
        {q: 'Your best friend breaks a school rule. You…', hint: {uk: 'Твій найкращий друг порушив шкільне правило. Ти…', pl: 'Twój najlepszy przyjaciel złamał szkolną zasadę. Ty…', en: ''},
          a: [['…go with them. Rules can wait.', 'gryffindor'], ['…stay loyal and keep the secret.', 'hufflepuff'], ['…ask why the rule exists at all.', 'ravenclaw'], ['…remember it. It might be useful later.', 'slytherin']]},
        {q: 'Choose a path in the Forbidden Forest.', hint: {uk: 'Обери стежку в Забороненому лісі.', pl: 'Wybierz ścieżkę w Zakazanym Lesie.', en: ''},
          a: [['The dark one with strange noises.', 'gryffindor'], ['The one where the centaurs read the stars.', 'ravenclaw'], ['The quiet one, together with Hagrid.', 'hufflepuff'], ['The secret one that nobody else knows.', 'slytherin']]}
      ]
    },
    factions: {
      gryffindor: {icon: '🦁', color: '#c4302b', uk: 'Ґрифіндор', pl: 'Gryffindor', en: 'Gryffindor', motto: {uk: 'Сміливість і відвага', pl: 'Odwaga i męstwo', en: 'Courage and daring'}},
      slytherin: {icon: '🐍', color: '#2e8b57', uk: 'Слизерин', pl: 'Slytherin', en: 'Slytherin', motto: {uk: 'Амбіції і кмітливість', pl: 'Ambicja i spryt', en: 'Ambition and cunning'}},
      ravenclaw: {icon: '🦅', color: '#3b6fd4', uk: 'Рейвенклов', pl: 'Ravenclaw', en: 'Ravenclaw', motto: {uk: 'Розум і мудрість', pl: 'Rozum i mądrość', en: 'Wit and wisdom'}},
      hufflepuff: {icon: '🦡', color: '#d9a400', uk: 'Гафелпаф', pl: 'Hufflepuff', en: 'Hufflepuff', motto: {uk: 'Вірність і працьовитість', pl: 'Lojalność i pracowitość', en: 'Loyalty and hard work'}}
    },
    standings: {uk: 'Кубок факультетів', pl: 'Puchar Domów', en: 'The House Cup'},
    collection: {uk: 'Картки з шоколадних жаб', pl: 'Karty z czekoladowych żab', en: 'Chocolate Frog Cards'}, cardIcon: '🐸',
    artifacts: {uk: 'Скарби Гоґвортсу', pl: 'Skarby Hogwartu', en: 'Hogwarts treasures'},
    journal: {
      title: {uk: 'Листи з Гоґвортсу', pl: 'Listy z Hogwartu', en: 'Letters from Hogwarts'}, icon: '🦉',
      open: 'Dear Mum and Dad,', sign: 'Love, your {faction} first-year',
      lines: [
        'Today at Hogwarts: {scene_en}. I learned a new word: “{w1}”. Someone said: “{line1}”',
        'You won\'t believe what happened. Everyone kept saying “{w1}” and “{w2}”. I think I finally understand them.',
        'The owl is waiting, so just quickly: today was about “{w1}”. I heard: “{line1}”. And “{w2}” means {t2}!',
        'Our house is fighting for the Cup. I earned points today. New words for you: {w1}, {w2}, {w3}.'
      ]
    }
  },

  'vampire-diaries-1': {
    theme: 'tvd',
    points: {icon: '💧', uk: 'краплі вербени', pl: 'krople werbeny', en: 'vervain drops'},
    ritual: {
      icon: '🌙',
      title: {uk: 'Хто ти в Містик Фоллс?', pl: 'Kim jesteś w Mystic Falls?', en: 'Who are you in Mystic Falls?'},
      intro: {uk: 'Ніч, туман над кладовищем, ворон на надгробку. П\'ять питань англійською — і місто вирішить, на чиєму ти боці.', pl: 'Noc, mgła nad cmentarzem, kruk na nagrobku. Pięć pytań po angielsku — i miasto zdecyduje, po czyjej jesteś stronie.', en: 'Night, fog over the cemetery, a crow on a gravestone. Five questions, and the town decides whose side you are on.'},
      reveal: {uk: 'Ворон злітає з надгробка. Твоя сторона:', pl: 'Kruk zrywa się z nagrobka. Twoja strona:', en: 'The crow takes off from the gravestone. Your side:'},
      questions: [
        {q: 'A stranger asks you to invite him in. You…', hint: {uk: 'Незнайомець просить запросити його в дім. Ти…', pl: 'Nieznajomy prosi, żebyś zaprosił go do środka. Ty…', en: ''},
          a: [['…smile and say: "Come in." What could go wrong?', 'salvatore'], ['…check if he can step on the porch without me.', 'bennett'], ['…offer him a glass of tea with vervain.', 'council'], ['…tell him to leave before I lose my temper.', 'lockwood']]},
        {q: 'What do you keep in your pocket?', hint: {uk: 'Що ти тримаєш у кишені?', pl: 'Co trzymasz w kieszeni?', en: ''},
          a: [['A ring that protects me from the sun.', 'salvatore'], ['An old crystal from my grandmother.', 'bennett'], ['A wooden stake. Just in case.', 'council'], ['The keys to my father\'s car.', 'lockwood']]},
        {q: 'Someone you love has a dark secret. You…', hint: {uk: 'Хтось, кого ти любиш, має темну таємницю. Ти…', pl: 'Ktoś, kogo kochasz, ma mroczną tajemnicę. Ty…', en: ''},
          a: [['…keep the secret. I have one too.', 'salvatore'], ['…look for the truth in old books.', 'bennett'], ['…tell the Founders\' Council.', 'council'], ['…pretend I don\'t care.', 'lockwood']]},
        {q: 'Where do you spend Friday night?', hint: {uk: 'Де ти проводиш вечір п\'ятниці?', pl: 'Gdzie spędzasz piątkowy wieczór?', en: ''},
          a: [['In the old mansion with a glass of bourbon.', 'salvatore'], ['At Grams\' house, lighting candles.', 'bennett'], ['At the Founders\' party, watching everyone.', 'council'], ['At the bonfire party by the falls.', 'lockwood']]},
        {q: 'Choose one word that describes you.', hint: {uk: 'Обери одне слово про себе.', pl: 'Wybierz jedno słowo o sobie.', en: ''},
          a: [['Eternal.', 'salvatore'], ['Powerful.', 'bennett'], ['Watchful.', 'council'], ['Wild.', 'lockwood']]}
      ]
    },
    factions: {
      salvatore: {icon: '🦇', color: '#8b1e2f', uk: 'Дім Сальваторе', pl: 'Dom Salvatore', en: 'House Salvatore', motto: {uk: 'Вічність і таємниці', pl: 'Wieczność i tajemnice', en: 'Eternity and secrets'}},
      bennett: {icon: '🕯️', color: '#7b5bd6', uk: 'Відьми Беннет', pl: 'Czarownice Bennett', en: 'The Bennett Witches', motto: {uk: 'Сила природи', pl: 'Siła natury', en: 'The power of nature'}},
      council: {icon: '🏛️', color: '#b08d3c', uk: 'Рада засновників', pl: 'Rada Założycieli', en: 'The Founders\' Council', motto: {uk: 'Захистити місто', pl: 'Chronić miasto', en: 'Protect the town'}},
      lockwood: {icon: '🐺', color: '#4f6b7a', uk: 'Родина Локвудів', pl: 'Rodzina Lockwoodów', en: 'The Lockwoods', motto: {uk: 'Кров і гнів', pl: 'Krew i gniew', en: 'Blood and temper'}}
    },
    standings: {uk: 'Рада засновників: рейтинг сторін', pl: 'Rada Założycieli: ranking stron', en: 'Founders\' Council standings'},
    collection: {uk: 'Карти Містик Фоллс', pl: 'Karty Mystic Falls', en: 'Mystic Falls cards'}, cardIcon: '🃏',
    artifacts: {uk: 'Артефакти уроків', pl: 'Artefakty lekcji', en: 'Lesson artifacts'},
    journal: {
      title: {uk: 'Мій щоденник з Містик Фоллс', pl: 'Mój pamiętnik z Mystic Falls', en: 'My Mystic Falls diary'}, icon: '📔',
      open: 'Dear Diary,', sign: '— the new kid at Mystic Falls High',
      lines: [
        'Today felt different. {scene_en}. I keep thinking about one word: “{w1}”. Somebody said: “{line1}”',
        'I can\'t sleep. Stefan said “{w1}”, and Damon just smiled. Bonnie says it means {t1}. I\'m not sure I want to know.',
        'Mystic Falls is full of secrets. Today I learned “{w1}”, “{w2}” and “{w3}”. I wrote them down so I don\'t forget.',
        'Something is wrong in this town. I heard: “{line1}”. And then: “{line2}”. I\'m scared, but I\'m not going to run away.'
      ]
    }
  },

  'friends-s1': {
    theme: null,
    points: {icon: '☕', uk: 'чашки кави', pl: 'filiżanki kawy', en: 'coffee cups'},
    ritual: {
      icon: '🛋️',
      title: {uk: 'Чий ти друг?', pl: 'Czyim jesteś przyjacielem?', en: 'Whose friend are you?'},
      intro: {uk: 'Помаранчевий диван у Central Perk вільний. П\'ять питань англійською — і ти дізнаєшся, з ким сидітимеш.', pl: 'Pomarańczowa kanapa w Central Perk jest wolna. Pięć pytań po angielsku — i dowiesz się, z kim usiądziesz.', en: 'The orange couch at Central Perk is free. Five questions, and you will know who you sit with.'},
      reveal: {uk: 'Гантер кличе тебе до столика:', pl: 'Gunther woła cię do stolika:', en: 'Gunther calls you to the table:'},
      questions: [
        {q: 'Your friends are coming over. You…', hint: {uk: 'До тебе приходять друзі. Ти…', pl: 'Przyjaciele przychodzą do ciebie. Ty…', en: ''},
          a: [['…clean the apartment twice and cook dinner.', 'monica'], ['…tell a joke to break the ice.', 'chandler'], ['…play a song about a smelly cat.', 'phoebe'], ['…ask: "How you doin\'?" and order pizza.', 'joey']]},
        {q: 'What is your dream job?', hint: {uk: 'Робота твоєї мрії?', pl: 'Twoja wymarzona praca?', en: ''},
          a: [['Head chef in a famous restaurant.', 'monica'], ['Something with numbers. Don\'t ask.', 'chandler'], ['A singer in a coffee house.', 'phoebe'], ['An actor in a soap opera.', 'joey']]},
        {q: 'Someone ate your sandwich. You…', hint: {uk: 'Хтось з\'їв твій сендвіч. Ти…', pl: 'Ktoś zjadł twoją kanapkę. Ty…', en: ''},
          a: [['…make a list of rules for the fridge.', 'monica'], ['…make a sarcastic comment.', 'chandler'], ['…believe it was a sign from the universe.', 'phoebe'], ['…shout: "JOEY DOESN\'T SHARE FOOD!"', 'joey']]},
        {q: 'Pick a place in New York.', hint: {uk: 'Обери місце в Нью-Йорку.', pl: 'Wybierz miejsce w Nowym Jorku.', en: ''},
          a: [['A big apartment with a purple door.', 'monica'], ['The apartment across the hall.', 'chandler'], ['A street corner with a guitar.', 'phoebe'], ['A pizza place, any pizza place.', 'joey']]},
        {q: 'Your friend is sad. What do you say?', hint: {uk: 'Твоєму другові сумно. Що ти скажеш?', pl: 'Twój przyjaciel jest smutny. Co powiesz?', en: ''},
          a: [['"Don\'t worry, I\'ll fix everything."', 'monica'], ['"Could this BE any worse? …Sorry."', 'chandler'], ['"Your aura is just a bit grey today."', 'phoebe'], ['"Let\'s get a sandwich. Two sandwiches."', 'joey']]}
      ]
    },
    factions: {
      monica: {icon: '🍳', color: '#7b3fa0', uk: 'Команда Моніки', pl: 'Drużyna Moniki', en: 'Team Monica', motto: {uk: 'Порядок і турбота', pl: 'Porządek i troska', en: 'Order and care'}},
      chandler: {icon: '😏', color: '#2f6fae', uk: 'Команда Чендлера', pl: 'Drużyna Chandlera', en: 'Team Chandler', motto: {uk: 'Сарказм як суперсила', pl: 'Sarkazm jako supermoc', en: 'Sarcasm as a superpower'}},
      phoebe: {icon: '🎸', color: '#d3843a', uk: 'Команда Фібі', pl: 'Drużyna Phoebe', en: 'Team Phoebe', motto: {uk: 'Дивацтво і свобода', pl: 'Dziwactwo i wolność', en: 'Weird and free'}},
      joey: {icon: '🍕', color: '#c0392b', uk: 'Команда Джої', pl: 'Drużyna Joeya', en: 'Team Joey', motto: {uk: 'Їжа і дружба', pl: 'Jedzenie i przyjaźń', en: 'Food and friendship'}}
    },
    standings: {uk: 'Битва за диван', pl: 'Bitwa o kanapę', en: 'The battle for the couch'},
    collection: {uk: 'Фото з холодильника', pl: 'Zdjęcia z lodówki', en: 'Fridge photos'}, cardIcon: '📸',
    artifacts: {uk: 'Сувеніри з квартири', pl: 'Pamiątki z mieszkania', en: 'Apartment souvenirs'},
    journal: {
      title: {uk: 'Щоденник сьомого друга', pl: 'Pamiętnik siódmego przyjaciela', en: 'The seventh friend\'s diary'}, icon: '☕',
      open: 'Dear Diary,', sign: '— written on the orange couch',
      lines: [
        'So today: {scene_en}. Best line of the day: “{line1}”',
        'New word I stole from the gang: “{w1}”. It means {t1}. Chandler used it sarcastically, of course.',
        'Gunther overheard us saying “{w1}” and “{w2}”. He pretended not to listen. He listened.',
        'Things I learned today: {w1}, {w2}, {w3}. Things Joey learned today: where the sandwiches are.'
      ]
    }
  },

  'home-alone': {
    theme: null,
    points: {icon: '🎄', uk: 'різдвяні вогники', pl: 'świąteczne światełka', en: 'Christmas lights'},
    ritual: {
      icon: '🏠',
      title: {uk: 'Хто ти в домі Маккалістерів?', pl: 'Kim jesteś w domu McCallisterów?', en: 'Who are you in the McCallister house?'},
      intro: {uk: 'Ніч перед Різдвом, сніг за вікном. П\'ять питань англійською — і ти дізнаєшся свою роль в обороні дому.', pl: 'Noc przed świętami, śnieg za oknem. Pięć pytań po angielsku — i poznasz swoją rolę w obronie domu.', en: 'The night before Christmas, snow outside. Five questions, and you will find your role in defending the house.'},
      reveal: {uk: 'Сирена на кухні вмикається сама. Твоя команда:', pl: 'Syrena w kuchni włącza się sama. Twoja drużyna:', en: 'The kitchen siren goes off by itself. Your team:'},
      questions: [
        {q: 'Burglars are coming tonight. You…', hint: {uk: 'Сьогодні вночі прийдуть грабіжники. Ти…', pl: 'Dziś w nocy przyjdą włamywacze. Ty…', en: ''},
          a: [['…draw a battle plan and set traps.', 'traps'], ['…call the police and the whole family.', 'family'], ['…go next door and ask the old neighbor for help.', 'neighbors'], ['…go shopping. Pizza first.', 'pizza']]},
        {q: 'What is your favourite trap?', hint: {uk: 'Твоя улюблена пастка?', pl: 'Twoja ulubiona pułapka?', en: ''},
          a: [['Paint cans on a rope.', 'traps'], ['A hot doorknob.', 'traps'], ['Ice on the stairs.', 'neighbors'], ['A tarantula. Don\'t ask.', 'pizza']]},
        {q: 'The family forgot you at home. You feel…', hint: {uk: 'Родина забула тебе вдома. Ти почуваєшся…', pl: 'Rodzina zapomniała cię w domu. Czujesz się…', en: ''},
          a: [['…free! I can do anything!', 'pizza'], ['…worried. Who will eat with me?', 'family'], ['…ready. This is my house now.', 'traps'], ['…a little lonely, so I go to church.', 'neighbors']]},
        {q: 'Pick your Christmas dinner.', hint: {uk: 'Обери різдвяну вечерю.', pl: 'Wybierz świąteczną kolację.', en: ''},
          a: [['A cheese pizza, just for me.', 'pizza'], ['A big turkey with the whole family.', 'family'], ['Macaroni and cheese by the tree.', 'traps'], ['Soup with my neighbor.', 'neighbors']]},
        {q: 'Choose one word that describes you.', hint: {uk: 'Обери одне слово про себе.', pl: 'Wybierz jedno słowo o sobie.', en: ''},
          a: [['Clever.', 'traps'], ['Caring.', 'family'], ['Kind.', 'neighbors'], ['Hungry.', 'pizza']]}
      ]
    },
    factions: {
      traps: {icon: '🪤', color: '#c0392b', uk: 'Майстри пасток', pl: 'Mistrzowie pułapek', en: 'Trap Masters', motto: {uk: 'План, мотузка, фарба', pl: 'Plan, sznurek, farba', en: 'Plan, rope, paint'}},
      family: {icon: '👨‍👩‍👧‍👦', color: '#2e7d4f', uk: 'Родина Маккалістерів', pl: 'Rodzina McCallisterów', en: 'The McCallisters', motto: {uk: 'Разом удома', pl: 'Razem w domu', en: 'Home together'}},
      neighbors: {icon: '❄️', color: '#3b6fd4', uk: 'Сусіди з Вінетки', pl: 'Sąsiedzi z Winnetki', en: 'Winnetka Neighbors', motto: {uk: 'Добро і сніг', pl: 'Dobro i śnieg', en: 'Kindness and snow'}},
      pizza: {icon: '🍕', color: '#d9a400', uk: 'Клуб «Сирна піца»', pl: 'Klub „Pizza serowa”', en: 'The Cheese Pizza Club', motto: {uk: 'Свобода і піца', pl: 'Wolność i pizza', en: 'Freedom and pizza'}}
    },
    standings: {uk: 'Оборона дому: рейтинг команд', pl: 'Obrona domu: ranking drużyn', en: 'House defence standings'},
    collection: {uk: 'Різдвяні іграшки', pl: 'Bombki choinkowe', en: 'Christmas ornaments'}, cardIcon: '🎁',
    artifacts: {uk: 'Речі з дому', pl: 'Rzeczy z domu', en: 'Things from the house'},
    journal: {
      title: {uk: 'Мій таємний записник', pl: 'Mój tajny notes', en: 'My secret notebook'}, icon: '📒',
      open: 'My secret notebook. TOP SECRET.', sign: '— Kevin\'s friend from next door',
      lines: [
        'Today: {scene_en}. New word: “{w1}”. I heard: “{line1}”',
        'Battle plan, part 2. Words I need: {w1}, {w2}, {w3}. Buzz would never understand.',
        'I\'m not afraid anymore. Today I learned “{w1}”. It means {t1}. Very useful against burglars.',
        'Dear Santa, I learned “{w1}” and “{w2}”. Please bring my family back. P.S. And more pizza.'
      ]
    }
  },

  'himym-s1': {
    theme: null,
    points: {icon: '🍺', uk: 'келихи в MacLaren\'s', pl: 'kufle w MacLaren\'s', en: 'MacLaren\'s pints'},
    ritual: {
      icon: '🎺',
      title: {uk: 'Хто ти в банді?', pl: 'Kim jesteś w paczce?', en: 'Who are you in the gang?'},
      intro: {uk: 'Ваш столик у MacLaren\'s вільний. П\'ять питань англійською — і стане ясно, чия ти людина.', pl: 'Wasz stolik w MacLaren\'s jest wolny. Pięć pytań po angielsku — i wszystko będzie jasne.', en: 'Your booth at MacLaren\'s is free. Five questions, and it will be clear whose person you are.'},
      reveal: {uk: 'Барні піднімає келих: «Це буде ЛЕГЕН… стривай… ДАРНО!» Твоя команда:', pl: 'Barney unosi kufel: „Będzie LEGEN… czekaj… DARNIE!” Twoja drużyna:', en: 'Barney raises his glass: "It\'s going to be LEGEN… wait for it… DARY!" Your team:'},
      questions: [
        {q: 'It\'s Friday night. What\'s the plan?', hint: {uk: 'Вечір п\'ятниці. Який план?', pl: 'Piątkowy wieczór. Jaki plan?', en: ''},
          a: [['Suit up! Tonight is going to be legendary.', 'barney'], ['Find the one. She could be here tonight.', 'ted'], ['A quiet night in with wine and cheese.', 'lily'], ['Hockey at the bar with a scotch.', 'robin']]},
        {q: 'Your friend has a big problem. You…', hint: {uk: 'У твого друга велика проблема. Ти…', pl: 'Twój przyjaciel ma duży problem. Ty…', en: ''},
          a: [['…make a plan and secretly fix everything.', 'lily'], ['…give a long speech about fate.', 'ted'], ['…say: "Challenge accepted!"', 'barney'], ['…tell the truth, even if it hurts.', 'robin']]},
        {q: 'What is in your closet?', hint: {uk: 'Що в тебе в шафі?', pl: 'Co masz w szafie?', en: ''},
          a: [['Twenty identical suits.', 'barney'], ['An old shirt that reminds me of my ex.', 'ted'], ['Paintings nobody has seen.', 'lily'], ['A secret from my past. Don\'t ask.', 'robin']]},
        {q: 'Choose a perfect date.', hint: {uk: 'Обери ідеальне побачення.', pl: 'Wybierz idealną randkę.', en: ''},
          a: [['Steal a blue French horn for her.', 'ted'], ['A shooting range and a hockey game.', 'robin'], ['Dinner at home with my best friend.', 'lily'], ['Date? I have a playbook for that.', 'barney']]},
        {q: 'Choose one word that describes you.', hint: {uk: 'Обери одне слово про себе.', pl: 'Wybierz jedno słowo o sobie.', en: ''},
          a: [['Romantic.', 'ted'], ['Awesome.', 'barney'], ['Loyal.', 'lily'], ['Independent.', 'robin']]}
      ]
    },
    factions: {
      ted: {icon: '🎺', color: '#2f6fae', uk: 'Команда Теда', pl: 'Drużyna Teda', en: 'Team Ted', motto: {uk: 'Віра в долю', pl: 'Wiara w przeznaczenie', en: 'Believe in fate'}},
      barney: {icon: '🤵', color: '#3a3a4a', uk: 'Команда Барні', pl: 'Drużyna Barneya', en: 'Team Barney', motto: {uk: 'Одягни костюм!', pl: 'Załóż garnitur!', en: 'Suit up!'}},
      lily: {icon: '🎨', color: '#c0577a', uk: 'Команда Лілі й Маршалла', pl: 'Drużyna Lily i Marshalla', en: 'Team Lily & Marshall', motto: {uk: 'Любов і вірність', pl: 'Miłość i wierność', en: 'Love and loyalty'}},
      robin: {icon: '🏒', color: '#c4302b', uk: 'Команда Робін', pl: 'Drużyna Robin', en: 'Team Robin', motto: {uk: 'Свобода понад усе', pl: 'Wolność ponad wszystko', en: 'Freedom first'}}
    },
    standings: {uk: 'Рейтинг столиків MacLaren\'s', pl: 'Ranking stolików MacLaren\'s', en: 'MacLaren\'s booth standings'},
    collection: {uk: 'Легендарні історії', pl: 'Legendarne historie', en: 'Legendary stories'}, cardIcon: '📼',
    artifacts: {uk: 'Сувеніри банди', pl: 'Pamiątki paczki', en: 'Gang souvenirs'},
    journal: {
      title: {uk: 'Нотатки з MacLaren\'s', pl: 'Notatki z MacLaren\'s', en: 'Notes from MacLaren\'s'}, icon: '📓',
      open: 'Note to future me:', sign: '— your past self, New York',
      lines: ['Tonight at MacLaren\'s: {scene_en}. Word of the night: “{w1}”.', 'New words: {w1}, {w2}, {w3}. Barney says they are legendary.']
    }
  },

  'cars': {
    theme: null,
    points: {icon: '🏁', uk: 'кола', pl: 'okrążenia', en: 'laps'},
    ritual: {
      icon: '🏎️',
      title: {uk: 'Твоє місце в Радіатор-Спрінгз', pl: 'Twoje miejsce w Chłodnicy Górskiej', en: 'Your place in Radiator Springs'},
      intro: {uk: 'Стара дорога 66, захід сонця, неонові вогні. П\'ять простих питань англійською — і місто покаже, де твій гараж.', pl: 'Stara droga 66, zachód słońca, neony. Pięć prostych pytań po angielsku — i miasto pokaże ci twój garaż.', en: 'Old Route 66, sunset, neon lights. Five easy questions, and the town shows you your garage.'},
      reveal: {uk: 'Неонові вогні спалахують. Твоя команда:', pl: 'Neony się zapalają. Twoja drużyna:', en: 'The neon lights come on. Your team:'},
      questions: [
        {q: 'What do you love?', hint: {uk: 'Що ти любиш?', pl: 'Co kochasz?', en: ''},
          a: [['Speed! I am fast.', 'speed'], ['My friends.', 'tow'], ['A quiet road in the mountains.', 'cone'], ['Old stories and wise advice.', 'doc']]},
        {q: 'What colour are you?', hint: {uk: 'Якого ти кольору?', pl: 'Jakiego jesteś koloru?', en: ''},
          a: [['Red.', 'speed'], ['Brown and a little rusty.', 'tow'], ['Blue.', 'cone'], ['Dark blue.', 'doc']]},
        {q: 'Your friend is lost on the road. You…', hint: {uk: 'Твій друг загубився на дорозі. Ти…', pl: 'Twój przyjaciel zgubił się na drodze. Ty…', en: ''},
          a: [['…drive very fast to find him.', 'speed'], ['…tow him home.', 'tow'], ['…give him a room for the night.', 'cone'], ['…show him the right way.', 'doc']]},
        {q: 'Where do you sleep?', hint: {uk: 'Де ти спиш?', pl: 'Gdzie śpisz?', en: ''},
          a: [['In a big trailer.', 'speed'], ['In a junkyard.', 'tow'], ['In a cone motel.', 'cone'], ['In a garage.', 'doc']]},
        {q: 'Choose one word.', hint: {uk: 'Обери одне слово.', pl: 'Wybierz jedno słowo.', en: ''},
          a: [['Fast.', 'speed'], ['Funny.', 'tow'], ['Kind.', 'cone'], ['Wise.', 'doc']]}
      ]
    },
    factions: {
      speed: {icon: '⚡', color: '#c4302b', uk: 'Команда Блискавки', pl: 'Drużyna Zygzaka', en: 'Team Lightning', motto: {uk: 'Я — швидкість!', pl: 'Jestem szybkością!', en: 'I am speed!'}},
      tow: {icon: '🪝', color: '#8a5a3a', uk: 'Буксир Метра', pl: 'Holownik Złomka', en: 'Mater\'s Tow Crew', motto: {uk: 'Друзі понад усе', pl: 'Przyjaciele ponad wszystko', en: 'Friends first'}},
      cone: {icon: '🔶', color: '#3b6fd4', uk: 'Мотель «Затишний конус»', pl: 'Motel „Przytulny Pachołek”', en: 'The Cozy Cone', motto: {uk: 'Дорога — це життя', pl: 'Droga to życie', en: 'The road is life'}},
      doc: {icon: '🏆', color: '#1f3a6b', uk: 'Гараж Дока', pl: 'Warsztat Doca', en: 'Doc\'s Garage', motto: {uk: 'Мудрість і досвід', pl: 'Mądrość i doświadczenie', en: 'Wisdom and experience'}}
    },
    standings: {uk: 'Велика гонка команд', pl: 'Wielki wyścig drużyn', en: 'The big team race'},
    collection: {uk: 'Наліпки з гонок', pl: 'Naklejki z wyścigów', en: 'Race stickers'}, cardIcon: '🏁',
    artifacts: {uk: 'Сувеніри з дороги 66', pl: 'Pamiątki z drogi 66', en: 'Route 66 souvenirs'},
    journal: {
      title: {uk: 'Бортовий журнал', pl: 'Dziennik trasy', en: 'My road logbook'}, icon: '🗺️',
      open: 'Logbook:', sign: '— the rookie of the pit crew',
      lines: ['Today: {scene_en}. New word: “{w1}”.', 'Words for the road: {w1}, {w2}, {w3}.']
    }
  },

  'zootopia': {
    theme: null,
    points: {icon: '🥕', uk: 'морквини', pl: 'marchewki', en: 'carrots'},
    ritual: {
      icon: '🚆',
      title: {uk: 'Твій район Зоотрополіса', pl: 'Twoja dzielnica Zwierzogrodu', en: 'Your Zootopia district'},
      intro: {uk: 'Потяг прибуває на центральний вокзал. П\'ять питань англійською — і місто покаже, де твій дім.', pl: 'Pociąg wjeżdża na dworzec główny. Pięć pytań po angielsku — i miasto pokaże, gdzie jest twój dom.', en: 'The train pulls into the main station. Five questions, and the city shows you where home is.'},
      reveal: {uk: 'Двері потяга відчиняються. Твій район:', pl: 'Drzwi pociągu się otwierają. Twoja dzielnica:', en: 'The train doors open. Your district:'},
      questions: [
        {q: 'What is the perfect weather for you?', hint: {uk: 'Яка погода для тебе ідеальна?', pl: 'Jaka pogoda jest dla ciebie idealna?', en: ''},
          a: [['Hot and sunny, like a desert.', 'sahara'], ['Cold, with lots of snow.', 'tundra'], ['Warm rain every day.', 'rainforest'], ['Any weather, if I\'m with my family.', 'burrows']]},
        {q: 'You see someone breaking the law. You…', hint: {uk: 'Ти бачиш, як хтось порушує закон. Ти…', pl: 'Widzisz, jak ktoś łamie prawo. Ty…', en: ''},
          a: [['…run after him. I\'m a real cop!', 'burrows'], ['…call my friends in high places.', 'tundra'], ['…watch from above and take notes.', 'rainforest'], ['…talk to him. Maybe he has a reason.', 'sahara']]},
        {q: 'Pick a job in the city.', hint: {uk: 'Обери роботу в місті.', pl: 'Wybierz pracę w mieście.', en: ''},
          a: [['Police officer at the ZPD.', 'burrows'], ['Boss of a big family business.', 'tundra'], ['Yoga teacher at a spa.', 'sahara'], ['Scientist in a secret lab.', 'rainforest']]},
        {q: 'What do you always carry?', hint: {uk: 'Що ти завжди маєш із собою?', pl: 'Co zawsze nosisz ze sobą?', en: ''},
          a: [['A carrot pen that records voices.', 'burrows'], ['A warm scarf.', 'tundra'], ['Sunglasses.', 'sahara'], ['An umbrella, obviously.', 'rainforest']]},
        {q: 'Choose your motto.', hint: {uk: 'Обери свій девіз.', pl: 'Wybierz swoje motto.', en: ''},
          a: [['Anyone can be anything.', 'burrows'], ['Respect the family.', 'tundra'], ['Relax, it\'s all good.', 'sahara'], ['Look closer.', 'rainforest']]}
      ]
    },
    factions: {
      burrows: {icon: '🐰', color: '#d3843a', uk: 'Бані Барроу', pl: 'Królikowo', en: 'Bunnyburrow', motto: {uk: 'Будь-хто може бути ким завгодно', pl: 'Każdy może być kim chce', en: 'Anyone can be anything'}},
      sahara: {icon: '🌵', color: '#d9a400', uk: 'Сахара-сквер', pl: 'Plac Sahary', en: 'Sahara Square', motto: {uk: 'Спокій і сонце', pl: 'Spokój i słońce', en: 'Calm and sun'}},
      tundra: {icon: '🐻‍❄️', color: '#3b8fd4', uk: 'Тундратаун', pl: 'Tundrowo', en: 'Tundratown', motto: {uk: 'Повага і родина', pl: 'Szacunek i rodzina', en: 'Respect and family'}},
      rainforest: {icon: '🌿', color: '#2e8b57', uk: 'Дощовий ліс', pl: 'Las Deszczowy', en: 'Rainforest District', motto: {uk: 'Придивись уважніше', pl: 'Przyjrzyj się bliżej', en: 'Look closer'}}
    },
    standings: {uk: 'Битва районів', pl: 'Bitwa dzielnic', en: 'Battle of the districts'},
    collection: {uk: 'Справи ZPD', pl: 'Akta ZPD', en: 'ZPD case files'}, cardIcon: '🗂️',
    artifacts: {uk: 'Значки і жетони', pl: 'Odznaki i żetony', en: 'Badges and tokens'},
    journal: {
      title: {uk: 'Блокнот новачка ZPD', pl: 'Notatnik rekruta ZPD', en: 'A ZPD rookie\'s notebook'}, icon: '🥕',
      open: 'Rookie\'s field notes.', sign: '— rookie officer, ZPD',
      lines: [
        'Case update: {scene_en}. Key word: “{w1}”. Witness said: “{line1}”',
        'Note to self: “{w1}” means {t1}. Nick laughed when I wrote it down. Whatever.',
        'Words for the report: {w1}, {w2}, {w3}. Chief Bogo will be impressed. Maybe.',
        'Today I learned “{w1}” and “{w2}”. Try everything!'
      ]
    }
  }
};
