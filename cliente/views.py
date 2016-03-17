from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, View, UpdateView, \
    DeleteView, DetailView, CreateView
from cliente.models import Sexo, EstadoCivil, TipoDeCliente, \
    TipoDeRelacion, TipoDeInformacionDeContacto, Cliente, Contacto, \
    InformacionDeContacto, ClienteDireccion, ClienteEstadoDeRegistro, \
    Cliente
from cliente.forms import SexoForm, EstadoCivilForm, TipoDeClienteForm, \
    TipoDeRelacionForm, TipoDeInformacionDeContactoForm, ClienteForm, \
    ContactoForm, InformacionDeContactoForm, ClienteDireccionForm, \
    ClienteEstadoDeRegistroForm, ClienteForm, InformacionDeContactoFormSet
from mtvmcotizacionv02.views import valor_Personalizacionvisual, get_query
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from direccion.models import Direccion, Ciudad, Inmueble, Edificacion, \
    TipoDeEdificacion, Ascensor, HorarioDisponible
from direccion.forms import DireccionForm, EdificacionForm, AscensorFormSet, \
    HorarioDisponibleFormSet, InmuebleForm
from ambiente.forms import Ambiente
import json
from django.db.models import Count


# Create your views here.
# app sexo
class SexoListView(ListView):
    model = Sexo
    paginate_by = 10
    context_object_name = 'sexos'
    template_name = 'sexo_lista.html'

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
        context = super(SexoListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['sexo', ])
            lista_sexo = Sexo.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['sexo', ])
            lista_sexo = Sexo.objects.filter(entry_query)
        elif order_by:
            lista_sexo = Sexo.objects.all().order_by(order_by)
        else:
            lista_sexo = Sexo.objects.all()

        paginator = Paginator(lista_sexo, 10)
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
            entry_query = get_query(search, ['sexo', ])
            queryset = Sexo.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['sexo', ])
            queryset = Sexo.objects.filter(entry_query)
        elif order_by:
            queryset = Sexo.objects.all().order_by(order_by)
        else:
            queryset = Sexo.objects.all()

        return queryset


