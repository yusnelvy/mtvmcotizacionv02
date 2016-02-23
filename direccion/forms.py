"""
Docstring documentación pendiente

"""


from django.forms import ModelForm, TextInput
from direccion.models import Pais, Provincia, Ciudad, \
    Barrio, Direccion, TipoDeEdificacion, Edificacion, \
    TipoDeAscensor, Ascensor, TipoDeInmueble, \
    EspecificacionDeInmueble, Inmueble
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd, SelectMD, Checkbox


class PaisForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Pais
        fields = '__all__'
        labels = {
            'pais': ('Nombre del país')
        }
        widgets = {
            'pais': TextInput(attrs={'required': 'required'}),
            'codigo_telefonico': TextInput(attrs={'type': 'number','required': 'required'})
            }


class ProvinciaForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    def __init__(self, *args, **kwargs):
        super(ProvinciaForm, self).__init__(*args, **kwargs)
        self.fields['pais'].empty_label = "Seleccione el país"

    class Meta:
        model = Provincia
        fields = 'pais', 'provincia', 'codigo_telefonico'
        labels = {
            'provincia': ('Nombre de provincia'),
            'pais': ('Seleccione el país')
        }
        widgets = {
            'provincia': TextInput(attrs={'required': 'required'}),
            'pais': SelectMD(attrs={'required': 'required'})
            }


class CiudadForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    def __init__(self, *args, **kwargs):
        super(CiudadForm, self).__init__(*args, **kwargs)
        self.fields['pais'].empty_label = "Seleccione el pais"
        self.fields['provincia'].empty_label = "Seleccione la provincia"

    class Meta:
        model = Ciudad
        fields = 'pais', 'provincia', 'ciudad'
        labels = {
            'ciudad': ('Nombre de la ciudad'),
            'provincia': ('Seleccione una provincia'),
            'pais': ('Seleccione un país')
        }
        widgets = {
            #'pais': SelectMD(attrs={'required': 'required'},
            #'provincia': SelectMD(attrs={'required': 'required'},
            'ciudad': TextInput(attrs={'required': 'required'}),
        }


class BarrioForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    def __init__(self, *args, **kwargs):
        super(BarrioForm, self).__init__(*args, **kwargs)
        self.fields['pais'].empty_label = "Seleccione el país"
        self.fields['provincia'].empty_label = "Seleccione la provincia"
        self.fields['ciudad'].empty_label = "Seleccione la ciudad"

    class Meta:
        model = Barrio
        fields = '__all__'
        labels = {
            'barrio': ('Nombre del barrio'),
            'ciudad': ('Ciudad'),
            'provincia': ('Provincia'),
            'pais': ('País')
        }
        widgets = {
            'barrio': TextInput(attrs={'required': 'required'})
            }


class DireccionForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Direccion
        fields = '__all__'
        labels = {
            'calle': ('Calle'),
            'altura': ('Altura'),
            'barrio': ('Barrio'),
            'ciudad': ('Ciudad'),
            'provincia': ('Provincia'),
            'pais': ('País'),
            'zip': ('Código postal / Zip'),
            'adicional': ('Información adicional'),
            'punto_referencia': ('Punto de referencia')
        }


class TipoDeEdificacionForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeEdificacion
        fields = '__all__'
        labels = {
            'tipo_de_edificacion': ('Nombre del tipo de edificación'),
            'descripcion': ('Descripción del tipo de edificación')
        }
        widgets = {
            'tipo_de_edificacion': TextInput(attrs={'required': 'required'}),
            #'descripcion': TextInput(attrs={'required': 'required'})
        }


class EdificacionForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Edificacion
        fields = '__all__'


class TipoDeAscensorForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeAscensor
        fields = '__all__'
        labels = {
            'descripcion': ('Descripción del tipo de ascensor'),
            'tipo_de_ascensor': ('Nombre del tipo de ascensor')
        }
        widgets = {
            'tipo_de_ascensor': TextInput(attrs={'required': 'required'})
        }


class AscensorForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Ascensor
        fields = '__all__'


class TipoDeInmuebleForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeInmueble
        fields = '__all__'
        labels = {
            'tipo_de_inmueble': ('Nombre del tipo de inmueble'),
            'descripcion': ('Descipción del tipo de inmueble')
        }
        widgets = {
            'tipo_de_inmueble': TextInput(attrs={'required': 'required'}),
        }


class EspecificacionDeInmuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = EspecificacionDeInmueble
        fields = '__all__'


class InmuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Inmueble
        fields = '__all__'
        labels = {
            'inmueble': ('Nombre del inmueble'),
            'especificacion_de_inmueble': ('Tipo de inmueble'),
            'nombre_del_piso': ('Nombre del piso del inmueble'),
            'numero_de_pisos': ('N° del piso del inmueble'),
            'cantidad_de_ambientes': ('N° de ambientes'),
            'numero_de_plantas': ('N° de pisos internos del inmueble'),
            'pisos_escalera': ('N° de pisos a recorrer por escaleras para llegar al inmueble')
        }
