"""
Docstring documentación pendiente

"""

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.generic import ListView, View, UpdateView, DeleteView
from trabajador.models import CargoTrabajador, Trabajador, \
    TrabajadorEstadoDeRegistro
from trabajador.forms import CargoTrabajadorForm, TrabajadorForm
from estadoderegistro.models import EstadoDeRegistro
from mtvmcotizacionv02.views import valor_Personalizacionvisual, get_query
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# app trabajador
class TrabajadorListView(ListView):
    model = Trabajador
    paginate_by = 10
    context_object_name = 'trabajadores'
    template_name = 'trabajador_lista.html'

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
        context = super(TrabajadorListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['dni',
                                             'nombre',
                                             'apellido',
                                             'direccion',
                                             'telefono',
                                             'email',
                                             'volumen_en_camion',
                                             'cargo_trabajador__cargo_trabajador', ])
            lista_trabajador = Trabajador.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['dni',
                                             'nombre',
                                             'apellido',
                                             'direccion',
                                             'telefono',
                                             'email',
                                             'volumen_en_camion',
                                             'cargo_trabajador__cargo_trabajador', ])
            lista_trabajador = Trabajador.objects.filter(entry_query)
        elif order_by:
            lista_trabajador = Trabajador.objects.all().order_by(order_by)
        else:
            lista_trabajador = Trabajador.objects.all()

        paginator = Paginator(lista_trabajador, 10)
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
            entry_query = get_query(search, ['dni',
                                             'nombre',
                                             'apellido',
                                             'direccion',
                                             'telefono',
                                             'email',
                                             'volumen_en_camion',
                                             'cargo_trabajador__cargo_trabajador', ])
            queryset = Trabajador.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['dni',
                                             'nombre',
                                             'apellido',
                                             'direccion',
                                             'telefono',
                                             'email',
                                             'volumen_en_camion',
                                             'cargo_trabajador__cargo_trabajador', ])
            queryset = Trabajador.objects.filter(entry_query)
        elif order_by:
            queryset = Trabajador.objects.all().order_by(order_by)
        else:
            queryset = Trabajador.objects.all()

        return queryset


class TrabajadorView(View):
    form_class = TrabajadorForm
    template_name = 'trabajador_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            estadoactual = EstadoDeRegistro.objects.filter(model='trabajador',
                                                           estado__estado='Activo')

            agregarestado = TrabajadorEstadoDeRegistro.objects.create(trabajador=id_reg,
                                                                      estado_de_registro_id=estadoactual[0].id,
                                                                      usuario_id=2,
                                                                      observacion='Creación de trabajador',
                                                                      predefinido=True)
            agregarestado.save()

            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('utrabajadores:edit_trabajador',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('utrabajadores:list_trabajador'))

        return render(request, self.template_name, {'form': form})


