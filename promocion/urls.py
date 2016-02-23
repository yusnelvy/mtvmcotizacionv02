"""
Docstring pendiente para este documento
"""


from django.conf.urls import patterns, url
from promocion.views import MedioListView, MedioView, \
    MedioUpdate, MedioDelete, MedioEspecificoListView, \
    MedioEspecificoView, MedioEspecificoUpdate, \
    MedioEspecificoDelete, TipoDeReferidoListView, \
    TipoDeReferidoView, TipoDeReferidoUpdate, \
    TipoDeReferidoDelete, AlianzaListView, AlianzaView, \
    AlianzaUpdate, AlianzaDelete, InstitucionListView, \
    InstitucionView, InstitucionUpdate, InstitucionDelete, \
    PersonaAliadoListView, PersonaAliadoView, \
    PersonaAliadoUpdate, PersonaAliadoDelete, \
    FuenteDePromocionListView, FuenteDePromocionView, \
    FuenteDePromocionUpdate, FuenteDePromocionDelete


urlpatterns = patterns('',
                       url(r'^medio/$',
                           MedioListView.as_view(),
                           name='list_medio'),
                       url(r'^medio/nuevo/',
                           MedioView.as_view(),
                           name='add_medio'),
                       url(r'^medio/editar/(?P<pk>\d+)/$',
                           MedioUpdate.as_view(),
                           name='edit_medio'),
                       url(r'^medio/eliminar/(?P<pk>\d+)/$',
                           MedioDelete.as_view(),
                           name='eliminar_medio'),
                       url(r'^medio_especifico/$',
                           MedioEspecificoListView.as_view(),
                           name='list_medioespecifico'),
                       url(r'^medio_especifico/nuevo/',
                           MedioEspecificoView.as_view(),
                           name='add_medioespecifico'),
                       url(r'^medio_especifico/editar/(?P<pk>\d+)/$',
                           MedioEspecificoUpdate.as_view(),
                           name='edit_medioespecifico'),
                       url(r'^medio_especifico/eliminar/(?P<pk>\d+)/$',
                           MedioEspecificoDelete.as_view(),
                           name='eliminar_medioespecifico'),
                       url(r'^tipo_de_referido/$',
                           TipoDeReferidoListView.as_view(),
                           name='list_tipodereferido'),
                       url(r'^tipo_de_referido/nuevo/',
                           TipoDeReferidoView.as_view(),
                           name='add_tipodereferido'),
                       url(r'^tipo_de_referido/editar/(?P<pk>\d+)/$',
                           TipoDeReferidoUpdate.as_view(),
                           name='edit_tipodereferido'),
                       url(r'^tipo_de_referido/eliminar/(?P<pk>\d+)/$',
                           TipoDeReferidoDelete.as_view(),
                           name='eliminar_tipodereferido'),
                       url(r'^alianza/$',
                           AlianzaListView.as_view(),
                           name='list_alianza'),
                       url(r'^alianza/nuevo/',
                           AlianzaView.as_view(),
                           name='add_alianza'),
                       url(r'^alianza/editar/(?P<pk>\d+)/$',
                           AlianzaUpdate.as_view(),
                           name='edit_alianza'),
                       url(r'^alianza/eliminar/(?P<pk>\d+)/$',
                           AlianzaDelete.as_view(),
                           name='eliminar_alianza'),
                       url(r'^institucion/$',
                           InstitucionListView.as_view(),
                           name='list_institucion'),
                       url(r'^institucion/nuevo/',
                           InstitucionView.as_view(),
                           name='add_institucion'),
                       url(r'^institucion/editar/(?P<pk>\d+)/$',
                           InstitucionUpdate.as_view(),
                           name='edit_institucion'),
                       url(r'^institucion/eliminar/(?P<pk>\d+)/$',
                           InstitucionDelete.as_view(),
                           name='eliminar_institucion'),
                       url(r'^persona_aliada/$',
                           PersonaAliadoListView.as_view(),
                           name='list_personaaliado'),
                       url(r'^persona_aliada/nuevo/',
                           PersonaAliadoView.as_view(),
                           name='add_personaaliado'),
                       url(r'^persona_aliada/editar/(?P<pk>\d+)/$',
                           PersonaAliadoUpdate.as_view(),
                           name='edit_personaaliado'),
                       url(r'^persona_aliada/eliminar/(?P<pk>\d+)/$',
                           PersonaAliadoDelete.as_view(),
                           name='eliminar_personaaliado'),
                       url(r'^fuente_de_promocion/$',
                           FuenteDePromocionListView.as_view(),
                           name='list_fuentedepromocion'),
                       url(r'^fuente_de_promocion/nuevo/',
                           FuenteDePromocionView.as_view(),
                           name='add_fuentedepromocion'),
                       url(r'^fuente_de_promocion/editar/(?P<pk>\d+)/$',
                           FuenteDePromocionUpdate.as_view(),
                           name='edit_fuentedepromocion'),
                       url(r'^fuente_de_promocion/eliminar/(?P<pk>\d+)/$',
                           FuenteDePromocionDelete.as_view(),
                           name='eliminar_fuentedepromocion'),
                       )
