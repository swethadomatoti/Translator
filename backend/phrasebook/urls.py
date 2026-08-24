from django.urls import path

from .views import LanguageListView, PhraseChipsView, TranslateView

urlpatterns = [
    path('languages/', LanguageListView.as_view(), name='languages'),
    path('phrases/', PhraseChipsView.as_view(), name='phrases'),
    path('translate/', TranslateView.as_view(), name='translate'),
]
