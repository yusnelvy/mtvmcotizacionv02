"""
Docstring pendiente para este documento
"""


from django.conf.urls import patterns, url
from herramienta.views import HerramientaListView, HerramientaView, \
    HerramientaUpdate, HerramientaDelete, DotacionBasicaDeCamionListView, \
    DotacionBasicaDeCamionView, DotacionBasicaDeCamionUpdate, \
    DotacionBasicaDeCamionDelete


urlpatterns = patterns('',
                       url(r'^$',
                           HerramientaListView.as_view(),
                           name='list_herramienta'),
                       url(r'^nuevo/',
                           HerramientaView.as_view(),
                           name='add_herramienta'),
                       url(r'^editar/(?P<pk>\d+)/$',
                           HerramientaUpdate.as_view(),
                           name='edit_herramienta'),
                       url(r'^eliminar/(?P<pk>\d+)/$',
                           HerramientaDelete.as_view(),
                           name='eliminar_herramienta'),
                       url(r'^dotacion_basica_de_camion/$',
                           DotacionBasicaDeCamionListView.as_view(),
                           name='list_dotacionbasicadecamion'),
                       url(r'^dotacion_basica_de_camion/nuevo/',
                           DotacionBasicaDeCamionView.as_view(),
                           name='add_dotacionbasicadecamion'),
                       url(r'^dotacion_basica_de_camion/editar/(?P<pk>\d+)/$',
                           DotacionBasicaDeCamionUpdate.as_view(),
                           name='edit_dotacionbasicadecamion'),
                       url(r'^dotacion_basica_de_camion/eliminar/(?P<pk>\d+)/$',
                           DotacionBasicaDeCamionDelete.as_view(),
                           name='eliminar_dotacionbasicadecamion'),
                       )
