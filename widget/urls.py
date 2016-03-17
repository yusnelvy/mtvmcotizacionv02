"""
Docstring pendiente para este documento
"""
from django.conf.urls import patterns, url
from widget.views import WidgetListView, WidgetView, \
    WidgetUpdate, WidgetDelete

urlpatterns = patterns('',
                       url(r'^$',
                           WidgetListView.as_view(),
                           name='list_widget'),
                       url(r'^nuevo',
                           WidgetView.as_view(),
                           name='add_widget'),
                       url(r'^editar/(?P<pk>\d+)/$',
                           WidgetUpdate.as_view(),
                           name='edit_widget'),
                       url(r'^eliminar/(?P<pk>\d+)/$',
                           WidgetDelete.as_view(),
                           name='eliminar_widget'),
                       )
