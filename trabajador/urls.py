"""
Docstring pendiente para este documento
"""


from django.conf.urls import patterns, url
from trabajador.views import TrabajadorListView, TrabajadorView, \
    TrabajadorUpdate, TrabajadorDelete, CargoTrabajadorListView, \
    CargoTrabajadorView, CargoTrabajadorUpdate, CargoTrabajadorDelete


urlpatterns = patterns('',
                       url(r'^$',
                           TrabajadorListView.as_view(),
                           name='list_trabajador'),
                       url(r'^nuevo/',
                           TrabajadorView.as_view(),
                           name='add_trabajador'),
                       url(r'^editar/(?P<pk>\d+)/$',
                           TrabajadorUpdate.as_view(),
                           name='edit_trabajador'),
                       url(r'^eliminar/(?P<pk>\d+)/$',
                           TrabajadorDelete.as_view(),
                           name='eliminar_trabajador'),
                       url(r'^cargo_trabajador/$',
                           CargoTrabajadorListView.as_view(),
                           name='list_cargotrabajador'),
                       url(r'^cargo_trabajador/nuevo/',
                           CargoTrabajadorView.as_view(),
                           name='add_cargotrabajador'),
                       url(r'^cargo_trabajador/editar/(?P<pk>\d+)/$',
                           CargoTrabajadorUpdate.as_view(),
                           name='edit_cargotrabajador'),
                       url(r'^cargo_trabajador/eliminar/(?P<pk>\d+)/$',
                           CargoTrabajadorDelete.as_view(),
                           name='eliminar_cargotrabajador'),
                       )
