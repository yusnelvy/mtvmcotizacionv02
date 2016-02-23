from django.forms import ModelForm, Select
from menu.models import Menu, MenuFavorito, Relacion
from django import forms


class MenuForm(ModelForm):
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
    item_choices = [(content.item_origen, content.item_relacion) for content in Menu.objects.filter(nivel=3)]

    item_origen = forms.ChoiceField(
        widget=Select(attrs={'class': 'form-control'}),
        label='Item origen',
        choices=item_choices)
    item_relacion = forms.ChoiceField(
        widget=Select(attrs={'class': 'form-control'}),
        label='item relación',
        choices=item_choices)

    class Meta:
        model = Relacion
        fields = '__all__'
