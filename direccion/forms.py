"""
Docstring documentación pendiente

"""


from django.forms import ModelForm, TextInput, Select
from direccion.models import Pais, Provincia, Ciudad, \
    Barrio, Direccion, TipoDeEdificacion, Edificio, \
    TipoDeAscensor, Ascensor, TipoDeInmueble, \
    EspecificacionDeInmueble, Inmueble


class PaisForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Pais
        fields = '__all__'
        labels = {
            'pais': ('País')
        }
        widgets = {
            'pais': TextInput(attrs={'class': 'form-control'}),
            }


class ProvinciaForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    def __init__(self, *args, **kwargs):
        super(ProvinciaForm, self).__init__(*args, **kwargs)
        self.fields['pais'].empty_label = "Seleccione el país"

    class Meta:
        model = Provincia
        fields = '__all__'
        labels = {
            'provincia': ('Provincia'),
            'pais': ('País')
        }


class CiudadForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    def __init__(self, *args, **kwargs):
        super(CiudadForm, self).__init__(*args, **kwargs)
        self.fields['pais'].empty_label = "Seleccione el pais"
        self.fields['provincia'].empty_label = "Seleccione la provincia"

    class Meta:
        model = Ciudad
        fields = '__all__'
        labels = {
            'ciudad': ('Ciudad'),
            'provincia': ('Provincia'),
            'pais': ('País')
        }
        widgets = {
            'ciudad': TextInput(attrs={'class': 'form-control'}),
            'provincia': TextInput(attrs={'class': 'form-control'}),
            'pais': TextInput(attrs={'class': 'form-control'})
        }

class BarrioForm(ModelForm):
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
            'barrio': ('Barrio'),
            'ciudad': ('Ciudad'),
            'provincia': ('Provincia'),
            'pais': ('País')
        }
        widgets = {
            'barrio': TextInput(attrs={'class': 'form-control'}),
            'pais': Select(attrs={'class': 'form-control'}),
            'ciudad': Select(attrs={'class': 'form-control'}),
            'provincia': Select(attrs={'class': 'form-control'}),
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


class TipoDeEdificacionForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeEdificacion
        fields = '__all__'
        labels = {
            'tipo_de_edificacion': ('Nombre del tipo de edificación')
        }
        widgets = {
            'tipo_de_edificacion': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'})
        }

class EdificioForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Edificio
        fields = '__all__'


class TipoDeAscensorForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeAscensor
        fields = '__all__'
        widgets = {
            'tipo_de_ascensor': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'})
        }

class AscensorForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Ascensor
        fields = '__all__'


class TipoDeInmuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeInmueble
        fields = '__all__'
        labels = {
            'tipo_de_inmueble': ('Nombre del tipo de inmueble')
        }
        widgets = {
            'tipo_de_inmueble': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'})
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
