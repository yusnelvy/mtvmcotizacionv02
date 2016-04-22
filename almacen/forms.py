"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput
from almacen.models import Unidad
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd


class UnidadForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Unidad
        fields = '__all__'
