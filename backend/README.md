# Bhasha backend (Django)

REST API serving the offline-style phrasebook: languages, sample phrase chips,
and phrase-matching translation.

## Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_phrasebook   # loads languages + phrases from phrasebook/data.py
python manage.py runserver 8000
```

The API is served at `http://127.0.0.1:8000/api/`.

## Endpoints

- `GET /api/languages/` — all supported languages (code, name, native name, BCP-47 tag, group, phrasebook flag)
- `GET /api/phrases/?lang=<code>` — up to 10 sample phrases in that language, for the "Try a phrase" chips
- `POST /api/translate/` — body `{ "text": "...", "from": "te", "to": "en" }`, returns:
  - `{ "status": "ok", "translation": "...", "phrase_slug": "..." }`
  - `{ "status": "no-match" }` — phrase isn't in the curated phrasebook
  - `{ "status": "unsupported", "phrasebook_languages": [...] }` — phrase matched, but not translated into the target language
  - `{ "status": "empty" }` — empty text submitted

## Data

`phrasebook/data.py` holds the seed data. Edit it and re-run `seed_phrasebook`
to update, or manage `Language`/`Phrase` rows directly via `/admin/` after
creating a superuser (`python manage.py createsuperuser`).

CORS is open to `http://localhost:5173` / `http://127.0.0.1:5173` (the Vite
dev server) in `config/settings.py`.

## Machine translation fallback

When `/api/translate/` doesn't find an exact phrasebook match, it falls back
to machine translation, tried in two tiers:

1. **Argos Translate** (`machine_translate.py`) — fast, offline, but only
   covers en/hi/es/fr pairs. Install its models with
   `python manage.py install_mt_models`.
2. **NLLB-200** (`broad_translate.py`) — offline, covers all languages in
   `phrasebook/data.py` (including Telugu/Tamil/Kannada/Malayalam, which Argos
   has no models for). Much heavier: ~2.4GB download, noticeably more RAM/CPU
   per request than Argos. Install/cache it with
   `python manage.py install_broad_mt_model`. Run this once during setup/build
   — otherwise it downloads on the first request that needs it, which is slow.

Both are no-API-key, no-cost, fully local models — there's no external
translation service involved.
