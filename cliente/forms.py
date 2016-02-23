"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput
from cliente.models import Sexo, EstadoCivil, TipoDeCliente, \
    TipoDeRelacion, TipoDeInformacionDeContacto, Cliente, \
    Contacto, InformacionDeContacto, ClienteDireccion, \
    ClienteEstadoDeRegistro
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd, SelectMD, Checkbox


class SexoForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Sexo
        fields = '__all__'
        widgets = {
            'sexo': TextInput(attrs={'required': 'required'}),
            }
        labels = {
            'sexo': ('Nombre del sexo')
        }


class EstadoCivilForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = EstadoCivil
        fields = '__all__'
        labels = {
            'estado_civil': ('Nombre del estado civil')
        }
        widgets = {
            'estado_civil': TextInput(attrs={'required': 'required'})
            }


class TipoDeClienteForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeCliente
        fields = '__all__'
        widgets = {
            'tipo_de_cliente': TextInput(attrs={'required': 'required'}),
            'descripcion': TextInput(attrs={'required': 'required'})
            }
        labels = {
            'tipo_de_cliente': ('Nombre del tipo de cliente'),
            'descripcion': ('Descripción del tipo de cliente')
        }


class TipoDeRelacionForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeRelacion
        fields = '__all__'
        widgets = {
            'tipo_de_relacion': TextInput(attrs={'required': 'required'}),
            'descripcion': TextInput(attrs={'required': 'required'})
            }
        labels = {
            'tipo_de_relacion': ('Nombre del tipo de relación'),
            'descripcion': ('Descripción del tipo de relación')
        }


class TipoDeInformacionDeContactoForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeInformacionDeContacto
        fields = '__all__'
        widgets = {
            'tipo_de_informacion_de_contacto': TextInput(attrs={'required': 'required'}),
            'descripcion': TextInput(attrs={'required': 'required'})
            }
        labels = {
            'tipo_de_informacion_de_contacto': ('Nombre del tipo de informacion de contacto'),
            'descripcion': ('Descripción del tipo de informacion de contacto')
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
