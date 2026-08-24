from django.core.management.base import BaseCommand
from django.db import transaction

from phrasebook.data import LANGUAGES, PHRASES
from phrasebook.models import Language, Phrase


class Command(BaseCommand):
    help = "Seed (or re-seed) the Language and Phrase tables from phrasebook/data.py"

    @transaction.atomic
    def handle(self, *args, **options):
        Language.objects.all().delete()
        Phrase.objects.all().delete()

        for order, lang in enumerate(LANGUAGES):
            Language.objects.create(order=order, **lang)

        for order, phrase in enumerate(PHRASES):
            Phrase.objects.create(order=order, **phrase)

        self.stdout.write(self.style.SUCCESS(
            f"Seeded {len(LANGUAGES)} languages and {len(PHRASES)} phrases."
        ))
