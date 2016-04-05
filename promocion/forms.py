"""
Docstring documentación pendiente

"""
from promocion.models import Medio, MedioEspecifico, \
    TipoDeReferido, Alianza, Institucion, PersonaAliado, \
    FuenteDePromocion
from base.forms import BaseFormMd, SelectMD, selectSearchMD
from djangular.forms import NgModelFormMixin, NgModelForm
from django.forms import ModelForm, TextInput


class MedioForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Medio
        fields = '__all__'
        labels = {
            'medio': ('Nombre del medio'),
            'descripcion': ('Descripción del medio')
        }


class MedioEspecificoForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = MedioEspecifico
        fields = '__all__'
        widgets = {
            'medio': selectSearchMD(attrs={'tabindex': '1'})
        }
        labels = {
            'medio': ('Nombre del medio'),
            'descripcion': ('Descripción del medio especifico'),
            'medio_especifico': ('Nombre del medio especifico')
        }


class TipoDeReferidoForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeReferido
        fields = '__all__'
        widgets = {
            'medio_especifico': selectSearchMD(attrs={'tabindex': '1'})
        }
        labels = {
            'tipo_de_referido': ('Nombre del tipo de referido'),
            'descripcion': ('Descripción del medio especifico'),
            'medio_especifico': ('Nombre del medio especifico')
        }


class AlianzaForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Alianza
        fields = '__all__'
        widgets = {
            'medio_especifico': selectSearchMD(attrs={'tabindex': '1'}),
            'fecha_vigencia': TextInput(attrs={'type': 'date'})
        }
        labels = {
            'porcentaje_comision': ('Porcentaje de la comisión de la alianza'),
            'alianza': ('Nombre de la alianza'),
            'observacion': ('Observación de la alianza'),
            'fecha_vigencia': ('Fecha de vigencia de la alianza'),
            'medio_especifico': ('Nombre del medio especifico de la alianza')
        }


class InstitucionForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Institucion
        fields = '__all__'
        widgets = {
            'alianza': selectSearchMD(attrs={'tabindex': '1'})
        }
        labels = {
            'nombre': ('Nombre de la institución'),
            'cuit': ('Cuit de la institución'),
            'pagina_web': ('Pagina web de la institución'),
            'persona_contacto': ('Persona de contacto de la institución'),
            'telefono': ('Teléfono de la institución'),
            'telefono_movil': ('Teléfono móvil de la institución'),
            'email': ('Correo de la institución'),
            'alianza': ('Nombre de la alianza asociada')
        }


class PersonaAliadoForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = PersonaAliado
        fields = '__all__'
        widgets = {
            'institucion': selectSearchMD(attrs={'tabindex': '1'})
        }
        labels = {
            'nombre': ('Nombre de la persona aliada'),
            'dni': ('DNI de la persona aliada'),
            'telefono_movil_1': ('Teléfono móvil 1 de la persona aliada'),
            'telefono_movil_2': ('Teléfono móvil 2 de la persona aliada'),
            'telefono': ('Teléfono de la persona aliada'),
            'email_principal': ('Correo principal de la persona aliada'),
            'email_secundario': ('Correo secundario de la persona aliada'),
            'observacion': ('Observación de la persona aliada'),
            'institucion': ('Nombre de la institución')
        }


class FuenteDePromocionForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = FuenteDePromocion
        fields = '__all__'
