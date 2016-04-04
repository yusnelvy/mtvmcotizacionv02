"""
Docstring pendiente para este documento
"""


from django.conf.urls import patterns, url
from cotizacionweb.views import CotizacionDetail

urlpatterns = patterns('',
                       url(r'^cotizacion_ficha/(?P<pk>\d+)/$',
                           CotizacionDetail.as_view(),
                           name='ficha_cotizacion'),
                       )
