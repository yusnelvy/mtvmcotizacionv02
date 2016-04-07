from django.contrib import admin
from vehiculo.models import Vehiculo, DetalleDeVehiculo, EstadoDeVehiculo, \
    ChoferAsignado

# Register your models here.
admin.site.register(Vehiculo)
admin.site.register(DetalleDeVehiculo)
admin.site.register(EstadoDeVehiculo)
admin.site.register(ChoferAsignado)
