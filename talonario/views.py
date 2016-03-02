"""
Docstring documentación pendiente

"""

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.generic import ListView, View, UpdateView, DeleteView
from talonario.models import TipoDeDocumentoImpreso, Talonario, DocumentoDelTalonario, \
    TalonarioEstado, DocumentoDelTalonarioEstado, TrazabilidadTalonario
from talonario.forms import TipoDeDocumentoImpresoForm, TalonarioForm, \
    DocumentoDelTalonarioForm
from gestiondedocumento.models import EstadoDeDocumento
from mtvmcotizacionv02.views import valor_Personalizacionvisual
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime


# Create your views here.
# app tipo de documento impreso
class TipoDeDocumentoImpresoListView(ListView):
    model = TipoDeDocumentoImpreso
    paginate_by = 10
    context_object_name = 'tipodedocumentoimpresos'
    template_name = 'tipodedocumentoimpreso_lista.html'

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
        context = super(TipoDeDocumentoImpresoListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        if order_by:
            lista_tipodedocumentoimpreso = TipoDeDocumentoImpreso.objects.all().order_by(order_by)
        else:
            lista_tipodedocumentoimpreso = TipoDeDocumentoImpreso.objects.all()

        paginator = Paginator(lista_tipodedocumentoimpreso, 10)
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
            queryset = TipoDeDocumentoImpreso.objects.all().order_by(order_by)
        else:
            queryset = TipoDeDocumentoImpreso.objects.all()

        return queryset


class TipoDeDocumentoImpresoView(View):
    form_class = TipoDeDocumentoImpresoForm
    template_name = 'tipodedocumentoimpreso_add.html'

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
                return HttpResponseRedirect(reverse('utalonarios:edit_tipodedocumentoimpreso',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect('utalonarios:list_tipodedocumentoimpreso')

        return render(request, self.template_name, {'form': form})


class TipoDeDocumentoImpresoUpdate(UpdateView):
    template_name = 'tipodedocumentoimpreso_edit.html'
    form_class = TipoDeDocumentoImpresoForm
    model = TipoDeDocumentoImpreso

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TipoDeDocumentoImpresoUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        tipodedocumentoimpreso = TipoDeDocumentoImpreso.objects.get(pk=self.object.pk)
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
            lista_tipodedocumentoimpreso = TipoDeDocumentoImpreso.objects.all().order_by(order_by)
        else:
            lista_tipodedocumentoimpreso = TipoDeDocumentoImpreso.objects.all()

        paginator = Paginator(lista_tipodedocumentoimpreso, nropag)
        # Show 25 contacts per page

        if page == '0':
            tipodedocumentoimpresos = lista_tipodedocumentoimpreso
        else:
            try:
                tipodedocumentoimpresos = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                tipodedocumentoimpresos = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                tipodedocumentoimpresos = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(tipodedocumentoimpresos.object_list[i].id == tipodedocumentoimpreso.id):
                    if tipodedocumentoimpresos.has_previous:
                        try:
                            previousitem = tipodedocumentoimpresos.object_list[i-1].id
                        except:
                            previousitem = None

                    if tipodedocumentoimpresos.has_next:
                        try:
                            nextitem = tipodedocumentoimpresos.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(tipodedocumentoimpresos)
            for i in range(0, countitem):
                if(tipodedocumentoimpresos[i].id == tipodedocumentoimpreso.id):
                    try:
                        previousitem = tipodedocumentoimpresos[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = tipodedocumentoimpresos[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            tipodedocumentoimpreso_previous = TipoDeDocumentoImpreso.objects.get(pk=previousitem)
        except:
            tipodedocumentoimpreso_previous = None
        try:
            tipodedocumentoimpreso_next = TipoDeDocumentoImpreso.objects.get(pk=nextitem)
        except:
            tipodedocumentoimpreso_next = None

        context['tipodedocumentoimpreso_previous'] = tipodedocumentoimpreso_previous
        context['tipodedocumentoimpreso_next'] = tipodedocumentoimpreso_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Tipo de documento impreso " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('utalonarios:list_tipodedocumentoimpreso'))
                #return render_to_response(self.template_name, self.get_context_data())


class TipoDeDocumentoImpresoDelete(DeleteView):
    model = TipoDeDocumentoImpreso
    form_class = TipoDeDocumentoImpresoForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app talonario
class TalonarioListView(ListView):
    model = Talonario
    paginate_by = 10
    context_object_name = 'talonarios'
    template_name = 'talonario_lista.html'

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
        context = super(TalonarioListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        if order_by:
            lista_talonario = Talonario.objects.all().order_by(order_by)
        else:
            lista_talonario = Talonario.objects.all()

        paginator = Paginator(lista_talonario, 10)
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
            queryset = Talonario.objects.all().order_by(order_by)
        else:
            queryset = Talonario.objects.all()

        return queryset


class TalonarioView(View):
    form_class = TalonarioForm
    template_name = 'talonario_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()
            estadoactual = EstadoDeDocumento.objects.filter(tipo_de_documento__tipo_de_documento='talonario',
                                                            estado_de_documento='creado')

            agregarestado = TalonarioEstado.objects.create(talonario=id_reg,
                                                           estado_de_documento_id=estadoactual[0].id,
                                                           usuario_id=2,
                                                           observacion='Creación del talonario',
                                                           predefinido=True)
            agregarestado.save()

            agregartrazabilidad = TrazabilidadTalonario.objects.create(talonario=id_reg,
                                                                       usuario_id=2,
                                                                       descripcion='Registro del talonario: ' + id_reg.talonario)
            agregartrazabilidad.save()

            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('utalonarios:edit_talonario',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('utalonarios:list_talonario'))

        return render(request, self.template_name, {'form': form})


class TalonarioUpdate(UpdateView):
    template_name = 'talonario_edit.html'
    form_class = TalonarioForm
    model = Talonario

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TalonarioUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        talonario = Talonario.objects.get(pk=self.object.pk)
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
            lista_talonario = Talonario.objects.all().order_by(order_by)
        else:
            lista_talonario = Talonario.objects.all()

        paginator = Paginator(lista_talonario, nropag)
        # Show 25 contacts per page

        if page == '0':
            talonarios = lista_talonario
        else:
            try:
                talonarios = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                talonarios = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                talonarios = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(talonarios.object_list[i].id == talonario.id):
                    if talonarios.has_previous:
                        try:
                            previousitem = talonarios.object_list[i-1].id
                        except:
                            previousitem = None

                    if talonarios.has_next:
                        try:
                            nextitem = talonarios.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(talonarios)
            for i in range(0, countitem):
                if(talonarios[i].id == talonario.id):
                    try:
                        previousitem = talonarios[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = talonarios[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            talonario_previous = Talonario.objects.get(pk=previousitem)
        except:
            talonario_previous = None
        try:
            talonario_next = Talonario.objects.get(pk=nextitem)
        except:
            talonario_next = None

        context['talonario_previous'] = talonario_previous
        context['talonario_next'] = talonario_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        agregartrazabilidad = TrazabilidadTalonario.objects.create(talonario=self.object,
                                                                   usuario_id=2,
                                                                   fecha_modificacion=datetime.now(),
                                                                   descripcion='Actualización del talonario: ' + self.object.talonario)
        agregartrazabilidad.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Talonario " + str(self.object) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('utalonarios:list_talonario'))
                #return render_to_response(self.template_name, self.get_context_data())


class TalonarioDelete(DeleteView):
    model = Talonario
    form_class = TalonarioForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app documento del talonario
class DocumentoDelTalonarioListView(ListView):
    model = DocumentoDelTalonario
    paginate_by = 10
    context_object_name = 'documentodeltalonarios'
    template_name = 'documentodeltalonario_lista.html'

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
        context = super(DocumentoDelTalonarioListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        if order_by:
            lista_documentodeltalonario = DocumentoDelTalonario.objects.all().order_by(order_by)
        else:
            lista_documentodeltalonario = DocumentoDelTalonario.objects.all()

        paginator = Paginator(lista_documentodeltalonario, 10)
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
            queryset = DocumentoDelTalonario.objects.all().order_by(order_by)
        else:
            queryset = DocumentoDelTalonario.objects.all()

        return queryset


class DocumentoDelTalonarioView(View):
    form_class = DocumentoDelTalonarioForm
    template_name = 'documentodeltalonario_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()
            estadoactual = EstadoDeDocumento.objects.filter(tipo_de_documento__descripcion='documento del talonario',
                                                            estado__estado='Activo')

            agregarestado = DocumentoDelTalonarioEstado.objects.create(documento_del_talonario=id_reg,
                                                                       estado_de_documento_id=estadoactual[0].id,
                                                                       usuario_id=2,
                                                                       observacion='Creación del documento',
                                                                       predefinido=True)
            agregarestado.save()

            if 'regEdit' in request.POST:
                messages.success(request, "Registro guardado.")
                return HttpResponseRedirect(reverse('utalonarios:edit_documentodeltalonario',
                                                    args=(id_reg.id,)))
            else:
                return HttpResponseRedirect(reverse('utalonarios:list_documentodeltalonario'))

        return render(request, self.template_name, {'form': form})


class DocumentoDelTalonarioUpdate(UpdateView):
    template_name = 'documentodeltalonario_edit.html'
    form_class = DocumentoDelTalonarioForm
    model = DocumentoDelTalonario

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DocumentoDelTalonarioUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        documentodeltalonario = DocumentoDelTalonario.objects.get(pk=self.object.pk)
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
            lista_documentodeltalonario = DocumentoDelTalonario.objects.all().order_by(order_by)
        else:
            lista_documentodeltalonario = DocumentoDelTalonario.objects.all()

        paginator = Paginator(lista_documentodeltalonario, nropag)
        # Show 25 contacts per page

        if page == '0':
            documentodeltalonarios = lista_documentodeltalonario
        else:
            try:
                documentodeltalonarios = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                documentodeltalonarios = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                documentodeltalonarios = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(documentodeltalonarios.object_list[i].id == documentodeltalonario.id):
                    if documentodeltalonarios.has_previous:
                        try:
                            previousitem = documentodeltalonarios.object_list[i-1].id
                        except:
                            previousitem = None

                    if documentodeltalonarios.has_next:
                        try:
                            nextitem = documentodeltalonarios.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(documentodeltalonarios)
            for i in range(0, countitem):
                if(documentodeltalonarios[i].id == documentodeltalonario.id):
                    try:
                        previousitem = documentodeltalonarios[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = documentodeltalonarios[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            documentodeltalonario_previous = DocumentoDelTalonario.objects.get(pk=previousitem)
        except:
            documentodeltalonario_previous = None
        try:
            documentodeltalonario_next = DocumentoDelTalonario.objects.get(pk=nextitem)
        except:
            documentodeltalonario_next = None

        context['documentodeltalonario_previous'] = documentodeltalonario_previous
        context['documentodeltalonario_next'] = documentodeltalonario_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_reg = self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Documento del talonario " + str(id_reg) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('utalonarios:list_documentodeltalonario'))
                #return render_to_response(self.template_name, self.get_context_data())


class DocumentoDelTalonarioDelete(DeleteView):
    model = DocumentoDelTalonario
    form_class = DocumentoDelTalonarioForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app trazabilidad talonario
class TrazabilidadTalonarioListView(ListView):
    model = TrazabilidadTalonario
    paginate_by = 10
    context_object_name = 'trazabilidadtalonarios'
    template_name = 'trazabilidadtalonario_lista.html'

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
        context = super(TrazabilidadTalonarioListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        if order_by:
            lista_trazabilidadtalonario = TrazabilidadTalonario.objects.all().order_by(order_by)
        else:
            lista_trazabilidadtalonario = TrazabilidadTalonario.objects.all()

        paginator = Paginator(lista_trazabilidadtalonario, 10)
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
            queryset = TrazabilidadTalonario.objects.all().order_by(order_by)
        else:
            queryset = TrazabilidadTalonario.objects.all()

        return queryset
