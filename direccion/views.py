"""
Docstring documentación pendiente

"""

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.generic import ListView, View, UpdateView, DeleteView
from direccion.models import Pais, Provincia, Ciudad, \
    Barrio, Direccion, TipoDeEdificacion, TipoDeAscensor, \
    TipoDeInmueble, EspecificacionDeInmueble
from direccion.forms import PaisForm, ProvinciaForm, \
    CiudadForm, BarrioForm, DireccionForm, TipoDeEdificacionForm, \
    TipoDeAscensorForm, TipoDeInmuebleForm, EspecificacionDeInmuebleForm
from mtvmcotizacionv02.views import valor_Personalizacionvisual, get_query
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import transaction
import sys


# Create your views here.
# app país
class PaisListView(ListView):
    model = Pais
    paginate_by = 10
    context_object_name = 'paises'
    template_name = 'pais_lista.html'

    def get_paginate_by(self, queryset):
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        page = self.request.GET.get('page')
        if page == '0':
            return None
        else:
            return self.request.GET.get('paginate_by', nropag)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PaisListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")
        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['pais',
                                             'codigo_telefonico', ])
            lista_pais = Pais.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['pais',
                                             'codigo_telefonico', ])
            lista_pais = Pais.objects.filter(entry_query)
        elif order_by:
            lista_pais = Pais.objects.all().order_by(order_by)
        else:
            lista_pais = Pais.objects.all()

        paginator = Paginator(lista_pais, 10)
        page = self.request.GET.get('page')
        if page:

            if int(page) > int(range_gap):
                start = int(page)-int(range_gap)
            else:
                start = 1

            if int(page) < paginator.num_pages-int(range_gap):
                end = int(page)+int(range_gap)+1
            else:
                end = paginator.num_pages+1
        else:
            if 1 > int(range_gap):
                start = 1-int(range_gap)
            else:
                start = 1

            if 1 < paginator.num_pages-int(range_gap):
                end = 1+int(range_gap)+1
            else:
                end = paginator.num_pages+1

        context['ultimo'] = str(paginator.num_pages)
        context['page_range2'] = range(start, end)
        return context

    def get_queryset(self):

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['pais',
                                             'codigo_telefonico', ])
            queryset = Pais.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['pais',
                                             'codigo_telefonico', ])
            queryset = Pais.objects.filter(entry_query)
        elif order_by:
            queryset = Pais.objects.all().order_by(order_by)
        else:
            queryset = Pais.objects.all()

        return queryset


class PaisView(View):
    form_class = PaisForm
    template_name = 'pais_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()
            if 'regEdit' in request.POST:

                # <process form cleaned data>
                messages.success(self.request, "País '" + str(id_reg) + "' agregado con éxito.",
                                 extra_tags=reverse('udirecciones:list_pais'))
                return HttpResponseRedirect(reverse('udirecciones:edit_pais',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "País '" + str(id_reg) + "' agregado con éxito.")
                return HttpResponseRedirect(reverse('udirecciones:list_pais'))

        return render(request, self.template_name, {'form': form})


class PaisUpdate(UpdateView):
    template_name = 'pais_edit.html'
    form_class = PaisForm
    model = Pais

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PaisUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        pais = Pais.objects.get(pk=self.object.pk)
        redirect_to = self.request.REQUEST.get('next', '')
        order_by = self.request.REQUEST.get('order_by', '')
        page = self.request.REQUEST.get('page', '')

        if order_by:
            redirect_to = redirect_to + '&order_by=' + order_by

        if page:
            redirect_to = redirect_to + '&page=' + page

        variable = self.request.REQUEST.get('next', '').split("?")
        if len(variable) > 1:

            if variable[1].split("=")[0] == 'page':
                page = self.request.REQUEST.get('next', '').split("?")[1].split("=")[1]
            elif variable[1].split("=")[0] == 'order_by':
                order_by = self.request.REQUEST.get('next', '').split("?")[1].split("=")[1]

        if order_by:
            lista_pais = Pais.objects.all().order_by(order_by)
        else:
            lista_pais = Pais.objects.all()

        paginator = Paginator(lista_pais, nropag)
        # Show 25 contacts per page

        if page == '0':
            paises = lista_pais
        else:
            try:
                paises = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                paises = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                paises = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(paises.object_list[i].id == pais.id):
                    if paises.has_previous:
                        try:
                            previousitem = paises.object_list[i-1].id
                        except:
                            previousitem = None

                    if paises.has_next:
                        try:
                            nextitem = paises.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(paises)
            for i in range(0, countitem):
                if(paises[i].id == pais.id):
                    try:
                        previousitem = paises[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = paises[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            pais_previous = Pais.objects.get(pk=previousitem)
        except:
            pais_previous = None
        try:
            pais_next = Pais.objects.get(pk=nextitem)
        except:
            pais_next = None

        context['pais_previous'] = pais_previous
        context['pais_next'] = pais_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "País '" + str(self.object) + "' guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "País '" + str(self.object) + "' guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                return render_to_response(self.template_name, self.get_context_data())


class PaisDelete(DeleteView):
    model = Pais
    form_class = PaisForm
    template_name = 'server_confirm_delete.html'

    @transaction.atomic
    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        context = self.obj.id

        order_by = self.request.REQUEST.get('order_by', '')
        page = self.request.REQUEST.get('page', '')
        next = self.request.REQUEST.get('next', '')
        variable = self.request.REQUEST.get('next', '').split("?")
        if len(variable) > 1:

            if variable[1].split("=")[0] == 'ficha':
                next = variable[0]
                if order_by and page:
                    next = next + '?order_by=' + order_by + '&page='+ page
                elif order_by:
                    next = next + '?order_by=' + order_by
                elif page:
                    next = next + '?page=' + page
            elif variable[1].split("=")[0] == 'page':
                if order_by:
                    next = next + '&order_by=' + order_by
            elif variable[1].split("=")[0] == 'order_by':
                if page:
                    next = next + '&page=' + page

        self.obj.delete()
        messages.success(self.request, "Pais " + str(self.obj) + " eliminado con éxito.", extra_tags=next)
        return render(request, '../../mensaje/templates/mensaje.html', {'obj': context})


# app provincia
class ProvinciaListView(ListView):
    model = Provincia
    paginate_by = 10
    context_object_name = 'provincias'
    template_name = 'provincia_lista.html'

    def get_paginate_by(self, queryset):
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        page = self.request.GET.get('page')
        if page == '0':
            return None
        else:
            return self.request.GET.get('paginate_by', nropag)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProvinciaListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")
        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['provincia',
                                             'pais__pais',
                                             'codigo_telefonico', ])

            lista_provincia = Provincia.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['provincia',
                                             'pais__pais',
                                             'codigo_telefonico', ])

            lista_provincia = Provincia.objects.filter(entry_query)
        elif order_by:
            lista_provincia = Provincia.objects.all().order_by(order_by)
        else:
            lista_provincia = Provincia.objects.all()

        paginator = Paginator(lista_provincia, 10)
        page = self.request.GET.get('page')
        if page:

            if int(page) > int(range_gap):
                start = int(page)-int(range_gap)
            else:
                start = 1

            if int(page) < paginator.num_pages-int(range_gap):
                end = int(page)+int(range_gap)+1
            else:
                end = paginator.num_pages+1
        else:
            if 1 > int(range_gap):
                start = 1-int(range_gap)
            else:
                start = 1

            if 1 < paginator.num_pages-int(range_gap):
                end = 1+int(range_gap)+1
            else:
                end = paginator.num_pages+1

        context['ultimo'] = str(paginator.num_pages)
        context['page_range2'] = range(start, end)
        return context

    def get_queryset(self):

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['provincia',
                                             'pais__pais',
                                             'codigo_telefonico', ])

            queryset = Provincia.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['provincia',
                                             'pais__pais',
                                             'codigo_telefonico', ])

            queryset = Provincia.objects.filter(entry_query)
        elif order_by:
            queryset = Provincia.objects.all().order_by(order_by)
        else:
            queryset = Provincia.objects.all()

        return queryset


