"""
Docstring documentación pendiente

"""

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.generic import ListView, View, UpdateView, DeleteView
from mensaje.models import TipoDeMensaje, Mensaje
from mensaje.forms import TipoDeMensajeForm, MensajeForm
from mtvmcotizacionv02.views import valor_Personalizacionvisual, get_query
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# app tipo de mensaje
class TipoDeMensajeListView(ListView):
    model = TipoDeMensaje
    paginate_by = 10
    context_object_name = 'tiposdemensajes'
    template_name = 'tipodemensaje_lista.html'

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
        context = super(TipoDeMensajeListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")
        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_mensaje',
                                             'descripcion', ])
            lista_mensaje = TipoDeMensaje.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_mensaje',
                                             'descripcion', ])
            lista_mensaje = TipoDeMensaje.objects.filter(entry_query)
        elif order_by:
            lista_mensaje = TipoDeMensaje.objects.all().order_by(order_by)
        else:
            lista_mensaje = TipoDeMensaje.objects.all()

        paginator = Paginator(lista_mensaje, 10)
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
            entry_query = get_query(search, ['tipo_de_mensaje',
                                             'descripcion', ])
            queryset = TipoDeMensaje.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_mensaje',
                                             'descripcion', ])
            queryset = TipoDeMensaje.objects.filter(entry_query)
        elif order_by:
            queryset = TipoDeMensaje.objects.all().order_by(order_by)
        else:
            queryset = TipoDeMensaje.objects.all()

        return queryset


class TipoDeMensajeView(View):
    form_class = TipoDeMensajeForm
    template_name = 'tipodemensaje_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Tipo de mensaje '" + str(id_reg) + "'  agregado con éxito.",
                                 extra_tags=reverse('umensajes:list_tipodemensaje'))
                return HttpResponseRedirect(reverse('umensajes:edit_tipodemensaje',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Tipo de mensaje '" + str(id_reg) + "'  agregado con éxito.")
                return HttpResponseRedirect(reverse('umensajes:list_tipodemensaje'))

        return render(request, self.template_name, {'form': form})


class TipoDeMensajeUpdate(UpdateView):
    template_name = 'tipodemensaje_edit.html'
    form_class = TipoDeMensajeForm
    model = TipoDeMensaje

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TipoDeMensajeUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        tipodemensaje = TipoDeMensaje.objects.get(pk=self.object.pk)
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
            lista_tipodemensaje = TipoDeMensaje.objects.all().order_by(order_by)
        else:
            lista_tipodemensaje = TipoDeMensaje.objects.all()

        paginator = Paginator(lista_tipodemensaje, nropag)
        # Show 25 contacts per page

        if page == '0':
            tipodemensajes = lista_tipodemensaje
        else:
            try:
                tipodemensajes = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                tipodemensajes = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                tipodemensajes = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(tipodemensajes.object_list[i].id == tipodemensaje.id):
                    if tipodemensajes.has_previous:
                        try:
                            previousitem = tipodemensajes.object_list[i-1].id
                        except:
                            previousitem = None

                    if tipodemensajes.has_next:
                        try:
                            nextitem = tipodemensajes.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(tipodemensajes)
            for i in range(0, countitem):
                if(tipodemensajes[i].id == tipodemensaje.id):
                    try:
                        previousitem = tipodemensajes[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = tipodemensajes[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            tipodemensaje_previous = TipoDeMensaje.objects.get(pk=previousitem)
        except:
            tipodemensaje_previous = None
        try:
            tipodemensaje_next = TipoDeMensaje.objects.get(pk=nextitem)
        except:
            tipodemensaje_next = None

        context['tipodemensaje_previous'] = tipodemensaje_previous
        context['tipodemensaje_next'] = tipodemensaje_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Tipo de mensaje '" + str(self.object) + "'  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Tipo de mensaje '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                messages.success(self.request, "Tipo de mensaje '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(reverse('umensajes:list_tipodemensaje'))
                #return render_to_response(self.template_name, self.get_context_data())


class TipoDeMensajeDelete(DeleteView):
    model = TipoDeMensaje
    form_class = TipoDeMensajeForm
    template_name = 'server_confirm_delete.html'

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
        messages.success(self.request, "Tipo de Mensaje " + str(self.obj) + " eliminado con éxito.", extra_tags=next)
        return render(request, '../../mensaje/templates/mensaje.html', {'obj': context})


# app mensaje
class MensajeListView(ListView):
    model = Mensaje
    paginate_by = 10
    context_object_name = 'mensajes'
    template_name = 'mensaje_lista.html'

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
        context = super(MensajeListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")
        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_mensaje__tipo_de_mensaje',
                                             'codigo',
                                             'mensaje',
                                             'descripcion', ])
            lista_mensaje = Mensaje.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_mensaje__tipo_de_mensaje',
                                             'codigo',
                                             'mensaje',
                                             'descripcion', ])
            lista_mensaje = Mensaje.objects.filter(entry_query)
        elif order_by:
            lista_mensaje = Mensaje.objects.all().order_by(order_by)
        else:
            lista_mensaje = Mensaje.objects.all()

        paginator = Paginator(lista_mensaje, 10)
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
            entry_query = get_query(search, ['tipo_de_mensaje__tipo_de_mensaje',
                                             'codigo',
                                             'mensaje',
                                             'descripcion', ])
            queryset = Mensaje.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_mensaje__tipo_de_mensaje',
                                             'codigo',
                                             'mensaje',
                                             'descripcion', ])
            queryset = Mensaje.objects.filter(entry_query)
        elif order_by:
            queryset = Mensaje.objects.all().order_by(order_by)
        else:
            queryset = Mensaje.objects.all()

        return queryset


