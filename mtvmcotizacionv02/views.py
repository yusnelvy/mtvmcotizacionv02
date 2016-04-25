from django.contrib.auth import logout
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Q
from django.template import RequestContext
import re
from premisas.models import PersonalizacionVisual
from django.core.urlresolvers import reverse
from widget.models import Widget
from gestiondedocumento.models import EstadoDeDocumento
from cotizacionweb.models import CotizacionEstado


def pantalla_inicial(request):
    """Docstring"""
    return render(request, 'index.html')


def guia_de_estilo(request):
    """Docstring"""
    return render(request, 'guiadeestilo.html')


def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')


def show_dashboard(request):
    """
    Mostrar el dashboard inicial
    """
    context = {'show_dashboard': ""}
    return render(request, 'base_menu.html', context)


# funciones para realizar las consultas de busqueda (search)
def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:

        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']

    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]


def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.

    '''
    query = None  # Query to search for every search term
    or_query = None  # Query to search for a given term in each field
    for field_name in search_fields:
        q = Q(**{"%s__icontains" % field_name: query_string})
        if or_query is None:
            or_query = q
        else:
            or_query = or_query | q
    if query is None:
        query = or_query
    else:
        query = query & or_query
    return query


#Esta funcion separa una cadena en varias variables de busqueda
#si existe espacio en blancos entre las palabras para generar el query
def get_querymultiplestring(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.

    '''
    query = None  # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None  # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query


def valor_Personalizacionvisual(usuario, tipo):

    if usuario == "std":
        valor = PersonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                     tipo=tipo)
    else:
        valor = PersonalizacionVisual.objects.values('valor').filter(usuario=usuario,
                                                                     tipo=tipo)
        if len(valor) == 0:
            valor = PersonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                         tipo=tipo)
    valor = valor[0]['valor']
    return valor


def sidebarUpdate(request):
    """e"""
    sidebarStatus = PersonalizacionVisual.objects.filter(usuario__username="std",
                                                         tipo="sidebarClosedOpen")
    if request.method == "GET" and request.is_ajax():
        nivel = request.GET['nivel']
        sidebarStatus.update(valor=nivel)

    sidebarStatus = PersonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                         tipo="sidebarClosedOpen")

    mensaje = {'estatus': 'ok', 'msj': 'Registro guardado', 'sidebarStatus': str(sidebarStatus[0]['valor'])}
    return JsonResponse(mensaje, safe=False)


def sidebar(request):
    """e"""
    all_categories = PersonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                          tipo="sidebarClosedOpen")

    return {
        'sidebar': all_categories[0]['valor'],
    }


def wVisible(request):
    """e"""
    all_categories2 = Widget.objects.values('nombre','visible', 'numero_de_columna').filter(usuario=1)

    return {
        'w_visble': all_categories2,
    }

def wOrden(request):
    """e"""
    all_widgets = Widget.objects.values('nombre','orden', 'visible').filter(usuario=1).order_by('orden')

    return {
        'w_orden': all_widgets,
    }

def porcentaje_FasesDelProceso(request):
    """e"""
    contador = EstadoDeDocumento.objects.filter(tipo_de_documento=3).count()
    incremento = (100/contador)
    cotizacion = request.GET.get('cotizacion')
    id_estado = CotizacionEstado.objects.filter(predefinido=True).exclude(estado_de_documento=None)
    # id_estado = CotizacionEstado.objects.filter(predefinido=True, cotizacion=cotizacion).exclude(estado_de_documento=None)
    ordenActual = id_estado[0].estado_de_documento.orden
    porcentajeString = str(round(incremento*ordenActual))
    porcentaje = porcentajeString + '%'
    return {
        'w_porcentaje': porcentaje,
    }

def fases_FasesDelProceso(request):
    """e"""
    id_estado = CotizacionEstado.objects.filter(predefinido=True).exclude(estado_de_documento=None)
    # id_estado = CotizacionEstado.objects.filter(predefinido=True, cotizacion=cotizacion).exclude(estado_de_documento=None)
    ordenActual = id_estado[0].estado_de_documento.orden
    fasesFaltantes = EstadoDeDocumento.objects.values('estado_de_documento','orden').filter(tipo_de_documento=3, orden__gt=ordenActual)
    fasesSuperadas = EstadoDeDocumento.objects.values('estado_de_documento','orden').filter(tipo_de_documento=3).exclude(orden__gt=ordenActual).exclude(orden=ordenActual)
    faseActual = EstadoDeDocumento.objects.values('estado_de_documento','orden').filter(tipo_de_documento=3, orden=ordenActual)
    return {
        'w_fasesA': faseActual,
        'w_fasesS': fasesSuperadas,
        'w_fasesF': fasesFaltantes,
    }
