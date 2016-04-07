from django.contrib import admin
from direccion.models import Pais, Provincia, Ciudad, \
    Barrio, Direccion, TipoDeEdificacion, Edificacion, \
    TipoDeAscensor, Ascensor, TipoDeInmueble, \
    EspecificacionDeInmueble, Inmueble, Calle

# Register your models here.
admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Ciudad)
admin.site.register(Barrio)
admin.site.register(Direccion)
admin.site.register(TipoDeEdificacion)
admin.site.register(Edificacion)
admin.site.register(TipoDeAscensor)
admin.site.register(Ascensor)
admin.site.register(TipoDeInmueble)
admin.site.register(EspecificacionDeInmueble)
admin.site.register(Inmueble)
admin.site.register(Calle)
