"""
Docstring pendiente para este documento
"""


from django.conf.urls import patterns, url
from gestiondedocumento.views import TipoDeDocumentoListView, TipoDeDocumentoView, \
    TipoDeDocumentoUpdate, TipoDeDocumentoDelete, EstadoDeDocumentoListView, \
    EstadoDeDocumentoView, EstadoDeDocumentoUpdate, EstadoDeDocumentoDelete


urlpatterns = patterns('',
                       url(r'^tipo_de_documento/$',
                           TipoDeDocumentoListView.as_view(),
                           name='list_tipodedocumento'),
                       url(r'^tipo_de_documento/nuevo',
                           TipoDeDocumentoView.as_view(),
                           name='add_tipodedocumento'),
                       url(r'^tipo_de_documento/editar/(?P<pk>\d+)/$',
                           TipoDeDocumentoUpdate.as_view(),
                           name='edit_tipodedocumento'),
                       url(r'^tipo_de_documento/eliminar/(?P<pk>\d+)/$',
                           TipoDeDocumentoDelete.as_view(),
                           name='eliminar_tipodedocumento'),
                       url(r'^estado_de_documento/$',
                           EstadoDeDocumentoListView.as_view(),
                           name='list_estadodedocumento'),
                       url(r'^estado_de_documento/nuevo',
                           EstadoDeDocumentoView.as_view(),
                           name='add_estadodedocumento'),
                       url(r'^estado_de_documento/editar/(?P<pk>\d+)/$',
                           EstadoDeDocumentoUpdate.as_view(),
                           name='edit_estadodedocumento'),
                       url(r'^estado_de_documento/eliminar/(?P<pk>\d+)/$',
                           EstadoDeDocumentoDelete.as_view(),
                           name='eliminar_estadodedocumento'),
                       )
