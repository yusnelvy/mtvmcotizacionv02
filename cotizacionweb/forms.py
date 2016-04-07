"""
Docstring documentación pendiente

"""
from django import forms
from djangular.forms import NgForm
from cotizador.models import Cotizador


class CotizacionForm(forms.Form):
    cotizador_choices = [(cotizador.id, cotizador.id_trabajador) for cotizador in Cotizador.objects.all()]

    fecha_mudanza = forms.DateField()
    hora_mudanza = forms.TimeField()
    fecha_visita = forms.DateField()
    hora_visita = forms.TimeField()
    cotizador = forms.ChoiceField(label='Cotizador',
                                  choices=cotizador_choices)
