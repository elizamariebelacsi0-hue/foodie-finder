"""
WSGI config for foodie_finder project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Use production settings if RENDER environment variable is present
if 'RENDER' in os.environ:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodie_finder.settings_production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodie_finder.settings')

application = get_wsgi_application()
