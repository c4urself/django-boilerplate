import sys
import os
import site

PROJECT_NAME = 'compass'
TLD = 'nl'
PYTHON_VERSION = '2.6'

# set old sys.path
prev_sys_path = list(sys.path)

# site packages from virtualenv added to sys.path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

sitesdir = '%(PROJECT_ROOT)s/env-%(PROJECT_NAME)s/lib/python%(PYTHON_VERSION)s/site-packages' % {'PROJECT_ROOT': PROJECT_ROOT,
                                                                                                 'PROJECT_NAME': PROJECT_NAME,
                                                                                                 'TLD': TLD,
                                                                                                 'PYTHON_VERSION': PYTHON_VERSION}
site.addsitedir(sitesdir)
# website added to sys.path
sys.path.append(PROJECT_ROOT)

## reorder sys.path so that virtualenv packages show up first and are thereby 'leading'
# get a list of 'new' items
new_sys_path = [p for p in sys.path if p not in prev_sys_path]
# remove 'new' items to add them to front
for item in new_sys_path:
    sys.path.remove(item)
sys.path[0:0] = new_sys_path
#sys.path[0:0] = ['/Library/Python/2.6/site-packages/PIL']

os.environ['DJANGO_SETTINGS_MODULE'] = '%s.settings' % PROJECT_NAME
os.environ['PYTHON_EGG_CACHE'] = '/tmp' if os != 'nt' else 'C:\Temp'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

