"""
docstring

Documentacion del proyecto

"""

from django.db import models
from estadoderegistro.models import EstadoDeRegistro
from gestiondedocumento.models import EstadoDeDocumento
from cotizador.models import Cotizador
from django.contrib.auth.models import User
from mueble.models import EspecificacionDeMueble
from contenedor.models import Contenedor, TipoDeContenido
from ambiente.models import Ambiente
from servicio.models import Servicio
from material.models import Material
from herramienta.models import Herramienta
from cliente.models import Cliente, ClienteDireccion
from almacen.models import Unidad

ORIGEN_CHOICES = (
    ('A', 'Automatico'),
    ('C', 'Call center'),
    ('M', 'Manual'),
    )


# Create your models here.
class TipoDireccion(models.Model):
    """docstring for TipoDireccion"""
    def __init__(self, *args, **kwargs):
        super(TipoDireccion, self).__init__(*args, **kwargs)
    tipo_direccion = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.tipo_direccion

    class Meta:
        verbose_name = "Tipo de dirección"
        verbose_name_plural = "Tipo de direcciones"
        ordering = ['tipo_direccion']


class FechaDeCotizacion(models.Model):
    """docstring for FechaDeCotizacion"""
    def __init__(self, *args, **kwargs):
        super(FechaDeCotizacion, self).__init__(*args, **kwargs)
    nombre_fecha = models.CharField(max_length=100, unique=True)
    obligatoria = models.BooleanField(default=None)

    def __str__(self):
        return self.nombre_fecha

    class Meta:
        verbose_name = "Fecha de cotización"
        verbose_name_plural = "Fechas de cotizaciones"
        ordering = ['nombre_fecha']


class ConceptoDeCotizacion(models.Model):
    """docstring for ConceptoDeCotizacion"""
    def __init__(self, *args, **kwargs):
        super(ConceptoDeCotizacion, self).__init__(*args, **kwargs)
    concepto = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    positivo = models.BooleanField(default=None)

    def __str__(self):
        return self.concepto

    class Meta:
        verbose_name = "Concepto de cotización"
        verbose_name_plural = "Conceptos de cotizaciones"
        ordering = ['concepto']


class TipoAbono(models.Model):
    """docstring for TipoAbono"""
    def __init__(self, *args, **kwargs):
        super(TipoAbono, self).__init__(*args, **kwargs)
    tipo_abono = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tipo_abono

    class Meta:
        verbose_name = "Tipo de abono"
        verbose_name_plural = "Tipos de abonos"
        ordering = ['tipo_abono']


class Cotizacion(models.Model):
    """docstring for Cotizacion"""
    def __init__(self, *args, **kwargs):
        super(Cotizacion, self).__init__(*args, **kwargs)
    cliente = models.ForeignKey(Cliente)
    cotizador = models.ForeignKey(Cotizador, null=True, blank=True)
    numero_contrato = models.CharField(max_length=100, blank=True)
    numero_cotizacion = models.CharField(max_length=100, blank=True)
    nombre_cliente = models.CharField(max_length=300)
    fecha_de_cotizacion = models.DateField(auto_now_add=True, blank=True)
    hora_de_cotizacion = models.TimeField(auto_now_add=True, blank=True)
    tiempo_carga = models.DecimalField(max_digits=7, decimal_places=2,
                                       blank=True, default=0.00)
    total_recorrido_tiempo = models.DecimalField(max_digits=7, decimal_places=2,
                                                 blank=True, default=0.00)
    total_recorrido_km = models.DecimalField(max_digits=7, decimal_places=2,
                                             blank=True, default=0.00)
    nivel_de_complejidad_riesgo = models.CharField(max_length=25, blank=True)
    porcentaje_complejidad_riesgo = models.DecimalField(max_digits=7,
                                                        decimal_places=2,
                                                        default=6)
    como_abona = models.ForeignKey(TipoAbono, null=True, blank=True)

    def __str__(self):
        return str(self.pk)

    def _get_volumen_de_contenedores(self):
        return round((2*2*2)/1000000, 3)
        # falta definir el calculo
    volumen_de_contenedores = property(_get_volumen_de_contenedores)

    def _get_volumen_de_muebles(self):
        return round((2*2*2)/1000000, 3)
        # falta definir el calculo
    volumen_de_muebles = property(_get_volumen_de_muebles)

    def _get_volumen_total(self):
        return round((2*2*2)/1000000, 3)
        # falta definir el calculo
    volumen_total = property(_get_volumen_total)

    class Meta:
        verbose_name = "Cotización"
        verbose_name_plural = "Cotizaciones"
        ordering = ['numero_cotizacion']


