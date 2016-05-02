"""
Docstring documentación pendiente

"""
from vehiculo.models import Vehiculo, DetalleDeVehiculo, ChoferAsignado
from base.forms import BaseFormMd
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd, SelectMD, Checkbox
from django.forms import ModelForm, TextInput, Textarea, Select


class VehiculoForm(ModelForm):
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


class DetalleDeVehiculoForm(ModelForm):
    """

    Docstring documentación pendiente
    """
    class Meta:
        model = DetalleDeVehiculo
        fields = '__all__'
        widgets = {
            'vehiculo': Select(attrs={'required': 'required', 'tabindex': '1'}),
            'observacion': Textarea(attrs={'tabindex': '10', 'cols': '1', 'rows': '1'})
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
