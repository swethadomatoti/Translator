from django.db import migrations


def seed_languages(apps, schema_editor):
    Language = apps.get_model("phrasebook", "Language")

    languages = [
        ("en", "English", "English", "en-US", "English & Indian languages", True, 0),
        ("hi", "Hindi", "हिन्दी", "hi-IN", "English & Indian languages", True, 1),
        ("te", "Telugu", "తెలుగు", "te-IN", "English & Indian languages", True, 2),
        ("ta", "Tamil", "தமிழ்", "ta-IN", "English & Indian languages", True, 3),
        ("kn", "Kannada", "ಕನ್ನಡ", "kn-IN", "English & Indian languages", True, 4),
        ("ml", "Malayalam", "മലയാളം", "ml-IN", "English & Indian languages", True, 5),
        ("bn", "Bengali", "বাংলা", "bn-IN", "English & Indian languages", False, 6),
        ("mr", "Marathi", "मराठी", "mr-IN", "English & Indian languages", False, 7),
        ("gu", "Gujarati", "ગુજરાતી", "gu-IN", "English & Indian languages", False, 8),
        ("pa", "Punjabi", "ਪੰਜਾਬੀ", "pa-IN", "English & Indian languages", False, 9),
        ("ur", "Urdu", "اردو", "ur-IN", "English & Indian languages", False, 10),
        ("or", "Odia", "ଓଡ଼ିଆ", "or-IN", "English & Indian languages", False, 11),
        ("as", "Assamese", "অসমীয়া", "as-IN", "English & Indian languages", False, 12),
        ("ne", "Nepali", "नेपाली", "ne-NP", "English & Indian languages", False, 13),
        ("si", "Sinhala", "සිංහල", "si-LK", "English & Indian languages", False, 14),

        ("zh", "Chinese (Simplified)", "中文", "zh-CN", "East & Southeast Asia", False, 15),
        ("zhTW", "Chinese (Traditional)", "中文(繁體)", "zh-TW", "East & Southeast Asia", False, 16),
        ("ja", "Japanese", "日本語", "ja-JP", "East & Southeast Asia", False, 17),
        ("ko", "Korean", "한국어", "ko-KR", "East & Southeast Asia", False, 18),
        ("th", "Thai", "ไทย", "th-TH", "East & Southeast Asia", False, 19),
        ("vi", "Vietnamese", "Tiếng Việt", "vi-VN", "East & Southeast Asia", False, 20),
        ("id", "Indonesian", "Bahasa Indonesia", "id-ID", "East & Southeast Asia", False, 21),
        ("ms", "Malay", "Bahasa Melayu", "ms-MY", "East & Southeast Asia", False, 22),
        ("tl", "Filipino", "Filipino", "fil-PH", "East & Southeast Asia", False, 23),
        ("my", "Burmese", "မြန်မာ", "my-MM", "East & Southeast Asia", False, 24),
        ("mn", "Mongolian", "Монгол", "mn-MN", "East & Southeast Asia", False, 25),

        ("es", "Spanish", "Español", "es-ES", "Europe", True, 26),
        ("fr", "French", "Français", "fr-FR", "Europe", True, 27),
        ("de", "German", "Deutsch", "de-DE", "Europe", False, 28),
        ("it", "Italian", "Italiano", "it-IT", "Europe", False, 29),
        ("pt", "Portuguese", "Português", "pt-PT", "Europe", False, 30),
        ("nl", "Dutch", "Nederlands", "nl-NL", "Europe", False, 31),
        ("ru", "Russian", "Русский", "ru-RU", "Europe", False, 32),
        ("uk", "Ukrainian", "Українська", "uk-UA", "Europe", False, 33),
        ("pl", "Polish", "Polski", "pl-PL", "Europe", False, 34),
        ("sv", "Swedish", "Svenska", "sv-SE", "Europe", False, 35),
        ("no", "Norwegian", "Norsk", "nb-NO", "Europe", False, 36),
        ("da", "Danish", "Dansk", "da-DK", "Europe", False, 37),
        ("fi", "Finnish", "Suomi", "fi-FI", "Europe", False, 38),
        ("el", "Greek", "Ελληνικά", "el-GR", "Europe", False, 39),
        ("cs", "Czech", "Čeština", "cs-CZ", "Europe", False, 40),
        ("hu", "Hungarian", "Magyar", "hu-HU", "Europe", False, 41),
        ("ro", "Romanian", "Română", "ro-RO", "Europe", False, 42),

        ("ar", "Arabic", "العربية", "ar-SA", "Middle East & Africa", False, 43),
        ("he", "Hebrew", "עברית", "he-IL", "Middle East & Africa", False, 44),
        ("fa", "Persian", "فارسی", "fa-IR", "Middle East & Africa", False, 45),
        ("tr", "Turkish", "Türkçe", "tr-TR", "Middle East & Africa", False, 46),
        ("sw", "Swahili", "Kiswahili", "sw-KE", "Middle East & Africa", False, 47),
        ("zu", "Zulu", "isiZulu", "zu-ZA", "Middle East & Africa", False, 48),
        ("am", "Amharic", "አማርኛ", "am-ET", "Middle East & Africa", False, 49),
    ]

    for code, name, native, bcp47, group, is_phrasebook, order in languages:
        Language.objects.get_or_create(
            code=code,
            defaults={
                "name": name,
                "native": native,
                "bcp47": bcp47,
                "group": group,
                "is_phrasebook": is_phrasebook,
                "order": order,
            },
        )
def reverse_seed_languages(apps, schema_editor):
    Language = apps.get_model("phrasebook", "Language")

    codes = [
        "en", "hi", "te", "ta", "kn", "ml", "bn", "mr", "gu", "pa",
        "ur", "or", "as", "ne", "si",
        "zh", "zhTW", "ja", "ko", "th", "vi", "id", "ms", "tl", "my", "mn",
        "es", "fr", "de", "it", "pt", "nl", "ru", "uk", "pl", "sv",
        "no", "da", "fi", "el", "cs", "hu", "ro",
        "ar", "he", "fa", "tr", "sw", "zu", "am",
    ]

    Language.objects.filter(code__in=codes).delete()

class Migration(migrations.Migration):

    dependencies = [
        ("phrasebook", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_languages, reverse_seed_languages),
    ]