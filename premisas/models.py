from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Empresa(models.Model):
    """docstring for Empresa"""
    codigo = models.CharField(max_length=10)
    empresa = models.CharField(max_length=250)
    telefonos = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    sitio_web = models.URLField()
    correo = models.EmailField()
    responsable = models.CharField(max_length=250, null=True, blank=True)
    cuit = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(upload_to='static/img/')
    telefono_call_center = models.CharField(max_length=100)

    def __str__(self):
        return self.empresa


class PersonalizacionVisual(models.Model):
    """docstring for PersonalizacionVisual"""
    usuario = models.ForeignKey(User)
    tipo = models.CharField(max_length=250)
    valor = models.CharField(max_length=100)

    def __str__(self):
        return u' %s - %s' % (self.usuario, self.tipo)

    class Meta:
        verbose_name = "Personalización Visual"
        verbose_name_plural = "Personalizaciones Visuales"
        unique_together = (("usuario", "tipo"),)


class VarianteVisual(models.Model):
    """docstring for VarianteVisual"""
    usuario = models.ForeignKey(User)
    nombre = models.CharField(max_length=100, unique=True)
    model = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Variente Visual"
        verbose_name_plural = "Variantes Visuales"


class VarianteVisualDetalle(models.Model):
    """docstring for VarianteVisualDetalle"""
    variante_visual = models.ForeignKey(VarianteVisual)
    campo = models.CharField(max_length=100)
    visibilidad = models.IntegerField()

    def __str__(self):
        return u' %s - %s' % (self.variante_visual, self.campo)

    class Meta:
        verbose_name = "Detalle de la variente visual"
        verbose_name_plural = "Detalle de las variantes visuales"


class DatosPrecargado(models.Model):
    """docstring for DatosPrecargado"""
    nombre_app = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    dato = models.CharField(max_length=100)
    tipo_de_dato = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)

    def __str__(self):
        return u' %s - %s' % (self.nombre_app, self.model, self.dato)

    class Meta:
        verbose_name = "Dato precargado"
        verbose_name_plural = "Datos precargados"


class Moneda(models.Model):
    """docstring for Moneda"""
    moneda = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.moneda

    class Meta:
        verbose_name = "Moneda"
        verbose_name_plural = "Monedas"