class CotizacionDireccion(models.Model):
    """docstring for CotizacionDireccion"""
    def __init__(self, *args, **kwargs):
        super(CotizacionDireccion, self).__init__(*args, **kwargs)
    cotizacion = models.ForeignKey(Cotizacion)
    clientedireccion = models.ForeignKey(ClienteDireccion)
    tipo_direccion = models.ForeignKey(TipoDireccion)
    direccion = models.TextField()
    orden = models.IntegerField()
    nombre_de_edificio = models.CharField(max_length=250, blank=True)
    tipo_de_edificacion = models.CharField(max_length=100, blank=True)
    rampa = models.BooleanField(default=False)
    distancia_del_vehiculo = models.IntegerField(default=0)
    cantidad_pisos = models.IntegerField(default=0)
    escalera_estrecha = models.BooleanField(default=False)
    escalera_inclinada = models.BooleanField(default=False)
    escalon_grande = models.BooleanField(default=False)
    especificacion_de_inmueble = models.CharField(max_length=250, blank=True)
    numero_de_inmueble = models.CharField(max_length=100, blank=True)
    numero_de_pisos = models.IntegerField(default=0)
    nombre_piso = models.CharField(max_length=100, blank=True)
    cantidad_de_ambientes = models.IntegerField(default=0)
    pisos_por_escalera = models.IntegerField(default=0)
    numero_de_plantas = models.IntegerField(default=0)
    total_m2 = models.DecimalField(max_digits=7, decimal_places=2,
                                   null=True, blank=True)
    baulera = models.BooleanField(default=False)
    volumen_baulera = models.DecimalField(max_digits=7, decimal_places=2,
                                          null=True, blank=True)

    def __str__(self):
        return u' %s - %s' % (self.cotizacion, self.direccion)

    class Meta:
        verbose_name = "Dirección de la cotización"
        verbose_name_plural = "Direcciones de la cotización"
        ordering = ['cotizacion', 'orden']


class CotizacionAmbiente(models.Model):
    """docstring for CotizacionAmbiente"""
    def __init__(self, *args, **kwargs):
        super(CotizacionAmbiente, self).__init__(*args, **kwargs)
    direccion_origen = models.ForeignKey(CotizacionDireccion)
    ambiente = models.ForeignKey(Ambiente)
    nombre = models.CharField(max_length=100)
    observaciones = models.TextField()

    def __str__(self):
        return str(self.ambiente)

    def _get_cantidad_muebles(self):
        return round((2*2*2)/1000000, 3)
        # falta definir el calculo
    cantidad_muebles = property(_get_cantidad_muebles)

    def _get_volumen_muebles(self):
        return round((2*2*2)/1000000, 3)
        # falta definir el calculo
    volumen_muebles = property(_get_volumen_muebles)

    def _get_cantidad_contenedores(self):
        return round((2*2*2)/1000000, 3)
        # falta definir el calculo
    cantidad_contenedores = property(_get_cantidad_contenedores)

    def _get_volumen_contenedores(self):
        return round((2*2*2)/1000000, 3)
        # falta definir el calculo
    volumen_contenedores = property(_get_volumen_contenedores)

    class Meta:
        verbose_name = "Ambiente de la cotización"
        verbose_name_plural = "Ambientes de la cotización"
        ordering = ['direccion_origen', 'ambiente']


