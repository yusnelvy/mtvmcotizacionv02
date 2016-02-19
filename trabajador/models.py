from django.db import models
from estadoderegistro.models import EstadoDeRegistro
from django.contrib.auth.models import User


# Create your models here.
class CargoTrabajador(models.Model):
    """docstring for CargoTrabajador"""
    def __init__(self, *args, **kwargs):
        super(CargoTrabajador, self).__init__(*args, **kwargs)

    cargo_trabajador = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    cargo_padre = models.ForeignKey("self", null=True, blank=True, related_name='cargochild_set')

    def __str__(self):
        return self.cargo_trabajador

    class Meta:
        verbose_name = "Cargo de trabajador"
        verbose_name_plural = "Cargos de trabajadores"
        ordering = ['cargo_trabajador']


class Trabajador(models.Model):
    """docstring for Trabajador"""
    def __init__(self, *args, **kwargs):
        super(Trabajador, self).__init__(*args, **kwargs)

    dni = models.CharField(max_length=15, blank=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    volumen_en_camion = models.IntegerField()
    cargo_trabajador = models.ForeignKey(CargoTrabajador)

    def __str__(self):
        return u' %s - %s' % (self.nombre, self.apellido)

    class Meta:
        verbose_name = "Trabajador"
        verbose_name_plural = "Trabajadores"
        ordering = ['nombre', 'apellido']


class TrabajadorEstadoDeRegistro(models.Model):
    """docstring for TrabajadorEstadoDeRegistro"""
    def __init__(self, *args, **kwargs):
        super(TrabajadorEstadoDeRegistro, self).__init__(*args, **kwargs)

    trabajador = models.ForeignKey(Trabajador)
    estado_de_registro = models.ForeignKey(EstadoDeRegistro)
    fecha = models.DateField(auto_now_add=True, blank=True)
    usuario = models.ForeignKey(User)
    observacion = models.TextField(blank=True)
    predefinido = models.BooleanField(default=None)

    def __str__(self):
        return u' %s - %s' % (self.trabajador, self.estado_de_registro)

    class Meta:
        verbose_name = "Estado de registro de trabajador"
        verbose_name_plural = "Estados de registro de trabajador"
        ordering = ["trabajador", "estado_de_registro"]
