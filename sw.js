/* Офлайн-кэш: сеть-сначала (свежая версия при интернете, кэш — без интернета) */
var CACHE='app-cache-v1';
self.addEventListener('install',function(e){self.skipWaiting();});
self.addEventListener('activate',function(e){e.waitUntil(self.clients.claim());});
self.addEventListener('fetch',function(e){
  if(e.request.method!=='GET')return;
  e.respondWith(
    fetch(e.request).then(function(resp){
      try{var copy=resp.clone();caches.open(CACHE).then(function(c){c.put(e.request,copy);});}catch(_){}
      return resp;
    }).catch(function(){
      return caches.match(e.request).then(function(r){return r||caches.match('index.html')||caches.match('./');});
    })
  );
});
