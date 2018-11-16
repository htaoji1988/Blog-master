"""
WSGI config for Blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""
import sys
import os

sys.path.append('/opt/web-app/Blog-master')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Blog.settings")

application = get_wsgi_application()
