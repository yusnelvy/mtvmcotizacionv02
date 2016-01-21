"""
Docstring pendiente para este documento
"""


from django.conf.urls import patterns, url
from mueble.views import TipoDeMuebleListView, TipoDeMuebleView, \
    TipoDeMuebleUpdate, TipoDeMuebleDelete


urlpatterns = patterns('',
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
                       )
