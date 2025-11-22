# Generated manually for user approval system

from django.db import migrations


def activate_existing_users(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    # Activate all existing users except those with admin emails
    admin_emails = [
        'admin@foodiefinder.com',
        'manager@foodiefinder.com', 
        'supervisor@foodiefinder.com',
        'director@foodiefinder.com',
        'owner@foodiefinder.com'
    ]
    
    for user in User.objects.all():
        if user.email not in admin_emails and not user.is_superuser:
            user.is_active = True
            user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_add_restaurant_approval'),
    ]

    operations = [
        migrations.RunPython(activate_existing_users),
    ]