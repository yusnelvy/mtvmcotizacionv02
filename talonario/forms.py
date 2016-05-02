"""
Docstring documentación pendiente

"""
from talonario.models import TipoDeDocumentoImpreso, Talonario, \
    DocumentoDelTalonario
from base.forms import BaseFormMd, SelectMD, Select
from djangular.forms import NgModelFormMixin, NgModelForm
from django.forms.models import inlineformset_factory
from django.forms import ModelForm, TextInput, Textarea


class TipoDeDocumentoImpresoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeDocumentoImpreso
        fields = '__all__'
        widgets = {
            'tipo_de_documento_impreso': TextInput(attrs={'required': 'required', 'tabindex':'1'}),
            'descripcion': Textarea(attrs={'required': 'required', 'tabindex': '2', 'cols': '1', 'rows': '1'})
            }
        labels = {
            'tipo_de_documento_impreso': ('Nombre del tipo de mueble'),
            'descripcion': ('Descripción del tipo de mueble')
            }


class TalonarioForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Talonario
        fields = 'tipo_de_documento_impreso', \
                 'talonario', \
                 'descripcion', \
                 'prefijo', \
                 'separador', \
                 'numero_desde', \
                 'numero_hasta', \
                 'separado_sufijo', \
                 'numeracion_correlativa', \
                 'numero_de_documento', \
                 'cantidad_fija'
        labels = {
            'talonario': ('Nombre del talonario'),
            'descripcion': ('Descripción del talonario'),
            'cantidad_fija': ('Cantidad fija del talonario')
        }
        widgets = {
            'tipo_de_documento_impreso': Select(attrs={'tabindex': '1'}),
            'descripcion': Textarea(attrs={'required': 'required', 'tabindex': '2', 'cols': '1', 'rows': '1'})
            }


class DocumentoDelTalonarioForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = DocumentoDelTalonario
        fields = '__all__'
        labels = {
            'talonario': ('Nombre del talonario'),
            'numero': ('Numero del talonario'),
            'estado': ('Estado del talonario'),
            'informacion_de_proceso': ('Información de proceso del talonario'),
            'informacion_de_beneficiari': ('Información de beneficiara del talonario'),
            'numero_final': ('Numero final del talonario')
        }
        widgets = {
            'talonario': Select(attrs={'tabindex': '1'})
            }
