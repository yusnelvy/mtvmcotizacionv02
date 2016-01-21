"""
Docstring pendiente para este documento
"""


from django.conf.urls import patterns, url
from contenedor.views import ContenedorListView, ContenedorView, \
    ContenedorUpdate, ContenedorDelete


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
                       )
