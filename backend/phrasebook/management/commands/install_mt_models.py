from django.core.management.base import BaseCommand

from phrasebook.machine_translate import MT_LANGUAGES, ensure_installed


class Command(BaseCommand):
    help = "Download and install the local machine-translation models (English/Hindi/Spanish/French)."

    def handle(self, *args, **options):
        self.stdout.write(f"Installing machine-translation models for: {', '.join(sorted(MT_LANGUAGES))}...")
        ensure_installed()
        self.stdout.write(self.style.SUCCESS("Machine-translation models installed."))
