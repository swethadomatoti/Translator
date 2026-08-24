from rest_framework import serializers

from .models import Language, Phrase


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['code', 'name', 'native', 'bcp47', 'group', 'is_phrasebook']


class PhraseChipSerializer(serializers.Serializer):
    slug = serializers.CharField()
    text = serializers.CharField()
