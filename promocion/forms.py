"""
Docstring documentación pendiente

"""
from promocion.models import Medio, MedioEspecifico, \
    TipoDeReferido, Alianza, Institucion, PersonaAliado, \
    FuenteDePromocion
from base.forms import BaseFormMd
from djangular.forms import NgModelFormMixin, NgModelForm


class MedioForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Medio
        fields = '__all__'


class MedioEspecificoForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = MedioEspecifico
        fields = '__all__'


class TipoDeReferidoForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeReferido
        fields = '__all__'


class AlianzaForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Alianza
        fields = '__all__'


class InstitucionForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Institucion
        fields = '__all__'


class PersonaAliadoForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = PersonaAliado
        fields = '__all__'


class FuenteDePromocionForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = FuenteDePromocion
        fields = '__all__'
