"""
docstring

Documentacion del proyecto

"""
from django.db import models


# Create your models here.
class TipoDeDocumento(models.Model):
    """docstring for TipoDeDocumento"""
    def __init__(self, *args, **kwargs):
        super(TipoDeDocumento, self).__init__(*args, **kwargs)
    tipo_de_documento = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.tipo_de_documento

    class Meta:
        verbose_name = "Tipo de documento"
        verbose_name_plural = "Tipos de documento"
        ordering = ['tipo_de_documento']


class EstadoDeDocumento(models.Model):
    """docstring"""
    tipo_de_documento = models.ForeignKey(TipoDeDocumento, on_delete=models.PROTECT)
    estado_de_documento = models.CharField(max_length=100)
    descripcion = models.TextField()
    orden = models.IntegerField()
    observacion = models.TextField(blank=True)

    def __str__(self):
        return u' %s - %s' % (self.tipo_de_documento, self.estado_de_documento)

    class Meta:
        verbose_name = "Estado de documento"
        verbose_name_plural = "Estados de documentos"
        ordering = ['tipo_de_documento', 'estado_de_documento']
