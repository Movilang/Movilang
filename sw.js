/* MoviLang service worker
   - pliki z wersją (?v=…) i /assets/: od razu z pamięci, a w tle odświeżenie (stale-while-revalidate) — powrót na stronę jest natychmiastowy
   - strona (index) i reszta: sieć najpierw, pamięć jako zapas offline */
var C = 'ml-v2';
self.addEventListener('install', function (e) { self.skipWaiting(); e.waitUntil(caches.open(C).then(function (c) { return c.addAll(['/', '/assets/favicon.svg']).catch(function () {}); })); });
self.addEventListener('activate', function (e) { e.waitUntil(caches.keys().then(function (ks) { return Promise.all(ks.filter(function (k) { return k !== C; }).map(function (k) { return caches.delete(k); })); }).then(function () { return self.clients.claim(); })); });
function put(r, res) { if (res && res.ok) { var cp = res.clone(); caches.open(C).then(function (c) { c.put(r, cp); }); } return res; }
self.addEventListener('fetch', function (e) {
  var r = e.request, u = new URL(r.url);
  if (r.method !== 'GET' || u.origin !== location.origin) return;
  if (/^\/assets\//.test(u.pathname) || /[?&]v=\d/.test(u.search)) {
    e.respondWith(caches.match(r).then(function (m) {
      var net = fetch(r).then(function (res) { return put(r, res); });
      if (m) { e.waitUntil(net.catch(function () {})); return m; }
      return net;
    }));
    return;
  }
  e.respondWith(fetch(r).then(function (res) { return put(r, res); }).catch(function () { return caches.match(r).then(function (m) { return m || caches.match('/'); }); }));
});
