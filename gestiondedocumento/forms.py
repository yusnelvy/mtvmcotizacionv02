"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput, Textarea, Select
from gestiondedocumento.models import TipoDeDocumento, EstadoDeDocumento
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd, SelectMD, Checkbox


class TipoDeDocumentoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeDocumento
        fields = '__all__'
        widgets = {
            'tipo_de_documento': TextInput(attrs={'required': 'required', 'tabindex':'1'}),
            'descripcion': Textarea(attrs={'required': 'required', 'tabindex': '2', 'cols': '1', 'rows': '1'}),
            }
        labels = {
            'tipo_de_documento': ('Nombre del tipo de documento'),
            'descripcion': ('Descripción del tipo de documento')
        }


class EstadoDeDocumentoForm(ModelForm):
    """
    Docstring documentación pendiente
    """

    def __init__(self, *args, **kwargs):
        super(EstadoDeDocumentoForm, self).__init__(*args, **kwargs)
        self.fields['tipo_de_documento'].empty_label = "Seleccione el tipo de documento"

    class Meta:
        model = EstadoDeDocumento
        fields = '__all__'
        widgets = {
            'tipo_de_documento': Select(attrs={'required': 'required', 'tabindex': '1'}),
            'estado_de_documento': TextInput(attrs={'required': 'required', 'tabindex':'2'}),
            'descripcion': Textarea(attrs={'required': 'required', 'tabindex': '3', 'cols': '1', 'rows': '1'}),
            'observacion': Textarea(attrs={'required': 'required', 'tabindex': '5', 'cols': '1', 'rows': '1'}),
            }
        labels = {
            'tipo_de_documento': ('Seleccione un tipo de documento'),
            'estado_de_documento': ('Nombre del estado del documento'),
            'descripcion': ('Descripción del estado de documento'),
            'orden': ('Orden del estado de documento'),
            'observacion': ('Observación del estado de documento')
        }
