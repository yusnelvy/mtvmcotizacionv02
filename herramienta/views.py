"""
Docstring documentación pendiente

"""

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.generic import ListView, View, UpdateView, DeleteView
from herramienta.models import Herramienta, DotacionBasicaDeCamion
from herramienta.forms import HerramientaForm, DotacionBasicaDeCamionForm
from mtvmcotizacionv02.views import valor_Personalizacionvisual, get_query
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# app herramienta
class HerramientaListView(ListView):
    model = Herramienta
    paginate_by = 10
    context_object_name = 'herramientas'
    template_name = 'herramienta_lista.html'

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
        context = super(HerramientaListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['herramienta',
                                             'unidad__unidad',
                                             'descripcion',
                                             'volumen_en_camion',
                                             'peso_kg', ])

            lista_herramienta = Herramienta.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['herramienta',
                                             'unidad__unidad',
                                             'descripcion',
                                             'volumen_en_camion',
                                             'peso_kg', ])

            lista_herramienta = Herramienta.objects.filter(entry_query)
        elif order_by:
            lista_herramienta = Herramienta.objects.all().order_by(order_by)
        else:
            lista_herramienta = Herramienta.objects.all()

        paginator = Paginator(lista_herramienta, 10)
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
            entry_query = get_query(search, ['herramienta',
                                             'unidad__unidad',
                                             'descripcion',
                                             'volumen_en_camion',
                                             'peso_kg', ])

            queryset = Herramienta.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['herramienta',
                                             'unidad__unidad',
                                             'descripcion',
                                             'volumen_en_camion',
                                             'peso_kg', ])

            queryset = Herramienta.objects.filter(entry_query)
        elif order_by:
            queryset = Herramienta.objects.all().order_by(order_by)
        else:
            queryset = Herramienta.objects.all()

        return queryset


