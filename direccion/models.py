"""
docstring

Documentacion del proyecto

"""
from django.db import models
from smart_selects.db_fields import ChainedForeignKey


# Create your models here.
class Pais(models.Model):
    """docstring for Pais"""
    def __init__(self, *args, **kwargs):
        super(Pais, self).__init__(*args, **kwargs)

    pais = models.CharField(max_length=100, unique=True)
    codigo_telefonico = models.CharField(max_length=10)

    def __str__(self):
        return self.pais

    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"
        ordering = ['pais']


class Provincia(models.Model):
    """docstring for Provincia"""
    def __init__(self, *args, **kwargs):
        super(Provincia, self).__init__(*args, **kwargs)

    provincia = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)
    codigo_telefonico = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.provincia

    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"
        ordering = ['pais', 'provincia']
        unique_together = (("provincia", "pais"),)


class Ciudad(models.Model):
    """docstring for Ciudad"""
    def __init__(self, *args, **kwargs):
        super(Ciudad, self).__init__(*args, **kwargs)

    ciudad = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)
    provincia = ChainedForeignKey(Provincia, chained_field='pais', chained_model_field='pais')

    def __str__(self):
        return self.ciudad

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        ordering = ['provincia', 'ciudad']
        unique_together = (("ciudad", "provincia"),)


class Barrio(models.Model):
    """docstring for Barrio"""
    def __init__(self, *args, **kwargs):
        super(Barrio, self).__init__(*args, **kwargs)

    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)
    provincia = ChainedForeignKey(Provincia, chained_field='pais', chained_model_field='pais')
    ciudad = ChainedForeignKey(Ciudad, chained_field='provincia', chained_model_field='provincia')
    barrio = models.CharField(max_length=100)

    def __str__(self):
        return self.barrio

    class Meta:
        verbose_name = "Barrio"
        verbose_name_plural = "Barrios"
        ordering = ['ciudad', 'barrio']
        unique_together = (("barrio", "ciudad"),)


class Direccion(models.Model):
    """docstring for Direccion"""
    def __init__(self, *args, **kwargs):
        super(Direccion, self).__init__(*args, **kwargs)

    calle = models.CharField(max_length=100)
    altura = models.CharField(max_length=100)
    barrio = ChainedForeignKey(Barrio, chained_field='ciudad', chained_model_field='ciudad')
    ciudad = ChainedForeignKey(Ciudad, chained_field='provincia', chained_model_field='provincia')
    provincia = ChainedForeignKey(Provincia, chained_field='pais', chained_model_field='pais')
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)
    zip = models.CharField(max_length=100, blank=True)
    punto_referencia = models.TextField(blank=True)
    observacion = models.TextField(blank=True)

    def __str__(self):

        return u' %s - %s - %s' % (self.calle, self.altura, self.barrio)

    def full_direccion(self):
        return '%s. %s, %s barrio %s, %s, %s %s' % (self.pais, self.provincia,
                                                    self.ciudad, self.barrio,
                                                    "calle "+self.calle,
                                                    "altura "+self.altura,
                                                    "Punto de referencia "+self.punto_referencia)

    class Meta:
        verbose_name = "Dirección"
        verbose_name_plural = "Direcciones"


class TipoDeEdificacion(models.Model):
    """docstring for TipoDeEdificacion"""
    def __init__(self, *args, **kwargs):
        super(TipoDeEdificacion, self).__init__(*args, **kwargs)

    tipo_de_edificacion = models.CharField(max_length=100)
    descripcion = models.TextField()
    nombre = models.BooleanField(default=None)

    def __str__(self):
        return self.tipo_de_edificacion

    class Meta:
        verbose_name = "Tipo de edificación"
        verbose_name_plural = "Tipos de edificación"


class Edificacion(models.Model):
    """docstring for Edificacion"""
    def __init__(self, *args, **kwargs):
        super(Edificacion, self).__init__(*args, **kwargs)

    direccion = models.ForeignKey(Direccion)
    nombre_de_edificio = models.CharField(max_length=250, blank=True)
    tipo_de_edificacion = models.ForeignKey(TipoDeEdificacion, on_delete=models.PROTECT)
    cantidad_de_pisos = models.IntegerField(null=True, blank=True)
    cantidad_de_inmuebles_por_piso = models.IntegerField(null=True, blank=True)
    total_inmuebles = models.IntegerField(null=True, blank=True)
    rampa = models.BooleanField(default=None)
    distancia_del_vehiculo = models.IntegerField(null=True, blank=True)
    escalera_estrecha = models.BooleanField(default=None)
    escalera_inclinada = models.BooleanField(default=None)
    escalon_grande = models.BooleanField(default=None)

    def __str__(self):
        return self.nombre_de_edificio

    class Meta:
        verbose_name = "Edificación"
        verbose_name_plural = "Edificaciones"


