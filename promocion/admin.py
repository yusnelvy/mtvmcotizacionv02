from django.contrib import admin
from promocion.models import Medio, MedioEspecifico, TipoDeReferido, \
    Alianza, AlianzaEstado, Institucion, PersonaAliado, FuenteDePromocion

# Register your models here.
admin.site.register(Medio)
admin.site.register(MedioEspecifico)
admin.site.register(TipoDeReferido)
admin.site.register(Alianza)
admin.site.register(AlianzaEstado)
admin.site.register(Institucion)
admin.site.register(PersonaAliado)
admin.site.register(FuenteDePromocion)
