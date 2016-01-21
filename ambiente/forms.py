"""
Docstring documentación pendiente

"""

from django.forms import ModelForm
from ambiente.models import Ambiente


class AmbienteForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Ambiente
        fields = '__all__'
