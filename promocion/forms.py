"""
Docstring documentación pendiente

"""
from promocion.models import Medio, MedioEspecifico, \
    TipoDeReferido, Alianza, Institucion, PersonaAliado, \
    FuenteDePromocion
from base.forms import BaseFormMd, SelectMD, selectSearchMD, Select
from djangular.forms import NgModelFormMixin, NgModelForm
from django.forms import ModelForm, TextInput, Textarea, Select


class MedioForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Medio
        fields = '__all__'
        widgets = {
            'medio': TextInput(attrs={'required': 'required', 'tabindex':'1'}),
            'descripcion': Textarea(attrs={'required': 'required', 'tabindex': '2', 'cols': '1', 'rows': '1'}),
            }
        labels = {
            'medio': ('Nombre del medio'),
            'descripcion': ('Descripción del medio')
        }


class MedioEspecificoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    def __init__(self, *args, **kwargs):
        super(MedioEspecificoForm, self).__init__(*args, **kwargs)
        self.fields['medio'].empty_label = "Seleccione el medio"

    class Meta:
        model = MedioEspecifico
        fields = '__all__'
        widgets = {
            'medio': Select(attrs={'required': 'required', 'tabindex': '1'}),
            'medio_especifico': TextInput(attrs={'required': 'required', 'tabindex': '2'}),
            'descripcion': Textarea(attrs={'required': 'required', 'tabindex': '3', 'cols': '1', 'rows': '1'}),
        }
        labels = {
            'medio': ('Nombre del medio'),
            'descripcion': ('Descripción del medio especifico'),
            'medio_especifico': ('Nombre del medio especifico')
        }


class TipoDeReferidoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    def __init__(self, *args, **kwargs):
        super(TipoDeReferidoForm, self).__init__(*args, **kwargs)
        self.fields['medio_especifico'].empty_label = "Seleccione el medio especifico"

    class Meta:
        model = TipoDeReferido
        fields = '__all__'
        widgets = {
            'medio_especifico': Select(attrs={'required': 'required', 'tabindex': '1'}),
            'tipo_de_referido': TextInput(attrs={'required': 'required', 'tabindex': '2'}),
            'descripcion': Textarea(attrs={'required': 'required', 'tabindex': '3', 'cols': '1', 'rows': '1'}),
        }
        labels = {
            'tipo_de_referido': ('Nombre del tipo de referido'),
            'descripcion': ('Descripción del tipo de referido'),
            'medio_especifico': ('Nombre del medio especifico')
        }


class AlianzaForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Alianza
        fields = '__all__'
        widgets = {
            'medio_especifico': Select(attrs={'tabindex': '1'}),
            'alianza': TextInput(attrs={'required': 'required', 'tabindex': '2'}),
            'observacion': Textarea(attrs={'required': 'required', 'tabindex': '3', 'cols': '1', 'rows': '1'}),
            'fecha_vigencia': TextInput(attrs={'type': 'date'})
        }
        labels = {
            'porcentaje_comision': ('Porcentaje de la comisión de la alianza'),
            'alianza': ('Nombre de la alianza'),
            'observacion': ('Observación de la alianza'),
            'fecha_vigencia': ('Fecha de vigencia de la alianza'),
            'medio_especifico': ('Nombre del medio especifico de la alianza')
        }


class InstitucionForm(ModelForm):
    """
    Docstring documentación pendiente
    """

    def __init__(self, *args, **kwargs):
        super(InstitucionForm, self).__init__(*args, **kwargs)
        self.fields['alianza'].empty_label = "Seleccione una alianza"

    class Meta:
        model = Institucion
        fields = '__all__'
        widgets = {
            'alianza': Select(attrs={'tabindex': '1'}),
            'nombre': TextInput(attrs={'required': 'required', 'tabindex': '2'}),
            'pagina_web': Textarea(attrs={'required': 'required', 'tabindex': '3', 'cols': '1', 'rows': '1'}),
            'email': Textarea(attrs={'required': 'required', 'tabindex': '4', 'cols': '1', 'rows': '1'}),
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


class PersonaAliadoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    def __init__(self, *args, **kwargs):
        super(PersonaAliadoForm, self).__init__(*args, **kwargs)
        self.fields['institucion'].empty_label = "Seleccione una institucion"

    class Meta:
        model = PersonaAliado
        fields = '__all__'
        widgets = {
            'institucion': Select(attrs={'tabindex': '1'}),
            'nombre': TextInput(attrs={'required': 'required', 'tabindex': '2'}),
            'observacion': Textarea(attrs={'required': 'required', 'tabindex': '3', 'cols': '1', 'rows': '1'}),
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
