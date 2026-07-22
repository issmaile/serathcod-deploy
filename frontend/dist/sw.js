const CACHE_NAME = 'serathcod-v1';
const STATIC_ASSETS = ['/','/index.html','/manifest.json','/icon-192.png','/icon-512.png'];
self.addEventListener('install',(e)=>{e.waitUntil(caches.open(CACHE_NAME).then(c=>c.addAll(STATIC_ASSETS)));self.skipWaiting()});
self.addEventListener('activate',(e)=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==CACHE_NAME).map(x=>caches.delete(x)))));self.clients.claim()});
self.addEventListener('fetch',(e)=>{if(e.request.method!=='GET')return;e.respondWith(caches.match(e.request).then(c=>{const f=fetch(e.request).then(r=>{if(r.status===200){const cl=r.clone();caches.open(CACHE_NAME).then(ca=>ca.put(e.request,cl))}return r});return c||f}))});
