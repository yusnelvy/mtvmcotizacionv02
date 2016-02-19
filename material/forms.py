"""
Docstring documentación pendiente

"""
from material.models import Material, TipoDeMaterial, \
    PrecioDeMaterial, MaterialesPorServicio
from base.forms import BaseFormMd
from djangular.forms import NgModelFormMixin, NgModelForm
from django.forms.models import inlineformset_factory


class MaterialForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Material
        fields = '__all__'


class TipoDeMaterialForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeMaterial
        fields = '__all__'


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
