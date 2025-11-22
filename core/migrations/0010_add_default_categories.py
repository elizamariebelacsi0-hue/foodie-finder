# Generated manually for default categories

from django.db import migrations


def add_default_categories(apps, schema_editor):
    Category = apps.get_model('core', 'Category')
    
    default_categories = [
        'Breakfast',
        'Lunch', 
        'Dinner',
        'Snack',
        'Drinks',
        'Dessert',
        'Appetizer',
        'Main Course',
        'Side Dish',
        'Soup',
        'Salad',
        'Seafood',
        'Vegetarian',
        'Fast Food',
        'Traditional Filipino',
        'International'
    ]
    
    for category_name in default_categories:
        Category.objects.get_or_create(name=category_name)


def reverse_add_categories(apps, schema_editor):
    Category = apps.get_model('core', 'Category')
    Category.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_category_remove_dish_dish_category_dish_categories'),
    ]

    operations = [
        migrations.RunPython(add_default_categories, reverse_add_categories),
    ]