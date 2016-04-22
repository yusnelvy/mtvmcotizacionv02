from django.contrib import admin
from contenedor.models import Contenedor, ContenedorTipicoPorMueble, \
    TipoDeContenido


# Register your models here.
admin.site.register(Contenedor)
admin.site.register(ContenedorTipicoPorMueble)
admin.site.register(TipoDeContenido)
