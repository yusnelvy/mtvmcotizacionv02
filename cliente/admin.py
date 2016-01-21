from django.contrib import admin
from cliente.models import Sexo, EstadoCivil, TipoDeCliente, \
    TipoDeContacto, TipoDeInformacionDeContacto


# Register your models here.
admin.site.register(Sexo)
admin.site.register(EstadoCivil)
admin.site.register(TipoDeCliente)
admin.site.register(TipoDeContacto)
admin.site.register(TipoDeInformacionDeContacto)
