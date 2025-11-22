# Generated migration for restaurant coordinates

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_add_dish_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=11.5564, max_digits=9),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=124.2595, max_digits=9),
        ),
    ]