class ProvinciaView(View):
    form_class = ProvinciaForm
    template_name = 'provincia_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:

                # <process form cleaned data>
                messages.success(self.request, "Provincia '" + str(id_reg) + "' agregado con éxito.",
                                 extra_tags=reverse('udirecciones:list_provincia'))
                return HttpResponseRedirect(reverse('udirecciones:edit_provincia',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Provincia '" + str(id_reg) + "' agregado con éxito.")
                return HttpResponseRedirect(reverse('udirecciones:list_provincia'))

        return render(request, self.template_name, {'form': form})


class ProvinciaUpdate(UpdateView):
    template_name = 'provincia_edit.html'
    form_class = ProvinciaForm
    model = Provincia

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProvinciaUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        provincia = Provincia.objects.get(pk=self.object.pk)
        redirect_to = self.request.REQUEST.get('next', '')
        order_by = self.request.REQUEST.get('order_by', '')
        page = self.request.REQUEST.get('page', '')

        if order_by:
            redirect_to = redirect_to + '&order_by=' + order_by

        if page:
            redirect_to = redirect_to + '&page=' + page

        variable = self.request.REQUEST.get('next', '').split("?")
        if len(variable) > 1:

            if variable[1].split("=")[0] == 'page':
                page = self.request.REQUEST.get('next', '').split("?")[1].split("=")[1]
            elif variable[1].split("=")[0] == 'order_by':
                order_by = self.request.REQUEST.get('next', '').split("?")[1].split("=")[1]

        if order_by:
            lista_provincia = Provincia.objects.all().order_by(order_by)
        else:
            lista_provincia = Provincia.objects.all()

        paginator = Paginator(lista_provincia, nropag)
        # Show 25 contacts per page

        if page == '0':
            provincias = lista_provincia
        else:
            try:
                provincias = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                provincias = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                provincias = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(provincias.object_list[i].id == provincia.id):
                    if provincias.has_previous:
                        try:
                            previousitem = provincias.object_list[i-1].id
                        except:
                            previousitem = None

                    if provincias.has_next:
                        try:
                            nextitem = provincias.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(provincias)
            for i in range(0, countitem):
                if(provincias[i].id == provincia.id):
                    try:
                        previousitem = provincias[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = provincias[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            provincia_previous = Provincia.objects.get(pk=previousitem)
        except:
            provincia_previous = None
        try:
            provincia_next = Provincia.objects.get(pk=nextitem)
        except:
            provincia_next = None

        context['provincia_previous'] = provincia_previous
        context['provincia_next'] = provincia_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Provincia '" + str(self.object) + "' guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Provincia '" + str(self.object) + "' guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                return render_to_response(self.template_name, self.get_context_data())


class ProvinciaDelete(DeleteView):
    model = Provincia
    form_class = ProvinciaForm
    template_name = 'server_confirm_delete.html'

    @transaction.atomic
    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        context = self.obj.id

        order_by = self.request.REQUEST.get('order_by', '')
        page = self.request.REQUEST.get('page', '')
        next = self.request.REQUEST.get('next', '')
        variable = self.request.REQUEST.get('next', '').split("?")
        if len(variable) > 1:

            if variable[1].split("=")[0] == 'ficha':
                next = variable[0]
                if order_by and page:
                    next = next + '?order_by=' + order_by + '&page='+ page
                elif order_by:
                    next = next + '?order_by=' + order_by
                elif page:
                    next = next + '?page=' + page
            elif variable[1].split("=")[0] == 'page':
                if order_by:
                    next = next + '&order_by=' + order_by
            elif variable[1].split("=")[0] == 'order_by':
                if page:
                    next = next + '&page=' + page

        self.obj.delete()
        messages.success(self.request, "Provincia " + str(self.obj) + " eliminado con éxito.", extra_tags=next)
        return render(request, '../../mensaje/templates/mensaje.html', {'obj': context})


# app ciudad
class CiudadListView(ListView):
    model = Ciudad
    paginate_by = 10
    context_object_name = 'ciudades'
    template_name = 'ciudad_lista.html'

    def get_paginate_by(self, queryset):
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        page = self.request.GET.get('page')
        if page == '0':
            return None
        else:
            return self.request.GET.get('paginate_by', nropag)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CiudadListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")
        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['provincia__provincia',
                                             'pais__pais',
                                             'ciudad', ])

            lista_ciudad = Ciudad.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['provincia__provincia',
                                             'pais__pais',
                                             'ciudad', ])

            lista_ciudad = Ciudad.objects.filter(entry_query)
        elif order_by:
            lista_ciudad = Ciudad.objects.all().order_by(order_by)
        else:
            lista_ciudad = Ciudad.objects.all()

        paginator = Paginator(lista_ciudad, 10)
        page = self.request.GET.get('page')
        if page:

            if int(page) > int(range_gap):
                start = int(page)-int(range_gap)
            else:
                start = 1

            if int(page) < paginator.num_pages-int(range_gap):
                end = int(page)+int(range_gap)+1
            else:
                end = paginator.num_pages+1
        else:
            if 1 > int(range_gap):
                start = 1-int(range_gap)
            else:
                start = 1

            if 1 < paginator.num_pages-int(range_gap):
                end = 1+int(range_gap)+1
            else:
                end = paginator.num_pages+1

        context['ultimo'] = str(paginator.num_pages)
        context['page_range2'] = range(start, end)
        return context

    def get_queryset(self):

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['provincia__provincia',
                                             'pais__pais',
                                             'ciudad', ])

            queryset = Ciudad.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['provincia__provincia',
                                             'pais__pais',
                                             'ciudad', ])

            queryset = Ciudad.objects.filter(entry_query)
        elif order_by:
            queryset = Ciudad.objects.all().order_by(order_by)
        else:
            queryset = Ciudad.objects.all()

        return queryset


