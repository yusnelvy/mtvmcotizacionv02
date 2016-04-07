from django.contrib import admin
from trabajador.models import CargoTrabajador, Trabajador, \
    TrabajadorEstadoDeRegistro

# Register your models here.
admin.site.register(CargoTrabajador)
admin.site.register(Trabajador)
admin.site.register(TrabajadorEstadoDeRegistro)
