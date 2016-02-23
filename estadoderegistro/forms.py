"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput, Select
from estadoderegistro.models import Estado, EstadoDeRegistro
from django.contrib.contenttypes.models import ContentType
from django import forms
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd, SelectMD


class EstadoForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Estado
        fields = '__all__'
        widgets = {
            'estado': TextInput(attrs={'required': 'required'}),
            'descripcion': TextInput(attrs={'required': 'required'}),
            }


class EstadoDeRegistroForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    model_choices = [(content.model, content.model) for content in ContentType.objects.all()]
    model = forms.ChoiceField(
        widget=SelectMD(attrs={'required': 'required'}),
        label='Seleccione el model',
        choices=model_choices)

    class Meta:
        model = EstadoDeRegistro
        fields = '__all__'
        widgets = {
            'estado': SelectMD(attrs={'required': 'required'}),
            'descripcion': TextInput(attrs={'required': 'required'}),
            'observacion': TextInput(),
            }
        labels = {
            'estado': ('Seleccione el estado'),
            'descripcion': ('descripción del estado de registro'),
            'observacion': ('Observación del estado de registro')
        }
