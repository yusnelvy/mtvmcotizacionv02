from django.contrib import admin
from cotizacionweb.models import TipoDireccion, \
    ConceptoDeCotizacion, FechaDeCotizacion
from cotizacionweb.models import Cotizacion, CotizacionEstado,\
    CotizacionDireccion, TipoDireccion, CotizacionBitacora, \
    CotizacionAmbiente, CotizacionMueble, FechaDeCotizacion, \
    CotizacionHistoricoFecha


# Register your models here.
admin.site.register(TipoDireccion)
admin.site.register(ConceptoDeCotizacion)
admin.site.register(FechaDeCotizacion)
