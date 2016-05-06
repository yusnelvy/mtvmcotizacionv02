"""
Docstring documentación pendiente

"""

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, View, UpdateView, DeleteView
from ambiente.models import Ambiente, AmbientePorTipoDeInmueble, \
    AmbienteEstadoDeRegistro
from ambiente.forms import AmbienteForm, AmbientePorTipoDeInmuebleForm
from estadoderegistro.models import EstadoDeRegistro
from direccion.models import EspecificacionDeInmueble
from mtvmcotizacionv02.views import valor_Personalizacionvisual, get_query
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table

from io import BytesIO
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required, login_required
from django.forms.formsets import formset_factory


# Create your views here.
# app ambiente
class AmbienteListView(ListView):
    model = Ambiente
    paginate_by = 10
    context_object_name = 'ambientes'
    template_name = 'ambiente_lista.html'

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
        context = super(AmbienteListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['ambiente',
                                             'descripcion', ])
            lista_ambiente = Ambiente.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['ambiente',
                                             'descripcion', ])
            lista_ambiente = Ambiente.objects.filter(entry_query)
        elif order_by:
            lista_ambiente = Ambiente.objects.all().order_by(order_by)
        else:
            lista_ambiente = Ambiente.objects.all()

        paginator = Paginator(lista_ambiente, 10)
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
            entry_query = get_query(search, ['ambiente',
                                             'descripcion', ])
            queryset = Ambiente.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['ambiente',
                                             'descripcion', ])
            queryset = Ambiente.objects.filter(entry_query)
        elif order_by:
            queryset = Ambiente.objects.all().order_by(order_by)
        else:
            queryset = Ambiente.objects.all()

        return queryset