class MensajeView(View):
    form_class = MensajeForm
    template_name = 'mensaje_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Mensaje '" + str(id_reg) + "'  agregado con éxito.",
                                 extra_tags=reverse('umensajes:list_mensaje'))
                return HttpResponseRedirect(reverse('umensajes:edit_mensaje',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Mensaje '" + str(id_reg) + "'  agregado con éxito.")
                return HttpResponseRedirect(reverse('umensajes:list_mensaje'))

        return render(request, self.template_name, {'form': form})


class MensajeUpdate(UpdateView):
    template_name = 'mensaje_edit.html'
    form_class = MensajeForm
    model = Mensaje

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MensajeUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        mensaje = Mensaje.objects.get(pk=self.object.pk)
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
            lista_mensaje = Mensaje.objects.all().order_by(order_by)
        else:
            lista_mensaje = Mensaje.objects.all()

        paginator = Paginator(lista_mensaje, nropag)
        # Show 25 contacts per page

        if page == '0':
            mensajes = lista_mensaje
        else:
            try:
                mensajes = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                mensajes = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                mensajes = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(mensajes.object_list[i].id == mensaje.id):
                    if mensajes.has_previous:
                        try:
                            previousitem = mensajes.object_list[i-1].id
                        except:
                            previousitem = None

                    if mensajes.has_next:
                        try:
                            nextitem = mensajes.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(mensajes)
            for i in range(0, countitem):
                if(mensajes[i].id == mensaje.id):
                    try:
                        previousitem = mensajes[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = mensajes[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            mensaje_previous = Mensaje.objects.get(pk=previousitem)
        except:
            mensaje_previous = None
        try:
            mensaje_next = Mensaje.objects.get(pk=nextitem)
        except:
            mensaje_next = None

        context['mensaje_previous'] = mensaje_previous
        context['mensaje_next'] = mensaje_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Mensaje '" + str(self.object) + "'  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Mensaje '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                return render_to_response(self.template_name, self.get_context_data())


class MensajeDelete(DeleteView):
    model = Mensaje
    form_class = MensajeForm
    template_name = 'server_confirm_delete.html'

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
        messages.success(self.request, "Mensaje " + str(self.obj) + " eliminado con éxito.", extra_tags=next)
        return render(request, '../../mensaje/templates/mensaje.html', {'obj': context})
