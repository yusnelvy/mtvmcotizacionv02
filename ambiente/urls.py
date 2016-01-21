"""
Docstring pendiente para este documento
"""


from django.conf.urls import patterns, url
from ambiente.views import AmbienteListView, AmbienteView, \
    AmbienteUpdate, AmbienteDelete


urlpatterns = patterns('',
                       url(r'^$',
                           AmbienteListView.as_view(),
                           name='list_ambiente'),
                       url(r'^nuevo',
                           AmbienteView.as_view(),
                           name='add_ambiente'),
                       url(r'^editar/(?P<pk>\d+)/$',
                           AmbienteUpdate.as_view(),
                           name='edit_ambiente'),
                       url(r'^eliminar/(?P<pk>\d+)/$',
                           AmbienteDelete.as_view(),
                           name='eliminar_ambiente'),
                       )
