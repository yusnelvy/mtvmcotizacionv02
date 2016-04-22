"""
Docstring pendiente para este documento
"""


from django.conf.urls import patterns, url
from cotizador.views import CotizadorListView, CotizadorView, \
    CotizadorUpdate, CotizadorDelete

urlpatterns = patterns('',
                       url(r'^$',
                           CotizadorListView.as_view(),
                           name='list_cotizador'),
                       url(r'^nuevo',
                           CotizadorView.as_view(),
                           name='add_cotizador'),
                       url(r'^editar/(?P<pk>\d+)/$',
                           CotizadorUpdate.as_view(),
                           name='edit_cotizador'),
                       url(r'^eliminar/(?P<pk>\d+)/$',
                           CotizadorDelete.as_view(),
                           name='eliminar_cotizador'),
                       )
