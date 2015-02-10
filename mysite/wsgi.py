"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('/Applications/djangostack-1.6.10-0/apps/django/django_projects/mysite')
os.environ.setdefault("PYTHON_EGG_CACHE", "/Applications/djangostack-1.6.10-0/apps/django/django_projects/mysite/egg_cache")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
