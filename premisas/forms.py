"""
Docstring documentación pendiente

"""
from premisas.models import Empresa, PersonalizacionVisual, \
    VarianteVisual, VarianteVisualDetalle, DatosPrecargado
from base.forms import BaseFormMd, SelectMD
from djangular.forms import NgModelFormMixin, NgModelForm
from django.forms.models import inlineformset_factory
from django.forms import Select, ModelChoiceField, TextInput, NumberInput
from django.contrib.contenttypes.models import ContentType
from django import forms


class EmpresaForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Empresa
        fields = '__all__'
        widgets = {
            'codigo': TextInput(attrs={'required': 'required', 'tabindex': '1'}),
            'empresa': TextInput(attrs={'required': 'required', 'tabindex': '2'}),
            'telefonos': NumberInput(attrs={'required': 'required', 'tabindex': '3'}),
            'telefono_call_center': NumberInput(attrs={'required': 'required'})
            }
        labels = {
            'codigo': ('Código de la empresa'),
            'empresa': ('Nombre de la empresa'),
            'telefonos': ('Teléfono de la empresa'),
            'direccion': ('Dirección de la empresa'),
            'sitio_web': ('Sitio web de la empresa'),
            'correo': ('Correo de la empresa'),
            'responsable': ('Responsable de la empresa'),
            'cuit': ('Cuit de la empresa'),
            'logo': ('Logo de la empresa'),
            'telefono_call_center': ('Teléfono del call center')
            }


class PersonalizacionVisualForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = PersonalizacionVisual
        fields = '__all__'
        widgets = {
            'usuario': SelectMD(attrs={'required': 'required', 'tabindex': '1'}),
        }
        labels = {
            'usuario': ('Nombre del usuario'),
            'tipo': ('Tipo de personalización'),
            'valor': ('Valor de personalización')
            }


class VarianteVisualForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    model_choices = [(content.model, content.model) for content in ContentType.objects.all()]
    model = forms.ChoiceField(
        widget=SelectMD(attrs={'ng-change': 'selectChanged()'}),
        label='Model',
        choices=model_choices)

    class Meta:
        model = VarianteVisual
        fields = '__all__'
        widgets = {
            'usuario': SelectMD()
        }

VarianteVisualDetalleFormSet = inlineformset_factory(VarianteVisual,
                                                     VarianteVisualDetalle,
                                                     fields=('campo', 'visibilidad'), extra=1)


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
