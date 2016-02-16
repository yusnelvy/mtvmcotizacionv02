"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput
from mueble.models import TipoDeMueble, Mueble, \
    EspecificacionDeMueble, MueblePorAmbiente
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd
#from django.forms.forms import _html_output


class TipoDeMuebleForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    class Meta:
        model = TipoDeMueble
        fields = '__all__'
        widgets = {
            'tipo_de_mueble': TextInput(attrs={'required': 'required'})
            }
        labels = {
            'descripcion': ('Descripción del tipo de mueble'),
            'tipo_de_mueble': ('Nombre del tipo de mueble')
            }


class MuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Mueble
        fields = '__all__'
        widgets = {
            'descripcion': TextInput()
            }


class EspecificacionDeMuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = EspecificacionDeMueble
        fields = '__all__'


class MueblePorAmbienteForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = MueblePorAmbiente
        fields = '__all__'
