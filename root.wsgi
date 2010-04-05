
import os, sys

sys.path.append("/domains/alwaysalwaysnew.pantechnoco.com/libs/")
os.environ['DJANGO_SETTINGS_MODULE'] = 'alwaysalwaysnew.settings'

from django.core.handlers import wsgi
application = wsgi.WSGIHandler()
