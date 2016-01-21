from .base import *


INSTALLED_APPS += ('import_export',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_mtvmcotizacion',
        'USER': 'root',
        'PASSWORD': 'md123',
        'HOST': '',
        'PORT': '',
    }
}
