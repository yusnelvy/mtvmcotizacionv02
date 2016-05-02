"""
Docstring documentación pendiente

"""
from servicio.models import Servicio, ComplejidadServicio, \
    PrecioDeServicio, HerramientasPorServicio
from base.forms import BaseFormMd, SelectMD, Select, Checkbox
from djangular.forms import NgModelFormMixin, NgModelForm
from django.forms.models import inlineformset_factory
from django.forms import ModelForm, TextInput, Textarea
from djangular.forms.widgets import CheckboxChoiceInput
from django.forms.widgets import CheckboxFieldRenderer


class ServicioForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Servicio
        fields = 'unidad_de_venta', 'servicio', 'descripcion'
        labels = {
            'servicio': ('Nombre del servicio'),
            'descripcion': ('Descripción del servicio')
        }
        widgets = {
            'servicio': TextInput(attrs={'required': 'required', 'tabindex':'1'}),
            'descripcion': Textarea(attrs={'required': 'required', 'tabindex': '2', 'cols': '1', 'rows': '1'}),
            'unidad_de_venta': Select(attrs={'required': 'required', 'tabindex': '3'})
        }


class ComplejidadServicioForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = ComplejidadServicio
        fields = 'servicio', 'porcentaje', 'descripcion', 'predefinido'
        labels = {
            'servicio': ('Nombre del servicio'),
            'descripcion': ('Descripción de la complejidad del servicio'),
            'porcentaje': ('Porcentaje complejidad del servicio'),
            'predefinido': ('¿La complejidad es predefinida del servicio?')
        }
        widgets = {
            'servicio': Select(attrs={'tabindex': '1'}),
            'descripcion': Textarea(attrs={'required': 'required', 'tabindex': '2', 'cols': '1', 'rows': '1'}),
            'predefinido': Checkbox()
        }


class PrecioDeServicioForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = PrecioDeServicio
        fields = '__all__'
        labels = {
            'servicio': ('Nombre del servicio'),
            'precio_base': ('Precio base del servicio'),
            'cantidad_de_gracia': ('Cantidad de gracias del servicio'),
            'user_preparador': ('Usuario preparador del servicio'),
            'user_aprobador': ('Usuario aprobador del servicio'),
            'fecha_aprobacion': ('Fecha de aprobación del servicio')
        }
        widgets = {
            'servicio': Select(attrs={'tabindex': '1'}),
            'user_preparador': Select(attrs={'tabindex': '2'}),
            'user_aprobador': Select(attrs={'tabindex': '3'})
        }


class HerramientasPorServicioForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = HerramientasPorServicio
        fields = '__all__'
