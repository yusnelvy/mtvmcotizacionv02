"""
Docstring pendiente para este documento
"""

from django.conf.urls import patterns, url
from talonario.views import TipoDeDocumentoImpresoListView, \
    TipoDeDocumentoImpresoView, TipoDeDocumentoImpresoUpdate, \
    TipoDeDocumentoImpresoDelete, TalonarioListView, TalonarioView, \
    TalonarioUpdate, TalonarioDelete, DocumentoDelTalonarioListView, \
    DocumentoDelTalonarioView, DocumentoDelTalonarioUpdate, \
    DocumentoDelTalonarioDelete, TrazabilidadTalonarioListView


urlpatterns = patterns('',
                       url(r'^$',
                           TalonarioListView.as_view(),
                           name='list_talonario'),
                       url(r'^nuevo/',
                           TalonarioView.as_view(),
                           name='add_talonario'),
                       url(r'^editar/(?P<pk>\d+)/$',
                           TalonarioUpdate.as_view(),
                           name='edit_talonario'),
                       url(r'^eliminar/(?P<pk>\d+)/$',
                           TalonarioDelete.as_view(),
                           name='eliminar_talonario'),
                       url(r'^tipo_de_documento/$',
                           TipoDeDocumentoImpresoListView.as_view(),
                           name='list_tipodedocumento'),
                       url(r'^tipo_de_documento/nuevo/',
                           TipoDeDocumentoImpresoView.as_view(),
                           name='add_tipodedocumento'),
                       url(r'^tipo_de_documento/editar/(?P<pk>\d+)/$',
                           TipoDeDocumentoImpresoUpdate.as_view(),
                           name='edit_tipodedocumento'),
                       url(r'^tipo_de_documento/eliminar/(?P<pk>\d+)/$',
                           TipoDeDocumentoImpresoDelete.as_view(),
                           name='eliminar_tipodedocumento'),
                       url(r'^documento_del_talonario/$',
                           DocumentoDelTalonarioListView.as_view(),
                           name='list_documentodeltalonario'),
                       url(r'^documento_del_talonario/nuevo/',
                           DocumentoDelTalonarioView.as_view(),
                           name='add_documentodeltalonario'),
                       url(r'^documento_del_talonario/editar/(?P<pk>\d+)/$',
                           DocumentoDelTalonarioUpdate.as_view(),
                           name='edit_documentodeltalonario'),
                       url(r'^documento_del_talonario/eliminar/(?P<pk>\d+)/$',
                           DocumentoDelTalonarioDelete.as_view(),
                           name='eliminar_documentodeltalonario'),
                       url(r'^trazabilidad_talonario/$',
                           TrazabilidadTalonarioListView.as_view(),
                           name='list_trazabilidadtalonario'),
                       )
