from django import template
from django.core.urlresolvers import reverse
from widget.models import Widget

register = template.Library()

@register.simple_tag
def configurar_Widget(name):
    """docstring"""
    visible = Widget.objects.values('visible').filter(nombre=name, usuario=1)
    columnas = Widget.objects.values('numero_de_columna').filter(nombre=name, usuario=1)
    color = Widget.objects.values('color').filter(nombre=name, usuario=1)
    orden = Widget.objects.values('orden').filter(nombre=name, usuario=1)

    clases = ''

    if visible[0]['visible'] == True:
        classV = 'ocultarWidget'
    else:
        classV = 'claseV2'

    if columnas[0]['numero_de_columna'] == '1x1':
        classC = 'fixed-panel'
    elif columnas[0]['numero_de_columna'] == '1x2':
        classC = 'fixed-panel'
    elif columnas[0]['numero_de_columna'] == '2x1':
        classC = 'fixed-panel'
    elif columnas[0]['numero_de_columna'] == '2x2':
        classC = 'fixed-panel'
    elif columnas[0]['numero_de_columna'] == '3x1':
        classC = 'fixed-panel'
    else:
        classC = 'fixed-panel'

    if color[0]['color'] == 'Azul':
        classCo = 'panelAzul'
    elif color[0]['color'] == 'Verde':
        classCo = 'panelVerde'
    elif color[0]['color'] == 'Amarillo':
        classCo = 'panelAmarillo'
    elif color[0]['color'] == 'Rojo':
        classCo = 'panelRojo'
    else:
        classCo = 'panelNaranja'

    clases = classV + ' ' + classC + ' ' + classCo


    context = clases
    return context

@register.simple_tag
def configurar_WidgetColor(name):
    """docstring"""
    color = Widget.objects.values('color').filter(nombre=name, usuario=1)

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

    return classCo

@register.simple_tag
def configurar_WidgetVisible():
    """docstring"""
    visibleAF = Widget.objects.values('visible').filter(nombre='Autofiltros', usuario=1)
    visibleFR = Widget.objects.values('visible').filter(nombre='Filtros Rápidos', usuario=1)
    visibleM = Widget.objects.values('visible').filter(nombre='Menú', usuario = 1)
    visibleR = Widget.objects.values('visible').filter(nombre='Tablas Relacionadas', usuario = 1)
    visibleF = Widget.objects.values('visible').filter(nombre='Ficha', usuario = 1)

    if visibleAF[0]['visible'] == True:
        classAF = "controlWidgetMostrar('liautofiltros');"
    else:
        classAF = "controlWidgetCerrar('liautofiltros');"

    if visibleFR[0]['visible'] == True:
        classFR = "controlWidgetMostrar('lifiltrorapido');"
    else:
        classFR = "controlWidgetCerrar('lifiltrorapido');"

    if visibleM[0]['visible'] == True:
        classM = "controlWidgetMostrar('limenu');"
    else:
        classM = "controlWidgetCerrar('limenu');"

    if visibleR[0]['visible'] == True:
        classR = "controlWidgetMostrar('lirelacion');"
    else:
        classR = "controlWidgetCerrar('lirelacion');"

    if visibleF[0]['visible'] == True:
        classF = "controlWidgetMostrar('lificha');"
    else:
        classF = "controlWidgetCerrar('lificha');"

    context = classFR + ' ' + classAF + ' ' + classM + ' ' + classR + ' ' + classF
    return context


@register.simple_tag
def cambiar_WidgetVisible(name):
    """docstring"""
    Widget.objects.filter(nombre=name).update(visible=False)
    return name


@register.simple_tag
def configurar_WidgetColumna(name):
    """docstring"""
    columna = Widget.objects.values('numero_de_columna').filter(nombre=name, usuario=1)

    if columna[0]['numero_de_columna'] == '1x0':
        columna = "minima"
    if columna[0]['numero_de_columna'] == '1x1':
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

    context = columna
    return context
