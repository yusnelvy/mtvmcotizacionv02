"""
Docstring documentación pendiente

"""
from servicio.models import Servicio, ComplejidadServicio, \
    PrecioDeServicio, HerramientasPorServicio
from base.forms import BaseFormMd, SelectMD
from djangular.forms import NgModelFormMixin, NgModelForm
from django.forms.models import inlineformset_factory
from django.forms import ModelForm, TextInput


class ServicioForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Servicio
        fields = 'unidad_de_venta', 'servicio', 'descripcion'
        labels = {
            'servicio': ('Nombre del servicio'),
            'descripcion': ('Descripción del ambiente')
        }
        widgets = {
            'servicio': TextInput(attrs={'required': 'required'}),
            'descripcion': TextInput(attrs={'required': 'required'}),
            'unidad_de_venta': SelectMD(attrs={'required': 'required', 'tabindex': '1'})
        }


class ComplejidadServicioForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = ComplejidadServicio
        fields = '__all__'


class PrecioDeServicioForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = PrecioDeServicio
        fields = '__all__'


class HerramientasPorServicioForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = HerramientasPorServicio
        fields = '__all__'
