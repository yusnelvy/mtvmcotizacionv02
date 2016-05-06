"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput, Select, Textarea
from estadoderegistro.models import Estado, EstadoDeRegistro
from django.contrib.contenttypes.models import ContentType
from django import forms
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd, SelectMD


class EstadoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Estado
        fields = '__all__'
        widgets = {
            'estado': TextInput(attrs={'required': 'required', 'tabindex':'1'}),
            'descripcion': Textarea(attrs={'tabindex': '2', 'cols': '1', 'rows': '1'})
            }
        labels = {
            'descripcion': ('Descripción del estado'),
            'estado': ('Nombre del estado')
            }


class EstadoDeRegistroForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    model_choices = [(content.model, content.model) for content in ContentType.objects.all()]
    model = forms.ChoiceField(
        widget=Select(attrs={'required': 'required'}),
        label='Seleccione el model',
        choices=model_choices)

    def __init__(self, *args, **kwargs):
        super(EstadoDeRegistroForm, self).__init__(*args, **kwargs)
        self.fields['estado'].empty_label = "Seleccione el estado"

    class Meta:
        model = EstadoDeRegistro
        fields = '__all__'
        widgets = {
            'estado': Select(attrs={'required': 'required', 'tabindex': '1'}),
            'descripcion': Textarea(attrs={'tabindex': '2', 'cols': '1', 'rows': '1'}),
            'observacion': Textarea(attrs={'tabindex': '3', 'cols': '1', 'rows': '1'}),
            }
        labels = {
            'estado': ('Estado asociado'),
            'descripcion': ('Descripción del estado de registro'),
            'observacion': ('Observación del estado de registro')
            }
