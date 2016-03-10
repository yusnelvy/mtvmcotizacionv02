"""
Docstring documentación pendiente

"""
from widget.models import Widget
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd
from django.forms import ModelForm, TextInput
from django import forms


class WidgetForm(ModelForm):
    """
    Docstring documentación pendiente
    """

    Desplegable_choices = (
           ('1', '1'),
           ('2', '2'),
           ('3', '3'),
       )
    desplegable = forms.ChoiceField(
           label='Desplegable',
           choices=Desplegable_choices)

    NroColumnas_choices = (
           ('1x1', '1x1'),
           ('1x2', '1x2'),
           ('2x1', '2x1'),
           ('2x2', '2x2'),
           ('1x3', '1x3'),
           ('2x3', '2x3'),
       )
    numero_de_columna = forms.ChoiceField(
           label='Numero de Columnas',
           choices=NroColumnas_choices)

    Color_choices = (
           ('Azul', 'Azul'),
           ('Rojo', 'Rojo'),
           ('Verde', 'Verde'),
       )
    color = forms.ChoiceField(
           label='Color',
           choices=Color_choices)

    class Meta:
        model = Widget
        fields = '__all__'
        labels = {
            'nombre': ('Nombre del Widget'),
            'visible': ('Visible'),
            'desplegable': ('Desplegable'),
            'numero_de_columna': ('Numero de Columnas'),
            'color': ('Color'),
            'orden': ('Orden')
        }
