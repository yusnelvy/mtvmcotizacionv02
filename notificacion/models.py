from django.db import models
from django.contrib.auth.models import User
from gestiondedocumento.models import EstadoDeDocumento


# Create your models here.
class Notificacion(models.Model):
    """docstring for Notificación"""
    def __init__(self, *args, **kwargs):
        super(Notificacion, self).__init__(*args, **kwargs)

    origen = models.CharField(max_length=100)
    titulo = models.CharField(max_length=250)
    texto = models.TextField()
    estado = models.CharField(max_length=100, blank=True)
    fecha_entrega = models.DateTimeField()
    fecha_alerta = models.DateTimeField()
    log = models.TextField(blank=True)
    url = models.CharField(max_length=500)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="user")
    user_origen = models.ForeignKey(User, related_name="user_origen")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Notificación"
        verbose_name_plural = "Notificaciones"
        ordering = ["titulo"]


class NotificacionEstado(models.Model):
    """docstring for NotificacionEstado"""
    def __init__(self, *args, **kwargs):
        super(NotificacionEstado, self).__init__(*args, **kwargs)
    notificacion = models.ForeignKey(Notificacion)
    usuario_registro = models.ForeignKey(User)
    estado_de_documento = models.ForeignKey(EstadoDeDocumento)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    observacion = models.TextField(blank=True)
    predefinido = models.BooleanField(default=None)

    def __str__(self):
        return u' %s - %s' % (self.notificacion, self.usuario_registro)

    class Meta:
        verbose_name = "Estado de la notificación"
        verbose_name_plural = "Estados de la notificación"
        ordering = ['notificacion', 'usuario_registro']