class AmbienteView(View):
    form_class = AmbienteForm
    template_name = 'ambiente_add.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            estadoactual = EstadoDeRegistro.objects.filter(model='ambiente',
                                                           estado__estado='Activo')

            agregarestado = AmbienteEstadoDeRegistro.objects.create(ambiente=id_reg,
                                                                    estado_de_registro_id=estadoactual[0].id,
                                                                    usuario_id=self.request.user.id,
                                                                    predefinido=True)
            agregarestado.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Ambiente '" + str(id_reg) + "' agregado con éxito.",
                                 extra_tags=reverse('uambientes:list_ambiente'))
                return HttpResponseRedirect(reverse('uambientes:edit_ambiente',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Ambiente '" + str(id_reg) + "' agregado con éxito.")
                return HttpResponseRedirect(reverse('uambientes:list_ambiente'))

        return render(request, self.template_name, {'form': form})


class AmbienteUpdate(UpdateView):
    template_name = 'ambiente_edit.html'
    form_class = AmbienteForm
    model = Ambiente

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AmbienteUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        ambiente = Ambiente.objects.get(pk=self.object.pk)
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
            lista_ambiente = Ambiente.objects.all().order_by(order_by)
        else:
            lista_ambiente = Ambiente.objects.all()

        paginator = Paginator(lista_ambiente, nropag)
        # Show 25 contacts per page

        if page == '0':
            ambientes = lista_ambiente
        else:
            try:
                ambientes = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                ambientes = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                ambientes = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(ambientes.object_list[i].id == ambiente.id):
                    if ambientes.has_previous:
                        try:
                            previousitem = ambientes.object_list[i-1].id
                        except:
                            previousitem = None

                    if ambientes.has_next:
                        try:
                            nextitem = ambientes.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(ambientes)
            for i in range(0, countitem):
                if(ambientes[i].id == ambiente.id):
                    try:
                        previousitem = ambientes[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = ambientes[i+1].id
                    except:
                        nextitem = None
                    break
        try:
            ambiente_previous = Ambiente.objects.get(pk=previousitem)
        except:
            ambiente_previous = None
        try:
            ambiente_next = Ambiente.objects.get(pk=nextitem)
        except:
            ambiente_next = None

        context['ambiente_previous'] = ambiente_previous
        context['ambiente_next'] = ambiente_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Ambiente " + str(self.object) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Ambiente '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                messages.success(self.request, "Ambiente '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(reverse('uambientes:list_ambiente'))
                #return render_to_response(self.template_name, self.get_context_data())


class AmbienteDelete(DeleteView):
    model = Ambiente
    form_class = AmbienteForm
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
        messages.success(self.request, "Ambiente " + str(self.obj) + " eliminado con éxito.", extra_tags=next)
        return render(request, '../../mensaje/templates/mensaje.html', {'obj': context})


# app ambientes por tipo de inmueble
class AmbientePorTipoDeInmuebleListView(ListView):
    model = AmbientePorTipoDeInmueble
    paginate_by = 10
    context_object_name = 'ambientesportipoinmueble'
    template_name = 'ambienteportipodeinmueble_lista.html'

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
        context = super(AmbientePorTipoDeInmuebleListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['ambiente__ambiente',
                                             'especificacion_de_inmueble__especificacion_de_inmueble', ])
            lista_ambiente = AmbientePorTipoDeInmueble.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['ambiente__ambiente',
                                             'especificacion_de_inmueble__especificacion_de_inmueble', ])
            lista_ambiente = AmbientePorTipoDeInmueble.objects.filter(entry_query)
        elif order_by:
            lista_ambiente = AmbientePorTipoDeInmueble.objects.all().order_by(order_by)
        else:
            lista_ambiente = AmbientePorTipoDeInmueble.objects.all()

        paginator = Paginator(lista_ambiente, 10)
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
            entry_query = get_query(search, ['ambiente__ambiente',
                                             'especificacion_de_inmueble__especificacion_de_inmueble', ])
            queryset = AmbientePorTipoDeInmueble.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['ambiente__ambiente',
                                             'especificacion_de_inmueble__especificacion_de_inmueble', ])
            queryset = AmbientePorTipoDeInmueble.objects.filter(entry_query)
        elif order_by:
            queryset = AmbientePorTipoDeInmueble.objects.all().order_by(order_by)
        else:
            queryset = AmbientePorTipoDeInmueble.objects.all()

        return queryset


class AmbientePorTipoDeInmuebleView(View):
    form_class_formset = formset_factory(AmbientePorTipoDeInmuebleForm)
    template_name = 'ambienteportipodeinmueble_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""

        if self.request.GET.get('ambiente'):
            form_class_formset = formset_factory(AmbientePorTipoDeInmuebleForm,
                                                 extra=EspecificacionDeInmueble.objects.count(),
                                                 max_num=EspecificacionDeInmueble.objects.count())
            ambienteportipodeinmueble = AmbientePorTipoDeInmueble.objects.filter(ambiente=self.request.GET.get('var1'))
            inmueble = EspecificacionDeInmueble.objects.exclude(id__in=ambienteportipodeinmueble.values('especificacion_de_inmueble'))
            ambiente = Ambiente.objects.none()
        else:
            form_class_formset = formset_factory(AmbientePorTipoDeInmuebleForm,
                                                 extra=Ambiente.objects.count(),
                                                 max_num=Ambiente.objects.count())
            ambienteportipodeinmueble = AmbientePorTipoDeInmueble.objects.filter(especificacion_de_inmueble=self.request.GET.get('var2'))
            ambiente = Ambiente.objects.exclude(id__in=ambienteportipodeinmueble.values('ambiente'))
            inmueble = EspecificacionDeInmueble.objects.none()
        data = []

        if ambienteportipodeinmueble:

            for item in ambienteportipodeinmueble:
                data.append({'ambiente': item.ambiente,
                             'especificacion_de_inmueble': item.especificacion_de_inmueble,
                             'predeterminado': item.predeterminado,
                             'ch_agregar': True
                             })
        if ambiente:
            for item in ambiente:
                data.append({'ambiente': item.id,
                             'especificacion_de_inmueble': self.request.GET.get('var2')
                             })

        if inmueble:
            for item in inmueble:
                data.append({'ambiente': self.request.GET.get('var1'),
                             'especificacion_de_inmueble': item.id
                             })

        if len(data) > 0:
            formset = self.form_class_formset(initial=data)
        else:
            formset = self.form_class_formset()

        return render(request, self.template_name, {'formset': formset,
                                                    'ambienteportipodeinmueble': ambienteportipodeinmueble,
                                                    'inmueble': inmueble,
                                                    'ambiente': ambiente,
                                                    'variable1': Ambiente.objects.all(),
                                                    'variable2': EspecificacionDeInmueble.objects.all()})

    def post(self, request, *args, **kwargs):
        formset = self.form_class_formset(request.POST)
        if formset.is_valid():

            ambiente = self.request.GET.get('ambiente')
            if ambiente:
                existeambienteportipodeinmueble = AmbientePorTipoDeInmueble.objects.filter(ambiente=self.request.GET.get('var1'))
                if existecontenedor:
                    AmbientePorTipoDeInmueble.objects.filter(ambiente=
                                                             self.request.GET.get('var1')).delete()
            else:
                existeambienteportipodeinmueble = AmbientePorTipoDeInmueble.objects.filter(especificacion_de_inmueble=self.request.GET.get('var1'))
                if existecontenedor:
                    AmbientePorTipoDeInmueble.objects.filter(especificacion_de_inmueble=
                                                             self.request.GET.get('var1')).delete()

            for form in formset.forms:
                if form.cleaned_data.get('ch_agregar'):

                    add_ambienteportipodemueble(str(form.cleaned_data['ambiente'].id),
                                                str(form.cleaned_data['especificacion_de_inmueble'].id),
                                                str(form.cleaned_data['predeterminado'].id))
                #form.save()

            # <process form cleaned data>
            messages.success(self.request, "Registro guardado.")
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('uambientes:list_ambienteportipoinmueble'))

        return render(request, self.template_name, {'formset': formset})


