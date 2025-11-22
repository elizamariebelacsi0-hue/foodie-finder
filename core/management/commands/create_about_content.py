from django.core.management.base import BaseCommand
from core.models import AboutContent

class Command(BaseCommand):
    help = 'Create default AboutContent instance'

    def handle(self, *args, **options):
        if not AboutContent.objects.exists():
            AboutContent.objects.create()
            self.stdout.write(
                self.style.SUCCESS('Successfully created AboutContent instance')
            )
        else:
            self.stdout.write(
                self.style.WARNING('AboutContent instance already exists')
            )