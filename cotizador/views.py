"""
Docstring documentación pendiente

"""

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, View, UpdateView, DeleteView
from cotizador.models import Cotizador
from cotizador.forms import CotizadorForm
from mtvmcotizacionv02.views import valor_Personalizacionvisual, get_query
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# app cotizador
class CotizadorListView(ListView):
    model = Cotizador
    paginate_by = 10
    context_object_name = 'cotizadores'
    template_name = 'cotizador_lista.html'

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
        context = super(CotizadorListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['id_trabajador__nombre',
                                             'id_trabajador__apellido', ])
            lista_cotizador = Cotizador.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['id_trabajador__nombre',
                                             'id_trabajador__apellido', ])
            lista_cotizador = Cotizador.objects.filter(entry_query)
        elif order_by:
            lista_cotizador = Cotizador.objects.all().order_by(order_by)
        else:
            lista_cotizador = Cotizador.objects.all()

        paginator = Paginator(lista_cotizador, 10)
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
            entry_query = get_query(search, ['id_trabajador__nombre',
                                             'id_trabajador__apellido', ])
            queryset = Cotizador.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['id_trabajador__nombre',
                                             'id_trabajador__apellido', ])
            queryset = Cotizador.objects.filter(entry_query)
        elif order_by:
            queryset = Cotizador.objects.all().order_by(order_by)
        else:
            queryset = Cotizador.objects.all()

        return queryset


class CotizadorView(View):
    form_class = CotizadorForm
    template_name = 'cotizador_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Cotizador '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('ucotizadores:edit_cotizador',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Cotizador '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('ucotizadores:list_cotizador'))

        return render(request, self.template_name, {'form': form})


class CotizadorUpdate(UpdateView):
    template_name = 'cotizador_edit.html'
    form_class = CotizadorForm
    model = Cotizador

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CotizadorUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        cotizador = Cotizador.objects.get(pk=self.object.pk)
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
            lista_cotizador = Cotizador.objects.all().order_by(order_by)
        else:
            lista_cotizador = Cotizador.objects.all()

        paginator = Paginator(lista_cotizador, nropag)
        # Show 25 contacts per page

        if page == '0':
            cotizadores = lista_cotizador
        else:
            try:
                cotizadores = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                cotizadores = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                cotizadores = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(cotizadores.object_list[i].id == cotizador.id):
                    if cotizadores.has_previous:
                        try:
                            previousitem = cotizadores.object_list[i-1].id
                        except:
                            previousitem = None

                    if cotizadores.has_next:
                        try:
                            nextitem = cotizadores.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(cotizadores)
            for i in range(0, countitem):
                if(cotizadores[i].id == cotizador.id):
                    try:
                        previousitem = cotizadores[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = cotizadores[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            cotizador_previous = Cotizador.objects.get(pk=previousitem)
        except:
            cotizador_previous = None
        try:
            cotizador_next = Cotizador.objects.get(pk=nextitem)
        except:
            cotizador_next = None

        context['cotizador_previous'] = cotizador_previous
        context['cotizador_next'] = cotizador_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Cotizador " + str(self.object) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Cotizador '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                messages.success(self.request, "Cotizador '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(reverse('ucotizadores:list_cotizador'))
                #return render_to_response(self.template_name, self.get_context_data())


class CotizadorDelete(DeleteView):
    model = Cotizador
    form_class = CotizadorForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            messages.success(self.request, "Cotizador '" + str(self.obj) + "'  eliminado con éxito.")
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())
