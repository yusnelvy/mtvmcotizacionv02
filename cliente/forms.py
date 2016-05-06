"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput, RadioSelect, Textarea
from cliente.models import Sexo, EstadoCivil, TipoDeCliente, \
    TipoDeRelacion, TipoDeInformacionDeContacto, Cliente, \
    Contacto, InformacionDeContacto, ClienteDireccion, \
    ClienteEstadoDeRegistro
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd, SelectMD, Checkbox, InputFecha
from django import forms
from django.forms.models import inlineformset_factory


class SexoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Sexo
        fields = '__all__'
        widgets = {
            'sexo': TextInput(attrs={'required': 'required', 'tabindex': '1'})
            }
        labels = {
            'sexo': ('Nombre del sexo')
        }


class EstadoCivilForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = EstadoCivil
        fields = '__all__'
        widgets = {
            'estado_civil': TextInput(attrs={'required': 'required', 'tabindex': '1'})
            }
        labels = {
            'estado_civil': ('Nombre del estado civil')
        }


class TipoDeClienteForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeCliente
        fields = '__all__'
        widgets = {
            'tipo_de_cliente': TextInput(attrs={'required': 'required', 'tabindex': '1'}),
            'descripcion': Textarea(attrs={'required': 'required', 'tabindex': '2', 'cols': '1', 'rows': '1'}),
            }
        labels = {
            'tipo_de_cliente': ('Nombre del tipo de cliente'),
            'descripcion': ('Descripción del tipo de cliente')
        }


class TipoDeRelacionForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeRelacion
        fields = '__all__'
        widgets = {
            'tipo_de_relacion': TextInput(attrs={'required': 'required', 'tabindex': '1'}),
            'descripcion': Textarea(attrs={'required': 'required', 'tabindex': '2', 'cols': '1', 'rows': '1'}),
            }
        labels = {
            'tipo_de_relacion': ('Nombre del tipo de relación'),
            'descripcion': ('Descripción del tipo de relación')
        }


class TipoDeInformacionDeContactoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeInformacionDeContacto
        fields = '__all__'
        widgets = {
            'tipo_de_informacion_de_contacto': TextInput(attrs={'required': 'required', 'tabindex': '1'}),
            'descripcion': Textarea(attrs={'required': 'required', 'tabindex': '2', 'cols': '1', 'rows': '1'}),
            }
        labels = {
            'tipo_de_informacion_de_contacto': ('Nombre del tipo de informacion de contacto'),
            'descripcion': ('Descripción del tipo de informacion de contacto')
        }


class ClienteForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['tipo_de_cliente'].empty_label = None

    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'tipo_de_cliente': RadioSelect(attrs={'onclick': 'radioColor();'}),
            'observaciones': Textarea(attrs={'cols': '1', 'rows': '1'}),
            'cuit': TextInput(),
            'nombre': TextInput()
        }
        labels = {
            'cuit': ('Cuit de la entidad'),
            'nombre': ('Nombre del cliente'),
            'tipo_de_cliente': ('Tipo del cliente a registrar')
        }


class InformacionDeContactoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = InformacionDeContacto
        #exclude = ['tech', 'operator', ]
        fields = 'tipo_de_informacion_de_contacto', 'informacion_de_contacto'
        widgets = {
            'tipo_de_informacion_de_contacto': RadioSelect(attrs={'onclick': 'radioColor();', 'required': 'required'}),
            'informacion_de_contacto': TextInput(attrs={'required': 'required'})
        }
        labels = {
            'tipo_de_informacion_de_contacto': ('Seleccione el tipo de información de contacto:')
        }

    def __init__(self, *args, **kwargs):
        super(InformacionDeContactoForm, self).__init__(*args, **kwargs)
        self.fields['tipo_de_informacion_de_contacto'].empty_label = None


class ContactoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    def __init__(self, *args, **kwargs):
        super(ContactoForm, self).__init__(*args, **kwargs)
        self.fields['sexo'].empty_label = None
        self.fields['estado_civil'].empty_label = None

    class Meta:
        model = Contacto
        fields = '__all__'
        widgets = {
            'sexo': RadioSelect(attrs={'onclick': 'radioColor();', 'required': 'required'}),
            'estado_civil': RadioSelect(attrs={'onclick': 'radioColor();'}),
            'fecha_nacimiento': TextInput(attrs={'required': 'required'}),
            'observaciones': Textarea(attrs={'cols': '1', 'rows': '1'}),
            'dni': TextInput(attrs={'required': 'required'})
        }
        labels = {
            'dni': ('DNI del cliente'),
            'nombre': ('Nombre del cliente'),
            'sexo': ('Sexo del cliente'),
            'estado_civil': ('Estado civil del cliente'),
            'fecha_nacimiento': ('Fecha de nacimiento del cliente'),
            'tipo_de_relacion': ('Tipo de relación con el cliente')
        }

InformacionDeContactoFormSet = inlineformset_factory(Contacto,
                                                     InformacionDeContacto,
                                                     form=InformacionDeContactoForm,
                                                     extra=1)


class ClienteDireccionForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = ClienteDireccion
        fields = '__all__'
        labels = {
            'calle': ('Calle de la dirección:'),
            'altura': ('Altura de la dirección:'),
            'barrio': ('Barrio de la dirección:'),
            'ciudad': ('Ciudad de la dirección:'),
            'provincia': ('Provincia de la dirección:'),
            'pais': ('País de la dirección'),
            'codigo_postal/zip': ('Código postal / zip de la dirección'),
            'punto_de_referencia': ('Punto de referencia de la dirección')
        }


class ClienteEstadoDeRegistroForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = ClienteEstadoDeRegistro
        fields = '__all__'
