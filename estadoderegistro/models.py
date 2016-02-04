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


class EstadoDeRegistro(models.Model):
    """docstring"""
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    model = models.CharField(max_length=100)
    descripcion = models.TextField()
    observacion = models.TextField(blank=True)

    def __str__(self):
        return u' %s - %s' % (self.model, self.estado)

    class Meta:
        verbose_name = "Estado de registro"
        verbose_name_plural = "Estados de registros"
        ordering = ['model', 'estado']
