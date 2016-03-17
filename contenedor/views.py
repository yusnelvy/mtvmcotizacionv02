"""
Docstring documentación pendiente

"""

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.generic import ListView, View, UpdateView, DeleteView
from contenedor.models import Contenedor, ContenedorTipicoPorMueble
from contenedor.forms import ContenedorForm, ContenedorTipicoPorMuebleForm
from mtvmcotizacionv02.views import valor_Personalizacionvisual, get_query
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# app contenedor
class ContenedorListView(ListView):
    model = Contenedor
    paginate_by = 10
    context_object_name = 'contenedores'
    template_name = 'contenedor_lista.html'

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
        context = super(ContenedorListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")
        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['contenedor',
                                             'descripcion',
                                             'capacidad_de_volumen',
                                             'capacidad_de_peso',
                                             'ancho',
                                             'largo',
                                             'alto',
                                             'volumen_en_camion', ])

            lista_contenedor = Contenedor.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['contenedor',
                                             'descripcion',
                                             'capacidad_de_volumen',
                                             'capacidad_de_peso',
                                             'ancho',
                                             'largo',
                                             'alto',
                                             'volumen_en_camion', ])

            lista_contenedor = Contenedor.objects.filter(entry_query)
        elif order_by:
            lista_contenedor = Contenedor.objects.all().order_by(order_by)
        else:
            lista_contenedor = Contenedor.objects.all()

        paginator = Paginator(lista_contenedor, 10)
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
            entry_query = get_query(search, ['contenedor',
                                             'descripcion',
                                             'capacidad_de_volumen',
                                             'capacidad_de_peso',
                                             'ancho',
                                             'largo',
                                             'alto',
                                             'volumen_en_camion', ])

            queryset = Contenedor.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['contenedor',
                                             'descripcion',
                                             'capacidad_de_volumen',
                                             'capacidad_de_peso',
                                             'ancho',
                                             'largo',
                                             'alto',
                                             'volumen_en_camion', ])

            queryset = Contenedor.objects.filter(entry_query)
        elif order_by:
            queryset = Contenedor.objects.all().order_by(order_by)
        else:
            queryset = Contenedor.objects.all()

        return queryset


