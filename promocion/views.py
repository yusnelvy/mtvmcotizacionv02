"""
Docstring documentación pendiente

"""

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.views.generic import ListView, View, UpdateView, DeleteView
from promocion.models import Medio, MedioEspecifico, TipoDeReferido, \
    Alianza, AlianzaEstado, Institucion, PersonaAliado, FuenteDePromocion
from promocion.forms import MedioForm, MedioEspecificoForm, \
    TipoDeReferidoForm, AlianzaForm, InstitucionForm, PersonaAliadoForm, \
    FuenteDePromocionForm
from estadoderegistro.models import EstadoDeRegistro
from mtvmcotizacionv02.views import valor_Personalizacionvisual, get_query
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# app medio
class MedioListView(ListView):
    model = Medio
    paginate_by = 10
    context_object_name = 'medios'
    template_name = 'medio_lista.html'

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
        context = super(MedioListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['medio',
                                             'descripcion', ])
            lista_medio = Medio.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['medio',
                                             'descripcion', ])
            lista_medio = Medio.objects.filter(entry_query)
        elif order_by:
            lista_medio = Medio.objects.all().order_by(order_by)
        else:
            lista_medio = Medio.objects.all()

        paginator = Paginator(lista_medio, 10)
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
            entry_query = get_query(search, ['medio',
                                             'descripcion', ])
            queryset = Medio.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['medio',
                                             'descripcion', ])
            queryset = Medio.objects.filter(entry_query)
        elif order_by:
            queryset = Medio.objects.all().order_by(order_by)
        else:
            queryset = Medio.objects.all()

        return queryset