class CuidadView(View):
    form_class = CiudadForm
    template_name = 'ciudad_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:

                # <process form cleaned data>
                messages.success(self.request, "Ciudad '" + str(id_reg) + "' registrado con éxito.",
                                 extra_tags=reverse('udirecciones:list_ciudad'))
                return HttpResponseRedirect(reverse('udirecciones:edit_ciudad',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Ciudad '" + str(id_reg) + "' registrado con éxito.")
                return HttpResponseRedirect(reverse('udirecciones:list_ciudad'))

        return render(request, self.template_name, {'form': form})


class CiudadUpdate(UpdateView):
    template_name = 'ciudad_edit.html'
    form_class = CiudadForm
    model = Ciudad

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CiudadUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        ciudad = Ciudad.objects.get(pk=self.object.pk)
        redirect_to = self.request.REQUEST.get('next', '')
        order_by = self.request.REQUEST.get('order_by', '')
        page = self.request.REQUEST.get('page', '')

        if order_by:
            redirect_to = redirect_to + '&order_by=' + order_by

        if page:
            redirect_to = redirect_to + '&page=' + page

        variable = self.request.REQUEST.get('next', '').split("?")
        if len(variable) > 1:

            if variable[1].split("=")[0] == 'page':
                page = self.request.REQUEST.get('next', '').split("?")[1].split("=")[1]
            elif variable[1].split("=")[0] == 'order_by':
                order_by = self.request.REQUEST.get('next', '').split("?")[1].split("=")[1]

        if order_by:
            lista_ciudad = Ciudad.objects.all().order_by(order_by)
        else:
            lista_ciudad = Ciudad.objects.all()

        paginator = Paginator(lista_ciudad, nropag)
        # Show 25 contacts per page

        if page == '0':
            ciudades = lista_ciudad
        else:
            try:
                ciudades = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                ciudades = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                ciudades = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(ciudades.object_list[i].id == ciudad.id):
                    if ciudades.has_previous:
                        try:
                            previousitem = ciudades.object_list[i-1].id
                        except:
                            previousitem = None

                    if ciudades.has_next:
                        try:
                            nextitem = ciudades.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(ciudades)
            for i in range(0, countitem):
                if(ciudades[i].id == ciudad.id):
                    try:
                        previousitem = ciudades[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = ciudades[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            ciudad_previous = Ciudad.objects.get(pk=previousitem)
        except:
            ciudad_previous = None
        try:
            ciudad_next = Ciudad.objects.get(pk=nextitem)
        except:
            ciudad_next = None

        context['ciudad_previous'] = ciudad_previous
        context['ciudad_next'] = ciudad_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Ciudad '" + str(self.object) + "'  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Ciudad '" + str(self.object) + "' guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                return render_to_response(self.template_name, self.get_context_data())


class CiudadDelete(DeleteView):
    model = Ciudad
    form_class = CiudadForm
    template_name = 'server_confirm_delete.html'

    @transaction.atomic
    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        context = self.obj.id

        order_by = self.request.REQUEST.get('order_by', '')
        page = self.request.REQUEST.get('page', '')
        next = self.request.REQUEST.get('next', '')
        variable = self.request.REQUEST.get('next', '').split("?")
        if len(variable) > 1:

            if variable[1].split("=")[0] == 'ficha':
                next = variable[0]
                if order_by and page:
                    next = next + '?order_by=' + order_by + '&page='+ page
                elif order_by:
                    next = next + '?order_by=' + order_by
                elif page:
                    next = next + '?page=' + page
            elif variable[1].split("=")[0] == 'page':
                if order_by:
                    next = next + '&order_by=' + order_by
            elif variable[1].split("=")[0] == 'order_by':
                if page:
                    next = next + '&page=' + page

        self.obj.delete()
        messages.success(self.request, "Ciudad " + str(self.obj) + " eliminado con éxito.", extra_tags=next)
        return render(request, '../../mensaje/templates/mensaje.html', {'obj': context})


# app barrio
class BarrioListView(ListView):
    model = Barrio
    paginate_by = 10
    context_object_name = 'barrios'
    template_name = 'barrio_lista.html'

    def get_paginate_by(self, queryset):
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        page = self.request.GET.get('page')
        if page == '0':
            return None
        else:
            return self.request.GET.get('paginate_by', nropag)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BarrioListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")
        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['barrio',
                                             'provincia__provincia',
                                             'pais__pais',
                                             'ciudad__ciudad', ])

            lista_barrio = Barrio.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['barrio',
                                             'provincia__provincia',
                                             'pais__pais',
                                             'ciudad__ciudad', ])

            lista_barrio = Barrio.objects.filter(entry_query)
        elif order_by:
            lista_barrio = Barrio.objects.all().order_by(order_by)
        else:
            lista_barrio = Barrio.objects.all()

        paginator = Paginator(lista_barrio, 10)
        page = self.request.GET.get('page')
        if page:

            if int(page) > int(range_gap):
                start = int(page)-int(range_gap)
            else:
                start = 1

            if int(page) < paginator.num_pages-int(range_gap):
                end = int(page)+int(range_gap)+1
            else:
                end = paginator.num_pages+1
        else:
            if 1 > int(range_gap):
                start = 1-int(range_gap)
            else:
                start = 1

            if 1 < paginator.num_pages-int(range_gap):
                end = 1+int(range_gap)+1
            else:
                end = paginator.num_pages+1

        context['ultimo'] = str(paginator.num_pages)
        context['page_range2'] = range(start, end)
        return context

    def get_queryset(self):

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['barrio',
                                             'provincia__provincia',
                                             'pais__pais',
                                             'ciudad__ciudad', ])

            queryset = Barrio.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['barrio',
                                             'provincia__provincia',
                                             'pais__pais',
                                             'ciudad__ciudad', ])

            queryset = Barrio.objects.filter(entry_query)
        elif order_by:
            queryset = Barrio.objects.all().order_by(order_by)
        else:
            queryset = Barrio.objects.all()

        return queryset


