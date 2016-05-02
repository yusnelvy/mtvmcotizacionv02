"""
Docstring pendiente para este documento
"""


from django.conf.urls import patterns, url
from cotizacionweb.views import CotizacionDetail, \
    TipoDireccionListView, TipoDireccionView, \
    TipoDireccionUpdate, TipoDireccionDelete, \
    ConceptoDeCotizacionListView, ConceptoDeCotizacionView, \
    ConceptoDeCotizacionUpdate, ConceptoDeCotizacionDelete, \
    FechaDeCotizacionListView, FechaDeCotizacionView, \
    FechaDeCotizacionUpdate, FechaDeCotizacionDelete, \
    CotizacionBitacoraView, CotizacionListView, \
    CotizacionAmbienteView, CotizacionAmbienteDetail, \
    CotizacionMuebleView, CotizacionMuebleUpdate, \
    CotizacionMuebleDelete, CotizacionAmbienteDelete, \
    ContenedorMuebleDelete, ServicioMuebleDelete, \
    ContenedorMuebleView, ServicioMuebleView, \
    CotizacionDireccionDelete
from cotizacionweb import views

urlpatterns = patterns('',
                       url(r'^$',
                           CotizacionListView.as_view(),
                           name='list_cotizacion'),
                       url(r'^cotizacion_ficha/(?P<pk>\d+)/$',
                           CotizacionDetail.as_view(),
                           name='ficha_cotizacion'),
                       url(r'^cotizacion_direccion/eliminar/(?P<pk>\d+)/$',
                           CotizacionDireccionDelete.as_view(),
                           name='eliminar_cotizaciondireccion'),
                       url(r'^cotizacionambiente_ficha/(?P<pk>\d+)/$',
                           CotizacionAmbienteDetail.as_view(),
                           name='ficha_cotizacionambiente'),
                       url(r'^cotizacion_ambiente/nuevo',
                           CotizacionAmbienteView.as_view(),
                           name='add_cotizacionambiente'),
                       url(r'^cotizacion_ambiente/eliminar/(?P<pk>\d+)/$',
                           CotizacionAmbienteDelete.as_view(),
                           name='eliminar_cotizacionambiente'),
                       url(r'^cotizacion_mueble/nuevo',
                           CotizacionMuebleView.as_view(),
                           name='add_cotizacionmueble'),
                       url(r'^cotizacion_mueble/editar/(?P<pk>\d+)/$',
                           CotizacionMuebleUpdate.as_view(),
                           name='edit_cotizacionmueble'),
                       url(r'^cotizacion_mueble/eliminar/(?P<pk>\d+)/$',
                           CotizacionMuebleDelete.as_view(),
                           name='eliminar_cotizacionmueble'),
                       url(r'^contenedor_mueble/nuevo',
                           ContenedorMuebleView.as_view(),
                           name='add_contenedormueble'),
                       url(r'^contenedor_mueble/eliminar/(?P<pk>\d+)/$',
                           ContenedorMuebleDelete.as_view(),
                           name='eliminar_contenedormueble'),
                       url(r'^servicio_mueble/nuevo',
                           ServicioMuebleView.as_view(),
                           name='add_serviciomueble'),
                       url(r'^servicio_mueble/eliminar/(?P<pk>\d+)/$',
                           ServicioMuebleDelete.as_view(),
                           name='eliminar_serviciomueble'),
                       url(r'^cambiar_estadodedocumento/(?P<pk>\d+)/',
                           views.CotizacionEstadoDeDocumento,
                           name='cambiar_estadodedocumento'),
                       url(r'^tipo_direccion/$',
                           TipoDireccionListView.as_view(),
                           name='list_tipodireccion'),
                       url(r'^tipo_direccion/nuevo',
                           TipoDireccionView.as_view(),
                           name='add_tipodireccion'),
                       url(r'^tipo_direccion/editar/(?P<pk>\d+)/$',
                           TipoDireccionUpdate.as_view(),
                           name='edit_tipodireccion'),
                       url(r'^tipo_direccion/eliminar/(?P<pk>\d+)/$',
                           TipoDireccionDelete.as_view(),
                           name='eliminar_tipodireccion'),
                       url(r'^concepto_de_cotizacion/$',
                           ConceptoDeCotizacionListView.as_view(),
                           name='list_conceptodecotizacion'),
                       url(r'^concepto_de_cotizacion/nuevo',
                           ConceptoDeCotizacionView.as_view(),
                           name='add_conceptodecotizacion'),
                       url(r'^concepto_de_cotizacion/editar/(?P<pk>\d+)/$',
                           ConceptoDeCotizacionUpdate.as_view(),
                           name='edit_conceptodecotizacion'),
                       url(r'^concepto_de_cotizacion/eliminar/(?P<pk>\d+)/$',
                           ConceptoDeCotizacionDelete.as_view(),
                           name='eliminar_conceptodecotizacion'),
                       url(r'^fecha_de_cotizacion/$',
                           FechaDeCotizacionListView.as_view(),
                           name='list_fechadecotizacion'),
                       url(r'^fecha_de_cotizacion/nuevo',
                           FechaDeCotizacionView.as_view(),
                           name='add_fechadecotizacion'),
                       url(r'^fecha_de_cotizacion/editar/(?P<pk>\d+)/$',
                           FechaDeCotizacionUpdate.as_view(),
                           name='edit_fechadecotizacion'),
                       url(r'^fecha_de_cotizacion/eliminar/(?P<pk>\d+)/$',
                           FechaDeCotizacionDelete.as_view(),
                           name='eliminar_fechadecotizacion'),
                       url(r'^bitacora_de_cotizacion/nuevo',
                           CotizacionBitacoraView.as_view(),
                           name='add_bitacoradecotizacion'),
                       )
