"""
Docstring documentación pendiente

"""


from django.forms import ModelForm, TextInput, Select, \
    ModelChoiceField, Textarea, RadioSelect
from direccion.models import Pais, Provincia, Ciudad, \
    Barrio, Direccion, TipoDeEdificacion, Edificacion, \
    TipoDeAscensor, Ascensor, TipoDeInmueble, \
    EspecificacionDeInmueble, Inmueble, HorarioDisponible
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd, SelectMD, Checkbox, radioSelectPlus
from django.forms.models import inlineformset_factory
from django import forms


class PaisForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Pais
        fields = '__all__'
        labels = {
            'pais': ('Nombre del país'),
            'codigo_telefonico': ('Código telefónico del país')
        }
        widgets = {
            'pais': TextInput(attrs={'required': 'required', 'tabindex': '1'}),
            'codigo_telefonico': TextInput(attrs={'required': 'required', 'tabindex': '2'})
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
        fields = 'pais', 'provincia', 'codigo_telefonico'
        labels = {
            'provincia': ('Nombre de la provincia'),
            'pais': ('País asociado a la provincia'),
            'codigo_telefonico': ('Código telefónico de la provincia')
        }
        widgets = {
            'provincia': TextInput(attrs={'required': 'required'}),
            'pais': Select(attrs={'required': 'required', 'tabindex': '1', 'ng-change': 'onChange()'})
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
        fields = 'pais', 'provincia', 'ciudad'
        widgets = {
            'pais': Select(attrs={'ng-change': 'onChange()', 'tabindex': '1'}),
            'provincia': Select(attrs={'ng-change': 'onChange()', 'tabindex': '2'}),
            'ciudad': TextInput(attrs={'required': 'required', 'tabindex': '3'}),
        }
        labels = {
            'ciudad': ('Nombre de la ciudad'),
            'provincia': ('Provincia asociada a la ciudad'),
            'pais': ('País asociado a la ciudad')
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
            'barrio': ('Nombre del barrio'),
            'ciudad': ('Ciudad asociada'),
            'provincia': ('Provincia asociada'),
            'pais': ('País asociado')
        }
        widgets = {
            'barrio': TextInput(attrs={'required': 'required'}),
            'pais': Select(attrs={'ng-change': 'onChange()'}),
            'ciudad': Select(attrs={'ng-change': 'onChange()'}),
            'provincia': Select(attrs={'ng-change': 'onChange()'})
            }


class DireccionForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Direccion
        fields = '__all__'
        labels = {
            'calle': ('Calle de la dirección'),
            'altura': ('Altura de la dirección'),
            'barrio': ('Barrio de la dirección'),
            'ciudad': ('Ciudad de la dirección'),
            'provincia': ('Provincia de la dirección'),
            'pais': ('País de la dirección'),
            'zip': ('Código postal / Zip de la dirección'),
            'observacion': ('Información adicional de la dirección'),
            'punto_referencia': ('Punto de referencia de la dirección')
        }
        widgets = {
            'observacion': Textarea(attrs={'cols': '1', 'rows': '1'}),
            'punto_referencia': Textarea(attrs={'cols': '1', 'rows': '1'})
        }


class TipoDeEdificacionForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDeEdificacion
        fields = '__all__'
        labels = {
            'tipo_de_edificacion': ('Nombre del tipo de edificación'),
            'descripcion': ('Descripción del tipo de edificación'),
            'nombre': ('¿Nombre predeterminado de la edificación?')
        }
        widgets = {
            'tipo_de_edificacion': TextInput(attrs={'required': 'required', 'tabindex': '1'}),
            'descripcion': Textarea(attrs={'required': 'required', 'tabindex': '2', 'cols': '1', 'rows': '1'}),
            'nombre': Checkbox(attrs={'tabindex': '3'}),
        }


class EdificacionForm(ModelForm):
    """
    Docstring documentación pendiente
    """

    class Meta:
        model = Edificacion
        fields = '__all__'
        widgets = {
            'cantidad_de_pisos': radioSelectPlus(),
            'cantidad_de_inmuebles_por_piso': radioSelectPlus(),
            #'total_inmuebles': radioSelectPlus(),
            'rampa': Checkbox(),
            'escalera_estrecha': Checkbox(),
            'escalera_inclinada': Checkbox(),
            'escalon_grande': Checkbox()
        }
        labels = {
            'nombre_de_edificio': ('Nombre del edificio'),
            'tipo_de_edificacion': ('Tipo de edificación'),
            'cantidad_de_pisos': ('cantidad de pisos de la edificación'),
            'total_inmuebles': ('Total de inmuebles de la edificación'),
            'rampa': ('¿Tiene rampa la edificación?'),
            'distancia_del_vehiculo': ('Distancia del vehículo de carga al inmueble (m):'),
            'escalera_estrecha': ('¿Tiene escalera estrecha la edificación?'),
            'escalera_inclinada': ('¿Tiene escalera inclinada la edificación?'),
            'escalon_grande': ('¿Tiene escalón Grande la edificación?')
        }

AscensorFormSet = inlineformset_factory(Edificacion,
                                        Ascensor,
                                        fields=('tipo_de_ascensor',
                                                'cantidad',
                                                'piso_ascensor',
                                                'velocidad_por_piso',
                                                'ancho',
                                                'largo',
                                                'alto',
                                                'capacidad_carga'), extra=1,
                                        # widgets={'cantidad': radioSelectPlus(),
                                        #          'piso_ascensor': radioSelectPlus()},
                                        labels={'cantidad': ('Cantidad de ascensor:'),
                                                'piso_ascensor': ('Cantidad de pisos por el ascensor:'),
                                                'velocidad_por_piso': ('Velocidad por piso del ascensor:'),
                                                'ancho': ('Ancho del ascensor (cm)'),
                                                'largo': ('Largo del ascensor (cm)'),
                                                'alto': ('Alto del ascensor (cm)'),
                                                'capacidad_carga': ('Capacidad de carga del ascensor (Kg):')})

HorarioDisponibleFormSet = inlineformset_factory(Edificacion,
                                                 HorarioDisponible,
                                                 fields=('lunes',
                                                         'martes',
                                                         'miercoles',
                                                         'jueves',
                                                         'viernes',
                                                         'sabado',
                                                         'domingo',
                                                         'hora_desde',
                                                         'hora_hasta',
                                                         'edificio',
                                                         'ascensor',
                                                         'observacion'), extra=1,
                                                 widgets={'lunes': Checkbox(),
                                                          'martes': Checkbox(),
                                                          'miercoles': Checkbox(),
                                                          'jueves': Checkbox(),
                                                          'viernes': Checkbox(),
                                                          'sabado': Checkbox(),
                                                          'domingo': Checkbox(),
                                                          'edificio': Checkbox(),
                                                          'ascensor': Checkbox(),
                                                          'observacion': Textarea(attrs={'cols': '1', 'rows': '1'})},
                                                 labels={'hora_desde': ('Disponible desde la hora (H):'),
                                                         'hora_hasta': ('Disponible hasta la hora (H):'),
                                                         'edificio': ('¿Horarios disponibles para el edificio?'),
                                                         'ascensor': ('¿Horarios disponibles para el ascensor?')})


class TipoDeAscensorForm(ModelForm):
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
            'tipo_de_ascensor': TextInput(attrs={'required': 'required', 'tabindex': '1'}),
            'descripcion': Textarea(attrs={'required': 'required', 'tabindex': '2', 'cols': '1', 'rows': '1'}),
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
            'tipo_de_inmueble': ('Nombre del tipo de inmueble'),
            'descripcion': ('Descipción del tipo de inmueble')
        }
        widgets = {
            'tipo_de_inmueble': TextInput(attrs={'required': 'required', 'tabindex': '2'}),
            'descripcion': Textarea(attrs={'required': 'required', 'tabindex': '3', 'cols': '1', 'rows': '1'})
        }


class EspecificacionDeInmuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    def __init__(self, *args, **kwargs):
        super(EspecificacionDeInmuebleForm, self).__init__(*args, **kwargs)
        self.fields['tipo_de_inmueble'].empty_label = "Seleccione el tipo de inmueble"

    class Meta:
        model = EspecificacionDeInmueble
        fields = '__all__'
        widgets = {
            'tipo_de_inmueble': Select(attrs={'required': 'required', 'tabindex': '1'}),
            'especificacion_de_inmueble': TextInput(attrs={'required': 'required', 'tabindex': '2'}),
            'descripcion': Textarea(attrs={'required': 'required', 'tabindex': '3', 'cols': '1', 'rows': '1'}),
            'predeterminado': Checkbox(attrs={'tabindex': '4'}),
            }
        labels = {
            'tipo_de_inmueble': ('Tipo de inmueble asociado'),
            'especificacion_de_inmueble': ('Especificaión de inmueble'),
            'descripcion': ('Descripción de la especificaión de inmueble'),
            'predeterminado': ('¿Es predeterminada?')
            }


class InmuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    def __init__(self, *args, **kwargs):
        direccion = kwargs.pop('direccion', '')
        super(InmuebleForm, self).__init__(*args, **kwargs)
        self.fields['edificacion'] = forms.ModelChoiceField(queryset=Edificacion.objects.filter(direccion=direccion))

    class Meta:
        model = Inmueble
        fields = '__all__'
        labels = {
            'inmueble': ('Nombre del inmueble'),
            'especificacion_de_inmueble': ('Tipo de inmueble de la edificación'),
            'nombre_del_piso': ('Nombre del piso del inmueble'),
            'numero_de_pisos': ('N° del piso donde se encuentra el inmueble'),
            'cantidad_de_ambientes': ('N° de ambientes'),
            'numero_de_plantas': ('N° de pisos internos del inmueble'),
            'pisos_por_escalera': ('N° de pisos a recorrer por escaleras para llegar al inmueble'),
            'total_m2': ('Total de metros cuadrado del inmueble (m2)'),
            'baulera': ('¿Tiene baulera el inmueble?'),
            'volumen_baulera': ('Volumen de la baulera (m3)'),
            'edificacion': ('Nombre de la edificación'),
            'numero_de_inmueble': ('Numero de inmuebles en la edificación')
        }
        widgets = {
            'especificacion_de_inmueble': Select(),
            'baulera': Checkbox(),
            'numero_de_pisos': radioSelectPlus(),
            'pisos_por_escalera': radioSelectPlus(),
            'numero_de_inmueble': radioSelectPlus(),
            'numero_de_plantas': radioSelectPlus()
        }
