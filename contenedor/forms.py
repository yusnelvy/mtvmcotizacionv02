"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput
from contenedor.models import Contenedor, ContenedorTipicoPorMueble


class ContenedorForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Contenedor
        fields = '__all__'
        widgets = {
            'contenedor': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'})
            }


class ContenedorTipicoPorMuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = ContenedorTipicoPorMueble
        fields = '__all__'
