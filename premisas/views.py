"""
Docstring documentación pendiente

"""

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.views.generic import ListView, View, UpdateView, DeleteView, \
    CreateView
from premisas.models import Empresa, PersonalizacionVisual, \
    VarianteVisual, VarianteVisualDetalle, DatosPrecargado
from premisas.forms import EmpresaForm, PersonalizacionVisualForm, \
    VarianteVisualForm, VarianteVisualDetalleFormSet, \
    DatosPrecargadoForm
from mtvmcotizacionv02.views import valor_Personalizacionvisual, get_query
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.contenttypes.models import ContentType
from django.core import serializers
import json


# Create your views here.
# app empresa
class EmpresaListView(ListView):
    model = Empresa
    paginate_by = 10
    context_object_name = 'empresas'
    template_name = 'empresa_lista.html'

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
        context = super(EmpresaListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['codigo',
                                             'empresa',
                                             'telefonos',
                                             'direccion',
                                             'sitio_web',
                                             'correo',
                                             'responsable',
                                             'cuit',
                                             'telefono_call_center', ])
            lista_empresa = Empresa.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['codigo',
                                             'empresa',
                                             'telefonos',
                                             'direccion',
                                             'sitio_web',
                                             'correo',
                                             'responsable',
                                             'cuit',
                                             'telefono_call_center', ])
            lista_empresa = Empresa.objects.filter(entry_query)
        elif order_by:
            lista_empresa = Empresa.objects.all().order_by(order_by)
        else:
            lista_empresa = Empresa.objects.all()

        paginator = Paginator(lista_empresa, 10)
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
            entry_query = get_query(search, ['codigo',
                                             'empresa',
                                             'telefonos',
                                             'direccion',
                                             'sitio_web',
                                             'correo',
                                             'responsable',
                                             'cuit',
                                             'telefono_call_center', ])
            queryset = Empresa.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['codigo',
                                             'empresa',
                                             'telefonos',
                                             'direccion',
                                             'sitio_web',
                                             'correo',
                                             'responsable',
                                             'cuit',
                                             'telefono_call_center', ])
            queryset = Empresa.objects.filter(entry_query)
        elif order_by:
            queryset = Empresa.objects.all().order_by(order_by)
        else:
            queryset = Empresa.objects.all()

        return queryset