class SexoView(View):
    form_class = SexoForm
    template_name = 'sexo_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Sexo '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('uclientes:edit_sexo',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Sexo '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('uclientes:list_sexo'))

        return render(request, self.template_name, {'form': form})


class SexoUpdate(UpdateView):
    template_name = 'sexo_edit.html'
    form_class = SexoForm
    model = Sexo

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(SexoUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        sexo = Sexo.objects.get(pk=self.object.pk)
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
            lista_sexo = Sexo.objects.all().order_by(order_by)
        else:
            lista_sexo = Sexo.objects.all()

        paginator = Paginator(lista_sexo, nropag)
        # Show 25 contacts per page

        if page == '0':
            sexos = lista_sexo
        else:
            try:
                sexos = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                sexos = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                sexos = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(sexos.object_list[i].id == sexo.id):
                    if sexos.has_previous:
                        try:
                            previousitem = sexos.object_list[i-1].id
                        except:
                            previousitem = None

                    if sexos.has_next:
                        try:
                            nextitem = sexos.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(sexos)
            for i in range(0, countitem):
                if(sexos[i].id == sexo.id):
                    try:
                        previousitem = sexos[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = sexos[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            sexo_previous = Sexo.objects.get(pk=previousitem)
        except:
            sexo_previous = None
        try:
            sexo_next = Sexo.objects.get(pk=nextitem)
        except:
            sexo_next = None

        context['sexo_previous'] = sexo_previous
        context['sexo_next'] = sexo_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Sexo '" + str(self.object) + "'  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Sexo '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                return render_to_response(self.template_name, self.get_context_data())


class SexoDelete(DeleteView):
    model = Sexo
    form_class = SexoForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            messages.success(self.request, "Sexo '" + str(self.object) + "'  eliminado con éxito.")
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app estado civil
class EstadoCivilListView(ListView):
    model = EstadoCivil
    paginate_by = 10
    context_object_name = 'estados_civil'
    template_name = 'estado_civil_lista.html'

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
        context = super(EstadoCivilListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['estado_civil', ])
            lista_estado_civil = EstadoCivil.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['estado_civil', ])
            lista_estado_civil = EstadoCivil.objects.filter(entry_query)
        elif order_by:
            lista_estado_civil = EstadoCivil.objects.all().order_by(order_by)
        else:
            lista_estado_civil = EstadoCivil.objects.all()

        paginator = Paginator(lista_estado_civil, 10)
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
            entry_query = get_query(search, ['estado_civil', ])
            queryset = EstadoCivil.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['estado_civil', ])
            queryset = EstadoCivil.objects.filter(entry_query)
        elif order_by:
            lista_estado_civil = EstadoCivil.objects.all().order_by(order_by)
            queryset = EstadoCivil.objects.all()

        return queryset


class EstadoCivilView(View):
    form_class = EstadoCivilForm
    template_name = 'estado_civil_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Estado civil '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('uclientes:edit_estado_civil',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Estado civil '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('uclientes:list_estado_civil'))

        return render(request, self.template_name, {'form': form})


class EstadoCivilUpdate(UpdateView):
    template_name = 'estado_civil_edit.html'
    form_class = EstadoCivilForm
    model = EstadoCivil

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(EstadoCivilUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        estado_civil = EstadoCivil.objects.get(pk=self.object.pk)
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
            lista_estado_civil = EstadoCivil.objects.all().order_by(order_by)
        else:
            lista_estado_civil = EstadoCivil.objects.all()

        paginator = Paginator(lista_estado_civil, nropag)
        # Show 25 contacts per page

        if page == '0':
            estados_civil = lista_estado_civil
        else:
            try:
                estados_civil = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                estados_civil = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                estados_civil = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(estados_civil.object_list[i].id == estado_civil.id):
                    if estados_civil.has_previous:
                        try:
                            previousitem = estados_civil.object_list[i-1].id
                        except:
                            previousitem = None

                    if estados_civil.has_next:
                        try:
                            nextitem = estados_civil.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(estados_civil)
            for i in range(0, countitem):
                if(estados_civil[i].id == estado_civil.id):
                    try:
                        previousitem = estados_civil[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = estados_civil[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            estado_civil_previous = EstadoCivil.objects.get(pk=previousitem)
        except:
            estado_civil_previous = None
        try:
            estado_civil_next = EstadoCivil.objects.get(pk=nextitem)
        except:
            estado_civil_next = None

        context['estado_civil_previous'] = estado_civil_previous
        context['estado_civil_next'] = estado_civil_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Estado civil '" + str(self.object) + "'  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Estado civil '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                return render_to_response(self.template_name, self.get_context_data())


class EstadoCivilDelete(DeleteView):
    model = EstadoCivil
    form_class = EstadoCivilForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            messages.success(self.request, "Estado civil '" + str(self.obj) + "'  eliminado con éxito.")
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app tipo de cliente
class TipoDeClienteListView(ListView):
    model = TipoDeCliente
    paginate_by = 10
    context_object_name = 'tiposdecliente'
    template_name = 'tipodecliente_lista.html'

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
        context = super(TipoDeClienteListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_cliente',
                                             'descripcion' ])
            lista_tipodecliente = TipoDeCliente.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_cliente',
                                             'descripcion' ])
            lista_tipodecliente = TipoDeCliente.objects.filter(entry_query)
        elif order_by:
            lista_tipodecliente = TipoDeCliente.objects.all().order_by(order_by)
        else:
            lista_tipodecliente = TipoDeCliente.objects.all()

        paginator = Paginator(lista_tipodecliente, 10)
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
            entry_query = get_query(search, ['tipo_de_cliente',
                                             'descripcion', ])
            queryset = TipoDeCliente.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_cliente',
                                             'descripcion', ])
            queryset = TipoDeCliente.objects.filter(entry_query)
        elif order_by:
            queryset = TipoDeCliente.objects.all().order_by(order_by)
        else:
            queryset = TipoDeCliente.objects.all()

        return queryset


class TipoDeClienteView(View):
    form_class = TipoDeClienteForm
    template_name = 'tipodecliente_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Tipo de cliente '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('uclientes:edit_tipo_de_cliente',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Tipo de cliente '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('uclientes:list_tipo_de_cliente'))

        return render(request, self.template_name, {'form': form})


class TipoDeClienteUpdate(UpdateView):
    template_name = 'tipodecliente_edit.html'
    form_class = TipoDeClienteForm
    model = TipoDeCliente

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TipoDeClienteUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        tipodecliente = TipoDeCliente.objects.get(pk=self.object.pk)
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
            lista_tipodecliente = TipoDeCliente.objects.all().order_by(order_by)
        else:
            lista_tipodecliente = TipoDeCliente.objects.all()

        paginator = Paginator(lista_tipodecliente, nropag)
        # Show 25 contacts per page

        if page == '0':
            tiposdecliente = lista_tipodecliente
        else:
            try:
                tiposdecliente = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                tiposdecliente = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                tiposdecliente = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(tiposdecliente.object_list[i].id == tipodecliente.id):
                    if tiposdecliente.has_previous:
                        try:
                            previousitem = tiposdecliente.object_list[i-1].id
                        except:
                            previousitem = None

                    if tiposdecliente.has_next:
                        try:
                            nextitem = tiposdecliente.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(tiposdecliente)
            for i in range(0, countitem):
                if(tiposdecliente[i].id == tiposdecliente.id):
                    try:
                        previousitem = tiposdecliente[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = tiposdecliente[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            tipodecliente_previous = TipoDeCliente.objects.get(pk=previousitem)
        except:
            tipodecliente_previous = None
        try:
            tipodecliente_next = TipoDeCliente.objects.get(pk=nextitem)
        except:
            tipodecliente_next = None

        context['tipodecliente_previous'] = tipodecliente_previous
        context['tipodecliente_next'] = tipodecliente_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Tipo de cliente '" + str(self.object) + "'  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Tipo de cliente '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                return render_to_response(self.template_name, self.get_context_data())


class TipoDeClienteDelete(DeleteView):
    model = TipoDeCliente
    form_class = TipoDeClienteForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            messages.success(self.request, "Tipo de cliente '" + str(self.obj) + "'  eliminado con éxito.")
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app tipo de relacion
class TipoDeRelacionListView(ListView):
    model = TipoDeRelacion
    paginate_by = 10
    context_object_name = 'tiposderelacion'
    template_name = 'tipoderelacion_lista.html'

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
        context = super(TipoDeRelacionListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_relacion',
                                             'descripcion', ])
            lista_tipoderelacion = TipoDeRelacion.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_relacion',
                                             'descripcion', ])
            lista_tipoderelacion = TipoDeRelacion.objects.filter(entry_query)
        elif order_by:
            lista_tipoderelacion = TipoDeRelacion.objects.all().order_by(order_by)
        else:
            lista_tipoderelacion = TipoDeRelacion.objects.all()

        paginator = Paginator(lista_tipoderelacion, 10)
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
            entry_query = get_query(search, ['tipo_de_relacion',
                                             'descripcion', ])
            queryset = TipoDeRelacion.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_relacion',
                                             'descripcion', ])
            queryset = TipoDeRelacion.objects.filter(entry_query)
        elif order_by:
            queryset = TipoDeRelacion.objects.all().order_by(order_by)
        else:
            queryset = TipoDeRelacion.objects.all()

        return queryset