class ContenedorView(View):
    form_class = ContenedorForm
    template_name = 'contenedor_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Contenedor '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('ucontenedores:edit_contenedor',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Contenedor '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('ucontenedores:list_contenedor'))

        return render(request, self.template_name, {'form': form})


class ContenedorUpdate(UpdateView):
    template_name = 'contenedor_edit.html'
    form_class = ContenedorForm
    model = Contenedor

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ContenedorUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        contenedor = Contenedor.objects.get(pk=self.object.pk)
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
            lista_contenedor = Contenedor.objects.all().order_by(order_by)
        else:
            lista_contenedor = Contenedor.objects.all()

        paginator = Paginator(lista_contenedor, nropag)
        # Show 25 contacts per page

        if page == '0':
            contenedores = lista_contenedor
        else:
            try:
                contenedores = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                contenedores = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                contenedores = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(contenedores.object_list[i].id == contenedor.id):
                    if contenedores.has_previous:
                        try:
                            previousitem = contenedores.object_list[i-1].id
                        except:
                            previousitem = None

                    if contenedores.has_next:
                        try:
                            nextitem = contenedores.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(contenedores)
            for i in range(0, countitem):
                if(contenedores[i].id == contenedor.id):
                    try:
                        previousitem = contenedores[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = contenedores[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            contenedor_previous = Contenedor.objects.get(pk=previousitem)
        except:
            contenedor_previous = None
        try:
            contenedor_next = Contenedor.objects.get(pk=nextitem)
        except:
            contenedor_next = None

        context['contenedor_previous'] = contenedor_previous
        context['contenedor_next'] = contenedor_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Contenedor '" + str(self.object) + "'  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Contenedor '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                return render_to_response(self.template_name, self.get_context_data())


class ContenedorDelete(DeleteView):
    model = Contenedor
    form_class = ContenedorForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            messages.success(self.request, "Contenedor '" + str(self.object) + "'  eliminado con éxito.")
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app contenedor típico por mueble
class ContenedorTipicoPorMuebleListView(ListView):
    model = ContenedorTipicoPorMueble
    paginate_by = 10
    context_object_name = 'contenedorestipicos'
    template_name = 'contenedortipico_lista.html'

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
        context = super(ContenedorTipicoPorMuebleListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")
        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['contenedor__contenedor',
                                             'especificacion_de_mueble__especificacion_de_mueble',
                                             'cantidad', ])

            lista_contenedor = ContenedorTipicoPorMueble.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['contenedor__contenedor',
                                             'especificacion_de_mueble__especificacion_de_mueble',
                                             'cantidad', ])

            lista_contenedor = ContenedorTipicoPorMueble.objects.filter(entry_query)
        elif order_by:
            lista_contenedor = ContenedorTipicoPorMueble.objects.all().order_by(order_by)
        else:
            lista_contenedor = ContenedorTipicoPorMueble.objects.all()

        paginator = Paginator(lista_contenedor, 10)
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
            entry_query = get_query(search, ['contenedor__contenedor',
                                             'especificacion_de_mueble__especificacion_de_mueble',
                                             'cantidad', ])

            queryset = ContenedorTipicoPorMueble.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['contenedor__contenedor',
                                             'especificacion_de_mueble__especificacion_de_mueble',
                                             'cantidad', ])

            queryset = ContenedorTipicoPorMueble.objects.filter(entry_query)
        elif order_by:
            queryset = ContenedorTipicoPorMueble.objects.all().order_by(order_by)
        else:
            queryset = ContenedorTipicoPorMueble.objects.all()

        return queryset


class ContenedorTipicoPorMuebleView(View):
    form_class = ContenedorTipicoPorMuebleForm
    template_name = 'contenedortipico_add.html'

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
                return HttpResponseRedirect(reverse('ucontenedores:edit_contenedortipico',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('ucontenedores:list_contenedortipico'))

        return render(request, self.template_name, {'form': form})


class ContenedorTipicoPorMuebleUpdate(UpdateView):
    template_name = 'contenedortipico_edit.html'
    form_class = ContenedorTipicoPorMuebleForm
    model = ContenedorTipicoPorMueble

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ContenedorTipicoPorMuebleUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        contenedortipico = ContenedorTipicoPorMueble.objects.get(pk=self.object.pk)
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
            lista_contenedortipico = ContenedorTipicoPorMueble.objects.all().order_by(order_by)
        else:
            lista_contenedortipico = ContenedorTipicoPorMueble.objects.all()

        paginator = Paginator(lista_contenedortipico, nropag)
        # Show 25 contacts per page

        if page == '0':
            contenedorestipicos = lista_contenedortipico
        else:
            try:
                contenedorestipicos = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                contenedorestipicos = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                contenedorestipicos = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(contenedorestipicos.object_list[i].id == contenedortipico.id):
                    if contenedorestipicos.has_previous:
                        try:
                            previousitem = contenedorestipicos.object_list[i-1].id
                        except:
                            previousitem = None

                    if contenedorestipicos.has_next:
                        try:
                            nextitem = contenedorestipicos.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(contenedorestipicos)
            for i in range(0, countitem):
                if(contenedorestipicos[i].id == contenedortipico.id):
                    try:
                        previousitem = contenedorestipicos[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = contenedorestipicos[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            contenedortipico_previous = ContenedorTipicoPorMueble.objects.get(pk=previousitem)
        except:
            contenedortipico_previous = None
        try:
            contenedortipico_next = ContenedorTipicoPorMueble.objects.get(pk=nextitem)
        except:
            contenedortipico_next = None

        context['contenedortipico_previous'] = contenedortipico_previous
        context['contenedortipico_next'] = contenedortipico_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Contenedor típico por mueble " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return render_to_response(self.template_name, self.get_context_data())


class ContenedorTipicoPorMuebleDelete(DeleteView):
    model = ContenedorTipicoPorMueble
    form_class = ContenedorTipicoPorMuebleForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())
