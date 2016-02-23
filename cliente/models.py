"""
docstring

Documentacion del proyecto

"""
from django.db import models
from estadoderegistro.models import EstadoDeRegistro
from django.contrib.auth.models import User
from direccion.models import Direccion


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
    def __init__(self, *args, **kwargs):
        super(TipoDeCliente, self).__init__(*args, **kwargs)
    tipo_de_cliente = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.tipo_de_cliente

    class Meta:
        verbose_name = "Tipo de cliente"
        verbose_name_plural = "Tipos de cliente"
        ordering = ['tipo_de_cliente']


class TipoDeRelacion(models.Model):
    """docstring for TipoDeRelacion"""
    def __init__(self, *args, **kwargs):
        super(TipoDeRelacion, self).__init__(*args, **kwargs)
    tipo_de_relacion = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.tipo_de_relacion

    class Meta:
        verbose_name = "Tipo de relacion"
        verbose_name_plural = "Tipos de relaciones"
        ordering = ['tipo_de_relacion']


class TipoDeInformacionDeContacto(models.Model):
    """docstring for TipoDeInformacionDeContacto"""
    def __init__(self, *args, **kwargs):
        super(TipoDeInformacionDeContacto, self).__init__(*args, **kwargs)
    tipo_de_informacion_de_contacto = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.tipo_de_informacion_de_contacto

    class Meta:
        verbose_name = "Tipo de información de contacto"
        verbose_name_plural = "Tipos de información de contacto"
        ordering = ['tipo_de_informacion_de_contacto']


class Cliente(models.Model):
    """docstring for Cliente"""
    def __init__(self, *args, **kwargs):
        super(Cliente, self).__init__(*args, **kwargs)
    tipo_de_cliente = models.ForeignKey(TipoDeCliente, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class Contacto(models.Model):
    """docstring for Contacto"""
    def __init__(self, *args, **kwargs):
        super(Contacto, self).__init__(*args, **kwargs)
    dni = models.CharField(max_length=15, blank=True)
    nombre = models.CharField(max_length=300)
    cliente = models.ForeignKey(Cliente)
    sexo = models.ForeignKey(Sexo, on_delete=models.PROTECT)
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.PROTECT)
    fecha_nacimiento = models.DateField(blank=True)
    tipo_de_relacion = models.ForeignKey(TipoDeRelacion, on_delete=models.PROTECT)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ['nombre']


class InformacionDeContacto(models.Model):
    """docstring for InformacionDeContacto"""
    def __init__(self, *args, **kwargs):
        super(InformacionDeContacto, self).__init__(*args, **kwargs)
    contacto = models.ForeignKey(Contacto)
    tipo_de_informacion_de_contacto = models.ForeignKey(TipoDeInformacionDeContacto, on_delete=models.PROTECT)
    informacion_de_contacto = models.CharField(max_length=250)

    def __str__(self):
        return u' %s - %s' % (self.contacto, self.tipo_de_informacion_de_contacto)

    class Meta:
        verbose_name = "Información de contacto"
        verbose_name_plural = "Informaciones de contactos"
        ordering = ['contacto', 'tipo_de_informacion_de_contacto']


class ClienteDireccion(models.Model):
    """docstring for ClienteDireccion"""
    def __init__(self, *args, **kwargs):
        super(ClienteDireccion, self).__init__(*args, **kwargs)

    cliente = models.ForeignKey(Cliente)
    direccion = models.ForeignKey(Direccion, on_delete=models.PROTECT)

    def __str__(self):
        return u' %s - %s' % (self.cliente, self.direccion)

    class Meta:
        verbose_name = "Dirección del cliente"
        verbose_name_plural = "Direcciones del cliente"
        ordering = ["cliente", "direccion"]


class ClienteEstadoDeRegistro(models.Model):
    """docstring for ClienteEstadoDeRegistro"""
    def __init__(self, *args, **kwargs):
        super(ClienteEstadoDeRegistro, self).__init__(*args, **kwargs)

    cliente = models.ForeignKey(Cliente)
    estado_de_registro = models.ForeignKey(EstadoDeRegistro)
    fecha = models.DateField(auto_now_add=True, blank=True)
    usuario = models.ForeignKey(User)
    observacion = models.TextField(blank=True)
    predefinido = models.BooleanField(default=None)

    def __str__(self):
        return u' %s - %s' % (self.cliente, self.estado_de_registro)

    class Meta:
        verbose_name = "Estado de registro de cliente"
        verbose_name_plural = "Estados de registro de cliente"
        ordering = ["cliente", "estado_de_registro"]
