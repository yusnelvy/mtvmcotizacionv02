"""
Docstring documentación pendiente

"""

from herramienta.models import Herramienta, DotacionBasicaDeCamion
from base.forms import BaseFormMd, SelectMD
from djangular.forms import NgModelFormMixin, NgModelForm


class HerramientaForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Herramienta
        fields = 'unidad', 'herramienta', 'descripcion', 'volumen_en_camion', 'peso_kg'
        widgets = {
            'unidad': SelectMD(attrs={'tabindex': '1'})
            }
        labels = {
            'unidad': ('Unidad de la herramienta'),
            'herramienta': ('Nombre de la herramienta'),
            'descripcion': ('Descripción de la herramienta'),
            'volumen_en_camion': ('Volumen de la herramienta en el camion'),
            'peso_kg': ('Peso de la herramienta')
        }


class DotacionBasicaDeCamionForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = DotacionBasicaDeCamion
        fields = '__all__'
