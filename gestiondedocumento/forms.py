"""
Docstring documentación pendiente

"""

from django.forms import ModelForm
from gestiondedocumento.models import TipoDeDocumento, EstadoDeDocumento


class TipoDeDocumentoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeDocumento
        fields = '__all__'


class EstadoDeDocumentoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = EstadoDeDocumento
        fields = '__all__'
