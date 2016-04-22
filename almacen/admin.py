from django.contrib import admin
from almacen.models import Almacen, TipoDeMovimiento, Unidad

# Register your models here.
admin.site.register(Almacen)
admin.site.register(TipoDeMovimiento)
admin.site.register(Unidad)
