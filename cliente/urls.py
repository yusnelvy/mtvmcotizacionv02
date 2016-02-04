"""
Docstring pendiente para este documento
"""


from django.conf.urls import patterns, url
from cliente.views import SexoListView, SexoView, SexoUpdate, \
    SexoDelete, EstadoCivilListView, EstadoCivilView, \
    EstadoCivilUpdate, EstadoCivilDelete, TipoDeClienteListView, \
    TipoDeClienteView, TipoDeClienteUpdate, TipoDeClienteDelete, \
    TipoDeRelacionListView, TipoDeRelacionView, TipoDeRelacionUpdate, \
    TipoDeRelacionDelete, TipoDeInformacionDeContactoListView, \
    TipoDeInformacionDeContactoView, TipoDeInformacionDeContactoUpdate, \
    TipoDeInformacionDeContactoDelete


urlpatterns = patterns('',
                       url(r'^sexo/$',
                           SexoListView.as_view(),
                           name='list_sexo'),
                       url(r'^sexo/nuevo',
                           SexoView.as_view(),
                           name='add_sexo'),
                       url(r'^sexo/editar/(?P<pk>\d+)/$',
                           SexoUpdate.as_view(),
                           name='edit_sexo'),
                       url(r'^sexo/eliminar/(?P<pk>\d+)/$',
                           SexoDelete.as_view(),
                           name='eliminar_sexo'),
                       url(r'^estado_civil/$',
                           EstadoCivilListView.as_view(),
                           name='list_estado_civil'),
                       url(r'^estado_civil/nuevo',
                           EstadoCivilView.as_view(),
                           name='add_estado_civil'),
                       url(r'^estado_civil/editar/(?P<pk>\d+)/$',
                           EstadoCivilUpdate.as_view(),
                           name='edit_estado_civil'),
                       url(r'^estado_civil/eliminar/(?P<pk>\d+)/$',
                           EstadoCivilDelete.as_view(),
                           name='eliminar_estado_civil'),
                       url(r'^tipo_de_cliente/$',
                           TipoDeClienteListView.as_view(),
                           name='list_tipo_de_cliente'),
                       url(r'^tipo_de_cliente/nuevo',
                           TipoDeClienteView.as_view(),
                           name='add_tipo_de_cliente'),
                       url(r'^tipo_de_cliente/editar/(?P<pk>\d+)/$',
                           TipoDeClienteUpdate.as_view(),
                           name='edit_tipo_de_cliente'),
                       url(r'^tipo_de_cliente/eliminar/(?P<pk>\d+)/$',
                           TipoDeClienteDelete.as_view(),
                           name='eliminar_tipo_de_cliente'),
                       url(r'^tipo_de_relacion/$',
                           TipoDeRelacionListView.as_view(),
                           name='list_tipo_de_relacion'),
                       url(r'^tipo_de_relacion/nuevo',
                           TipoDeRelacionView.as_view(),
                           name='add_tipo_de_relacion'),
                       url(r'^tipo_de_relacion/editar/(?P<pk>\d+)/$',
                           TipoDeRelacionUpdate.as_view(),
                           name='edit_tipo_de_relacion'),
                       url(r'^tipo_de_relacion/eliminar/(?P<pk>\d+)/$',
                           TipoDeRelacionDelete.as_view(),
                           name='eliminar_tipo_de_relacion'),
                       url(r'^tipo_de_informacion_de_contacto/$',
                           TipoDeInformacionDeContactoListView.as_view(),
                           name='list_tipo_de_informacion_de_contacto'),
                       url(r'^tipo_de_informacion_de_contacto/nuevo',
                           TipoDeInformacionDeContactoView.as_view(),
                           name='add_tipo_de_informacion_de_contacto'),
                       url(r'^tipo_de_informacion_de_contacto/editar/(?P<pk>\d+)/$',
                           TipoDeInformacionDeContactoUpdate.as_view(),
                           name='edit_tipo_de_informacion_de_contacto'),
                       url(r'^tipo_de_informacion_de_contacto/eliminar/(?P<pk>\d+)/$',
                           TipoDeInformacionDeContactoDelete.as_view(),
                           name='eliminar_tipo_de_informacion_de_contacto'),

                       )
