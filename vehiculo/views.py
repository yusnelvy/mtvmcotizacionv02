"""
Docstring documentación pendiente

"""

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.views.generic import ListView, View, UpdateView, DeleteView
from vehiculo.models import Vehiculo, DetalleDeVehiculo, EstadoDeVehiculo, \
    ChoferAsignado
from vehiculo.forms import VehiculoForm, DetalleDeVehiculoForm, ChoferAsignadoForm
from estadoderegistro.models import EstadoDeRegistro
from mtvmcotizacionv02.views import valor_Personalizacionvisual
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# app vehículo
class VehiculoListView(ListView):
    model = Vehiculo
    paginate_by = 10
    context_object_name = 'vehiculos'
    template_name = 'vehiculo_lista.html'

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
        context = super(VehiculoListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        if order_by:
            lista_vehiculo = Vehiculo.objects.all().order_by(order_by)
        else:
            lista_vehiculo = Vehiculo.objects.all()

        paginator = Paginator(lista_vehiculo, 10)
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
            queryset = Vehiculo.objects.all().order_by(order_by)
        else:
            queryset = Vehiculo.objects.all()

        return queryset


class VehiculoView(View):
    form_class = VehiculoForm
    template_name = 'vehiculo_add.html'

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
                return HttpResponseRedirect(reverse('uvehiculos:edit_vehiculo',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('uvehiculos:list_vehiculo'))

        return render(request, self.template_name, {'form': form})


class VehiculoUpdate(UpdateView):
    template_name = 'vehiculo_edit.html'
    form_class = VehiculoForm
    model = Vehiculo

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(VehiculoUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        vehiculo = Vehiculo.objects.get(pk=self.object.pk)
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
            lista_vehiculo = Vehiculo.objects.all().order_by(order_by)
        else:
            lista_vehiculo = Vehiculo.objects.all()

        paginator = Paginator(lista_vehiculo, nropag)
        # Show 25 contacts per page

        if page == '0':
            vehiculos = lista_vehiculo
        else:
            try:
                vehiculos = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                vehiculos = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                vehiculos = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(vehiculos.object_list[i].id == vehiculo.id):
                    if vehiculos.has_previous:
                        try:
                            previousitem = vehiculos.object_list[i-1].id
                        except:
                            previousitem = None

                    if vehiculos.has_next:
                        try:
                            nextitem = vehiculos.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(vehiculos)
            for i in range(0, countitem):
                if(vehiculos[i].id == vehiculo.id):
                    try:
                        previousitem = vehiculos[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = vehiculos[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            vehiculo_previous = Vehiculo.objects.get(pk=previousitem)
        except:
            vehiculo_previous = None
        try:
            vehiculo_next = Vehiculo.objects.get(pk=nextitem)
        except:
            vehiculo_next = None

        context['vehiculo_previous'] = vehiculo_previous
        context['vehiculo_next'] = vehiculo_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Vehiculo " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('uvehiculos:list_vehiculo'))
                #return render_to_response(self.template_name, self.get_context_data())


class VehiculoDelete(DeleteView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app detalle de vehículo
class DetalleDeVehiculoListView(ListView):
    model = DetalleDeVehiculo
    paginate_by = 10
    context_object_name = 'detalledevehiculos'
    template_name = 'detalledevehiculo_lista.html'

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
        context = super(DetalleDeVehiculoListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        if order_by:
            lista_detalledevehiculo = DetalleDeVehiculo.objects.all().order_by(order_by)
        else:
            lista_detalledevehiculo = DetalleDeVehiculo.objects.all()

        paginator = Paginator(lista_detalledevehiculo, 10)
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
            queryset = DetalleDeVehiculo.objects.all().order_by(order_by)
        else:
            queryset = DetalleDeVehiculo.objects.all()

        return queryset


class DetalleDeVehiculoView(View):
    form_class = DetalleDeVehiculoForm
    template_name = 'detalledevehiculo_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            estadoactual = EstadoDeRegistro.objects.filter(model='vehiculo',
                                                           estado__estado='Activo')

            agregarestado = EstadoDeVehiculo.objects.create(vehiculo=id_reg,
                                                            estado_de_registro_id=estadoactual[0].id,
                                                            usuario_id=2,
                                                            observecion='Creación de detalle de vehículo',
                                                            predefinido=True)
            agregarestado.save()
            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('uvehiculos:edit_detalledevehiculo',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('uvehiculos:list_detalledevehiculo'))

        return render(request, self.template_name, {'form': form})


class DetalleDeVehiculoUpdate(UpdateView):
    template_name = 'detalledevehiculo_edit.html'
    form_class = DetalleDeVehiculoForm
    model = DetalleDeVehiculo

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DetalleDeVehiculoUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        detalledevehiculo = DetalleDeVehiculo.objects.get(pk=self.object.pk)
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
            lista_detalledevehiculo = DetalleDeVehiculo.objects.all().order_by(order_by)
        else:
            lista_detalledevehiculo = DetalleDeVehiculo.objects.all()

        paginator = Paginator(lista_detalledevehiculo, nropag)
        # Show 25 contacts per page

        if page == '0':
            detalledevehiculos = lista_detalledevehiculo
        else:
            try:
                detalledevehiculos = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                detalledevehiculos = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                detalledevehiculos = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(detalledevehiculos.object_list[i].id == detalledevehiculo.id):
                    if detalledevehiculos.has_previous:
                        try:
                            previousitem = detalledevehiculos.object_list[i-1].id
                        except:
                            previousitem = None

                    if detalledevehiculos.has_next:
                        try:
                            nextitem = detalledevehiculos.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(detalledevehiculos)
            for i in range(0, countitem):
                if(detalledevehiculos[i].id == detalledevehiculo.id):
                    try:
                        previousitem = detalledevehiculos[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = detalledevehiculos[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            detalledevehiculo_previous = DetalleDeVehiculo.objects.get(pk=previousitem)
        except:
            detalledevehiculo_previous = None
        try:
            detalledevehiculo_next = DetalleDeVehiculo.objects.get(pk=nextitem)
        except:
            detalledevehiculo_next = None

        context['detalledevehiculo_previous'] = detalledevehiculo_previous
        context['detalledevehiculo_next'] = detalledevehiculo_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "DetalleDeVehiculo " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('uvehiculos:list_detalledevehiculo'))
                #return render_to_response(self.template_name, self.get_context_data())


class DetalleDeVehiculoDelete(DeleteView):
    model = DetalleDeVehiculo
    form_class = DetalleDeVehiculoForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app chofer asignado
class ChoferAsignadoListView(ListView):
    model = ChoferAsignado
    paginate_by = 10
    context_object_name = 'choferasignados'
    template_name = 'choferasignado_lista.html'

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
        context = super(ChoferAsignadoListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        if order_by:
            lista_choferasignado = ChoferAsignado.objects.all().order_by(order_by)
        else:
            lista_choferasignado = ChoferAsignado.objects.all()

        paginator = Paginator(lista_choferasignado, 10)
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
            queryset = ChoferAsignado.objects.all().order_by(order_by)
        else:
            queryset = ChoferAsignado.objects.all()

        return queryset


class ChoferAsignadoView(View):
    form_class = ChoferAsignadoForm
    template_name = 'choferasignado_add.html'

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
                return HttpResponseRedirect(reverse('uvehiculos:edit_choferasignado',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('uvehiculos:list_choferasignado'))

        return render(request, self.template_name, {'form': form})


class ChoferAsignadoUpdate(UpdateView):
    template_name = 'choferasignado_edit.html'
    form_class = ChoferAsignadoForm
    model = ChoferAsignado

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ChoferAsignadoUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        choferasignado = ChoferAsignado.objects.get(pk=self.object.pk)
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
            lista_choferasignado = ChoferAsignado.objects.all().order_by(order_by)
        else:
            lista_choferasignado = ChoferAsignado.objects.all()

        paginator = Paginator(lista_choferasignado, nropag)
        # Show 25 contacts per page

        if page == '0':
            choferasignados = lista_choferasignado
        else:
            try:
                choferasignados = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                choferasignados = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                choferasignados = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(choferasignados.object_list[i].id == choferasignado.id):
                    if choferasignados.has_previous:
                        try:
                            previousitem = choferasignados.object_list[i-1].id
                        except:
                            previousitem = None

                    if choferasignados.has_next:
                        try:
                            nextitem = choferasignados.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(choferasignados)
            for i in range(0, countitem):
                if(choferasignados[i].id == choferasignado.id):
                    try:
                        previousitem = choferasignados[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = choferasignados[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            choferasignado_previous = ChoferAsignado.objects.get(pk=previousitem)
        except:
            choferasignado_previous = None
        try:
            choferasignado_next = ChoferAsignado.objects.get(pk=nextitem)
        except:
            choferasignado_next = None

        context['choferasignado_previous'] = choferasignado_previous
        context['choferasignado_next'] = choferasignado_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "ChoferAsignado " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('uvehiculos:list_choferasignado'))
                #return render_to_response(self.template_name, self.get_context_data())


class ChoferAsignadoDelete(DeleteView):
    model = ChoferAsignado
    form_class = ChoferAsignadoForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())