class BarrioView(View):
    form_class = BarrioForm
    template_name = 'barrio_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Barrio '" + str(id_reg) + "' registrado con éxito.",
                                 extra_tags=reverse('udirecciones:list_barrio'))
                return HttpResponseRedirect(reverse('udirecciones:edit_barrio',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Barrio '" + str(id_reg) + "' registrado con éxito.")
                return HttpResponseRedirect(reverse('udirecciones:list_barrio'))

        return render(request, self.template_name, {'form': form})


class BarrioUpdate(UpdateView):
    template_name = 'barrio_edit.html'
    form_class = BarrioForm
    model = Barrio

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BarrioUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        barrio = Barrio.objects.get(pk=self.object.pk)
        redirect_to = self.request.REQUEST.get('next', '')
        order_by = self.request.REQUEST.get('order_by', '')
        page = self.request.REQUEST.get('page', '')

        if order_by:
            redirect_to = redirect_to + '&order_by=' + order_by

        if page:
            redirect_to = redirect_to + '&page=' + page

        variable = self.request.REQUEST.get('next', '').split("?")
        if len(variable) > 1:

            if variable[1].split("=")[0] == 'page':
                page = self.request.REQUEST.get('next', '').split("?")[1].split("=")[1]
            elif variable[1].split("=")[0] == 'order_by':
                order_by = self.request.REQUEST.get('next', '').split("?")[1].split("=")[1]

        if order_by:
            lista_barrio = Barrio.objects.all().order_by(order_by)
        else:
            lista_barrio = Barrio.objects.all()

        paginator = Paginator(lista_barrio, nropag)
        # Show 25 contacts per page

        if page == '0':
            barrios = lista_barrio
        else:
            try:
                barrios = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                barrios = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                barrios = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(barrios.object_list[i].id == barrio.id):
                    if barrios.has_previous:
                        try:
                            previousitem = barrios.object_list[i-1].id
                        except:
                            previousitem = None

                    if barrios.has_next:
                        try:
                            nextitem = barrios.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(barrios)
            for i in range(0, countitem):
                if(barrios[i].id == barrio.id):
                    try:
                        previousitem = barrios[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = barrios[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            barrio_previous = Barrio.objects.get(pk=previousitem)
        except:
            barrio_previous = None
        try:
            barrio_next = Barrio.objects.get(pk=nextitem)
        except:
            barrio_next = None

        context['barrio_previous'] = barrio_previous
        context['barrio_next'] = barrio_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Barrio '" + str(self.object) + "' guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Barrio '" + str(self.object) + "' guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                return render_to_response(self.template_name, self.get_context_data())


class BarrioDelete(DeleteView):
    model = Barrio
    form_class = BarrioForm
    template_name = 'server_confirm_delete.html'

    @transaction.atomic
    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        context = self.obj.id

        order_by = self.request.REQUEST.get('order_by', '')
        page = self.request.REQUEST.get('page', '')
        next = self.request.REQUEST.get('next', '')
        variable = self.request.REQUEST.get('next', '').split("?")
        if len(variable) > 1:

            if variable[1].split("=")[0] == 'ficha':
                next = variable[0]
                if order_by and page:
                    next = next + '?order_by=' + order_by + '&page='+ page
                elif order_by:
                    next = next + '?order_by=' + order_by
                elif page:
                    next = next + '?page=' + page
            elif variable[1].split("=")[0] == 'page':
                if order_by:
                    next = next + '&order_by=' + order_by
            elif variable[1].split("=")[0] == 'order_by':
                if page:
                    next = next + '&page=' + page

        self.obj.delete()
        messages.success(self.request, "Barrio " + str(self.obj) + " eliminado con éxito.", extra_tags=next)
        return render(request, '../../mensaje/templates/mensaje.html', {'obj': context})


# app direccion
class DireccionListView(ListView):
    model = Direccion
    paginate_by = 10
    context_object_name = 'direcciones'
    template_name = 'direccion_lista.html'

    def get_paginate_by(self, queryset):
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        page = self.request.GET.get('page')
        if page == '0':
            return None
        else:
            return self.request.GET.get('paginate_by', nropag)

    def get_queryset(self):

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['calle',
                                             'altura',
                                             'barrio__barrio',
                                             'ciudad__ciudad',
                                             'zip',
                                             'provincia__provincia',
                                             'pais__pais',
                                             'punto_de_referencia', ])

            queryset = Direccion.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['calle',
                                             'altura',
                                             'barrio__barrio',
                                             'ciudad__ciudad',
                                             'zip',
                                             'provincia__provincia',
                                             'pais__pais',
                                             'punto_de_referencia', ])

            queryset = Direccion.objects.filter(entry_query)
        elif order_by:
            queryset = Direccion.objects.all().order_by(order_by)
        else:
            queryset = Direccion.objects.all()

        return queryset


class DireccionView(View):
    form_class = DireccionForm
    template_name = 'direccion_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            # <process form cleaned data>
            messages.success(self.request, "Direccion registrada.")
            return HttpResponseRedirect(reverse('udirecciones:DireccionListView'))

        return render(request, self.template_name, {'form': form})


class DireccionUpdate(UpdateView):
    template_name = 'direccion_edit.html'
    form_class = DireccionForm
    model = Direccion

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        redirect_to = self.request.GET['next']
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app tipo de edificación
class TipoDeEdificacionListView(ListView):
    model = TipoDeEdificacion
    paginate_by = 10
    context_object_name = 'tiposdeedificaciones'
    template_name = 'tipodeedificacion_lista.html'

    def get_paginate_by(self, queryset):
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        page = self.request.GET.get('page')
        if page == '0':
            return None
        else:
            return self.request.GET.get('paginate_by', nropag)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TipoDeEdificacionListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")
        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_edificacion',
                                             'descripcion', ])

            lista_tipodeedificacion = TipoDeEdificacion.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_edificacion',
                                             'descripcion', ])

            lista_tipodeedificacion = TipoDeEdificacion.objects.filter(entry_query)
        elif order_by:
            lista_tipodeedificacion = TipoDeEdificacion.objects.all().order_by(order_by)
        else:
            lista_tipodeedificacion = TipoDeEdificacion.objects.all()

        paginator = Paginator(lista_tipodeedificacion, 10)
        page = self.request.GET.get('page')
        if page:

            if int(page) > int(range_gap):
                start = int(page)-int(range_gap)
            else:
                start = 1

            if int(page) < paginator.num_pages-int(range_gap):
                end = int(page)+int(range_gap)+1
            else:
                end = paginator.num_pages+1
        else:
            if 1 > int(range_gap):
                start = 1-int(range_gap)
            else:
                start = 1

            if 1 < paginator.num_pages-int(range_gap):
                end = 1+int(range_gap)+1
            else:
                end = paginator.num_pages+1

        context['ultimo'] = str(paginator.num_pages)
        context['page_range2'] = range(start, end)
        return context

    def get_queryset(self):

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_edificacion',
                                             'descripcion', ])

            queryset = TipoDeEdificacion.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_edificacion',
                                             'descripcion', ])

            queryset = TipoDeEdificacion.objects.filter(entry_query)
        elif order_by:
            queryset = TipoDeEdificacion.objects.all().order_by(order_by)
        else:
            queryset = TipoDeEdificacion.objects.all()

        return queryset


