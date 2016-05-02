from django.contrib import admin
from mueble.models import TipoDeMueble, Mueble, EspecificacionDeMueble,\
    MueblePorAmbiente

# Register your models here.
admin.site.register(TipoDeMueble)
admin.site.register(Mueble)
admin.site.register(EspecificacionDeMueble)
admin.site.register(MueblePorAmbiente)
