"""
WSGI config for HamsterKombat project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

environ_mode = os.environ.get('DJANGO_ENVIRON_MODE','local')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"hamster_kombat.settings.{environ_mode}")

application = get_wsgi_application()
