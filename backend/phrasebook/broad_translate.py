"""Broad-coverage machine translation fallback via Meta's NLLB-200 model.

Free and fully offline (no API key), unlike a hosted translation API. Used as
a second-tier fallback behind machine_translate.py (Argos): Argos only covers
en/hi/es/fr, so anything outside that -- including Telugu/Tamil/Kannada/
Malayalam, which Argos has no models for at all -- falls through to here.

Much heavier than Argos: the model is ~2.4GB on first download and needs
noticeably more RAM/CPU per request. See backend/README.md for the resource
implications before enabling this in production.
"""
MODEL_NAME = 'facebook/nllb-200-distilled-600M'

# This app's language codes (phrasebook/data.py) mapped to NLLB's FLORES-200 codes.
FLORES_CODES = {
    'en': 'eng_Latn', 'hi': 'hin_Deva', 'te': 'tel_Telu', 'ta': 'tam_Taml',
    'kn': 'kan_Knda', 'ml': 'mal_Mlym', 'bn': 'ben_Beng', 'mr': 'mar_Deva',
    'gu': 'guj_Gujr', 'pa': 'pan_Guru', 'ur': 'urd_Arab', 'or': 'ory_Orya',
    'as': 'asm_Beng', 'ne': 'npi_Deva', 'si': 'sin_Sinh',
    'zh': 'zho_Hans', 'zhTW': 'zho_Hant', 'ja': 'jpn_Jpan', 'ko': 'kor_Hang',
    'th': 'tha_Thai', 'vi': 'vie_Latn', 'id': 'ind_Latn', 'ms': 'zsm_Latn',
    'tl': 'tgl_Latn', 'my': 'mya_Mymr', 'mn': 'khk_Cyrl',
    'es': 'spa_Latn', 'fr': 'fra_Latn', 'de': 'deu_Latn', 'it': 'ita_Latn',
    'pt': 'por_Latn', 'nl': 'nld_Latn', 'ru': 'rus_Cyrl', 'uk': 'ukr_Cyrl',
    'pl': 'pol_Latn', 'sv': 'swe_Latn', 'no': 'nob_Latn', 'da': 'dan_Latn',
    'fi': 'fin_Latn', 'el': 'ell_Grek', 'cs': 'ces_Latn', 'hu': 'hun_Latn',
    'ro': 'ron_Latn', 'ar': 'arb_Arab', 'he': 'heb_Hebr', 'fa': 'pes_Arab',
    'tr': 'tur_Latn', 'sw': 'swh_Latn', 'zu': 'zul_Latn', 'am': 'amh_Ethi',
}

_tokenizer = None
_model = None


def supports(from_code, to_code):
    return from_code != to_code and from_code in FLORES_CODES and to_code in FLORES_CODES


def _get_model():
    global _tokenizer, _model
    if _model is None:
        from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
        _tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        _model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    return _tokenizer, _model


def translate(text, from_code, to_code):
    """Return translated text, or None if this pair isn't supported or the model fails."""
    if not supports(from_code, to_code):
        return None
    try:
        tokenizer, model = _get_model()
        tokenizer.src_lang = FLORES_CODES[from_code]
        inputs = tokenizer(text, return_tensors='pt')
        tokens = model.generate(
            **inputs,
            forced_bos_token_id=tokenizer.convert_tokens_to_ids(FLORES_CODES[to_code]),
            max_length=400,
        )
        return tokenizer.batch_decode(tokens, skip_special_tokens=True)[0]
    except Exception:
        return None
