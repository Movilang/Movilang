/* MovieLang — клієнтський застосунок.
   Два режими бекенду: Supabase (якщо заповнено config.js) або DEMO (localStorage). */
(function () {
'use strict';

/* ================= helpers ================= */
var $app = document.getElementById('app');
function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]; }); }
function toast(msg) { var t = document.createElement('div'); t.className = 'toast'; t.setAttribute('role', 'status'); t.textContent = msg; document.body.appendChild(t); setTimeout(function () { t.remove(); }, 3200); }
function uid() { return 'id' + Math.random().toString(36).slice(2, 10) + Date.now().toString(36); }
function fmtDate(d) { if (!d) return '—'; try { return new Date(d).toLocaleDateString('uk-UA', {day:'2-digit',month:'2-digit',year:'numeric'}); } catch (e) { return d; } }
function genCode() { var a = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789', s = ''; for (var i = 0; i < 12; i++) { s += a[Math.floor(Math.random() * a.length)]; if (i === 3 || i === 7) s += '-'; } return s; }
function say(t) { try { var u = new SpeechSynthesisUtterance(t); u.lang = 'en-GB'; u.rate = .9; speechSynthesis.cancel(); speechSynthesis.speak(u); } catch (e) { toast('Озвучення недоступне в цьому браузері'); } }
var TASK_TYPES = { vocabulary:'VOCABULARY', listening:'LISTENING', subtitles:'SUBTITLES', grammar:'GRAMMAR', speaking:'SPEAKING', quiz:'MINI QUIZ', final:'ФІНАЛ' };
var POSTER_CLASSES = ['p1','p2','p3','p4','p5','p6','p7','p8'];

/* ================= default content ================= */
var DEFAULT_SETTINGS = {
  hero_eyebrow: 'Онлайн-марафон англійської · A2–B2',
  hero_w1: 'Дивись.', hero_w2: 'Розумій.', hero_w3: 'Говори.',
  hero_lead: 'Вчи англійську на сценах з улюблених фільмів і серіалів. Купуєш персональний ключ, відкриваєш марафон і щодня проходиш короткі завдання: слова зі сцени, аудіювання, субтитри з пропусками, граматику і говоріння.',
  plan1_name: 'Один фільм', plan1_price: '299 ₴', plan1_text: '1 марафон на вибір\n7–10 уроків\nСловник і картки\nСертифікат після фіналу',
  plan2_name: 'Пакет фільмів', plan2_price: '699 ₴', plan2_text: '3 марафони на вибір\nПеревірка speaking-завдань\nРозширений словник з аудіо\nКлюч можна подарувати',
  plan3_name: 'Підписка', plan3_price: '349 ₴ / міс', plan3_text: 'Усі марафони каталогу\nНові марафони щомісяця\nРозмовний клуб онлайн\nСкасування в один клік',
  buy_info: 'Щоб купити ключ, напишіть нам: hello@movielang.example — ключ надійде на пошту протягом години.',
  faq: 'Чи потрібно мати сам фільм?|Ні. Уроки містять опис сцен і навчальні аудіо, а всі завдання ми створюємо самі.\nЯкий рівень англійської потрібен?|Від A2. Кожен марафон має позначку рівня, а пояснення граматики написані українською.\nЩо таке ключ доступу?|Персональний код з 12 символів. Введи його в кабінеті, і марафон відкриється.\nСкільки часу займає урок?|10–15 хвилин. Прогрес зберігається після кожного уроку.\nЧи можна подарувати ключ?|Так. Ключ не прив\'язаний до покупця, доки його не активовано.'
};

function T(type, scene, q, options, answer, tip, extra) { var t = {type:type, scene:scene, q:q, options:options || [], answer:answer || 0, tip:tip || ''}; if (extra) for (var k in extra) t[k] = extra[k]; return t; }
var SEED_COURSES = [
  {slug:'harry-potter-1', title:'Гаррі Поттер і філософський камінь', kind:'film', level:'A2–B1', price:'299 ₴', poster:'p1', published:true, description:'Проходиш історію разом з героєм: від дивного листа до фінальної перемоги. Кожен урок спирається на одну сцену і тренує одну тему граматики.'},
  {slug:'friends-s1', title:'Друзі. Сезон 1', kind:'series', level:'A2', price:'299 ₴', poster:'p2', published:true, description:'Побутова англійська, жарти й розмовні фрази шести друзів у Нью-Йорку.'},
  {slug:'zootopia', title:'Зоотрополіс', kind:'film', level:'A2', price:'299 ₴', poster:'p3', published:true, description:'Місто тварин, детективна історія і проста зрозуміла лексика.'},
  {slug:'sherlock-s1', title:'Шерлок. Сезон 1', kind:'series', level:'B2', price:'349 ₴', poster:'p7', published:true, description:'Швидкі діалоги, дедукція і британська англійська для рівня B2.'}
];
var SEED_HP_LESSONS = [
  {num:1, title:'Звичайний будинок, незвичайний хлопчик', grammar:'Present Simple', scene:'Хлопчик живе з тіткою, дядьком і кузеном; його кімната — під сходами.', tasks:[
    T('vocabulary','Кімната під сходами.','What does <b>stairs</b> mean?',['сходи','стіни','двері'],0,'Stairs — сходи.'),
    T('listening','Тітка дає хлопчику доручення.','Listen. What does she want Harry to do?',['clean the kitchen','cook breakfast','go to school'],1,'Cook breakfast — приготувати сніданок.',{say:'Harry, go and cook breakfast. Now!'}),
    T('grammar','Present Simple: he / she / it + -s.','Harry ____ with his aunt and uncle.',['live','lives','living'],1,'Після he/she/it додаємо -s: Harry lives.'),
    T('quiz','Питання за сюжетом.','Where does Harry sleep at the start of the story?',['in a big bedroom','under the stairs','at school'],1,'Under the stairs — під сходами.')]},
  {num:2, title:'Лист, який не можна зупинити', grammar:'Past Simple', scene:'Приходять десятки листів, дядько намагається їх сховати.', tasks:[
    T('vocabulary','Лист з печаткою.','What is an <b>envelope</b>?',['конверт','марка','скриня'],0,'Envelope — конверт.'),
    T('subtitles','Дядько забирає лист.','Uncle Vernon ____ the letter and burned it.',['took','takes','take'],0,'Past Simple від take — took.'),
    T('quiz','Питання за сюжетом.','Where does the family go to escape the letters?',['to a small island','to London','to the zoo'],0,'To a small island — на маленький острів.')]},
  {num:3, title:'Ти чарівник', grammar:'to be', scene:'Велетень знаходить хлопчика на острові й розповідає правду.', tasks:[
    T('subtitles','Велетень розповідає хлопчику правду про нього.','You are a ____, Harry.',['wizard','teacher','student'],0,'Wizard — чарівник.'),
    T('listening','День народження в хатинці.','Listen. What does Hagrid bring for Harry?',['a book','a cake','a broom'],1,'A cake — торт.',{say:'Happy birthday, Harry! I brought you a cake.'}),
    T('grammar','to be: is / are / was / were.','His parents ____ wizards.',['was','were','is'],1,'Множина в минулому — were.'),
    T('speaking','Опиши героя.','Повтори вголос: <i>“Hagrid is tall and very kind.”</i>',[],0,'У повній версії система оцінює вимову.',{say:'Hagrid is tall and very kind.'})]},
  {num:4, title:'Покупки на чарівній вулиці', grammar:'can / can\'t', scene:'Купівля мантії, книжок, палички та сови.', tasks:[
    T('vocabulary','Магазин паличок.','What is a <b>wand</b>?',['чарівна паличка','мантія','сова'],0,'Wand — чарівна паличка.'),
    T('grammar','can / can\'t.','Muggles ____ see the magic street.',['can','can\'t','are'],1,'Звичайні люди не бачать вулицю — can\'t.'),
    T('speaking','Рольова гра в магазині.','Повтори вголос: <i>“Can I try this one?”</i>',[],0,'Can I…? — ввічливе прохання.',{say:'Can I try this one?'})]},
  {num:5, title:'Платформа і потяг', grammar:'Питання', scene:'Пошук дивної платформи, знайомство в потязі.', tasks:[
    T('listening','Знайомство в потязі.','Listen and choose what you hear.',['Is this seat free?','Is this street free?','Is this sweet free?'],0,'Seat — місце.',{say:'Is this seat free?'}),
    T('grammar','Порядок слів у питанні.','____ you like sweets?',['Do','Does','Are'],0,'З you — Do you…?'),
    T('quiz','Питання за сюжетом.','How do they get to the platform?',['through a wall','by car','by plane'],0,'Through a wall — крізь стіну.')]},
  {num:6, title:'Капелюх обирає дім', grammar:'Прикметники', scene:'Церемонія розподілу учнів по гуртожитках.', tasks:[
    T('vocabulary','Характер.','What does <b>brave</b> mean?',['сміливий','розумний','добрий'],0,'Brave — сміливий.'),
    T('subtitles','Хлопчик хвилюється перед вибором.','Harry is ____ because he doesn\'t want the wrong house.',['nervous','bored','angry'],0,'Nervous — схвильований.'),
    T('grammar','Порівняння.','The Great Hall is ____ than the classroom.',['big','bigger','biggest'],1,'Порівняння: big → bigger.')]},
  {num:7, title:'Перший урок польотів', grammar:'Present Continuous', scene:'Урок на мітлах і перша гра в повітрі.', tasks:[
    T('grammar','Present Continuous.','Look! Harry ____ very fast.',['flies','is flying','fly'],1,'Дія зараз — is flying.'),
    T('listening','Учитель дає команду.','Listen. What must students say to the broom?',['up','go','fly'],0,'Up — вгору.',{say:'Hold your hand over the broom and say: up!'}),
    T('speaking','Коментатор матчу.','Повтори вголос: <i>“He is flying higher and higher!”</i>',[],0,'Тренуємо інтонацію.',{say:'He is flying higher and higher!'})]},
  {num:8, title:'Фінал: твоя улюблена сцена', grammar:'Повторення', scene:'Підземні випробування й фінальна зустріч.', tasks:[
    T('quiz','Питання за сюжетом.','What animal brings letters?',['an owl','a cat','a rat'],0,'An owl — сова.'),
    T('quiz','Питання за сюжетом.','What game do they play on the way to the stone?',['chess','cards','football'],0,'Chess — шахи.'),
    T('final','Фінальне завдання.','Describe your favourite scene and character in English (80–120 words). Use 3 verbs in Past Simple and can / can\'t.',[],0,'Відповідь збережеться в кабінеті.')]}
];

/* ================= DEMO backend (localStorage) ================= */
function DemoBackend() {
  var KEY = 'movielang_demo_db_v1', SKEY = 'movielang_demo_session';
  var mem = null;
  function load() {
    if (mem) return mem;
    try { mem = JSON.parse(localStorage.getItem(KEY) || 'null'); } catch (e) { mem = null; }
    if (!mem) mem = seed();
    return mem;
  }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(mem)); } catch (e) {} }
  function seed() {
    var db = {users:[], courses:[], lessons:[], keys:[], enrollments:[], progress:[], settings:JSON.parse(JSON.stringify(DEFAULT_SETTINGS))};
    var now = Date.now(), day = 86400000;
    db.users.push({id:'u_admin', email:'admin@movielang.demo', password:'admin123', name:'Адміністратор', role:'admin', created_at:new Date(now - 30*day).toISOString()});
    var students = [['olena@example.com','Олена К.',20],['andrii@example.com','Андрій М.',12],['maria@example.com','Марія С.',5],['ivan@example.com','Іван П.',2]];
    SEED_COURSES.forEach(function (c, i) { var cc = JSON.parse(JSON.stringify(c)); cc.id = 'c' + (i + 1); cc.created_at = new Date(now - 25*day).toISOString(); db.courses.push(cc); });
    SEED_HP_LESSONS.forEach(function (l) { var ll = JSON.parse(JSON.stringify(l)); ll.id = 'l' + l.num; ll.course_id = 'c1'; db.lessons.push(ll); });
    students.forEach(function (s, i) {
      var id = 'u_s' + i; db.users.push({id:id, email:s[0], password:'demo123', name:s[1], role:'student', created_at:new Date(now - s[2]*day).toISOString()});
      var code = genCode(); db.keys.push({code:code, course_id:'c1', created_at:new Date(now - s[2]*day).toISOString(), activated_by:id, activated_at:new Date(now - s[2]*day + 3600000).toISOString()});
      db.enrollments.push({user_id:id, course_id:'c1', created_at:new Date(now - s[2]*day).toISOString()});
      var done = [6,4,2,1][i];
      for (var n = 1; n <= done; n++) db.progress.push({user_id:id, lesson_id:'l' + n, score:[100,88,75,92,67,100][(n + i) % 6], completed_at:new Date(now - (s[2] - n)*day).toISOString()});
    });
    for (var k = 0; k < 3; k++) db.keys.push({code:genCode(), course_id:'c1', created_at:new Date(now - day).toISOString(), activated_by:null, activated_at:null});
    db.keys.push({code:'HPS1-7KQ4-WZ9M', course_id:'c1', created_at:new Date(now).toISOString(), activated_by:null, activated_at:null});
    mem = db; save(); return db;
  }
  function me() { var id; try { id = localStorage.getItem(SKEY); } catch (e) {} var u = load().users.filter(function (x) { return x.id === id; })[0]; return u ? {id:u.id, email:u.email, name:u.name, role:u.role} : null; }
  function setSession(id) { try { if (id) localStorage.setItem(SKEY, id); else localStorage.removeItem(SKEY); } catch (e) {} }
  function needAdmin() { var u = me(); if (!u || u.role !== 'admin') throw new Error('Потрібні права адміністратора'); }
  function P(v) { return Promise.resolve(v); }
  return {
    mode:'demo',
    getUser: function () { return P(me()); },
    signUp: function (email, pass, name) {
      var db = load(); email = email.trim().toLowerCase();
      if (db.users.some(function (u) { return u.email === email; })) return Promise.reject(new Error('Користувач з такою поштою вже існує'));
      var u = {id:uid(), email:email, password:pass, name:name || email.split('@')[0], role:'student', created_at:new Date().toISOString()};
      db.users.push(u); save(); setSession(u.id); return P(me());
    },
    signIn: function (email, pass) {
      var u = load().users.filter(function (x) { return x.email === email.trim().toLowerCase() && x.password === pass; })[0];
      if (!u) return Promise.reject(new Error('Невірна пошта або пароль'));
      setSession(u.id); return P(me());
    },
    signOut: function () { setSession(null); return P(true); },
    getSettings: function () { var s = load().settings; var o = {}; for (var k in DEFAULT_SETTINGS) o[k] = s[k] != null ? s[k] : DEFAULT_SETTINGS[k]; return P(o); },
    saveSettings: function (obj) { needAdmin(); var db = load(); for (var k in obj) db.settings[k] = obj[k]; save(); return P(true); },
    listCourses: function (all) { var db = load(); return P(db.courses.filter(function (c) { return all || c.published; }).map(function (c) { var o = JSON.parse(JSON.stringify(c)); o.lessons_count = db.lessons.filter(function (l) { return l.course_id === c.id; }).length; return o; })); },
    getCourse: function (id) { var c = load().courses.filter(function (x) { return x.id === id; })[0]; return P(c ? JSON.parse(JSON.stringify(c)) : null); },
    saveCourse: function (c) { needAdmin(); var db = load(); if (!c.id) { c.id = uid(); c.created_at = new Date().toISOString(); db.courses.push(c); } else { db.courses = db.courses.map(function (x) { return x.id === c.id ? Object.assign({}, x, c) : x; }); } save(); return P(c); },
    deleteCourse: function (id) { needAdmin(); var db = load(); db.courses = db.courses.filter(function (x) { return x.id !== id; }); db.lessons = db.lessons.filter(function (l) { return l.course_id !== id; }); save(); return P(true); },
    listLessons: function (courseId) { return P(load().lessons.filter(function (l) { return l.course_id === courseId; }).sort(function (a, b) { return a.num - b.num; }).map(function (l) { return JSON.parse(JSON.stringify(l)); })); },
    getLesson: function (id) { var l = load().lessons.filter(function (x) { return x.id === id; })[0]; return P(l ? JSON.parse(JSON.stringify(l)) : null); },
    saveLesson: function (l) { needAdmin(); var db = load(); if (!l.id) { l.id = uid(); db.lessons.push(l); } else { db.lessons = db.lessons.map(function (x) { return x.id === l.id ? l : x; }); } save(); return P(l); },
    deleteLesson: function (id) { needAdmin(); var db = load(); db.lessons = db.lessons.filter(function (x) { return x.id !== id; }); save(); return P(true); },
    myEnrollments: function () { var u = me(); if (!u) return P([]); return P(load().enrollments.filter(function (e) { return e.user_id === u.id; }).map(function (e) { return e.course_id; })); },
    activateKey: function (code) {
      var u = me(); if (!u) return Promise.reject(new Error('Увійдіть в акаунт'));
      var db = load(); code = code.trim().toUpperCase();
      var k = db.keys.filter(function (x) { return x.code === code; })[0];
      if (!k) return P({ok:false, msg:'Такого ключа не знайдено. Перевір літери O та 0, I та 1.'});
      if (k.activated_by) return P({ok:false, msg:'Цей ключ уже активовано.'});
      k.activated_by = u.id; k.activated_at = new Date().toISOString();
      var ids = k.course_id ? [k.course_id] : db.courses.map(function (c) { return c.id; });
      ids.forEach(function (cid) { if (!db.enrollments.some(function (e) { return e.user_id === u.id && e.course_id === cid; })) db.enrollments.push({user_id:u.id, course_id:cid, created_at:new Date().toISOString()}); });
      save(); return P({ok:true, course_id:k.course_id});
    },
    myProgress: function () { var u = me(); if (!u) return P([]); return P(load().progress.filter(function (p) { return p.user_id === u.id; })); },
    saveProgress: function (lessonId, score, answer) {
      var u = me(); if (!u) return P(false); var db = load();
      db.progress = db.progress.filter(function (p) { return !(p.user_id === u.id && p.lesson_id === lessonId); });
      db.progress.push({user_id:u.id, lesson_id:lessonId, score:score, answer:answer || null, completed_at:new Date().toISOString()}); save(); return P(true);
    },
    adminData: function () { needAdmin(); var db = load(); return P({users:db.users.map(function (u) { return {id:u.id, email:u.email, name:u.name, role:u.role, created_at:u.created_at}; }), keys:db.keys.slice(), enrollments:db.enrollments.slice(), progress:db.progress.slice()}); },
    createKeys: function (courseId, n) { needAdmin(); var db = load(), out = []; for (var i = 0; i < n; i++) { var k = {code:genCode(), course_id:courseId || null, created_at:new Date().toISOString(), activated_by:null, activated_at:null}; db.keys.push(k); out.push(k); } save(); return P(out); },
    deleteKey: function (code) { needAdmin(); var db = load(); db.keys = db.keys.filter(function (k) { return k.code !== code; }); save(); return P(true); },
    setRole: function (userId, role) { needAdmin(); var db = load(); db.users.forEach(function (u) { if (u.id === userId) u.role = role; }); save(); return P(true); },
    resetDemo: function () { try { localStorage.removeItem(KEY); localStorage.removeItem(SKEY); } catch (e) {} mem = null; load(); return P(true); }
  };
}

