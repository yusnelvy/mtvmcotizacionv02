"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput
from mensaje.models import TipoDeMensaje, Mensaje
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd, SelectMD, Checkbox


class TipoDeMensajeForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """

    class Meta:
        model = TipoDeMensaje
        fields = '__all__'
        widgets = {
            'tipo_de_mensaje': TextInput(attrs={'required': 'required'}),
            'descripcion': TextInput(attrs={'required': 'required'})
            }
        labels = {
            'tipo_de_mensaje': ('Nombre del tipo de mensaje'),
            'descripcion': ('Descripción del tipo de mensaje')
        }


class MensajeForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Mensaje
        fields = '__all__'
        widgets = {
            'mensaje': TextInput(attrs={'required': 'required'}),
            'descripcion': TextInput(attrs={'required': 'required'}),
            'codigo': TextInput(attrs={'required': 'required'}),
            'tipo_de_mensaje': SelectMD()
            }
        labels = {
            'tipo_de_mensaje': ('Nombre del tipo de mensaje'),
            'mensaje': ('Texto del mensaje'),
            'codigo': ('Código del mensaje'),
            'descripcion': ('Descripción del tipo de mensaje')
        }
