"""
Docstring pendiente para este documento
"""


from django.conf.urls import patterns, url
from ambiente.views import AmbienteListView, AmbienteView, \
    AmbienteUpdate, AmbienteDelete, AmbientePorTipoDeInmuebleListView, \
    AmbientePorTipoDeInmuebleView, AmbientePorTipoDeInmuebleUpdate,\
    AmbientePorTipoDeInmuebleDelete


urlpatterns = patterns('',
                       url(r'^$',
                           AmbienteListView.as_view(),
                           name='list_ambiente'),
                       url(r'^nuevo',
                           AmbienteView.as_view(),
                           name='add_ambiente'),
                       url(r'^editar/(?P<pk>\d+)/$',
                           AmbienteUpdate.as_view(),
                           name='edit_ambiente'),
                       url(r'^eliminar/(?P<pk>\d+)/$',
                           AmbienteDelete.as_view(),
                           name='eliminar_ambiente'),
                       url(r'^ambiente_por_tipo_de_inmueble/$',
                           AmbientePorTipoDeInmuebleListView.as_view(),
                           name='list_ambienteportipoinmueble'),
                       url(r'^ambiente_por_tipo_de_inmueble/nuevo',
                           AmbientePorTipoDeInmuebleView.as_view(),
                           name='add_ambienteportipoinmueble'),
                       url(r'^ambiente_por_tipo_de_inmueble/editar/(?P<pk>\d+)/$',
                           AmbientePorTipoDeInmuebleUpdate.as_view(),
                           name='edit_ambienteportipoinmueble'),
                       url(r'^ambiente_por_tipo_de_inmueble/eliminar/(?P<pk>\d+)/$',
                           AmbientePorTipoDeInmuebleDelete.as_view(),
                           name='eliminar_ambienteportipoinmueble'),
                       )
