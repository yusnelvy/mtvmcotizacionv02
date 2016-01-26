"""
docstring

Documentacion del proyecto

"""
from django.db import models
from ambiente.models import AmbientePorTipoDeInmueble


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


class Mueble(models.Model):
    """docstring for Mueble"""
    def __init__(self, *args, **kwargs):
        super(Mueble, self).__init__(*args, **kwargs)
    mueble = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    tipo_de_mueble = models.ForeignKey(TipoDeMueble)
    trasladable = models.BooleanField(default=None)

    def __str__(self):
        return self.mueble

    class Meta:
        verbose_name = "Mueble"
        verbose_name_plural = "Muebles"
        ordering = ['mueble']


class EspecificacionDeMueble(models.Model):
    """docstring for EspecificacionDeMueble"""
    def __init__(self, *args, **kwargs):
        super(EspecificacionDeMueble, self).__init__(*args, **kwargs)
    mueble = models.ForeignKey(Mueble)
    especificacion_de_mueble = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    ancho = models.DecimalField(max_digits=7, decimal_places=2)
    largo = models.DecimalField(max_digits=7, decimal_places=2)
    alto = models.DecimalField(max_digits=7, decimal_places=2)
    volumen_en_camion = models.IntegerField()
    predefinido = models.BooleanField(default=None)

    def __str__(self):
        return self.especificacion_de_mueble

    class Meta:
        verbose_name = "Especificación del mueble"
        verbose_name_plural = "Especificaciones del mueble"
        ordering = ['especificacion_de_mueble']


class MueblePorAmbiente(models.Model):
    """docstring for MueblePorAmbiente"""
    def __init__(self, *args, **kwargs):
        super(MueblePorAmbiente, self).__init__(*args, **kwargs)
    especificacion_de_mueble = models.ForeignKey(EspecificacionDeMueble)
    ambiente_por_tipo_de_inmueble = models.ForeignKey(AmbientePorTipoDeInmueble)
    predefinido = models.BooleanField(default=None)

    def __str__(self):
        return u' %s - %s' % (self.especificacion_de_mueble, self.ambiente_por_tipo_de_inmueble)

    class Meta:
        verbose_name = "Mueble por ambiente"
        verbose_name_plural = "Muebles por ambiente "
        ordering = ['especificacion_de_mueble', 'ambiente_por_tipo_de_inmueble']