class TipoDeEdificacionView(View):
    form_class = TipoDeEdificacionForm
    template_name = 'tipodeedificacion_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Tipo de edificación '" + str(id_reg) + "' agregado con éxito.",
                                 extra_tags=reverse('udirecciones:list_tipo_de_edificacion'))
                return HttpResponseRedirect(reverse('udirecciones:edit_tipo_de_edificacion',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Tipo de edificación '" + str(id_reg) + "' agregado con éxito.")
                return HttpResponseRedirect(reverse('udirecciones:list_tipo_de_edificacion'))

        return render(request, self.template_name, {'form': form})


class TipoDeEdificacionUpdate(UpdateView):
    template_name = 'tipodeedificacion_edit.html'
    form_class = TipoDeEdificacionForm
    model = TipoDeEdificacion

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TipoDeEdificacionUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        tipodeedificacion = TipoDeEdificacion.objects.get(pk=self.object.pk)
        redirect_to = self.request.REQUEST.get('next', '')
        order_by = self.request.REQUEST.get('order_by', '')
        page = self.request.REQUEST.get('page', '')

        if order_by:
            redirect_to = redirect_to + '&order_by=' + order_by

        if page:
            redirect_to = redirect_to + '&page=' + page

        variable = self.request.REQUEST.get('next', '').split("?")
        if len(variable) > 1:

            if variable[1].split("=")[0] == 'page':
                page = self.request.REQUEST.get('next', '').split("?")[1].split("=")[1]
            elif variable[1].split("=")[0] == 'order_by':
                order_by = self.request.REQUEST.get('next', '').split("?")[1].split("=")[1]

        if order_by:
            lista_tipodeedificacion = TipoDeEdificacion.objects.all().order_by(order_by)
        else:
            lista_tipodeedificacion = TipoDeEdificacion.objects.all()

        paginator = Paginator(lista_tipodeedificacion, nropag)
        # Show 25 contacts per page

        if page == '0':
            tiposdeedificaciones = lista_tipodeedificacion
        else:
            try:
                tiposdeedificaciones = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                tiposdeedificaciones = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                tiposdeedificaciones = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(tiposdeedificaciones.object_list[i].id == tipodeedificacion.id):
                    if tiposdeedificaciones.has_previous:
                        try:
                            previousitem = tiposdeedificaciones.object_list[i-1].id
                        except:
                            previousitem = None

                    if tiposdeedificaciones.has_next:
                        try:
                            nextitem = tiposdeedificaciones.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(tiposdeedificaciones)
            for i in range(0, countitem):
                if(tiposdeedificaciones[i].id == tipodeedificacion.id):
                    try:
                        previousitem = tiposdeedificaciones[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = tiposdeedificaciones[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            tipodeedificacion_previous = TipoDeEdificacion.objects.get(pk=previousitem)
        except:
            tipodeedificacion_previous = None
        try:
            tipodeedificacion_next = TipoDeEdificacion.objects.get(pk=nextitem)
        except:
            tipodeedificacion_next = None

        context['tipodeedificacion_previous'] = tipodeedificacion_previous
        context['tipodeedificacion_next'] = tipodeedificacion_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Tipo de edificación '" + str(self.object) + "' guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Tipo de edificación '" + str(self.object) + "' guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                return render_to_response(self.template_name, self.get_context_data())


class TipoDeEdificacionDelete(DeleteView):
    model = TipoDeEdificacion
    form_class = TipoDeEdificacionForm
    template_name = 'server_confirm_delete.html'

    @transaction.atomic
    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        context = self.obj.id

        order_by = self.request.REQUEST.get('order_by', '')
        page = self.request.REQUEST.get('page', '')
        next = self.request.REQUEST.get('next', '')
        variable = self.request.REQUEST.get('next', '').split("?")
        if len(variable) > 1:

            if variable[1].split("=")[0] == 'ficha':
                next = variable[0]
                if order_by and page:
                    next = next + '?order_by=' + order_by + '&page='+ page
                elif order_by:
                    next = next + '?order_by=' + order_by
                elif page:
                    next = next + '?page=' + page
            elif variable[1].split("=")[0] == 'page':
                if order_by:
                    next = next + '&order_by=' + order_by
            elif variable[1].split("=")[0] == 'order_by':
                if page:
                    next = next + '&page=' + page

        self.obj.delete()
        messages.success(self.request, "Tipo de edificación " + str(self.obj) + " eliminado con éxito.", extra_tags=next)
        return render(request, '../../mensaje/templates/mensaje.html', {'obj': context})


# app tipo de ascensor
class TipoDeAscensorListView(ListView):
    model = TipoDeAscensorForm
    paginate_by = 10
    context_object_name = 'tiposdeascensores'
    template_name = 'tipodeascensor_lista.html'

    def get_paginate_by(self, queryset):
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        page = self.request.GET.get('page')
        if page == '0':
            return None
        else:
            return self.request.GET.get('paginate_by', nropag)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TipoDeAscensorListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")
        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_ascensor',
                                             'descripcion', ])

            lista_tipodeascensor = TipoDeAscensor.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_ascensor',
                                             'descripcion', ])

            lista_tipodeascensor = TipoDeAscensor.objects.filter(entry_query)
        elif order_by:
            lista_tipodeascensor = TipoDeAscensor.objects.all().order_by(order_by)
        else:
            lista_tipodeascensor = TipoDeAscensor.objects.all()

        paginator = Paginator(lista_tipodeascensor, 10)
        page = self.request.GET.get('page')
        if page:

            if int(page) > int(range_gap):
                start = int(page)-int(range_gap)
            else:
                start = 1

            if int(page) < paginator.num_pages-int(range_gap):
                end = int(page)+int(range_gap)+1
            else:
                end = paginator.num_pages+1
        else:
            if 1 > int(range_gap):
                start = 1-int(range_gap)
            else:
                start = 1

            if 1 < paginator.num_pages-int(range_gap):
                end = 1+int(range_gap)+1
            else:
                end = paginator.num_pages+1

        context['ultimo'] = str(paginator.num_pages)
        context['page_range2'] = range(start, end)
        return context

    def get_queryset(self):

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_ascensor',
                                             'descripcion', ])

            queryset = TipoDeAscensor.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_ascensor',
                                             'descripcion', ])

            queryset = TipoDeAscensor.objects.filter(entry_query)
        elif order_by:
            queryset = TipoDeAscensor.objects.all().order_by(order_by)
        else:
            queryset = TipoDeAscensor.objects.all()

        return queryset


