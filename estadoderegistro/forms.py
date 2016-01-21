"""
Docstring documentación pendiente

"""

from django.forms import ModelForm
from estadoderegistro.models import Estado, TipoDeRegistro, \
    EstadoDeRegistro


class EstadoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Estado
        fields = '__all__'


class TipoDeRegistroForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeRegistro
        fields = '__all__'


class EstadoDeRegistroForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = EstadoDeRegistro
        fields = '__all__'