/* ================= Supabase backend ================= */
function SupabaseBackend(url, key) {
  var sb = window.supabase.createClient(url, key);
  var cachedUser;
  function ok(r) { if (r.error) throw new Error(r.error.message); return r.data; }
  function profile() {
    return sb.auth.getUser().then(function (r) {
      var u = r.data && r.data.user; if (!u) return null;
      return sb.from('profiles').select('*').eq('id', u.id).maybeSingle().then(function (p) {
        var pr = p.data || {};
        return {id:u.id, email:u.email, name:pr.name || (u.user_metadata && u.user_metadata.name) || u.email, role:pr.role || 'student'};
      });
    });
  }
  return {
    mode:'supabase',
    getUser: function () { return profile().then(function (u) { cachedUser = u; return u; }); },
    signUp: function (email, pass, name) {
      return sb.auth.signUp({email:email.trim(), password:pass, options:{data:{name:name}}}).then(function (r) {
        if (r.error) throw new Error(r.error.message);
        if (!r.data.session) throw new Error('Акаунт створено! Перевір пошту (і папку «Спам»), натисни посилання з листа, потім увійди.');
        return profile();
      });
    },
    signIn: function (email, pass) { return sb.auth.signInWithPassword({email:email.trim(), password:pass}).then(function (r) {
      if (r.error) { var m = (r.error.message || '').toLowerCase();
        if (m.indexOf('not confirmed') > -1) throw new Error('Пошту не підтверджено. Відкрий лист від Supabase і натисни посилання, потім увійди.');
        if (m.indexOf('invalid') > -1) throw new Error('Невірна пошта або пароль.');
        throw new Error('Помилка входу: ' + r.error.message); }
      return profile(); }); },
    signOut: function () { return sb.auth.signOut(); },
    getSettings: function () { return sb.from('site_settings').select('*').then(function (r) { var o = {}; for (var k in DEFAULT_SETTINGS) o[k] = DEFAULT_SETTINGS[k]; (r.data || []).forEach(function (x) { o[x.key] = x.value; }); return o; }); },
    saveSettings: function (obj) { var rows = Object.keys(obj).map(function (k) { return {key:k, value:obj[k]}; }); return sb.from('site_settings').upsert(rows).then(ok); },
    listCourses: function (all) {
      var q = sb.from('courses').select('*, lessons(count)').order('created_at');
      if (!all) q = q.eq('published', true);
      return q.then(ok).then(function (rows) { return rows.map(function (c) { c.lessons_count = c.lessons && c.lessons[0] ? c.lessons[0].count : 0; delete c.lessons; return c; }); });
    },
    getCourse: function (id) { return sb.from('courses').select('*').eq('id', id).maybeSingle().then(ok); },
    saveCourse: function (c) { var row = {slug:c.slug, title:c.title, kind:c.kind, level:c.level, price:c.price, poster:c.poster, published:!!c.published, description:c.description}; if (c.id) row.id = c.id; return sb.from('courses').upsert(row).select().single().then(ok); },
    deleteCourse: function (id) { return sb.from('courses').delete().eq('id', id).then(ok); },
    listLessons: function (courseId) { return sb.from('lessons').select('*').eq('course_id', courseId).order('num').then(ok); },
    getLesson: function (id) { return sb.from('lessons').select('*').eq('id', id).maybeSingle().then(ok); },
    saveLesson: function (l) { var row = {course_id:l.course_id, num:l.num, title:l.title, grammar:l.grammar, scene:l.scene, tasks:l.tasks}; if (l.id) row.id = l.id; return sb.from('lessons').upsert(row).select().single().then(ok); },
    deleteLesson: function (id) { return sb.from('lessons').delete().eq('id', id).then(ok); },
    myEnrollments: function () { if (!cachedUser) return Promise.resolve([]); return sb.from('enrollments').select('course_id').eq('user_id', cachedUser.id).then(ok).then(function (r) { return r.map(function (x) { return x.course_id; }); }); },
    activateKey: function (code) { return sb.rpc('activate_key', {p_code:code.trim().toUpperCase()}).then(ok); },
    myProgress: function () { if (!cachedUser) return Promise.resolve([]); return sb.from('progress').select('*').eq('user_id', cachedUser.id).then(ok); },
    saveProgress: function (lessonId, score, answer) { if (!cachedUser) return Promise.resolve(false); return sb.from('progress').upsert({user_id:cachedUser.id, lesson_id:lessonId, score:score, answer:answer || null, completed_at:new Date().toISOString()}).then(ok); },
    adminData: function () {
      return Promise.all([sb.from('profiles').select('*').order('created_at'), sb.from('access_keys').select('*').order('created_at', {ascending:false}), sb.from('enrollments').select('*'), sb.from('progress').select('*')])
        .then(function (r) { r.forEach(ok); return {users:r[0].data, keys:r[1].data, enrollments:r[2].data, progress:r[3].data}; });
    },
    createKeys: function (courseId, n) { var rows = []; for (var i = 0; i < n; i++) rows.push({code:genCode(), course_id:courseId || null}); return sb.from('access_keys').insert(rows).select().then(ok); },
    deleteKey: function (code) { return sb.from('access_keys').delete().eq('code', code).then(ok); },
    setRole: function (userId, role) { return sb.from('profiles').update({role:role}).eq('id', userId).then(ok); }
  };
}

