"""
Docstring pendiente para este documento
"""

from django.conf.urls import patterns, url
from servicio.views import ServicioListView, \
    ServicioView, ServicioUpdate, ServicioDelete, \
    ComplejidadServicioListView, ComplejidadServicioView, \
    ComplejidadServicioUpdate, ComplejidadServicioDelete, \
    PrecioDeServicioListView, PrecioDeServicioView, \
    PrecioDeServicioUpdate, PrecioDeServicioDelete, \
    HerramientasPorServicioListView, HerramientasPorServicioView, \
    HerramientasPorServicioUpdate, HerramientasPorServicioDelete


urlpatterns = patterns('',
                       url(r'^$',
                           ServicioListView.as_view(),
                           name='list_servicio'),
                       url(r'^nuevo/',
                           ServicioView.as_view(),
                           name='add_servicio'),
                       url(r'^editar/(?P<pk>\d+)/$',
                           ServicioUpdate.as_view(),
                           name='edit_servicio'),
                       url(r'^eliminar/(?P<pk>\d+)/$',
                           ServicioDelete.as_view(),
                           name='eliminar_servicio'),
                       url(r'^complejidad_servicio/$',
                           ComplejidadServicioListView.as_view(),
                           name='list_complejidadservicio'),
                       url(r'^complejidad_servicio/nuevo/',
                           ComplejidadServicioView.as_view(),
                           name='add_complejidadservicio'),
                       url(r'^complejidad_servicio/editar/(?P<pk>\d+)/$',
                           ComplejidadServicioUpdate.as_view(),
                           name='edit_complejidadservicio'),
                       url(r'^complejidad_servicio/eliminar/(?P<pk>\d+)/$',
                           ComplejidadServicioDelete.as_view(),
                           name='eliminar_complejidadservicio'),
                       url(r'^precio_de_servicio/$',
                           PrecioDeServicioListView.as_view(),
                           name='list_preciodeservicio'),
                       url(r'^precio_de_servicio/nuevo/',
                           PrecioDeServicioView.as_view(),
                           name='add_preciodeservicio'),
                       url(r'^precio_de_servicio/editar/(?P<pk>\d+)/$',
                           PrecioDeServicioUpdate.as_view(),
                           name='edit_preciodeservicio'),
                       url(r'^precio_de_servicio/eliminar/(?P<pk>\d+)/$',
                           PrecioDeServicioDelete.as_view(),
                           name='eliminar_preciodeservicio'),
                       url(r'^herramientas_por_servicio/$',
                           HerramientasPorServicioListView.as_view(),
                           name='list_herramientaporservicio'),
                       url(r'^herramientas_por_servicio/nuevo/',
                           HerramientasPorServicioView.as_view(),
                           name='add_herramientaporservicio'),
                       url(r'^herramientas_por_servicio/editar/(?P<pk>\d+)/$',
                           HerramientasPorServicioUpdate.as_view(),
                           name='edit_herramientaporservicio'),
                       url(r'^herramientas_por_servicio/eliminar/(?P<pk>\d+)/$',
                           HerramientasPorServicioDelete.as_view(),
                           name='eliminar_herramientaporservicio'),
                       )
