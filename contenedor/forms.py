"""
Docstring documentación pendiente

"""

from django.forms import ModelForm
from contenedor.models import Contenedor


class ContenedorForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Contenedor
        fields = '__all__'
