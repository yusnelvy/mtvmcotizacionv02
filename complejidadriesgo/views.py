from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.generic import ListView, View, UpdateView, DeleteView
from complejidadriesgo.models import ComplejidadRiesgo, NivelComplejidadRiesgo
from complejidadriesgo.forms import ComplejidadRiesgoForm, NivelComplejidadRiesgoForm
from mtvmcotizacionv02.views import valor_Personalizacionvisual, get_query
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# app complejidad y riesgo
class ComplejidadRiesgoListView(ListView):
    model = ComplejidadRiesgo
    paginate_by = 10
    context_object_name = 'complejidadriesgos'
    template_name = 'complejidadriesgo_lista.html'

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
        context = super(ComplejidadRiesgoListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['situacion',
                                             'descripcion',
                                             'factor_complejidad',
                                             'factor_riesgo', ])
            lista_complejidadriesgo = ComplejidadRiesgo.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['situacion',
                                             'descripcion',
                                             'factor_complejidad',
                                             'factor_riesgo', ])
            lista_complejidadriesgo = ComplejidadRiesgo.objects.filter(entry_query)
        elif order_by:
            lista_complejidadriesgo = ComplejidadRiesgo.objects.all().order_by(order_by)
        else:
            lista_complejidadriesgo = ComplejidadRiesgo.objects.all()

        paginator = Paginator(lista_complejidadriesgo, 10)
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
            entry_query = get_query(search, ['situacion',
                                             'descripcion',
                                             'factor_complejidad',
                                             'factor_riesgo', ])
            queryset = ComplejidadRiesgo.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['situacion',
                                             'descripcion',
                                             'factor_complejidad',
                                             'factor_riesgo', ])
            queryset = ComplejidadRiesgo.objects.filter(entry_query)
        elif order_by:
            queryset = ComplejidadRiesgo.objects.all().order_by(order_by)
        else:
            queryset = ComplejidadRiesgo.objects.all()

        return queryset


