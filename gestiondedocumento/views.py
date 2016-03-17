"""
Docstring documentación pendiente

"""

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.generic import ListView, View, UpdateView, DeleteView
from gestiondedocumento.models import TipoDeDocumento, EstadoDeDocumento
from gestiondedocumento.forms import TipoDeDocumentoForm, EstadoDeDocumentoForm
from mtvmcotizacionv02.views import valor_Personalizacionvisual, get_query
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# app tipo de documento
class TipoDeDocumentoListView(ListView):
    model = TipoDeDocumento
    paginate_by = 10
    context_object_name = 'tiposdedocumento'
    template_name = 'tipodedocumento_lista.html'

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
        context = super(TipoDeDocumentoListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")
        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_documento',
                                             'descripcion', ])

            lista_tipodedocumento = TipoDeDocumento.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_documento',
                                             'descripcion', ])

            lista_tipodedocumento = TipoDeDocumento.objects.filter(entry_query)
        elif order_by:
            lista_tipodedocumento = TipoDeDocumento.objects.all().order_by(order_by)
        else:
            lista_tipodedocumento = TipoDeDocumento.objects.all()

        paginator = Paginator(lista_tipodedocumento, 10)
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
            entry_query = get_query(search, ['tipo_de_documento',
                                             'descripcion', ])

            queryset = TipoDeDocumento.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_documento',
                                             'descripcion', ])

            queryset = TipoDeDocumento.objects.filter(entry_query)
        elif order_by:
            queryset = TipoDeDocumento.objects.all().order_by(order_by)
        else:
            queryset = TipoDeDocumento.objects.all()

        return queryset


class TipoDeDocumentoView(View):
    form_class = TipoDeDocumentoForm
    template_name = 'tipodedocumento_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Tipo de documento '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('ugestiondedocumentos:edit_tipodedocumento',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Tipo de documento '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('ugestiondedocumentos:list_tipodedocumento'))

        return render(request, self.template_name, {'form': form})


class TipoDeDocumentoUpdate(UpdateView):
    template_name = 'tipodedocumento_edit.html'
    form_class = TipoDeDocumentoForm
    model = TipoDeDocumento

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TipoDeDocumentoUpdate, self).get_context_data(**kwargs)
        # if self.request.user.id is not None:
        #     nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        # else:
        #     nropag = valor_Personalizacionvisual("std", "paginacion")
        nropag = 10

        tipodedocumento = TipoDeDocumento.objects.get(pk=self.object.pk)
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
            lista_tipodedocumento = TipoDeDocumento.objects.all().order_by(order_by)
        else:
            lista_tipodedocumento = TipoDeDocumento.objects.all()

        paginator = Paginator(lista_tipodedocumento, nropag)
        # Show 25 contacts per page

        if page == '0':
            tiposdedocumento = lista_tipodedocumento
        else:
            try:
                tiposdedocumento = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                tiposdedocumento = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                tiposdedocumento = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(tiposdedocumento.object_list[i].id == tipodedocumento.id):
                    if tiposdedocumento.has_previous:
                        try:
                            previousitem = tiposdedocumento.object_list[i-1].id
                        except:
                            previousitem = None

                    if tiposdedocumento.has_next:
                        try:
                            nextitem = tiposdedocumento.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(tiposdedocumento)
            for i in range(0, countitem):
                if(tiposdedocumento[i].id == tipodedocumento.id):
                    try:
                        previousitem = tiposdedocumento[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = tiposdedocumento[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            tipodedocumento_previous = TipoDeDocumento.objects.get(pk=previousitem)
        except:
            tipodedocumento_previous = None
        try:
            tipodedocumento_next = TipoDeDocumento.objects.get(pk=nextitem)
        except:
            tipodedocumento_next = None

        context['tipodedocumento_previous'] = tipodedocumento_previous
        context['tipodedocumento_next'] = tipodedocumento_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Tipo de documento '" + str(self.object) + "'  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Tipo de documento '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                return render_to_response(self.template_name, self.get_context_data())


class TipoDeDocumentoDelete(DeleteView):
    model = TipoDeDocumento
    form_class = TipoDeDocumentoForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            messages.success(self.request, "Tipo de documento '" + str(self.obj) + "'  eliminado con éxito.")
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app estado de documento
class EstadoDeDocumentoListView(ListView):
    model = EstadoDeDocumento
    paginate_by = 10
    context_object_name = 'estadosdedocumento'
    template_name = 'estadodedocumento_lista.html'

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
        context = super(EstadoDeDocumentoListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")
        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_documento__tipo_de_documento',
                                             'estado_de_documento',
                                             'descripcion', ])

            lista_estadodedocumento = EstadoDeDocumento.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_documento__tipo_de_documento',
                                             'estado_de_documento',
                                             'descripcion', ])

            lista_estadodedocumento = EstadoDeDocumento.objects.filter(entry_query)
        elif order_by:
            lista_estadodedocumento = EstadoDeDocumento.objects.all().order_by(order_by)
        else:
            lista_estadodedocumento = EstadoDeDocumento.objects.all()

        paginator = Paginator(lista_estadodedocumento, 10)
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
            entry_query = get_query(search, ['tipo_de_documento__tipo_de_documento',
                                             'estado_de_documento',
                                             'descripcion', ])

            queryset = EstadoDeDocumento.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_documento__tipo_de_documento',
                                             'estado_de_documento',
                                             'descripcion', ])

            queryset = EstadoDeDocumento.objects.filter(entry_query)
        elif order_by:
            queryset = EstadoDeDocumento.objects.all().order_by(order_by)
        else:
            queryset = EstadoDeDocumento.objects.all()

        return queryset


