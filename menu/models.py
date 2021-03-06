from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Menu(models.Model):
    """docstring for Menu"""
    def __init__(self, *args, **kwargs):
        super(Menu, self).__init__(*args, **kwargs)

    menu = models.CharField(max_length=250)
    transaccion = models.CharField(max_length=20, unique=True)
    namespace = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    nivel = models.IntegerField()
    padre = models.BooleanField(default=False)
    menu_padre = models.ForeignKey("self", null=True,
                                   blank=True,
                                   related_name='nenuchild_set')

    def __str__(self):
        return self.menu

    class Meta:
        verbose_name = "menu"
        verbose_name_plural = "Menus"
        ordering = ["menu"]


class MenuFavorito(models.Model):
    """docstring for MenuFavorito"""
    def __init__(self, *args, **kwargs):
        super(MenuFavorito, self).__init__(*args, **kwargs)

    usuario = models.ForeignKey(User)
    menu = models.ForeignKey(Menu)
    grupo = models.CharField(max_length=100)
    orden = models.IntegerField()

    def __str__(self):
        return u' %s - %s - %s' % (self.usuario,
                                   self.menu,
                                   self.grupo)

    class Meta:
        verbose_name = "Menu favorito"
        verbose_name_plural = "Menus favoritos"
        ordering = ["usuario", "menu", "grupo"]


class Relacion(models.Model):
    """docstring for Relación"""
    def __init__(self, *args, **kwargs):
        super(Relacion, self).__init__(*args, **kwargs)

    item_origen = models.ForeignKey(Menu, related_name="item_origen")
    item_relacion = models.ForeignKey(Menu, related_name="item_relacion")
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return u' %s - %s - %s' % (self.item_origen,
                                   self.item_relacion,
                                   self.nombre)

    class Meta:
        verbose_name = "Relación"
        verbose_name_plural = "Relaciones"
