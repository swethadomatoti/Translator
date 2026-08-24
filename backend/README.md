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
to **Argos Translate** (`machine_translate.py`) — offline, no API key, but
only covers en/hi/es/fr pairs (Argos has no models for Telugu/Tamil/Kannada/
Malayalam or most other languages in `phrasebook/data.py`). Install its
models with `python manage.py install_mt_models` — run this during
setup/build, not left to happen lazily on the first live request.

`broad_translate.py` and `install_broad_mt_model.py` are an unused,
not-currently-wired-in NLLB-200 based fallback that would cover all
languages. It's disabled: on a small Render instance it caused worker
timeouts and OOM crash loops (~2.4GB model, ~30s load time, ~3GB RAM per
worker), and re-enabling it safely needs pre-loading the model at worker
boot, a much longer gunicorn timeout, and a meaningfully bigger instance.
