"""
Docstring documentación pendiente

"""

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.generic import ListView, View, UpdateView, DeleteView
from material.models import TipoDeMaterial, Material, PrecioDeMaterial, \
    MaterialesPorServicio
from material.forms import TipoDeMaterialForm, MaterialForm, \
    PrecioDeMaterialForm, MaterialesPorServicioForm
from mtvmcotizacionv02.views import valor_Personalizacionvisual, get_query
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# app tipo de material
class TipoDeMaterialListView(ListView):
    model = TipoDeMaterial
    paginate_by = 10
    context_object_name = 'tiposdemateriales'
    template_name = 'tipodematerial_lista.html'

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
        context = super(TipoDeMaterialListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_material',
                                             'descripcion', ])

            lista_tipodematerial = TipoDeMaterial.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_material',
                                             'descripcion', ])

            lista_tipodematerial = TipoDeMaterial.objects.filter(entry_query)
        elif order_by:
            lista_tipodematerial = TipoDeMaterial.objects.all().order_by(order_by)
        else:
            lista_tipodematerial = TipoDeMaterial.objects.all()

        paginator = Paginator(lista_tipodematerial, 10)
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
            entry_query = get_query(search, ['tipo_de_material',
                                             'descripcion', ])

            queryset = TipoDeMaterial.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo_de_material',
                                             'descripcion', ])

            queryset = TipoDeMaterial.objects.filter(entry_query)
        elif order_by:
            queryset = TipoDeMaterial.objects.all().order_by(order_by)
        else:
            queryset = TipoDeMaterial.objects.all()

        return queryset


class TipoDeMaterialView(View):
    form_class = TipoDeMaterialForm
    template_name = 'tipodematerial_add.html'

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
                return HttpResponseRedirect(reverse('umateriales:edit_tipodematerial',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('umateriales:list_tipodematerial'))

        return render(request, self.template_name, {'form': form})


class TipoDeMaterialUpdate(UpdateView):
    template_name = 'tipodematerial_edit.html'
    form_class = TipoDeMaterialForm
    model = TipoDeMaterial

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TipoDeMaterialUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        tipodematerial = TipoDeMaterial.objects.get(pk=self.object.pk)
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
            lista_tipodematerial = TipoDeMaterial.objects.all().order_by(order_by)
        else:
            lista_tipodematerial = TipoDeMaterial.objects.all()

        paginator = Paginator(lista_tipodematerial, nropag)
        # Show 25 contacts per page

        if page == '0':
            tiposdemateriales = lista_tipodematerial
        else:
            try:
                tiposdemateriales = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                tiposdemateriales = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                tiposdemateriales = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(tiposdemateriales.object_list[i].id == tipodematerial.id):
                    if tiposdemateriales.has_previous:
                        try:
                            previousitem = tiposdemateriales.object_list[i-1].id
                        except:
                            previousitem = None

                    if tiposdemateriales.has_next:
                        try:
                            nextitem = tiposdemateriales.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(tiposdemateriales)
            for i in range(0, countitem):
                if(tiposdemateriales[i].id == tipodematerial.id):
                    try:
                        previousitem = tiposdemateriales[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = tiposdemateriales[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            tipodematerial_previous = TipoDeMaterial.objects.get(pk=previousitem)
        except:
            tipodematerial_previous = None
        try:
            tipodematerial_next = TipoDeMaterial.objects.get(pk=nextitem)
        except:
            tipodematerial_next = None

        context['tipodematerial_previous'] = tipodematerial_previous
        context['tipodematerial_next'] = tipodematerial_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "TipoDeMaterial " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('umateriales:list_tipodematerial'))
                #return render_to_response(self.template_name, self.get_context_data())


class TipoDeMaterialDelete(DeleteView):
    model = TipoDeMaterial
    form_class = TipoDeMaterialForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app material
class MaterialListView(ListView):
    model = Material
    paginate_by = 10
    context_object_name = 'materiales'
    template_name = 'material_lista.html'

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
        context = super(MaterialListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['material',
                                             'tipo_de_material__tipo_de_material',
                                             'descripcion',
                                             'unidad_de_consumo__unidad',
                                             'unidad_de_venta__unidad',
                                             'relacion_consumo_venta',
                                             'ancho',
                                             'largo',
                                             'alto',
                                             'peso_unidad_consumo_kg', ])

            lista_material = Material.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['material',
                                             'tipo_de_material__tipo_de_material',
                                             'descripcion',
                                             'unidad_de_consumo__unidad',
                                             'unidad_de_venta__unidad',
                                             'relacion_consumo_venta',
                                             'ancho',
                                             'largo',
                                             'alto',
                                             'peso_unidad_consumo_kg', ])

            lista_material = Material.objects.filter(entry_query)
        elif order_by:
            lista_material = Material.objects.all().order_by(order_by)
        else:
            lista_material = Material.objects.all()

        paginator = Paginator(lista_material, 10)
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
            entry_query = get_query(search, ['material',
                                             'tipo_de_material__tipo_de_material',
                                             'descripcion',
                                             'unidad_de_consumo__unidad',
                                             'unidad_de_venta__unidad',
                                             'relacion_consumo_venta',
                                             'ancho',
                                             'largo',
                                             'alto',
                                             'peso_unidad_consumo_kg', ])

            queryset = Material.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['material',
                                             'tipo_de_material__tipo_de_material',
                                             'descripcion',
                                             'unidad_de_consumo__unidad',
                                             'unidad_de_venta__unidad',
                                             'relacion_consumo_venta',
                                             'ancho',
                                             'largo',
                                             'alto',
                                             'peso_unidad_consumo_kg', ])

            queryset = Material.objects.filter(entry_query)
        elif order_by:
            queryset = Material.objects.all().order_by(order_by)
        else:
            queryset = Material.objects.all()

        return queryset


class MaterialView(View):
    form_class = MaterialForm
    template_name = 'material_add.html'

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
                return HttpResponseRedirect(reverse('umateriales:edit_material',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('umateriales:list_material'))

        return render(request, self.template_name, {'form': form})


class MaterialUpdate(UpdateView):
    template_name = 'material_edit.html'
    form_class = MaterialForm
    model = Material

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MaterialUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        material = Material.objects.get(pk=self.object.pk)
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
            lista_material = Material.objects.all().order_by(order_by)
        else:
            lista_material = Material.objects.all()

        paginator = Paginator(lista_material, nropag)
        # Show 25 contacts per page

        if page == '0':
            materiales = lista_material
        else:
            try:
                materiales = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                materiales = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                materiales = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(materiales.object_list[i].id == material.id):
                    if materiales.has_previous:
                        try:
                            previousitem = materiales.object_list[i-1].id
                        except:
                            previousitem = None

                    if materiales.has_next:
                        try:
                            nextitem = materiales.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(materiales)
            for i in range(0, countitem):
                if(materiales[i].id == material.id):
                    try:
                        previousitem = materiales[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = materiales[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            material_previous = Material.objects.get(pk=previousitem)
        except:
            material_previous = None
        try:
            material_next = Material.objects.get(pk=nextitem)
        except:
            material_next = None

        context['material_previous'] = material_previous
        context['material_next'] = material_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Material " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('umateriales:list_material'))
                #return render_to_response(self.template_name, self.get_context_data())


class MaterialDelete(DeleteView):
    model = Material
    form_class = MaterialForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())