class TrabajadorUpdate(UpdateView):
    template_name = 'trabajador_edit.html'
    form_class = TrabajadorForm
    model = Trabajador

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TrabajadorUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        trabajador = Trabajador.objects.get(pk=self.object.pk)
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
            lista_trabajador = Trabajador.objects.all().order_by(order_by)
        else:
            lista_trabajador = Trabajador.objects.all()

        paginator = Paginator(lista_trabajador, nropag)
        # Show 25 contacts per page

        if page == '0':
            trabajadores = lista_trabajador
        else:
            try:
                trabajadores = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                trabajadores = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                trabajadores = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(trabajadores.object_list[i].id == trabajador.id):
                    if trabajadores.has_previous:
                        try:
                            previousitem = trabajadores.object_list[i-1].id
                        except:
                            previousitem = None

                    if trabajadores.has_next:
                        try:
                            nextitem = trabajadores.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(trabajadores)
            for i in range(0, countitem):
                if(trabajadores[i].id == trabajador.id):
                    try:
                        previousitem = trabajadores[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = trabajadores[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            trabajador_previous = Trabajador.objects.get(pk=previousitem)
        except:
            trabajador_previous = None
        try:
            trabajador_next = Trabajador.objects.get(pk=nextitem)
        except:
            trabajador_next = None

        context['trabajador_previous'] = trabajador_previous
        context['trabajador_next'] = trabajador_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Trabajador " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('utrabajadores:list_trabajador'))
                #return render_to_response(self.template_name, self.get_context_data())


class TrabajadorDelete(DeleteView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app cargo trabajador
class CargoTrabajadorListView(ListView):
    model = CargoTrabajador
    paginate_by = 10
    context_object_name = 'cargotrabajadores'
    template_name = 'cargotrabajador_lista.html'

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
        context = super(CargoTrabajadorListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['cargo_trabajador',
                                             'descripcion',
                                             'cargo_padre__cargo_trabajador', ])
            lista_cargotrabajador = CargoTrabajador.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['cargo_trabajador',
                                             'descripcion',
                                             'cargo_padre__cargo_trabajador', ])
            lista_cargotrabajador = CargoTrabajador.objects.filter(entry_query)
        elif order_by:
            lista_cargotrabajador = CargoTrabajador.objects.all().order_by(order_by)
        else:
            lista_cargotrabajador = CargoTrabajador.objects.all()

        paginator = Paginator(lista_cargotrabajador, 10)
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
            entry_query = get_query(search, ['cargo_trabajador',
                                             'descripcion',
                                             'cargo_padre__cargo_trabajador', ])
            queryset = CargoTrabajador.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['cargo_trabajador',
                                             'descripcion',
                                             'cargo_padre__cargo_trabajador', ])
            queryset = CargoTrabajador.objects.filter(entry_query)
        elif order_by:
            queryset = CargoTrabajador.objects.all().order_by(order_by)
        else:
            queryset = CargoTrabajador.objects.all()

        return queryset


class CargoTrabajadorView(View):
    form_class = CargoTrabajadorForm
    template_name = 'cargotrabajador_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('utrabajadores:edit_cargotrabajador',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('utrabajadores:list_cargotrabajador'))

        return render(request, self.template_name, {'form': form})


class CargoTrabajadorUpdate(UpdateView):
    template_name = 'cargotrabajador_edit.html'
    form_class = CargoTrabajadorForm
    model = CargoTrabajador

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CargoTrabajadorUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        cargotrabajador = CargoTrabajador.objects.get(pk=self.object.pk)
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
            lista_cargotrabajador = CargoTrabajador.objects.all().order_by(order_by)
        else:
            lista_cargotrabajador = CargoTrabajador.objects.all()

        paginator = Paginator(lista_cargotrabajador, nropag)
        # Show 25 contacts per page

        if page == '0':
            cargotrabajadores = lista_cargotrabajador
        else:
            try:
                cargotrabajadores = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                cargotrabajadores = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                cargotrabajadores = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(cargotrabajadores.object_list[i].id == cargotrabajador.id):
                    if cargotrabajadores.has_previous:
                        try:
                            previousitem = cargotrabajadores.object_list[i-1].id
                        except:
                            previousitem = None

                    if cargotrabajadores.has_next:
                        try:
                            nextitem = cargotrabajadores.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(cargotrabajadores)
            for i in range(0, countitem):
                if(cargotrabajadores[i].id == cargotrabajador.id):
                    try:
                        previousitem = cargotrabajadores[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = cargotrabajadores[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            cargotrabajador_previous = CargoTrabajador.objects.get(pk=previousitem)
        except:
            cargotrabajador_previous = None
        try:
            cargotrabajador_next = CargoTrabajador.objects.get(pk=nextitem)
        except:
            cargotrabajador_next = None

        context['cargotrabajador_previous'] = cargotrabajador_previous
        context['cargotrabajador_next'] = cargotrabajador_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Cargo trabajador " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('utrabajadores:list_cargotrabajador'))
                #return render_to_response(self.template_name, self.get_context_data())


class CargoTrabajadorDelete(DeleteView):
    model = CargoTrabajador
    form_class = CargoTrabajadorForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())
