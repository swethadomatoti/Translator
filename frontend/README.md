# Bhasha frontend (React + Vite)

The Bhasha offline-phrasebook UI, wired to the Django backend for translation.

## Setup

```bash
cd frontend
npm install
npm run dev
```

Runs at `http://localhost:5173`. Requires the backend running at the URL in
`.env` (defaults to `http://127.0.0.1:8000/api`) — see `../backend/README.md`.

## Structure

- `src/App.jsx` — top-level state: languages, route, source text, translation output, banner
- `src/api.js` — fetch helpers for `/languages/`, `/phrases/`, `/translate/`
- `src/components/` — `HeroBand`, `LanguageBar`, `TranslatorPanel`, `Chips`, `Banner`, `Footer`, `Icons`
- `src/hooks/useHoldToTalk.js` — Web Speech API hold-to-talk mic input
- `src/hooks/useSpeech.js` — `speechSynthesis`-based "Listen" playback
- `src/index.css` — theme tokens (light/dark) and component styles, ported 1:1 from the design mockup

## Notes

- Hold-to-talk and photo capture rely on browser microphone/camera
  permissions and may be unavailable in some browsers.
- Photo capture only previews the image — Bhasha doesn't do OCR, matching the
  original design's scope.
