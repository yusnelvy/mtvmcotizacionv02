"""
Docstring documentación pendiente

"""
from talonario.models import TipoDeDocumentoImpreso, Talonario, \
    DocumentoDelTalonario
from base.forms import BaseFormMd, SelectMD
from djangular.forms import NgModelFormMixin, NgModelForm
from django.forms.models import inlineformset_factory


class TipoDeDocumentoImpresoForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeDocumentoImpreso
        fields = '__all__'


class TalonarioForm(NgModelFormMixin, NgModelForm, BaseFormMd):
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
            'tipo_de_documento_impreso': SelectMD(attrs={'tabindex': '1'})
            }


class DocumentoDelTalonarioForm(NgModelFormMixin, NgModelForm, BaseFormMd):
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
            'talonario': SelectMD(attrs={'tabindex': '1'})
            }
