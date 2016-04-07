from django.contrib import admin
from cliente.models import Sexo, EstadoCivil, TipoDeCliente, \
    TipoDeRelacion, TipoDeInformacionDeContacto, Cliente, Contacto, \
    InformacionDeContacto, ClienteDireccion, ClienteEstadoDeRegistro


# Register your models here.
admin.site.register(Sexo)
admin.site.register(EstadoCivil)
admin.site.register(TipoDeCliente)
admin.site.register(TipoDeRelacion)
admin.site.register(TipoDeInformacionDeContacto)
admin.site.register(Cliente)
admin.site.register(Contacto)
admin.site.register(InformacionDeContacto)
admin.site.register(ClienteDireccion)
admin.site.register(ClienteEstadoDeRegistro)
