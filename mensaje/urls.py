"""
Docstring pendiente para este documento
"""


from django.conf.urls import patterns, url
from mensaje.views import MensajeListView, MensajeView, \
    MensajeUpdate, MensajeDelete, TipoDeMensajeListView, \
    TipoDeMensajeView, TipoDeMensajeUpdate, \
    TipoDeMensajeDelete


urlpatterns = patterns('',
                       url(r'^$',
                           MensajeListView.as_view(),
                           name='list_mensaje'),
                       url(r'^nuevo',
                           MensajeView.as_view(),
                           name='add_mensaje'),
                       url(r'^editar/(?P<pk>\d+)/$',
                           MensajeUpdate.as_view(),
                           name='edit_mensaje'),
                       url(r'^eliminar/(?P<pk>\d+)/$',
                           MensajeDelete.as_view(),
                           name='eliminar_mensaje'),
                       url(r'^tipo_de_mensaje/$',
                           TipoDeMensajeListView.as_view(),
                           name='list_tipodemensaje'),
                       url(r'^tipo_de_mensaje/nuevo',
                           TipoDeMensajeView.as_view(),
                           name='add_tipodemensaje'),
                       url(r'^tipo_de_mensaje/editar/(?P<pk>\d+)/$',
                           TipoDeMensajeUpdate.as_view(),
                           name='edit_tipodemensaje'),
                       url(r'^tipo_de_mensaje/eliminar/(?P<pk>\d+)/$',
                           TipoDeMensajeDelete.as_view(),
                           name='eliminar_tipodemensaje'),
                       )
