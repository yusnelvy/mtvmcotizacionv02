"""
Docstring documentación pendiente

"""
from widget.models import Widget
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd


class WidgetForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Widget
        fields = '__all__'
