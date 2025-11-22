from django.db import migrations
from django.utils import timezone


def seed_forward(apps, schema_editor):
    Restaurant = apps.get_model('core', 'Restaurant')
    Dish = apps.get_model('core', 'Dish')

    # Create six featured restaurants in Naval Proper
    restos = []
    names = [
        'Naval Bites', 'Seaside Grill', 'Bamboo Kitchen',
        'Island Eats', 'Harbor Diner', 'Plaza Cafe'
    ]
    categories = ['Fast Food', 'Seafood', 'Asian', 'Fast Food', 'Diner', 'Dessert']
    for idx, name in enumerate(names):
        r = Restaurant.objects.create(
            name=name,
            location='Naval Proper',
            open_time=timezone.now().replace(hour=9, minute=0, second=0, microsecond=0).time(),
            close_time=timezone.now().replace(hour=21, minute=0, second=0, microsecond=0).time(),
            description='A beloved local spot serving favorites and comfort food.',
            featured=True,
            category=categories[idx],
        )
        restos.append(r)

    sample_dishes = [
        ('Adobo', 149.00), ('Sinigang', 199.00), ('Sisig', 249.00),
        ('Pancit', 129.00), ('Halo-Halo', 89.00), ('Chicken Inasal', 189.00),
    ]

    for i, r in enumerate(restos):
        for name, price in sample_dishes:
            Dish.objects.create(name=name, price=price + i * 10, restaurant=r)


def seed_backward(apps, schema_editor):
    Restaurant = apps.get_model('core', 'Restaurant')
    Dish = apps.get_model('core', 'Dish')
    Dish.objects.all().delete()
    Restaurant.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_forward, seed_backward),
    ]


