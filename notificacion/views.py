from django.shortcuts import render
from django.http import HttpResponseRedirect
from notificacion.models import Notificacion, NotificacionEstado
from notificacion.forms import NotificacionForm
from gestiondedocumento.models import EstadoDeDocumento
from django.views.generic import ListView, View, UpdateView, DeleteView
from mtvmcotizacionv02.views import valor_Personalizacionvisual, get_query
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# app notificacion
class NotificacionListView(ListView):
    model = Notificacion
    paginate_by = 10
    context_object_name = 'notificaciones'
    template_name = 'notificacion_lista.html'

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
        context = super(NotificacionListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['origen',
                                             'titulo',
                                             'texto',
                                             'estado',
                                             'user',
                                             'user_origen', ])
            lista_notificacion = Notificacion.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['origen',
                                             'titulo',
                                             'texto',
                                             'estado',
                                             'user',
                                             'user_origen', ])
            lista_notificacion = Notificacion.objects.filter(entry_query)
        elif order_by:
            lista_notificacion = Notificacion.objects.all().order_by(order_by)
        else:
            lista_notificacion = Notificacion.objects.all()

        paginator = Paginator(lista_notificacion, 10)
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
            entry_query = get_query(search, ['origen',
                                             'titulo',
                                             'texto',
                                             'estado',
                                             'user',
                                             'user_origen', ])
            queryset = Notificacion.objects.filter(entry_query
                                                   ).order_by(order_by
                                                              ).exclude(estado='Por entregar'
                                                                        ).exclude(estado='Eliminada'
                                                                                  ).exclude(estado='Archivada')
        elif search is not None and search != u"":
            entry_query = get_query(search, ['origen',
                                             'titulo',
                                             'texto',
                                             'estado',
                                             'user',
                                             'user_origen', ])
            queryset = Notificacion.objects.filter(entry_query
                                                   ).exclude(estado='Por entregar'
                                                             ).exclude(estado='Eliminada'
                                                                       ).exclude(estado='Archivada')
        elif order_by:
            queryset = Notificacion.objects.order_by(order_by
                                                     ).exclude(estado='Por entregar'
                                                               ).exclude(estado='Eliminada'
                                                                         ).exclude(estado='Archivada')
        else:
            queryset = Notificacion.objects.exclude(estado='Por entregar'
                                                    ).exclude(estado='Eliminada'
                                                              ).exclude(estado='Archivada')

        return queryset


class NotificacionView(View):
    form_class = NotificacionForm
    template_name = 'notificacion_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            estadoactual = EstadoDeDocumento.objects.filter(tipo_de_documento__tipo_de_documento='notificacion',
                                                            orden=1)
            id_reg = form.save(commit=False)
            id_reg.estado = estadoactual[0].estado_de_documento
            id_reg.save()

            agregarestadodedocumento = NotificacionEstado.objects.create(notificacion_id=id_reg.id,
                                                                         estado_de_documento_id=estadoactual[0].id,
                                                                         usuario_registro_id=2,
                                                                         observacion='creación de la notificación',
                                                                         predefinido=True)
            agregarestadodedocumento.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Notificacion '" + str(id_reg) + "' agregado con éxito.",
                                 extra_tags=reverse('unotificaciones:list_notificacion'))
                return HttpResponseRedirect(reverse('unotificaciones:edit_notificacion',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Notificacion '" + str(id_reg) + "' agregado con éxito.")
                return HttpResponseRedirect(reverse('unotificaciones:list_notificacion'))

        return render(request, self.template_name, {'form': form})


class NotificacionUpdate(UpdateView):
    template_name = 'notificacion_edit.html'
    form_class = NotificacionForm
    model = Notificacion

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(NotificacionUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        notificacion = Notificacion.objects.get(pk=self.object.pk)
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
            lista_notificacion = Notificacion.objects.order_by(order_by
                                                               ).exclude(estado='Por entregar'
                                                                         ).exclude(estado='Eliminada'
                                                                                   ).exclude(estado='Archivada')
        else:
            lista_notificacion = Notificacion.objects.exclude(estado='Por entregar'
                                                              ).exclude(estado='Eliminada'
                                                                        ).exclude(estado='Archivada')

        paginator = Paginator(lista_notificacion, nropag)
        # Show 25 contacts per page

        if page == '0':
            notificaciones = lista_notificacion
        else:
            try:
                notificaciones = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                notificaciones = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                notificaciones = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(notificaciones.object_list[i].id == notificacion.id):
                    if notificaciones.has_previous:
                        try:
                            previousitem = notificaciones.object_list[i-1].id
                        except:
                            previousitem = None

                    if notificaciones.has_next:
                        try:
                            nextitem = notificaciones.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(notificaciones)
            for i in range(0, countitem):
                if(notificaciones[i].id == notificacion.id):
                    try:
                        previousitem = notificaciones[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = notificaciones[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            notificacion_previous = Notificacion.objects.get(pk=previousitem)
        except:
            notificacion_previous = None
        try:
            notificacion_next = Notificacion.objects.get(pk=nextitem)
        except:
            notificacion_next = None

        context['notificacion_previous'] = notificacion_previous
        context['notificacion_next'] = notificacion_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Notificacion " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('unotificaciones:list_notificacion'))
                #return render_to_response(self.template_name, self.get_context_data())


class NotificacionDelete(DeleteView):
    model = Notificacion
    form_class = NotificacionForm
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

        estadoactual = EstadoDeDocumento.objects.filter(tipo_de_documento__tipo_de_documento='notificacion',
                                                        orden=6)
        self.obj.estado = estadoactual[0].estado_de_documento
        self.obj.save()
        agregarestadodedocumento = NotificacionEstado.objects.create(notificacion_id=self.obj.id,
                                                                     estado_de_documento_id=estadoactual[0].id,
                                                                     usuario_registro_id=2,
                                                                     observacion='Enviar la ' + self.obj +
                                                                                 ' notificación a la papelera',
                                                                     predefinido=True)
        agregarestadodedocumento.save()

        messages.success(self.request, "Notificación " + str(self.obj) + " eliminado con éxito.", extra_tags=next)
        return render(request, '../../mensaje/templates/mensaje.html', {'obj': context})
