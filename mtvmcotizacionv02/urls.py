"""mtvmcotizacionv02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from mtvmcotizacionv02 import views

urlpatterns = [
    url(r'^$', views.pantalla_inicial,
        name='pantalla_inicial'),
    url(r'^guia_de_estilo/', views.guia_de_estilo,
        name='guia_de_estilos'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^direccion/',
        include('direccion.urls', namespace="udirecciones")),
    url(r'^ambiente/',
        include('ambiente.urls', namespace="uambientes")),
    url(r'^cliente/',
        include('cliente.urls', namespace="uclientes")),
    url(r'^contenedor/',
        include('contenedor.urls', namespace="ucontenedores")),
    url(r'^mueble/',
        include('mueble.urls', namespace="umuebles")),
    url(r'^gestiondedocumento/',
        include('gestiondedocumento.urls', namespace="ugestiondedocumentos")),
    url(r'^estadoderegistro/',
        include('estadoderegistro.urls', namespace="uestadoderegistros")),
    url(r'^complejidadriesgo/',
        include('complejidadriesgo.urls', namespace="ucomplejidadriesgos")),
    url(r'^mensaje/',
        include('mensaje.urls', namespace="umensajes")),
    url(r'^premisas/',
        include('premisas.urls', namespace="upremisas")),
    url(r'^promocion/',
        include('promocion.urls', namespace="upromociones")),
    url(r'^menu/',
        include('menu.urls', namespace="umenus")),
    url(r'^chaining/',
        include('smart_selects.urls')),
    url(r'^sidebarUpdate/$', 'mtvmcotizacionv02.views.sidebarUpdate', name='sidebarUpdate')
]

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^static/(?P<path>.*)$',
                                'django.views.static.serve',
                                {'document_root': settings.STATICFILES_DIRS}),)
