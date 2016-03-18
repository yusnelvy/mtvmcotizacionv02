"""
Docstring documentación pendiente

"""

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.generic import ListView, View, UpdateView, DeleteView
from servicio.models import Servicio, ComplejidadServicio, PrecioDeServicio, \
    HerramientasPorServicio
from servicio.forms import ServicioForm, ComplejidadServicioForm, \
    PrecioDeServicioForm, HerramientasPorServicioForm
from mtvmcotizacionv02.views import valor_Personalizacionvisual, get_query
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# app servicio
class ServicioListView(ListView):
    model = Servicio
    paginate_by = 10
    context_object_name = 'servicios'
    template_name = 'servicio_lista.html'

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
        context = super(ServicioListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['servicio',
                                             'unidad_de_venta__unidad',
                                             'descripcion', ])
            lista_servicio = Servicio.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['servicio',
                                             'unidad_de_venta__unidad',
                                             'descripcion', ])
            lista_servicio = Servicio.objects.filter(entry_query)
        elif order_by:
            lista_servicio = Servicio.objects.all().order_by(order_by)
        else:
            lista_servicio = Servicio.objects.all()

        paginator = Paginator(lista_servicio, 10)
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
            entry_query = get_query(search, ['servicio',
                                             'unidad_de_venta__unidad',
                                             'descripcion', ])
            queryset = Servicio.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['servicio',
                                             'unidad_de_venta__unidad',
                                             'descripcion', ])
            queryset = Servicio.objects.filter(entry_query)
        elif order_by:
            queryset = Servicio.objects.all().order_by(order_by)
        else:
            queryset = Servicio.objects.all()

        return queryset