class TipoDeAscensor(models.Model):
    """docstring for TipoDeAscensor"""
    def __init__(self, *args, **kwargs):
        super(TipoDeAscensor, self).__init__(*args, **kwargs)

    tipo_de_ascensor = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.tipo_de_ascensor

    class Meta:
        verbose_name = "Tipo de ascensor"
        verbose_name_plural = "Tipos de ascensor"


class Ascensor(models.Model):
    """docstring for Ascensor"""
    def __init__(self, *args, **kwargs):
        super(Ascensor, self).__init__(*args, **kwargs)

    edificacion = models.ForeignKey(Edificacion)
    tipo_de_ascensor = models.ForeignKey(TipoDeAscensor, on_delete=models.PROTECT)
    cantidad = models.IntegerField(default=1)
    piso_ascensor = models.IntegerField()
    velocidad_por_piso = models.DecimalField(max_digits=7, decimal_places=2, default=6)
    ancho = models.DecimalField(max_digits=7, decimal_places=2)
    largo = models.DecimalField(max_digits=7, decimal_places=2)
    alto = models.DecimalField(max_digits=7, decimal_places=2)
    capacidad_carga = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return u' %s - %s' % (self.edificacion, self.tipo_de_ascensor)

    class Meta:
        verbose_name = "Ascensor"
        verbose_name_plural = "Ascensores"


class TipoDeInmueble(models.Model):
    """docstring for TipoDeInmueble"""
    def __init__(self, *args, **kwargs):
        super(TipoDeInmueble, self).__init__(*args, **kwargs)

    tipo_de_inmueble = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.tipo_de_inmueble

    class Meta:
        verbose_name = "Tipo de inmueble"
        verbose_name_plural = "Tipos de inmueble"
        ordering = ['tipo_de_inmueble']


class EspecificacionDeInmueble(models.Model):
    """docstring for EspecificacionDeInmueble"""
    def __init__(self, *args, **kwargs):
        super(EspecificacionDeInmueble, self).__init__(*args, **kwargs)

    tipo_de_inmueble = models.ForeignKey(TipoDeInmueble, on_delete=models.PROTECT)
    especificacion_de_inmueble = models.CharField(max_length=250)
    descripcion = models.TextField()
    predeterminado = models.BooleanField(default=None)

    def __str__(self):
        return self.especificacion_de_inmueble

    class Meta:
        verbose_name = "Especificación de inmueble"
        verbose_name_plural = "Especificaciones de inmueble"
        ordering = ['especificacion_de_inmueble']


class Inmueble(models.Model):
    """docstring for Inmueble"""
    def __init__(self, *args, **kwargs):
        super(Inmueble, self).__init__(*args, **kwargs)

    edificacion = models.ForeignKey(Edificacion)
    especificacion_de_inmueble = models.ForeignKey(EspecificacionDeInmueble,
                                                   on_delete=models.PROTECT)
    numero_de_inmueble = models.CharField(max_length=100)
    numero_de_pisos = models.IntegerField(null=True, blank=True)
    nombre_del_piso = models.CharField(max_length=100, blank=True)
    cantidad_de_ambientes = models.IntegerField()
    pisos_por_escalera = models.IntegerField(default=0, blank=True)
    numero_de_plantas = models.IntegerField(default=1, blank=True)
    total_m2 = models.DecimalField(max_digits=7, decimal_places=2,
                                   null=True, blank=True)
    baulera = models.BooleanField(default=False)
    volumen_baulera = models.DecimalField(max_digits=7, decimal_places=2,
                                          null=True, blank=True)

    def __str__(self):
        return str(self.numero_de_inmueble)

    class Meta:
        verbose_name = "Inmueble"
        verbose_name_plural = "Inmuebles"
        ordering = ['numero_de_inmueble']


class HorarioDisponible(models.Model):
    """docstring for HorarioDisponible"""
    def __init__(self, *args, **kwargs):
        super(HorarioDisponible, self).__init__(*args, **kwargs)

    edificacion = models.ForeignKey(Edificacion)
    lunes = models.BooleanField(default=None)
    martes = models.BooleanField(default=None)
    miercoles = models.BooleanField(default=None)
    jueves = models.BooleanField(default=None)
    viernes = models.BooleanField(default=None)
    sabado = models.BooleanField(default=None)
    domingo = models.BooleanField(default=None)
    hora_desde = models.TimeField()
    hora_hasta = models.TimeField()
    edificio = models.BooleanField(default=None)
    ascensor = models.BooleanField(default=None)
    observacion = models.TextField(blank=True)

    def __str__(self):
        return str(self.edificacion)

    class Meta:
        verbose_name = "Horario disponible"
        verbose_name_plural = "Horarios disponibles"


class Calle(models.Model):
    """docstring for Calle"""
    def __init__(self, *args, **kwargs):
        super(Calle, self).__init__(*args, **kwargs)

    ciudad = models.ForeignKey(Ciudad)
    calle = models.CharField(max_length=100)

    def __str__(self):
        return self.calle

    class Meta:
        verbose_name = "Calle"
        verbose_name_plural = "Calles"
        ordering = ['ciudad', 'calle']
        unique_together = (("calle", "ciudad"),)
