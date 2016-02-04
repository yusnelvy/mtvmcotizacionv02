"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput, Select
from estadoderegistro.models import Estado, EstadoDeRegistro
from django.contrib.contenttypes.models import ContentType
from django import forms


class EstadoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Estado
        fields = '__all__'
        widgets = {
            'estado': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            }


class EstadoDeRegistroForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    model_choices = [(content.model, content.model) for content in ContentType.objects.all()]
    model = forms.ChoiceField(
        widget=Select(attrs={'class': 'form-control'}),
        label='Model',
        choices=model_choices)

    class Meta:
        model = EstadoDeRegistro
        fields = '__all__'
        widgets = {
            'estado': Select(attrs={'class': 'form-control'}),
            'orden': TextInput(attrs={'class': 'form-control', 'type': 'number', 'step': '1.00'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            'observacion': TextInput(attrs={'class': 'form-control'}),
            }