class HerramientaView(View):
    form_class = HerramientaForm
    template_name = 'herramienta_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Herramienta '" + str(id_reg) + "'  agregado con éxito.",
                                 extra_tags=reverse('uherramientas:list_herramienta'))
                return HttpResponseRedirect(reverse('uherramientas:edit_herramienta',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('uherramientas:list_herramienta'))

        return render(request, self.template_name, {'form': form})


class HerramientaUpdate(UpdateView):
    template_name = 'herramienta_edit.html'
    form_class = HerramientaForm
    model = Herramienta

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HerramientaUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        herramienta = Herramienta.objects.get(pk=self.object.pk)
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
            lista_herramienta = Herramienta.objects.all().order_by(order_by)
        else:
            lista_herramienta = Herramienta.objects.all()

        paginator = Paginator(lista_herramienta, nropag)
        # Show 25 contacts per page

        if page == '0':
            herramientas = lista_herramienta
        else:
            try:
                herramientas = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                herramientas = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                herramientas = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(herramientas.object_list[i].id == herramienta.id):
                    if herramientas.has_previous:
                        try:
                            previousitem = herramientas.object_list[i-1].id
                        except:
                            previousitem = None

                    if herramientas.has_next:
                        try:
                            nextitem = herramientas.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(herramientas)
            for i in range(0, countitem):
                if(herramientas[i].id == herramienta.id):
                    try:
                        previousitem = herramientas[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = herramientas[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            herramienta_previous = Herramienta.objects.get(pk=previousitem)
        except:
            herramienta_previous = None
        try:
            herramienta_next = Herramienta.objects.get(pk=nextitem)
        except:
            herramienta_next = None

        context['herramienta_previous'] = herramienta_previous
        context['herramienta_next'] = herramienta_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Herramienta " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('uherramientas:list_herramienta'))
                #return render_to_response(self.template_name, self.get_context_data())


class HerramientaDelete(DeleteView):
    model = Herramienta
    form_class = HerramientaForm
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
        messages.success(self.request, "Herramienta " + str(self.obj) + " eliminado con éxito.", extra_tags=next)
        return render(request, '../../mensaje/templates/mensaje.html', {'obj': context})


# app dotación básica de camión
class DotacionBasicaDeCamionListView(ListView):
    model = DotacionBasicaDeCamion
    paginate_by = 10
    context_object_name = 'dotacionesbasicasdecamion'
    template_name = 'dotacionbasicadecamion_lista.html'

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
        context = super(DotacionBasicaDeCamionListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['herramienta__herramienta',
                                             'cantidad', ])

            lista_dotacionbasicadecamion = DotacionBasicaDeCamion.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['herramienta__herramienta',
                                             'cantidad', ])

            lista_dotacionbasicadecamion = DotacionBasicaDeCamion.objects.filter(entry_query)
        elif order_by:
            lista_dotacionbasicadecamion = DotacionBasicaDeCamion.objects.all().order_by(order_by)
        else:
            lista_dotacionbasicadecamion = DotacionBasicaDeCamion.objects.all()

        paginator = Paginator(lista_dotacionbasicadecamion, 10)
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
            entry_query = get_query(search, ['herramienta__herramienta',
                                             'cantidad', ])

            queryset = DotacionBasicaDeCamion.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['herramienta__herramienta',
                                             'cantidad', ])

            queryset = DotacionBasicaDeCamion.objects.filter(entry_query)
        elif order_by:
            queryset = DotacionBasicaDeCamion.objects.all().order_by(order_by)
        else:
            queryset = DotacionBasicaDeCamion.objects.all()

        return queryset


class DotacionBasicaDeCamionView(View):
    form_class = DotacionBasicaDeCamionForm
    template_name = 'dotacionbasicadecamion_add.html'

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
                return HttpResponseRedirect(reverse('uherramientas:edit_dotacionbasicadecamion',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('uherramientas:list_dotacionbasicadecamion'))

        return render(request, self.template_name, {'form': form})


class DotacionBasicaDeCamionUpdate(UpdateView):
    template_name = 'dotacionbasicadecamion_edit.html'
    form_class = DotacionBasicaDeCamionForm
    model = DotacionBasicaDeCamion

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DotacionBasicaDeCamionUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        dotacionbasicadecamion = DotacionBasicaDeCamion.objects.get(pk=self.object.pk)
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
            lista_dotacionbasicadecamion = DotacionBasicaDeCamion.objects.all().order_by(order_by)
        else:
            lista_dotacionbasicadecamion = DotacionBasicaDeCamion.objects.all()

        paginator = Paginator(lista_dotacionbasicadecamion, nropag)
        # Show 25 contacts per page

        if page == '0':
            dotacionbasicadecamions = lista_dotacionbasicadecamion
        else:
            try:
                dotacionbasicadecamions = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                dotacionbasicadecamions = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                dotacionbasicadecamions = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(dotacionbasicadecamions.object_list[i].id == dotacionbasicadecamion.id):
                    if dotacionbasicadecamions.has_previous:
                        try:
                            previousitem = dotacionbasicadecamions.object_list[i-1].id
                        except:
                            previousitem = None

                    if dotacionbasicadecamions.has_next:
                        try:
                            nextitem = dotacionbasicadecamions.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(dotacionbasicadecamions)
            for i in range(0, countitem):
                if(dotacionbasicadecamions[i].id == dotacionbasicadecamion.id):
                    try:
                        previousitem = dotacionbasicadecamions[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = dotacionbasicadecamions[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            dotacionbasicadecamion_previous = DotacionBasicaDeCamion.objects.get(pk=previousitem)
        except:
            dotacionbasicadecamion_previous = None
        try:
            dotacionbasicadecamion_next = DotacionBasicaDeCamion.objects.get(pk=nextitem)
        except:
            dotacionbasicadecamion_next = None

        context['dotacionbasicadecamion_previous'] = dotacionbasicadecamion_previous
        context['dotacionbasicadecamion_next'] = dotacionbasicadecamion_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Dotación básica de camión " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('uherramientas:list_herramienta'))
                #return render_to_response(self.template_name, self.get_context_data())


class DotacionBasicaDeCamionDelete(DeleteView):
    model = DotacionBasicaDeCamion
    form_class = DotacionBasicaDeCamionForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())
