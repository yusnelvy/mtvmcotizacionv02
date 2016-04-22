"""
Docstring pendiente para este documento
"""


from django.conf.urls import patterns, url
from contenedor.views import ContenedorListView, ContenedorView, \
    ContenedorUpdate, ContenedorDelete, ContenedorTipicoPorMuebleListView, \
    ContenedorTipicoPorMuebleView, ContenedorTipicoPorMuebleUpdate, \
    ContenedorTipicoPorMuebleDelete, TipoDeContenidoListView, \
    TipoDeContenidoView, TipoDeContenidoUpdate, TipoDeContenidoDelete


urlpatterns = patterns('',
                       url(r'^$',
                           ContenedorListView.as_view(),
                           name='list_contenedor'),
                       url(r'^nuevo',
                           ContenedorView.as_view(),
                           name='add_contenedor'),
                       url(r'^editar/(?P<pk>\d+)/$',
                           ContenedorUpdate.as_view(),
                           name='edit_contenedor'),
                       url(r'^eliminar/(?P<pk>\d+)/$',
                           ContenedorDelete.as_view(),
                           name='eliminar_contenedor'),
                       url(r'^contenedor_tipico_por_mueble/$',
                           ContenedorTipicoPorMuebleListView.as_view(),
                           name='list_contenedortipico'),
                       url(r'^contenedor_tipico_por_mueble/nuevo',
                           ContenedorTipicoPorMuebleView.as_view(),
                           name='add_contenedortipico'),
                       url(r'^contenedor_tipico_por_mueble/editar/(?P<pk>\d+)/$',
                           ContenedorTipicoPorMuebleUpdate.as_view(),
                           name='edit_contenedortipico'),
                       url(r'^contenedor_tipico_por_mueble/eliminar/(?P<pk>\d+)/$',
                           ContenedorTipicoPorMuebleDelete.as_view(),
                           name='eliminar_contenedortipico'),
                       url(r'^tipo_de_contenido/$',
                           TipoDeContenidoListView.as_view(),
                           name='list_tipodecontenido'),
                       url(r'^tipo_de_contenido/nuevo',
                           TipoDeContenidoView.as_view(),
                           name='add_tipodecontenido'),
                       url(r'^tipo_de_contenido/editar/(?P<pk>\d+)/$',
                           TipoDeContenidoUpdate.as_view(),
                           name='edit_tipodecontenido'),
                       url(r'^tipo_de_contenido/eliminar/(?P<pk>\d+)/$',
                           TipoDeContenidoDelete.as_view(),
                           name='eliminar_tipodecontenido'),
                       )
