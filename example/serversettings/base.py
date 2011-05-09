import os
import logging

gettext = lambda s: s

#PROJECT
PROJECT_PATH = os.sep.join(os.path.abspath(os.path.dirname(__file__)).split(os.sep)[:-1])
PROJECT_ROOT = os.sep.join(os.path.abspath(os.path.dirname(__file__)).split(os.sep)[:-2])

#MEDIA
SITE_PREFIX_URL = '/'
MEDIA_ROOT = os.path.join(PROJECT_PATH,"media/",)
MEDIA_URL = SITE_PREFIX_URL + 'media/'
ADMIN_MEDIA_PREFIX = STATIC_URL + '/admin/'

#STATIC
STATIC_ROOT = os.path.join(PROJECT_PATH,"layout/",)
STATIC_URL = SITE_PREFIX_URL + 'layout/'
STATICFILES_DIRS = (
    ("layout", os.path.join(PROJECT_ROOT, "layout",)),
)

#DEBUG
PATH_TO_DEBUG_LOG = os.path.join(PROJECT_ROOT, 'logs', 'debug.log' )
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = (
    ('Christian Verkerk', 'christian@changer.nl'),
)
MANAGERS = ADMINS

#DATABASES
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME':     '',                         # Or path to database file if using sqlite3.
        'USER':     '',                         # Not used with sqlite3.
        'PASSWORD': 'joopiedepopie',            # Not used with sqlite3.
        'HOST':     '',                         # Set to empty string for localhost. Not used with sqlite3.
        'PORT':     '',                         # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Amsterdam'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale

# Make this unique, and don't share it with anybody.
SECRET_KEY = '%4%a_d$$!%6b@##$hxe-u=^b6%%un&*1o(&s67$m+4^&=ly$td'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'example.urls'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
)
TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH,"templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    
    'example.main',
)