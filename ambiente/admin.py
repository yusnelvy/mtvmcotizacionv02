from django.contrib import admin
from ambiente.models import Ambiente, AmbientePorTipoDeInmueble, \
    AmbienteEstadoDeRegistro


# Register your models here.
admin.site.register(Ambiente)
admin.site.register(AmbientePorTipoDeInmueble)
admin.site.register(AmbienteEstadoDeRegistro)