/* ================= init ================= */
var cfg = window.MOVIELANG_CONFIG || {};
var API = (cfg.SUPABASE_URL && cfg.SUPABASE_ANON_KEY && window.supabase) ? SupabaseBackend(cfg.SUPABASE_URL, cfg.SUPABASE_ANON_KEY) : DemoBackend();
if (API.mode === 'demo') document.getElementById('demoBar').hidden = false;
var USER = null, SETTINGS = DEFAULT_SETTINGS;

function renderNav() {
  var links = '<a href="#/">Головна</a><a href="#/catalog">Каталог</a><a href="#/trial">Пробний урок</a><a href="#/pricing">Тарифи</a>';
  if (USER) links += '<a href="#/cabinet">Кабінет</a>';
  if (USER && USER.role === 'admin') links += '<a href="#/admin" style="color:var(--red)">Адмін</a>';
  document.getElementById('navlinks').innerHTML = links;
  document.getElementById('navuser').innerHTML = USER
    ? '<a class="userchip" href="#/cabinet" style="text-decoration:none"><span class="ava">' + esc((USER.name || '?')[0].toUpperCase()) + '</span><span class="muted" style="max-width:120px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">' + esc(USER.name) + '</span></a><button class="btn btn-ghost btn-sm" type="button" id="logoutBtn">Вийти</button>'
    : '<a class="btn btn-ghost btn-sm" href="#/login">Увійти</a><a class="btn btn-red btn-sm" href="#/register">Реєстрація</a>';
  var lb = document.getElementById('logoutBtn');
  if (lb) lb.onclick = function () { API.signOut().then(function () { USER = null; toast('Ви вийшли з акаунта'); location.hash = '#/'; renderNav(); route(); }); };
}

/* ================= views ================= */
function heroSvg() {
  return '<svg class="scene" viewBox="0 0 800 500" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><defs><radialGradient id="glow" cx="62%" cy="40%" r="45%"><stop offset="0" stop-color="#ffd27a" stop-opacity=".75"/><stop offset=".5" stop-color="#8b5cf6" stop-opacity=".25"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient><linearGradient id="floor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a1230"/><stop offset="1" stop-color="#050409"/></linearGradient></defs><rect width="800" height="500" fill="url(#floor)"/><rect width="800" height="500" fill="url(#glow)"/><rect x="90" y="70" width="150" height="190" rx="75" fill="#0c0a1a" stroke="#3a2f63" stroke-width="4"/><g transform="translate(470 150) rotate(-12)"><rect width="140" height="92" rx="6" fill="#efe2c4"/><path d="M0 6 L70 54 L140 6" fill="none" stroke="#c9b48a" stroke-width="3"/><circle cx="70" cy="56" r="15" fill="#b3202f"/></g><g fill="#ffe7a8"><circle cx="440" cy="120" r="2.5"/><circle cx="640" cy="110" r="2"/><circle cx="610" cy="280" r="2.5"/></g><g fill="#05040a"><circle cx="300" cy="250" r="44"/><path d="M210 500 C210 380 240 310 300 300 C360 310 392 380 392 500 Z"/></g></svg>';
}
function posterHtml(c, small) {
  var cls = POSTER_CLASSES.indexOf(c.poster) > -1 ? c.poster : 'p1';
  return '<div class="poster ' + cls + '"' + (small ? ' style="width:120px;flex:0 0 120px;padding:10px"' : '') + '><span class="perf l"></span><span class="perf r"></span>' +
    (small ? '' : '<span class="tag">' + (c.kind === 'series' ? 'СЕРІАЛ' : 'ФІЛЬМ') + ' · ' + esc(c.level) + '</span>' + (c.lessons_count ? '' : '<span class="tag new">СКОРО</span>')) +
    '<div class="ptitle"' + (small ? ' style="font-size:14px"' : '') + '>' + esc(c.title) + '</div></div>';
}
function catalogGrid(courses) {
  if (!courses.length) return '<div class="empty">Курсів поки немає. Адміністратор може додати їх в адмін-панелі.</div>';
  return '<div class="grid-films">' + courses.map(function (c) {
    return '<a class="film" href="#/course/' + esc(c.id) + '">' + posterHtml(c) + '<div class="film-meta"><span>' + (c.lessons_count || 0) + ' уроків</span><b>' + esc(c.price) + '</b></div></a>';
  }).join('') + '</div>';
}
function pricingHtml() {
  var s = SETTINGS;
  return '<div class="prices">' + [1,2,3].map(function (i) {
    var best = i === 2;
    return '<div class="price' + (best ? ' best' : '') + '">' + (best ? '<span class="ribbon">НАЙПОПУЛЯРНІШИЙ</span>' : '') +
      '<span class="eyebrow">' + esc(s['plan' + i + '_name']) + '</span><div class="amount">' + esc(s['plan' + i + '_price']) + '</div><p class="muted">&nbsp;</p><ul>' +
      String(s['plan' + i + '_text'] || '').split('\n').filter(Boolean).map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') +
      '</ul><a class="btn ' + (best ? 'btn-red' : 'btn-ghost') + '" href="#/buy">Купити ключ</a></div>';
  }).join('') + '</div>';
}
function faqHtml() {
  return '<div class="faq">' + String(SETTINGS.faq || '').split('\n').filter(Boolean).map(function (line, i) {
    var p = line.split('|'); return '<details' + (i === 0 ? ' open' : '') + '><summary>' + esc(p[0]) + '</summary><p>' + esc(p.slice(1).join('|')) + '</p></details>';
  }).join('') + '</div>';
}

