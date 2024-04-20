"""
WSGI config for server_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""
#Este archivo se usa para subir a producción tratándose de una aplicación síncrona
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server_django.settings')

application = get_wsgi_application()
