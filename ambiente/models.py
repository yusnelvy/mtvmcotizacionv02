from django.db import models
#from direccion.models import EspecificacionDeInmueble


# Create your models here.

class Ambiente(models.Model):
    """docstring for Ambiente"""
    def __init__(self, *args, **kwargs):
        super(Ambiente, self).__init__(*args, **kwargs)

    ambiente = models.CharField(max_length=100)
    descripcion = models.TextField()
    conteo_de_ambientes = models.BooleanField(default=False)

    def __str__(self):
        return self.ambiente

    class Meta:
        verbose_name = "Ambiente"
        verbose_name_plural = "Ambientes"
        ordering = ["ambiente"]


# class AmbientesPorTipoDeInmueble(models.Model):
#     """docstring for AmbientesPorTipoDeInmueble"""
#     def __init__(self, *args, **kwargs):
#         super(AmbientesPorTipoDeInmueble, self).__init__(*args, **kwargs)

#     ambiente = models.ForeignKey(Ambiente, on_delete=models.PROTECT)
#     especificacion_de_inmueble = models.ForeignKey(EspecificacionDeInmueble,
#                                                    on_delete=models.PROTECT)
#     predeterminado = models.BooleanField(default=False)

#     def __str__(self):
#         return u' %s - %s' % (self.ambiente, self.especificacion_de_inmueble)

#     class Meta:
#         verbose_name = "Ambiente por tipo inmueble"
#         verbose_name_plural = "Ambientes por tipos de inmueble"
#         ordering = ["especificacion_de_inmueble", "ambiente"]
#         unique_together = (("ambiente", "especificacion_de_inmueble"),)
#         # evaluar si se coloca unique together o no
