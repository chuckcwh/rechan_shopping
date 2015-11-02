import os
from os.path import dirname, abspath, basename, normpath, join
import sys
from django.core.exceptions import ImproperlyConfigured



# Get environment setting or return exception
def get_env_setting(setting, default=None):
    try:
        return os.environ[setting]
    except KeyError:
        if default is None:
            error_msg = "Set the %s env variable" % setting
            raise ImproperlyConfigured(error_msg)
        else:
            return default

DJANGO_ROOT = dirname(dirname(abspath(__file__)))
SITE_ROOT = dirname(DJANGO_ROOT)
BASE_DIR = dirname(DJANGO_ROOT)
SITE_NAME = basename(DJANGO_ROOT)
sys.path.append(DJANGO_ROOT)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# admin account? need test
ADMINS = (
    ('admin', 'password'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3' if 'test' in sys.argv else 'django.db.backends.mysql',
        'NAME': get_env_setting('rechan_DB_NAME', 'rechan_dev'),
        'USER': get_env_setting('rechan_DB_USER', 'root'),
        'PASSWORD': get_env_setting('rechan_DB_PASSWORD', ''),
        'HOST': get_env_setting('rechan_DB_HOST', '127.0.0.1'),
        'PORT': get_env_setting('rechan_DB_PORT', '3306'),
    }
}

TIME_ZONE = 'Asia/Taipei'
LANGUAGE_CODE = 'zh-hant'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))
MEDIA_URL = '/media/'
STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))
STATIC_URL = '/static/'
STATICFILES_DIRS = ()
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = True
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)
COMPRESS_DEBUG_TOGGLE = 'nocompress'
COMPRESS_CSS_HASHING_METHOD = 'content'

SECRET_KEY = '(==8u5k&eq+yefj40o3a_2=t(wip6m^-w@7nm1^b8%6r-fmukk'

# hosts need to be test
ALLOWED_HOSTS = [
    'ec2-52-24-226-149.us-west-2.compute.amazonaws.com',
    '52.24.226.149',
]

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    normpath(join(SITE_ROOT, 'templates')),
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = '%s.urls' % SITE_NAME

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
    'homepage',
    'website',
)

THIRD_PARTY_APPS = (
    'bower',
    'gunicorn',
    'compressor',
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

WSGI_APPLICATION = 'wsgi.application'

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_S3_SECURE_URLS =True
AWS_QUERYSTRING_AUTH = False
AWS_STORAGE_BUCKET_NAME = 'rechan'

DEBUG_TOOLBAR_CONFIG = dict(
    INTERCEPT_REDIRECTS = False,
)

EMAIL_HOST = 'www.rechan.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'service-rechan@gmail.com'
EMAIL_HOST_PASSWORD = 'zoU3TivXZCBK2F0x7QeoSA'

BOWER_INSTALL = 'bower install --allow-root'

FACEBOOK_APP_ID = ''
FACEBOOK_APP_SECRET = ''
FACEBOOK_APP_TOKEN = ''

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake'
    }
}






AUTH_USER_MODEL = 'rechan_shopping.Member'

LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'login'
