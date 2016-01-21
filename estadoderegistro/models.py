"""
docstring

Documentacion del proyecto

"""
from django.db import models


# Create your models here.
class Estado(models.Model):
    """docstring for Estado"""
    def __init__(self, *args, **kwargs):
        super(Estado, self).__init__(*args, **kwargs)
    estado = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.estado

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        ordering = ['estado']


class TipoDeRegistro(models.Model):
    """docstring for TipoDeRegistro"""
    def __init__(self, *args, **kwargs):
        super(TipoDeRegistro, self).__init__(*args, **kwargs)
    tipo_de_registro = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.tipo_de_registro

    class Meta:
        verbose_name = "Tipo de Registro"
        verbose_name_plural = "Tipos de registro"
        ordering = ['tipo_de_registro']


class EstadoDeRegistro(models.Model):
    """docstring"""
    estado = models.ForeignKey(Estado)
    tipo_de_registro = models.ForeignKey(TipoDeRegistro)
    orden = models.IntegerField()
    descripcion = models.TextField()
    observacion = models.TextField(blank=True)

    def __str__(self):
        return u' %s - %s' % (self.tipo_de_registro, self.estado)

    class Meta:
        verbose_name = "Estado de registro"
        verbose_name_plural = "Estados de registros"
        ordering = ['tipo_de_registro', 'estado']