class TipoDeAscensorView(View):
    form_class = TipoDeAscensorForm
    template_name = 'tipodeascensor_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Tipo de ascensor '" + str(id_reg) + "' agregado con éxito.",
                                 extra_tags=reverse('udirecciones:list_tipo_de_ascensor'))
                return HttpResponseRedirect(reverse('udirecciones:edit_tipo_de_ascensor',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Tipo de ascensor '" + str(id_reg) + "' agregado con éxito.")
                return HttpResponseRedirect(reverse('udirecciones:list_tipo_de_ascensor'))

        return render(request, self.template_name, {'form': form})


class TipoDeAscensorUpdate(UpdateView):
    template_name = 'tipodeascensor_edit.html'
    form_class = TipoDeAscensorForm
    model = TipoDeAscensor

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TipoDeAscensorUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        tipodeascensor = TipoDeAscensor.objects.get(pk=self.object.pk)
        redirect_to = self.request.REQUEST.get('next', '')
        order_by = self.request.REQUEST.get('order_by', '')
        page = self.request.REQUEST.get('page', '')

        if order_by:
            redirect_to = redirect_to + '&order_by=' + order_by

        if page:
            redirect_to = redirect_to + '&page=' + page

        variable = self.request.REQUEST.get('next', '').split("?")
        if len(variable) > 1:

            if variable[1].split("=")[0] == 'page':
                page = self.request.REQUEST.get('next', '').split("?")[1].split("=")[1]
            elif variable[1].split("=")[0] == 'order_by':
                order_by = self.request.REQUEST.get('next', '').split("?")[1].split("=")[1]

        if order_by:
            lista_tipodeascensor = TipoDeAscensor.objects.all().order_by(order_by)
        else:
            lista_tipodeascensor = TipoDeAscensor.objects.all()

        paginator = Paginator(lista_tipodeascensor, nropag)
        # Show 25 contacts per page

        if page == '0':
            tiposdeascensores = lista_tipodeascensor
        else:
            try:
                tiposdeascensores = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                tiposdeascensores = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                tiposdeascensores = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(tiposdeascensores.object_list[i].id == tipodeascensor.id):
                    if tiposdeascensores.has_previous:
                        try:
                            previousitem = tiposdeascensores.object_list[i-1].id
                        except:
                            previousitem = None

                    if tiposdeascensores.has_next:
                        try:
                            nextitem = tiposdeascensores.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(tiposdeascensores)
            for i in range(0, countitem):
                if(tiposdeascensores[i].id == tipodeascensor.id):
                    try:
                        previousitem = tiposdeascensores[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = tiposdeascensores[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            tipodeascensor_previous = TipoDeAscensor.objects.get(pk=previousitem)
        except:
            tipodeascensor_previous = None
        try:
            tipodeascensor_next = TipoDeAscensor.objects.get(pk=nextitem)
        except:
            tipodeascensor_next = None

        context['tipodeascensor_previous'] = tipodeascensor_previous
        context['tipodeascensor_next'] = tipodeascensor_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Tipo de ascensor '" + str(self.object) + "' guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Tipo de ascensor '" + str(self.object) + "' guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                return render_to_response(self.template_name, self.get_context_data())


class TipoDeAscensorDelete(DeleteView):
    model = TipoDeAscensor
    form_class = TipoDeAscensorForm
    template_name = 'server_confirm_delete.html'

    @transaction.atomic
    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        context = self.obj.id

        order_by = self.request.REQUEST.get('order_by', '')
        page = self.request.REQUEST.get('page', '')
        next = self.request.REQUEST.get('next', '')
        variable = self.request.REQUEST.get('next', '').split("?")
        if len(variable) > 1:

            if variable[1].split("=")[0] == 'ficha':
                next = variable[0]
                if order_by and page:
                    next = next + '?order_by=' + order_by + '&page='+ page
                elif order_by:
                    next = next + '?order_by=' + order_by
                elif page:
                    next = next + '?page=' + page
            elif variable[1].split("=")[0] == 'page':
                if order_by:
                    next = next + '&order_by=' + order_by
            elif variable[1].split("=")[0] == 'order_by':
                if page:
                    next = next + '&page=' + page

        self.obj.delete()
        messages.success(self.request, "Tipo de ascensor " + str(self.obj) + " eliminado con éxito.", extra_tags=next)
        return render(request, '../../mensaje/templates/mensaje.html', {'obj': context})


# app tipo de inmueble
class TipoDeInmuebleListView(ListView):
    model = TipoDeInmuebleForm
    paginate_by = 10
    context_object_name = 'tiposdeinmuebles'
    template_name = 'tipodeinmueble_lista.html'

    def get_paginate_by(self, queryset):
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        page = self.request.GET.get('page')
        if page == '0':
            return None
        else:
            return self.request.GET.get('paginate_by', nropag)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TipoDeInmuebleListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")
        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_inmueble',
                                             'descripcion', ])

            lista_tipodeinmueble = TipoDeInmueble.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_inmueble',
                                             'descripcion', ])

            lista_tipodeinmueble = TipoDeInmueble.objects.filter(entry_query)
        elif order_by:
            lista_tipodeinmueble = TipoDeInmueble.objects.all().order_by(order_by)
        else:
            lista_tipodeinmueble = TipoDeInmueble.objects.all()

        paginator = Paginator(lista_tipodeinmueble, 10)
        page = self.request.GET.get('page')
        if page:

            if int(page) > int(range_gap):
                start = int(page)-int(range_gap)
            else:
                start = 1

            if int(page) < paginator.num_pages-int(range_gap):
                end = int(page)+int(range_gap)+1
            else:
                end = paginator.num_pages+1
        else:
            if 1 > int(range_gap):
                start = 1-int(range_gap)
            else:
                start = 1

            if 1 < paginator.num_pages-int(range_gap):
                end = 1+int(range_gap)+1
            else:
                end = paginator.num_pages+1

        context['ultimo'] = str(paginator.num_pages)
        context['page_range2'] = range(start, end)
        return context

    def get_queryset(self):

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_inmueble',
                                             'descripcion', ])

            queryset = TipoDeInmueble.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_inmueble',
                                             'descripcion', ])

            queryset = TipoDeInmueble.objects.filter(entry_query)
        elif order_by:
            queryset = TipoDeInmueble.objects.all().order_by(order_by)
        else:
            queryset = TipoDeInmueble.objects.all()

        return queryset


