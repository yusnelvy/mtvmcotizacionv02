"""
Docstring documentación pendiente

"""

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, View, UpdateView, DeleteView
from almacen.models import Unidad
from almacen.forms import UnidadForm
from mtvmcotizacionv02.views import valor_Personalizacionvisual, get_query
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# app unidad
class UnidadListView(ListView):
    model = Unidad
    paginate_by = 10
    context_object_name = 'unidades'
    template_name = 'unidad_lista.html'

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
        context = super(UnidadListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['unidad',
                                             'descripcion',
                                             'nombre', ])
            lista_unidad = Unidad.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['unidad',
                                             'descripcion',
                                             'nombre', ])
            lista_unidad = Unidad.objects.filter(entry_query)
        elif order_by:
            lista_unidad = Unidad.objects.all().order_by(order_by)
        else:
            lista_unidad = Unidad.objects.all()

        paginator = Paginator(lista_unidad, 10)
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
            entry_query = get_query(search, ['unidad',
                                             'descripcion',
                                             'nombre', ])
            queryset = Unidad.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['unidad',
                                             'descripcion',
                                             'nombre', ])
            queryset = Unidad.objects.filter(entry_query)
        elif order_by:
            queryset = Unidad.objects.all().order_by(order_by)
        else:
            queryset = Unidad.objects.all()

        return queryset


class UnidadView(View):
    form_class = UnidadForm
    template_name = 'unidad_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Unidad '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('ualmacenes:edit_unidad',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Unidad '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('ualmacenes:list_unidad'))

        return render(request, self.template_name, {'form': form})


class UnidadUpdate(UpdateView):
    template_name = 'unidad_edit.html'
    form_class = UnidadForm
    model = Unidad

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(UnidadUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        unidad = Unidad.objects.get(pk=self.object.pk)
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
            lista_unidad = Unidad.objects.all().order_by(order_by)
        else:
            lista_unidad = Unidad.objects.all()

        paginator = Paginator(lista_unidad, nropag)
        # Show 25 contacts per page

        if page == '0':
            unidades = lista_unidad
        else:
            try:
                unidades = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                unidades = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                unidades = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(unidades.object_list[i].id == unidad.id):
                    if unidades.has_previous:
                        try:
                            previousitem = unidades.object_list[i-1].id
                        except:
                            previousitem = None

                    if unidades.has_next:
                        try:
                            nextitem = unidades.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(unidades)
            for i in range(0, countitem):
                if(unidades[i].id == unidad.id):
                    try:
                        previousitem = unidades[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = unidades[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            unidad_previous = Unidad.objects.get(pk=previousitem)
        except:
            unidad_previous = None
        try:
            unidad_next = Unidad.objects.get(pk=nextitem)
        except:
            unidad_next = None

        context['unidad_previous'] = unidad_previous
        context['unidad_next'] = unidad_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Unidad " + str(self.object) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Unidad '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                messages.success(self.request, "Unidad '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(reverse('ualmacenes:list_unidad'))
                #return render_to_response(self.template_name, self.get_context_data())


class UnidadDelete(DeleteView):
    model = Unidad
    form_class = UnidadForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            messages.success(self.request, "Unidad '" + str(self.obj) + "'  eliminado con éxito.")
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())
