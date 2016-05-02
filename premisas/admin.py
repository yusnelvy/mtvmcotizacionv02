from django.contrib import admin
from premisas.models import Empresa, PersonalizacionVisual, \
    VarianteVisual, VarianteVisualDetalle, DatosPrecargado, \
    Moneda


# Register your models here.
admin.site.register(Empresa)
admin.site.register(PersonalizacionVisual)
admin.site.register(VarianteVisual)
admin.site.register(VarianteVisualDetalle)
admin.site.register(DatosPrecargado)
admin.site.register(Moneda)
