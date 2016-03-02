from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
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
from mtvmcotizacionv02.views import valor_Personalizacionvisual
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from direccion.models  import Direccion, Ciudad
from direccion.forms import DireccionForm


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
        if order_by:
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
        if order_by:
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
        if order_by:
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
        if order_by:
            queryset = EstadoCivil.objects.all().order_by(order_by)
        else:
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
        if order_by:
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
        if order_by:
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
        id_reg = self.object.save()

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
        context = super(TipoDeRelacionListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        if order_by:
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
        if order_by:
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
        if order_by:
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
        if order_by:
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
        if order_by:
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
        if order_by:
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
                    return HttpResponseRedirect(reverse('uclientes:list_cliente'))

        return render(request, self.template_name, {'form': form})


class ClienteUpdate(UpdateView):
    template_name = 'cliente_edit.html'
    form_class = ClienteForm
    model = Cliente

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

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

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
            lista_contacto = Contacto.objects.all().order_by(order_by)
        else:
            lista_contacto = Contacto.objects.all()

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
        self.object = form.save(commit=False)
        item_form = InformacionDeContactoFormSet(self.request.POST,
                                                 self.request.FILES,
                                                 instance=self.object)
        if item_form.is_valid():
            id_reg = self.object.save()
            item_form.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Persona de contacto " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('uclientes:ficha_cliente',
                                                    args=(self.object.cliente.id,)))


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
        cliente = self.request.POST.get('cliente', '')

        if form.is_valid():
            id_reg = form.save()

            direccion = Direccion.objects.filter(id=id_reg.id)

            agregarclientedireccion = ClienteDireccion.objects.create(cliente=cliente,
                                                                      direccion=id_reg.id,
                                                                      titulo_de_direccion=titulo,
                                                                      detalle_de_direccion=direccion[0].full_direccion)
            clientedireccion = agregarclientedireccion.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Dirección '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('uclientes:edit_direccion',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('uclientes:add_inmueble') +
                                            "?clientedireccion="+str(clientedireccion.id))

        return render(request, self.template_name, {'form': form})
