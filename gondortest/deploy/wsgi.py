import os, sys

from django.core.handlers.wsgi import WSGIHandler
os.environ["DJANGO_SETTINGS_MODULE"] = "gondortest.settings"
application = WSGIHandler()
