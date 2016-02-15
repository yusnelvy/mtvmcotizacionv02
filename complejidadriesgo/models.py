from django.db import models


# Create your models here.
class ComplejidadRiesgo(models.Model):
    """docstring for ComplejidadRiesgo"""
    def __init__(self, *args, **kwargs):
        super(ComplejidadRiesgo, self).__init__(*args, **kwargs)

    situacion = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    factor_complejidad = models.IntegerField()
    factor_riesgo = models.IntegerField()

    def __str__(self):
        return self.situacion

    class Meta:
        verbose_name = "Complejidad y riesgo"
        verbose_name_plural = "Complejidades y riesgos"
        ordering = ["situacion"]


class NivelComplejidadRiesgo(models.Model):
    """docstring for NivelComplejidadRiesgo"""
    def __init__(self, *args, **kwargs):
        super(NivelComplejidadRiesgo, self).__init__(*args, **kwargs)

    nivel_complejidad_riesgo = models.CharField(max_length=25, unique=True)
    factor_inicial = models.IntegerField()
    factor_final = models.IntegerField()
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nivel_complejidad_riesgo

    class Meta:
        verbose_name = "Nivel de complejidad y riesgo"
        verbose_name_plural = "niveles de complejidades y riesgos"
        ordering = ["nivel_complejidad_riesgo"]
