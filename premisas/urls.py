"""
Docstring pendiente para este documento
"""


from django.conf.urls import patterns, url
from premisas.views import EmpresaListView, EmpresaView, \
    EmpresaUpdate, EmpresaDelete, PersonalizacionVisualListView, \
    PersonalizacionVisualView, PersonalizacionVisualUpdate, \
    PersonalizacionVisualDelete, VarianteVisualListView, \
    VarianteVisualCreateView, VarianteVisualUpdate, \
    VarianteVisualDelete, DatosPrecargadoListView, \
    DatosPrecargadoView


urlpatterns = patterns('',
                       url(r'^empresa/$',
                           EmpresaListView.as_view(),
                           name='list_empresa'),
                       url(r'^empresa/nuevo/',
                           EmpresaView.as_view(),
                           name='add_empresa'),
                       url(r'^empresa/editar/(?P<pk>\d+)/$',
                           EmpresaUpdate.as_view(),
                           name='edit_empresa'),
                       url(r'^empresa/eliminar/(?P<pk>\d+)/$',
                           EmpresaDelete.as_view(),
                           name='eliminar_empresa'),
                       url(r'^personalizacion_visual/$',
                           PersonalizacionVisualListView.as_view(),
                           name='list_personalizacionvisual'),
                       url(r'^personalizacion_visual/nuevo/',
                           PersonalizacionVisualView.as_view(),
                           name='add_personalizacionvisual'),
                       url(r'^personalizacion_visual/editar/(?P<pk>\d+)/$',
                           PersonalizacionVisualUpdate.as_view(),
                           name='edit_personalizacionvisual'),
                       url(r'^personalizacion_visual/eliminar/(?P<pk>\d+)/$',
                           PersonalizacionVisualDelete.as_view(),
                           name='eliminar_personalizacionvisual'),
                       url(r'^variante_visual/$',
                           VarianteVisualListView.as_view(),
                           name='list_variantevisual'),
                       url(r'^variante_visual/nuevo/',
                           VarianteVisualCreateView.as_view(),
                           name='add_variantevisual'),
                       url(r'^variante_visual/editar/(?P<pk>\d+)/$',
                           VarianteVisualUpdate.as_view(),
                           name='edit_variantevisual'),
                       url(r'^variante_visual/eliminar/(?P<pk>\d+)/$',
                           VarianteVisualDelete.as_view(),
                           name='eliminar_variantevisual'),
                       url(r'^datos_precargado/$',
                           DatosPrecargadoListView.as_view(),
                           name='list_datosprecargado'),
                       url(r'^datos_precargado/nuevo/',
                           DatosPrecargadoView.as_view(),
                           name='add_datosprecargado'),
                       )
