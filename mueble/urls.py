"""
Docstring pendiente para este documento
"""


from django.conf.urls import patterns, url
from mueble.views import TipoDeMuebleListView, TipoDeMuebleView, \
    TipoDeMuebleUpdate, TipoDeMuebleDelete, MuebleListView, \
    MuebleView, MuebleUpdate, MuebleDelete, EspecificacionDeMuebleListView, \
    EspecificacionDeMuebleView, EspecificacionDeMuebleUpdate, \
    EspecificacionDeMuebleDelete, MueblePorAmbienteListView, \
    MueblePorAmbienteView, MueblePorAmbienteUpdate, MueblePorAmbienteDelete


urlpatterns = patterns('',
                       url(r'^$',
                           MuebleListView.as_view(),
                           name='list_mueble'),
                       url(r'^nuevo',
                           MuebleView.as_view(),
                           name='add_mueble'),
                       url(r'^editar/(?P<pk>\d+)/$',
                           MuebleUpdate.as_view(),
                           name='edit_mueble'),
                       url(r'^eliminar/(?P<pk>\d+)/$',
                           MuebleDelete.as_view(),
                           name='eliminar_mueble'),
                       url(r'^tipo_de_mueble/$',
                           TipoDeMuebleListView.as_view(),
                           name='list_tipodemueble'),
                       url(r'^tipo_de_mueble/nuevo',
                           TipoDeMuebleView.as_view(),
                           name='add_tipodemueble'),
                       url(r'^tipo_de_mueble/editar/(?P<pk>\d+)/$',
                           TipoDeMuebleUpdate.as_view(),
                           name='edit_tipodemueble'),
                       url(r'^tipo_de_mueble/eliminar/(?P<pk>\d+)/$',
                           TipoDeMuebleDelete.as_view(),
                           name='eliminar_tipodemueble'),
                       url(r'^especificacion_de_mueble/$',
                           EspecificacionDeMuebleListView.as_view(),
                           name='list_especificaciondemueble'),
                       url(r'^especificacion_de_mueble/nuevo',
                           EspecificacionDeMuebleView.as_view(),
                           name='add_especificaciondemueble'),
                       url(r'^especificacion_de_mueble/editar/(?P<pk>\d+)/$',
                           EspecificacionDeMuebleUpdate.as_view(),
                           name='edit_especificaciondemueble'),
                       url(r'^especificacion_de_mueble/eliminar/(?P<pk>\d+)/$',
                           EspecificacionDeMuebleDelete.as_view(),
                           name='eliminar_especificaciondemueble'),
                       url(r'^mueble_por_ambiente/$',
                           MueblePorAmbienteListView.as_view(),
                           name='list_muebleporambiente'),
                       url(r'^mueble_por_ambiente/nuevo',
                           MueblePorAmbienteView.as_view(),
                           name='add_muebleporambiente'),
                       url(r'^mueble_por_ambiente/editar/(?P<pk>\d+)/$',
                           MueblePorAmbienteUpdate.as_view(),
                           name='edit_muebleporambiente'),
                       url(r'^mueble_por_ambiente/eliminar/(?P<pk>\d+)/$',
                           MueblePorAmbienteDelete.as_view(),
                           name='eliminar_muebleporambiente'),
                       )
