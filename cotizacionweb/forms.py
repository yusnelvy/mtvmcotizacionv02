"""
Docstring documentación pendiente

"""
from django.forms import ModelForm
from django import forms
from cotizacionweb.models import TipoDireccion, ConceptoDeCotizacion, \
    FechaDeCotizacion, CotizacionBitacora, CotizacionAmbiente, \
    CotizacionMueble, CotizacionDireccion, ContenedorMueble, \
    ServicioMueble
from cotizador.models import Cotizador


class CotizacionForm(forms.Form):
    cotizador_choices = [(cotizador.id, cotizador.id_trabajador) for cotizador in Cotizador.objects.all()]

    fecha_mudanza = forms.DateTimeField()
    fecha_visita = forms.DateTimeField()
    cotizador = forms.ChoiceField(label='Cotizador',
                                  choices=cotizador_choices)


class CotizacionDireccionForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = CotizacionDireccion
        fields = '__all__'


class TipoDireccionForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = TipoDireccion
        fields = '__all__'


class ConceptoDeCotizacionForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = ConceptoDeCotizacion
        fields = '__all__'


class FechaDeCotizacionForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = FechaDeCotizacion
        fields = '__all__'


class CotizacionBitacoraForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = CotizacionBitacora
        fields = '__all__'


class CotizacionAmbienteForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    ch_ambiente = forms.BooleanField(required=False)

    class Meta:
        model = CotizacionAmbiente
        fields = '__all__'


class CotizacionMuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    def __init__(self, *args, **kwargs):
        super(CotizacionMuebleForm, self).__init__(*args, **kwargs)
        self.fields['direccion_destino'] = forms.ModelChoiceField(queryset=CotizacionDireccion.objects.filter(tipo_direccion__tipo_direccion="Destino"))

    class Meta:
        model = CotizacionMueble
        fields = '__all__'


class ContenedorMuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    def __init__(self, *args, **kwargs):
        super(ContenedorMuebleForm, self).__init__(*args, **kwargs)
        self.fields['tipo_de_contenido'].empty_label = None

    ch_contenedor = forms.BooleanField(required=False)

    class Meta:
        model = ContenedorMueble
        fields = '__all__'


class ServicioMuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """

    ch_servicio = forms.BooleanField(required=False)

    class Meta:
        model = ServicioMueble
        fields = 'cotizacion_mueble', \
            'servicio', \
            'descripcion_servicio'