function viewHome() {
  return API.listCourses(false).then(function (courses) {
    var s = SETTINGS;
    $app.innerHTML =
      '<section class="hero"><div><div class="eyebrow">' + esc(s.hero_eyebrow) + '</div>' +
      '<h1 style="margin-top:18px"><span class="w">' + esc(s.hero_w1) + '</span><span class="w">' + esc(s.hero_w2) + '</span><span class="w">' + esc(s.hero_w3) + '</span></h1>' +
      '<div class="hero-sub">WATCH · UNDERSTAND · SPEAK</div><p class="lead">' + esc(s.hero_lead) + '</p>' +
      '<div class="hero-cta"><a class="btn btn-red" href="' + (USER ? '#/cabinet' : '#/register') + '"><span class="play"></span>' + (USER ? 'Мій кабінет' : 'Створити кабінет') + '</a><a class="btn btn-ghost" href="#/trial">Пробний урок безкоштовно</a></div>' +
      '<div class="hero-meta"><div><b>15 хв</b>на день</div><div><b>' + courses.length + '</b>марафонів</div><div><b>6 типів</b>завдань</div></div></div>' +
      '<div><div class="screen">' + heroSvg() + '<div class="tc"><i></i>REC · 00:14:32</div><div class="lvl">SUBTITLES CHALLENGE · A2</div><div class="sub">You are a <span class="gap">wizard</span>, Harry.</div><div class="progressbar"><i></i></div></div></div></section>' +
      '<section><div class="sec-head"><div class="eyebrow">Як це працює</div><h2>Від квитка до першої розмови</h2></div><div class="steps">' +
      [['Купуєш ключ','Обираєш фільм, пакет або підписку.'],['Активуєш','Вводиш код у кабінеті.'],['Відкриваєш марафон','Уроки за сценами фільму.'],['Виконуєш завдання','Слова, аудіо, субтитри, граматика, говоріння.'],['Бачиш прогрес','Статистика й бали в кабінеті.']].map(function (x) { return '<div class="step"><h3>' + x[0] + '</h3><p>' + x[1] + '</p></div>'; }).join('') +
      '</div></section>' +
      '<section><div class="sec-head"><div class="eyebrow">Каталог</div><h2>Фільми та серіали</h2></div>' + catalogGrid(courses) + '</section>' +
      '<section id="pricing"><div class="sec-head"><div class="eyebrow">Тарифи</div><h2>Обери свій квиток</h2></div>' + pricingHtml() + '</section>' +
      '<section><div class="sec-head"><div class="eyebrow">FAQ</div><h2>Питання та відповіді</h2></div>' + faqHtml() + '</section>';
  });
}
function viewCatalog() { return API.listCourses(false).then(function (c) { $app.innerHTML = '<div class="page"><div class="sec-head"><div class="eyebrow">Каталог</div><h2>Фільми та серіали</h2></div>' + catalogGrid(c) + '</div>'; }); }
function viewPricing() { $app.innerHTML = '<div class="page"><div class="sec-head"><div class="eyebrow">Тарифи</div><h2>Обери свій квиток</h2></div>' + pricingHtml() + '<div class="sec-head" style="margin-top:30px"><h2>Питання та відповіді</h2></div>' + faqHtml() + '</div>'; return Promise.resolve(); }
function viewBuy() {
  $app.innerHTML = '<div class="page"><div class="sec-head"><div class="eyebrow">Купівля ключа</div><h2>Як отримати ключ доступу</h2><p class="lead">' + esc(SETTINGS.buy_info) + '</p></div>' + pricingHtml() +
    '<div class="panel" style="max-width:560px"><h3>Уже маєш ключ?</h3><p class="muted" style="margin-block:8px 14px">Активуй його в особистому кабінеті.</p><a class="btn btn-red" href="' + (USER ? '#/cabinet' : '#/register') + '">' + (USER ? 'Перейти до кабінету' : 'Створити кабінет') + '</a></div></div>';
  return Promise.resolve();
}

function viewAuth(mode) {
  if (USER) { location.hash = '#/cabinet'; return Promise.resolve(); }
  var reg = mode === 'register';
  $app.innerHTML = '<div class="page"><div class="authbox panel"><div class="eyebrow">' + (reg ? 'Новий кабінет' : 'Вхід') + '</div><h2 style="font-size:32px;margin-block:10px 20px">' + (reg ? 'Створи свій кабінет' : 'З поверненням!') + '</h2>' +
    '<form class="form" id="authForm" novalidate>' +
    (reg ? '<label class="fl" for="aName">Ім\'я<input class="inp-s" id="aName" autocomplete="name" required></label>' : '') +
    '<label class="fl" for="aEmail">Пошта<input class="inp-s" id="aEmail" type="email" autocomplete="email" required></label>' +
    '<label class="fl" for="aPass">Пароль' + (reg ? ' (мінімум 6 символів)' : '') + '<input class="inp-s" id="aPass" type="password" autocomplete="' + (reg ? 'new-password' : 'current-password') + '" required></label>' +
    '<button class="btn btn-red" type="submit" style="justify-content:center">' + (reg ? 'Зареєструватися' : 'Увійти') + '</button><div class="msg" id="aMsg" role="status"></div></form>' +
    '<p class="muted small" style="margin-top:14px">' + (reg ? 'Вже є акаунт? <a href="#/login">Увійти</a>' : 'Ще немає акаунта? <a href="#/register">Створити кабінет</a>') + '</p>' +
    (API.mode === 'demo' && !reg ? '<p class="hint" style="margin-top:10px">Демо: адмін admin@movielang.demo / admin123, учень olena@example.com / demo123</p>' : '') + '</div></div>';
  document.getElementById('authForm').onsubmit = function (e) {
    e.preventDefault();
    var email = document.getElementById('aEmail').value, pass = document.getElementById('aPass').value, msg = document.getElementById('aMsg');
    var name = reg ? document.getElementById('aName').value.trim() : '';
    if (!/^\S+@\S+\.\S+$/.test(email)) { msg.className = 'msg err'; msg.textContent = 'Введи коректну пошту, напр. name@gmail.com'; return; }
    if (pass.length < 6) { msg.className = 'msg err'; msg.textContent = 'Пароль має містити щонайменше 6 символів.'; return; }
    if (reg && !name) { msg.className = 'msg err'; msg.textContent = 'Вкажи своє ім\'я.'; return; }
    msg.className = 'msg'; msg.textContent = 'Зачекай…';
    (reg ? API.signUp(email, pass, name) : API.signIn(email, pass)).then(function (u) {
      USER = u; renderNav(); toast(reg ? 'Кабінет створено!' : 'Вхід виконано'); location.hash = u && u.role === 'admin' ? '#/admin' : '#/cabinet';
    }).catch(function (err) { msg.className = 'msg err'; msg.textContent = err.message; });
  };
  return Promise.resolve();
}

function requireUser() { if (!USER) { location.hash = '#/login'; toast('Спершу увійди в акаунт'); return false; } return true; }

function viewCabinet() {
  if (!requireUser()) return Promise.resolve();
  return Promise.all([API.listCourses(true), API.myEnrollments(), API.myProgress()]).then(function (r) {
    var courses = r[0], enr = r[1], prog = r[2];
    var lessonPromises = enr.map(function (cid) { return API.listLessons(cid); });
    return Promise.all(lessonPromises).then(function (lessonLists) {
      var doneIds = {}; prog.forEach(function (p) { doneIds[p.lesson_id] = p; });
      var avg = prog.length ? Math.round(prog.reduce(function (a, p) { return a + (+p.score || 0); }, 0) / prog.length) : 0;
      var xp = prog.reduce(function (a, p) { return a + Math.round((+p.score || 0) / 10) * 10; }, 0);
      var days = {}; prog.forEach(function (p) { days[(p.completed_at || '').slice(0, 10)] = 1; });
      var allLessons = {}; lessonLists.forEach(function (ls) { ls.forEach(function (l) { allLessons[l.id] = l; }); });
      var my = enr.map(function (cid, i) { var c = courses.filter(function (x) { return x.id === cid; })[0]; if (!c) return ''; var ls = lessonLists[i], d = ls.filter(function (l) { return doneIds[l.id]; }).length, pct = ls.length ? Math.round(d / ls.length * 100) : 0;
        return '<a href="#/course/' + esc(c.id) + '" style="text-decoration:none" class="prog"><div class="top"><span>' + esc(c.title) + '</span><b>' + d + ' / ' + ls.length + '</b></div><div class="bar"><i style="width:' + pct + '%;background:' + (pct === 100 ? 'var(--ok)' : 'linear-gradient(90deg,var(--red),var(--violet))') + '"></i></div></a>'; }).join('');
      var recent = prog.slice().sort(function (a, b) { return (b.completed_at || '').localeCompare(a.completed_at || ''); }).slice(0, 6).map(function (p) { var l = allLessons[p.lesson_id]; return '<div><span>' + esc(l ? l.num + '. ' + l.title : 'Урок') + '</span><b class="score">' + esc(p.score) + '%</b></div>'; }).join('');
      var medals = [[prog.length >= 1, '1', 'Перший урок'], [prog.length >= 5, '5', 'П\'ять уроків'], [Object.keys(days).length >= 3, '3🔥', 'Три дні навчання'], [avg >= 90 && prog.length > 0, '★', 'Точність 90%+'], [enr.length >= 2, '2', 'Два марафони'], [lessonLists.some(function (ls) { return ls.length && ls.every(function (l) { return doneIds[l.id]; }); }), '🏁', 'Марафон пройдено']];
      $app.innerHTML = '<div class="page"><div class="sec-head"><div class="eyebrow">Особистий кабінет</div><h2>Привіт, ' + esc(USER.name) + '!</h2></div>' +
        '<div class="dash"><aside class="dside"><div class="user"><div class="ava">' + esc(USER.name[0].toUpperCase()) + '</div><div><b>' + esc(USER.name) + '</b><small>' + esc(USER.email) + '</small></div></div>' +
        '<form class="form" id="keyForm" novalidate><label class="fl" for="keyInput">Активувати ключ<input class="inp" id="keyInput" placeholder="XXXX-XXXX-XXXX" maxlength="14" autocomplete="off" style="font-size:15px;padding:11px 12px"></label><button class="btn btn-red btn-sm" type="submit" style="justify-content:center">Активувати</button><div class="msg small" id="keyMsg" role="status"></div>' +
        (API.mode === 'demo' ? '<p class="hint">Демо-ключ: HPS1-7KQ4-WZ9M</p>' : '') + '</form>' +
        (USER.role === 'admin' ? '<a class="btn btn-ghost btn-sm" href="#/admin" style="justify-content:center">Адмін-панель</a>' : '') + '</aside>' +
        '<div class="dmain"><div class="stats"><div class="stat"><b>' + prog.length + '</b><span>уроків пройдено</span></div><div class="stat"><b>' + avg + '%</b><span>середній бал</span></div><div class="stat"><b>' + xp + '</b><span>XP набрано</span></div><div class="stat"><b>' + Object.keys(days).length + '</b><span>днів навчання</span></div></div>' +
        '<div class="rows"><div class="box"><h4>Мої марафони</h4>' + (my || '<div class="empty small">Марафонів ще немає. Активуй ключ або <a href="#/trial">пройди пробний урок</a>.</div>') + '<a class="btn btn-ghost btn-sm" href="#/catalog" style="justify-self:start">Каталог курсів</a></div>' +
        '<div class="box"><h4>Досягнення</h4><div class="ach">' + medals.map(function (m) { return '<div class="medal' + (m[0] ? '' : ' off') + '"><span class="m" style="border-color:' + (m[0] ? 'var(--gold)' : 'var(--dim)') + ';color:' + (m[0] ? 'var(--gold)' : 'var(--dim)') + '">' + m[1] + '</span>' + m[2] + '</div>'; }).join('') + '</div>' +
        '<h4>Останні уроки</h4><div class="done-list">' + (recent || '<span class="muted">Ще немає пройдених уроків</span>') + '</div></div></div></div></div></div>';
      var inp = document.getElementById('keyInput'), msg = document.getElementById('keyMsg');
      inp.oninput = function () { var v = inp.value.toUpperCase().replace(/[^A-Z0-9]/g, '').slice(0, 12); inp.value = v.replace(/(.{4})(?=.)/g, '$1-'); };
      document.getElementById('keyForm').onsubmit = function (e) {
        e.preventDefault();
        if (inp.value.replace(/-/g, '').length !== 12) { msg.className = 'msg small err'; msg.textContent = 'Ключ має містити 12 символів.'; return; }
        API.activateKey(inp.value).then(function (res) {
          if (res.ok) { toast('Ключ активовано! Марафон відкрито.'); route(); } else { msg.className = 'msg small err'; msg.textContent = res.msg; }
        }).catch(function (err) { msg.className = 'msg small err'; msg.textContent = err.message; });
      };
    });
  });
}

