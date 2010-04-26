
import sys, os
import __main__

os.chdir("/domains/alwaysalwaysnew.pantechnoco.com/0.11.v.alwaysalwaysnew.pantechnoco.com/")
sys.path.append("/domains/alwaysalwaysnew.pantechnoco.com/0.11.v.alwaysalwaysnew.pantechnoco.com/libs/")
os.environ['DJANGO_SETTINGS_MODULE'] = 'alwaysalwaysnew.settings'

from django.core.handlers import wsgi
application = wsgi.WSGIHandler()
