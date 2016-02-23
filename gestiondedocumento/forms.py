"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput, Select
from gestiondedocumento.models import TipoDeDocumento, EstadoDeDocumento
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd, SelectMD, Checkbox


class TipoDeDocumentoForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeDocumento
        fields = '__all__'
        widgets = {
            'tipo_de_documento': TextInput(attrs={'required': 'required'}),
            'descripcion': TextInput(attrs={'required': 'required'}),
            }
        labels = {
            'tipo_de_documento': ('Nombre del tipo de documento'),
            'descripcion': ('Descripción del tipo de documento')
        }


class EstadoDeDocumentoForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = EstadoDeDocumento
        fields = '__all__'
        widgets = {
            'tipo_de_documento': SelectMD(attrs={'required': 'required'}),
            'orden': TextInput(attrs={'type': 'number', 'step': '1.00'}),
            'estado_de_documento': TextInput(attrs={'required': 'required'}),
            'descripcion': TextInput(),
            'observacion': TextInput(),
            }
        labels = {
            'tipo_de_documento': ('Seleccione un tipo de documento'),
            'estado_de_documento': ('Nombre del estado del documento'),
            'descripcion': ('Descripción del estado de documento'),
            'orden': ('Orden del estado de documento'),
            'observacion': ('Observación del estado de documento')
        }