function viewCourse(id) {
  return Promise.all([API.getCourse(id), API.listLessons(id), API.myEnrollments(), API.myProgress()]).then(function (r) {
    var c = r[0], ls = r[1], enrolled = r[2].indexOf(id) > -1 || (USER && USER.role === 'admin'), done = {};
    if (!c) { $app.innerHTML = '<div class="page"><div class="empty">Курс не знайдено. <a href="#/catalog">До каталогу</a></div></div>'; return; }
    r[3].forEach(function (p) { done[p.lesson_id] = p; });
    var types = {}; ls.forEach(function (l) { (l.tasks || []).forEach(function (t) { types[t.type] = 1; }); });
    $app.innerHTML = '<div class="page"><div class="mcard"><div class="panel"><div class="mhead">' + posterHtml(c, true) + '<div class="mhead-info"><div class="badges"><span class="badge hot">' + esc(c.level) + '</span><span class="badge">' + ls.length + ' уроків</span><span class="badge">' + (c.kind === 'series' ? 'серіал' : 'фільм') + '</span>' + (enrolled ? '<span class="badge" style="color:var(--ok)">доступ відкрито</span>' : '') + '</div>' +
      '<h2 style="font-size:clamp(24px,3.4vw,36px)">' + esc(c.title) + '</h2><p class="muted">' + esc(c.description) + '</p>' +
      (enrolled ? '' : '<div class="row"><a class="btn btn-red" href="#/buy">Купити ключ · ' + esc(c.price) + '</a>' + (USER ? '<a class="btn btn-ghost" href="#/cabinet">Активувати ключ</a>' : '<a class="btn btn-ghost" href="#/register">Створити кабінет</a>') + '</div>') + '</div></div>' +
      (ls.length ? '<ul class="lessons">' + ls.map(function (l, i) {
        var open = enrolled || i === 0, isDone = done[l.id];
        var inner = '<li class="' + (isDone ? 'done' : '') + '"><span class="lnum">' + (isDone ? '✓ ' : '') + String(l.num).padStart(2, '0') + '</span><span class="ltitle">' + esc(l.title) + '<small>' + esc(l.grammar) + (i === 0 && !enrolled ? ' · безкоштовно' : '') + '</small></span>' + (open ? (isDone ? '<b class="score">' + isDone.score + '%</b>' : '<span class="lock" style="color:var(--neon)">▶</span>') : '<span class="lock">🔒</span>') + '</li>';
        return open ? '<a class="lesson-link" href="#/lesson/' + esc(l.id) + '">' + inner + '</a>' : inner;
      }).join('') + '</ul>' : '<div class="empty" style="margin-top:20px">Уроки цього марафону скоро з\'являться.</div>') +
      '</div><div class="panel"><h3 style="margin-bottom:18px">Типи завдань у курсі</h3><div class="task-types">' + Object.keys(types).map(function (t) { return '<div class="ttype"><span class="k q">' + esc(t.slice(0, 2).toUpperCase()) + '</span><div><b>' + esc(TASK_TYPES[t] || t) + '</b></div></div>'; }).join('') + '</div></div></div></div>';
  });
}

/* ---------- lesson player ---------- */
function runPlayer(container, lesson, onFinish) {
  var tasks = lesson.tasks || [], cur = 0, res = [], finalText = '';
  container.innerHTML = '<div class="trial"><div class="tcard" id="tcard" aria-live="polite"></div><div class="tside" id="tside"></div></div>';
  var card = container.querySelector('#tcard'), side = container.querySelector('#tside');
  function renderSide() { side.innerHTML = tasks.map(function (t, i) { var c = i === cur ? 'on' : ''; if (res[i] === true) c += ' ok'; if (res[i] === false) c += ' bad'; return '<div class="tstep ' + c + '"><i>' + (i + 1) + '</i>' + esc(TASK_TYPES[t.type] || t.type) + '</div>'; }).join(''); }
  function qHtml(t) { return esc(t.q).replace(/&lt;(\/?)(b|i)&gt;/g, '<$1$2>').replace(/_{3,}/g, '<span class="gap">____</span>'); }
  function render() {
    var t = tasks[cur]; renderSide();
    var h = '<div class="ttop"><span class="ttag">' + esc(TASK_TYPES[t.type] || t.type) + '</span><span class="tcount">Завдання ' + (cur + 1) + ' з ' + tasks.length + '</span></div>' + (t.scene ? '<div class="tscene"><b>Сцена:</b> ' + esc(t.scene) + '</div>' : '') + '<div class="tq">' + qHtml(t) + '</div>';
    if (t.say) h += '<div><button class="speak" type="button" id="tsay"><span class="play"></span>Прослухати</button></div>';
    if (t.type === 'final') h += '<textarea class="inp-s" id="tfinal" rows="6" placeholder="My favourite scene is…"></textarea><div class="row"><button class="btn btn-red" type="button" id="tsubmit">Зберегти відповідь</button><span class="hint" id="wc">0 слів</span></div>';
    else if (t.type === 'speaking' || !(t.options && t.options.length)) h += '<div class="topts"><button class="topt" type="button" data-s="1">✓ Я повторив(ла)</button><button class="topt" type="button" data-s="0">Пропустити</button></div>';
    else h += '<div class="topts">' + t.options.map(function (o, i) { return '<button class="topt" type="button" data-i="' + i + '">' + esc(o) + '</button>'; }).join('') + '</div>';
    h += '<div class="tfb" id="tfb"></div><div class="tnav"><span class="hint">Підказки українською, завдання англійською</span><button class="btn btn-red" type="button" id="tnext" hidden>Далі</button></div>';
    card.innerHTML = h;
    var sb = card.querySelector('#tsay'); if (sb) sb.onclick = function () { say(t.say); };
    card.querySelectorAll('.topt').forEach(function (b) { b.onclick = function () { answer(b); }; });
    var ta = card.querySelector('#tfinal');
    if (ta) { ta.oninput = function () { card.querySelector('#wc').textContent = (ta.value.trim().split(/\s+/).filter(Boolean).length) + ' слів'; };
      card.querySelector('#tsubmit').onclick = function () { var n = ta.value.trim().split(/\s+/).filter(Boolean).length; if (n < 20) { var fb = card.querySelector('#tfb'); fb.className = 'tfb err'; fb.textContent = 'Напиши хоча б 20 слів (зараз ' + n + ').'; return; } finalText = ta.value.trim(); done(true, 'Відповідь збережено! ' + (t.tip || '')); }; }
  }
  function done(ok, text) {
    res[cur] = ok; var fb = card.querySelector('#tfb'); fb.className = 'tfb ' + (ok ? 'ok' : 'err'); fb.textContent = text;
    card.querySelectorAll('.topt,#tsubmit').forEach(function (x) { x.disabled = true; });
    renderSide(); var n = card.querySelector('#tnext'); n.hidden = false; n.textContent = cur < tasks.length - 1 ? 'Далі' : 'Показати результат'; n.onclick = next; n.focus();
  }
  function answer(b) {
    var t = tasks[cur], ok;
    if (b.dataset.s != null) ok = b.dataset.s === '1';
    else { ok = +b.dataset.i === +t.answer; card.querySelectorAll('.topt').forEach(function (x) { if (+x.dataset.i === +t.answer) x.classList.add('right'); }); if (!ok) b.classList.add('wrong'); var g = card.querySelector('.gap'); if (g) g.textContent = t.options[t.answer]; }
    done(ok, (ok ? 'Правильно! ' : 'Майже. ') + (t.tip || ''));
  }
  function next() { if (cur < tasks.length - 1) { cur++; render(); } else finish(); }
  function finish() {
    var sc = res.filter(Boolean).length, pct = tasks.length ? Math.round(sc / tasks.length * 100) : 0; cur = tasks.length; renderSide();
    card.innerHTML = '<div class="tres"><span class="ttag">РЕЗУЛЬТАТ</span><div class="big">' + sc + ' / ' + tasks.length + '</div><p class="lead" style="text-align:center" id="tresText">Бал: ' + pct + '%</p><div class="row" style="justify-content:center" id="tresBtns"></div></div>';
    onFinish(pct, finalText, card.querySelector('#tresText'), card.querySelector('#tresBtns'), function () { cur = 0; res = []; render(); });
  }
  if (!tasks.length) { card.innerHTML = '<div class="empty">У цьому уроці ще немає завдань.</div>'; return; }
  render();
}

