"""
Docstring documentación pendiente

"""
from servicio.models import Servicio, ComplejidadServicio, \
    PrecioDeServicio, HerramientasPorServicio
from base.forms import BaseFormMd
from djangular.forms import NgModelFormMixin, NgModelForm
from django.forms.models import inlineformset_factory


class ServicioForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Servicio
        fields = '__all__'


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
