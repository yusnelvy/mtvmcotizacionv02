from django.contrib import admin
from material.models import TipoDeMaterial, Material, PrecioDeMaterial, \
    MaterialesPorServicio

# Register your models here.
admin.site.register(TipoDeMaterial)
admin.site.register(Material)
admin.site.register(PrecioDeMaterial)
admin.site.register(MaterialesPorServicio)