class TipoDeInmuebleView(View):
    form_class = TipoDeInmuebleForm
    template_name = 'tipodeinmueble_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Tipo de inmueble '" + str(id_reg) + "' agregado con éxito.",
                                 extra_tags=reverse('udirecciones:list_tipo_de_inmueble'))
                return HttpResponseRedirect(reverse('udirecciones:edit_tipo_de_inmueble',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Tipo de inmueble '" + str(id_reg) + "' agregado con éxito.")
                return HttpResponseRedirect(reverse('udirecciones:list_tipo_de_inmueble'))

        return render(request, self.template_name, {'form': form})


class TipoDeInmuebleUpdate(UpdateView):
    template_name = 'tipodeinmueble_edit.html'
    form_class = TipoDeInmuebleForm
    model = TipoDeInmueble

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TipoDeInmuebleUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        tipodeinmueble = TipoDeInmueble.objects.get(pk=self.object.pk)
        redirect_to = self.request.REQUEST.get('next', '')
        order_by = self.request.REQUEST.get('order_by', '')
        page = self.request.REQUEST.get('page', '')

        if order_by:
            redirect_to = redirect_to + '&order_by=' + order_by

        if page:
            redirect_to = redirect_to + '&page=' + page

        variable = self.request.REQUEST.get('next', '').split("?")
        if len(variable) > 1:

            if variable[1].split("=")[0] == 'page':
                page = self.request.REQUEST.get('next', '').split("?")[1].split("=")[1]
            elif variable[1].split("=")[0] == 'order_by':
                order_by = self.request.REQUEST.get('next', '').split("?")[1].split("=")[1]

        if order_by:
            lista_tipodeinmueble = TipoDeInmueble.objects.all().order_by(order_by)
        else:
            lista_tipodeinmueble = TipoDeInmueble.objects.all()

        paginator = Paginator(lista_tipodeinmueble, nropag)
        # Show 25 contacts per page

        if page == '0':
            tiposdeinmuebles = lista_tipodeinmueble
        else:
            try:
                tiposdeinmuebles = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                tiposdeinmuebles = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                tiposdeinmuebles = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(tiposdeinmuebles.object_list[i].id == tipodeinmueble.id):
                    if tiposdeinmuebles.has_previous:
                        try:
                            previousitem = tiposdeinmuebles.object_list[i-1].id
                        except:
                            previousitem = None

                    if tiposdeinmuebles.has_next:
                        try:
                            nextitem = tiposdeinmuebles.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(tiposdeinmuebles)
            for i in range(0, countitem):
                if(tiposdeinmuebles[i].id == tipodeinmueble.id):
                    try:
                        previousitem = tiposdeinmuebles[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = tiposdeinmuebles[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            tipodeinmueble_previous = TipoDeInmueble.objects.get(pk=previousitem)
        except:
            tipodeinmueble_previous = None
        try:
            tipodeinmueble_next = TipoDeInmueble.objects.get(pk=nextitem)
        except:
            tipodeinmueble_next = None

        context['tipodeinmueble_previous'] = tipodeinmueble_previous
        context['tipodeinmueble_next'] = tipodeinmueble_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Tipo de inmueble '" + str(self.object) + "' guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Tipo de inmueble '" + str(self.object) + "' guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                return render_to_response(self.template_name, self.get_context_data())


class TipoDeInmuebleDelete(DeleteView):
    model = TipoDeInmueble
    form_class = TipoDeInmuebleForm
    template_name = 'server_confirm_delete.html'

    @transaction.atomic
    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        context = self.obj.id

        order_by = self.request.REQUEST.get('order_by', '')
        page = self.request.REQUEST.get('page', '')
        next = self.request.REQUEST.get('next', '')
        variable = self.request.REQUEST.get('next', '').split("?")
        if len(variable) > 1:

            if variable[1].split("=")[0] == 'ficha':
                next = variable[0]
                if order_by and page:
                    next = next + '?order_by=' + order_by + '&page='+ page
                elif order_by:
                    next = next + '?order_by=' + order_by
                elif page:
                    next = next + '?page=' + page
            elif variable[1].split("=")[0] == 'page':
                if order_by:
                    next = next + '&order_by=' + order_by
            elif variable[1].split("=")[0] == 'order_by':
                if page:
                    next = next + '&page=' + page

        self.obj.delete()
        messages.success(self.request, "Tipo de inmueble " + str(self.obj) + " eliminado con éxito.", extra_tags=next)
        return render(request, '../../mensaje/templates/mensaje.html', {'obj': context})


# app especificacion de inmueble
class EspecificacionDeInmuebleListView(ListView):
    model = EspecificacionDeInmuebleForm
    paginate_by = 10
    context_object_name = 'especificacionesdeinmuebles'
    template_name = 'especificaciondeinmueble_lista.html'

    def get_paginate_by(self, queryset):
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        page = self.request.GET.get('page')
        if page == '0':
            return None
        else:
            return self.request.GET.get('paginate_by', nropag)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(EspecificacionDeInmuebleListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")
        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_inmueble__tipo_de_inmueble',
                                             'descripcion',
                                             'especificacion_de_inmueble', ])

            lista_especificaciondeinmueble = EspecificacionDeInmueble.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_inmueble__tipo_de_inmueble',
                                             'descripcion',
                                             'especificacion_de_inmueble', ])

            lista_especificaciondeinmueble = EspecificacionDeInmueble.objects.filter(entry_query)
        elif order_by:
            lista_especificaciondeinmueble = EspecificacionDeInmueble.objects.all().order_by(order_by)
        else:
            lista_especificaciondeinmueble = EspecificacionDeInmueble.objects.all()

        paginator = Paginator(lista_especificaciondeinmueble, 10)
        page = self.request.GET.get('page')
        if page:

            if int(page) > int(range_gap):
                start = int(page)-int(range_gap)
            else:
                start = 1

            if int(page) < paginator.num_pages-int(range_gap):
                end = int(page)+int(range_gap)+1
            else:
                end = paginator.num_pages+1
        else:
            if 1 > int(range_gap):
                start = 1-int(range_gap)
            else:
                start = 1

            if 1 < paginator.num_pages-int(range_gap):
                end = 1+int(range_gap)+1
            else:
                end = paginator.num_pages+1

        context['ultimo'] = str(paginator.num_pages)
        context['page_range2'] = range(start, end)
        return context

    def get_queryset(self):

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_inmueble__tipo_de_inmueble',
                                             'descripcion',
                                             'especificacion_de_inmueble', ])

            queryset = EspecificacionDeInmueble.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_inmueble__tipo_de_inmueble',
                                             'descripcion',
                                             'especificacion_de_inmueble', ])

            queryset = EspecificacionDeInmueble.objects.filter(entry_query)
        elif order_by:
            queryset = EspecificacionDeInmueble.objects.all().order_by(order_by)
        else:
            queryset = EspecificacionDeInmueble.objects.all()

        return queryset


