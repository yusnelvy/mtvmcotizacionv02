"""
docstring

Documentacion del proyecto

"""
from django.db import models


# Create your models here.
class TipoDeMueble(models.Model):
    """docstring for TipoDeMueble"""
    def __init__(self, *args, **kwargs):
        super(TipoDeMueble, self).__init__(*args, **kwargs)
    tipo_de_mueble = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.tipo_de_mueble

    class Meta:
        verbose_name = "Tipo de mueble"
        verbose_name_plural = "Tipos de mueble"
        ordering = ['tipo_de_mueble']