class ComplejidadRiesgoView(View):
    form_class = ComplejidadRiesgoForm
    template_name = 'complejidadriesgo_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Complejidad riesgo '" + str(id_reg) + "'  registrado con éxito.",
                                 extra_tags=reverse('ucomplejidadriesgos:list_complejidadriesgo'))
                return HttpResponseRedirect(reverse('ucomplejidadriesgos:edit_complejidadriesgo',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Complejidad riesgo '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('ucomplejidadriesgos:list_complejidadriesgo'))

        return render(request, self.template_name, {'form': form})


class ComplejidadRiesgoUpdate(UpdateView):
    template_name = 'complejidadriesgo_edit.html'
    form_class = ComplejidadRiesgoForm
    model = ComplejidadRiesgo

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ComplejidadRiesgoUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        complejidadriesgo = ComplejidadRiesgo.objects.get(pk=self.object.pk)
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
            lista_complejidadriesgo = ComplejidadRiesgo.objects.all().order_by(order_by)
        else:
            lista_complejidadriesgo = ComplejidadRiesgo.objects.all()

        paginator = Paginator(lista_complejidadriesgo, nropag)
        # Show 25 contacts per page

        if page == '0':
            complejidadriesgos = lista_complejidadriesgo
        else:
            try:
                complejidadriesgos = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                complejidadriesgos = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                complejidadriesgos = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(complejidadriesgos.object_list[i].id == complejidadriesgo.id):
                    if complejidadriesgos.has_previous:
                        try:
                            previousitem = complejidadriesgos.object_list[i-1].id
                        except:
                            previousitem = None

                    if complejidadriesgos.has_next:
                        try:
                            nextitem = complejidadriesgos.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(complejidadriesgos)
            for i in range(0, countitem):
                if(complejidadriesgos[i].id == complejidadriesgo.id):
                    try:
                        previousitem = complejidadriesgos[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = complejidadriesgos[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            complejidadriesgo_previous = ComplejidadRiesgo.objects.get(pk=previousitem)
        except:
            complejidadriesgo_previous = None
        try:
            complejidadriesgo_next = ComplejidadRiesgo.objects.get(pk=nextitem)
        except:
            complejidadriesgo_next = None

        context['complejidadriesgo_previous'] = complejidadriesgo_previous
        context['complejidadriesgo_next'] = complejidadriesgo_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "complejidad riesgo '" + str(self.object) + "'  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "complejidad riesgo '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('ucomplejidadriesgos:list_complejidadriesgo'))
                #return render_to_response(self.template_name, self.get_context_data())


class ComplejidadRiesgoDelete(DeleteView):
    model = ComplejidadRiesgo
    form_class = ComplejidadRiesgoForm
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
        messages.success(self.request, "Complejidad riesgo " + str(self.obj) + " eliminado con éxito.", extra_tags=next)
        return render(request, '../../mensaje/templates/mensaje.html', {'obj': context})


# app nivel de complejidad y riesgo
class NivelComplejidadRiesgoListView(ListView):
    model = NivelComplejidadRiesgo
    paginate_by = 10
    context_object_name = 'nivelcomplejidadriesgos'
    template_name = 'nivelcomplejidadriesgo_lista.html'

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
        context = super(NivelComplejidadRiesgoListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['nivel_complejidad_riesgo',
                                             'factor_inicial',
                                             'factor_final',
                                             'porcentaje', ])
            lista_complejidadriesgo = NivelComplejidadRiesgo.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['nivel_complejidad_riesgo',
                                             'factor_inicial',
                                             'factor_final',
                                             'porcentaje', ])
            lista_complejidadriesgo = NivelComplejidadRiesgo.objects.filter(entry_query)
        elif order_by:
            lista_complejidadriesgo = NivelComplejidadRiesgo.objects.all().order_by(order_by)
        else:
            lista_complejidadriesgo = NivelComplejidadRiesgo.objects.all()

        paginator = Paginator(lista_complejidadriesgo, 10)
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
            entry_query = get_query(search, ['nivel_complejidad_riesgo',
                                             'factor_inicial',
                                             'factor_final',
                                             'porcentaje', ])
            queryset = NivelComplejidadRiesgo.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['nivel_complejidad_riesgo',
                                             'factor_inicial',
                                             'factor_final',
                                             'porcentaje', ])
            queryset = NivelComplejidadRiesgo.objects.filter(entry_query)
        elif order_by:
            queryset = NivelComplejidadRiesgo.objects.all().order_by(order_by)
        else:
            queryset = NivelComplejidadRiesgo.objects.all()

        return queryset


class NivelComplejidadRiesgoView(View):
    form_class = NivelComplejidadRiesgoForm
    template_name = 'nivelcomplejidadriesgo_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Nivel de complejidad y riesgo '" + str(id_reg) + "'  registrado con éxito.",
                                 extra_tags=reverse('ucomplejidadriesgos:list_nivelcomplejidadriesgo'))
                return HttpResponseRedirect(reverse('ucomplejidadriesgos:edit_nivelcomplejidadriesgo',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Nivel de complejidad y riesgo '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('ucomplejidadriesgos:list_nivelcomplejidadriesgo'))

        return render(request, self.template_name, {'form': form})


class NivelComplejidadRiesgoUpdate(UpdateView):
    template_name = 'nivelcomplejidadriesgo_edit.html'
    form_class = NivelComplejidadRiesgoForm
    model = NivelComplejidadRiesgo

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(NivelComplejidadRiesgoUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        nivelcomplejidadriesgo = NivelComplejidadRiesgo.objects.get(pk=self.object.pk)
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
            lista_nivelcomplejidadriesgo = NivelComplejidadRiesgo.objects.all().order_by(order_by)
        else:
            lista_nivelcomplejidadriesgo = NivelComplejidadRiesgo.objects.all()

        paginator = Paginator(lista_nivelcomplejidadriesgo, nropag)
        # Show 25 contacts per page

        if page == '0':
            nivelcomplejidadriesgos = lista_nivelcomplejidadriesgo
        else:
            try:
                nivelcomplejidadriesgos = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                nivelcomplejidadriesgos = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                nivelcomplejidadriesgos = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(nivelcomplejidadriesgos.object_list[i].id == nivelcomplejidadriesgo.id):
                    if nivelcomplejidadriesgos.has_previous:
                        try:
                            previousitem = nivelcomplejidadriesgos.object_list[i-1].id
                        except:
                            previousitem = None

                    if nivelcomplejidadriesgos.has_next:
                        try:
                            nextitem = nivelcomplejidadriesgos.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(nivelcomplejidadriesgos)
            for i in range(0, countitem):
                if(nivelcomplejidadriesgos[i].id == nivelcomplejidadriesgo.id):
                    try:
                        previousitem = nivelcomplejidadriesgos[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = nivelcomplejidadriesgos[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            nivelcomplejidadriesgo_previous = NivelComplejidadRiesgo.objects.get(pk=previousitem)
        except:
            nivelcomplejidadriesgo_previous = None
        try:
            nivelcomplejidadriesgo_next = NivelComplejidadRiesgo.objects.get(pk=nextitem)
        except:
            nivelcomplejidadriesgo_next = None

        context['nivelcomplejidadriesgo_previous'] = nivelcomplejidadriesgo_previous
        context['nivelcomplejidadriesgo_next'] = nivelcomplejidadriesgo_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Nivel de complejidad y riesgo '" + str(self.object) + "'  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Nivel de complejidad y riesgo '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                messages.success(self.request, "Nivel de complejidad y riesgo '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(reverse('ucomplejidadriesgos:list_nivelcomplejidadriesgo'))
                #return render_to_response(self.template_name, self.get_context_data())


class NivelComplejidadRiesgoDelete(DeleteView):
    model = NivelComplejidadRiesgo
    form_class = NivelComplejidadRiesgoForm
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
        messages.success(self.request, "Nivel de complejidad y riesgo " + str(self.obj) + " eliminado con éxito.", extra_tags=next)
        return render(request, '../../mensaje/templates/mensaje.html', {'obj': context})
