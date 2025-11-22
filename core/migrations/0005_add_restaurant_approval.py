# Generated manually for restaurant approval

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_add_role_to_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='is_approved',
            field=models.BooleanField(default=True),
        ),
    ]