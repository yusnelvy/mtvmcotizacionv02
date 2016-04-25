from django import template
from django.core.urlresolvers import reverse
from widget.models import Widget
from gestiondedocumento.models import EstadoDeDocumento
from cotizacionweb.models import CotizacionEstado

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

# @register.inclusion_tag('Fases-del-Proceso.html', takes_context=True)
# def pruebaContext(context):
#     prueba = context
#     return prueba



# @register.simple_tag
# def url_FasesDelProceso(request):
#     """e"""
#     url = request.path

#     contador = EstadoDeDocumento.objects.filter(tipo_de_documento=3).count()
#     incremento = (100/contador)
#     cotizacion = request.GET.get('cotizacion')
#     id_estado = CotizacionEstado.objects.filter(predefinido=True).exclude(estado_de_documento=None)
#     # id_estado = CotizacionEstado.objects.filter(predefinido=True, cotizacion=cotizacion).exclude(estado_de_documento=None)
#     ordenActual = id_estado[0].estado_de_documento.orden
#     porcentajeString = str(round(incremento*ordenActual))
#     porcentaje = porcentajeString + '%'
#     return {
#         'w_porcentaje': porcentaje,
#     }

# @register.simple_tag
# def fases_FasesDelProceso(request):
#     """e"""
#     id_estado = CotizacionEstado.objects.filter(predefinido=True).exclude(estado_de_documento=None)
#     # id_estado = CotizacionEstado.objects.filter(predefinido=True, cotizacion=cotizacion).exclude(estado_de_documento=None)
#     ordenActual = id_estado[0].estado_de_documento.orden
#     fasesFaltantes = EstadoDeDocumento.objects.values('estado_de_documento','orden').filter(tipo_de_documento=3, orden__gt=ordenActual)
#     fasesSuperadas = EstadoDeDocumento.objects.values('estado_de_documento','orden').filter(tipo_de_documento=3).exclude(orden__gt=ordenActual).exclude(orden=ordenActual)
#     faseActual = EstadoDeDocumento.objects.values('estado_de_documento','orden').filter(tipo_de_documento=3, orden=ordenActual)
#     return {
#         'w_fasesA': faseActual,
#         'w_fasesS': fasesSuperadas,
#         'w_fasesF': fasesFaltantes,
#     }
