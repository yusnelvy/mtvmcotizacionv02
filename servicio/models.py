from django.db import models
from almacen.models import Unidad
from django.contrib.auth.models import User
from herramienta.models import Herramienta
from mueble.models import EspecificacionDeMueble


# Create your models here.
class Servicio(models.Model):
    """docstring for Servicio"""
    servicio = models.CharField(max_length=100)
    unidad_de_venta = models.ForeignKey(Unidad, related_name='unidad_de_venta')
    unidad_de_consumo = models.ForeignKey(Unidad, related_name='unidad_de_consumo')
    descripcion = models.TextField()

    def __str__(self):
        return self.servicio

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ["servicio"]


class ComplejidadServicio(models.Model):
    """docstring for ComplejidadServicio"""
    descripcion = models.CharField(max_length=100)
    servicio = models.ForeignKey(Servicio)
    porcentaje = models.DecimalField(max_digits=7, decimal_places=2)
    predefinido = models.BooleanField(default=None)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Complejidad del servicio"
        verbose_name_plural = "Complejidades del servicio"
        ordering = ["descripcion"]


class PrecioDeServicio(models.Model):
    """docstring for PrecioDeServicio"""
    servicio = models.ForeignKey(Servicio)
    precio_base = models.DecimalField(max_digits=9, decimal_places=2)
    precio_marginal = models.DecimalField(max_digits=9, decimal_places=2)
    cantidad_de_gracia = models.DecimalField(max_digits=9, decimal_places=2)
    intervalo_1 = models.DecimalField(max_digits=9, decimal_places=2)
    porcentaje_1 = models.DecimalField(max_digits=9, decimal_places=2)
    intervalo_2 = models.DecimalField(max_digits=9, decimal_places=2)
    porcentaje_2 = models.DecimalField(max_digits=9, decimal_places=2)
    intervalo_3 = models.DecimalField(max_digits=9, decimal_places=2)
    porcentaje_3 = models.DecimalField(max_digits=9, decimal_places=2)
    redondeo = models.DecimalField(max_digits=9, decimal_places=2)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField()
    infinito = models.BooleanField(default=None)
    user_preparador = models.ForeignKey(User, related_name='user_preparador')
    fecha_preparacion = models.DateField(auto_now_add=True)
    user_aprobador = models.ForeignKey(User, null=True, blank=True, related_name='user_aprobador')
    fecha_aprobacion = models.DateField(blank=True)
    aprobado = models.BooleanField()

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = "Precio del servicio"
        verbose_name_plural = "Precios del servicio"


class HerramientasPorServicio(models.Model):
    """docstring for HerramientasPorServicio"""
    servicio = models.ForeignKey(Servicio)
    herramienta = models.ForeignKey(Herramienta)
    cantidad = models.DecimalField(max_digits=9, decimal_places=2)
    calculo = models.CharField(max_length=200)

    def __str__(self):
        return u' %s - %s' % (self.servicio, self.herramienta)

    class Meta:
        verbose_name = "Herramienta por servicio"
        verbose_name_plural = "Herramientas por servicio"
        ordering = ["servicio", "herramienta"]


class ServicioTipicoPorMueble(models.Model):
    """docstring for ContenedorTipicoPorMueble"""
    def __init__(self, *args, **kwargs):
        super(ServicioTipicoPorMueble, self).__init__(*args, **kwargs)

    servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT)
    especificacion_de_mueble = models.ForeignKey(EspecificacionDeMueble, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    predefinido = models.BooleanField(default=None)

    def __str__(self):
        return u' %s - %s' % (self.servicio, self.especificacion_de_mueble)

    class Meta:
        verbose_name = "Servicio tipico por mueble"
        verbose_name_plural = "Servicios tipicos por Muebles"
        ordering = ['servicio']
