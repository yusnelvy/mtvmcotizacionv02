"""
Docstring pendiente para este documento
"""


from django.conf.urls import patterns, url
from almacen.views import UnidadListView, UnidadView, \
    UnidadUpdate, UnidadDelete

urlpatterns = patterns('',
                       url(r'^unidad/$',
                           UnidadListView.as_view(),
                           name='list_unidad'),
                       url(r'^unidad/nuevo',
                           UnidadView.as_view(),
                           name='add_unidad'),
                       url(r'^unidad/editar/(?P<pk>\d+)/$',
                           UnidadUpdate.as_view(),
                           name='edit_unidad'),
                       url(r'^unidad/eliminar/(?P<pk>\d+)/$',
                           UnidadDelete.as_view(),
                           name='eliminar_unidad'),
                       )
