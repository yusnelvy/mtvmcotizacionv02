"""
Docstring documentación pendiente

"""

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.generic import ListView, View, UpdateView, DeleteView
from estadoderegistro.models import Estado, EstadoDeRegistro
from estadoderegistro.forms import EstadoForm, EstadoDeRegistroForm
from mtvmcotizacionv02.views import valor_Personalizacionvisual, get_query
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# app estado
class EstadoListView(ListView):
    model = Estado
    paginate_by = 10
    context_object_name = 'estados'
    template_name = 'estado_lista.html'

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
        context = super(EstadoListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")
        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['estado',
                                             'descripcion', ])

            lista_estado = Estado.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['estado',
                                             'descripcion', ])

            lista_estado = Estado.objects.filter(entry_query)
        elif order_by:
            lista_estado = Estado.objects.all().order_by(order_by)
        else:
            lista_estado = Estado.objects.all()

        paginator = Paginator(lista_estado, 10)
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
            entry_query = get_query(search, ['estado',
                                             'descripcion', ])

            queryset = Estado.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['estado',
                                             'descripcion', ])

            queryset = Estado.objects.filter(entry_query)
        elif order_by:
            queryset = Estado.objects.all().order_by(order_by)
        else:
            queryset = Estado.objects.all()

        return queryset


class EstadoView(View):
    form_class = EstadoForm
    template_name = 'estado_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Estado '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('uestadoderegistros:edit_estado',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Estado '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('uestadoderegistros:list_estado'))

        return render(request, self.template_name, {'form': form})


class EstadoUpdate(UpdateView):
    template_name = 'estado_edit.html'
    form_class = EstadoForm
    model = Estado

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(EstadoUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")
        #nropag = 10

        estado = Estado.objects.get(pk=self.object.pk)
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
            lista_estado = Estado.objects.all().order_by(order_by)
        else:
            lista_estado = Estado.objects.all()

        paginator = Paginator(lista_estado, nropag)
        # Show 25 contacts per page

        if page == '0':
            estados = lista_estado
        else:
            try:
                estados = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                estados = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                estados = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(estados.object_list[i].id == estado.id):
                    if estados.has_previous:
                        try:
                            previousitem = estados.object_list[i-1].id
                        except:
                            previousitem = None

                    if estados.has_next:
                        try:
                            nextitem = estados.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(estados)
            for i in range(0, countitem):
                if(estados[i].id == estado.id):
                    try:
                        previousitem = estados[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = estados[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            estado_previous = Estado.objects.get(pk=previousitem)
        except:
            estado_previous = None
        try:
            estado_next = Estado.objects.get(pk=nextitem)
        except:
            estado_next = None

        context['estado_previous'] = estado_previous
        context['estado_next'] = estado_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Estado '" + str(self.object) + "'  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Estado '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                return render_to_response(self.template_name, self.get_context_data())


class EstadoDelete(DeleteView):
    model = Estado
    form_class = EstadoForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            messages.success(self.request, "Estado '" + str(self.object) + "'  eliminado con éxito.")
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app estado de registro
class EstadoDeRegistroListView(ListView):
    model = EstadoDeRegistro
    paginate_by = 10
    context_object_name = 'estadosderegistro'
    template_name = 'estadoderegistro_lista.html'

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
        context = super(EstadoDeRegistroListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")
        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['estado__estado',
                                             'descripcion',
                                             'model', ])

            lista_estadoderegistro = EstadoDeRegistro.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['estado__estado',
                                             'descripcion',
                                             'model', ])

            lista_estadoderegistro = EstadoDeRegistro.objects.filter(entry_query)
        elif order_by:
            lista_estadoderegistro = EstadoDeRegistro.objects.all().order_by(order_by)
        else:
            lista_estadoderegistro = EstadoDeRegistro.objects.all()

        paginator = Paginator(lista_estadoderegistro, 10)
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
            entry_query = get_query(search, ['estado__estado',
                                             'descripcion',
                                             'model', ])

            queryset = EstadoDeRegistro.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['estado__estado',
                                             'descripcion',
                                             'model', ])

            queryset = EstadoDeRegistro.objects.filter(entry_query)
        elif order_by:
            queryset = EstadoDeRegistro.objects.all().order_by(order_by)
        else:
            queryset = EstadoDeRegistro.objects.all()

        return queryset


class EstadoDeRegistroView(View):
    form_class = EstadoDeRegistroForm
    template_name = 'estadoderegistro_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Estado de registro '" + str(id_reg) + "'  agregado con éxito.")
                return HttpResponseRedirect(reverse('uestadoderegistros:edit_estadoderegistro',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Estado de registro '" + str(id_reg) + "'  agregado con éxito.")
                return HttpResponseRedirect(reverse('uestadoderegistros:list_estadoderegistro'))

        return render(request, self.template_name, {'form': form})


class EstadoDeRegistroUpdate(UpdateView):
    template_name = 'estadoderegistro_edit.html'
    form_class = EstadoDeRegistroForm
    model = EstadoDeRegistro

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(EstadoDeRegistroUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")
        #nropag = 10

        estadoderegistro = EstadoDeRegistro.objects.get(pk=self.object.pk)
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
            lista_estadoderegistro = EstadoDeRegistro.objects.all().order_by(order_by)
        else:
            lista_estadoderegistro = EstadoDeRegistro.objects.all()

        paginator = Paginator(lista_estadoderegistro, nropag)
        # Show 25 contacts per page

        if page == '0':
            estadosdeRegistro = lista_estadoderegistro
        else:
            try:
                estadosdeRegistro = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                estadosdeRegistro = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                estadosdeRegistro = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(estadosdeRegistro.object_list[i].id == estadoderegistro.id):
                    if estadosdeRegistro.has_previous:
                        try:
                            previousitem = estadosdeRegistro.object_list[i-1].id
                        except:
                            previousitem = None

                    if estadosdeRegistro.has_next:
                        try:
                            nextitem = estadosdeRegistro.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(estadosdeRegistro)
            for i in range(0, countitem):
                if(estadosdeRegistro[i].id == estadoderegistro.id):
                    try:
                        previousitem = estadosdeRegistro[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = estadosdeRegistro[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            estadoderegistro_previous = EstadoDeRegistro.objects.get(pk=previousitem)
        except:
            estadoderegistro_previous = None
        try:
            estadoderegistro_next = EstadoDeRegistro.objects.get(pk=nextitem)
        except:
            estadoderegistro_next = None

        context['estadoderegistro_previous'] = estadoderegistro_previous
        context['estadoderegistro_next'] = estadoderegistro_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Estado de registro '" + str(self.object) + "'  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Estado de registro '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                return render_to_response(self.template_name, self.get_context_data())


class EstadoDeRegistroDelete(DeleteView):
    model = EstadoDeRegistro
    form_class = EstadoDeRegistroForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            messages.success(self.request, "Estado de registro '" + str(self.obj) + "'  eliminado con éxito.")
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())
