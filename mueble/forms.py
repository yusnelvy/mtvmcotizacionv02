"""
Docstring documentación pendiente

"""

from django.forms import ModelForm
from mueble.models import TipoDeMueble, Mueble, \
    EspecificacionDeMueble, MueblePorAmbiente


class TipoDeMuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeMueble
        fields = '__all__'


class MuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Mueble
        fields = '__all__'


class EspecificacionDeMuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = EspecificacionDeMueble
        fields = '__all__'


class MueblePorAmbienteForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = MueblePorAmbiente
        fields = '__all__'
