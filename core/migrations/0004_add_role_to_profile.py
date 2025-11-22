# Generated manually for role-based authentication

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_add_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('user', 'User'), ('restaurant', 'Restaurant'), ('admin', 'Admin')], default='user', max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='restaurant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.restaurant'),
        ),
    ]