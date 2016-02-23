from django.db import models
from premisas.models import Unidad
from django.contrib.auth.models import User
from servicio.models import Servicio


# Create your models here.
class TipoDeMaterial(models.Model):
    """docstring for TipoDeMaterial"""
    def __init__(self, *args, **kwargs):
        super(TipoDeMaterial, self).__init__(*args, **kwargs)

    tipo_de_material = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.tipo_de_material

    class Meta:
        verbose_name = "Tipo de material "
        verbose_name_plural = "Tipos de materiales"
        ordering = ["tipo_de_material"]


class Material(models.Model):
    """docstring for Material"""
    def __init__(self, *args, **kwargs):
        super(Material, self).__init__(*args, **kwargs)

    material = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo_de_material = models.ForeignKey(TipoDeMaterial)
    unidad_de_consumo = models.ForeignKey(Unidad, related_name='und_consumo')
    unidad_de_venta = models.ForeignKey(Unidad, related_name='und_venta')
    relacion_consumo_venta = models.DecimalField(max_digits=9, decimal_places=2)
    ancho = models.DecimalField(max_digits=7, decimal_places=2)
    largo = models.DecimalField(max_digits=7, decimal_places=2)
    alto = models.DecimalField(max_digits=7, decimal_places=2)
    peso_unidad_consumo_kg = models.DecimalField(max_digits=9, decimal_places=3)
    cotizable = models.BooleanField(default=None)

    def __str__(self):
        return self.tipo_de_material

    class Meta:
        verbose_name = "Material "
        verbose_name_plural = "Materiales"
        ordering = ["material"]


class PrecioDeMaterial(models.Model):
    """docstring for PrecioDeMaterial"""
    def __init__(self, *args, **kwargs):
        super(PrecioDeMaterial, self).__init__(*args, **kwargs)

    material = models.ForeignKey(Material)
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField()
    infinito = models.BooleanField(default=None)
    user_preparador = models.ForeignKey(User, related_name='user_preparador_material')
    fecha_preparacion = models.DateField(auto_now_add=True)
    user_aprobador = models.ForeignKey(User, null=True, blank=True, related_name='user_aprobador_material')
    fecha_aprobacion = models.DateField(blank=True)
    aprobado = models.BooleanField(default=None)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = "Precio del material"
        verbose_name_plural = "Precios del material"


class MaterialesPorServicio(models.Model):
    """docstring for MaterialesPorServicio"""
    def __init__(self, *args, **kwargs):
        super(MaterialesPorServicio, self).__init__(*args, **kwargs)

    servicio = models.ForeignKey(Servicio)
    material = models.ForeignKey(Material)
    cantidad = models.DecimalField(max_digits=9, decimal_places=2)
    calculo = models.CharField(max_length=200)

    def __str__(self):
        return u' %s - %s' % (self.servicio, self.material)

    class Meta:
        verbose_name = "Material por servicio"
        verbose_name_plural = "Materiales por servicio"
        ordering = ["servicio", "material"]