class MedioView(View):
    form_class = MedioForm
    template_name = 'medio_add.html'

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
                return HttpResponseRedirect(reverse('upromociones:edit_medio',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('upromociones:list_medio'))

        return render(request, self.template_name, {'form': form})


class MedioUpdate(UpdateView):
    template_name = 'medio_edit.html'
    form_class = MedioForm
    model = Medio

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MedioUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        medio = Medio.objects.get(pk=self.object.pk)
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
            lista_medio = Medio.objects.all().order_by(order_by)
        else:
            lista_medio = Medio.objects.all()

        paginator = Paginator(lista_medio, nropag)
        # Show 25 contacts per page

        if page == '0':
            medios = lista_medio
        else:
            try:
                medios = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                medios = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                medios = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(medios.object_list[i].id == medio.id):
                    if medios.has_previous:
                        try:
                            previousitem = medios.object_list[i-1].id
                        except:
                            previousitem = None

                    if medios.has_next:
                        try:
                            nextitem = medios.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(medios)
            for i in range(0, countitem):
                if(medios[i].id == medio.id):
                    try:
                        previousitem = medios[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = medios[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            medio_previous = Medio.objects.get(pk=previousitem)
        except:
            medio_previous = None
        try:
            medio_next = Medio.objects.get(pk=nextitem)
        except:
            medio_next = None

        context['medio_previous'] = medio_previous
        context['medio_next'] = medio_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Medio " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('upromociones:list_medio'))
                #return render_to_response(self.template_name, self.get_context_data())


class MedioDelete(DeleteView):
    model = Medio
    form_class = MedioForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app medio especifico
class MedioEspecificoListView(ListView):
    model = MedioEspecifico
    paginate_by = 10
    context_object_name = 'medioespecificos'
    template_name = 'medioespecifico_lista.html'

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
        context = super(MedioEspecificoListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['medio__medio',
                                             'descripcion',
                                             'medio_especifico', ])
            lista_medioespecifico = MedioEspecifico.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['medio__medio',
                                             'descripcion',
                                             'medio_especifico', ])
            lista_medioespecifico = MedioEspecifico.objects.filter(entry_query)
        elif order_by:
            lista_medioespecifico = MedioEspecifico.objects.all().order_by(order_by)
        else:
            lista_medioespecifico = MedioEspecifico.objects.all()

        paginator = Paginator(lista_medioespecifico, 10)
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
            entry_query = get_query(search, ['medio__medio',
                                             'descripcion',
                                             'medio_especifico', ])
            queryset = MedioEspecifico.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['medio__medio',
                                             'descripcion',
                                             'medio_especifico', ])
            queryset = MedioEspecifico.objects.filter(entry_query)
        elif order_by:
            queryset = MedioEspecifico.objects.all().order_by(order_by)
        else:
            queryset = MedioEspecifico.objects.all()

        return queryset


class MedioEspecificoView(View):
    form_class = MedioEspecificoForm
    template_name = 'medioespecifico_add.html'

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
                return HttpResponseRedirect(reverse('upromociones:edit_medioespecifico',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('upromociones:list_medioespecifico'))

        return render(request, self.template_name, {'form': form})


class MedioEspecificoUpdate(UpdateView):
    template_name = 'medioespecifico_edit.html'
    form_class = MedioEspecificoForm
    model = MedioEspecifico

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MedioEspecificoUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        medioespecifico = MedioEspecifico.objects.get(pk=self.object.pk)
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
            lista_medioespecifico = MedioEspecifico.objects.all().order_by(order_by)
        else:
            lista_medioespecifico = MedioEspecifico.objects.all()

        paginator = Paginator(lista_medioespecifico, nropag)
        # Show 25 contacts per page

        if page == '0':
            medioespecificos = lista_medioespecifico
        else:
            try:
                medioespecificos = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                medioespecificos = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                medioespecificos = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(medioespecificos.object_list[i].id == medioespecifico.id):
                    if medioespecificos.has_previous:
                        try:
                            previousitem = medioespecificos.object_list[i-1].id
                        except:
                            previousitem = None

                    if medioespecificos.has_next:
                        try:
                            nextitem = medioespecificos.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(medioespecificos)
            for i in range(0, countitem):
                if(medioespecificos[i].id == medioespecifico.id):
                    try:
                        previousitem = medioespecificos[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = medioespecificos[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            medioespecifico_previous = MedioEspecifico.objects.get(pk=previousitem)
        except:
            medioespecifico_previous = None
        try:
            medioespecifico_next = MedioEspecifico.objects.get(pk=nextitem)
        except:
            medioespecifico_next = None

        context['medioespecifico_previous'] = medioespecifico_previous
        context['medioespecifico_next'] = medioespecifico_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "MedioEspecifico " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('upromociones:list_medioespecifico'))
                #return render_to_response(self.template_name, self.get_context_data())


class MedioEspecificoDelete(DeleteView):
    model = MedioEspecifico
    form_class = MedioEspecificoForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app tipo de referido
class TipoDeReferidoListView(ListView):
    model = TipoDeReferido
    paginate_by = 10
    context_object_name = 'tipodereferidos'
    template_name = 'tipodereferido_lista.html'

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
        context = super(TipoDeReferidoListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_referido',
                                             'descripcion',
                                             'medio_especifico__medio_especifico', ])
            lista_tipodereferido = TipoDeReferido.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_referido',
                                             'descripcion',
                                             'medio_especifico__medio_especifico', ])
            lista_tipodereferido = TipoDeReferido.objects.filter(entry_query)
        elif order_by:
            lista_tipodereferido = TipoDeReferido.objects.all().order_by(order_by)
        else:
            lista_tipodereferido = TipoDeReferido.objects.all()

        paginator = Paginator(lista_tipodereferido, 10)
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
            entry_query = get_query(search, ['tipo_de_referido',
                                             'descripcion',
                                             'medio_especifico__medio_especifico', ])
            queryset = TipoDeReferido.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_referido',
                                             'descripcion',
                                             'medio_especifico__medio_especifico', ])
            queryset = TipoDeReferido.objects.filter(entry_query)
        elif order_by:
            queryset = TipoDeReferido.objects.all().order_by(order_by)
        else:
            queryset = TipoDeReferido.objects.all()

        return queryset


