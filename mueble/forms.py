"""
Docstring documentación pendiente

"""

from django.forms import ModelForm
from mueble.models import TipoDeMueble


class TipoDeMuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeMueble
        fields = '__all__'
