from django.db import models
from direccion.models import EspecificacionDeInmueble
from estadoderegistro.models import EstadoDeRegistro
from django.contrib.auth.models import User


# Create your models here.

class Ambiente(models.Model):
    """docstring for Ambiente"""
    def __init__(self, *args, **kwargs):
        super(Ambiente, self).__init__(*args, **kwargs)

    ambiente = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    conteo_de_ambientes = models.BooleanField(default=False)

    def __str__(self):
        return self.ambiente

    class Meta:
        verbose_name = "ambiente"
        verbose_name_plural = "Ambientes"
        ordering = ["ambiente"]


class AmbientePorTipoDeInmueble(models.Model):
    """docstring for AmbientePorTipoDeInmueble"""
    def __init__(self, *args, **kwargs):
        super(AmbientePorTipoDeInmueble, self).__init__(*args, **kwargs)

    ambiente = models.ForeignKey(Ambiente, on_delete=models.PROTECT)
    especificacion_de_inmueble = models.ForeignKey(EspecificacionDeInmueble,
                                                   on_delete=models.PROTECT)
    predeterminado = models.BooleanField(default=False)

    def __str__(self):
        return u' %s - %s' % (self.ambiente, self.especificacion_de_inmueble)

    class Meta:
        verbose_name = "Ambiente por tipo inmueble"
        verbose_name_plural = "Ambientes por tipos de inmueble"
        ordering = ["especificacion_de_inmueble", "ambiente"]


class AmbienteEstadoDeRegistro(models.Model):
    """docstring for AmbienteEstadoDeRegistro"""
    def __init__(self, *args, **kwargs):
        super(AmbienteEstadoDeRegistro, self).__init__(*args, **kwargs)

    ambiente = models.ForeignKey(Ambiente)
    estado_de_registro = models.ForeignKey(EstadoDeRegistro)
    fecha = models.DateField(auto_now_add=True, blank=True)
    usuario = models.ForeignKey(User)
    observacion = models.TextField(blank=True)
    predefinido = models.BooleanField(default=None)

    def __str__(self):
        return u' %s - %s' % (self.ambiente, self.estado_de_registro)

    class Meta:
        verbose_name = "Estado de registro de ambiente"
        verbose_name_plural = "Estados de registro de ambiente"
        ordering = ["ambiente", "estado_de_registro"]
