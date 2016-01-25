"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput, Select
from gestiondedocumento.models import TipoDeDocumento, EstadoDeDocumento


class TipoDeDocumentoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeDocumento
        fields = '__all__'
        widgets = {
            'tipo_de_documento': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            }


class EstadoDeDocumentoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = EstadoDeDocumento
        fields = '__all__'
        widgets = {
            'tipo_de_documento': Select(attrs={'class': 'form-control'}),
            'orden': TextInput(attrs={'class': 'form-control', 'type':'number', 'step':'1.00'}),
            'estado_de_documento': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            'observacion': TextInput(attrs={'class': 'form-control'}),
            }