class CotizacionMueble(models.Model):
    """docstring for CotizacionMueble"""
    def __init__(self, *args, **kwargs):
        super(CotizacionMueble, self).__init__(*args, **kwargs)
    cotizacion_ambiente = models.ForeignKey(CotizacionAmbiente)
    especificacion_de_mueble = models.ForeignKey(EspecificacionDeMueble)
    direccion_destino = models.ForeignKey(CotizacionDireccion)
    nombre_especificacion_de_mueble = models.CharField(max_length=100)
    ancho = models.DecimalField(max_digits=7, decimal_places=2)
    largo = models.DecimalField(max_digits=7, decimal_places=2)
    alto = models.DecimalField(max_digits=7, decimal_places=2)
    cantidad = models.IntegerField()
    volumen_en_camion = models.IntegerField()
    trasladable = models.BooleanField(default=None)
    observaciones = models.TextField()

    def __str__(self):
        return u' %s - %s' % (self.cotizacion_ambiente, self.especificacion_de_mueble)

    def _get_volumen(self):
        return self.especificacion_de_mueble.volumen_de_mueble
        # falta definir el calculo
    volumen = property(_get_volumen)

    class Meta:
        verbose_name = "Mueble de la cotización"
        verbose_name_plural = "Muebles de la cotización"
        ordering = ['cotizacion_ambiente', 'especificacion_de_mueble']


class ContenedorMueble(models.Model):
    """docstring for ContenedorMueble"""
    def __init__(self, *args, **kwargs):
        super(ContenedorMueble, self).__init__(*args, **kwargs)
    cotizacion_mueble = models.ForeignKey(CotizacionMueble)
    contenedor = models.ForeignKey(Contenedor)
    tipo_de_contenido = models.ForeignKey(TipoDeContenido)
    nombre_contenedor = models.CharField(max_length=100)
    cantidad = models.IntegerField()

    def __str__(self):
        return u' %s - %s' % (self.cotizacion_mueble, self.contenedor)

    def _get_volumen_total_en_camion(self):
        return self.contenedor.volumen_en_camion
        # falta definir el calculo
    volumen_total_en_camion = property(_get_volumen_total_en_camion)

    class Meta:
        verbose_name = "Contenedor del mueble"
        verbose_name_plural = "Contenedores del mueble"
        ordering = ['cotizacion_mueble', 'contenedor']


class ServicioMueble(models.Model):
    """docstring for ServicioMueble"""
    def __init__(self, *args, **kwargs):
        super(ServicioMueble, self).__init__(*args, **kwargs)
    cotizacion_mueble = models.ForeignKey(CotizacionMueble)
    servicio = models.ForeignKey(Servicio)
    descripcion_servicio = models.CharField(max_length=100)
    cantidad = models.DecimalField(max_digits=7, decimal_places=2)
    descripcion_cantidad = models.TextField()

    def __str__(self):
        return u' %s - %s' % (self.cotizacion_mueble, self.servicio)

    class Meta:
        verbose_name = "Servicio del mueble"
        verbose_name_plural = "Servicios del mueble"
        ordering = ['cotizacion_mueble', 'servicio']


class CotizacionServicio(models.Model):
    """docstring for CotizacionServicio"""
    def __init__(self, *args, **kwargs):
        super(CotizacionServicio, self).__init__(*args, **kwargs)
    cotizacion = models.ForeignKey(Cotizacion)
    servicio = models.ForeignKey(Servicio)
    nombre_de_servicio = models.CharField(max_length=100)
    complejidad_servicio = models.CharField(max_length=100)
    porcentaje_complejidad = models.DecimalField(max_digits=7, decimal_places=2)
    cantidad_servicio = models.DecimalField(max_digits=7, decimal_places=2)
    monto_servicio = models.DecimalField(max_digits=9, decimal_places=2)
    descripcion_de_monto_servicio = models.TextField()
    monto_servicio_asignado = models.DecimalField(max_digits=9, decimal_places=2)
    incluido_en_precio = models.BooleanField(default=None)
    aplicar_servicio = models.BooleanField(default=None)
    basico = models.BooleanField(default=None)
    observacion = models.TextField()

    def __str__(self):
        return u' %s - %s' % (self.cotizacion, self.servicio)

    class Meta:
        verbose_name = "Servicio de la cotización"
        verbose_name_plural = "Servicios de la cotización"
        ordering = ['cotizacion', 'servicio']


