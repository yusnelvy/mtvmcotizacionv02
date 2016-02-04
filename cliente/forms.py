"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput
from cliente.models import Sexo, EstadoCivil, TipoDeCliente, \
    TipoDeRelacion, TipoDeInformacionDeContacto, Cliente, \
    Contacto, InformacionDeContacto, ClienteDireccion, \
    ClienteEstadoDeRegistro


class SexoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Sexo
        fields = '__all__'
        widgets = {
            'sexo': TextInput(attrs={'class': 'form-control'}),
            }


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


class TipoDeRelacionForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeRelacion
        fields = '__all__'
        widgets = {
            'tipo_de_relacion': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'})
            }


class TipoDeInformacionDeContactoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeInformacionDeContacto
        fields = '__all__'
        widgets = {
            'tipo_de_informacion_de_contacto': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'})
            }


class ClienteForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Cliente
        fields = '__all__'


class ContactoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Contacto
        fields = '__all__'


class InformacionDeContactoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = InformacionDeContacto
        fields = '__all__'


class ClienteDireccionForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = ClienteDireccion
        fields = '__all__'


class ClienteEstadoDeRegistroForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = ClienteEstadoDeRegistro
        fields = '__all__'
