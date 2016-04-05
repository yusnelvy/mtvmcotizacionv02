from django.contrib import admin
from servicio.models import Servicio, ComplejidadServicio, PrecioDeServicio, \
    HerramientasPorServicio

# Register your models here.
admin.site.register(Servicio)
admin.site.register(ComplejidadServicio)
admin.site.register(PrecioDeServicio)
admin.site.register(HerramientasPorServicio)