class CotizacionMaterial(models.Model):
    """docstring for CotizacionMaterial"""
    def __init__(self, *args, **kwargs):
        super(CotizacionMaterial, self).__init__(*args, **kwargs)
    cotizacion = models.ForeignKey(Cotizacion)
    material = models.ForeignKey(Material)
    nombre_material = models.CharField(max_length=100)
    cantidad = models.DecimalField(max_digits=7, decimal_places=2)
    descripcion_de_cantidad = models.TextField()
    cantidad_asignada = models.DecimalField(max_digits=7, decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=9, decimal_places=2)
    monto_material = models.DecimalField(max_digits=9, decimal_places=2)
    monto_material_asignado = models.DecimalField(max_digits=9, decimal_places=2)
    peso_unitario = models.DecimalField(max_digits=7, decimal_places=2)
    peso_total = models.DecimalField(max_digits=7, decimal_places=2)
    inlcuido = models.BooleanField(default=None)
    basico = models.BooleanField(default=None)
    aplicar = models.BooleanField(default=None)
    observacion = models.TextField()

    def __str__(self):
        return u' %s - %s' % (self.cotizacion, self.material)

    class Meta:
        verbose_name = "Material de la cotización"
        verbose_name_plural = "Materiales de la cotización"
        ordering = ['cotizacion', 'material']


class CotizacionHerramienta(models.Model):
    """docstring for CotizacionHerramienta"""
    def __init__(self, *args, **kwargs):
        super(CotizacionHerramienta, self).__init__(*args, **kwargs)
    cotizacion = models.ForeignKey(Cotizacion)
    herramienta = models.ForeignKey(Herramienta)
    nombre_herramienta = models.CharField(max_length=100)
    cantidad = models.DecimalField(max_digits=7, decimal_places=2)
    descripcion_de_cantidad = models.TextField()
    cantidad_asignada = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return u' %s - %s' % (self.cotizacion, self.herramienta)

    class Meta:
        verbose_name = "Herramienta de la cotización"
        verbose_name_plural = "Herramientas de la cotización"
        ordering = ['cotizacion', 'herramienta']


class CotizacionPresupuesto(models.Model):
    """docstring for CotizacionPresupuesto"""
    def __init__(self, *args, **kwargs):
        super(CotizacionPresupuesto, self).__init__(*args, **kwargs)
    cotizacion = models.ForeignKey(Cotizacion)
    concepto = models.ForeignKey(ConceptoDeCotizacion)
    nombre_concepto = models.CharField(max_length=100)
    cantidad = models.DecimalField(max_digits=7, decimal_places=2)
    unidad_de_medida = models.ForeignKey(Unidad)
    precio_unitario = models.DecimalField(max_digits=9, decimal_places=2)
    precio_total = models.DecimalField(max_digits=9, decimal_places=2)
    precio_total_asignado = models.DecimalField(max_digits=9, decimal_places=2)
    descripcion_precio_total = models.TextField()

    def __str__(self):
        return u' %s - %s' % (self.cotizacion, self.concepto)

    class Meta:
        verbose_name = "Concepto de la cotización"
        verbose_name_plural = "Conceptos de la cotización"
        ordering = ['cotizacion', 'concepto']


class Abono(models.Model):
    """docstring for Abono"""
    def __init__(self, *args, **kwargs):
        super(Abono, self).__init__(*args, **kwargs)
    cotizacion = models.ForeignKey(Cotizacion)
    usuario_registro = models.ForeignKey(User)
    fecha_registro = models.DateField(auto_now_add=True)
    hora_registro = models.TimeField(auto_now_add=True)
    tipo_abono = models.ForeignKey(TipoAbono)
    monto_pagado = models.DecimalField(max_digits=9, decimal_places=2)
    monto_cotizacion = models.DecimalField(max_digits=9, decimal_places=2)
    banco = models.CharField(max_length=100, blank=True)
    numero_transaccion = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return u' %s - %s' % (self.cotizacion, self.usuario_registro)

    class Meta:
        verbose_name = "Concepto de la cotización"
        verbose_name_plural = "Conceptos de la cotización"
        ordering = ['cotizacion', 'usuario_registro']


