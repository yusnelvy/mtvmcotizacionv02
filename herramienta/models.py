from django.db import models
from premisas.models import Unidad
from vehiculo.models import DetalleDeVehiculo


# Create your models here.
class Herramienta(models.Model):
    """docstring for Herramienta"""
    def __init__(self, *args, **kwargs):
        super(Herramienta, self).__init__(*args, **kwargs)

    herramienta = models.CharField(max_length=100, unique=True)
    unidad = models.ForeignKey(Unidad)
    descripcion = models.TextField()
    volumen_en_camion = models.IntegerField()
    peso_kg = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.herramienta

    class Meta:
        verbose_name = "Herramienta"
        verbose_name_plural = "Herramientas"


class DotacionBasicaDeCamion(models.Model):
    """docstring for DotacionBasicaDeCamion"""
    def __init__(self, *args, **kwargs):
        super(DotacionBasicaDeCamion, self).__init__(*args, **kwargs)

    detalle_de_vehiculo = models.ForeignKey(DetalleDeVehiculo)
    herramienta = models.ForeignKey(Herramienta)
    cantidad = models.IntegerField()

    def __str__(self):
        return u' %s - %s' % (self.detalle_de_vehiculo, self.herramienta)

    class Meta:
        verbose_name = "Dotación básica de camión"
        verbose_name_plural = "Dotaciones básicas de camiones"
