"""
Docstring documentación pendiente

"""
from trabajador.models import Trabajador, CargoTrabajador
from base.forms import BaseFormMd
from djangular.forms import NgModelFormMixin, NgModelForm


class TrabajadorForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Trabajador
        fields = '__all__'


class CargoTrabajadorForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = CargoTrabajador
        fields = '__all__'
