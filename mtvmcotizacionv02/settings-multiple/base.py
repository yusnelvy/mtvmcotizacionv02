"""
Django settings for mtvmcotizacion project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z)sr!is=6dk1x82ajleb$wbqmen^cyrb1_jb7xjw0385mfzb%8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = False

# Redirect when login is correct.
LOGIN_REDIRECT_URL = "/home"

# Redirect when login is not correct.
LOGIN_URL = '/'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack',
    'ambiente',
    'cliente',
    'contenido',
    'cotizacion',
    'direccion',
    'inicio',
    'mueble',
    'presupuesto',
    'servicio',
    'telefono',
    'trabajador',
    'formtools',
    'premisas',
    'presupuesto.templatetags',
    'gestiondocumento'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'whoosh_index'),
    },
}

# CONFIGURACIÓN DE TEMPLATES:
# Es una secuencia de valores agrupados llamados procesadores
# de contexto - que tienen un objeto de solicitud
# como su argumento y devuelven un diccionario de temas que se
# fusionó con el contexto
#
TEMPLATES = [
    {
        # BACKEND: Referencia directa al Django's template backend API
        # En el caso de conectar Jinja2 hay que hacer referencia
        # con django.template.backends.jinja2.Jinja2.
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # DIRS: Lista de directorios donde el engine debe encontrar
        # los archivos de Templates
        'DIRS': [
            os.path.join(os.path.dirname(os.path.dirname(__file__)), 'template').replace('\\', '/'),
        ],
        # APP_DIRS: Lista de directorios donde se deben buscar los
        # templates específicos de aplicaciones en una carpeta llamada
        # templates en la raíz de cada aplicación.
        'APP_DIRS': True,
        # OPTIONS: Permite especificar opciones específicas del BackEnd
        'OPTIONS': {
            # 'loaders': []
            # Los loaders son los módulos que permiten cargar las aplicaciones
            # El estándar de loaders carga lo siguiente:
            # ('django.template.loaders.filesystem.Loader',
            # 'django.template.loaders.app_directories.Loader')
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'mtvmcotizacion.views.sidebar'
            ]
            # 'allowed_include_roots': [
            #
            # ]
        },
    },
]

ALLOWED_HOSTS = ['*']

ROOT_URLCONF = 'mtvmcotizacion.urls'

WSGI_APPLICATION = 'mtvmcotizacion.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

USE_TZ = True

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

# Configuraciones referidas al formato de fechas, horas y números
# USE_L10N Indica si el formato local será utilizado o no

USE_L10N = True

USE_THOUSAND_SEPARATOR = True

NUMBER_GROUPING = 3

DATE_INPUT_FORMATS = (
    '%Y-%m-%d',     # '2006-10-25'
    '%m/%d/%Y',     # '10/25/2006'
    '%m/%d/%y',     # '10/25/06'
    '%d-%m-%Y',     # '25-10-2006'
    '%d/%m/%Y',     # '25/10/2006'
    '%Y/%m/%d',     # '2006/10/25'
    '%b %d %Y',     # 'Oct 25 2006'
    '%b %d, %Y',    # 'Oct 25, 2006'
    '%d %b %Y',     # '25 Oct 2006'
    '%d %b, %Y',    # '25 Oct, 2006'
    '%B %d %Y',     # 'October 25 2006'
    '%B %d, %Y',    # 'October 25, 2006'
    '%d %B %Y',     # '25 October 2006'
    '%d %B, %Y',    # '25 October, 2006'
)

DATETIME_INPUT_FORMATS = (
    '%d-%m-%Y %H:%M:%S',     # '25-10-2006 14:30:59'
    '%d-%m-%Y %H:%M:%S.%f',  # '25-10-2006 14:30:59.000200'
    '%d-%m-%Y %H:%M',        # '25-10-2006 14:30'
    '%d-%m-%Y,'              # '25-10-2006'
    '%Y-%m-%d %H:%M:%S',     # '25-10-2006 14:30:59'
    '%Y-%m-%d %H:%M:%S.%f',  # '25-10-2006 14:30:59.000200'
    '%Y-%m-%d %H:%M',        # '25-10-2006 14:30'
    '%Y-%m-%d',              # '25-10-2006'
    '%Y-%m-%d %H:%M:%S',     # '2006-10-25 14:30:59'
    '%Y-%m-%d %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
    '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
    '%Y-%m-%d',              # '2006-10-25'
    '%m/%d/%Y %H:%M:%S',     # '10/25/2006 14:30:59'
    '%m/%d/%Y %H:%M:%S.%f',  # '10/25/2006 14:30:59.000200'
    '%m/%d/%Y %H:%M',        # '10/25/2006 14:30'
    '%m/%d/%Y',              # '10/25/2006'
    '%m/%d/%y %H:%M:%S',     # '10/25/06 14:30:59'
    '%m/%d/%y %H:%M:%S.%f',  # '10/25/06 14:30:59.000200'
    '%m/%d/%y %H:%M',        # '10/25/06 14:30'
    '%m/%d/%y',              # '10/25/06'
)

# Configuración de email
EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = 'desarrollomtvm@gmail.com'

EMAIL_HOST_PASSWORD = 'mtvmudarte'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

STATIC_URL = '/static/'
STATIC_ROOT = ''

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    )
