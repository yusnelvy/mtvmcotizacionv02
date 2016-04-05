from django.db import models
from estadoderegistro.models import EstadoDeRegistro
from django.contrib.auth.models import User
from direccion.models import Barrio
from cliente.models import Cliente


# Create your models here.
class Medio(models.Model):
    """docstring for Medio"""
    def __init__(self, *args, **kwargs):
        super(Medio, self).__init__(*args, **kwargs)

    medio = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.medio

    class Meta:
        verbose_name = "Medio"
        verbose_name_plural = "Medios"


class MedioEspecifico(models.Model):
    """docstring for MedioEspecifico"""
    def __init__(self, *args, **kwargs):
        super(MedioEspecifico, self).__init__(*args, **kwargs)

    medio = models.ForeignKey(Medio, on_delete=models.PROTECT)
    medio_especifico = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.medio_especifico

    class Meta:
        verbose_name = "Medio especifico"
        verbose_name_plural = "Medios especificos"


class TipoDeReferido(models.Model):
    """docstring for TipoDeReferido"""
    def __init__(self, *args, **kwargs):
        super(TipoDeReferido, self).__init__(*args, **kwargs)

    medio_especifico = models.ForeignKey(MedioEspecifico, on_delete=models.PROTECT)
    tipo_de_referido = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.tipo_de_referido

    class Meta:
        verbose_name = "Tipo de referido"
        verbose_name_plural = "Tipos de referidos"


class Alianza(models.Model):
    """docstring for Alianza"""
    def __init__(self, *args, **kwargs):
        super(Alianza, self).__init__(*args, **kwargs)

    medio_especifico = models.ForeignKey(MedioEspecifico, on_delete=models.PROTECT)
    alianza = models.CharField(max_length=100)
    porcentaje_comision = models.DecimalField(max_digits=7, decimal_places=2)
    observacion = models.TextField()
    fecha_vigencia = models.DateField()

    def __str__(self):
        return self.alianza

    class Meta:
        verbose_name = "Alianza"
        verbose_name_plural = "Alianzas"


class AlianzaEstado(models.Model):
    """docstring for AlianzaEstado"""
    def __init__(self, *args, **kwargs):
        super(AlianzaEstado, self).__init__(*args, **kwargs)

    alianza = models.ForeignKey(Alianza)
    estado_de_registro = models.ForeignKey(EstadoDeRegistro)
    fecha = models.DateField(auto_now_add=True, blank=True)
    usuario = models.ForeignKey(User)
    observacion = models.TextField(blank=True)
    predefinido = models.BooleanField(default=None)

    def __str__(self):
        return u' %s - %s' % (self.alianza, self.estado_de_registro)

    class Meta:
        verbose_name = "Estado de registro de alianza"
        verbose_name_plural = "Estados de registro de alianza"
        ordering = ["alianza", "estado_de_registro"]


class Institucion(models.Model):
    """docstring for Institucion"""
    def __init__(self, *args, **kwargs):
        super(Institucion, self).__init__(*args, **kwargs)

    alianza = models.ForeignKey(Alianza, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=250)
    cuit = models.CharField(max_length=25)
    pagina_web = models.CharField(max_length=250, blank=True)
    persona_contacto = models.CharField(max_length=250)
    telefono = models.CharField(max_length=25)
    telefono_movil = models.CharField(max_length=25)
    email = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Institución"
        verbose_name_plural = "Instituciones"


class PersonaAliado(models.Model):
    """docstring for PersonaAlaido"""
    def __init__(self, *args, **kwargs):
        super(PersonaAliado, self).__init__(*args, **kwargs)

    institucion = models.ForeignKey(Institucion, on_delete=models.PROTECT)
    dni = models.CharField(max_length=15, blank=True)
    nombre = models.CharField(max_length=250)
    telefono = models.CharField(max_length=100)
    telefono_movil_1 = models.CharField(max_length=25, blank=True)
    telefono_movil_2 = models.CharField(max_length=25, blank=True)
    email_principal = models.CharField(max_length=250, blank=True)
    email_secundario = models.CharField(max_length=250, blank=True)
    observacion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"


class FuenteDePromocion(models.Model):
    """docstring for FuenteDePromocion"""
    def __init__(self, *args, **kwargs):
        super(FuenteDePromocion, self).__init__(*args, **kwargs)

    medio_especifico = models.ForeignKey(MedioEspecifico, on_delete=models.PROTECT)
    tipo_de_referido = models.ForeignKey(TipoDeReferido, on_delete=models.PROTECT)
    barrio = models.ForeignKey(Barrio)
    cliente = models.ForeignKey(Cliente)
    nombre_referido = models.CharField(max_length=250, blank=True)
    telefono_referido = models.CharField(max_length=100, blank=True)
    persona_aliado = models.ForeignKey(PersonaAliado)
    institucion_aliado = models.TextField()
    alianza = models.TextField()
    condiciones_de_calculo_alianza = models.TextField()

    def __str__(self):
        return u' %s - %s' % (self.medio_especifico, self.tipo_de_referido)

    class Meta:
        verbose_name = "Fuente de promoción"
        verbose_name_plural = "Fuentes de promociones"