class TipoDeRelacionView(View):
    form_class = TipoDeRelacionForm
    template_name = 'tipoderelacion_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Tipo de relación '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('uclientes:edit_tipo_de_relacion',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Tipo de relación '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('uclientes:list_tipo_de_relacion'))

        return render(request, self.template_name, {'form': form})


class TipoDeRelacionUpdate(UpdateView):
    template_name = 'tipoderelacion_edit.html'
    form_class = TipoDeRelacionForm
    model = TipoDeRelacion

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TipoDeRelacionUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        tipoderelacion = TipoDeRelacion.objects.get(pk=self.object.pk)
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
            lista_tipoderelacion = TipoDeRelacion.objects.all().order_by(order_by)
        else:
            lista_tipoderelacion = TipoDeRelacion.objects.all()

        paginator = Paginator(lista_tipoderelacion, nropag)
        # Show 25 contacts per page

        if page == '0':
            tiposderelacion = lista_tipoderelacion
        else:
            try:
                tiposderelacion = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                tiposderelacion = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                tiposderelacion = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(tiposderelacion.object_list[i].id == tipoderelacion.id):
                    if tiposderelacion.has_previous:
                        try:
                            previousitem = tiposderelacion.object_list[i-1].id
                        except:
                            previousitem = None

                    if tiposderelacion.has_next:
                        try:
                            nextitem = tiposderelacion.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(tiposderelacion)
            for i in range(0, countitem):
                if(tiposderelacion[i].id == tiposderelacion.id):
                    try:
                        previousitem = tiposderelacion[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = tiposderelacion[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            tipoderelacion_previous = TipoDeRelacion.objects.get(pk=previousitem)
        except:
            tipoderelacion_previous = None
        try:
            tipoderelacion_next = TipoDeRelacion.objects.get(pk=nextitem)
        except:
            tipoderelacion_next = None

        context['tipoderelacion_previous'] = tipoderelacion_previous
        context['tipoderelacion_next'] = tipoderelacion_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Tipo de relación '" + str(self.object) + "'  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Tipo de relación '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                return render_to_response(self.template_name, self.get_context_data())


class TipoDeRelacionDelete(DeleteView):
    model = TipoDeRelacion
    form_class = TipoDeRelacionForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            messages.success(self.request, "Tipo de relación '" + str(self.obj) + "'  eliminado con éxito.")
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app tipo de informacion de contacto
class TipoDeInformacionDeContactoListView(ListView):
    model = TipoDeInformacionDeContacto
    paginate_by = 10
    context_object_name = 'tiposdeinformaciondecontacto'
    template_name = 'tipodeinformaciondecontacto_lista.html'

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
        context = super(TipoDeInformacionDeContactoListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_informacion_de_contacto',
                                             'descripcion', ])
            lista_tipodeinformaciondecontacto = TipoDeInformacionDeContacto.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_informacion_de_contacto',
                                             'descripcion', ])
            lista_tipodeinformaciondecontacto = TipoDeInformacionDeContacto.objects.filter(entry_query)
        elif order_by:
            lista_tipodeinformaciondecontacto = TipoDeInformacionDeContacto.objects.all().order_by(order_by)
        else:
            lista_tipodeinformaciondecontacto = TipoDeInformacionDeContacto.objects.all()

        paginator = Paginator(lista_tipodeinformaciondecontacto, 10)
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
            entry_query = get_query(search, ['tipo_de_informacion_de_contacto',
                                             'descripcion', ])
            queryset = TipoDeInformacionDeContacto.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_informacion_de_contacto',
                                             'descripcion', ])
            queryset = TipoDeInformacionDeContacto.objects.filter(entry_query)
        elif order_by:
            queryset = TipoDeInformacionDeContacto.objects.all().order_by(order_by)
        else:
            queryset = TipoDeInformacionDeContacto.objects.all()

        return queryset