class EspecificacionDeInmuebleView(View):
    form_class = EspecificacionDeInmuebleForm
    template_name = 'especificaciondeinmueble_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Especificación de inmueble '" + str(id_reg) + "' agregado con éxito.",
                                 extra_tags=reverse('udirecciones:list_especificaciondeinmueble'))
                return HttpResponseRedirect(reverse('udirecciones:edit_especificaciondeinmueble',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Especificación de inmueble '" + str(id_reg) + "' agregado con éxito.")
                return HttpResponseRedirect(reverse('udirecciones:list_especificaciondeinmueble'))

        return render(request, self.template_name, {'form': form})


class EspecificacionDeInmuebleUpdate(UpdateView):
    template_name = 'especificaciondeinmueble_edit.html'
    form_class = EspecificacionDeInmuebleForm
    model = EspecificacionDeInmueble

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(EspecificacionDeInmuebleUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        especificaciondeinmueble = EspecificacionDeInmueble.objects.get(pk=self.object.pk)
        redirect_to = self.request.REQUEST.get('next', '')
        order_by = self.request.REQUEST.get('order_by', '')
        page = self.request.REQUEST.get('page', '')

        if order_by:
            redirect_to = redirect_to + '&order_by=' + order_by

        if page:
            redirect_to = redirect_to + '&page=' + page

        variable = self.request.REQUEST.get('next', '').split("?")
        if len(variable) > 1:

            if variable[1].split("=")[0] == 'page':
                page = self.request.REQUEST.get('next', '').split("?")[1].split("=")[1]
            elif variable[1].split("=")[0] == 'order_by':
                order_by = self.request.REQUEST.get('next', '').split("?")[1].split("=")[1]

        if order_by:
            lista_especificaciondeinmueble = EspecificacionDeInmueble.objects.all().order_by(order_by)
        else:
            lista_especificaciondeinmueble = EspecificacionDeInmueble.objects.all()

        paginator = Paginator(lista_especificaciondeinmueble, nropag)
        # Show 25 contacts per page

        if page == '0':
            especificacionesdeinmuebles = lista_especificaciondeinmueble
        else:
            try:
                especificacionesdeinmuebles = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                especificacionesdeinmuebles = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                especificacionesdeinmuebles = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(especificacionesdeinmuebles.object_list[i].id == especificaciondeinmueble.id):
                    if especificacionesdeinmuebles.has_previous:
                        try:
                            previousitem = especificacionesdeinmuebles.object_list[i-1].id
                        except:
                            previousitem = None

                    if especificacionesdeinmuebles.has_next:
                        try:
                            nextitem = especificacionesdeinmuebles.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(especificacionesdeinmuebles)
            for i in range(0, countitem):
                if(especificacionesdeinmuebles[i].id == especificaciondeinmueble.id):
                    try:
                        previousitem = especificacionesdeinmuebles[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = especificacionesdeinmuebles[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            especificaciondeinmueble_previous = EspecificacionDeInmueble.objects.get(pk=previousitem)
        except:
            especificaciondeinmueble_previous = None
        try:
            especificaciondeinmueble_next = EspecificacionDeInmueble.objects.get(pk=nextitem)
        except:
            especificaciondeinmueble_next = None

        context['especificaciondeinmueble_previous'] = especificaciondeinmueble_previous
        context['especificaciondeinmueble_next'] = especificaciondeinmueble_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Especificación de inmueble " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return render_to_response(self.template_name, self.get_context_data())


class EspecificacionDeInmuebleDelete(DeleteView):
    model = EspecificacionDeInmueble
    form_class = EspecificacionDeInmuebleForm
    template_name = 'server_confirm_delete.html'

    @transaction.atomic
    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        context = self.obj.id

        order_by = self.request.REQUEST.get('order_by', '')
        page = self.request.REQUEST.get('page', '')
        next = self.request.REQUEST.get('next', '')
        variable = self.request.REQUEST.get('next', '').split("?")
        if len(variable) > 1:

            if variable[1].split("=")[0] == 'ficha':
                next = variable[0]
                if order_by and page:
                    next = next + '?order_by=' + order_by + '&page='+ page
                elif order_by:
                    next = next + '?order_by=' + order_by
                elif page:
                    next = next + '?page=' + page
            elif variable[1].split("=")[0] == 'page':
                if order_by:
                    next = next + '&order_by=' + order_by
            elif variable[1].split("=")[0] == 'order_by':
                if page:
                    next = next + '&page=' + page

        self.obj.delete()
        messages.success(self.request, "Especificación de inmueble " + str(self.obj) + " eliminado con éxito.", extra_tags=next)
        return render(request, '../../mensaje/templates/mensaje.html', {'obj': context})