function viewLesson(id) {
  return API.getLesson(id).then(function (l) {
    if (!l) { $app.innerHTML = '<div class="page"><div class="empty">Урок не знайдено.</div></div>'; return; }
    return Promise.all([API.getCourse(l.course_id), API.listLessons(l.course_id), API.myEnrollments()]).then(function (r) {
      var c = r[0], ls = r[1], enrolled = r[2].indexOf(l.course_id) > -1 || (USER && USER.role === 'admin');
      var isFirst = ls.length && ls[0].id === l.id, idx = ls.map(function (x) { return x.id; }).indexOf(l.id), nextL = ls[idx + 1];
      if (!enrolled && !isFirst) { $app.innerHTML = '<div class="page"><div class="empty">Цей урок відкривається після активації ключа. <a href="#/course/' + esc(l.course_id) + '">До марафону</a></div></div>'; return; }
      $app.innerHTML = '<div class="page"><div class="sec-head"><a href="#/course/' + esc(l.course_id) + '" class="muted small">← ' + esc(c ? c.title : 'Марафон') + '</a><div class="eyebrow">Урок ' + l.num + ' · ' + esc(l.grammar) + '</div><h2>' + esc(l.title) + '</h2><p class="lead">' + esc(l.scene) + '</p></div><div id="player"></div></div>';
      runPlayer(document.getElementById('player'), l, function (pct, finalText, textEl, btns, again) {
        if (USER) { API.saveProgress(l.id, pct, finalText).then(function () { textEl.textContent = 'Бал: ' + pct + '%. Результат збережено в кабінеті.'; }); }
        else textEl.textContent = 'Бал: ' + pct + '%. Створи кабінет, щоб зберігати прогрес.';
        btns.innerHTML = (nextL && enrolled ? '<a class="btn btn-red" href="#/lesson/' + esc(nextL.id) + '">Наступний урок</a>' : (!enrolled ? '<a class="btn btn-red" href="#/buy">Отримати ключ доступу</a>' : '')) + '<a class="btn btn-ghost" href="' + (USER ? '#/cabinet' : '#/register') + '">' + (USER ? 'Мій кабінет' : 'Створити кабінет') + '</a><button class="btn btn-ghost" type="button" id="again">Пройти ще раз</button>';
        btns.querySelector('#again').onclick = again;
      });
    });
  });
}

function viewTrial() {
  return API.listCourses(false).then(function (cs) {
    var c = cs.filter(function (x) { return x.lessons_count; })[0];
    if (!c) { $app.innerHTML = '<div class="page"><div class="empty">Пробний урок з\'явиться, щойно буде створено перший курс.</div></div>'; return; }
    return API.listLessons(c.id).then(function (ls) { location.replace('#/lesson/' + ls[0].id); });
  });
}

/* ================= ADMIN ================= */
var adminTab = 'stats';
function viewAdmin() {
  if (!requireUser()) return Promise.resolve();
  if (USER.role !== 'admin') { $app.innerHTML = '<div class="page"><div class="empty">Ця сторінка доступна лише адміністратору.</div></div>'; return Promise.resolve(); }
  $app.innerHTML = '<div class="page"><div class="sec-head"><div class="eyebrow">Адмін-панель</div><h2>Керування MovieLang</h2></div><div class="tabs" role="tablist">' +
    [['stats','Статистика'],['users','Користувачі'],['courses','Курси й уроки'],['keys','Ключі доступу'],['site','Тексти сайту']].map(function (t) { return '<button class="tab' + (adminTab === t[0] ? ' on' : '') + '" type="button" role="tab" data-t="' + t[0] + '">' + t[1] + '</button>'; }).join('') +
    '</div><div id="adminBody"><p class="muted">Завантаження…</p></div></div>';
  $app.querySelectorAll('.tab').forEach(function (b) { b.onclick = function () { adminTab = b.dataset.t; viewAdmin(); }; });
  var body = document.getElementById('adminBody');
  var f = {stats:adminStats, users:adminUsers, courses:adminCourses, keys:adminKeys, site:adminSite}[adminTab];
  return f(body).catch(function (e) { body.innerHTML = '<div class="empty">Помилка: ' + esc(e.message) + '</div>'; });
}

function adminStats(body) {
  return Promise.all([API.adminData(), API.listCourses(true)]).then(function (r) {
    var d = r[0], cs = r[1], now = Date.now(), wk = 7 * 86400000;
    var students = d.users.filter(function (u) { return u.role !== 'admin'; });
    var newWeek = d.users.filter(function (u) { return now - new Date(u.created_at) < wk; }).length;
    var activated = d.keys.filter(function (k) { return k.activated_by; }).length;
    var avg = d.progress.length ? Math.round(d.progress.reduce(function (a, p) { return a + (+p.score || 0); }, 0) / d.progress.length) : 0;
    var activeWeek = {}; d.progress.forEach(function (p) { if (now - new Date(p.completed_at) < wk) activeWeek[p.user_id] = 1; });
    var perCourse = cs.map(function (c) { return {t:c.title, n:d.enrollments.filter(function (e) { return e.course_id === c.id; }).length}; });
    var maxC = Math.max.apply(null, perCourse.map(function (x) { return x.n; }).concat([1]));
    var daysArr = []; for (var i = 13; i >= 0; i--) { var day = new Date(now - i * 86400000).toISOString().slice(0, 10); daysArr.push({d:day, n:d.progress.filter(function (p) { return (p.completed_at || '').slice(0, 10) === day; }).length}); }
    var maxD = Math.max.apply(null, daysArr.map(function (x) { return x.n; }).concat([1]));
    body.innerHTML = '<div style="display:grid;gap:18px"><div class="stats">' +
      '<div class="stat"><b>' + students.length + '</b><span>учнів усього</span></div><div class="stat"><b>' + newWeek + '</b><span>нових за 7 днів</span></div>' +
      '<div class="stat"><b>' + Object.keys(activeWeek).length + '</b><span>активних за 7 днів</span></div><div class="stat"><b>' + activated + ' / ' + d.keys.length + '</b><span>ключів активовано</span></div></div>' +
      '<div class="stats"><div class="stat"><b>' + d.progress.length + '</b><span>уроків пройдено</span></div><div class="stat"><b>' + avg + '%</b><span>середній бал</span></div><div class="stat"><b>' + cs.length + '</b><span>курсів</span></div><div class="stat"><b>' + d.enrollments.length + '</b><span>записів на курси</span></div></div>' +
      '<div class="rows"><div class="box"><h4>Пройдені уроки за 14 днів</h4><div class="week" style="grid-template-columns:repeat(14,1fr);height:140px">' +
      daysArr.map(function (x, i) { return '<div title="' + x.d + ': ' + x.n + '"><span style="color:var(--muted)">' + (x.n || '') + '</span><i style="height:' + Math.max(3, Math.round(x.n / maxD * 90)) + 'px"' + (i === 13 ? ' class="today"' : '') + '></i>' + x.d.slice(8) + '</div>'; }).join('') +
      '</div></div><div class="box"><h4>Учні за курсами</h4><div class="bars">' + perCourse.map(function (x) { return '<div class="b"><span>' + esc(x.t) + '</span><div class="t"><i style="width:' + Math.round(x.n / maxC * 100) + '%"></i></div><b>' + x.n + '</b></div>'; }).join('') + '</div></div></div>' +
      (API.mode === 'demo' ? '<div><button class="btn btn-danger btn-sm" type="button" id="resetDemo">Скинути демо-дані</button></div>' : '') + '</div>';
    var rd = document.getElementById('resetDemo');
    if (rd) rd.onclick = function () { if (rd.dataset.c) { API.resetDemo().then(function () { USER = null; renderNav(); location.hash = '#/login'; toast('Демо-дані скинуто'); }); } else { rd.dataset.c = 1; rd.textContent = 'Точно скинути? Натисни ще раз'; } };
  });
}

function adminUsers(body) {
  return API.adminData().then(function (d) {
    var rows = d.users.map(function (u) {
      var pr = d.progress.filter(function (p) { return p.user_id === u.id; }), enr = d.enrollments.filter(function (e) { return e.user_id === u.id; }).length;
      var avg = pr.length ? Math.round(pr.reduce(function (a, p) { return a + (+p.score || 0); }, 0) / pr.length) : 0;
      var last = pr.map(function (p) { return p.completed_at; }).sort().pop();
      return '<tr><td><b>' + esc(u.name || '—') + '</b><br><span class="muted small">' + esc(u.email) + '</span></td><td><span class="pill' + (u.role === 'admin' ? ' admin' : '') + '">' + esc(u.role) + '</span></td><td>' + fmtDate(u.created_at) + '</td><td class="num">' + enr + '</td><td class="num">' + pr.length + '</td><td class="num">' + (pr.length ? avg + '%' : '—') + '</td><td>' + fmtDate(last) + '</td><td>' +
        (u.id === USER.id ? '<span class="muted small">це ви</span>' : '<button class="btn btn-ghost btn-sm" type="button" data-role="' + esc(u.id) + '" data-to="' + (u.role === 'admin' ? 'student' : 'admin') + '">' + (u.role === 'admin' ? 'Зробити учнем' : 'Зробити адміном') + '</button>') + '</td></tr>';
    }).join('');
    body.innerHTML = '<p class="muted" style="margin-bottom:14px">Усього: ' + d.users.length + '</p><div class="tbl-wrap"><table class="tbl"><thead><tr><th>Користувач</th><th>Роль</th><th>Реєстрація</th><th>Курсів</th><th>Уроків</th><th>Сер. бал</th><th>Активність</th><th></th></tr></thead><tbody>' + rows + '</tbody></table></div>';
    body.querySelectorAll('[data-role]').forEach(function (b) { b.onclick = function () { API.setRole(b.dataset.role, b.dataset.to).then(function () { toast('Роль змінено'); viewAdmin(); }).catch(function (e) { toast(e.message); }); }; });
  });
}

