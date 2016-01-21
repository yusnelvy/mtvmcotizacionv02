"""
Docstring pendiente para este documento
"""


from django.conf.urls import patterns, url
from estadoderegistro.views import EstadoListView, EstadoView, \
    EstadoUpdate, EstadoDelete, TipoDeRegistroListView, \
    TipoDeRegistroView, TipoDeRegistroUpdate, TipoDeRegistroDelete, \
    EstadoDeRegistroListView, EstadoDeRegistroView, EstadoDeRegistroUpdate, \
    EstadoDeRegistroDelete


urlpatterns = patterns('',
                       url(r'^estado/$',
                           EstadoListView.as_view(),
                           name='list_estado'),
                       url(r'^estado/nuevo',
                           EstadoView.as_view(),
                           name='add_estado'),
                       url(r'^estado/editar/(?P<pk>\d+)/$',
                           EstadoUpdate.as_view(),
                           name='edit_estado'),
                       url(r'^estado/eliminar/(?P<pk>\d+)/$',
                           EstadoDelete.as_view(),
                           name='eliminar_estado'),
                       url(r'^tipo_de_registro/$',
                           TipoDeRegistroListView.as_view(),
                           name='list_tipoderegistro'),
                       url(r'^tipo_de_registro/nuevo',
                           TipoDeRegistroView.as_view(),
                           name='add_tipoderegistro'),
                       url(r'^tipo_de_registro/editar/(?P<pk>\d+)/$',
                           TipoDeRegistroUpdate.as_view(),
                           name='edit_tipoderegistro'),
                       url(r'^tipo_de_registro/eliminar/(?P<pk>\d+)/$',
                           TipoDeRegistroDelete.as_view(),
                           name='eliminar_tipoderegistro'),
                       url(r'^estado_de_registro/$',
                           EstadoDeRegistroListView.as_view(),
                           name='list_estadoderegistro'),
                       url(r'^estado_de_registro/nuevo',
                           EstadoDeRegistroView.as_view(),
                           name='add_estadoderegistro'),
                       url(r'^estado_de_registro/editar/(?P<pk>\d+)/$',
                           EstadoDeRegistroUpdate.as_view(),
                           name='edit_estadoderegistro'),
                       url(r'^estado_de_registro/eliminar/(?P<pk>\d+)/$',
                           EstadoDeRegistroDelete.as_view(),
                           name='eliminar_estadoderegistro'),
                       )
