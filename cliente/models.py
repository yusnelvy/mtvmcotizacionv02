"""
docstring

Documentacion del proyecto

"""
from django.db import models


# Create your models here.
class Sexo(models.Model):
    """docstring for Sexo"""
    def __init__(self, *args, **kwargs):
        super(Sexo, self).__init__(*args, **kwargs)
    sexo = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.sexo

    class Meta:
        verbose_name = "Sexo"
        verbose_name_plural = "Sexos"
        ordering = ['sexo']


class EstadoCivil(models.Model):
    """docstring for EstadoCivil"""

    def __init__(self, *args, **kwargs):
        super(EstadoCivil, self).__init__(*args, **kwargs)
    estado_civil = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.estado_civil

    class Meta:
        verbose_name = "Estado civil"
        verbose_name_plural = "Estados civil"
        ordering = ['estado_civil']


class TipoDeCliente(models.Model):
    """docstring for TipoDeCliente"""
    tipo_de_cliente = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.tipo_de_cliente

    class Meta:
        verbose_name = "Tipo de cliente"
        verbose_name_plural = "Tipos de cliente"
        ordering = ['tipo_de_cliente']


class TipoDeContacto(models.Model):
    """docstring for TipoDeContacto"""
    tipo_de_contacto = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.tipo_de_contacto

    class Meta:
        verbose_name = "Tipo de contacto"
        verbose_name_plural = "Tipos de contacto"
        ordering = ['tipo_de_contacto']


class TipoDeInformacionDeContacto(models.Model):
    """docstring for TipoDeInformacionDeContacto"""
    tipo_de_informacion_de_contacto = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.tipo_de_informacion_de_contacto

    class Meta:
        verbose_name = "Tipo de información de contacto"
        verbose_name_plural = "Tipos de información de contacto"
        ordering = ['tipo_de_informacion_de_contacto']
