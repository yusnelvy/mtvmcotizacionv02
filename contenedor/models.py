from django.db import models
from mueble.models import EspecificacionDeMueble


# Create your models here.
class Contenedor(models.Model):
    """docstring for Contenedor"""
    def __init__(self, *args, **kwargs):
        super(Contenedor, self).__init__(*args, **kwargs)

    contenedor = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    capacidad_de_volumen = models.DecimalField(max_digits=7, decimal_places=2)
    capacidad_de_peso = models.DecimalField(max_digits=7, decimal_places=2)
    ancho = models.IntegerField()
    largo = models.IntegerField()
    alto = models.IntegerField()
    volumen_en_camion = models.IntegerField()

    def __str__(self):
        return self.contenedor

    def _get_volumendecontenedor(self):
        return round((self.ancho*self.alto*self.largo)/1000000, 3)
    volumen_de_contenedor = property(_get_volumendecontenedor)

    class Meta:
        verbose_name = "Contenedor"
        verbose_name_plural = "Contenedores"
        ordering = ['contenedor']


class ContenedorTipicoPorMueble(models.Model):
    """docstring for ContenedorTipicoPorMueble"""
    def __init__(self, *args, **kwargs):
        super(ContenedorTipicoPorMueble, self).__init__(*args, **kwargs)

    contenedor = models.ForeignKey(Contenedor, on_delete=models.PROTECT)
    especificacion_de_mueble = models.ForeignKey(EspecificacionDeMueble, on_delete=models.PROTECT)
    cantidad = models.IntegerField()

    def __str__(self):
        return u' %s - %s' % (self.contenedor, self.especificacion_de_mueble)

    class Meta:
        verbose_name = "Contenedor tipico por mueble"
        verbose_name_plural = "Contenedores tipicos por Muebles"
        ordering = ['contenedor']
