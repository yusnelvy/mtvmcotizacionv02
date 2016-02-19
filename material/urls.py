"""
Docstring pendiente para este documento
"""


from django.conf.urls import patterns, url
from material.views import TipoDeMaterialListView, TipoDeMaterialView, \
    TipoDeMaterialUpdate, TipoDeMaterialDelete, MaterialListView, \
    MaterialView, MaterialUpdate, MaterialDelete


urlpatterns = patterns('',
                       url(r'^$',
                           MaterialListView.as_view(),
                           name='list_material'),
                       url(r'^nuevo/',
                           MaterialView.as_view(),
                           name='add_material'),
                       url(r'^editar/(?P<pk>\d+)/$',
                           MaterialUpdate.as_view(),
                           name='edit_material'),
                       url(r'^eliminar/(?P<pk>\d+)/$',
                           MaterialDelete.as_view(),
                           name='eliminar_material'),
                       url(r'^tipo_de_material/$',
                           TipoDeMaterialListView.as_view(),
                           name='list_tipodematerial'),
                       url(r'^tipo_de_material/nuevo/',
                           TipoDeMaterialView.as_view(),
                           name='add_tipodematerial'),
                       url(r'^tipo_de_material/editar/(?P<pk>\d+)/$',
                           TipoDeMaterialUpdate.as_view(),
                           name='edit_tipodematerial'),
                       url(r'^tipo_de_material/eliminar/(?P<pk>\d+)/$',
                           TipoDeMaterialDelete.as_view(),
                           name='eliminar_tipodematerial'),
                       )
