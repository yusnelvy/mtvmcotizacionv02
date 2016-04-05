"""
Docstring documentación pendiente

"""


from django.forms import ModelForm, TextInput, NumberInput, Select
from menu.models import Menu, MenuFavorito, Relacion
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd, SelectMD, Checkbox, selectSearchMD
from django import forms


class MenuForm(NgModelFormMixin, NgModelForm, BaseFormMd):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Menu
        fields = '__all__'
        widgets = {
            'menu_padre': selectSearchMD(),
            'menu': TextInput(attrs={'required': 'required'}),
            'transaccion': TextInput(attrs={'required': 'required'}),
            'nivel': NumberInput(attrs={'required': 'required'})
            }
        labels = {
            'menu': ('Nombre del menu'),
            'transaccion': ('Nombre de la transacción'),
            'namespace': ('Nombre del namespace'),
            'name': ('Texto del name'),
            'nivel': ('Numero del nivel'),
            'padre': ('¿Es menú padre?'),
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
            'usuario': selectSearchMD(attrs={'required': 'required', 'tabindex': '-1'}),
            'menu': selectSearchMD(attrs={'required': 'required', 'tabindex': '1'}),
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
    def __init__(self, *args, **kwargs):
       super(RelacionForm, self).__init__(*args, **kwargs)
       self.fields['item_origen'].query_set = Menu.objects.filter(nivel=3)
       self.fields['item_relacion'].query_set = Menu.objects.filter(nivel=3)

    class Meta:
        model = Relacion
        fields = '__all__'
        widgets = {
            'item_origen': selectSearchMD(),
            'item_relacion': selectSearchMD(),
            'nombre': TextInput(attrs={'required': 'required'})
            }
        labels = {
            'item_origen': ('Menú de origen'),
            'item_relacion': ('Menú de relación'),
            'nombre': ('Nombre de la relación')
            }