function adminCourses(body) {
  return API.listCourses(true).then(function (cs) {
    body.innerHTML = '<div class="row" style="justify-content:space-between;margin-bottom:14px"><span class="muted">Курсів: ' + cs.length + '</span><button class="btn btn-red btn-sm" type="button" id="newCourse">+ Новий курс</button></div>' +
      (cs.length ? '<div class="tbl-wrap"><table class="tbl"><thead><tr><th>Курс</th><th>Тип</th><th>Рівень</th><th>Уроків</th><th>Ціна</th><th>Статус</th><th></th></tr></thead><tbody>' + cs.map(function (c) {
        return '<tr><td><b>' + esc(c.title) + '</b></td><td>' + (c.kind === 'series' ? 'Серіал' : 'Фільм') + '</td><td>' + esc(c.level) + '</td><td class="num">' + c.lessons_count + '</td><td>' + esc(c.price) + '</td><td><span class="pill ' + (c.published ? 'ok' : 'warn') + '">' + (c.published ? 'опубліковано' : 'чернетка') + '</span></td><td><button class="btn btn-ghost btn-sm" type="button" data-edit="' + esc(c.id) + '">Редагувати</button></td></tr>';
      }).join('') + '</tbody></table></div>' : '<div class="empty">Курсів ще немає. <button class="btn btn-ghost btn-sm" type="button" id="importSeed">Додати демо-курс «Гаррі Поттер»</button></div>');
    document.getElementById('newCourse').onclick = function () { courseEditor(body, null); };
    body.querySelectorAll('[data-edit]').forEach(function (b) { b.onclick = function () { courseEditor(body, b.dataset.edit); }; });
    var imp = document.getElementById('importSeed');
    if (imp) imp.onclick = function () {
      imp.disabled = true;
      var c = JSON.parse(JSON.stringify(SEED_COURSES[0]));
      API.saveCourse(c).then(function (saved) { return SEED_HP_LESSONS.reduce(function (p, l) { return p.then(function () { var ll = JSON.parse(JSON.stringify(l)); ll.course_id = saved.id; return API.saveLesson(ll); }); }, Promise.resolve()); })
        .then(function () { toast('Демо-курс додано'); viewAdmin(); }).catch(function (e) { toast(e.message); imp.disabled = false; });
    };
  });
}

function courseEditor(body, id) {
  var p = id ? Promise.all([API.getCourse(id), API.listLessons(id)]) : Promise.resolve([{title:'', kind:'film', level:'A2', price:'299 ₴', poster:'p1', published:false, description:'', slug:''}, []]);
  return p.then(function (r) {
    var c = r[0], ls = r[1];
    body.innerHTML = '<div style="display:grid;gap:18px"><button class="btn btn-ghost btn-sm" type="button" id="back" style="justify-self:start">← Усі курси</button>' +
      '<form class="panel form" id="cForm" novalidate><h3>' + (id ? 'Редагування курсу' : 'Новий курс') + '</h3>' +
      '<label class="fl" for="cTitle">Назва<input class="inp-s" id="cTitle" value="' + esc(c.title) + '" required></label>' +
      '<div class="grid3"><label class="fl" for="cKind">Тип<select class="inp-s" id="cKind"><option value="film"' + (c.kind !== 'series' ? ' selected' : '') + '>Фільм</option><option value="series"' + (c.kind === 'series' ? ' selected' : '') + '>Серіал</option></select></label>' +
      '<label class="fl" for="cLevel">Рівень<input class="inp-s" id="cLevel" value="' + esc(c.level) + '"></label><label class="fl" for="cPrice">Ціна<input class="inp-s" id="cPrice" value="' + esc(c.price) + '"></label></div>' +
      '<div class="grid2"><label class="fl" for="cPoster">Колір постера<select class="inp-s" id="cPoster">' + POSTER_CLASSES.map(function (pc, i) { return '<option value="' + pc + '"' + (c.poster === pc ? ' selected' : '') + '>' + ['Фіолетовий','Бордовий','Синій','Зелений','Червоний','Золотий','Індиго','Рожевий'][i] + '</option>'; }).join('') + '</select></label>' +
      '<label class="fl" for="cPub">Статус<select class="inp-s" id="cPub"><option value="1"' + (c.published ? ' selected' : '') + '>Опубліковано</option><option value="0"' + (!c.published ? ' selected' : '') + '>Чернетка</option></select></label></div>' +
      '<label class="fl" for="cDesc">Опис<textarea class="inp-s" id="cDesc">' + esc(c.description) + '</textarea></label>' +
      '<div class="row"><button class="btn btn-red" type="submit">Зберегти курс</button>' + (id ? '<button class="btn btn-danger btn-sm" type="button" id="delC">Видалити курс</button>' : '') + '</div><div class="msg" id="cMsg"></div></form>' +
      (id ? '<div class="panel" style="display:grid;gap:14px"><div class="row" style="justify-content:space-between"><h3>Уроки (' + ls.length + ')</h3><button class="btn btn-red btn-sm" type="button" id="newL">+ Новий урок</button></div>' +
        (ls.length ? '<ul class="lessons" style="margin:0">' + ls.map(function (l) { return '<li><span class="lnum">' + String(l.num).padStart(2, '0') + '</span><span class="ltitle">' + esc(l.title) + '<small>' + esc(l.grammar) + ' · ' + (l.tasks || []).length + ' завдань</small></span><button class="btn btn-ghost btn-sm" type="button" data-l="' + esc(l.id) + '">Редагувати</button></li>'; }).join('') + '</ul>' : '<div class="empty">Додай перший урок.</div>') + '</div>' : '<p class="muted">Після збереження курсу можна буде додавати уроки.</p>') + '</div>';
    document.getElementById('back').onclick = function () { viewAdmin(); };
    document.getElementById('cForm').onsubmit = function (e) {
      e.preventDefault();
      var title = document.getElementById('cTitle').value.trim(), msg = document.getElementById('cMsg');
      if (!title) { msg.className = 'msg err'; msg.textContent = 'Вкажи назву курсу.'; return; }
      var nc = {id:id || undefined, title:title, slug:c.slug || title.toLowerCase().replace(/[^a-z0-9а-яіїєґ]+/gi, '-').slice(0, 60), kind:document.getElementById('cKind').value, level:document.getElementById('cLevel').value, price:document.getElementById('cPrice').value, poster:document.getElementById('cPoster').value, published:document.getElementById('cPub').value === '1', description:document.getElementById('cDesc').value};
      API.saveCourse(nc).then(function (s) { toast('Курс збережено'); courseEditor(body, s.id || id); }).catch(function (err) { msg.className = 'msg err'; msg.textContent = err.message; });
    };
    var dc = document.getElementById('delC');
    if (dc) dc.onclick = function () { if (!dc.dataset.c) { dc.dataset.c = 1; dc.textContent = 'Видалити разом з уроками? Натисни ще раз'; return; } API.deleteCourse(id).then(function () { toast('Курс видалено'); viewAdmin(); }); };
    var nl = document.getElementById('newL');
    if (nl) nl.onclick = function () { lessonEditor(body, id, null, ls.length + 1); };
    body.querySelectorAll('[data-l]').forEach(function (b) { b.onclick = function () { lessonEditor(body, id, b.dataset.l); }; });
  });
}

function lessonEditor(body, courseId, lessonId, nextNum) {
  var p = lessonId ? API.getLesson(lessonId) : Promise.resolve({course_id:courseId, num:nextNum, title:'', grammar:'', scene:'', tasks:[]});
  return p.then(function (l) {
    var tasks = JSON.parse(JSON.stringify(l.tasks || []));
    function taskHtml(t, i) {
      return '<div class="task-edit" data-i="' + i + '"><div class="row" style="justify-content:space-between"><b>Завдання ' + (i + 1) + '</b><button class="btn btn-danger btn-sm" type="button" data-del="' + i + '">Видалити</button></div>' +
        '<div class="grid2"><label class="fl">Тип<select class="inp-s" data-f="type">' + Object.keys(TASK_TYPES).map(function (k) { return '<option value="' + k + '"' + (t.type === k ? ' selected' : '') + '>' + TASK_TYPES[k] + '</option>'; }).join('') + '</select></label>' +
        '<label class="fl">Опис сцени<input class="inp-s" data-f="scene" value="' + esc(t.scene) + '"></label></div>' +
        '<label class="fl">Питання / речення (пропуск позначай ____)<input class="inp-s" data-f="q" value="' + esc(t.q) + '"></label>' +
        '<div class="grid2"><label class="fl">Варіанти через « / »<input class="inp-s" data-f="options" value="' + esc((t.options || []).join(' / ')) + '"></label>' +
        '<label class="fl">Номер правильного варіанта (1, 2, 3…)<input class="inp-s" data-f="answer" type="number" min="1" value="' + ((+t.answer || 0) + 1) + '"></label></div>' +
        '<div class="grid2"><label class="fl">Фраза для озвучення (необов\'язково)<input class="inp-s" data-f="say" value="' + esc(t.say) + '"></label>' +
        '<label class="fl">Пояснення після відповіді<input class="inp-s" data-f="tip" value="' + esc(t.tip) + '"></label></div></div>';
    }
    function collect() {
      body.querySelectorAll('.task-edit').forEach(function (el) {
        var i = +el.dataset.i, t = tasks[i];
        el.querySelectorAll('[data-f]').forEach(function (f) { var k = f.dataset.f, v = f.value; if (k === 'options') t.options = v.split('/').map(function (x) { return x.trim(); }).filter(Boolean); else if (k === 'answer') t.answer = Math.max(0, (parseInt(v, 10) || 1) - 1); else if (k === 'say') { if (v.trim()) t.say = v.trim(); else delete t.say; } else t[k] = v; });
      });
    }
    function render() {
      body.innerHTML = '<div style="display:grid;gap:18px"><button class="btn btn-ghost btn-sm" type="button" id="backC" style="justify-self:start">← До курсу</button>' +
        '<form class="panel form" id="lForm" novalidate><h3>' + (lessonId ? 'Редагування уроку' : 'Новий урок') + '</h3>' +
        '<div class="grid3"><label class="fl" for="lNum">Номер<input class="inp-s" id="lNum" type="number" min="1" value="' + esc(l.num) + '"></label><label class="fl" for="lTitle" style="grid-column:span 2">Назва уроку<input class="inp-s" id="lTitle" value="' + esc(l.title) + '"></label></div>' +
        '<div class="grid2"><label class="fl" for="lGr">Граматика / тема<input class="inp-s" id="lGr" value="' + esc(l.grammar) + '"></label><label class="fl" for="lScene">Сцена (опис своїми словами)<input class="inp-s" id="lScene" value="' + esc(l.scene) + '"></label></div>' +
        '<h3 style="margin-top:8px">Завдання (' + tasks.length + ')</h3>' + tasks.map(taskHtml).join('') +
        '<button class="btn btn-ghost btn-sm" type="button" id="addT" style="justify-self:start">+ Додати завдання</button>' +
        '<div class="row"><button class="btn btn-red" type="submit">Зберегти урок</button>' + (lessonId ? '<a class="btn btn-ghost btn-sm" href="#/lesson/' + esc(lessonId) + '">Переглянути як учень</a><button class="btn btn-danger btn-sm" type="button" id="delL">Видалити урок</button>' : '') + '</div><div class="msg" id="lMsg"></div></form></div>';
      document.getElementById('backC').onclick = function () { courseEditor(body, courseId); };
      document.getElementById('addT').onclick = function () { collect(); tasks.push({type:'quiz', scene:'', q:'', options:[], answer:0, tip:''}); render(); };
      body.querySelectorAll('[data-del]').forEach(function (b) { b.onclick = function () { collect(); tasks.splice(+b.dataset.del, 1); render(); }; });
      document.getElementById('lForm').onsubmit = function (e) {
        e.preventDefault(); collect();
        var msg = document.getElementById('lMsg'), title = document.getElementById('lTitle').value.trim();
        if (!title) { msg.className = 'msg err'; msg.textContent = 'Вкажи назву уроку.'; return; }
        var bad = tasks.filter(function (t) { return !t.q.trim(); }).length;
        if (bad) { msg.className = 'msg err'; msg.textContent = 'У ' + bad + ' завданні(ях) порожнє питання.'; return; }
        var nl = {id:lessonId || undefined, course_id:courseId, num:parseInt(document.getElementById('lNum').value, 10) || 1, title:title, grammar:document.getElementById('lGr').value, scene:document.getElementById('lScene').value, tasks:tasks};
        API.saveLesson(nl).then(function () { toast('Урок збережено'); courseEditor(body, courseId); }).catch(function (err) { msg.className = 'msg err'; msg.textContent = err.message; });
      };
      var dl = document.getElementById('delL');
      if (dl) dl.onclick = function () { if (!dl.dataset.c) { dl.dataset.c = 1; dl.textContent = 'Точно видалити? Натисни ще раз'; return; } API.deleteLesson(lessonId).then(function () { toast('Урок видалено'); courseEditor(body, courseId); }); };
    }
    render();
  });
}

