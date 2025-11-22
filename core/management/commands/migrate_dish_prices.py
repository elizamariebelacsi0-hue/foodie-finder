from django.core.management.base import BaseCommand
from core.models import Dish, DishServing

class Command(BaseCommand):
    help = 'Migrate existing dishes to have default serving sizes'

    def handle(self, *args, **options):
        dishes_updated = 0
        for dish in Dish.objects.all():
            # Check if dish already has servings
            if not dish.servings.exists():
                # Create a default solo serving with price 100 (placeholder)
                DishServing.objects.create(
                    dish=dish,
                    serving_size='solo',
                    price=100.00
                )
                dishes_updated += 1
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created default servings for {dishes_updated} dishes')
        )