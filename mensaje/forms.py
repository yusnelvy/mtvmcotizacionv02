"""
Docstring documentación pendiente

"""

from django.forms import ModelForm
from mensaje.models import TipoDeMensaje, Mensaje
from base.forms import BaseFormMd


class TipoDeMensajeForm(ModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """

    class Meta:
        model = TipoDeMensaje
        fields = '__all__'


class MensajeForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Mensaje
        fields = '__all__'
