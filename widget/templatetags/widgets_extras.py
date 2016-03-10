from django import template
from django.core.urlresolvers import reverse
from widget.models import Widget

register = template.Library()

@register.simple_tag
def configurar_Widget(name):
    """docstring"""
    visible = Widget.objects.values('visible').filter(nombre=name, usuario=1)
    desplegable = Widget.objects.values('desplegable').filter(nombre=name, usuario=1)
    columnas = Widget.objects.values('numero_de_columna').filter(nombre=name, usuario=1)
    color = Widget.objects.values('color').filter(nombre=name, usuario=1)
    orden = Widget.objects.values('orden').filter(nombre=name, usuario=1)

    clases = ''

    if visible[0]['visible'] == True:
        classV = 'ocultarWidget'
    else:
        classV = 'claseV2'

    if desplegable[0]['desplegable'] == 1:
        classD = 'panel-info forma-panel'
    elif desplegable[0]['desplegable'] == 2:
        classD = 'panel-info forma-panel'
    else:
        classD = 'claseD3'

    if columnas[0]['numero_de_columna'] == '1x1':
        classC = 'fixed-panel'
    elif columnas[0]['numero_de_columna'] == '1x2':
        classC = 'claseC2'
    elif columnas[0]['numero_de_columna'] == '2x1':
        classC = 'claseC3'
    elif columnas[0]['numero_de_columna'] == '2x2':
        classC = 'claseC4'
    elif columnas[0]['numero_de_columna'] == '3x1':
        classC = 'claseC5'
    else:
        classC = 'claseC6'

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

    clases = classV + ' ' + classD + ' ' + classC + ' ' + classCo


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

    if visibleAF[0]['visible'] == True:
        classAF = "controlWidgetMostrar('panelautofiltro');"
    else:
        classAF = "controlWidgetCerrar('panelautofiltro');"

    if visibleFR[0]['visible'] == True:
        classFR = "controlWidgetMostrar('panelfiltrosrapidos');"
    else:
        classFR = "controlWidgetCerrar('panelfiltrosrapidos');"

    if visibleM[0]['visible'] == True:
        classM = "controlWidgetMostrar('panelmenu');"
    else:
        classM = "controlWidgetCerrar('panelmenu');"

    if visibleR[0]['visible'] == True:
        classR = "controlWidgetMostrar('panelrelacion');"
    else:
        classR = "controlWidgetCerrar('panelrelacion');"

    context = classFR + ' ' + classAF + ' ' + classM + ' ' + classR
    return context


@register.simple_tag
def cambiar_WidgetVisible(name):
    """docstring"""
    Widget.objects.filter(nombre=name).update(visible=False)
    return name
