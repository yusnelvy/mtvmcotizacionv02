"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput, NumberInput, Textarea
from complejidadriesgo.models import ComplejidadRiesgo, NivelComplejidadRiesgo
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd, SelectMD, Checkbox
from django import forms

class ComplejidadRiesgoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = ComplejidadRiesgo
        fields = '__all__'
        widgets = {
            'situacion': TextInput(attrs={'required': 'required', 'tabindex':'1'}),
            'descripcion': Textarea(attrs={'required': 'required', 'tabindex': '2', 'cols': '1', 'rows': '1'}),
        }
        labels = {
            'situacion': ('Nombre de la situación'),
            'descripcion': ('Descripción de la situación'),
            'factor_complejidad': ('Factor de complejidad de la situación'),
            'factor_riesgo': ('Factor de riesgo de la situación')
        }


class NivelComplejidadRiesgoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = NivelComplejidadRiesgo
        fields = '__all__'
        widgets = {
            'nivel_complejidad_riesgo': TextInput(attrs={'required': 'required', 'tabindex':'1'}),
            'factor_inicial': NumberInput(attrs={'required': 'required', 'tabindex':'2'}),
            'factor_final': NumberInput(attrs={'required': 'required', 'tabindex':'3'})
        }
        labels = {
            'nivel_complejidad_riesgo': ('Nombre del nivel complejidad y riesgo'),
            'factor_inicial': ('Factor inicial del nivel de complejidad y riesgo'),
            'factor_final': ('Factor final del nivel de complejidad y riesgo'),
            'porcentaje': ('Porcentaje del nivel de complejidad y riesgo')
        }

