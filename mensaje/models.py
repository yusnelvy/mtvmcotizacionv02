from django.db import models


# Create your models here.
class TipoDeMensaje(models.Model):
    """docstring for TipoDeMensaje"""
    def __init__(self, *args, **kwargs):
        super(TipoDeMensaje, self).__init__(*args, **kwargs)

    tipo_de_mensaje = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.tipo_de_mensaje

    class Meta:
        verbose_name = "Tipo de mensaje"
        verbose_name_plural = "Tipos de mensajes"


class Mensaje(models.Model):
    """docstring for Mensaje"""
    def __init__(self, *args, **kwargs):
        super(Mensaje, self).__init__(*args, **kwargs)

    tipo_de_mensaje = models.ForeignKey(TipoDeMensaje, on_delete=models.PROTECT)
    codigo = models.CharField(max_length=15)
    mensaje = models.CharField(max_length=250)
    descripcion = models.TextField()

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"
