"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput, NumberInput
from menu.models import Menu, MenuFavorito, Relacion
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd, SelectMD, Checkbox


class MenuForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Menu
        fields = '__all__'
        widgets = {
            'menu_padre': SelectMD(),
            'menu': TextInput(attrs={'required': 'required'}),
            'transaccion': TextInput(attrs={'required': 'required'}),
            'namespace': TextInput(attrs={'required': 'required'}),
            'name': TextInput(attrs={'required': 'required'}),
            'nivel': NumberInput(attrs={'required': 'required'})
            }
        labels = {
            'menu': ('Nombre del menu'),
            'transaccion': ('Nombre de la transacción'),
            'namespace': ('Nombre del namespace'),
            'name': ('Texto del name'),
            'nivel': ('Numero del nivel'),
            'padre': ('Menú padre'),
            'menu_padre': ('Menú padre asignado')
            }


class MenuFavoritoForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = MenuFavorito
        fields = '__all__'
        widgets = {
            'usuario': SelectMD(),
            'menu': SelectMD(),
            'grupo': TextInput(attrs={'required': 'required'}),
            'orden': NumberInput(attrs={'required': 'required'})
            }
        labels = {
            'menu': ('Nombre del menu'),
            'grupo': ('Nombre del grupo'),
            'usuario': ('Nombre del usuario'),
            'orden': ('Numero del orden')
            }


class RelacionForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Relacion
        fields = '__all__'
        widgets = {
            'item_origen': SelectMD(),
            'item_relacion': SelectMD(),
            'nombre': TextInput(attrs={'required': 'required'})
            }
        labels = {
            'item_origen': ('Menú de origen'),
            'item_relacion': ('Menú de relación'),
            'nombre': ('Nombre de la relación')
            }
