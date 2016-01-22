"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput
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
        widgets = {
            'estado_civil': TextInput(attrs={'class': 'form-control'})
            }


class TipoDeClienteForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeCliente
        fields = '__all__'
        widgets = {
            'tipo_de_cliente': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'})
            }


class TipoDeContactoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeContacto
        fields = '__all__'
        widgets = {
            'tipo_de_contacto': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'})
            }


class TipoDeInformacionDeContactoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeInformacionDeContacto
        fields = '__all__'
