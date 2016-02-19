"""
Docstring pendiente para este documento
"""


from django.conf.urls import patterns, url
from vehiculo.views import VehiculoListView, VehiculoView, \
    VehiculoUpdate, VehiculoDelete, DetalleDeVehiculoListView, \
    DetalleDeVehiculoView, DetalleDeVehiculoUpdate, \
    DetalleDeVehiculoDelete, ChoferAsignadoListView, \
    ChoferAsignadoView, ChoferAsignadoUpdate, \
    ChoferAsignadoDelete


urlpatterns = patterns('',
                       url(r'^$',
                           VehiculoListView.as_view(),
                           name='list_vehiculo'),
                       url(r'^nuevo/',
                           VehiculoView.as_view(),
                           name='add_vehiculo'),
                       url(r'^editar/(?P<pk>\d+)/$',
                           VehiculoUpdate.as_view(),
                           name='edit_vehiculo'),
                       url(r'^eliminar/(?P<pk>\d+)/$',
                           VehiculoDelete.as_view(),
                           name='eliminar_vehiculo'),
                       url(r'^detalle_de_vehiculo/$',
                           DetalleDeVehiculoListView.as_view(),
                           name='list_detalledevehiculo'),
                       url(r'^detalle_de_vehiculo/nuevo/',
                           DetalleDeVehiculoView.as_view(),
                           name='add_detalledevehiculo'),
                       url(r'^detalle_de_vehiculo/editar/(?P<pk>\d+)/$',
                           DetalleDeVehiculoUpdate.as_view(),
                           name='edit_detalledevehiculo'),
                       url(r'^detalle_de_vehiculo/eliminar/(?P<pk>\d+)/$',
                           DetalleDeVehiculoDelete.as_view(),
                           name='eliminar_detalledevehiculo'),
                       url(r'^chofer_asignado/$',
                           ChoferAsignadoListView.as_view(),
                           name='list_choferasignado'),
                       url(r'^chofer_asignado/nuevo/',
                           ChoferAsignadoView.as_view(),
                           name='add_choferasignado'),
                       url(r'^chofer_asignado/editar/(?P<pk>\d+)/$',
                           ChoferAsignadoUpdate.as_view(),
                           name='edit_choferasignado'),
                       url(r'^chofer_asignado/eliminar/(?P<pk>\d+)/$',
                           ChoferAsignadoDelete.as_view(),
                           name='eliminar_choferasignado'),
                       )
