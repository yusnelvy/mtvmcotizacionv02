"""
Docstring pendiente para este documento
"""


from django.conf.urls import patterns, url
from complejidadriesgo.views import ComplejidadRiesgoListView,  \
    ComplejidadRiesgoView, ComplejidadRiesgoUpdate, \
    ComplejidadRiesgoDelete, NivelComplejidadRiesgoListView, \
    NivelComplejidadRiesgoView, NivelComplejidadRiesgoUpdate,\
    NivelComplejidadRiesgoDelete


urlpatterns = patterns('',
                       url(r'^$',
                           ComplejidadRiesgoListView.as_view(),
                           name='list_complejidadriesgo'),
                       url(r'^nuevo',
                           ComplejidadRiesgoView.as_view(),
                           name='add_complejidadriesgo'),
                       url(r'^editar/(?P<pk>\d+)/$',
                           ComplejidadRiesgoUpdate.as_view(),
                           name='edit_complejidadriesgo'),
                       url(r'^eliminar/(?P<pk>\d+)/$',
                           ComplejidadRiesgoDelete.as_view(),
                           name='eliminar_complejidadriesgo'),
                       url(r'^nivel/$',
                           NivelComplejidadRiesgoListView.as_view(),
                           name='list_nivelcomplejidadriesgo'),
                       url(r'^nivel/nuevo',
                           NivelComplejidadRiesgoView.as_view(),
                           name='add_nivelcomplejidadriesgo'),
                       url(r'^nivel/editar/(?P<pk>\d+)/$',
                           NivelComplejidadRiesgoUpdate.as_view(),
                           name='edit_nivelcomplejidadriesgo'),
                       url(r'^nivel/eliminar/(?P<pk>\d+)/$',
                           NivelComplejidadRiesgoDelete.as_view(),
                           name='eliminar_nivelcomplejidadriesgo'),
                       )
