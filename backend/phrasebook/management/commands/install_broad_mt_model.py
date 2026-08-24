from django.core.management.base import BaseCommand

from phrasebook.broad_translate import MODEL_NAME, _get_model


class Command(BaseCommand):
    help = "Download and cache the broad-coverage NLLB-200 translation model (~2.4GB)."

    def handle(self, *args, **options):
        self.stdout.write(f"Downloading {MODEL_NAME}...")
        _get_model()
        self.stdout.write(self.style.SUCCESS("Broad-coverage translation model installed."))
