"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput
from contenedor.models import Contenedor, ContenedorTipicoPorMueble, \
    TipoDeContenido
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd, SelectMD, Checkbox


class ContenedorForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Contenedor
        fields = '__all__'
        widgets = {
            'contenedor': TextInput(attrs={'required': 'required'}),
            'descripcion': TextInput(attrs={'required': 'required'})
            }
        labels = {
            'descripcion': ('Descripción del contenedor'),
            'contenedor': ('Nombre del contenedor'),
            'capacidad_de_volumen': ('Capacidad de volumen del contenedor'),
            'capacidad_de_peso': ('Capacidad de peso del contenedor'),
            'ancho': ('Ancho del contenedor'),
            'largo': ('Largo del contenedor'),
            'alto': ('Alto del contenedor'),
            'volumen_en_camion': ('Volumen del contenedor en el camión')
            }


class ContenedorTipicoPorMuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = ContenedorTipicoPorMueble
        fields = '__all__'


class TipoDeContenidoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeContenido
        fields = '__all__'
