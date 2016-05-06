"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput, Textarea, Select
from mensaje.models import TipoDeMensaje, Mensaje
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd, SelectMD, Checkbox


class TipoDeMensajeForm(ModelForm):
    """
    Docstring documentación pendiente
    """

    class Meta:
        model = TipoDeMensaje
        fields = '__all__'
        widgets = {
            'tipo_de_mensaje': TextInput(attrs={'required': 'required', 'tabindex':'1'}),
            'descripcion': Textarea(attrs={'required': 'required', 'tabindex': '2', 'cols': '1', 'rows': '1'}),
            }
        labels = {
            'descripcion': ('Descripción del tipo de mensaje'),
            'tipo_de_mensaje': ('Nombre del tipo de mensaje')
            }


class MensajeForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    def __init__(self, *args, **kwargs):
        super(MensajeForm, self).__init__(*args, **kwargs)
        self.fields['tipo_de_mensaje'].empty_label = "Seleccione el tipo de mensaje"

    class Meta:
        model = Mensaje
        fields = '__all__'
        widgets = {
            'mensaje': TextInput(attrs={'required': 'required', 'tabindex':'2'}),
            'descripcion': Textarea(attrs={'required': 'required', 'tabindex': '3', 'cols': '1', 'rows': '1'}),
            'codigo': TextInput(attrs={'required': 'required', 'tabindex':'4'}),
            'tipo_de_mensaje': Select(attrs={'required': 'required', 'tabindex': '1'})
            }
        labels = {
            'tipo_de_mensaje': ('Nombre del tipo de mensaje'),
            'mensaje': ('Texto del mensaje'),
            'codigo': ('Código del mensaje'),
            'descripcion': ('Descripción del tipo de mensaje')
        }
