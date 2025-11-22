from django.core.management.base import BaseCommand
from core.models import Dish, DishServing
import random

class Command(BaseCommand):
    help = 'Setup sample dishes with proper serving sizes and pricing'

    def handle(self, *args, **options):
        # Sample serving configurations
        serving_configs = [
            {'solo': 80, 'sharing': 150, 'family': 280},
            {'solo': 120, 'sharing': 220, 'family': 400, 'party': 650},
            {'solo': 95, 'family': 320},
            {'solo': 150, 'sharing': 280},
            {'solo': 60, 'sharing': 110, 'family': 200, 'party': 350},
        ]
        
        dishes_updated = 0
        for dish in Dish.objects.all():
            # Clear existing servings
            dish.servings.all().delete()
            
            # Add random serving configuration
            config = random.choice(serving_configs)
            for serving_size, price in config.items():
                DishServing.objects.create(
                    dish=dish,
                    serving_size=serving_size,
                    price=price + random.randint(-20, 30)  # Add some variation
                )
            
            # Ensure description exists
            if not dish.description:
                dish.description = f"Delicious {dish.name} prepared with fresh ingredients and authentic flavors."
                dish.save()
            
            dishes_updated += 1
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully updated {dishes_updated} dishes with proper serving sizes')
        )