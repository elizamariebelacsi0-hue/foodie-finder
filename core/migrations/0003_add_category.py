from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0002_seed_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='category',
            field=models.CharField(default='Fast Food', max_length=40),
        ),
    ]
