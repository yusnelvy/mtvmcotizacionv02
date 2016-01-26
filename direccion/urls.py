from django.conf.urls import patterns, url
from direccion.views import PaisListView, ProvinciaListView, \
    CiudadListView, BarrioListView, DireccionListView, PaisView, \
    PaisUpdate, PaisDelete, ProvinciaView, ProvinciaUpdate, \
    ProvinciaDelete, CuidadView, CiudadUpdate, CiudadDelete, \
    BarrioView, BarrioUpdate, BarrioDelete, TipoDeEdificacionListView, \
    TipoDeEdificacionView, TipoDeEdificacionUpdate, TipoDeEdificacionDelete, \
    TipoDeAscensorListView, TipoDeAscensorView, TipoDeAscensorUpdate, \
    TipoDeAscensorDelete, TipoDeInmuebleListView, TipoDeInmuebleView, \
    TipoDeInmuebleUpdate, TipoDeInmuebleDelete, EspecificacionDeInmuebleListView, \
    EspecificacionDeInmuebleView, EspecificacionDeInmuebleUpdate, \
    EspecificacionDeInmuebleDelete



urlpatterns = patterns('',
                       url(r'^pais/$',
                           PaisListView.as_view(),
                           name='list_pais'),
                       url(r'^pais/nuevo',
                           PaisView.as_view(),
                           name='add_pais'),
                       url(r'^pais/editar/(?P<pk>\d+)/$',
                           PaisUpdate.as_view(),
                           name='edit_pais'),
                       url(r'^pais/eliminar/(?P<pk>\d+)/$',
                           PaisDelete.as_view(),
                           name='eliminar_pais'),
                       url(r'^provincia/$',
                           ProvinciaListView.as_view(),
                           name='list_provincia'),
                       url(r'^provincia/nuevo',
                           ProvinciaView.as_view(),
                           name='add_provincia'),
                       url(r'^provincia/editar/(?P<pk>\d+)/$',
                           ProvinciaUpdate.as_view(),
                           name='edit_provincia'),
                       url(r'^provincia/eliminar/(?P<pk>\d+)/$',
                           ProvinciaDelete.as_view(),
                           name='eliminar_provincia'),
                       url(r'^ciudad/$',
                           CiudadListView.as_view(),
                           name='list_ciudad'),
                       url(r'^ciudad/nuevo',
                           CuidadView.as_view(),
                           name='add_ciudad'),
                       url(r'^ciudad/editar/(?P<pk>\d+)/$',
                           CiudadUpdate.as_view(),
                           name='edit_ciudad'),
                       url(r'^ciudad/eliminar/(?P<pk>\d+)/$',
                           CiudadDelete.as_view(),
                           name='eliminar_ciudad'),
                       url(r'^barrio/$',
                           BarrioListView.as_view(),
                           name='list_barrio'),
                       url(r'^barrio/nuevo',
                           BarrioView.as_view(),
                           name='add_barrio'),
                       url(r'^barrio/editar/(?P<pk>\d+)/$',
                           BarrioUpdate.as_view(),
                           name='edit_barrio'),
                       url(r'^barrio/eliminar/(?P<pk>\d+)/$',
                           BarrioDelete.as_view(),
                           name='eliminar_barrio'),
                       url(r'^direccion/$',
                           DireccionListView.as_view(),
                           name='DireccionListView'),
                       url(r'^tipo_de_edificacion/$',
                           TipoDeEdificacionListView.as_view(),
                           name='list_tipo_de_edificacion'),
                       url(r'^tipo_de_edificacion/nuevo',
                           TipoDeEdificacionView.as_view(),
                           name='add_tipo_de_edificacion'),
                       url(r'^tipo_de_edificacion/editar/(?P<pk>\d+)/$',
                           TipoDeEdificacionUpdate.as_view(),
                           name='edit_tipo_de_edificacion'),
                       url(r'^tipo_de_edificacion/eliminar/(?P<pk>\d+)/$',
                           TipoDeEdificacionDelete.as_view(),
                           name='eliminar_tipo_de_edificacion'),
                       url(r'^tipo_de_ascensor/$',
                           TipoDeAscensorListView.as_view(),
                           name='list_tipo_de_ascensor'),
                       url(r'^tipo_de_ascensor/nuevo',
                           TipoDeAscensorView.as_view(),
                           name='add_tipo_de_ascensor'),
                       url(r'^tipo_de_ascensor/editar/(?P<pk>\d+)/$',
                           TipoDeAscensorUpdate.as_view(),
                           name='edit_tipo_de_ascensor'),
                       url(r'^tipo_de_ascensor/eliminar/(?P<pk>\d+)/$',
                           TipoDeAscensorDelete.as_view(),
                           name='eliminar_tipo_de_ascensor'),
                       url(r'^tipo_de_inmueble/$',
                           TipoDeInmuebleListView.as_view(),
                           name='list_tipo_de_inmueble'),
                       url(r'^tipo_de_inmueble/nuevo',
                           TipoDeInmuebleView.as_view(),
                           name='add_tipo_de_inmueble'),
                       url(r'^tipo_de_inmueble/editar/(?P<pk>\d+)/$',
                           TipoDeInmuebleUpdate.as_view(),
                           name='edit_tipo_de_inmueble'),
                       url(r'^tipo_de_inmueble/eliminar/(?P<pk>\d+)/$',
                           TipoDeInmuebleDelete.as_view(),
                           name='eliminar_tipo_de_inmueble'),
                       url(r'^especificacion_de_inmueble/$',
                           EspecificacionDeInmuebleListView.as_view(),
                           name='list_especificaciondeinmueble'),
                       url(r'^especificacion_de_inmueble/nuevo',
                           EspecificacionDeInmuebleView.as_view(),
                           name='add_especificaciondeinmueble'),
                       url(r'^especificacion_de_inmueble/editar/(?P<pk>\d+)/$',
                           EspecificacionDeInmuebleUpdate.as_view(),
                           name='edit_especificaciondeinmueble'),
                       url(r'^especificacion_de_inmueble/eliminar/(?P<pk>\d+)/$',
                           EspecificacionDeInmuebleDelete.as_view(),
                           name='eliminar_especificaciondeinmueble'),
                       )
