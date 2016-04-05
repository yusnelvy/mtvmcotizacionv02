from django.contrib import admin
from talonario.models import TipoDeDocumentoImpreso, Talonario, DocumentoDelTalonario, \
    TalonarioEstado, DocumentoDelTalonarioEstado, TrazabilidadTalonario

# Register your models here.
admin.site.register(TipoDeDocumentoImpreso)
admin.site.register(Talonario)
admin.site.register(DocumentoDelTalonario)
admin.site.register(TalonarioEstado)
admin.site.register(DocumentoDelTalonarioEstado)
admin.site.register(TrazabilidadTalonario)
