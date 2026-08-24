"""Local machine translation fallback for phrasebook misses.

Uses argostranslate (open-source, offline, no API key) to translate between
the language pairs it actually supports. Argos has no Telugu, Tamil, Kannada,
or Malayalam models, so those languages stay phrasebook-only; this only
covers English/Hindi/Spanish/French.
"""
MT_LANGUAGES = {'en', 'hi', 'es', 'fr'}

_installed = False


def supports(from_code, to_code):
    return from_code != to_code and from_code in MT_LANGUAGES and to_code in MT_LANGUAGES


def ensure_installed():
    global _installed
    if _installed:
        return
    import argostranslate.package as package

    installed = {(p.from_code, p.to_code) for p in package.get_installed_packages()}
    needed = {
        (a, b)
        for a in MT_LANGUAGES
        for b in MT_LANGUAGES
        if a != b and (a == 'en' or b == 'en')
    }
    missing = needed - installed
    if not missing:
        _installed = True
        return

    package.update_package_index()
    available = package.get_available_packages()
    still_missing = set()
    for from_code, to_code in missing:
        match = next(
            (p for p in available if p.from_code == from_code and p.to_code == to_code), None
        )
        if not match:
            continue
        for attempt in range(2):
            try:
                package.install_from_path(match.download())
                break
            except Exception:
                if attempt == 1:
                    still_missing.add((from_code, to_code))

    _installed = not still_missing


def translate(text, from_code, to_code):
    """Return translated text, or None if this pair isn't supported."""
    if not supports(from_code, to_code):
        return None

    ensure_installed()
    import argostranslate.translate as translate_mod

    installed_languages = translate_mod.get_installed_languages()
    from_lang = next((l for l in installed_languages if l.code == from_code), None)
    to_lang = next((l for l in installed_languages if l.code == to_code), None)
    if not from_lang or not to_lang:
        return None

    translation = from_lang.get_translation(to_lang)
    if not translation:
        return None
    return translation.translate(text)
