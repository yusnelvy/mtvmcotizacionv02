"""
Docstring pendiente para este documento
"""


from django.conf.urls import patterns, url
from notificacion.views import NotificacionListView, \
    NotificacionView, NotificacionUpdate, NotificacionDelete

urlpatterns = patterns('',
                       url(r'^$',
                           NotificacionListView.as_view(),
                           name='list_notificacion'),
                       url(r'^nuevo',
                           NotificacionView.as_view(),
                           name='add_notificacion'),
                       url(r'^editar/(?P<pk>\d+)/$',
                           NotificacionUpdate.as_view(),
                           name='edit_notificacion'),
                       url(r'^eliminar/(?P<pk>\d+)/$',
                           NotificacionDelete.as_view(),
                           name='eliminar_notificacion'),
                       )
