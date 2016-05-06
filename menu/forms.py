"""
Docstring documentación pendiente

"""


from django.forms import ModelForm, TextInput, NumberInput, Select
from menu.models import Menu, MenuFavorito, Relacion
from djangular.forms import NgModelFormMixin, NgModelForm
from base.forms import BaseFormMd, SelectMD, Checkbox, selectSearchMD
from django import forms


class MenuForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Menu
        fields = '__all__'
        widgets = {
            'menu_padre': Select(attrs={'required': 'required', 'tabindex': '1'}),
            'menu': TextInput(attrs={'required': 'required', 'tabindex':'2'}),
            'transaccion': TextInput(attrs={'required': 'required', 'tabindex':'3'}),
            'nivel': NumberInput(attrs={'required': 'required', 'tabindex':'4'}),
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


class MenuFavoritoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = MenuFavorito
        fields = '__all__'
        widgets = {
            'usuario': Select(attrs={'required': 'required', 'tabindex': '1', 'ng-change': 'onChange()'}),
            'menu': Select(attrs={'required': 'required', 'tabindex': '2', 'ng-change': 'onChange()'}),
            'grupo': TextInput(attrs={'required': 'required', 'tabindex': '-3'}),
            'orden': NumberInput(attrs={'required': 'required', 'tabindex': '4'})
            }
        labels = {
            'menu': ('Nombre del menu'),
            'grupo': ('Nombre del grupo'),
            'usuario': ('Nombre del usuario'),
            'orden': ('Numero del orden')
            }


class RelacionForm(ModelForm):
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
            'item_origen': Select(attrs={'required': 'required', 'tabindex': '1', 'ng-change': 'onChange()'}),
            'item_relacion': Select(attrs={'required': 'required', 'tabindex': '1', 'ng-change': 'onChange()'}),
            'nombre': TextInput(attrs={'required': 'required', 'tabindex': '2'}),
            }
        labels = {
            'item_origen': ('Menú de origen'),
            'item_relacion': ('Menú de relación'),
            'nombre': ('Nombre de la relación')
            }
