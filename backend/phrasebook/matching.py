"""Offline-style phrasebook matching: normalize + exact/transliteration lookup.

Mirrors the client-side matching logic from the original Bhasha mockup so the
API behaves identically whether the match happens in the browser or here.
"""
import re
import unicodedata

from .models import Phrase

_PUNCT_RE = re.compile(r"[.,!?¿¡؛۔]")
_SPACE_RE = re.compile(r"\s+")


def normalize(text):
    text = text.lower()
    text = unicodedata.normalize('NFKC', text)
    text = _PUNCT_RE.sub('', text)
    text = _SPACE_RE.sub(' ', text).strip()
    return text


def find_phrase(text, from_code):
    norm = normalize(text)
    if not norm:
        return None

    phrases = list(Phrase.objects.all())

    for phrase in phrases:
        candidates = []
        translation = phrase.translations.get(from_code)
        if translation:
            candidates.append(normalize(translation))
        for variant in phrase.translit.get(from_code, []):
            candidates.append(normalize(variant))
        if norm in candidates:
            return phrase

    if from_code != 'en':
        for phrase in phrases:
            english = phrase.translations.get('en')
            if english and normalize(english) == norm:
                return phrase

    return None
