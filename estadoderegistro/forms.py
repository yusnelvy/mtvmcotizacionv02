"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput, Select
from estadoderegistro.models import Estado, TipoDeRegistro, \
    EstadoDeRegistro


class EstadoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Estado
        fields = '__all__'
        widgets = {
            'estado': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            }


class TipoDeRegistroForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeRegistro
        fields = '__all__'
        widgets = {
            'tipo_de_registro': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            }


class EstadoDeRegistroForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = EstadoDeRegistro
        fields = '__all__'
        widgets = {
            'estado': Select(attrs={'class': 'form-control'}),
            'tipo_de_registro': Select  (attrs={'class': 'form-control'}),
            'orden': TextInput(attrs={'class': 'form-control', 'type':'number', 'step':'1.00'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            'observacion': TextInput(attrs={'class': 'form-control'}),
            }
