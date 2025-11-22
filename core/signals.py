from django.db.models.signals import post_save, post_migrate
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, contact_number="")


@receiver(post_migrate)
def ensure_default_admin(sender, **kwargs):
    # Create the one-and-only default admin if none exists
    if not User.objects.filter(is_superuser=True).exists():
        email = 'carlmarco19@gmail.com'
        password = 'carlTzy1902'
        user, _ = User.objects.get_or_create(username=email, defaults={'email': email, 'first_name': 'Admin'})
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

