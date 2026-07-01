// InvoiceIQ Service Worker — full offline support
// Caches all static assets at install time, serves from cache when offline.
// Only /api/* calls go to the network (they need the backend to work).

const CACHE_NAME = 'invoiceiq-v1';

// Assets to precache on install — the full shell app
const PRECACHE_URLS = [
  '/',
  '/index.html',
  '/manifest.webmanifest',
  '/icon-192.png',
  '/icon-512.png',
  '/maskable-icon-512.png',
  '/favicon.svg',
  '/apple-touch-icon.png',
];

// Install: precache all shell assets
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(PRECACHE_URLS);
    })
  );
  self.skipWaiting();
});

// Activate: clean up old caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    )
  );
  self.clients.claim();
});

// Fetch strategy:
// - /api/* → network only (needs backend)
// - navigation (HTML) → network-first, fall back to cache
// - static assets (JS/CSS/images/fonts) → cache-first, fall back to network
self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);

  // API calls: always hit the network, never cache
  if (url.pathname.startsWith('/api/')) {
    return;
  }

  // Navigation (HTML): try network → fallback to cache
  if (event.request.mode === 'navigate') {
    event.respondWith(
      fetch(event.request).catch(() => caches.match('/index.html'))
    );
    return;
  }

  // Static assets: cache-first, then network to fill cache
  event.respondWith(
    caches.match(event.request).then((cached) => {
      if (cached) return cached;
      return fetch(event.request).then((response) => {
        // Cache successful responses for static assets
        if (response.ok && event.request.method === 'GET') {
          const cloned = response.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(event.request, cloned));
        }
        return response;
      });
    })
  );
});