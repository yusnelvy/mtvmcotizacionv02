from django.contrib import admin
from cotizacionweb.models import TipoDireccion, \
    ConceptoDeCotizacion, FechaDeCotizacion

# Register your models here.
admin.site.register(TipoDireccion)
admin.site.register(ConceptoDeCotizacion)
admin.site.register(FechaDeCotizacion)
