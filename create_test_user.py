#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodie_finder.settings_production')
django.setup()

from django.contrib.auth.models import User
from core.models import Profile

# Create test user
email = 'test@example.com'
password = 'testpass123'

if not User.objects.filter(username=email).exists():
    user = User.objects.create_user(
        username=email,
        email=email,
        password=password,
        first_name='Test',
        last_name='User'
    )
    user.is_active = True
    user.save()
    print(f"Test user created: {email} / {password}")
else:
    print("Test user already exists")