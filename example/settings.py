#
# 1. Imports base settings from `/settings/base.py`
# 2. Imports settings based on server name, unless:
#     a. The environmental setting `SERVER_TYPE` has been set in the `django.wsgi` script
#     b. The name of the server corresponds to a name in the `DEVELOPMENT_MACHINES` tuple
#
import os
import platform
import sys
import warnings

from django.utils.importlib import import_module

DEVELOPMENT_MACHINES = ('christian-mac',)

def get_server_name():
    server_type = os.environ.get('SERVER_TYPE','')
    server_name = platform.node().split('.')[0]
    if server_type:
        return server_type
    if server_name in DEVELOPMENT_MACHINES:
        return 'local'
    else:
        return server_name
    
def override_settings(dottedpath):
    
    #sys.path.append(os.sep.join(os.path.abspath(os.path.dirname(__file__)).split(os.sep)[:-2]))
    #sys.path.append(os.sep.join(os.path.abspath(os.path.dirname(__file__)).split(os.sep)[:-1]))
    sys.path.append(os.path.abspath(os.path.dirname(__file__)))
    
    try:
        _module = import_module(dottedpath)
    except ImportError, e:
        warnings.warn("Failed to import %s" % dottedpath)
        warnings.warn("Exact error was: %s" % e)
    else:
        _thismodule = sys.modules[__name__]
        for _keyword in dir(_module):
            if _keyword.isupper() and not _keyword.startswith('__'):
                setattr(_thismodule, _keyword, getattr(_module, _keyword))

override_settings('serversettings.base')
override_settings('serversettings.%s' % get_server_name())