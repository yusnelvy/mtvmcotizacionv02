"""
Docstring documentación pendiente

"""

from django.forms import ModelForm
from cliente.models import Sexo, EstadoCivil, TipoDeCliente, \
    TipoDeContacto, TipoDeInformacionDeContacto


class SexoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Sexo
        fields = '__all__'


class EstadoCivilForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = EstadoCivil
        fields = '__all__'
        labels = {
            'estado_civil': ('Nombre del Estado civil')
        }


class TipoDeClienteForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeCliente
        fields = '__all__'


class TipoDeContactoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeContacto
        fields = '__all__'


class TipoDeInformacionDeContactoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeInformacionDeContacto
        fields = '__all__'