class TipoDeReferidoView(View):
    form_class = TipoDeReferidoForm
    template_name = 'tipodereferido_add.html'

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
                return HttpResponseRedirect(reverse('upromociones:edit_tipodereferido',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('upromociones:list_tipodereferido'))

        return render(request, self.template_name, {'form': form})


class TipoDeReferidoUpdate(UpdateView):
    template_name = 'tipodereferido_edit.html'
    form_class = TipoDeReferidoForm
    model = TipoDeReferido

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TipoDeReferidoUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        tipodereferido = TipoDeReferido.objects.get(pk=self.object.pk)
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
            lista_tipodereferido = TipoDeReferido.objects.all().order_by(order_by)
        else:
            lista_tipodereferido = TipoDeReferido.objects.all()

        paginator = Paginator(lista_tipodereferido, nropag)
        # Show 25 contacts per page

        if page == '0':
            tipodereferidos = lista_tipodereferido
        else:
            try:
                tipodereferidos = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                tipodereferidos = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                tipodereferidos = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(tipodereferidos.object_list[i].id == tipodereferido.id):
                    if tipodereferidos.has_previous:
                        try:
                            previousitem = tipodereferidos.object_list[i-1].id
                        except:
                            previousitem = None

                    if tipodereferidos.has_next:
                        try:
                            nextitem = tipodereferidos.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(tipodereferidos)
            for i in range(0, countitem):
                if(tipodereferidos[i].id == tipodereferido.id):
                    try:
                        previousitem = tipodereferidos[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = tipodereferidos[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            tipodereferido_previous = TipoDeReferido.objects.get(pk=previousitem)
        except:
            tipodereferido_previous = None
        try:
            tipodereferido_next = TipoDeReferido.objects.get(pk=nextitem)
        except:
            tipodereferido_next = None

        context['tipodereferido_previous'] = tipodereferido_previous
        context['tipodereferido_next'] = tipodereferido_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "TipoDeReferido " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('upromociones:list_tipodereferido'))
                #return render_to_response(self.template_name, self.get_context_data())


class TipoDeReferidoDelete(DeleteView):
    model = TipoDeReferido
    form_class = TipoDeReferidoForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app alianza
class AlianzaListView(ListView):
    model = Alianza
    paginate_by = 10
    context_object_name = 'alianzas'
    template_name = 'alianza_lista.html'

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
        context = super(AlianzaListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['alianza',
                                             'porcentaje_comision',
                                             'medio_especifico__medio_especifico',
                                             'fecha_vigencia', ])
            lista_alianza = Alianza.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['alianza',
                                             'porcentaje_comision',
                                             'medio_especifico__medio_especifico',
                                             'fecha_vigencia', ])
            lista_alianza = Alianza.objects.filter(entry_query)
        elif order_by:
            lista_alianza = Alianza.objects.all().order_by(order_by)
        else:
            lista_alianza = Alianza.objects.all()

        paginator = Paginator(lista_alianza, 10)
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
            entry_query = get_query(search, ['alianza',
                                             'porcentaje_comision',
                                             'medio_especifico__medio_especifico',
                                             'fecha_vigencia', ])
            queryset = Alianza.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['alianza',
                                             'porcentaje_comision',
                                             'medio_especifico__medio_especifico',
                                             'fecha_vigencia', ])
            queryset = Alianza.objects.filter(entry_query)
        elif order_by:
            queryset = Alianza.objects.all().order_by(order_by)
        else:
            queryset = Alianza.objects.all()

        return queryset


class AlianzaView(View):
    form_class = AlianzaForm
    template_name = 'alianza_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            estadoactual = EstadoDeRegistro.objects.filter(model='alianza',
                                                           estado__estado='Activo')

            agregarestado = AlianzaEstado.objects.create(alianza=id_reg,
                                                         estado_de_registro_id=estadoactual[0].id,
                                                         usuario_id=2,
                                                         observacion='Creación de una alianza',
                                                         predefinido=True)
            agregarestado.save()

            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('upromociones:edit_alianza',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('upromociones:list_alianza'))

        return render(request, self.template_name, {'form': form})


