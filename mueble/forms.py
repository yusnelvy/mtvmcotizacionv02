"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput
from mueble.models import TipoDeMueble, Mueble, \
    EspecificacionDeMueble, MueblePorAmbiente
from djangular.forms import NgModelFormMixin, NgModelForm
#from django.forms.forms import _html_output


class TipoDeMuebleForm(NgModelFormMixin, NgModelForm):
    def as_p(self):
        """
        Returns this form rendered as HTML <md-input-container>s.

        """
        return self._html_output(
            normal_row='<md-input-container%(html_class_attr)s>%(label)s %(field)s%(help_text)s</md-input-container>',
            error_row='%s',
            row_ender='</md-input-container>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True)

    class Meta:
        model = TipoDeMueble
        fields = '__all__'
        widgets = {
            'tipo_de_mueble': TextInput(attrs={'required': 'required'})
            }
        labels = {
            'descripcion': ('Descripción del tipo de mueble'),
            'tipo_de_mueble': ('Nombre del tipo de mueble')
            }

    # fields as usual

    # def as_p(self):
    #     "Returns this form rendered as HTML <p>s."
    #     return self._html_output(
    #         normal_row = u'<p%(html_class_attr)s>%(label)s</p> %(field)s%(help_text)s',
    #         error_row = u'%s',
    #         row_ender = '</p>',
    #         help_text_html = u' <span class="helptext">%s</span>',
    #         errors_on_separate_row = True)


# class TipoDeMuebleForm(ModelForm):
#     """
#     Docstring documentación pendiente
#     """
#     class Meta:
#         model = TipoDeMueble
#         fields = '__all__'
#         widgets = {
#             'descripcion': TextInput()
#             }
#         labels = {
#             'descripcion': ('Descripción del tipo de mueble'),
#             'tipo_de_mueble': ('Nombre del tipo de mueble')
#         }


class MuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Mueble
        fields = '__all__'
        widgets = {
            'descripcion': TextInput()
            }


class EspecificacionDeMuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = EspecificacionDeMueble
        fields = '__all__'


class MueblePorAmbienteForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = MueblePorAmbiente
        fields = '__all__'
