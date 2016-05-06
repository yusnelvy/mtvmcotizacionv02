"""
Docstring documentación pendiente

"""
from material.models import Material, TipoDeMaterial, \
    PrecioDeMaterial, MaterialesPorServicio
from base.forms import BaseFormMd
from djangular.forms import NgModelFormMixin, NgModelForm
from django.forms.models import inlineformset_factory
from base.forms import BaseFormMd, SelectMD, Checkbox
from django.forms import ModelForm, TextInput, Textarea, Select

class MaterialForm(ModelForm):
    """
    Docstring documentación pendiente
    """

    def __init__(self, *args, **kwargs):
        super(MaterialForm, self).__init__(*args, **kwargs)
        self.fields['tipo_de_material'].empty_label = "Seleccione el tipo de material"
        self.fields['unidad_de_consumo'].empty_label = "Seleccione la unidad de consumo"
        self.fields['unidad_de_venta'].empty_label = "Seleccione la unidad de venta"

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
            'tipo_de_material': Select(attrs={'required': 'required', 'tabindex': '1', 'ng-change': 'onChange()'}),
            'unidad_de_consumo': Select(attrs={'required': 'required', 'tabindex': '1', 'ng-change': 'onChange()'}),
            'unidad_de_venta': Select(attrs={'required': 'required', 'tabindex': '1', 'ng-change': 'onChange()'}),
            'material': TextInput(attrs={'required': 'required', 'tabindex':'2'}),
            'descripcion': Textarea(attrs={'tabindex': '3', 'cols': '1', 'rows': '1'}),
            }


class TipoDeMaterialForm(ModelForm):
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
        widgets = {
            'tipo_de_material': TextInput(attrs={'required': 'required', 'tabindex':'1'}),
            'descripcion': Textarea(attrs={'tabindex': '2', 'cols': '1', 'rows': '1'}),
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
