from django.contrib import admin

from .models import Language, Phrase


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'native', 'group', 'is_phrasebook', 'order']
    list_filter = ['group', 'is_phrasebook']
    search_fields = ['code', 'name', 'native']


@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin):
    list_display = ['slug', 'order']
    search_fields = ['slug']
