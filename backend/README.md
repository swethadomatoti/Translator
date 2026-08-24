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
