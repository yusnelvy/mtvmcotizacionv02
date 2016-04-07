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
    TipoDeInformacionDeContactoDelete, ClienteView, ClienteListView, \
    ClienteDetail, ClienteUpdate, ContactoCreateView, ContactoUpdate, \
    ClienteDireccionView, ClienteInmuebleView, EdificacionCreateView,\
    InmuebleUpdate, ClienteDireccionUpdate, EdificacionUpdate, \
    ClienteDelete, ContactoDelete, ClienteDireccionDelete
from cliente import views


urlpatterns = patterns('',
                       url(r'^$',
                           ClienteListView.as_view(),
                           name='list_cliente'),
                       url(r'^nuevo',
                           ClienteView.as_view(),
                           name='add_cliente'),
                       url(r'^editar/(?P<pk>\d+)/$',
                           ClienteUpdate.as_view(),
                           name='edit_cliente'),
                       url(r'^cliente_ficha/(?P<pk>\d+)/$',
                           ClienteDetail.as_view(),
                           name='ficha_cliente'),
                       url(r'^eliminar/(?P<pk>\d+)/$',
                           ClienteDelete.as_view(),
                           name='eliminar_cliente'),
                       url(r'^contacto/nuevo',
                           ContactoCreateView.as_view(),
                           name='add_contacto'),
                       url(r'^contacto/editar/(?P<pk>\d+)/$',
                           ContactoUpdate.as_view(),
                           name='edit_contacto'),
                       url(r'^contacto/eliminar/(?P<pk>\d+)/$',
                           ContactoDelete.as_view(),
                           name='eliminar_contacto'),
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
                       url(r'^direccion/nuevo',
                           ClienteDireccionView.as_view(),
                           name='add_direccion'),
                       url(r'^direccion/editar/(?P<pk>\d+)/$',
                           ClienteDireccionUpdate.as_view(),
                           name='edit_direccion'),
                       url(r'^direccion/eliminar/(?P<pk>\d+)/$',
                           ClienteDireccionDelete.as_view(),
                           name='eliminar_direccion'),
                       url(r'^inmueble/nuevo',
                           ClienteInmuebleView.as_view(),
                           name='add_inmueble'),
                       url(r'^inmueble/editar/(?P<pk>\d+)/$',
                           InmuebleUpdate.as_view(),
                           name='edit_inmueble'),
                       url(r'^edificacion/nuevo',
                           EdificacionCreateView.as_view(),
                           name='add_edificacion'),
                       url(r'^edificacion/editar/(?P<pk>\d+)/$',
                           EdificacionUpdate.as_view(),
                           name='edit_edificacion'),
                       url(r'^inmueble/exchange/(?P<id_especificacion>\d+)/$',
                           views.exchange_especificaciondeinmueble,
                           name='exchange_especificaciondeinmueble'),
                       url(r'^ascensor/delete/(?P<pk>\d+)/$',
                           views.delete_ascensor,
                           name='delete_ascensor'),
                       url(r'^horariodisponible/delete/(?P<pk>\d+)/$',
                           views.delete_horariodisponible,
                           name='delete_horariodisponible'),
                       url(r'^informaciondecontacto/delete/(?P<pk>\d+)/$',
                           views.delete_informaciondecontacto,
                           name='delete_informaciondecontacto'),
                       )