class TipoDeInformacionDeContactoView(View):
    form_class = TipoDeInformacionDeContactoForm
    template_name = 'tipodeinformaciondecontacto_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Tipo de información de contacto '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('uclientes:edit_tipo_de_informacion_de_contacto',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Tipo de información de contacto '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('uclientes:list_tipo_de_informacion_de_contacto'))

        return render(request, self.template_name, {'form': form})


class TipoDeInformacionDeContactoUpdate(UpdateView):
    template_name = 'tipodeinformaciondecontacto_edit.html'
    form_class = TipoDeInformacionDeContactoForm
    model = TipoDeInformacionDeContacto

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TipoDeInformacionDeContactoUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        tipodeinformaciondecontacto = TipoDeInformacionDeContacto.objects.get(pk=self.object.pk)
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
            lista_tipodeinformaciondecontacto = TipoDeInformacionDeContacto.objects.all().order_by(order_by)
        else:
            lista_tipodeinformaciondecontacto = TipoDeInformacionDeContacto.objects.all()

        paginator = Paginator(lista_tipodeinformaciondecontacto, nropag)
        # Show 25 contacts per page

        if page == '0':
            tiposdeinformaciondecontacto = lista_tipodeinformaciondecontacto
        else:
            try:
                tiposdeinformaciondecontacto = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                tiposdeinformaciondecontacto = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                tiposdeinformaciondecontacto = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(tiposdeinformaciondecontacto.object_list[i].id == tipodeinformaciondecontacto.id):
                    if tiposdeinformaciondecontacto.has_previous:
                        try:
                            previousitem = tiposdeinformaciondecontacto.object_list[i-1].id
                        except:
                            previousitem = None

                    if tiposdeinformaciondecontacto.has_next:
                        try:
                            nextitem = tiposdeinformaciondecontacto.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(tiposdeinformaciondecontacto)
            for i in range(0, countitem):
                if(tiposdeinformaciondecontacto[i].id == tiposdeinformaciondecontacto.id):
                    try:
                        previousitem = tiposdeinformaciondecontacto[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = tiposdeinformaciondecontacto[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            tipodeinformaciondecontacto_previous = TipoDeInformacionDeContacto.objects.get(pk=previousitem)
        except:
            tipodeinformaciondecontacto_previous = None
        try:
            tipodeinformaciondecontacto_next = TipoDeInformacionDeContacto.objects.get(pk=nextitem)
        except:
            tipodeinformaciondecontacto_next = None

        context['tipodeinformaciondecontacto_previous'] = tipodeinformaciondecontacto_previous
        context['tipodeinformaciondecontacto_next'] = tipodeinformaciondecontacto_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Tipo de información de contacto '" + str(self.object) + "'  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Tipo de información de contacto '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                return render_to_response(self.template_name, self.get_context_data())


class TipoDeInformacionDeContactoDelete(DeleteView):
    model = TipoDeInformacionDeContacto
    form_class = TipoDeInformacionDeContactoForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            messages.success(self.request, "Tipo de información de contacto '" + str(self.obj) + "'  eliminado con éxito.")
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app cliente
class ClienteListView(ListView):
    model = Cliente
    paginate_by = 10
    context_object_name = 'cliente'
    template_name = 'cliente_lista.html'

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
        context = super(ClienteListView, self).get_context_data(**kwargs)
        # Add in the cliente
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_cliente__tipo_de_cliente',
                                             'cuit',
                                             'nombre', ])
            lista_cliente = Cliente.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_cliente__tipo_de_cliente',
                                             'cuit',
                                             'nombre', ])
            lista_cliente = Cliente.objects.filter(entry_query)
        elif order_by:
            lista_cliente = Cliente.objects.all().order_by(order_by)
        else:
            lista_cliente = Cliente.objects.all()

        paginator = Paginator(lista_cliente, 10)
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

        context['detalle_cliente'] = Contacto.objects.filter(tipo_de_relacion__tipo_de_relacion="cliente")
        context['ultimo'] = str(paginator.num_pages)
        context['page_range2'] = range(start, end)
        return context

    def get_queryset(self):

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_cliente__tipo_de_cliente',
                                             'cuit',
                                             'nombre', ])
            queryset = Cliente.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_cliente__tipo_de_cliente',
                                             'cuit',
                                             'nombre', ])
            queryset = Cliente.objects.filter(entry_query)
        elif order_by:
            queryset = Cliente.objects.all().order_by(order_by)
        else:
            queryset = Cliente.objects.all()

        return queryset


class ClienteView(View):
    form_class = ClienteForm
    template_name = 'cliente_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        tipodecliente = TipoDeCliente.objects.filter(tipo_de_cliente='Particular')
        data = {
            'tipo_de_cliente': tipodecliente[0].id
        }

        form = self.form_class(initial=data)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('uclientes:edit_cliente',
                                                    args=(id_reg.id,)))
            else:
                if id_reg.tipo_de_cliente.tipo_de_cliente == 'Particular':
                    return HttpResponseRedirect(reverse('uclientes:add_contacto') +
                                                "?cliente="+str(id_reg.id) +
                                                "&relacion=cliente")
                else:
                    return HttpResponseRedirect(reverse('uclientes:ficha_cliente',
                                                args=(id_reg.id,)))

        return render(request, self.template_name, {'form': form})


