"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput
from ambiente.models import Ambiente, AmbientePorTipoDeInmueble


class AmbienteForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Ambiente
        fields = '__all__'
        widgets = {
            'ambiente': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            }


class AmbientePorTipoDeInmuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = AmbientePorTipoDeInmueble
        fields = '__all__'
