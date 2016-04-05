"""
Django settings for mtvmcotizacionv02 project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h_p9%cp&*vv=eg&zjy27(oshuae0pj_rlt&(#6=*9r-s%^^9$9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'direccion',
    'ambiente',
    'cliente',
    'contenedor',
    'mueble',
    'gestiondedocumento',
    'estadoderegistro',
    'complejidadriesgo',
    'mensaje',
    'premisas',
    'promocion',
    'menu',
    'trabajador',
    'vehiculo',
    'base',
    'herramienta',
    'material',
    'servicio',
    'talonario',
    'djangular',
    'widget',
    'cotizador',
    'cotizacionweb'
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

ROOT_URLCONF = 'mtvmcotizacionv02.urls'

TEMPLATES = [
    {
        # BACKEND: Referencia directa al Django's template backend API
        # En el caso de conectar Jinja2 hay que hacer referencia
        # con django.template.backends.jinja2.Jinja2.
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # DIRS: Lista de directorios donde el engine debe encontrar
        # los archivos de Templates
        'DIRS': [
            os.path.join(os.path.dirname(__file__), 'templates').replace('\\', '/'),
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
                'base.forms.BaseFormMd',
                'mtvmcotizacionv02.views.sidebar',
                'menu.views.lista_Menu',
                'widget.views.orden_Widgets',
                'menu.views.lista_Relacion'
            ]
            # 'allowed_include_roots': [
            #
            # ]
        },
    },
]

WSGI_APPLICATION = 'mtvmcotizacionv02.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_mtvmcotizacionv2',
        'USER': 'root',
        'PASSWORD': 'md123',
        'HOST': '',
        'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Configuración de email
EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = 'desarrollomtvm@gmail.com'

EMAIL_HOST_PASSWORD = 'mtvmudarte'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    )
