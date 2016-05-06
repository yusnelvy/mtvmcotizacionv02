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

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from api.views import ClienteViewSet, PaisViewSet, \
    ProvinciaViewSet, TipoDeClienteViewSet, \
    CiudadViewSet, BarrioViewSet, CalleViewSet, \
    DireccionViewSet


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'api/v1/tipodecliente', TipoDeClienteViewSet)
router.register(r'api/v1/cliente', ClienteViewSet)
router.register(r'api/v1/pais', PaisViewSet)
router.register(r'api/v1/provincia', ProvinciaViewSet)
router.register(r'api/v1/ciudad', CiudadViewSet)
router.register(r'api/v1/barrio', BarrioViewSet)
router.register(r'api/v1/calle', CalleViewSet)
router.register(r'api/v1/direccion', DireccionViewSet)

urlpatterns = [
    url(r'^$', views.pantalla_inicial,
        name='pantalla_inicial'),
    url(r'^guia_de_estilo/',
        views.guia_de_estilo,
        name='guia_de_estilos'),
    url(r'^admin/',
        include(admin.site.urls)),
    url(r'^direccion/',
        include('direccion.urls',
                namespace="udirecciones")),
    url(r'^ambiente/',
        include('ambiente.urls',
                namespace="uambientes")),
    url(r'^cliente/',
        include('cliente.urls',
                namespace="uclientes")),
    url(r'^contenedor/',
        include('contenedor.urls',
                namespace="ucontenedores")),
    url(r'^mueble/',
        include('mueble.urls',
                namespace="umuebles")),
    url(r'^gestiondedocumento/',
        include('gestiondedocumento.urls',
                namespace="ugestiondedocumentos")),
    url(r'^estadoderegistro/',
        include('estadoderegistro.urls',
                namespace="uestadoderegistros")),
    url(r'^complejidadriesgo/',
        include('complejidadriesgo.urls',
                namespace="ucomplejidadriesgos")),
    url(r'^mensaje/',
        include('mensaje.urls',
                namespace="umensajes")),
    url(r'^premisas/',
        include('premisas.urls',
                namespace="upremisas")),
    url(r'^promocion/',
        include('promocion.urls',
                namespace="upromociones")),
    url(r'^menu/',
        include('menu.urls',
                namespace="umenus")),
    url(r'^herramienta/',
        include('herramienta.urls',
                namespace="uherramientas")),
    url(r'^material/',
        include('material.urls',
                namespace="umateriales")),
    url(r'^servicio/',
        include('servicio.urls',
                namespace="uservicios")),
    url(r'^talonario/',
        include('talonario.urls',
                namespace="utalonarios")),
    url(r'^trabajador/',
        include('trabajador.urls',
                namespace="utrabajadores")),
    url(r'^vehiculo/',
        include('vehiculo.urls',
                namespace="uvehiculos")),
    url(r'^widget/',
        include('widget.urls',
                namespace="uwidgets")),
    url(r'^cotizacionweb/',
        include('cotizacionweb.urls',
                namespace="ucotizacionesweb")),
    url(r'^almacen/',
        include('almacen.urls',
                namespace="ualmacenes")),
    url(r'^cotizador/',
        include('cotizador.urls',
                namespace="ucotizadores")),
    url(r'^usuario/',
        include('usuario.urls',
                namespace="uusuarios")),
    url(r'^notificacion/',
        include('notificacion.urls',
                namespace="unotificaciones")),
    url(r'^api/',
        include('api.urls',
                namespace="uapis")),
    url(r'^chaining/',
        include('smart_selects.urls')),
    url(r'^sidebarUpdate/$',
        'mtvmcotizacionv02.views.sidebarUpdate',
        name='sidebarUpdate'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls',
                namespace='rest_framework'))
]

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^static/(?P<path>.*)$',
                                'django.views.static.serve',
                                {'document_root': settings.STATICFILES_DIRS}),)
