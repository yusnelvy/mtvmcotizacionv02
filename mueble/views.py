from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.generic import ListView, View, UpdateView, DeleteView
from mueble.models import TipoDeMueble
from mueble.forms import TipoDeMuebleForm
#from mtvmcotizacionv02.views import valor_Personalizacionvisual
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

    # def get_paginate_by(self, queryset):
    #     if self.request.user.id is not None:
    #         nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
    #         range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
    #     else:
    #         nropag = valor_Personalizacionvisual("std", "paginacion")
    #         range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

    #     page = self.request.GET.get('page')
    #     if page == '0':
    #         return None
    #     else:
    #         return self.request.GET.get('paginate_by', nropag)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TipoDeMuebleListView, self).get_context_data(**kwargs)
        # Add in the pais
        # if self.request.user.id is not None:
        #     range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        # else:
        #     range_gap = valor_Personalizacionvisual("std", "rangopaginacion")
        range_gap = 3
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
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('umuebles:edit_tipodemueble',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('umuebles:list_tipodemueble'))

        return render(request, self.template_name, {'form': form})


class TipoDeMuebleUpdate(UpdateView):
    template_name = 'tipodemueble_edit.html'
    form_class = TipoDeMuebleForm
    model = TipoDeMueble

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TipoDeMuebleUpdate, self).get_context_data(**kwargs)
        # if self.request.user.id is not None:
        #     nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        # else:
        #     nropag = valor_Personalizacionvisual("std", "paginacion")
        nropag = 10

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

            messages.success(self.request, "TipoDeMueble " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return render_to_response(self.template_name, self.get_context_data())


class TipoDeMuebleDelete(DeleteView):
    model = TipoDeMueble
    form_class = TipoDeMuebleForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())
