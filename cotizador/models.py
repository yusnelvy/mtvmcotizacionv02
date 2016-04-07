"""
docstring

Documentacion del proyecto

"""
from django.db import models
from trabajador.models import Trabajador


# Create your models here.
class Cotizador(models.Model):
    """docstring for Cotizador"""
    def __init__(self, *args, **kwargs):
        super(Cotizador, self).__init__(*args, **kwargs)

    id_trabajador = models.ForeignKey(Trabajador)

    def __str__(self):
        return str(self.id_trabajador)

    class Meta:
        verbose_name = "Cotizador"
        verbose_name_plural = "Cotizadores"
        ordering = ['id_trabajador']
