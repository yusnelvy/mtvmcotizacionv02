"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput, Textarea
from ambiente.models import Ambiente, AmbientePorTipoDeInmueble
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd, SelectMD, Checkbox


class AmbienteForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Ambiente
        fields = '__all__'
        labels = {
            'ambiente': ('Nombre del ambiente'),
            'descripcion': ('Descripción del ambiente'),
            'conteo_de_ambientes': ('¿El ambiente es contable?')
        }
        widgets = {
            'ambiente': TextInput(attrs={'required': 'required', 'tabindex': '1'}),
            'descripcion': Textarea(attrs={'required': 'required', 'tabindex': '2', 'cols': '1', 'rows': '1'}),
            'conteo_de_ambientes': Checkbox(attrs={'tabindex': '3'}),

        }


class AmbientePorTipoDeInmuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = AmbientePorTipoDeInmueble
        fields = '__all__'
