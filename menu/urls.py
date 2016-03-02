"""
Docstring pendiente para este documento
"""


from django.conf.urls import patterns, url
from menu.views import MenuListView, MenuView, \
    MenuUpdate, MenuDelete, MenuFavoritoListView, \
    MenuFavoritoView, MenuFavoritoUpdate, \
    MenuFavoritoDelete, RelacionListView, \
    RelacionView, RelacionUpdate, RelacionDelete

from menu import views




urlpatterns = patterns('',
                       url(r'^$',
                           MenuListView.as_view(),
                           name='list_menu'),
                       url(r'^nuevo',
                           MenuView.as_view(),
                           name='add_menu'),
                       url(r'^editar/(?P<pk>\d+)/$',
                           MenuUpdate.as_view(),
                           name='edit_menu'),
                       url(r'^eliminar/(?P<pk>\d+)/$',
                           MenuDelete.as_view(),
                           name='eliminar_menu'),
                       url(r'^menu_favorito/$',
                           MenuFavoritoListView.as_view(),
                           name='list_menufavorito'),
                       url(r'^menu_favorito/nuevo',
                           MenuFavoritoView.as_view(),
                           name='add_menufavorito'),
                       url(r'^menu_favorito/editar/(?P<pk>\d+)/$',
                           MenuFavoritoUpdate.as_view(),
                           name='edit_menufavorito'),
                       url(r'^menu_favorito/eliminar/(?P<pk>\d+)/$',
                           MenuFavoritoDelete.as_view(),
                           name='eliminar_menufavorito'),
                       url(r'^relacion/$',
                           RelacionListView.as_view(),
                           name='list_relacion'),
                       url(r'^relacion/nuevo',
                           RelacionView.as_view(),
                           name='add_relacion'),
                       url(r'^relacion/editar/(?P<pk>\d+)/$',
                           RelacionUpdate.as_view(),
                           name='edit_relacion'),
                       url(r'^relacion/eliminar/(?P<pk>\d+)/$',
                           RelacionDelete.as_view(),
                           name='eliminar_relacion'),
                       url(r'^menu_ver/$',
                           views.lista_Menu,
                           name='menu_ver'),
                       url(r'^relacion_ver/$',
                           views.lista_Relacion,
                           name='relacion_ver'),
                       url(r'^transaccion',
                           views.lista_Transaccion,
                           name='transaccion'),
                      )