class ClienteUpdate(UpdateView):
    template_name = 'cliente_edit.html'
    form_class = ClienteForm
    model = Cliente
    second_form_class = ContactoForm

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ClienteUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        cliente = Cliente.objects.get(pk=self.object.pk)
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
            lista_cliente = Cliente.objects.all().order_by(order_by)
        else:
            lista_cliente = Cliente.objects.all()

        paginator = Paginator(lista_cliente, nropag)
        # Show 25 contacts per page

        if page == '0':
            clientes = lista_cliente
        else:
            try:
                clientes = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                clientes = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                clientes = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(clientes.object_list[i].id == cliente.id):
                    if clientes.has_previous:
                        try:
                            previousitem = clientes.object_list[i-1].id
                        except:
                            previousitem = None

                    if clientes.has_next:
                        try:
                            nextitem = clientes.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(clientes)
            for i in range(0, countitem):
                if(clientes[i].id == clientes.id):
                    try:
                        previousitem = clientes[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = clientes[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            cliente_previous = Cliente.objects.get(pk=previousitem)
        except:
            cliente_previous = None
        try:
            cliente_next = Cliente.objects.get(pk=nextitem)
        except:
            cliente_next = None

        context['cliente_previous'] = cliente_previous
        context['cliente_next'] = cliente_next
        contacto1 = Contacto.objects.filter(cliente=self.object.pk,
                                            tipo_de_relacion__tipo_de_relacion='cliente')

        if contacto1:
            contacto = Contacto.objects.get(pk=contacto1[0].id)
            if self.request.POST:
                context['contacto'] = self.second_form_class(self.request.POST, instance=contacto)
                item_form = InformacionDeContactoFormSet(self.request.POST, instance=contacto)
            else:
                context['contacto'] = self.second_form_class(instance=contacto)
                item_form = InformacionDeContactoFormSet(instance=contacto)

            context['item_form'] = item_form

        return context

    def form_valid(self, form):
        context = self.get_context_data()

        if form.is_valid():
            self.object = form.save()

            if self.object.tipo_de_cliente == 'Particular':
                contacto = context['contacto']
                item_form = context['item_form']
                if contacto.is_valid() and item_form.is_valid():
                    contacto.save()
                    item_form.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Cliente " + str(self.object) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return render_to_response(self.template_name, self.get_context_data())


class ClienteDelete(DeleteView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


class ClienteDetail(DetailView):

    model = Cliente
    context_object_name = "cliente"
    template_name = 'cliente_ficha.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ClienteDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['contacto_cliente'] = InformacionDeContacto.objects.filter(contacto__cliente=self.object.pk,
                                                                           contacto__tipo_de_relacion__tipo_de_relacion='cliente')
        context['contactos'] = InformacionDeContacto.objects.filter(contacto__cliente=self.object.pk).exclude(contacto__tipo_de_relacion__tipo_de_relacion='cliente')
        context['direcciones'] = ClienteDireccion.objects.filter(cliente=self.object.pk)

        return context


# app contacto

class ContactoCreateView(CreateView):
    template_name = 'contacto_add.html'
    model = Contacto
    form_class = ContactoForm

    def get_initial(self):
        super(ContactoCreateView, self).get_initial()
        cliente = Cliente.objects.filter(id=self.request.GET.get('cliente'))
        if self.request.GET.get('relacion'):
            relacion = TipoDeRelacion.objects.filter(tipo_de_relacion=self.request.GET.get('relacion'))
            data = {
                'cliente': cliente[0].id,
                'nombre': cliente[0].nombre,
                'tipo_de_relacion': relacion[0].id
            }
        else:
            data = {
                'cliente': cliente[0].id
            }

        self.initial = data
        return self.initial

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        item_form = InformacionDeContactoFormSet()

        return self.render_to_response(
            self.get_context_data(form=form,
                                  item_form=item_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        item_form = InformacionDeContactoFormSet(self.request.POST)
        if (form.is_valid() and item_form.is_valid()):
            return self.form_valid(form, item_form)
        else:
            return self.form_invalid(form, item_form)

    def form_valid(self, form, item_form):
        """
        Called if all forms are valid. Creates a Contacto instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        item_form.instance = self.object
        item_form.save()

        if 'regEdit' in self.request.POST:
            messages.success(self.request, "Registro guardado.")
            return HttpResponseRedirect(reverse('uclientes:edit_contacto',
                                                args=(self.object,)))
        else:
            messages.success(self.request, "Contacto '" + str(self.object) + "'  registrado con éxito.")
            return HttpResponseRedirect(reverse('uclientes:ficha_cliente',
                                                args=(self.object.cliente.id,)))

    def form_invalid(self, form, item_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  item_form=item_form))


class ContactoUpdate(UpdateView):
    template_name = 'contacto_edit.html'
    form_class = ContactoForm
    model = Contacto

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ContactoUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        contacto = Contacto.objects.get(pk=self.object.pk)
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
            lista_contacto = Contacto.objects.all().order_by(order_by
                                                             ).exclude(tipo_de_relacion__tipo_de_relacion=
                                                                       'cliente')
        else:
            lista_contacto = Contacto.objects.all().exclude(tipo_de_relacion__tipo_de_relacion=
                                                            'cliente')

        paginator = Paginator(lista_contacto, nropag)
        # Show 25 contacts per page

        if page == '0':
            contactos = lista_contacto
        else:
            try:
                contactos = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                contactos = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                contactos = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(contactos.object_list[i].id == contacto.id):
                    if contactos.has_previous:
                        try:
                            previousitem = contactos.object_list[i-1].id
                        except:
                            previousitem = None

                    if contactos.has_next:
                        try:
                            nextitem = contactos.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(contactos)
            for i in range(0, countitem):
                if(contactos[i].id == contacto.id):
                    try:
                        previousitem = contactos[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = contactos[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            contacto_previous = Contacto.objects.get(pk=previousitem)
        except:
            contacto_previous = None
        try:
            contacto_next = Contacto.objects.get(pk=nextitem)
        except:
            contacto_next = None

        context['contacto_previous'] = contacto_previous
        context['contacto_next'] = contacto_next
        if self.request.POST:
            item_form = InformacionDeContactoFormSet(self.request.POST, instance=self.object)
        else:
            item_form = InformacionDeContactoFormSet(instance=self.object)

        context['item_form'] = item_form
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        item_form = context['item_form']

        if form.is_valid() and item_form.is_valid():
            self.object = form.save()
            item_form.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Persona de contacto " + str(self.object) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            messages.success(self.request, "Persona de contacto " + str(self.object) + "  guardado con éxito.")
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('uclientes:ficha_cliente',
                                                    args=(self.object.cliente.id,)))


# app direccion
class ClienteDireccionView(View):
    form_class = DireccionForm
    template_name = 'clientedireccion_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        puntogeografico = Ciudad.objects.filter(ciudad='Buenos Aires')
        data = {
            'pais': puntogeografico[0].pais,
            'provincia': puntogeografico[0].provincia,
            'ciudad': puntogeografico[0].id
        }

        form = self.form_class(initial=data)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        titulo = self.request.POST.get('titulo_de_direccion', '')
        cliente = self.request.GET.get('cliente', '')

        if form.is_valid():
            id_reg = form.save()

            direccion = Direccion.objects.filter(id=id_reg.id)

            agregarclientedireccion = ClienteDireccion.objects.create(cliente_id=cliente,
                                                                      direccion_id=id_reg.id,
                                                                      titulo_de_direccion=titulo,
                                                                      detalle_de_direccion=direccion[0].full_direccion())
            agregarclientedireccion.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Dirección '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('uclientes:edit_direccion',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Dirección:  '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('uclientes:add_inmueble') +
                                            "?clientedireccion="+str(agregarclientedireccion.id))

        return render(request, self.template_name, {'form': form})


class ClienteDireccionUpdate(UpdateView):
    template_name = 'clientedireccion_edit.html'
    form_class = DireccionForm
    model = Direccion

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ClienteDireccionUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        clientedireccion = Direccion.objects.get(pk=self.object.pk)
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
            lista_clientedireccion = Direccion.objects.all().order_by(order_by)
        else:
            lista_clientedireccion = Direccion.objects.all()

        paginator = Paginator(lista_clientedireccion, nropag)
        # Show 25 contacts per page

        if page == '0':
            clientedirecciones = lista_clientedireccion
        else:
            try:
                clientedirecciones = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                clientedirecciones = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                clientedirecciones = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(clientedirecciones.object_list[i].id == clientedireccion.id):
                    if clientedirecciones.has_previous:
                        try:
                            previousitem = clientedirecciones.object_list[i-1].id
                        except:
                            previousitem = None

                    if clientedirecciones.has_next:
                        try:
                            nextitem = clientedirecciones.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(clientedirecciones)
            for i in range(0, countitem):
                if(clientedirecciones[i].id == clientedirecciones.id):
                    try:
                        previousitem = clientedirecciones[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = clientedirecciones[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            clientedireccion_previous = DireccionForm.objects.get(pk=previousitem)
        except:
            clientedireccion_previous = None
        try:
            clientedireccion_next = DireccionForm.objects.get(pk=nextitem)
        except:
            clientedireccion_next = None

        context['clientedireccion_previous'] = clientedireccion_previous
        context['clientedireccion_next'] = clientedireccion_next

        direccion = ClienteDireccion.objects.filter(id=self.request.GET.get('clientedireccion'))
        context['titulo'] = direccion[0].titulo_de_direccion
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        clientedireccion = self.request.GET.get('clientedireccion', '')
        titulo = self.request.POST.get('titulo_de_direccion', '')

        clientedireccion = ClienteDireccion.objects.filter(id=clientedireccion)

        clientedireccion.update(titulo_de_direccion=titulo)

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Dirección '" + str(self.object) + "'  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Dirección '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to +
                                            "&clientedireccion="+str(clientedireccion[0].id))
            else:
                return render_to_response(self.template_name, self.get_context_data())


class ClienteInmuebleView(View):
    form_class = InmuebleForm
    template_name = 'clienteinmueble_add.html'

    def get_context_data(self, **kwargs):
        context = super(ClienteInmuebleView, self).get_context_data(**kwargs)
        direccion = Direccion.objects.filter(clientedireccion=
                                             self.request.GET.get('clientedireccion'))
        context['form'].fields['edificacion'].queryset = Edificacion.objects.for_direccion(direccion.id)
        return context

    def get(self, request, *args, **kwargs):
        """docstring"""

        direccion = Direccion.objects.filter(clientedireccion=
                                             self.request.GET.get('clientedireccion'))
        if self.request.GET.get('edificacion'):
            edificacion = Edificacion.objects.filter(id=self.request.GET.get('edificacion'))
            data = {
                'edificacion': edificacion[0].id
                }
            form = self.form_class(initial=data, direccion=direccion[0].id)
        else:
            form = self.form_class(direccion=direccion[0].id)
        return render(request, self.template_name, {'form': form,
                                                    'direccion': direccion})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        clientedireccion = self.request.GET.get('clientedireccion', '')

        direccion = Direccion.objects.filter(clientedireccion=clientedireccion)

        if form.is_valid():
            id_reg = form.save()

            inmueble = Inmueble.objects.filter(id=id_reg.id)

            clientedireccion = ClienteDireccion.objects.filter(id=clientedireccion)

            clientedireccion.update(inmueble=inmueble[0].id, edificacion=inmueble[0].edificacion)

            if 'regEdit' in request.POST:
                messages.success(self.request, "Inmueble '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('uclientes:edit_direccion',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Inmueble:  '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('uclientes:ficha_cliente',
                                                    args=(clientedireccion[0].cliente.id,)))

        return render(request, self.template_name, {'form': form,
                                                    'direccion': direccion})


class InmuebleUpdate(UpdateView):
    template_name = 'clienteinmueble_edit.html'
    form_class = InmuebleForm
    model = Inmueble

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(InmuebleUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        inmueble = Inmueble.objects.get(pk=self.object.pk)
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
            lista_inmueble = Inmueble.objects.all().order_by(order_by)
        else:
            lista_inmueble = Inmueble.objects.all()

        paginator = Paginator(lista_inmueble, nropag)
        # Show 25 contacts per page

        if page == '0':
            inmuebles = lista_inmueble
        else:
            try:
                inmuebles = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                inmuebles = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                inmuebles = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(inmuebles.object_list[i].id == inmueble.id):
                    if inmuebles.has_previous:
                        try:
                            previousitem = inmuebles.object_list[i-1].id
                        except:
                            previousitem = None

                    if inmuebles.has_next:
                        try:
                            nextitem = inmuebles.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(inmuebles)
            for i in range(0, countitem):
                if(inmuebles[i].id == inmueble.id):
                    try:
                        previousitem = inmuebles[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = inmuebles[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            inmueble_previous = Inmueble.objects.get(pk=previousitem)
        except:
            inmueble_previous = None
        try:
            inmueble_next = Inmueble.objects.get(pk=nextitem)
        except:
            inmueble_next = None

        context['inmueble_previous'] = inmueble_previous
        context['inmueble_next'] = inmueble_next

        direccion = Direccion.objects.filter(clientedireccion=
                                             self.request.GET.get('clientedireccion'))
        context['direccion'] = direccion
        context['form'].fields['edificacion'].queryset = Edificacion.objects.filter(direccion=direccion[0].id)
        return context

    def get_form_kwargs(self):
        kwargs = super(InmuebleUpdate, self).get_form_kwargs()
        direccion = Direccion.objects.filter(clientedireccion=
                                             self.request.GET.get('clientedireccion'))
        kwargs['direccion'] = direccion[0].id
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        clientedireccion = self.request.GET.get('clientedireccion', '')
        clientedireccion = ClienteDireccion.objects.filter(id=clientedireccion)
        clientedireccion.update(inmueble=self.object.id, edificacion=self.object.edificacion)

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Inmueble '" + str(self.object) + "'  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Inmueble '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                return render_to_response(self.template_name, self.get_context_data())


class EdificacionCreateView(CreateView):
    template_name = 'clienteedificacion_add.html'
    model = Edificacion
    form_class = EdificacionForm

    def get_initial(self):
        super(EdificacionCreateView, self).get_initial()
        clientedireccion = ClienteDireccion.objects.filter(id=self.request.GET.get('clientedireccion'))
        data = {
            'direccion': clientedireccion[0].direccion
            }

        self.initial = data
        return self.initial

    def get_context_data(self, **kwargs):
        context = super(EdificacionCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['itemascensor_form'] = AscensorFormSet(self.request.POST)
            context['itemhorariodisponible_form'] = HorarioDisponibleFormSet(self.request.POST)
        else:
            context['itemascensor_form'] = AscensorFormSet()
            context['itemhorariodisponible_form'] = HorarioDisponibleFormSet()
        return context

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        itemascensor_form = AscensorFormSet()
        itemhorariodisponible_form = HorarioDisponibleFormSet()

        return self.render_to_response(
            self.get_context_data(form=form,
                                  itemascensor_form=itemascensor_form,
                                  itemhorariodisponible_form=itemhorariodisponible_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if (form.is_valid()):
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """
        Called if all forms are valid. Creates a Contacto instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        context = self.get_context_data()
        itemascensor_form = context['itemascensor_form']
        itemhorariodisponible_form = context['itemhorariodisponible_form']
        clientedireccion = self.request.GET.get('clientedireccion', '')
        clientedireccion = ClienteDireccion.objects.filter(id=clientedireccion)
        redirect_to = self.request.GET.get('next', '')
        nombre = self.request.POST.get('nombre_de_edificio', '')
        if nombre:
            nombre = nombre
        else:
            tipodeedificacion = TipoDeEdificacion.objects.filter(id=self.request.POST.get('tipo_de_edificacion', ''))
            nombre = tipodeedificacion[0].tipo_de_edificacion

        if itemascensor_form.is_valid() and itemhorariodisponible_form.is_valid():
            self.object = form.save(commit=False)
            self.object.nombre_de_edificio = nombre
            self.object.save()
            itemascensor_form.instance = self.object
            itemascensor_form.save()
            itemhorariodisponible_form.instance = self.object
            itemhorariodisponible_form.save()

        elif itemascensor_form.is_valid():

            self.object = form.save(commit=False)
            self.object.nombre_de_edificio = nombre
            self.object.save()
            itemascensor_form.instance = self.object
            itemascensor_form.save()

        elif itemhorariodisponible_form.is_valid():

            self.object = form.save(commit=False)
            self.object.nombre_de_edificio = nombre
            self.object.save()
            itemhorariodisponible_form.instance = self.object
            itemhorariodisponible_form.save()

        else:
            self.object = form.save(commit=False)
            self.object.nombre_de_edificio = nombre
            self.object.save()

        if 'regEdit' in self.request.POST:
            messages.success(self.request, "Registro guardado.")
            return HttpResponseRedirect(reverse('uclientes:edit_contacto',
                                                args=(self.object,)))
        else:
            if redirect_to:
                messages.success(self.request, "Edificación '" + str(self.object) + "'  registrado con éxito.")
                return HttpResponseRedirect(redirect_to +
                                            "&edificacion="+str(self.object.id) +
                                            "&clientedireccion="+str(clientedireccion[0].id))
            else:
                messages.success(self.request, "Edificación '" + str(self.object) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('uclientes:ficha_cliente',
                                                    args=(clientedireccion[0].cliente.id,)))

    def form_invalid(self, form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form))


class EdificacionUpdate(UpdateView):
    template_name = 'clienteedificacion_edit.html'
    form_class = EdificacionForm
    model = Edificacion

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(EdificacionUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        edificacion = Edificacion.objects.get(pk=self.object.pk)
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
            lista_edificacion = Edificacion.objects.all().order_by(order_by)
        else:
            lista_edificacion = Edificacion.objects.all()

        paginator = Paginator(lista_edificacion, nropag)
        # Show 25 contacts per page

        if page == '0':
            edificacions = lista_edificacion
        else:
            try:
                edificacions = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                edificacions = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                edificacions = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(edificacions.object_list[i].id == edificacion.id):
                    if edificacions.has_previous:
                        try:
                            previousitem = edificacions.object_list[i-1].id
                        except:
                            previousitem = None

                    if edificacions.has_next:
                        try:
                            nextitem = edificacions.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(edificacions)
            for i in range(0, countitem):
                if(edificacions[i].id == edificacion.id):
                    try:
                        previousitem = edificacions[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = edificacions[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            edificacion_previous = Edificacion.objects.get(pk=previousitem)
        except:
            edificacion_previous = None
        try:
            edificacion_next = Edificacion.objects.get(pk=nextitem)
        except:
            edificacion_next = None

        context['edificacion_previous'] = edificacion_previous
        context['edificacion_next'] = edificacion_next
        if self.request.POST:
            itemascensor_form = AscensorFormSet(self.request.POST, instance=self.object)
            itemhorariodisponible_form = HorarioDisponibleFormSet(self.request.POST, instance=self.object)
        else:
            itemascensor_form = AscensorFormSet(instance=self.object)
            itemhorariodisponible_form = HorarioDisponibleFormSet(instance=self.object)

        context['itemascensor_form'] = itemascensor_form
        context['itemhorariodisponible_form'] = itemhorariodisponible_form
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        itemascensor_form = context['itemascensor_form']
        itemhorariodisponible_form = context['itemhorariodisponible_form']
        clientedireccion = self.request.GET.get('clientedireccion', '')
        clientedireccion = ClienteDireccion.objects.filter(id=clientedireccion)
        nombre = self.request.POST.get('nombre_de_edificio', '')
        if nombre:
            nombre = nombre
        else:
            tipodeedificacion = TipoDeEdificacion.objects.filter(id=self.request.POST.get('tipo_de_edificacion', ''))
            nombre = tipodeedificacion[0].tipo_de_edificacion

        if itemascensor_form.is_valid() and itemhorariodisponible_form.is_valid():
            self.object = form.save(commit=False)
            self.object.nombre_de_edificio = nombre
            self.object.save()
            itemascensor_form.instance = self.object
            itemascensor_form.save()
            itemhorariodisponible_form.instance = self.object
            itemhorariodisponible_form.save()

        elif itemascensor_form.is_valid():

            self.object = form.save(commit=False)
            self.object.nombre_de_edificio = nombre
            self.object.save()
            itemascensor_form.instance = self.object
            itemascensor_form.save()

        elif itemhorariodisponible_form.is_valid():

            self.object = form.save(commit=False)
            self.object.nombre_de_edificio = nombre
            self.object.save()
            itemhorariodisponible_form.instance = self.object
            itemhorariodisponible_form.save()

        else:
            self.object = form.save(commit=False)
            self.object.nombre_de_edificio = nombre
            self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Edificación " + str(self.object) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            messages.success(self.request, "Edificación " + str(self.object) + "  guardado con éxito.")
            if redirect_to:
                return HttpResponseRedirect(redirect_to +
                                            "&clientedireccion="+str(clientedireccion[0].id))
            else:
                return HttpResponseRedirect(reverse('uclientes:ficha_cliente',
                                                    args=(self.object.cliente.id,)))


# view para obtener la cantidad de ambientes que tiene una especificacion de inmueble
def exchange_especificaciondeinmueble(request, id_especificacion):

    ambientes = Ambiente.objects.filter(ambienteportipodeinmueble__especificacion_de_inmueble=
                                        id_especificacion,
                                        conteo_de_ambientes=True
                                        ).values('ambienteportipodeinmueble__especificacion_de_inmueble'
                                                 ).annotate(tcount=Count('ambiente')
                                                            ).order_by('ambienteportipodeinmueble__especificacion_de_inmueble')
    if ambientes:
        response = {'cant_ambiente': ambientes[0]['tcount']}
    else:
        response = {
            'cant_ambiente': 0
            }

    return HttpResponse(json.dumps(response), content_type='application/json')


def delete_ascensor(request, pk):
    ascensor = Ascensor.objects.get(pk=pk)
    ascensor.delete()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')


def delete_horariodisponible(request, pk):
    horariodisponible = HorarioDisponible.objects.get(pk=pk)
    horariodisponible.delete()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')


def delete_informaciondecontacto(request, pk):
    informaciondecontacto = InformacionDeContacto.objects.get(pk=pk)
    informaciondecontacto.delete()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')
