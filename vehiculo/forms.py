"""
Docstring documentación pendiente

"""
from vehiculo.models import Vehiculo, DetalleDeVehiculo, ChoferAsignado
from base.forms import BaseFormMd
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd, SelectMD, Checkbox


class VehiculoForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """

    Docstring documentación pendiente
    """
    class Meta:
        model = Vehiculo
        fields = '__all__'
        labels = {
            'marca': ('Marca del vehículo'),
            'modelo': ('Modelo del vehículo'),
            'transmision': ('Transmisión del vehículo'),
            'motor': ('Motor del vehículo'),
            'volumen_total_carga': ('Volumen de carga del vehículo'),
            'peso_total_carga': ('Peso de carga del vehículo')
        }


class DetalleDeVehiculoForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """

    Docstring documentación pendiente
    """
    class Meta:
        model = DetalleDeVehiculo
        fields = '__all__'
        widgets = {
            'vehiculo': SelectMD(attrs={'required': 'required', 'tabindex': '1'})
            }
        labels = {
            'vehiculo': ('Nombre del vehículo'),
            'numero_de_camion': ('Numero del vehículo'),
            'ancho': ('Ancho del vehículo'),
            'largo': ('Largo del vehículo'),
            'alto': ('Alto del vehículo'),
            'ancho_aux': ('Ancho auxiliar del vehículo'),
            'largo_aux': ('Largo auxiliar del vehículo'),
            'alto_aux': ('Alto auxiliar del vehículo'),
            'observacion': ('Observación del vehículo'),
            'tara_vehiculo': ('Peso tara del vehículo')
        }


class ChoferAsignadoForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """

    Docstring documentación pendiente
    """
    class Meta:
        model = ChoferAsignado
        fields = '__all__'
