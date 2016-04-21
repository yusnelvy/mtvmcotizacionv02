"""
Docstring documentación pendiente

"""
from material.models import Material, TipoDeMaterial, \
    PrecioDeMaterial, MaterialesPorServicio
from base.forms import BaseFormMd
from djangular.forms import NgModelFormMixin, NgModelForm
from django.forms.models import inlineformset_factory
from base.forms import BaseFormMd, SelectMD, Checkbox
from django.forms import ModelForm, TextInput

class MaterialForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Material
        fields = 'tipo_de_material', 'unidad_de_consumo', 'unidad_de_venta', 'material', 'descripcion', 'relacion_consumo_venta', 'ancho', 'largo', 'alto', 'peso_unidad_consumo_kg', 'cotizable'
        labels = {
            'tipo_de_material': ('Nombre del tipo de material'),
            'descripcion': ('Descripción del material'),
            'unidad_de_consumo': ('Unidad de consumo del material'),
            'unidad_de_venta': ('Unidad de venta del material'),
            'material': ('Nombre del material'),
            'relacion_consumo_venta': ('Relación de consumo del material'),
            'ancho': ('Ancho del material (cm)'),
            'largo': ('Largo del material (cm)'),
            'alto': ('Alto del material (cm)'),
            'peso_unidad_consumo_kg': ('Peso de consumo del material (Kg)'),
            'cotizable': ('¿El material es cotizable?')
        }
        widgets = {
            'descripcion': TextInput()
            }


class TipoDeMaterialForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeMaterial
        fields = '__all__'
        labels = {
            'tipo_de_material': ('Nombre del tipo de material'),
            'descripcion': ('Descripción del tipo de material')
        }


class PrecioDeMaterialForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = PrecioDeMaterial
        fields = '__all__'


class MaterialesPorServicioForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = MaterialesPorServicio
        fields = '__all__'
