from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.generic import ListView, View, UpdateView, DeleteView
from cliente.models import Sexo, EstadoCivil, TipoDeCliente, \
    TipoDeRelacion, TipoDeInformacionDeContacto, Cliente, Contacto, \
    InformacionDeContacto, ClienteDireccion, ClienteEstadoDeRegistro
from cliente.forms import SexoForm, EstadoCivilForm, TipoDeClienteForm, \
    TipoDeRelacionForm, TipoDeInformacionDeContactoForm, ClienteForm, \
    ContactoForm, InformacionDeContactoForm, ClienteDireccionForm, \
    ClienteEstadoDeRegistroForm
from mtvmcotizacionv02.views import valor_Personalizacionvisual
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
        #range_gap = 3
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
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('uclientes:edit_sexo',
                                                    args=(id_reg.id,)))
            else:
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
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Sexo " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
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
        context = super(EstadoCivilListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")
        #range_gap = 3
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
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('uclientes:edit_estado_civil',
                                                    args=(id_reg.id,)))
            else:
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
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Estado Civil " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
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
        context = super(TipoDeClienteListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")
        #range_gap = 3
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
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('uclientes:edit_tipo_de_cliente',
                                                    args=(id_reg.id,)))
            else:
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

            messages.success(self.request, "Tipo de cliente " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
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
        #range_gap = 3
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
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('uclientes:edit_tipo_de_relacion',
                                                    args=(id_reg.id,)))
            else:
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
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Tipo de contacto " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
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
        context = super(TipoDeInformacionDeContactoListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")
        #range_gap = 3
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
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('uclientes:edit_tipo_de_informacion_de_contacto',
                                                    args=(id_reg.id,)))
            else:
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
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Tipo de informacion de contacto " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
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
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())
