from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Widget(models.Model):
    """docstring for Widget"""
    def __init__(self, *args, **kwargs):
        super(Widget, self).__init__(*args, **kwargs)

    usuario = models.ForeignKey(User)
    nombre = models.CharField(max_length=100)
    visible = models.BooleanField(default=None)
    desplegable = models.IntegerField()
    numero_de_columna = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    orden = models.IntegerField()

    def __str__(self):
        return u' %s - %s' % (self.usuario, self.nombre)

    class Meta:
        verbose_name = "Widget"
        verbose_name_plural = "Widgetes"
        ordering = ["nombre"]
        unique_together = (("usuario", "nombre"),)
