import sys

from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'PORT': '5432',
        'NAME': 'homegarden',
        'USER': 'postgres',
        'PASSWORD': 'abcd1234',
        'OPTIONS': {
            # "autocommit": True,
        },
    }
}

BASE_URL = "http://localhost:8000/"

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
#             'datefmt' : "%d/%b/%Y %H:%M:%S"
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'handlers': {
#         'file': {
#             'level': 'WARNING',
#             'class': 'logging.FileHandler',
#             'filename': '_temp/logs/app.log',
#             'formatter': 'verbose'
#         },
#         'mail_admins':{
#             'level':'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'include_html': True,
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers':['file'],
#             'propagate': True,
#             'level':'WARNING',
#         },
#         '_main': {
#             'handlers': ['file'],
#             'level': 'WARNING',
#         },
#     }
# }

