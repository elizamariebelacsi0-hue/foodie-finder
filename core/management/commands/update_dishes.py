from django.core.management.base import BaseCommand
from core.models import Dish, Category

class Command(BaseCommand):
    help = 'Update dishes with descriptions and categories'

    def handle(self, *args, **options):
        # Create default categories if they don't exist
        categories = ['Breakfast', 'Lunch', 'Dinner', 'Snack', 'Dessert', 'Beverage']
        for cat_name in categories:
            Category.objects.get_or_create(name=cat_name)
        
        # Update dishes without descriptions
        dishes_updated = 0
        for dish in Dish.objects.all():
            if not dish.description:
                dish.description = f"Delicious {dish.name} served at {dish.restaurant.name}"
                dish.save()
                dishes_updated += 1
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully updated {dishes_updated} dishes with descriptions')
        )