"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput
from menu.models import Menu, MenuFavorito, Relacion


class MenuForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Menu
        fields = '__all__'


class MenuFavoritoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = MenuFavorito
        fields = '__all__'


class RelacionForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Relacion
        fields = '__all__'
