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
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            'capacidad_de_volumen': TextInput(attrs={'class': 'form-control'}),
            'capacidad_de_peso': TextInput(attrs={'class': 'form-control'}),
            'ancho': TextInput(attrs={'class': 'form-control'}),
            'largo': TextInput(attrs={'class': 'form-control'}),
            'alto': TextInput(attrs={'class': 'form-control'}),
            'volumen_en_camion': TextInput(attrs={'class': 'form-control'})
            }
