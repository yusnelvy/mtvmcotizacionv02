"""
Docstring documentación pendiente

"""
from premisas.models import Empresa, PersonalizacionVisual, \
    VarianteVisual, VarianteVisualDetalle, DatosPrecargado
from base.forms import BaseFormMd, SelectMD
from djangular.forms import NgModelFormMixin, NgModelForm
from django.forms.models import inlineformset_factory
from django.forms import ModelForm, Select, ModelChoiceField, TextInput, NumberInput, RadioSelect, Textarea
from django.contrib.contenttypes.models import ContentType
from django import forms


class EmpresaForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Empresa
        fields = '__all__'
        widgets = {
            'codigo': TextInput(attrs={'required': 'required', 'tabindex':'1'}),
            'empresa': TextInput(attrs={'required': 'required', 'tabindex': '2'}),
            'telefonos': NumberInput(attrs={'required': 'required', 'tabindex': '3'}),
            'direccion': Textarea(attrs={'tabindex': '4', 'cols': '1', 'rows': '1'}),
            'sitio_web': Textarea(attrs={'tabindex': '5', 'cols': '1', 'rows': '1'}),
            'correo': Textarea(attrs={'tabindex': '6', 'cols': '1', 'rows': '1'}),
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


class PersonalizacionVisualForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = PersonalizacionVisual
        fields = '__all__'
        widgets = {
            'usuario': Select(attrs={'required': 'required', 'tabindex': '1'}),
            'tipo': Textarea(attrs={'required': 'required', 'tabindex': '2', 'cols': '1', 'rows': '1'}),
            'valor': TextInput(attrs={'required': 'required', 'tabindex': '3'})
        }
        labels = {
            'usuario': ('Nombre del usuario'),
            'tipo': ('Tipo de personalización'),
            'valor': ('Valor de personalización')
            }


class VarianteVisualForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    model_choices = [(content.model, content.model) for content in ContentType.objects.all()]
    model = forms.ChoiceField(
        widget=Select(attrs={'ng-change': 'selectChanged()'}),
        label='Nombre del model',
        choices=model_choices)

    class Meta:
        model = VarianteVisual
        fields = 'nombre', 'model', 'usuario'
        widgets = {
            'usuario': Select(attrs={'required': 'required', 'tabindex': '1'}),
            'nombre': Textarea(attrs={'required': 'required', 'tabindex': '2', 'cols': '1', 'rows': '1'}),
            'model': TextInput(attrs={'required': 'required', 'tabindex': '3'})
        }
        labels = {
            'usuario': ('Usuario'),
            'nombre': ('Nombre de la variante'),
            'model': ('Nombre del model')
            }

VarianteVisualDetalleFormSet = inlineformset_factory(VarianteVisual,
                                                     VarianteVisualDetalle, widgets={'visibilidad': RadioSelect()} ,
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
