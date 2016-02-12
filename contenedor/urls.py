"""
Docstring pendiente para este documento
"""


from django.conf.urls import patterns, url
from contenedor.views import ContenedorListView, ContenedorView, \
    ContenedorUpdate, ContenedorDelete, ContenedorTipicoPorMuebleListView, \
    ContenedorTipicoPorMuebleView, ContenedorTipicoPorMuebleUpdate, \
    ContenedorTipicoPorMuebleDelete


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
                       )
