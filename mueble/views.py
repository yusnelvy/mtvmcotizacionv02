from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.generic import ListView, View, UpdateView, DeleteView
from mueble.models import TipoDeMueble, Mueble, EspecificacionDeMueble,\
    MueblePorAmbiente
from mueble.forms import TipoDeMuebleForm, MuebleForm, EspecificacionDeMuebleForm, \
    MueblePorAmbienteForm
from mtvmcotizacionv02.views import valor_Personalizacionvisual
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# app tipo de mueble
class TipoDeMuebleListView(ListView):
    model = TipoDeMueble
    paginate_by = 10
    context_object_name = 'tiposdemueble'
    template_name = 'tipodemueble_lista.html'

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
        context = super(TipoDeMuebleListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        if order_by:
            lista_tipodemueble = TipoDeMueble.objects.all().order_by(order_by)
        else:
            lista_tipodemueble = TipoDeMueble.objects.all()

        paginator = Paginator(lista_tipodemueble, 10)
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
            queryset = TipoDeMueble.objects.all().order_by(order_by)
        else:
            queryset = TipoDeMueble.objects.all()

        return queryset


class TipoDeMuebleView(View):
    form_class = TipoDeMuebleForm
    template_name = 'tipodemueble_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Tipo de mueble '" + str(id_reg) + "'  agregado con éxito.")
                return HttpResponseRedirect(reverse('umuebles:edit_tipodemueble',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Tipo de mueble '" + str(id_reg) + "'  agregado con éxito.")
                return HttpResponseRedirect(reverse('umuebles:list_tipodemueble'))

        return render(request, self.template_name, {'form': form})


class TipoDeMuebleUpdate(UpdateView):
    template_name = 'tipodemueble_edit.html'
    form_class = TipoDeMuebleForm
    model = TipoDeMueble

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TipoDeMuebleUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        tipodemueble = TipoDeMueble.objects.get(pk=self.object.pk)
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
            lista_tipodemueble = TipoDeMueble.objects.all().order_by(order_by)
        else:
            lista_tipodemueble = TipoDeMueble.objects.all()

        paginator = Paginator(lista_tipodemueble, nropag)
        # Show 25 contacts per page

        if page == '0':
            tiposdemueble = lista_tipodemueble
        else:
            try:
                tiposdemueble = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                tiposdemueble = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                tiposdemueble = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(tiposdemueble.object_list[i].id == tipodemueble.id):
                    if tiposdemueble.has_previous:
                        try:
                            previousitem = tiposdemueble.object_list[i-1].id
                        except:
                            previousitem = None

                    if tiposdemueble.has_next:
                        try:
                            nextitem = tiposdemueble.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(tiposdemueble)
            for i in range(0, countitem):
                if(tiposdemueble[i].id == tipodemueble.id):
                    try:
                        previousitem = tiposdemueble[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = tiposdemueble[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            tipodemueble_previous = TipoDeMueble.objects.get(pk=previousitem)
        except:
            tipodemueble_previous = None
        try:
            tipodemueble_next = TipoDeMueble.objects.get(pk=nextitem)
        except:
            tipodemueble_next = None

        context['tipodemueble_previous'] = tipodemueble_previous
        context['tipodemueble_next'] = tipodemueble_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Tipo de mueble '" + str(self.object) + "'  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Tipo de mueble '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                messages.success(self.request, "Tipo de mueble '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(reverse('umuebles:list_tipodemueble'))


class TipoDeMuebleDelete(DeleteView):
    model = TipoDeMueble
    form_class = TipoDeMuebleForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            messages.success(self.request, "Tipo de mueble '" + str(self.obj) + "'  eliminado con éxito.")
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app mueble
class MuebleListView(ListView):
    model = Mueble
    paginate_by = 10
    context_object_name = 'muebles'
    template_name = 'mueble_lista.html'

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
        context = super(MuebleListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        if order_by:
            lista_mueble = Mueble.objects.all().order_by(order_by)
        else:
            lista_mueble = Mueble.objects.all()

        paginator = Paginator(lista_mueble, 10)
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
            queryset = Mueble.objects.all().order_by(order_by)
        else:
            queryset = Mueble.objects.all()

        return queryset


class MuebleView(View):
    form_class = MuebleForm
    template_name = 'mueble_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Mueble '" + str(id_reg) + "' agregado con éxito.")
                return HttpResponseRedirect(reverse('umuebles:edit_mueble',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Mueble '" + str(id_reg) + "' agregado con éxito.")
                return HttpResponseRedirect(reverse('umuebles:list_mueble'))

        return render(request, self.template_name, {'form': form})


class MuebleUpdate(UpdateView):
    template_name = 'mueble_edit.html'
    form_class = MuebleForm
    model = Mueble

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MuebleUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        mueble = Mueble.objects.get(pk=self.object.pk)
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
            lista_mueble = Mueble.objects.all().order_by(order_by)
        else:
            lista_mueble = Mueble.objects.all()

        paginator = Paginator(lista_mueble, nropag)
        # Show 25 contacts per page

        if page == '0':
            muebles = lista_mueble
        else:
            try:
                muebles = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                muebles = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                muebles = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(muebles.object_list[i].id == mueble.id):
                    if muebles.has_previous:
                        try:
                            previousitem = muebles.object_list[i-1].id
                        except:
                            previousitem = None

                    if muebles.has_next:
                        try:
                            nextitem = muebles.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(muebles)
            for i in range(0, countitem):
                if(muebles[i].id == mueble.id):
                    try:
                        previousitem = muebles[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = muebles[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            mueble_previous = Mueble.objects.get(pk=previousitem)
        except:
            mueble_previous = None
        try:
            mueble_next = Mueble.objects.get(pk=nextitem)
        except:
            mueble_next = None

        context['mueble_previous'] = mueble_previous
        context['mueble_next'] = mueble_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Mueble '" + str(self.object) + "' guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Mueble '" + str(self.object) + "' guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                return render_to_response(self.template_name, self.get_context_data())


class MuebleDelete(DeleteView):
    model = Mueble
    form_class = MuebleForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            messages.success(self.request, "Mueble '" + str(self.obj) + "' eliminado con éxito.")
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app especificación de mueble
class EspecificacionDeMuebleListView(ListView):
    model = EspecificacionDeMueble
    paginate_by = 10
    context_object_name = 'especificacionesdemueble'
    template_name = 'especificaciondemueble_lista.html'

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
        context = super(EspecificacionDeMuebleListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        if order_by:
            lista_especificaciondemueble = EspecificacionDeMueble.objects.all().order_by(order_by)
        else:
            lista_especificaciondemueble = EspecificacionDeMueble.objects.all()

        paginator = Paginator(lista_especificaciondemueble, 10)
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
            queryset = EspecificacionDeMueble.objects.all().order_by(order_by)
        else:
            queryset = EspecificacionDeMueble.objects.all()

        return queryset


class EspecificacionDeMuebleView(View):
    form_class = EspecificacionDeMuebleForm
    template_name = 'especificaciondemueble_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Especificación '" + str(id_reg) + "' agregado con éxito.")
                return HttpResponseRedirect(reverse('umuebles:edit_especificaciondemueble',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Especificación '" + str(id_reg) + "' agregado con éxito.")
                return HttpResponseRedirect(reverse('umuebles:list_especificaciondemueble'))

        return render(request, self.template_name, {'form': form})


class EspecificacionDeMuebleUpdate(UpdateView):
    template_name = 'especificaciondemueble_edit.html'
    form_class = EspecificacionDeMuebleForm
    model = EspecificacionDeMueble

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(EspecificacionDeMuebleUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        especificaciondemueble = EspecificacionDeMueble.objects.get(pk=self.object.pk)
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
            lista_especificaciondemueble = EspecificacionDeMueble.objects.all().order_by(order_by)
        else:
            lista_especificaciondemueble = EspecificacionDeMueble.objects.all()

        paginator = Paginator(lista_especificaciondemueble, nropag)
        # Show 25 contacts per page

        if page == '0':
            especificacionesdemueble = lista_especificaciondemueble
        else:
            try:
                especificacionesdemueble = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                especificacionesdemueble = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                especificacionesdemueble = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(especificacionesdemueble.object_list[i].id == especificaciondemueble.id):
                    if especificacionesdemueble.has_previous:
                        try:
                            previousitem = especificacionesdemueble.object_list[i-1].id
                        except:
                            previousitem = None

                    if especificacionesdemueble.has_next:
                        try:
                            nextitem = especificacionesdemueble.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(especificacionesdemueble)
            for i in range(0, countitem):
                if(especificacionesdemueble[i].id == especificaciondemueble.id):
                    try:
                        previousitem = especificacionesdemueble[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = especificacionesdemueble[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            especificaciondemueble_previous = EspecificacionDeMueble.objects.get(pk=previousitem)
        except:
            especificaciondemueble_previous = None
        try:
            especificaciondemueble_next = EspecificacionDeMueble.objects.get(pk=nextitem)
        except:
            especificaciondemueble_next = None

        context['especificaciondemueble_previous'] = especificaciondemueble_previous
        context['especificaciondemueble_next'] = especificaciondemueble_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Especificación de mueble '" + str(self.object) + "'  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Especificación de mueble '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                return render_to_response(self.template_name, self.get_context_data())


class EspecificacionDeMuebleDelete(DeleteView):
    model = EspecificacionDeMueble
    form_class = EspecificacionDeMuebleForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            messages.success(self.request, "Especificación '" + str(self.obj) + "' eliminado con éxito.")
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app mueble por ambiente
class MueblePorAmbienteListView(ListView):
    model = MueblePorAmbiente
    paginate_by = 10
    context_object_name = 'mueblesporambiente'
    template_name = 'muebleporambiente_lista.html'

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
        context = super(MueblePorAmbienteListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        if order_by:
            lista_muebleporambiente = MueblePorAmbiente.objects.all().order_by(order_by)
        else:
            lista_muebleporambiente = MueblePorAmbiente.objects.all()

        paginator = Paginator(lista_muebleporambiente, 10)
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
            queryset = MueblePorAmbiente.objects.all().order_by(order_by)
        else:
            queryset = MueblePorAmbiente.objects.all()

        return queryset


class MueblePorAmbienteView(View):
    form_class = MueblePorAmbienteForm
    template_name = 'muebleporambiente_add.html'

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
                return HttpResponseRedirect(reverse('umuebles:edit_muebleporambiente',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('umuebles:list_muebleporambiente'))

        return render(request, self.template_name, {'form': form})


class MueblePorAmbienteUpdate(UpdateView):
    template_name = 'muebleporambiente_edit.html'
    form_class = MueblePorAmbienteForm
    model = MueblePorAmbiente

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MueblePorAmbienteUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        muebleporambiente = MueblePorAmbiente.objects.get(pk=self.object.pk)
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
            lista_muebleporambiente = MueblePorAmbiente.objects.all().order_by(order_by)
        else:
            lista_muebleporambiente = MueblePorAmbiente.objects.all()

        paginator = Paginator(lista_muebleporambiente, nropag)
        # Show 25 contacts per page

        if page == '0':
            mueblesporambiente = lista_muebleporambiente
        else:
            try:
                mueblesporambiente = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                mueblesporambiente = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                mueblesporambiente = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(mueblesporambiente.object_list[i].id == muebleporambiente.id):
                    if mueblesporambiente.has_previous:
                        try:
                            previousitem = mueblesporambiente.object_list[i-1].id
                        except:
                            previousitem = None

                    if mueblesporambiente.has_next:
                        try:
                            nextitem = mueblesporambiente.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(mueblesporambiente)
            for i in range(0, countitem):
                if(mueblesporambiente[i].id == muebleporambiente.id):
                    try:
                        previousitem = mueblesporambiente[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = mueblesporambiente[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            muebleporambiente_previous = MueblePorAmbiente.objects.get(pk=previousitem)
        except:
            muebleporambiente_previous = None
        try:
            muebleporambiente_next = MueblePorAmbiente.objects.get(pk=nextitem)
        except:
            muebleporambiente_next = None

        context['muebleporambiente_previous'] = muebleporambiente_previous
        context['muebleporambiente_next'] = muebleporambiente_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Mueble por ambiente" + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return render_to_response(self.template_name, self.get_context_data())


class MueblePorAmbienteDelete(DeleteView):
    model = MueblePorAmbiente
    form_class = MueblePorAmbienteForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())
