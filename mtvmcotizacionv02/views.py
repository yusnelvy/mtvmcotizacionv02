from django.contrib.auth import logout
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Q
from django.template import RequestContext
import re
from premisas.models import PersonalizacionVisual
from menu.models import Menu, Relacion, MenuFavorito
from django.core.urlresolvers import reverse


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

    if sidebarStatus[0].valor == '0':
        sidebarStatus.update(valor=1)
    else:
        sidebarStatus.update(valor=0)

    sidebarStatus = PersonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                         tipo="sidebarClosedOpen")

    mensaje = {'estatus': 'ok', 'msj': 'Registro guardado', 'sidebarStatus': sidebarStatus[0]['valor']}
    return JsonResponse(mensaje, safe=False)


def sidebar(request):
    """e"""
    all_categories = PersonalizacionVisual.objects.values('valor').filter(usuario__username="std",
                                                                          tipo="sidebarClosedOpen")

    return {
        'sidebar': all_categories[0]['valor'],
    }


def lista_Relacion(request):
    """docstring"""
    menu = Menu.objects.filter(nivel=3)
    url1 = request.path
    relacion = ''
    hola = 'diferentes'
    for i in menu:

        url2 = reverse('%s:%s' % (i.namespace, i.name))
        if (url1 == (url2)):
            hola = 'iguales'
            relacion = Relacion.objects.filter(item_origen_id=i.id)

            break

    context = {'relacion': relacion, 'url1': url1, 'url2': 'url2', 'hola': hola}
    return context


def lista_Menu(request):
    """docstring"""
    urlactual = request.path

    idActual = 0

    idActualFav = 0

    urln3 = ''

    nivel1 =  Menu.objects.filter(nivel=1)

    nivel2 =  Menu.objects.filter(nivel=2)

    nivel3 =  Menu.objects.filter(nivel=3)

    favoritos = MenuFavorito.objects.all().order_by('orden')

    for i in nivel3:
        urln3 = reverse('%s:%s' % (i.namespace, i.name))
        if (urlactual == urln3):
            idActual = i.id
            favoritos2 = MenuFavorito.objects.all().filter(menu_id = i.id)
            for j in favoritos2:
                    idActualFav = j.id

    context = {'nivel1': nivel1, 'nivel2': nivel2,
               'nivel3': nivel3, 'favoritos': favoritos, 'urlactual': urlactual, 'idActual': idActual, 'idActualFav': idActualFav}
    return context


def lista_Transaccion(request):
    """docstring"""
    transaccion2 = request.GET.get('variable')
    relacion =   Menu.objects.filter(nivel=3)

    for i in relacion:

        if (i.transaccion == transaccion2):
            url = '%s:%s' % (i.namespace, i.name)
            return JsonResponse({'url': reverse(url)}, safe=False)

    return JsonResponse({'url': ''}, safe=False)


