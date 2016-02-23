"""
Docstring documentación pendiente

"""

from herramienta.models import Herramienta, DotacionBasicaDeCamion
from base.forms import BaseFormMd
from djangular.forms import NgModelFormMixin, NgModelForm


class HerramientaForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Herramienta
        fields = '__all__'


class DotacionBasicaDeCamionForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = DotacionBasicaDeCamion
        fields = '__all__'
