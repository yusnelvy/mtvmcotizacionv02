"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput, Textarea, Select
from mueble.models import TipoDeMueble, Mueble, \
    EspecificacionDeMueble, MueblePorAmbiente
from djangular.forms import NgModelFormMixin, NgModelForm
from djangular.forms.widgets import CheckboxChoiceInput
from base.forms import BaseFormMd, SelectMD, Checkbox, selectSearchMD
#from djangular.forms import CheckboxChoiceInput, CheckboxFieldRenderer, CheckboxFieldRendererMixin
#from django.forms.forms import _html_output
from django.forms.widgets import CheckboxFieldRenderer
from django import forms


class TipoDeMuebleForm(ModelForm):
    class Meta:
        model = TipoDeMueble
        fields = '__all__'
        widgets = {
            'tipo_de_mueble': TextInput(attrs={'required': 'required', 'tabindex':'1'}),
            'descripcion': Textarea(attrs={'required': 'required', 'tabindex': '2', 'cols': '1', 'rows': '1'}),
            }
        labels = {
            'descripcion': ('Descripción del tipo de mueble'),
            'tipo_de_mueble': ('Nombre del tipo de mueble')
            }


class MuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    def __init__(self, *args, **kwargs):
        super(MuebleForm, self).__init__(*args, **kwargs)
        self.fields['tipo_de_mueble'].empty_label = 'Seleccione un tipo de mueble'

    class Meta:
        model = Mueble
        fields = '__all__'
        widgets = {
            'tipo_de_mueble': Select(attrs={'required': 'required', 'tabindex': '1', 'ng-change': 'onChange()'}),
            'mueble': TextInput(attrs={'required': 'required', 'tabindex': '2'}),
            'descripcion': Textarea(attrs={'required': 'required', 'tabindex': '3', 'cols': '1', 'rows': '1'}),
            'trasladable': Checkbox(attrs={'tabindex': '4'}),
            'fragil': Checkbox(attrs={'tabindex': '5'}),
            'pesado': Checkbox(attrs={'tabindex': '6'}),
            'contenido_fragil': Checkbox(attrs={'tabindex': '7'}),
            'contenido_textil': Checkbox(attrs={'tabindex': '8'}),
            }
        labels = {
            'tipo_de_mueble': ('Tipo de mueble asociado'),
            'mueble': ('Nombre del mueble'),
            'descripcion': ('Descripción del mueble'),
            'trasladable': ('¿Mueble trasladable?'),
            'fragil': ('¿Mueble fragil?'),
            'pesado': ('¿Mueble pesado?'),
            'contenido_fragil': ('¿Posee contenido fragil?'),
            'contenido_textil': ('¿Posee contenido textil?')
            }


class EspecificacionDeMuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    def __init__(self, *args, **kwargs):
        super(EspecificacionDeMuebleForm, self).__init__(*args, **kwargs)
        self.fields['mueble'].empty_label = 'Seleccione un mueble'

    class Meta:
        model = EspecificacionDeMueble
        fields = '__all__'
        widgets = {
            'mueble': Select(attrs={'required': 'required', 'tabindex': '1', 'ng-change': 'onChange()'}),
            'especificacion_de_mueble': TextInput(attrs={'required': 'required', 'tabindex': '2'}),
            'descripcion': Textarea(attrs={'required': 'required', 'tabindex': '3', 'cols': '1', 'rows': '1'}),
            'predefinido': Checkbox(attrs={'tabindex': '8'}),
        }
        labels = {
            'mueble': ('Nombre del mueble asociado'),
            'especificacion_de_mueble': ('Especificación del mueble'),
            'descripcion': ('Descripción de la especificación'),
            'ancho': ('Ancho del mueble'),
            'largo': ('Largo del mueble'),
            'alto': ('Alto del mueble'),
            'volumen_en_camion': ('Volumen en el camion del mueble'),
            'predefinido': ('¿Es predefinido del mueble?')
        }


class MueblePorAmbienteForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = MueblePorAmbiente
        fields = '__all__'
