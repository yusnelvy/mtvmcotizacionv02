"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput
from django import forms
from ambiente.models import Ambiente, AmbientePorTipoDeInmueble
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd, SelectMD, Checkbox
from direccion.models import EspecificacionDeInmueble


class AmbienteForm(NgModelFormMixin, NgModelForm, BaseFormMd):
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
            'ambiente': TextInput(attrs={'required': 'required', 'tabindex': '-1'}),

        }


class AmbientePorTipoDeInmuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    def __init__(self, *args, **kwargs):
        super(AmbientePorTipoDeInmuebleForm, self).__init__(*args, **kwargs)
        self.fields['ambiente'].empty_label = None
        self.fields['especificacion_de_inmueble'].empty_label = None

    ch_agregar = forms.BooleanField(required=False)

    class Meta:
        model = AmbientePorTipoDeInmueble
        fields = '__all__'


class AmbientePorTipoDeInmuebleForm2(forms.Form):
    """
    Docstring documentación pendiente
    """
    ambiente_choices = [(ambiente.id, ambiente.ambiente) for ambiente in Ambiente.objects.all()]
    inmueble_choices = [(inmueble.id, inmueble.especificacion_de_inmueble) for inmueble in EspecificacionDeInmueble.objects.all()]

    ch_agregar = forms.BooleanField(required=False)
    ambiente = forms.ChoiceField(label='Ambiente',
                                 choices=ambiente_choices)
    especificacion_de_inmueble = forms.ChoiceField(label='Especificación de inmueble',
                                                   choices=inmueble_choices)
    predeterminado = forms.BooleanField(required=False)
