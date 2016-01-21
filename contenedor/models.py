from django.db import models


# Create your models here.
class Contenedor(models.Model):
    """docstring for Contenedor"""
    def __init__(self, *args, **kwargs):
        super(Contenedor, self).__init__(*args, **kwargs)

    contenedor = models.CharField(max_length=100)
    descripcion = models.TextField()
    capacidad_de_volumen = models.DecimalField(max_digits=7, decimal_places=3)
    capacidad_de_peso = models.DecimalField(max_digits=7, decimal_places=3)
    ancho = models.IntegerField()
    largo = models.IntegerField()
    alto = models.IntegerField()
    volumen_en_camion = models.IntegerField()

    def __str__(self):
        return self.contenedor

    class Meta:
        verbose_name = "Contenedor"
        verbose_name_plural = "Contenedores"
        ordering = ['contenedor']
