"""
Docstring documentación pendiente

"""
from trabajador.models import Trabajador, CargoTrabajador
from base.forms import BaseFormMd
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd, SelectMD, Checkbox


class TrabajadorForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Trabajador
        fields = 'cargo_trabajador', 'dni', 'nombre', 'apellido', 'direccion', 'telefono', 'email', 'volumen_en_camion'
        widgets = {
            'cargo_trabajador': SelectMD(attrs={'tabindex': '1'})
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


class CargoTrabajadorForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = CargoTrabajador
        fields = 'cargo_padre', 'cargo_trabajador', 'descripcion'
        widgets = {
            'cargo_padre': SelectMD(attrs={'tabindex': '1'})
            }
        labels = {
            'cargo_padre': ('Nombre del cargo padre'),
            'cargo_trabajador': ('Nombre del cargo del trabajador'),
            'descripcion': ('Descripción del cargo del trabajador')
        }
