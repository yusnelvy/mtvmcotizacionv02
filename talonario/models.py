from django.db import models
from estadoderegistro.models import EstadoDeRegistro
from django.contrib.auth.models import User


# Create your models here.
class TipoDeDocumentoImpreso(models.Model):
    """docstring for TipoDeDocumentoImpreso"""
    def __init__(self, *args, **kwargs):
        super(TipoDeDocumentoImpreso, self).__init__(*args, **kwargs)

    tipo_de_documento_impreso = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.tipo_de_documento_impreso

    class Meta:
        verbose_name = "Tipo de documento impreso"
        verbose_name_plural = "Tipos de documento impreso"
        ordering = ["tipo_de_documento_impreso"]


class Talonario(models.Model):
    """docstring for Talonario"""
    def __init__(self, *args, **kwargs):
        super(Talonario, self).__init__(*args, **kwargs)

    talonario = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    prefijo = models.CharField(max_length=10, blank=True)
    separador = models.CharField(max_length=10, blank=True)
    numero_desde = models.CharField(max_length=50)
    numero_hasta = models.CharField(max_length=50)
    separado_sufijo = models.CharField(max_length=10, blank=True)
    sufijo = models.CharField(max_length=10, blank=True)
    numeracion_correlativa = models.BooleanField(default=None)
    numero_de_documento = models.IntegerField()
    tipo_de_documento_impreso = models.ForeignKey(TipoDeDocumentoImpreso)
    cantidad_fija = models.BooleanField(default=None)

    def __str__(self):
        return self.talonario

    class Meta:
        verbose_name = "Talonario"
        verbose_name_plural = "Talonarios"
        ordering = ["talonario"]


class DocumentoDelTalonario(models.Model):
    """docstring for DocumentoDelTalonario"""
    def __init__(self, *args, **kwargs):
        super(DocumentoDelTalonario, self).__init__(*args, **kwargs)

    talonario = models.ForeignKey(Talonario)
    numero = models.CharField(max_length=50)
    estado = models.CharField(max_length=10)
    informacion_de_proceso = models.TextField()
    informacion_de_beneficiari = models.TextField()
    numero_final = models.CharField(max_length=250)

    def __str__(self):
        return u' %s - %s' % (self.talonario, self.numero)

    class Meta:
        verbose_name = "Documento del talonario"
        verbose_name_plural = "Documentos del talonario"
        ordering = ["talonario", "numero"]


class TalonarioEstado(models.Model):
    """docstring for TalonarioEstado"""
    def __init__(self, *args, **kwargs):
        super(TalonarioEstado, self).__init__(*args, **kwargs)

    talonario = models.ForeignKey(Talonario)
    estado_de_documento = models.ForeignKey(EstadoDeRegistro)
    fecha_registro = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(User)
    observacion = models.TextField(blank=True)
    predefinido = models.BooleanField(default=None)

    def __str__(self):
        return u' %s - %s' % (self.talonario, self.estado_de_documento)

    class Meta:
        verbose_name = "Estado del talonario"
        verbose_name_plural = "Estados de los talonarios"
        ordering = ["talonario", "estado_de_documento"]


class TrazabilidadTalonario(models.Model):
    """docstring for TrazabilidadTalonario"""
    def __init__(self, *args, **kwargs):
        super(TrazabilidadTalonario, self).__init__(*args, **kwargs)

    talonario = models.ForeignKey(Talonario)
    fecha_registro = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(null=True, blank=True)
    usuario = models.ForeignKey(User)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = "Trazabilidad del talonario"
        verbose_name_plural = "Trazabilidad de los talonarios"


class DocumentoDelTalonarioEstado(models.Model):
    """docstring for DocumentoDelTalonarioEstado"""
    def __init__(self, *args, **kwargs):
        super(DocumentoDelTalonarioEstado, self).__init__(*args, **kwargs)

    documento_del_talonario = models.ForeignKey(DocumentoDelTalonario)
    estado_de_documento = models.ForeignKey(EstadoDeRegistro)
    fecha_registro = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(User)
    observacion = models.TextField(blank=True)
    predefinido = models.BooleanField(default=None)

    def __str__(self):
        return u' %s - %s' % (self.documento_del_talonario, self.estado_de_documento)

    class Meta:
        verbose_name = "Estado del documento del talonario"
        verbose_name_plural = "Estados de los documentos de los talonarios"
        ordering = ["documento_del_talonario", "estado_de_documento"]
