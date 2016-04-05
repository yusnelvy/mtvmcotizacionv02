from django import template
from django.core.urlresolvers import reverse
from widget.models import Widget

register = template.Library()

@register.simple_tag
def configurar_WidgetColor(name):
    """docstring"""
    color = Widget.objects.values('color').filter(nombre=name, usuario=1)

    if color:
        if color[0]['color'] == 'Azul':
            classCo = 'claseAzul'
        elif color[0]['color'] == 'Verde':
            classCo = 'claseVerde'
        elif color[0]['color'] == 'Amarillo':
            classCo = 'claseAmarillo'
        elif color[0]['color'] == 'Rojo':
            classCo = 'claseRojo'
        else:
            classCo = 'claseNaranja'
    else:
        classCo = 'claseNaranja'


    return classCo

@register.simple_tag
def configurar_WidgetVisible(name):
    """docstring"""
    visible = Widget.objects.values('visible').filter(nombre=name, usuario=1)
    if visible:
        isVisible = visible[0]['visible']
    else:
        isVisible = False
    return isVisible

@register.simple_tag
def retornar_WidgetPorUsuario(name):
    """docstring"""
    widgetsN = Widget.objects.values('nombre').filter(usuario=usuario)
    widgetsO = Widget.objects.values('orden').filter(usuario=usuario)
    return widgetsN

@register.simple_tag
def cambiar_WidgetVisible(name):
    """docstring"""
    Widget.objects.filter(nombre=name).update(visible=False)
    return name

@register.simple_tag
def configurar_WidgetColumna(name):
    """docstring"""
    columna = Widget.objects.values('numero_de_columna').filter(nombre=name, usuario=1)

    if columna:

        if columna[0]['numero_de_columna'] == '1x0':
            columna = "minima"
        elif columna[0]['numero_de_columna'] == '1x1':
            columna = "tamano1x1"
        elif columna[0]['numero_de_columna'] == '1x2':
            columna = "tamano1x2"
        elif columna[0]['numero_de_columna'] == '2x1':
            columna = "tamano2x1"
        elif columna[0]['numero_de_columna'] == '2x2':
            columna = "tamano2x2"
        elif columna[0]['numero_de_columna'] == '1x3':
            columna = "tamano1x3"
        else:
            columna = "tamano2x3"

    else:
        columna = "tamano2x3"

    context = columna
    return context