# class AmbientePorTipoDeInmuebleView(View):
#     form_class = AmbientePorTipoDeInmuebleForm
#     template_name = 'ambienteportipodeinmueble_add.html'

#     def get(self, request, *args, **kwargs):
#         """docstring"""
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)

#         if form.is_valid():
#             id_reg = form.save()

#             if 'regEdit' in request.POST:
#                 messages.success(request, "Registro guardado.")
#                 return HttpResponseRedirect(reverse('uambientes:edit_ambienteportipoinmueble',
#                                                     args=(id_reg.id,)))
#             else:
#                 return HttpResponseRedirect(reverse('uambientes:list_ambienteportipoinmueble'))

#         return render(request, self.template_name, {'form': form})


class AmbientePorTipoDeInmuebleUpdate(UpdateView):
    template_name = 'ambienteportipodeinmueble_edit.html'
    form_class = AmbientePorTipoDeInmuebleForm
    model = AmbientePorTipoDeInmueble

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AmbientePorTipoDeInmuebleUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        ambienteportipoinmueble = AmbientePorTipoDeInmueble.objects.get(pk=self.object.pk)
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
            lista_ambienteportipoinmueble = AmbientePorTipoDeInmueble.objects.all().order_by(order_by)
        else:
            lista_ambienteportipoinmueble = AmbientePorTipoDeInmueble.objects.all()

        paginator = Paginator(lista_ambienteportipoinmueble, nropag)
        # Show 25 contacts per page

        if page == '0':
            ambientesportipoinmueble = lista_ambienteportipoinmueble
        else:
            try:
                ambientesportipoinmueble = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                ambientesportipoinmueble = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                ambientesportipoinmueble = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(ambientesportipoinmueble.object_list[i].id == ambienteportipoinmueble.id):
                    if ambientesportipoinmueble.has_previous:
                        try:
                            previousitem = ambientesportipoinmueble.object_list[i-1].id
                        except:
                            previousitem = None

                    if ambientesportipoinmueble.has_next:
                        try:
                            nextitem = ambientesportipoinmueble.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(ambientesportipoinmueble)
            for i in range(0, countitem):
                if(ambientesportipoinmueble[i].id == ambiente.id):
                    try:
                        previousitem = ambientesportipoinmueble[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = ambientesportipoinmueble[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            ambienteportipoinmueble_previous = AmbientePorTipoDeInmueble.objects.get(pk=previousitem)
        except:
            ambienteportipoinmueble_previous = None
        try:
            ambienteportipoinmueble_next = AmbientePorTipoDeInmueble.objects.get(pk=nextitem)
        except:
            ambienteportipoinmueble_next = None

        context['ambienteportipoinmueble_previous'] = ambienteportipoinmueble_previous
        context['ambienteportipoinmueble_next'] = ambienteportipoinmueble_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Ambiente por tipo de inmueble " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('uambientes:list_ambienteportipoinmueble'))
                #return render_to_response(self.template_name, self.get_context_data())


class AmbientePorTipoDeInmuebleDelete(DeleteView):
    model = AmbientePorTipoDeInmueble
    form_class = AmbientePorTipoDeInmuebleForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


def generar_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "ambientes.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    clientes = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Ambientes", styles['Heading1'])
    clientes.append(header)
    headings = ('Ambiente', 'Descripcion', 'Conteo')
    allclientes = [(p.ambiente, p.descripcion, p.conteo_de_ambientes) for p in Ambiente.objects.all()]

    t = Table([headings] + allclientes)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))
    clientes.append(t)
    doc.build(clientes)
    response.write(buff.getvalue())
    buff.close()
    return response
