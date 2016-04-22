"""
Docstring documentación pendiente

"""
from django import forms
from cotizacionweb.models import TipoDireccion, ConceptoDeCotizacion, \
    FechaDeCotizacion, CotizacionBitacora
from cotizador.models import Cotizador
from djangular.forms import NgModelFormMixin, NgModelForm, NgForm
from base.forms import BaseFormMd


class CotizacionForm(forms.Form):
    cotizador_choices = [(cotizador.id, cotizador.id_trabajador) for cotizador in Cotizador.objects.all()]

    fecha_mudanza = forms.DateTimeField()
    fecha_visita = forms.DateTimeField()
    cotizador = forms.ChoiceField(label='Cotizador',
                                  choices=cotizador_choices)


class TipoDireccionForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDireccion
        fields = '__all__'


class ConceptoDeCotizacionForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = ConceptoDeCotizacion
        fields = '__all__'


class FechaDeCotizacionForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = FechaDeCotizacion
        fields = '__all__'


class CotizacionBitacoraForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = CotizacionBitacora
        fields = '__all__'
