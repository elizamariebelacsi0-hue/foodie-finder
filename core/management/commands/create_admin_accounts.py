from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Profile


class Command(BaseCommand):
    help = 'Create 5 admin accounts with predefined emails'

    def handle(self, *args, **options):
        admin_accounts = [
            ('admin@foodiefinder.com', 'Admin', 'User'),
            ('manager@foodiefinder.com', 'Manager', 'User'),
            ('supervisor@foodiefinder.com', 'Supervisor', 'User'),
            ('director@foodiefinder.com', 'Director', 'User'),
            ('owner@foodiefinder.com', 'Owner', 'User'),
        ]
        
        for email, first_name, last_name in admin_accounts:
            user, created = User.objects.get_or_create(
                username=email,
                defaults={
                    'email': email,
                    'first_name': first_name,
                    'last_name': last_name,
                    'is_staff': True,
                    'is_superuser': True
                }
            )
            
            if created:
                user.set_password('admin123')
                user.save()
                self.stdout.write(f'Created admin user: {email}')
            
            # Update profile
            profile, _ = Profile.objects.get_or_create(user=user)
            profile.role = 'admin'
            profile.save()
            
            if not created:
                self.stdout.write(f'Updated existing user: {email}')

        self.stdout.write(self.style.SUCCESS('Admin accounts ready!'))
        self.stdout.write('Login credentials:')
        for email, _, _ in admin_accounts:
            self.stdout.write(f'  {email} / admin123')