class EstadoDeDocumentoView(View):
    form_class = EstadoDeDocumentoForm
    template_name = 'estadodedocumento_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Estado del documento '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('ugestiondedocumentos:edit_estadodedocumento',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Estado del documento '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('ugestiondedocumentos:list_estadodedocumento'))

        return render(request, self.template_name, {'form': form})


class EstadoDeDocumentoUpdate(UpdateView):
    template_name = 'estadodedocumento_edit.html'
    form_class = EstadoDeDocumentoForm
    model = EstadoDeDocumento

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(EstadoDeDocumentoUpdate, self).get_context_data(**kwargs)
        # if self.request.user.id is not None:
        #     nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        # else:
        #     nropag = valor_Personalizacionvisual("std", "paginacion")
        nropag = 10

        estadodedocumento = EstadoDeDocumento.objects.get(pk=self.object.pk)
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
            lista_estadodedocumento = EstadoDeDocumento.objects.all().order_by(order_by)
        else:
            lista_estadodedocumento = EstadoDeDocumento.objects.all()

        paginator = Paginator(lista_estadodedocumento, nropag)
        # Show 25 contacts per page

        if page == '0':
            estadosdedocumento = lista_estadodedocumento
        else:
            try:
                estadosdedocumento = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                estadosdedocumento = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                estadosdedocumento = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(estadosdedocumento.object_list[i].id == estadodedocumento.id):
                    if estadosdedocumento.has_previous:
                        try:
                            previousitem = estadosdedocumento.object_list[i-1].id
                        except:
                            previousitem = None

                    if estadosdedocumento.has_next:
                        try:
                            nextitem = estadosdedocumento.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(estadosdedocumento)
            for i in range(0, countitem):
                if(estadosdedocumento[i].id == estadodedocumento.id):
                    try:
                        previousitem = estadosdedocumento[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = estadosdedocumento[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            estadodedocumento_previous = EstadoDeDocumento.objects.get(pk=previousitem)
        except:
            estadodedocumento_previous = None
        try:
            estadodedocumento_next = EstadoDeDocumento.objects.get(pk=nextitem)
        except:
            estadodedocumento_next = None

        context['estadodedocumento_previous'] = estadodedocumento_previous
        context['estadodedocumento_next'] = estadodedocumento_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Estado del documento '" + str(self.object) + "'  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Estado del documento '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                return render_to_response(self.template_name, self.get_context_data())


class EstadoDeDocumentoDelete(DeleteView):
    model = EstadoDeDocumento
    form_class = EstadoDeDocumentoForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            messages.success(self.request, "Estado del documento '" + str(self.obj) + "'  eliminado con éxito.")
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())
