
"""
Django settings for django_boilerplate project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n8f&s%8p_ul6qa#&n-3e8r*$71qq3y=8aqav0oevqklih1qh@d'

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'django_extensions',
    'debug_toolbar',
    'bootstrap3',
    'gcm',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'model_mommy',
    # 'compressor',

    'apps.account',
    'apps.vegetables',
    'apps.listings',
    'apps.orders',
    'apps.rating',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    "django.contrib.messages.context_processors.messages",
)


COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
}

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'apps.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'
USE_I18N = True
USE_L10N = True
USE_TZ = False

AUTH_USER_MODEL = 'account.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader',
 'django.template.loaders.app_directories.Loader')

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

LOGIN_URL = '/login'

GRAPPELLI_ADMIN_TITLE = "Home Garden Networking"

GCM_APIKEY = "AIzaSyCt3Qr5JoFNO3BqRyWnt_z2yOVhvT6Q1cA"
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'rdtcontacttree@gmail.com'
EMAIL_HOST_PASSWORD = 'invincible123$#'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

SEND_BROKEN_LINK_EMAILS = True

ADMINS = (
    ('Administrator', 'abdulshukoorpk@gmail.com'),
    ('Administrator1', 'navajyothms1989@gmail.com'),
    ('Administrator2','arunghosh@gmail.com'),
    ('Administrator3', 'harry.hvp@gmail.com'),
         )
MANAGERS = ADMINS
SHOW_PERFORM = False
