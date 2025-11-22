from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Profile, Restaurant


class Command(BaseCommand):
    help = 'Setup user roles and create sample restaurant accounts'

    def handle(self, *args, **options):
        # Create admin profile if it doesn't exist
        admin_users = User.objects.filter(is_superuser=True)
        for admin_user in admin_users:
            profile, created = Profile.objects.get_or_create(user=admin_user)
            if created or profile.role != 'admin':
                profile.role = 'admin'
                profile.save()
                self.stdout.write(f'Set {admin_user.username} as admin')

        # Create sample restaurant accounts
        restaurants = Restaurant.objects.all()[:3]  # Get first 3 restaurants
        
        for i, restaurant in enumerate(restaurants):
            username = f"{restaurant.name.lower().replace(' ', '')}@restaurant.com"
            
            # Create restaurant user if doesn't exist
            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    'email': username,
                    'first_name': restaurant.name,
                    'last_name': 'Restaurant'
                }
            )
            
            if created:
                user.set_password('restaurant123')
                user.save()
                self.stdout.write(f'Created restaurant user: {username}')
            
            # Update profile
            profile, _ = Profile.objects.get_or_create(user=user)
            profile.role = 'restaurant'
            profile.restaurant = restaurant
            profile.save()
            
            self.stdout.write(f'Set {username} as restaurant owner of {restaurant.name}')

        self.stdout.write(self.style.SUCCESS('Successfully setup roles!'))
        self.stdout.write('Restaurant login credentials:')
        for restaurant in restaurants:
            username = f"{restaurant.name.lower().replace(' ', '')}@restaurant.com"
            self.stdout.write(f'  {restaurant.name}: {username} / restaurant123')