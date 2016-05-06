"""
Docstring documentación pendiente

"""
from django.forms import ModelForm
from notificacion.models import Notificacion


class NotificacionForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Notificacion
        fields = '__all__'
