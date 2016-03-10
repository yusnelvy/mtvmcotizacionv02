from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, JsonResponse
from django.template import RequestContext
from django.views.generic import ListView, View, UpdateView, DeleteView
from mtvmcotizacionv02.views import valor_Personalizacionvisual
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from widget.models import Widget
from widget.forms import WidgetForm
from django.forms.formsets import formset_factory


# Create your views here.
# app personalizacion visual
class WidgetListView(ListView):
    model = Widget
    paginate_by = 10
    context_object_name = 'widgets'
    template_name = 'widget_lista.html'

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
        context = super(WidgetListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        if order_by:
            lista_widget = Widget.objects.all().order_by(order_by)
        else:
            lista_widget = Widget.objects.all()

        paginator = Paginator(lista_widget, 10)
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
            queryset = Widget.objects.all().order_by(order_by)
        else:
            queryset = Widget.objects.all()

        return queryset


class WidgetView(View):
    form_class = WidgetForm
    template_name = 'widget_add.html'

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
                return HttpResponseRedirect(reverse('uwidgets:edit_widget',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('uwidgets:list_widget'))

        return render(request, self.template_name, {'form': form})


class WidgetUpdate(UpdateView):
    template_name = 'widget_edit.html'
    form_class = WidgetForm
    model = Widget

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(WidgetUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        widget = Widget.objects.get(pk=self.object.pk)
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
            lista_widget = Widget.objects.all().order_by(order_by)
        else:
            lista_widget = Widget.objects.all()

        paginator = Paginator(lista_widget, nropag)
        # Show 25 contacts per page

        if page == '0':
            widgets = lista_widget
        else:
            try:
                widgets = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                widgets = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                widgets = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(widgets.object_list[i].id == widget.id):
                    if widgets.has_previous:
                        try:
                            previousitem = widgets.object_list[i-1].id
                        except:
                            previousitem = None

                    if widgets.has_next:
                        try:
                            nextitem = widgets.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(widgets)
            for i in range(0, countitem):
                if(widgets[i].id == widget.id):
                    try:
                        previousitem = widgets[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = widgets[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            widget_previous = Widget.objects.get(pk=previousitem)
        except:
            widget_previous = None
        try:
            widget_next = Widget.objects.get(pk=nextitem)
        except:
            widget_next = None

        context['widget_previous'] = widget_previous
        context['widget_next'] = widget_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Widget " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('uwidgets:list_widget'))
                #return render_to_response(self.template_name, self.get_context_data())


class WidgetDelete(DeleteView):
    model = Widget
    form_class = WidgetForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


class ConfigurarWidgetView(View):
    form_class_formset = formset_factory(WidgetForm,
                                         extra=Widget.objects.filter(usuario=1).count(),
                                         max_num=Widget.objects.filter(usuario=1).count())
    template_name = 'widget_configuracion.html'
    def get(self, request, *args, **kwargs):

        """docstring"""
        user = 1
        widgets = Widget.objects.filter(usuario=1)
        if widgets:
           data = []
           for item in widgets:
               data.append({'nombre': item.nombre,
                            'visible': item.visible,
                            'desplegable': item.desplegable,
                            'numero_de_columna': item.numero_de_columna,
                            'color': item.color,
                            'orden': item.orden,
                            'usuario': 1
                            })

           formset = self.form_class_formset(initial=data)
        else:
           formset = self.form_class_formset()

        return render(request, self.template_name, {'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.form_class_formset(request.POST)
        if formset.is_valid():
            for form in formset:
                #params = urllib.urlencode({'mueble': 'form.cleaned_data["mueble"]'})
                form.save()
            # <process form cleaned data>
            messages.success(self.request, "Registro guardado.")
            return HttpResponseRedirect(reverse('uwidgets:configurar_widget'))

        else:
            for form in formset:
                widgets = Widget.objects.filter(usuario_id=form.cleaned_data['usuario'],
                                                nombre=form.cleaned_data['nombre'])
                if widgets:
                    widgets.update(visible=form.cleaned_data['visible'],
                                   desplegable=form.cleaned_data['desplegable'],
                                   numero_de_columna=form.cleaned_data['numero_de_columna'],
                                   color=form.cleaned_data['color'],
                                   orden=form.cleaned_data['orden'])
                else:
                    form.save()
            messages.success(self.request, "Registro guardado.")
            return HttpResponseRedirect(reverse('uwidgets:configurar_widget'))
        return render(request, self.template_name, {'formset': formset})


def cambiar_WidgetVisible(request):
    """docstring"""
    if request.method == "GET" and request.is_ajax():
        name = request.GET['name']
        Widget.objects.filter(nombre=name).update(visible=False)



