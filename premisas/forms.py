"""
Docstring documentación pendiente

"""
from premisas.models import Empresa, PersonalizacionVisual, \
    VarianteVisual, VarianteVisualDetalle, DatosPrecargado
from base.forms import BaseFormMd
from djangular.forms import NgModelFormMixin, NgModelForm
from django.forms.models import inlineformset_factory
from django.forms import Select, ModelChoiceField
from django.contrib.contenttypes.models import ContentType
from django import forms


class EmpresaForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Empresa
        fields = '__all__'


class PersonalizacionVisualForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = PersonalizacionVisual
        fields = '__all__'


class VarianteVisualForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    model_choices = [(content.model, content.model) for content in ContentType.objects.all()]
    model = forms.ChoiceField(
        widget=Select(attrs={'class': 'form-control'}),
        label='Model',
        choices=model_choices)

    class Meta:
        model = VarianteVisual
        fields = '__all__'

VarianteVisualDetalleFormSet = inlineformset_factory(VarianteVisual,
                                                     VarianteVisualDetalle,
                                                     fields=('campo', 'visibilidad'))


class DatosPrecargadoForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    nombreapp_choices = [(content['app_label'], content['app_label']) for content in ContentType.objects.values('app_label').distinct().order_by()]
    lista_model = ModelChoiceField(ContentType.objects, widget=Select(attrs={'class': 'form-control'}), empty_label=None, label='Model:')
    nombre_app = forms.ChoiceField(
        widget=Select(attrs={'class': 'form-control'}),
        label='Nombre de la app',
        choices=nombreapp_choices)

    dato = forms.ChoiceField(
        widget=Select(attrs={'class': 'form-control'}),
        label='Dato',
        choices=())

    class Meta:
        model = DatosPrecargado
        fields = '__all__'
