from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Almacen(models.Model):
    """docstring for Almacen"""
    def __init__(self, *args, **kwargs):
        super(Almacen, self).__init__(*args, **kwargs)

    almacen = models.CharField(max_length=100, unique=True)
    ventas = models.BooleanField(default=False)
    compras = models.BooleanField(default=False)
    consumo = models.BooleanField(default=False)
    produccion = models.BooleanField(default=False)
    descripcion = models.TextField()

    def __str__(self):
        return self.almacen

    class Meta:
        verbose_name = "Almacen"
        verbose_name_plural = "Almacenes"
        ordering = ["almacen"]


class TipoDeMovimiento(models.Model):
    """docstring for TipoDeMovimiento"""
    def __init__(self, *args, **kwargs):
        super(TipoDeMovimiento, self).__init__(*args, **kwargs)

    tipo_de_movimiento = models.CharField(max_length=100, unique=True)
    sentido = models.BooleanField(default=False)
    descripcion = models.TextField()

    def __str__(self):
        return self.tipo_de_movimiento

    class Meta:
        verbose_name = "Tipo de movimiento"
        verbose_name_plural = "Tipos de movimientos"
        ordering = ["tipo_de_movimiento"]


class Unidad(models.Model):
    """docstring for Unidad"""
    unidad = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.unidad

    class Meta:
        verbose_name = "Unidad"
        verbose_name_plural = "Unidades"
