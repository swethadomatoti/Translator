from rest_framework.response import Response
from rest_framework.views import APIView

from . import machine_translate
from .matching import find_phrase
from .models import Language, Phrase
from .serializers import LanguageSerializer


class LanguageListView(APIView):
    def get(self, request):
        languages = Language.objects.all()
        return Response(LanguageSerializer(languages, many=True).data)


class PhraseChipsView(APIView):
    def get(self, request):
        lang = request.query_params.get('lang', 'en')
        phrases = Phrase.objects.all()
        chips = [
            {'slug': p.slug, 'text': p.translations[lang]}
            for p in phrases if lang in p.translations
        ][:10]
        return Response(chips)


class TranslateView(APIView):
    def post(self, request):
        text = (request.data.get('text') or '').strip()
        from_code = request.data.get('from')
        to_code = request.data.get('to')

        if not from_code or not to_code:
            return Response({'status': 'error', 'message': "'from' and 'to' language codes are required."}, status=400)

        if not text:
            return Response({'status': 'empty'})

        phrase = find_phrase(text, from_code)
        if not phrase:
            if machine_translate.supports(from_code, to_code):
                translation = machine_translate.translate(text, from_code, to_code)
                if translation:
                    return Response({'status': 'ok', 'translation': translation, 'source': 'machine_translation'})
            return Response({'status': 'no-match'})

        translation = phrase.translations.get(to_code)
        if not translation:
            phrasebook_names = list(
                Language.objects.filter(is_phrasebook=True).values_list('name', flat=True)
            )
            return Response({'status': 'unsupported', 'phrasebook_languages': phrasebook_names})

        return Response({'status': 'ok', 'translation': translation, 'phrase_slug': phrase.slug})