class EmpresaView(View):
    form_class = EmpresaForm
    template_name = 'empresa_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Empresa '" + str(id_reg) + "'  agregado con éxito.",
                                 extra_tags=reverse('upremisas:list_empresa'))
                return HttpResponseRedirect(reverse('upremisas:edit_empresa',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Empresa '" + str(id_reg) + "'  agregado con éxito.")
                return HttpResponseRedirect(reverse('upremisas:list_empresa'))

        return render(request, self.template_name, {'form': form})


class EmpresaUpdate(UpdateView):
    template_name = 'empresa_edit.html'
    form_class = EmpresaForm
    model = Empresa

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(EmpresaUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        empresa = Empresa.objects.get(pk=self.object.pk)
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
            lista_empresa = Empresa.objects.all().order_by(order_by)
        else:
            lista_empresa = Empresa.objects.all()

        paginator = Paginator(lista_empresa, nropag)
        # Show 25 contacts per page

        if page == '0':
            empresas = lista_empresa
        else:
            try:
                empresas = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                empresas = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                empresas = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(empresas.object_list[i].id == empresa.id):
                    if empresas.has_previous:
                        try:
                            previousitem = empresas.object_list[i-1].id
                        except:
                            previousitem = None

                    if empresas.has_next:
                        try:
                            nextitem = empresas.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(empresas)
            for i in range(0, countitem):
                if(empresas[i].id == empresa.id):
                    try:
                        previousitem = empresas[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = empresas[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            empresa_previous = Empresa.objects.get(pk=previousitem)
        except:
            empresa_previous = None
        try:
            empresa_next = Empresa.objects.get(pk=nextitem)
        except:
            empresa_next = None

        context['empresa_previous'] = empresa_previous
        context['empresa_next'] = empresa_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Empresa " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('upremisas:list_empresa'))
                #return render_to_response(self.template_name, self.get_context_data())


class EmpresaDelete(DeleteView):
    model = Empresa
    form_class = EmpresaForm
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
        messages.success(self.request, "Empresa " + str(self.obj) + " eliminado con éxito.", extra_tags=next)
        return render(request, '../../mensaje/templates/mensaje.html', {'obj': context})


# app personalizacion visual
class PersonalizacionVisualListView(ListView):
    model = PersonalizacionVisual
    paginate_by = 10
    context_object_name = 'personalizacionvisuales'
    template_name = 'personalizacionvisual_lista.html'

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
        context = super(PersonalizacionVisualListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['tipo',
                                             'usuario__username',
                                             'valor', ])
            lista_personalizacionvisual = PersonalizacionVisual.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo',
                                             'usuario__username',
                                             'valor', ])
            lista_personalizacionvisual = PersonalizacionVisual.objects.filter(entry_query)
        elif order_by:
            lista_personalizacionvisual = PersonalizacionVisual.objects.all().order_by(order_by)
        else:
            lista_personalizacionvisual = PersonalizacionVisual.objects.all()

        paginator = Paginator(lista_personalizacionvisual, 10)
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
            entry_query = get_query(search, ['tipo',
                                             'usuario__username',
                                             'valor', ])
            queryset = PersonalizacionVisual.objects.filter(entry_query).order_by(order_by)
        elif order_by:
            queryset = PersonalizacionVisual.objects.all().order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipo',
                                             'usuario__username',
                                             'valor', ])
            queryset = PersonalizacionVisual.objects.filter(entry_query)
        else:
            queryset = PersonalizacionVisual.objects.all()

        return queryset


class PersonalizacionVisualView(View):
    form_class = PersonalizacionVisualForm
    template_name = 'personalizacionvisual_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Personalizacion visual '" + str(id_reg) + "'  agregado con éxito.",
                                 extra_tags=reverse('upremisas:list_personalizacionvisual'))
                return HttpResponseRedirect(reverse('upremisas:edit_personalizacionvisual',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Personalizacion visual '" + str(id_reg) + "'  agregado con éxito.")
                return HttpResponseRedirect(reverse('upremisas:list_personalizacionvisual'))

        return render(request, self.template_name, {'form': form})


class PersonalizacionVisualUpdate(UpdateView):
    template_name = 'personalizacionvisual_edit.html'
    form_class = PersonalizacionVisualForm
    model = PersonalizacionVisual

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PersonalizacionVisualUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        personalizacionvisual = PersonalizacionVisual.objects.get(pk=self.object.pk)
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
            lista_personalizacionvisual = PersonalizacionVisual.objects.all().order_by(order_by)
        else:
            lista_personalizacionvisual = PersonalizacionVisual.objects.all()

        paginator = Paginator(lista_personalizacionvisual, nropag)
        # Show 25 contacts per page

        if page == '0':
            personalizacionvisuales = lista_personalizacionvisual
        else:
            try:
                personalizacionvisuales = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                personalizacionvisuales = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                personalizacionvisuales = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(personalizacionvisuales.object_list[i].id == personalizacionvisual.id):
                    if personalizacionvisuales.has_previous:
                        try:
                            previousitem = personalizacionvisuales.object_list[i-1].id
                        except:
                            previousitem = None

                    if personalizacionvisuales.has_next:
                        try:
                            nextitem = personalizacionvisuales.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(personalizacionvisuales)
            for i in range(0, countitem):
                if(personalizacionvisuales[i].id == personalizacionvisual.id):
                    try:
                        previousitem = personalizacionvisuales[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = personalizacionvisuales[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            personalizacionvisual_previous = PersonalizacionVisual.objects.get(pk=previousitem)
        except:
            personalizacionvisual_previous = None
        try:
            personalizacionvisual_next = PersonalizacionVisual.objects.get(pk=nextitem)
        except:
            personalizacionvisual_next = None

        context['personalizacionvisual_previous'] = personalizacionvisual_previous
        context['personalizacionvisual_next'] = personalizacionvisual_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "PersonalizacionVisual " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('upremisas:list_personalizacionvisual'))
                #return render_to_response(self.template_name, self.get_context_data())


class PersonalizacionVisualDelete(DeleteView):
    model = PersonalizacionVisual
    form_class = PersonalizacionVisualForm
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
        messages.success(self.request, "Personalizacion visual " + str(self.obj) + " eliminado con éxito.", extra_tags=next)
        return render(request, '../../mensaje/templates/mensaje.html', {'obj': context})


# app variante visual
class VarianteVisualListView(ListView):
    model = VarianteVisual
    paginate_by = 10
    context_object_name = 'variantevisuales'
    template_name = 'variantevisual_lista.html'

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
        context = super(VarianteVisualListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['nombre',
                                             'usuario__username',
                                             'model', ])
            lista_variantevisual = VarianteVisual.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['nombre',
                                             'usuario__username',
                                             'model', ])
            lista_variantevisual = VarianteVisual.objects.filter(entry_query)
        elif order_by:
            lista_variantevisual = VarianteVisual.objects.all().order_by(order_by)
        else:
            lista_variantevisual = VarianteVisual.objects.all()

        paginator = Paginator(lista_variantevisual, 10)
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
            entry_query = get_query(search, ['nombre',
                                             'usuario__username',
                                             'model', ])
            queryset = VarianteVisual.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['nombre',
                                             'usuario__username',
                                             'model', ])
            queryset = VarianteVisual.objects.filter(entry_query)
        elif order_by:
            queryset = VarianteVisual.objects.all().order_by(order_by)
        else:
            queryset = VarianteVisual.objects.all()

        return queryset


class VarianteVisualCreateView(CreateView):
    template_name = 'variantevisual_add.html'
    model = VarianteVisual
    form_class = VarianteVisualForm

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        item_form = VarianteVisualDetalleFormSet()

        return self.render_to_response(
            self.get_context_data(form=form,
                                  item_form=item_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        item_form = VarianteVisualDetalleFormSet(self.request.POST)
        if (form.is_valid() and item_form.is_valid()):
            return self.form_valid(form, item_form)
        else:
            return self.form_invalid(form, item_form)

    def form_valid(self, form, item_form):
        """
        Called if all forms are valid. Creates a VarianteVisual instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        item_form.instance = self.object
        item_form.save()

        if 'regEdit' in self.request.POST:
            messages.success(self.request, "Variante visual '" + str(id_reg) + "'  agregado con éxito.",
                             extra_tags=reverse('upremisas:list_variantevisual'))
            return HttpResponseRedirect(reverse('upremisas:edit_variantevisual',
                                                args=(self.object,)))
        else:
            messages.success(self.request, "Variante visual '" + str(id_reg) + "'  agregado con éxito.")
            return HttpResponseRedirect(reverse('upremisas:list_variantevisual'))

    def form_invalid(self, form, item_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  item_form=item_form))


class VarianteVisualUpdate(UpdateView):
    template_name = 'variantevisual_edit.html'
    form_class = VarianteVisualForm
    model = VarianteVisual

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(VarianteVisualUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        variantevisual = VarianteVisual.objects.get(pk=self.object.pk)
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
            lista_variantevisual = VarianteVisual.objects.all().order_by(order_by)
        else:
            lista_variantevisual = VarianteVisual.objects.all()

        paginator = Paginator(lista_variantevisual, nropag)
        # Show 25 contacts per page

        if page == '0':
            variantevisuales = lista_variantevisual
        else:
            try:
                variantevisuales = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                variantevisuales = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                variantevisuales = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(variantevisuales.object_list[i].id == variantevisual.id):
                    if variantevisuales.has_previous:
                        try:
                            previousitem = variantevisuales.object_list[i-1].id
                        except:
                            previousitem = None

                    if variantevisuales.has_next:
                        try:
                            nextitem = variantevisuales.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(variantevisuales)
            for i in range(0, countitem):
                if(variantevisuales[i].id == variantevisual.id):
                    try:
                        previousitem = variantevisuales[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = variantevisuales[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            variantevisual_previous = VarianteVisual.objects.get(pk=previousitem)
        except:
            variantevisual_previous = None
        try:
            variantevisual_next = VarianteVisual.objects.get(pk=nextitem)
        except:
            variantevisual_next = None

        context['variantevisual_previous'] = variantevisual_previous
        context['variantevisual_next'] = variantevisual_next

        item_form = VarianteVisualDetalleFormSet(instance=self.object)
        context['item_form'] = item_form
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        item_form = VarianteVisualDetalleFormSet(self.request.POST,
                                                 self.request.FILES,
                                                 instance=self.object)
        if item_form.is_valid():
            id_reg = self.object.save()
            item_form.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Variante visual " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('upremisas:list_variantevisual'))
                #return render_to_response(self.template_name, self.get_context_data())


class VarianteVisualDelete(DeleteView):
    model = VarianteVisual
    form_class = VarianteVisualForm
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
        messages.success(self.request, "Variante visual " + str(self.obj) + " eliminado con éxito.", extra_tags=next)
        return render(request, '../../mensaje/templates/mensaje.html', {'obj': context})


# app datos precargados
class DatosPrecargadoListView(ListView):
    model = DatosPrecargado
    paginate_by = 10
    context_object_name = 'datosprecargados'
    template_name = 'datosprecargado_lista.html'

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
        context = super(DatosPrecargadoListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['nombre_app',
                                             'dato',
                                             'model',
                                             'tipo_de_dato',
                                             'valor', ])
            lista_datosprecargado = DatosPrecargado.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['nombre_app',
                                             'dato',
                                             'model',
                                             'tipo_de_dato',
                                             'valor', ])
            lista_datosprecargado = DatosPrecargado.objects.filter(entry_query)
        elif order_by:
            lista_datosprecargado = DatosPrecargado.objects.all().order_by(order_by)
        else:
            lista_datosprecargado = DatosPrecargado.objects.all()

        paginator = Paginator(lista_datosprecargado, 10)
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
            entry_query = get_query(search, ['nombre_app',
                                             'dato',
                                             'model',
                                             'tipo_de_dato',
                                             'valor', ])
            queryset = DatosPrecargado.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['nombre_app',
                                             'dato',
                                             'model',
                                             'tipo_de_dato',
                                             'valor', ])
            queryset = DatosPrecargado.objects.filter(entry_query)
        elif order_by:
            queryset = DatosPrecargado.objects.all().order_by(order_by)
        else:
            queryset = DatosPrecargado.objects.all()

        return queryset


class DatosPrecargadoView(View):
    form_class = DatosPrecargadoForm
    template_name = 'datosprecargado_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        if self.request.is_ajax():
            nombreapp_id = self.request.GET.get('id_nombre_app')
            if nombreapp_id:
                data = serializers.serialize("xml", ContentType.objects.filter(app_label=nombreapp_id))
                json_model = serializers.serialize("json", ContentType.objects.filter(app_label=nombreapp_id))
                #return JsonResponse(data, safe=False)

                return HttpResponse(data, mimetype="application/javascript")

        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('upremisas:edit_datosprecargado',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('upremisas:list_datosprecargado'))

        return render(request, self.template_name, {'form': form})


class DatosPrecargadoUpdate(UpdateView):
    template_name = 'datosprecargado_edit.html'
    form_class = DatosPrecargadoForm
    model = DatosPrecargado

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DatosPrecargadoUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        datosprecargado = DatosPrecargado.objects.get(pk=self.object.pk)
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
            lista_datosprecargado = DatosPrecargado.objects.all().order_by(order_by)
        else:
            lista_datosprecargado = DatosPrecargado.objects.all()

        paginator = Paginator(lista_datosprecargado, nropag)
        # Show 25 contacts per page

        if page == '0':
            datosprecargados = lista_datosprecargado
        else:
            try:
                datosprecargados = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                datosprecargados = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                datosprecargados = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(datosprecargados.object_list[i].id == datosprecargado.id):
                    if datosprecargados.has_previous:
                        try:
                            previousitem = datosprecargados.object_list[i-1].id
                        except:
                            previousitem = None

                    if datosprecargados.has_next:
                        try:
                            nextitem = datosprecargados.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(datosprecargados)
            for i in range(0, countitem):
                if(datosprecargados[i].id == datosprecargado.id):
                    try:
                        previousitem = datosprecargados[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = datosprecargados[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            datosprecargado_previous = DatosPrecargado.objects.get(pk=previousitem)
        except:
            datosprecargado_previous = None
        try:
            datosprecargado_next = DatosPrecargado.objects.get(pk=nextitem)
        except:
            datosprecargado_next = None

        context['datosprecargado_previous'] = datosprecargado_previous
        context['datosprecargado_next'] = datosprecargado_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "DatosPrecargado " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('upremisas:list_datosprecargado'))
                #return render_to_response(self.template_name, self.get_context_data())


class DatosPrecargadoDelete(DeleteView):
    model = DatosPrecargado
    form_class = DatosPrecargadoForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# view para llenar select dinamico segun el model seleccionado
def exchange_fields(model):

    fields = _related_models(model)

    def _related_models(m):
        return [
            f.related_model for f in m._meta.get_fields()
        ]

    if fields:

        response = {
            'cant_ambiente': 'consulto'
            }
    else:
        response = {
            'cant_ambiente': 0
            }

    return HttpResponse(json.dumps(response), content_type='application/json')
