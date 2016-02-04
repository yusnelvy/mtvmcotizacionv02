"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput
from contenedor.models import Contenedor


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