class CotizacionComplejidadRiesgo(models.Model):
    """docstring for CotizacionComplejidadRiesgo"""
    def __init__(self, *args, **kwargs):
        super(CotizacionComplejidadRiesgo, self).__init__(*args, **kwargs)
    cotizacion = models.ForeignKey(Cotizacion)
    situacion = models.CharField(max_length=100)
    factor_complejidad = models.IntegerField()
    factor_riesgo = models.IntegerField()
    observacion = models.TextField()

    def __str__(self):
        return u' %s - %s' % (self.cotizacion, self.situacion)

    class Meta:
        verbose_name = "Situación de la cotización"
        verbose_name_plural = "Situaciones de la cotización"
        ordering = ['cotizacion', 'situacion']


class CotizacionBitacora(models.Model):
    """docstring for CotizacionBitacora"""
    def __init__(self, *args, **kwargs):
        super(CotizacionBitacora, self).__init__(*args, **kwargs)
    cotizacion = models.ForeignKey(Cotizacion)
    usuario_registro = models.ForeignKey(User)
    fecha_registro = models.DateField(auto_now_add=True)
    hora_registro = models.TimeField(auto_now_add=True)
    observacion = models.TextField()
    origen_de_registro = models.CharField(max_length=20, choices=ORIGEN_CHOICES)

    def __str__(self):
        return u' %s - %s' % (self.cotizacion, self.observacion)

    class Meta:
        verbose_name = "Observación de la cotización"
        verbose_name_plural = "Observaciones de la cotización"
        ordering = ['cotizacion', 'observacion']


class CotizacionHistoricoFecha(models.Model):
    """docstring for CotizacionHistoricoFecha"""
    def __init__(self, *args, **kwargs):
        super(CotizacionHistoricoFecha, self).__init__(*args, **kwargs)
    cotizacion = models.ForeignKey(Cotizacion)
    usuario_registro = models.ForeignKey(User)
    tipo_fecha = models.ForeignKey(FechaDeCotizacion)
    nombre_tipo_fecha = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    observacion = models.TextField()
    aplicar = models.BooleanField(default=None)

    def __str__(self):
        return u' %s - %s' % (self.cotizacion, self.tipo_fecha)

    class Meta:
        verbose_name = "Observación de la cotización"
        verbose_name_plural = "Observaciones de la cotización"
        ordering = ['cotizacion', 'tipo_fecha']


class CotizacionEstado(models.Model):
    """docstring for CotizacionEstado"""
    def __init__(self, *args, **kwargs):
        super(CotizacionEstado, self).__init__(*args, **kwargs)
    cotizacion = models.ForeignKey(Cotizacion)
    usuario_registro = models.ForeignKey(User)
    estado_de_documento = models.ForeignKey(EstadoDeDocumento, null=True, blank=True)
    estado_de_registro = models.ForeignKey(EstadoDeRegistro, null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    observacion = models.TextField(blank=True)
    predefinido = models.BooleanField(default=None)

    def __str__(self):
        return u' %s - %s' % (self.cotizacion, self.usuario_registro)

    class Meta:
        verbose_name = "Estado de la cotización"
        verbose_name_plural = "Estados de la cotización"
        ordering = ['cotizacion', 'usuario_registro']


class ArgumentoDeVenta(models.Model):
    """docstring for ArgumentoDeVenta"""
    def __init__(self, *args, **kwargs):
        super(ArgumentoDeVenta, self).__init__(*args, **kwargs)
    cotizacion = models.ForeignKey(Cotizacion)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    aplicado = models.BooleanField(default=None)

    def __str__(self):
        return u' %s - %s' % (self.cotizacion, self.titulo)

    class Meta:
        verbose_name = "Argumento de venta"
        verbose_name_plural = "Argumentos de venta"
        ordering = ['cotizacion', 'titulo']
