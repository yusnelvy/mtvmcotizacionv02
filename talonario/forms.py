"""
Docstring documentación pendiente

"""
from talonario.models import TipoDeDocumentoImpreso, Talonario, \
    DocumentoDelTalonario
from base.forms import BaseFormMd
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
        fields = '__all__'


class DocumentoDelTalonarioForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = DocumentoDelTalonario
        fields = '__all__'