class AlianzaUpdate(UpdateView):
    template_name = 'alianza_edit.html'
    form_class = AlianzaForm
    model = Alianza

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AlianzaUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        alianza = Alianza.objects.get(pk=self.object.pk)
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
            lista_alianza = Alianza.objects.all().order_by(order_by)
        else:
            lista_alianza = Alianza.objects.all()

        paginator = Paginator(lista_alianza, nropag)
        # Show 25 contacts per page

        if page == '0':
            alianzas = lista_alianza
        else:
            try:
                alianzas = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                alianzas = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                alianzas = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(alianzas.object_list[i].id == alianza.id):
                    if alianzas.has_previous:
                        try:
                            previousitem = alianzas.object_list[i-1].id
                        except:
                            previousitem = None

                    if alianzas.has_next:
                        try:
                            nextitem = alianzas.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(alianzas)
            for i in range(0, countitem):
                if(alianzas[i].id == alianza.id):
                    try:
                        previousitem = alianzas[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = alianzas[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            alianza_previous = Alianza.objects.get(pk=previousitem)
        except:
            alianza_previous = None
        try:
            alianza_next = Alianza.objects.get(pk=nextitem)
        except:
            alianza_next = None

        context['alianza_previous'] = alianza_previous
        context['alianza_next'] = alianza_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Alianza " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('upromociones:list_alianza'))
                #return render_to_response(self.template_name, self.get_context_data())


class AlianzaDelete(DeleteView):
    model = Alianza
    form_class = AlianzaForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app institución
class InstitucionListView(ListView):
    model = Institucion
    paginate_by = 10
    context_object_name = 'instituciones'
    template_name = 'institucion_lista.html'

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
        context = super(InstitucionListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['alianza__alianza',
                                             'nombre',
                                             'cuit',
                                             'pagina_web',
                                             'persona_contacto',
                                             'telefono',
                                             'telefono_movil',
                                             'email', ])
            lista_institucion = Institucion.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['alianza__alianza',
                                             'nombre',
                                             'cuit',
                                             'pagina_web',
                                             'persona_contacto',
                                             'telefono',
                                             'telefono_movil',
                                             'email', ])
            lista_institucion = Institucion.objects.filter(entry_query)
        elif order_by:
            lista_institucion = Institucion.objects.all().order_by(order_by)
        else:
            lista_institucion = Institucion.objects.all()

        paginator = Paginator(lista_institucion, 10)
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
            entry_query = get_query(search, ['alianza__alianza',
                                             'nombre',
                                             'cuit',
                                             'pagina_web',
                                             'persona_contacto',
                                             'telefono',
                                             'telefono_movil',
                                             'email', ])
            queryset = Institucion.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['alianza__alianza',
                                             'nombre',
                                             'cuit',
                                             'pagina_web',
                                             'persona_contacto',
                                             'telefono',
                                             'telefono_movil',
                                             'email', ])
            queryset = Institucion.objects.filter(entry_query)
        elif order_by:
            queryset = Institucion.objects.all().order_by(order_by)
        else:
            queryset = Institucion.objects.all()

        return queryset


