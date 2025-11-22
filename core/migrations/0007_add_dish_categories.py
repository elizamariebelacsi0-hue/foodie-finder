# Generated manually for dish categories

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_fix_user_approval'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='dish_category',
            field=models.CharField(blank=True, help_text='e.g., Soup, Chicken BBQ, Sinigang na Hipon', max_length=100),
        ),
        migrations.AddField(
            model_name='dish',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]