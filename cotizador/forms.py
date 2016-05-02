"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput
from cotizador.models import Cotizador
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd


class CotizadorForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Cotizador
        fields = '__all__'