function adminKeys(body) {
  return Promise.all([API.adminData(), API.listCourses(true)]).then(function (r) {
    var d = r[0], cs = r[1], cname = {}, uname = {};
    cs.forEach(function (c) { cname[c.id] = c.title; }); d.users.forEach(function (u) { uname[u.id] = u.email; });
    var keys = d.keys.slice().sort(function (a, b) { return (b.created_at || '').localeCompare(a.created_at || ''); });
    body.innerHTML = '<form class="panel form" id="kForm" novalidate style="margin-bottom:18px"><h3>Згенерувати ключі</h3><div class="grid3"><label class="fl" for="kCourse">Курс<select class="inp-s" id="kCourse"><option value="">Усі курси (підписка)</option>' + cs.map(function (c) { return '<option value="' + esc(c.id) + '">' + esc(c.title) + '</option>'; }).join('') + '</select></label>' +
      '<label class="fl" for="kN">Кількість<input class="inp-s" id="kN" type="number" min="1" max="100" value="5"></label><div style="align-self:end"><button class="btn btn-red" type="submit">Створити</button></div></div><div id="kNew"></div></form>' +
      '<div class="tbl-wrap"><table class="tbl"><thead><tr><th>Ключ</th><th>Курс</th><th>Створено</th><th>Статус</th><th></th></tr></thead><tbody>' + keys.map(function (k) {
        return '<tr><td style="font-family:var(--f-mono)">' + esc(k.code) + '</td><td>' + esc(k.course_id ? (cname[k.course_id] || '—') : 'Усі курси') + '</td><td>' + fmtDate(k.created_at) + '</td><td>' + (k.activated_by ? '<span class="pill ok">активовано</span><br><span class="muted small">' + esc(uname[k.activated_by] || '') + ', ' + fmtDate(k.activated_at) + '</span>' : '<span class="pill warn">вільний</span>') + '</td><td>' + (k.activated_by ? '' : '<button class="btn btn-ghost btn-sm" type="button" data-copy="' + esc(k.code) + '">Копіювати</button> <button class="btn btn-danger btn-sm" type="button" data-kdel="' + esc(k.code) + '">Видалити</button>') + '</td></tr>';
      }).join('') + '</tbody></table></div>';
    document.getElementById('kForm').onsubmit = function (e) {
      e.preventDefault();
      var n = Math.min(100, Math.max(1, parseInt(document.getElementById('kN').value, 10) || 1));
      API.createKeys(document.getElementById('kCourse').value, n).then(function (ks) { toast('Створено ключів: ' + ks.length); viewAdmin().then(function () { var box = document.getElementById('kNew'); if (box) box.innerHTML = '<p class="muted small" style="margin-top:10px">Нові ключі:</p><pre style="font-family:var(--f-mono);color:var(--neon);white-space:pre-wrap;user-select:all">' + ks.map(function (k) { return esc(k.code); }).join('\n') + '</pre>'; }); }).catch(function (err) { toast(err.message); });
    };
    body.querySelectorAll('[data-copy]').forEach(function (b) { b.onclick = function () { var c = b.dataset.copy; (navigator.clipboard ? navigator.clipboard.writeText(c) : Promise.reject()).then(function () { toast('Скопійовано: ' + c); }).catch(function () { toast('Ключ: ' + c); }); }; });
    body.querySelectorAll('[data-kdel]').forEach(function (b) { b.onclick = function () { if (!b.dataset.c) { b.dataset.c = 1; b.textContent = 'Точно?'; return; } API.deleteKey(b.dataset.kdel).then(function () { toast('Ключ видалено'); viewAdmin(); }); }; });
  });
}

function adminSite(body) {
  return API.getSettings().then(function (s) {
    var fields = [['hero_eyebrow','Надзаголовок головної','input'],['hero_w1','Заголовок, слово 1','input'],['hero_w2','Заголовок, слово 2','input'],['hero_w3','Заголовок, слово 3','input'],['hero_lead','Опис під заголовком','textarea'],
      ['plan1_name','Тариф 1: назва','input'],['plan1_price','Тариф 1: ціна','input'],['plan1_text','Тариф 1: пункти (кожен з нового рядка)','textarea'],
      ['plan2_name','Тариф 2: назва','input'],['plan2_price','Тариф 2: ціна','input'],['plan2_text','Тариф 2: пункти','textarea'],
      ['plan3_name','Тариф 3: назва','input'],['plan3_price','Тариф 3: ціна','input'],['plan3_text','Тариф 3: пункти','textarea'],
      ['buy_info','Як купити ключ (текст на сторінці покупки)','textarea'],['faq','FAQ: кожен рядок «Питання|Відповідь»','textarea']];
    body.innerHTML = '<form class="panel form" id="sForm" novalidate><h3>Тексти на сайті</h3><p class="muted small">Зміни одразу з\'являться на головній, у тарифах і FAQ.</p>' +
      fields.map(function (f) { var id = 's_' + f[0]; return '<label class="fl" for="' + id + '">' + f[1] + (f[2] === 'textarea' ? '<textarea class="inp-s" id="' + id + '" rows="' + (f[0] === 'faq' ? 8 : 4) + '">' + esc(s[f[0]]) + '</textarea>' : '<input class="inp-s" id="' + id + '" value="' + esc(s[f[0]]) + '">') + '</label>'; }).join('') +
      '<div class="row"><button class="btn btn-red" type="submit">Зберегти зміни</button><a class="btn btn-ghost btn-sm" href="#/">Переглянути сайт</a></div></form>';
    document.getElementById('sForm').onsubmit = function (e) {
      e.preventDefault(); var o = {};
      fields.forEach(function (f) { o[f[0]] = document.getElementById('s_' + f[0]).value; });
      API.saveSettings(o).then(function () { SETTINGS = Object.assign({}, SETTINGS, o); toast('Тексти сайту збережено'); }).catch(function (err) { toast(err.message); });
    };
  });
}

/* ================= router ================= */
function route() {
  var h = location.hash.replace(/^#\/?/, ''), parts = h.split('/'), p;
  window.scrollTo(0, 0);
  switch (parts[0]) {
    case '': p = viewHome(); break;
    case 'catalog': p = viewCatalog(); break;
    case 'pricing': p = viewPricing(); break;
    case 'buy': p = viewBuy(); break;
    case 'trial': p = viewTrial(); break;
    case 'login': p = viewAuth('login'); break;
    case 'register': p = viewAuth('register'); break;
    case 'cabinet': p = viewCabinet(); break;
    case 'course': p = viewCourse(parts[1]); break;
    case 'lesson': p = viewLesson(parts[1]); break;
    case 'admin': p = viewAdmin(); break;
    default: $app.innerHTML = '<div class="page"><div class="empty">Сторінку не знайдено. <a href="#/">На головну</a></div></div>'; p = Promise.resolve();
  }
  Promise.resolve(p).catch(function (e) { $app.innerHTML = '<div class="page"><div class="empty">Помилка: ' + esc(e.message) + '</div></div>'; });
}
window.addEventListener('hashchange', route);
$app.innerHTML = '<div class="page"><p class="muted">Завантаження…</p></div>';
Promise.all([API.getUser().catch(function () { return null; }), API.getSettings().catch(function () { return DEFAULT_SETTINGS; })]).then(function (r) {
  USER = r[0]; SETTINGS = r[1]; renderNav(); route();
});
})();
