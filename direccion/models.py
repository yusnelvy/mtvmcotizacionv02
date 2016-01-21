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

    pais = models.CharField(max_length=250, unique=True)

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
    zip = models.CharField(max_length=100)
    punto_referencia = models.CharField(max_length=250)
    adicional = models.CharField(max_length=250, blank=True)

    def __str__(self):

        return u' %s - %s - %s' % (self.calle, self.altura, self.barrio)

    def full_direccion(self):
        return '%s. %s, %s barrio %s, %s, %s %s' % (self.pais, self.provincia,
                                                    self.ciudad, self.barrio,
                                                    "calle "+self.calle,
                                                    "altura "+self.altura,
                                                    "Punto de referencia "+self.punto_referencia)

    class Meta:
        verbose_name = "Direccion"
        verbose_name_plural = "Direcciones"


class TipoDeEdificacion(models.Model):
    """docstring for TipoDeEdificacion"""
    def __init__(self, *args, **kwargs):
        super(TipoDeEdificacion, self).__init__(*args, **kwargs)

    tipo_de_edificacion = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.tipo_de_edificacion

    class Meta:
        verbose_name = "Tipo de edificación"
        verbose_name_plural = "Tipos de edificación"


class Edificio(models.Model):
    """docstring for Edificio"""
    def __init__(self, *args, **kwargs):
        super(Edificio, self).__init__(*args, **kwargs)

    nombre_de_edificio = models.CharField(max_length=100)
    tipo_de_edificacion = models.ForeignKey(TipoDeEdificacion, on_delete=models.PROTECT)
    cantidad_de_pisos = models.IntegerField()
    cantidad_de_inmuebles_por_piso = models.IntegerField()
    total_inmuebles = models.IntegerField()
    rampa = models.BooleanField(default=False)
    distancia_del_vehiculo = models.IntegerField()
    escalera_estrecha = models.BooleanField(default=False)
    escalera_inclinada = models.BooleanField(default=False)
    escalon_grande = models.BooleanField(default=False)

    def __str__(self):
        return self.tipo_de_edificacion

    class Meta:
        verbose_name = "Tipo de edificación"
        verbose_name_plural = "Tipos de edificación"


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

    edificio = models.ForeignKey(Edificio)
    tipo_de_ascensor = models.ForeignKey(TipoDeAscensor)
    cantidad = models.IntegerField()
    piso_ascensor = models.IntegerField()
    velocidad_por_piso = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return u' %s - %s' % (self.edificio, self.tipo_de_ascensor)

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
    especificacion_de_inmueble = models.CharField(max_length=100)
    descripcion = models.TextField()

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

    edificio = models.ForeignKey(Edificio)
    especificacion_de_inmueble = models.ForeignKey(EspecificacionDeInmueble, on_delete=models.PROTECT)
    numero_de_inmueble = models.IntegerField()
    numero_de_pisos = models.IntegerField()
    nombre_del_piso = models.CharField(max_length=100)
    cantidad_de_ambientes = models.IntegerField()
    pisos_por_escalera = models.IntegerField()
    numero_de_plantas = models.IntegerField()
    total_m2 = models.DecimalField(max_digits=7, decimal_places=2)
    baulera = models.BooleanField(default=False)
    volumen_baulera = models.DecimalField(max_digits=8, decimal_places=3)

    def __str__(self):
        return str(self.numero_de_inmueble)

    class Meta:
        verbose_name = "Inmueble"
        verbose_name_plural = "Inmuebles"
        ordering = ['numero_de_inmueble']
