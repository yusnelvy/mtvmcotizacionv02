"""
Docstring documentación pendiente

"""
from trabajador.models import Trabajador, CargoTrabajador
from base.forms import BaseFormMd
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd, SelectMD, Checkbox, Select
from django.forms import ModelForm, TextInput, Textarea


class TrabajadorForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Trabajador
        fields = 'cargo_trabajador', 'dni', 'nombre', 'apellido', 'direccion', 'telefono', 'email', 'volumen_en_camion'
        widgets = {
            'dni': TextInput(attrs={'required': 'required', 'tabindex':'2'}),
            'nombre': Textarea(attrs={'required': 'required', 'tabindex': '3', 'cols': '1', 'rows': '1'}),
            'apellido': Textarea(attrs={'required': 'required', 'tabindex': '4', 'cols': '1', 'rows': '1'}),
            'direccion': Textarea(attrs={'required': 'required', 'tabindex': '5', 'cols': '1', 'rows': '1'}),
            'cargo_trabajador': Select(attrs={'tabindex': '1'})
            }
        labels = {
            'cargo_trabajador': ('Nombre del cargo del trabajador'),
            'dni': ('DNI del trabajador'),
            'nombre': ('Nombre del trabajador'),
            'apellido': ('Apellido del trabajador'),
            'direccion': ('Dirección del trabajador'),
            'telefono': ('Teléfono del trabajador'),
            'email': ('Correo del trabajador'),
            'volumen_en_camion': ('Volumen del trabajador en el camión')
        }


class CargoTrabajadorForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = CargoTrabajador
        fields = 'cargo_padre', 'cargo_trabajador', 'descripcion'
        widgets = {
            'cargo_trabajador': TextInput(attrs={'required': 'required', 'tabindex':'1'}),
            'descripcion': Textarea(attrs={'required': 'required', 'tabindex': '2', 'cols': '1', 'rows': '1'}),
            'cargo_padre': Select(attrs={'tabindex': '3'})
            }
        labels = {
            'cargo_padre': ('Nombre del cargo padre'),
            'cargo_trabajador': ('Nombre del cargo del trabajador'),
            'descripcion': ('Descripción del cargo del trabajador')
        }