class InstitucionView(View):
    form_class = InstitucionForm
    template_name = 'institucion_add.html'

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
                return HttpResponseRedirect(reverse('upromociones:edit_institucion',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('upromociones:list_institucion'))

        return render(request, self.template_name, {'form': form})


class InstitucionUpdate(UpdateView):
    template_name = 'institucion_edit.html'
    form_class = InstitucionForm
    model = Institucion

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(InstitucionUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        institucion = Institucion.objects.get(pk=self.object.pk)
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
            lista_institucion = Institucion.objects.all().order_by(order_by)
        else:
            lista_institucion = Institucion.objects.all()

        paginator = Paginator(lista_institucion, nropag)
        # Show 25 contacts per page

        if page == '0':
            instituciones = lista_institucion
        else:
            try:
                instituciones = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                instituciones = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                instituciones = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(instituciones.object_list[i].id == institucion.id):
                    if instituciones.has_previous:
                        try:
                            previousitem = instituciones.object_list[i-1].id
                        except:
                            previousitem = None

                    if instituciones.has_next:
                        try:
                            nextitem = instituciones.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(instituciones)
            for i in range(0, countitem):
                if(instituciones[i].id == institucion.id):
                    try:
                        previousitem = instituciones[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = instituciones[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            institucion_previous = Institucion.objects.get(pk=previousitem)
        except:
            institucion_previous = None
        try:
            institucion_next = Institucion.objects.get(pk=nextitem)
        except:
            institucion_next = None

        context['institucion_previous'] = institucion_previous
        context['institucion_next'] = institucion_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Institucion " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('upromociones:list_institucion'))
                #return render_to_response(self.template_name, self.get_context_data())


class InstitucionDelete(DeleteView):
    model = Institucion
    form_class = InstitucionForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app persona aliado
class PersonaAliadoListView(ListView):
    model = PersonaAliado
    paginate_by = 10
    context_object_name = 'personaaliados'
    template_name = 'personaaliado_lista.html'

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
        context = super(PersonaAliadoListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['institucion__nombre',
                                             'dni',
                                             'nombre',
                                             'telefono',
                                             'telefono_movil_1',
                                             'telefono_movil_2',
                                             'email_principal',
                                             'email_secundario', ])
            lista_personaaliado = PersonaAliado.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['institucion__nombre',
                                             'dni',
                                             'nombre',
                                             'telefono',
                                             'telefono_movil_1',
                                             'telefono_movil_2',
                                             'email_principal',
                                             'email_secundario', ])
            lista_personaaliado = PersonaAliado.objects.filter(entry_query)
        elif order_by:
            lista_personaaliado = PersonaAliado.objects.all().order_by(order_by)
        else:
            lista_personaaliado = PersonaAliado.objects.all()

        paginator = Paginator(lista_personaaliado, 10)
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
            entry_query = get_query(search, ['institucion__nombre',
                                             'dni',
                                             'nombre',
                                             'telefono',
                                             'telefono_movil_1',
                                             'telefono_movil_2',
                                             'email_principal',
                                             'email_secundario', ])
            queryset = PersonaAliado.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['institucion__nombre',
                                             'dni',
                                             'nombre',
                                             'telefono',
                                             'telefono_movil_1',
                                             'telefono_movil_2',
                                             'email_principal',
                                             'email_secundario', ])
            queryset = PersonaAliado.objects.filter(entry_query)
        elif order_by:
            queryset = PersonaAliado.objects.all().order_by(order_by)
        else:
            queryset = PersonaAliado.objects.all()

        return queryset


class PersonaAliadoView(View):
    form_class = PersonaAliadoForm
    template_name = 'personaaliado_add.html'

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
                return HttpResponseRedirect(reverse('upromociones:edit_personaaliado',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('upromociones:list_personaaliado'))

        return render(request, self.template_name, {'form': form})


class PersonaAliadoUpdate(UpdateView):
    template_name = 'personaaliado_edit.html'
    form_class = PersonaAliadoForm
    model = PersonaAliado

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PersonaAliadoUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        personaaliado = PersonaAliado.objects.get(pk=self.object.pk)
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
            lista_personaaliado = PersonaAliado.objects.all().order_by(order_by)
        else:
            lista_personaaliado = PersonaAliado.objects.all()

        paginator = Paginator(lista_personaaliado, nropag)
        # Show 25 contacts per page

        if page == '0':
            personaaliados = lista_personaaliado
        else:
            try:
                personaaliados = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                personaaliados = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                personaaliados = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(personaaliados.object_list[i].id == personaaliado.id):
                    if personaaliados.has_previous:
                        try:
                            previousitem = personaaliados.object_list[i-1].id
                        except:
                            previousitem = None

                    if personaaliados.has_next:
                        try:
                            nextitem = personaaliados.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(personaaliados)
            for i in range(0, countitem):
                if(personaaliados[i].id == personaaliado.id):
                    try:
                        previousitem = personaaliados[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = personaaliados[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            personaaliado_previous = PersonaAliado.objects.get(pk=previousitem)
        except:
            personaaliado_previous = None
        try:
            personaaliado_next = PersonaAliado.objects.get(pk=nextitem)
        except:
            personaaliado_next = None

        context['personaaliado_previous'] = personaaliado_previous
        context['personaaliado_next'] = personaaliado_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "PersonaAliado " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('upromociones:list_personaaliado'))
                #return render_to_response(self.template_name, self.get_context_data())


class PersonaAliadoDelete(DeleteView):
    model = PersonaAliado
    form_class = PersonaAliadoForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app fuente de promoción
class FuenteDePromocionListView(ListView):
    model = FuenteDePromocion
    paginate_by = 10
    context_object_name = 'fuentedepromociones'
    template_name = 'fuentedepromocion_lista.html'

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
        context = super(FuenteDePromocionListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['medio_especifico__medio_especifico',
                                             'tipo_de_referido__tipo_de_referido',
                                             'barrio__barrio',
                                             'cliente__nombre',
                                             'nombre_referido',
                                             'telefono_referido',
                                             'persona_aliado__nombre',
                                             'institucion_aliado',
                                             'alianza', ])
            lista_fuentedepromocion = FuenteDePromocion.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['medio_especifico__medio_especifico',
                                             'tipo_de_referido__tipo_de_referido',
                                             'barrio__barrio',
                                             'cliente__nombre',
                                             'nombre_referido',
                                             'telefono_referido',
                                             'persona_aliado__nombre',
                                             'institucion_aliado',
                                             'alianza', ])
            lista_fuentedepromocion = FuenteDePromocion.objects.filter(entry_query)
        elif order_by:
            lista_fuentedepromocion = FuenteDePromocion.objects.all().order_by(order_by)
        else:
            lista_fuentedepromocion = FuenteDePromocion.objects.all()

        paginator = Paginator(lista_fuentedepromocion, 10)
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
            entry_query = get_query(search, ['medio_especifico__medio_especifico',
                                             'tipo_de_referido__tipo_de_referido',
                                             'barrio__barrio',
                                             'cliente__nombre',
                                             'nombre_referido',
                                             'telefono_referido',
                                             'persona_aliado__nombre',
                                             'institucion_aliado',
                                             'alianza', ])
            queryset = FuenteDePromocion.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['medio_especifico__medio_especifico',
                                             'tipo_de_referido__tipo_de_referido',
                                             'barrio__barrio',
                                             'cliente__nombre',
                                             'nombre_referido',
                                             'telefono_referido',
                                             'persona_aliado__nombre',
                                             'institucion_aliado',
                                             'alianza', ])
            queryset = FuenteDePromocion.objects.filter(entry_query)
        elif order_by:
            queryset = FuenteDePromocion.objects.all().order_by(order_by)
        else:
            queryset = FuenteDePromocion.objects.all()

        return queryset


class FuenteDePromocionView(View):
    form_class = FuenteDePromocionForm
    template_name = 'fuentedepromocion_add.html'

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
                return HttpResponseRedirect(reverse('upromociones:edit_fuentedepromocion',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('upromociones:list_fuentedepromocion'))

        return render(request, self.template_name, {'form': form})


class FuenteDePromocionUpdate(UpdateView):
    template_name = 'fuentedepromocion_edit.html'
    form_class = FuenteDePromocionForm
    model = FuenteDePromocion

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FuenteDePromocionUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        fuentedepromocion = FuenteDePromocion.objects.get(pk=self.object.pk)
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
            lista_fuentedepromocion = FuenteDePromocion.objects.all().order_by(order_by)
        else:
            lista_fuentedepromocion = FuenteDePromocion.objects.all()

        paginator = Paginator(lista_fuentedepromocion, nropag)
        # Show 25 contacts per page

        if page == '0':
            fuentedepromociones = lista_fuentedepromocion
        else:
            try:
                fuentedepromociones = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                fuentedepromociones = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                fuentedepromociones = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(fuentedepromociones.object_list[i].id == fuentedepromocion.id):
                    if fuentedepromociones.has_previous:
                        try:
                            previousitem = fuentedepromociones.object_list[i-1].id
                        except:
                            previousitem = None

                    if fuentedepromociones.has_next:
                        try:
                            nextitem = fuentedepromociones.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(fuentedepromociones)
            for i in range(0, countitem):
                if(fuentedepromociones[i].id == fuentedepromocion.id):
                    try:
                        previousitem = fuentedepromociones[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = fuentedepromociones[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            fuentedepromocion_previous = FuenteDePromocion.objects.get(pk=previousitem)
        except:
            fuentedepromocion_previous = None
        try:
            fuentedepromocion_next = FuenteDePromocion.objects.get(pk=nextitem)
        except:
            fuentedepromocion_next = None

        context['fuentedepromocion_previous'] = fuentedepromocion_previous
        context['fuentedepromocion_next'] = fuentedepromocion_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Fuente de promoción " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('upromociones:list_fuentedepromocion'))
                #return render_to_response(self.template_name, self.get_context_data())


class FuenteDePromocionDelete(DeleteView):
    model = FuenteDePromocion
    form_class = FuenteDePromocionForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())
