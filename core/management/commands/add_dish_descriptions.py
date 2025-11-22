from django.core.management.base import BaseCommand
from core.models import Dish

class Command(BaseCommand):
    help = 'Add sample descriptions to existing dishes'

    def handle(self, *args, **options):
        # Sample descriptions for common Filipino dishes
        descriptions = {
            'Adobo': 'Traditional Filipino dish with tender chicken or pork braised in soy sauce, vinegar, and garlic',
            'Lechon': 'Crispy roasted whole pig, a Filipino festive centerpiece with golden crackling skin',
            'Sinigang': 'Sour soup with tamarind broth, vegetables, and your choice of pork, beef, or shrimp',
            'Pancit': 'Stir-fried noodles with vegetables and meat, a Filipino birthday tradition',
            'Lumpia': 'Fresh or fried spring rolls filled with vegetables and meat, served with sweet sauce',
            'Kare-Kare': 'Rich peanut stew with oxtail and vegetables, served with shrimp paste',
            'Sisig': 'Sizzling dish made from chopped pig face and liver, seasoned with onions and chili',
            'Halo-Halo': 'Popular Filipino dessert with shaved ice, mixed beans, fruits, and ice cream',
            'Chicken BBQ': 'Grilled chicken marinated in sweet and savory sauce, served with rice',
            'Pork BBQ': 'Tender grilled pork skewers with sweet barbecue glaze',
            'Beef Steak': 'Filipino-style beef steak with onions and soy-citrus marinade',
            'Fish Fillet': 'Fresh fish fillet grilled or fried to perfection',
            'Fried Rice': 'Garlic fried rice with eggs and your choice of meat or seafood',
            'Burger': 'Juicy beef patty with fresh lettuce, tomato, and special sauce',
            'Pizza': 'Wood-fired pizza with fresh toppings and melted cheese',
            'Pasta': 'Italian-style pasta with your choice of sauce and toppings',
            'Salad': 'Fresh mixed greens with vegetables and house dressing',
            'Soup': 'Hearty soup made with fresh ingredients and aromatic herbs',
            'Rice': 'Steamed jasmine rice, perfect companion to any dish',
            'Chicken': 'Tender chicken prepared with Filipino spices and herbs'
        }

        updated_count = 0
        for dish in Dish.objects.all():
            # Check if dish name contains any of our keywords
            for keyword, description in descriptions.items():
                if keyword.lower() in dish.name.lower() and not dish.description:
                    dish.description = description
                    dish.save()
                    updated_count += 1
                    self.stdout.write(f'Updated {dish.name}: {description}')
                    break

        self.stdout.write(
            self.style.SUCCESS(f'Successfully updated {updated_count} dishes with descriptions')
        )