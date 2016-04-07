from django.contrib import admin
from gestiondedocumento.models import TipoDeDocumento, EstadoDeDocumento

# Register your models here.
admin.site.register(TipoDeDocumento)
admin.site.register(EstadoDeDocumento)
