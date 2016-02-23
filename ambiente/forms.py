"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput
from ambiente.models import Ambiente, AmbientePorTipoDeInmueble
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd, SelectMD, Checkbox


class AmbienteForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Ambiente
        fields = '__all__'
        labels = {
            'ambiente': ('Nombre del ambiente'),
            'descripcion': ('Descripción del ambiente')
        }
        widgets = {
            'ambiente': TextInput(attrs={'required': 'required'}),
            'descripcion': TextInput(attrs={'required': 'required'}),
        }


class AmbientePorTipoDeInmuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = AmbientePorTipoDeInmueble
        fields = '__all__'
