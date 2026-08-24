const BASE_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api';

async function request(path, options) {
  const res = await fetch(`${BASE_URL}${path}`, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  });
  if (!res.ok) {
    throw new Error(`Request to ${path} failed with ${res.status}`);
  }
  return res.json();
}

export function fetchLanguages() {
  return request('/languages/');
}

export function fetchPhraseChips(lang) {
  return request(`/phrases/?lang=${encodeURIComponent(lang)}`);
}

export function translate({ text, from, to }) {
  return request('/translate/', {
    method: 'POST',
    body: JSON.stringify({ text, from, to }),
  });
}