class ServicioView(View):
    form_class = ServicioForm
    template_name = 'servicio_add.html'

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
                return HttpResponseRedirect(reverse('uservicios:edit_servicio',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('uservicios:list_servicio'))

        return render(request, self.template_name, {'form': form})


class ServicioUpdate(UpdateView):
    template_name = 'servicio_edit.html'
    form_class = ServicioForm
    model = Servicio

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ServicioUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        servicio = Servicio.objects.get(pk=self.object.pk)
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
            lista_servicio = Servicio.objects.all().order_by(order_by)
        else:
            lista_servicio = Servicio.objects.all()

        paginator = Paginator(lista_servicio, nropag)
        # Show 25 contacts per page

        if page == '0':
            servicios = lista_servicio
        else:
            try:
                servicios = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                servicios = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                servicios = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(servicios.object_list[i].id == servicio.id):
                    if servicios.has_previous:
                        try:
                            previousitem = servicios.object_list[i-1].id
                        except:
                            previousitem = None

                    if servicios.has_next:
                        try:
                            nextitem = servicios.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(servicios)
            for i in range(0, countitem):
                if(servicios[i].id == servicio.id):
                    try:
                        previousitem = servicios[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = servicios[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            servicio_previous = Servicio.objects.get(pk=previousitem)
        except:
            servicio_previous = None
        try:
            servicio_next = Servicio.objects.get(pk=nextitem)
        except:
            servicio_next = None

        context['servicio_previous'] = servicio_previous
        context['servicio_next'] = servicio_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Servicio " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('uservicios:list_servicio'))
                #return render_to_response(self.template_name, self.get_context_data())


class ServicioDelete(DeleteView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app complejidad servicio
class ComplejidadServicioListView(ListView):
    model = ComplejidadServicio
    paginate_by = 10
    context_object_name = 'complejidadservicios'
    template_name = 'complejidadservicio_lista.html'

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
        context = super(ComplejidadServicioListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['servicio__servicio',
                                             'porcentaje',
                                             'descripcion', ])
            lista_complejidadservicio = ComplejidadServicio.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['servicio__servicio',
                                             'porcentaje',
                                             'descripcion', ])
            lista_complejidadservicio = ComplejidadServicio.objects.filter(entry_query)
        elif order_by:
            lista_complejidadservicio = ComplejidadServicio.objects.all().order_by(order_by)
        else:
            lista_complejidadservicio = ComplejidadServicio.objects.all()

        paginator = Paginator(lista_complejidadservicio, 10)
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
            entry_query = get_query(search, ['servicio__servicio',
                                             'porcentaje',
                                             'descripcion', ])
            queryset = ComplejidadServicio.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['servicio__servicio',
                                             'porcentaje',
                                             'descripcion', ])
            queryset = ComplejidadServicio.objects.filter(entry_query)
        elif order_by:
            queryset = ComplejidadServicio.objects.all().order_by(order_by)
        else:
            queryset = ComplejidadServicio.objects.all()

        return queryset


class ComplejidadServicioView(View):
    form_class = ComplejidadServicioForm
    template_name = 'complejidadservicio_add.html'

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
                return HttpResponseRedirect(reverse('uservicios:edit_complejidadservicio',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('uservicios:list_complejidadservicio'))

        return render(request, self.template_name, {'form': form})


class ComplejidadServicioUpdate(UpdateView):
    template_name = 'complejidadservicio_edit.html'
    form_class = ComplejidadServicioForm
    model = ComplejidadServicio

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ComplejidadServicioUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        complejidadservicio = ComplejidadServicio.objects.get(pk=self.object.pk)
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
            lista_complejidadservicio = ComplejidadServicio.objects.all().order_by(order_by)
        else:
            lista_complejidadservicio = ComplejidadServicio.objects.all()

        paginator = Paginator(lista_complejidadservicio, nropag)
        # Show 25 contacts per page

        if page == '0':
            complejidadservicios = lista_complejidadservicio
        else:
            try:
                complejidadservicios = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                complejidadservicios = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                complejidadservicios = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(complejidadservicios.object_list[i].id == complejidadservicio.id):
                    if complejidadservicios.has_previous:
                        try:
                            previousitem = complejidadservicios.object_list[i-1].id
                        except:
                            previousitem = None

                    if complejidadservicios.has_next:
                        try:
                            nextitem = complejidadservicios.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(complejidadservicios)
            for i in range(0, countitem):
                if(complejidadservicios[i].id == complejidadservicio.id):
                    try:
                        previousitem = complejidadservicios[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = complejidadservicios[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            complejidadservicio_previous = ComplejidadServicio.objects.get(pk=previousitem)
        except:
            complejidadservicio_previous = None
        try:
            complejidadservicio_next = ComplejidadServicio.objects.get(pk=nextitem)
        except:
            complejidadservicio_next = None

        context['complejidadservicio_previous'] = complejidadservicio_previous
        context['complejidadservicio_next'] = complejidadservicio_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Complejidad de servicio " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('uservicios:list_complejidadservicio'))
                #return render_to_response(self.template_name, self.get_context_data())


class ComplejidadServicioDelete(DeleteView):
    model = ComplejidadServicio
    form_class = ComplejidadServicioForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app precio de servicio
class PrecioDeServicioListView(ListView):
    model = PrecioDeServicio
    paginate_by = 10
    context_object_name = 'preciodeservicios'
    template_name = 'preciodeservicio_lista.html'

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
        context = super(PrecioDeServicioListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['servicio__servicio',
                                             'precio_base',
                                             'cantidad_de_gracia', ])
            lista_preciodeservicio = PrecioDeServicio.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['servicio__servicio',
                                             'precio_base',
                                             'cantidad_de_gracia', ])
            lista_preciodeservicio = PrecioDeServicio.objects.filter(entry_query)
        elif order_by:
            lista_preciodeservicio = PrecioDeServicio.objects.all().order_by(order_by)
        else:
            lista_preciodeservicio = PrecioDeServicio.objects.all()

        paginator = Paginator(lista_preciodeservicio, 10)
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
            entry_query = get_query(search, ['servicio__servicio',
                                             'precio_base',
                                             'cantidad_de_gracia', ])
            queryset = PrecioDeServicio.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['servicio__servicio',
                                             'precio_base',
                                             'cantidad_de_gracia', ])
            queryset = PrecioDeServicio.objects.filter(entry_query)
        elif order_by:
            queryset = PrecioDeServicio.objects.all().order_by(order_by)
        else:
            queryset = PrecioDeServicio.objects.all()

        return queryset


class PrecioDeServicioView(View):
    form_class = PrecioDeServicioForm
    template_name = 'preciodeservicio_add.html'

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
                return HttpResponseRedirect(reverse('uservicios:edit_preciodeservicio',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('uservicios:list_preciodeservicio'))

        return render(request, self.template_name, {'form': form})


class PrecioDeServicioUpdate(UpdateView):
    template_name = 'preciodeservicio_edit.html'
    form_class = PrecioDeServicioForm
    model = PrecioDeServicio

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PrecioDeServicioUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        preciodeservicio = PrecioDeServicio.objects.get(pk=self.object.pk)
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
            lista_preciodeservicio = PrecioDeServicio.objects.all().order_by(order_by)
        else:
            lista_preciodeservicio = PrecioDeServicio.objects.all()

        paginator = Paginator(lista_preciodeservicio, nropag)
        # Show 25 contacts per page

        if page == '0':
            preciodeservicios = lista_preciodeservicio
        else:
            try:
                preciodeservicios = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                preciodeservicios = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                preciodeservicios = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(preciodeservicios.object_list[i].id == preciodeservicio.id):
                    if preciodeservicios.has_previous:
                        try:
                            previousitem = preciodeservicios.object_list[i-1].id
                        except:
                            previousitem = None

                    if preciodeservicios.has_next:
                        try:
                            nextitem = preciodeservicios.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(preciodeservicios)
            for i in range(0, countitem):
                if(preciodeservicios[i].id == preciodeservicio.id):
                    try:
                        previousitem = preciodeservicios[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = preciodeservicios[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            preciodeservicio_previous = PrecioDeServicio.objects.get(pk=previousitem)
        except:
            preciodeservicio_previous = None
        try:
            preciodeservicio_next = PrecioDeServicio.objects.get(pk=nextitem)
        except:
            preciodeservicio_next = None

        context['preciodeservicio_previous'] = preciodeservicio_previous
        context['preciodeservicio_next'] = preciodeservicio_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Complejidad de servicio " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('uservicios:list_preciodeservicio'))
                #return render_to_response(self.template_name, self.get_context_data())


class PrecioDeServicioDelete(DeleteView):
    model = PrecioDeServicio
    form_class = PrecioDeServicioForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app herramienta por servicio
class HerramientasPorServicioListView(ListView):
    model = HerramientasPorServicio
    paginate_by = 10
    context_object_name = 'herramientaporservicios'
    template_name = 'herramientaporservicio_lista.html'

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
        context = super(HerramientasPorServicioListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['servicio__servicio',
                                             'herramienta__herramienta',
                                             'cantidad', ])
            lista_herramientaporservicio = HerramientasPorServicio.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['servicio__servicio',
                                             'herramienta__herramienta',
                                             'cantidad', ])
            lista_herramientaporservicio = HerramientasPorServicio.objects.filter(entry_query)
        elif order_by:
            lista_herramientaporservicio = HerramientasPorServicio.objects.all().order_by(order_by)
        else:
            lista_herramientaporservicio = HerramientasPorServicio.objects.all()

        paginator = Paginator(lista_herramientaporservicio, 10)
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
            entry_query = get_query(search, ['servicio__servicio',
                                             'herramienta__herramienta',
                                             'cantidad', ])
            queryset = HerramientasPorServicio.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['servicio__servicio',
                                             'herramienta__herramienta',
                                             'cantidad', ])
            queryset = HerramientasPorServicio.objects.filter(entry_query)
        elif order_by:
            queryset = HerramientasPorServicio.objects.all().order_by(order_by)
        else:
            queryset = HerramientasPorServicio.objects.all()

        return queryset


class HerramientasPorServicioView(View):
    form_class = HerramientasPorServicioForm
    template_name = 'herramientaporservicio_add.html'

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
                return HttpResponseRedirect(reverse('uservicios:edit_herramientaporservicio',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('uservicios:list_herramientaporservicio'))

        return render(request, self.template_name, {'form': form})


class HerramientasPorServicioUpdate(UpdateView):
    template_name = 'herramientaporservicio_edit.html'
    form_class = HerramientasPorServicioForm
    model = HerramientasPorServicio

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HerramientasPorServicioUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        herramientaporservicio = HerramientasPorServicio.objects.get(pk=self.object.pk)
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
            lista_herramientaporservicio = HerramientasPorServicio.objects.all().order_by(order_by)
        else:
            lista_herramientaporservicio = HerramientasPorServicio.objects.all()

        paginator = Paginator(lista_herramientaporservicio, nropag)
        # Show 25 contacts per page

        if page == '0':
            herramientaporservicios = lista_herramientaporservicio
        else:
            try:
                herramientaporservicios = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                herramientaporservicios = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                herramientaporservicios = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(herramientaporservicios.object_list[i].id == herramientaporservicio.id):
                    if herramientaporservicios.has_previous:
                        try:
                            previousitem = herramientaporservicios.object_list[i-1].id
                        except:
                            previousitem = None

                    if herramientaporservicios.has_next:
                        try:
                            nextitem = herramientaporservicios.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(herramientaporservicios)
            for i in range(0, countitem):
                if(herramientaporservicios[i].id == herramientaporservicio.id):
                    try:
                        previousitem = herramientaporservicios[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = herramientaporservicios[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            herramientaporservicio_previous = HerramientasPorServicio.objects.get(pk=previousitem)
        except:
            herramientaporservicio_previous = None
        try:
            herramientaporservicio_next = HerramientasPorServicio.objects.get(pk=nextitem)
        except:
            herramientaporservicio_next = None

        context['herramientaporservicio_previous'] = herramientaporservicio_previous
        context['herramientaporservicio_next'] = herramientaporservicio_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Complejidad de servicio " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('uservicios:list_herramientaporservicio'))
                #return render_to_response(self.template_name, self.get_context_data())


class HerramientasPorServicioDelete(DeleteView):
    model = HerramientasPorServicio
    form_class = HerramientasPorServicioForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())
