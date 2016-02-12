"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput
from complejidadriesgo.models import ComplejidadRiesgo, NivelComplejidadRiesgo


class ComplejidadRiesgoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = ComplejidadRiesgo
        fields = '__all__'


class NivelComplejidadRiesgoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = NivelComplejidadRiesgo
        fields = '__all__'
