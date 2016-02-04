from django.contrib import admin
from premisas.models import Empresa, PersonalizacionVisual, \
    VarianteVisual

# Register your models here.
admin.site.register(Empresa)
admin.site.register(PersonalizacionVisual)
admin.site.register(VarianteVisual)
