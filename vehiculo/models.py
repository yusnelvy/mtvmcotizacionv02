from django.db import models
from django.contrib.auth.models import User
from estadoderegistro.models import EstadoDeRegistro
from trabajador.models import Trabajador


# Create your models here.
class Vehiculo(models.Model):
    """docstring for Vehiculo"""
    def __init__(self, *args, **kwargs):
        super(Vehiculo, self).__init__(*args, **kwargs)

    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    transmision = models.CharField(max_length=100)
    motor = models.CharField(max_length=100)
    volumen_total_carga = models.DecimalField(max_digits=7, decimal_places=2)
    peso_total_carga = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return u' %s - %s' % (self.marca, self.modelo)

    class Meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"


class DetalleDeVehiculo(models.Model):
    """docstring for DetalleDeVehiculo"""
    def __init__(self, *args, **kwargs):
        super(DetalleDeVehiculo, self).__init__(*args, **kwargs)

    vehiculo = models.ForeignKey(Vehiculo)
    numero_de_camion = models.IntegerField()
    ancho = models.DecimalField(max_digits=7, decimal_places=2)
    largo = models.DecimalField(max_digits=7, decimal_places=2)
    alto = models.DecimalField(max_digits=7, decimal_places=2)
    ancho_aux = models.DecimalField(max_digits=7, decimal_places=2, blank=True)
    largo_aux = models.DecimalField(max_digits=7, decimal_places=2, blank=True)
    alto_aux = models.DecimalField(max_digits=7, decimal_places=2, blank=True)
    tara_vehiculo = models.DecimalField(max_digits=7, decimal_places=7)
    observacion = models.TextField(blank=True)

    def __str__(self):
        return u' %s - %s' % (self.vehiculo, self.numero_de_camion)

    def _get_volumenmaximo(self):
        return round((self.ancho*self.alto*self.largo)/1000000, 3)
    volumen_maximo = property(_get_volumenmaximo)

    def _get_volumenmaximoaux(self):
        return round((self.ancho_aux*self.alto_aux*self.largo_aux)/1000000, 3)
    volumen_maximo_aux = property(_get_volumenmaximoaux)

    def _get_superficiecaja(self):
        return round((self.ancho*self.largo)/1000000, 2)
    superficie_caja = property(_get_superficiecaja)

    def _get_superficiecajaaux(self):
        return round((self.ancho_aux*self.largo_aux)/1000000, 2)
    superficie_caja_aux = property(_get_superficiecajaaux)

    class Meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"


class EstadoDeVehiculo(models.Model):
    """docstring for EstadoDeVehiculo"""
    def __init__(self, *args, **kwargs):
        super(EstadoDeVehiculo, self).__init__(*args, **kwargs)

    detalle_especifico = models.ForeignKey(DetalleDeVehiculo)
    estado_de_registro = models.ForeignKey(EstadoDeRegistro)
    fecha = models.DateField(auto_now_add=True, blank=True)
    usuario = models.ForeignKey(User)
    observacion = models.TextField(blank=True)
    predefinido = models.BooleanField(default=None)

    def __str__(self):
        return u' %s - %s' % (self.detalle_especifico, self.estado_de_registro)

    class Meta:
        verbose_name = "Estado de registro de vehículo"
        verbose_name_plural = "Estados de registro de vehículo"
        ordering = ["detalle_especifico", "estado_de_registro"]


class ChoferAsignado(models.Model):
    """docstring for ChoferAsignado"""
    def __init__(self, *args, **kwargs):
        super(ChoferAsignado, self).__init__(*args, **kwargs)

    detalle_de_vehiculo = models.ForeignKey(DetalleDeVehiculo)
    trabajador = models.ForeignKey(Trabajador)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField()

    def __str__(self):
        return u' %s - %s' % (self.detalle_de_vehiculo, self.trabajador)

    class Meta:
        verbose_name = "Chofer asignado"
        verbose_name_plural = "Choferes asignadoa"
        ordering = ["detalle_de_vehiculo", "trabajador"]
