"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput
from mueble.models import TipoDeMueble


class TipoDeMuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeMueble
        fields = '__all__'
        widgets = {
            'tipo_de_mueble': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'})
            }
