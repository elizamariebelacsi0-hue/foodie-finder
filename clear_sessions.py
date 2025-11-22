#!/usr/bin/env python
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodie_finder.settings')
django.setup()

from django.contrib.sessions.models import Session

# Clear all sessions
Session.objects.all().delete()
print("All sessions cleared successfully!")