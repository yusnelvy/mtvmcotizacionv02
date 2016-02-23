"""
Docstring documentación pendiente

"""
from vehiculo.models import Vehiculo, DetalleDeVehiculo, ChoferAsignado
from base.forms import BaseFormMd
from djangular.forms import NgModelFormMixin, NgModelForm


class VehiculoForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """

    Docstring documentación pendiente
    """
    class Meta:
        model = Vehiculo
        fields = '__all__'


class DetalleDeVehiculoForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """

    Docstring documentación pendiente
    """
    class Meta:
        model = DetalleDeVehiculo
        fields = '__all__'


class ChoferAsignadoForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """

    Docstring documentación pendiente
    """
    class Meta:
        model = ChoferAsignado
        fields = '__all__'
