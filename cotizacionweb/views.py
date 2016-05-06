"""
Docstring documentación pendiente

"""

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, \
    JsonResponse
from django.views.generic import ListView, View, UpdateView, \
    DeleteView, DetailView
from cotizacionweb.models import Cotizacion, CotizacionEstado,\
    CotizacionDireccion, TipoDireccion, CotizacionBitacora, \
    CotizacionAmbiente, CotizacionMueble, FechaDeCotizacion, \
    CotizacionHistoricoFecha, ServicioMueble, ContenedorMueble, \
    ConceptoDeCotizacion, CotizacionMueble
from cotizacionweb.forms import CotizacionForm, TipoDireccionForm, \
    ConceptoDeCotizacionForm, FechaDeCotizacionForm, CotizacionBitacoraForm, \
    CotizacionAmbienteForm, CotizacionMuebleForm, ContenedorMuebleForm, \
    ServicioMuebleForm, CotizacionDireccionForm
from cliente.models import Cliente, InformacionDeContacto, ClienteDireccion
from estadoderegistro.models import EstadoDeRegistro
from gestiondedocumento.models import EstadoDeDocumento
from direccion.models import Edificacion, Inmueble
from django.views.generic.edit import FormMixin
from django.core.urlresolvers import reverse
from ambiente.models import AmbientePorTipoDeInmueble, Ambiente
from mueble.models import MueblePorAmbiente, EspecificacionDeMueble
from contenedor.models import ContenedorTipicoPorMueble, Contenedor
from servicio.models import ServicioTipicoPorMueble, ComplejidadServicio, \
    Servicio
from mtvmcotizacionv02.views import valor_Personalizacionvisual, get_query
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from decimal import Decimal
from django.db.models import Sum
from django.forms.formsets import formset_factory
from django.contrib.auth.decorators import permission_required, login_required


# Create your views here.
# app cotización
class CotizacionListView(ListView):
    model = Cotizacion
    paginate_by = 10
    context_object_name = 'cotizaciones'
    template_name = 'cotizacion_lista.html'

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
        context = super(CotizacionListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['nombre_cliente',
                                             'cotizador__id_trabajador__nombre',
                                             'cotizador__id_trabajador__apellido',
                                             'numero_contrato',
                                             'numero_cotizacion',
                                             'fecha_de_cotizacion',
                                             'tiempo_carga',
                                             'total_recorrido_tiempo',
                                             'total_recorrido_km',
                                             'nivel_de_complejidad_riesgo',
                                             'porcentaje_complejidad_riesgo',
                                             'como_abona__tipo_abono', ])
            lista_cotizacion = Cotizacion.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['nombre_cliente',
                                             'cotizador__id_trabajador__nombre',
                                             'cotizador__id_trabajador__apellido',
                                             'numero_contrato',
                                             'numero_cotizacion',
                                             'fecha_de_cotizacion',
                                             'tiempo_carga',
                                             'total_recorrido_tiempo',
                                             'total_recorrido_km',
                                             'nivel_de_complejidad_riesgo',
                                             'porcentaje_complejidad_riesgo',
                                             'como_abona__tipo_abono', ])
            lista_cotizacion = Cotizacion.objects.filter(entry_query)
        elif order_by:
            lista_cotizacion = Cotizacion.objects.all().order_by(order_by)
        else:
            lista_cotizacion = Cotizacion.objects.all()

        paginator = Paginator(lista_cotizacion, 10)
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
            entry_query = get_query(search, ['nombre_cliente',
                                             'cotizador__id_trabajador__nombre',
                                             'cotizador__id_trabajador__apellido',
                                             'numero_contrato',
                                             'numero_cotizacion',
                                             'fecha_de_cotizacion',
                                             'tiempo_carga',
                                             'total_recorrido_tiempo',
                                             'total_recorrido_km',
                                             'nivel_de_complejidad_riesgo',
                                             'porcentaje_complejidad_riesgo',
                                             'como_abona__tipo_abono', ])
            queryset = Cotizacion.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['nombre_cliente',
                                             'cotizador__id_trabajador__nombre',
                                             'cotizador__id_trabajador__apellido',
                                             'numero_contrato',
                                             'numero_cotizacion',
                                             'fecha_de_cotizacion',
                                             'tiempo_carga',
                                             'total_recorrido_tiempo',
                                             'total_recorrido_km',
                                             'nivel_de_complejidad_riesgo',
                                             'porcentaje_complejidad_riesgo',
                                             'como_abona__tipo_abono', ])
            queryset = Cotizacion.objects.filter(entry_query)
        elif order_by:
            queryset = Cotizacion.objects.all().order_by(order_by)
        else:
            queryset = Cotizacion.objects.all()

        return queryset


class CotizacionDetail(FormMixin, DetailView):
    model = Cotizacion
    form_class = CotizacionForm
    context_object_name = "cotizacion"
    template_name = 'cotizacion_ficha.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CotizacionDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['contacto_cliente'] = InformacionDeContacto.objects.filter(contacto__cliente=self.object.cliente,
                                                                           contacto__tipo_de_relacion__tipo_de_relacion='cliente')
        context['contactos'] = InformacionDeContacto.objects.filter(contacto__cliente=self.object.cliente).exclude(contacto__tipo_de_relacion__tipo_de_relacion='cliente')
        context['direccion_origen'] = CotizacionDireccion.objects.filter(
            cotizacion=self.object.pk, tipo_direccion__tipo_direccion="Origen")
        context['direccion_destino'] = CotizacionDireccion.objects.filter(
            cotizacion=self.object.pk, tipo_direccion__tipo_direccion="Destino")

        context['mudanza'] = CotizacionHistoricoFecha.objects.filter(cotizacion=self.object.pk,
                                                                     nombre_tipo_fecha='Mudanza')
        context['visita'] = CotizacionHistoricoFecha.objects.filter(cotizacion=self.object.pk,
                                                                    nombre_tipo_fecha='Visita del cotizador')
        context['ambientes'] = CotizacionAmbiente.objects.filter(direccion_origen__cotizacion=self.object.pk)
        context['muebles'] = CotizacionMueble.objects.filter(cotizacion_ambiente__direccion_origen__cotizacion=self.object.pk)
        context['bitacora'] = CotizacionBitacora.objects.filter(cotizacion=self.object.pk)
        context['estadoactual'] = CotizacionEstado.objects.filter(cotizacion=self.object.pk,
                                                                  predefinido=True).exclude(estado_de_documento=None)
        context['fechasdecotizacion'] = CotizacionHistoricoFecha.objects.filter(cotizacion=self.object.pk).order_by('fecha')

        context['form'] = self.get_form()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        cotizacion = Cotizacion.objects.filter(pk=self.object.pk)
        cotizacion.update(cotizador=form.cleaned_data['cotizador'])

        if form.cleaned_data['fecha_mudanza']:
            mudanza = FechaDeCotizacion.objects.filter(nombre_fecha='Mudanza')
            if mudanza:
                agregarfecha = CotizacionHistoricoFecha.objects.create(cotizacion_id=self.object.pk,
                                                                       usuario_registro_id=2,
                                                                       tipo_fecha_id=mudanza[0].id,
                                                                       nombre_tipo_fecha=mudanza[0].nombre_fecha,
                                                                       fecha=form.cleaned_data['fecha_mudanza'],
                                                                       observacion='Fecha de la mudanza',
                                                                       aplicar=True)
                agregarfecha.save()

        if form.cleaned_data['fecha_visita']:
            visita = FechaDeCotizacion.objects.filter(nombre_fecha='Visita del cotizador')
            if visita:
                agregarfecha = CotizacionHistoricoFecha.objects.create(cotizacion_id=self.object.pk,
                                                                       usuario_registro_id=2,
                                                                       tipo_fecha_id=visita[0].id,
                                                                       nombre_tipo_fecha=visita[0].nombre_fecha,
                                                                       fecha=form.cleaned_data['fecha_visita'],
                                                                       observacion='Fecha de la visita',
                                                                       aplicar=True)
                agregarfecha.save()

                updateestado = CotizacionEstado.objects.filter(cotizacion=self.object.pk,
                                                               predefinido=True).exclude(estado_de_documento=None)
                updateestado.update(predefinido=False)

                estadoactual = EstadoDeDocumento.objects.filter(tipo_de_documento__tipo_de_documento='cotizacion',
                                                                orden=3)

                agregarestadodedocumento = CotizacionEstado.objects.create(cotizacion_id=self.object.pk,
                                                                           estado_de_documento_id=estadoactual[0].id,
                                                                           usuario_registro_id=2,
                                                                           observacion='Visita agendada',
                                                                           predefinido=True)
                agregarestadodedocumento.save()

                bitacora = CotizacionBitacora.objects.create(cotizacion_id=self.object.pk,
                                                             usuario_registro_id=2,
                                                             origen_de_registro='A',
                                                             observacion='Asignación de visita para el dia ' +
                                                                         str(form.cleaned_data['fecha_visita']) +
                                                                         ' del cotizador (falta definir)')
                bitacora.save()

        return render_to_response(self.template_name, self.get_context_data())

    def form_invalid(self, form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form))


#direccion
class CotizacionDireccionDelete(DeleteView):
    model = CotizacionDireccion
    form_class = CotizacionDireccionForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


#ambiente
class CotizacionAmbienteDetail(FormMixin, DetailView):
    model = CotizacionAmbiente
    form_class = CotizacionAmbienteForm
    context_object_name = "cotizacionambiente"
    template_name = 'cotizacionambiente_ficha.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CotizacionAmbienteDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books

        context['muebles'] = CotizacionMueble.objects.filter(cotizacion_ambiente=self.object.pk)

        context['ambientes'] = CotizacionAmbiente.objects.filter(direccion_origen__cotizacion=self.object.direccion_origen.cotizacion)
        return context


class CotizacionAmbienteView(View):
    form_class_formset = formset_factory(CotizacionAmbienteForm,
                                         extra=Ambiente.objects.count(),
                                         max_num=Ambiente.objects.count())
    template_name = 'cotizacionambiente_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        direccion = self.request.GET.get('direccion')
        direccion_origen = CotizacionDireccion.objects.get(pk=direccion)
        ambienteportipodeinmueble = Ambiente.objects.filter(ambienteportipodeinmueble__especificacion_de_inmueble__especificacion_de_inmueble=
                                                            direccion_origen.especificacion_de_inmueble)
        ambientes = Ambiente.objects.exclude(id__in=ambienteportipodeinmueble)
        data = []
        if ambienteportipodeinmueble:

            for item in ambienteportipodeinmueble:
                data.append({'direccion_origen': direccion,
                             'ambiente': item.id,
                             'nombre': item.ambiente,
                             })
        if ambientes:

            for item in ambientes:
                data.append({'direccion_origen': direccion,
                             'ambiente': item.id,
                             'nombre': item.ambiente,
                             })

            formset = self.form_class_formset(initial=data)
        else:
            formset = self.form_class_formset()

        return render(request, self.template_name, {'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.form_class_formset(request.POST)
        if formset.is_valid():
            for form in formset.forms:
                if form.cleaned_data.get('ch_ambiente'):
                    agregarambiente = add_cotizacionambiente(str(form.cleaned_data['direccion_origen'].id),
                                                             str(form.cleaned_data['ambiente'].id),
                                                             form.cleaned_data['nombre'],
                                                             form.cleaned_data['observaciones'])

                    direccion_origen = CotizacionDireccion.objects.get(pk=form.cleaned_data['direccion_origen'].id)
                    direccion_destino = CotizacionDireccion.objects.filter(cotizacion=direccion_origen.cotizacion)
                    ambienteportipoinmuble = AmbientePorTipoDeInmueble.objects.filter(especificacion_de_inmueble__especificacion_de_inmueble=
                                                                                      direccion_origen.especificacion_de_inmueble,
                                                                                      ambiente=form.cleaned_data['ambiente'].id)
                    if ambienteportipoinmuble:
                        muebles = MueblePorAmbiente.objects.filter(predefinido=True,
                                                                   ambiente_por_tipo_de_inmueble=ambienteportipoinmuble[0].id)
                        if muebles:
                            for mueble in muebles:
                                agregarmueble = add_cotizacionmueble(agregarambiente,
                                                                     mueble.especificacion_de_mueble.id,
                                                                     direccion_destino[0].id,
                                                                     mueble.especificacion_de_mueble.especificacion_de_mueble,
                                                                     mueble.especificacion_de_mueble.ancho,
                                                                     mueble.especificacion_de_mueble.alto,
                                                                     mueble.especificacion_de_mueble.largo, 1,
                                                                     mueble.especificacion_de_mueble.volumen_en_camion,
                                                                     mueble.especificacion_de_mueble.mueble.trasladable, '')

                                contenedores = ContenedorTipicoPorMueble.objects.filter(especificacion_de_mueble=mueble.especificacion_de_mueble.id)
                                for contenedor in contenedores:
                                    add_contenedormueble(agregarmueble,
                                                         contenedor.contenedor.id,
                                                         contenedor.tipo_de_contenido.id,
                                                         contenedor.contenedor.contenedor,
                                                         contenedor.cantidad)

                                contenedoremueble = ContenedorMueble.objects.filter(cotizacion_mueble=agregarmueble)
                                qcontenedorn = 0
                                qcontenedorf = 0
                                for cont in contenedoremueble:
                                    if (cont.tipo_de_contenido.nombre == 'objetos frágiles' or cont.tipo_de_contenido.nombre == 'textiles'):
                                        qcontenedorf = qcontenedorf + cont.cantidad
                                    else:
                                        qcontenedorn = qcontenedorn + cont.cantidad

                                servicios = ServicioTipicoPorMueble.objects.filter(predefinido=True,
                                                                                   especificacion_de_mueble=mueble.especificacion_de_mueble.id)
                                for servicio in servicios:
                                    cantidadservicio = servicio_cantidad(servicio.servicio.servicio,
                                                                         1, qcontenedorn, qcontenedorf,
                                                                         mueble.especificacion_de_mueble.volumen_de_mueble,
                                                                         direccion_origen.cantidad_pisos)

                                    add_serviciomueble(agregarmueble, servicio.servicio.id,
                                                       servicio.servicio.servicio,
                                                       cantidadservicio['cantidadservicio'],
                                                       cantidadservicio['descripcioncantidad'])
                #form.save()

            # <process form cleaned data>
            messages.success(self.request, "Registro guardado.")
            return HttpResponseRedirect(reverse('ucotizacionesweb:ficha_cotizacion',
                                        args=(direccion_origen.cotizacion.id,)))
        return render(request, self.template_name, {'formset': formset})


class CotizacionAmbienteDelete(DeleteView):
    model = CotizacionAmbiente
    form_class = CotizacionAmbienteForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            messages.success(self.request, "Ambiente '" + str(self.obj) + "'  eliminado con éxito.")
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


#mueble
class CotizacionMuebleView(View):
    form_class = CotizacionMuebleForm
    template_name = 'cotizacionmueble_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        if self.request.is_ajax():
            mueble_id = self.request.GET.get('id_especificacion_de_mueble')
            if mueble_id:
                mueble = EspecificacionDeMueble.objects.get(id=mueble_id)
                if mueble:
                    mueble = [{
                        'nombremueble': mueble.especificacion_de_mueble,
                        'trasladable': mueble.mueble.trasladable,
                        'ancho': mueble.ancho,
                        'largo': mueble.largo,
                        'alto': mueble.alto,
                        'volumenencamion': mueble.volumen_en_camion
                    }]

                return JsonResponse(mueble, safe=False)

        direcciondestino = CotizacionDireccion.objects.filter(tipo_direccion__tipo_direccion="Destino",
                                                              orden=1)
        if self.request.GET.get('ambiente'):
            data = {
                'cotizacion_ambiente': self.request.GET.get('ambiente'),
                'direccion_destino': direcciondestino[0].id
                }
        else:
            data = {
                'direccion_destino': direcciondestino[0].id
                }

        form = self.form_class(initial=data)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            mueble = CotizacionMueble.objects.filter(id=id_reg.id)

            contenedores = ContenedorTipicoPorMueble.objects.filter(especificacion_de_mueble=id_reg.especificacion_de_mueble.id)
            for contenedor in contenedores:
                add_contenedormueble(id_reg.id,
                                     contenedor.contenedor.id,
                                     contenedor.tipo_de_contenido.id,
                                     contenedor.contenedor.contenedor,
                                     (contenedor.cantidad*mueble[0].cantidad))

            contenedoremueble = ContenedorMueble.objects.filter(cotizacion_mueble=mueble[0].id)
            qcontenedorn = 0
            qcontenedorf = 0
            for cont in contenedoremueble:
                if (cont.tipo_de_contenido.nombre == 'objetos frágiles' or cont.tipo_de_contenido.nombre == 'textiles'):
                    qcontenedorf = qcontenedorf + cont.cantidad
                else:
                    qcontenedorn = qcontenedorn + cont.cantidad

            servicios = ServicioTipicoPorMueble.objects.filter(predefinido=True,
                                                               especificacion_de_mueble=mueble[0].especificacion_de_mueble.id)
            for servicio in servicios:
                cantidadservicio = servicio_cantidad(servicio.servicio.servicio,
                                                     mueble[0].cantidad,
                                                     qcontenedorn, qcontenedorf,
                                                     mueble[0].volumen,
                                                     mueble[0].cotizacion_ambiente.direccion_origen.cantidad_pisos)

                add_serviciomueble(id_reg.id, servicio.servicio.id,
                                   servicio.servicio.servicio,
                                   cantidadservicio['cantidadservicio'],
                                   cantidadservicio['descripcioncantidad'])

            messages.success(self.request, "Mueble '" + str(mueble[0].especificacion_de_mueble.id) + "'  registrado con éxito.")
            if 'regEdit' in request.POST:
                return HttpResponseRedirect(reverse('ucotizacionesweb:edit_tipodireccion',
                                                    args=(id_reg.id,)))
            else:
                redirect_to = self.request.REQUEST.get('next', '')
                if redirect_to:
                    return HttpResponseRedirect(redirect_to)
                else:
                    return HttpResponseRedirect(reverse('ucotizacionesweb:ficha_cotizacionambiente',
                                                args=(id_reg.cotizacion_ambiente,)))

        return render(request, self.template_name, {'form': form})


class CotizacionMuebleUpdate(UpdateView):
    template_name = 'cotizacionmueble_edit.html'
    form_class = CotizacionMuebleForm
    model = CotizacionMueble

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CotizacionMuebleUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        cotizacionmueble = CotizacionMueble.objects.get(pk=self.object.pk)
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
            lista_cotizacionmueble = CotizacionMueble.objects.all().order_by(order_by)
        else:
            lista_cotizacionmueble = CotizacionMueble.objects.all()

        paginator = Paginator(lista_cotizacionmueble, nropag)
        # Show 25 contacts per page

        if page == '0':
            cotizacionmuebles = lista_cotizacionmueble
        else:
            try:
                cotizacionmuebles = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                cotizacionmuebles = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                cotizacionmuebles = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(cotizacionmuebles.object_list[i].id == cotizacionmueble.id):
                    if cotizacionmuebles.has_previous:
                        try:
                            previousitem = cotizacionmuebles.object_list[i-1].id
                        except:
                            previousitem = None

                    if cotizacionmuebles.has_next:
                        try:
                            nextitem = cotizacionmuebles.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(cotizacionmuebles)
            for i in range(0, countitem):
                if(cotizacionmuebles[i].id == cotizacionmueble.id):
                    try:
                        previousitem = cotizacionmuebles[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = cotizacionmuebles[i+1].id
                    except:
                        nextitem = None
                    break
        try:
            cotizacionmueble_previous = CotizacionMueble.objects.get(pk=previousitem)
        except:
            cotizacionmueble_previous = None
        try:
            cotizacionmueble_next = CotizacionMueble.objects.get(pk=nextitem)
        except:
            cotizacionmueble_next = None

        context['cotizacionmueble_previous'] = cotizacionmueble_previous
        context['cotizacionmueble_next'] = cotizacionmueble_next
        context['contenedores'] = ContenedorMueble.objects.filter(cotizacion_mueble=self.object.pk)
        context['servicios'] = ServicioMueble.objects.filter(cotizacion_mueble=self.object.pk)

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        contenedores = ContenedorMueble.objects.filter(cotizacion_mueble=self.object.id)
        qcontenedorn = 0
        qcontenedorf = 0

        for contenedor in contenedores:
            if (contenedor.tipo_de_contenido.nombre == 'objetos frágiles' or contenedor.tipo_de_contenido.nombre == 'textiles'):
                qcontenedorf = qcontenedorf + contenedor.cantidad
            else:
                qcontenedorn = qcontenedorn + contenedor.cantidad

            contenedortipico = ContenedorTipicoPorMueble.objects.filter(contenedor=contenedor.contenedor,
                                                                        especificacion_de_mueble=self.object.especificacion_de_mueble,
                                                                        tipo_de_contenido=contenedor.tipo_de_contenido)

            if contenedortipico:
                edit_contenedormueble(contenedor.id, contenedor.tipo_de_contenido, (contenedortipico[0].cantidad*self.object.cantidad))

        servicios = ServicioMueble.objects.filter(cotizacion_mueble=self.object.id)
        for servicio in servicios:
            serviciotipico = ServicioTipicoPorMueble.objects.filter(servicio=servicio.servicio,
                                                                    especificacion_de_mueble=self.object.especificacion_de_mueble)
            if serviciotipico:
                cantidadservicio = servicio_cantidad(servicio.servicio.servicio,
                                                     self.object.cantidad, qcontenedorn, qcontenedorf,
                                                     self.object.volumen,
                                                     self.object.cotizacion_ambiente.direccion_origen.cantidad_pisos)
                edit_serviciomueble(servicio.id, cantidadservicio['cantidadservicio'],
                                    cantidadservicio['descripcioncantidad'])

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Mueble " + str(self.object) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Mueble '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                messages.success(self.request, "Mueble '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(reverse('ucotizacionesweb:ficha_cotizacionambiente',
                                            args=(self.object.cotizacion_ambiente,)))


class CotizacionMuebleDelete(DeleteView):
    model = CotizacionMueble
    form_class = CotizacionMuebleForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            messages.success(self.request, "mueble '" + str(self.obj) + "'  eliminado con éxito.")
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# contenedor mueble
class ContenedorMuebleView(View):
    form_class_formset = formset_factory(ContenedorMuebleForm,
                                         extra=Contenedor.objects.count(),
                                         max_num=Contenedor.objects.count())
    template_name = 'contenedormueble_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        mueble = CotizacionMueble.objects.get(id=self.request.GET.get('mueble'))
        contenedormueble = ContenedorMueble.objects.filter(cotizacion_mueble=
                                                           mueble.id)

        contenedortipicopormueble = ContenedorTipicoPorMueble.objects.filter(especificacion_de_mueble=
                                                                             mueble.especificacion_de_mueble.id
                                                                             ).exclude(contenedor__in=contenedormueble.values('contenedor'))
        contenedores = Contenedor.objects.exclude(id__in=contenedortipicopormueble.values('contenedor'))
        data = []

        if contenedormueble:

            for item in contenedormueble:
                data.append({'cotizacion_mueble': mueble.id,
                             'contenedor': item.contenedor,
                             'tipo_de_contenido': item.tipo_de_contenido,
                             'nombre_contenedor': item.nombre_contenedor,
                             'cantidad': item.cantidad,
                             'ch_contenedor': True
                             })
        if contenedortipicopormueble:
            for item in contenedortipicopormueble:
                data.append({'cotizacion_mueble': mueble.id,
                             'contenedor': item.contenedor,
                             'tipo_de_contenido': item.tipo_de_contenido,
                             'nombre_contenedor': item.contenedor.contenedor,
                             'cantidad': item.cantidad
                             })

        if contenedores:

            for item in contenedores:
                data.append({'cotizacion_mueble': mueble.id,
                             'contenedor': item.id,
                             'nombre_contenedor': item.contenedor,
                             'cantidad': 1
                             })

            formset = self.form_class_formset(initial=data)
        else:
            formset = self.form_class_formset()

        return render(request, self.template_name, {'formset': formset, 'mueble': mueble})

    def post(self, request, *args, **kwargs):
        formset = self.form_class_formset(request.POST)
        if formset.is_valid():
            mueble = self.request.GET.get('mueble')

            existecontenedor = ContenedorMueble.objects.filter(cotizacion_mueble=
                                                               mueble)
            if existecontenedor:
                ContenedorMueble.objects.filter(cotizacion_mueble=
                                                mueble).delete()
            for form in formset.forms:
                if form.cleaned_data.get('ch_contenedor'):

                    add_contenedormueble(str(form.cleaned_data['cotizacion_mueble'].id),
                                         str(form.cleaned_data['contenedor'].id),
                                         str(form.cleaned_data['tipo_de_contenido'].id),
                                         form.cleaned_data['nombre_contenedor'],
                                         form.cleaned_data['cantidad'])
                #form.save()

            # <process form cleaned data>
            messages.success(self.request, "Registro guardado.")
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('ucotizacionesweb:edit_cotizacionmueble',
                                            args=(mueble,)))

        return render(request, self.template_name, {'formset': formset})


class ContenedorMuebleDelete(DeleteView):
    model = ContenedorMueble
    form_class = ContenedorMuebleForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            messages.success(self.request, "contenedor '" + str(self.obj) + "'  eliminado con éxito.")
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


#servicio mueble
class ServicioMuebleView(View):
    form_class_formset = formset_factory(ServicioMuebleForm,
                                         extra=Servicio.objects.exclude(servicio='(TRA) Traslado'
                                                                        ).exclude(servicio='(MU) Mudanza').count(),
                                         max_num=Servicio.objects.exclude(servicio='(TRA) Traslado'
                                                                          ).exclude(servicio='(MU) Mudanza').count())
    template_name = 'serviciomueble_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        mueble = CotizacionMueble.objects.get(id=self.request.GET.get('mueble'))
        serviciomueble = ServicioMueble.objects.filter(cotizacion_mueble=
                                                       mueble.id)
        serviciotipicopormueble = ServicioTipicoPorMueble.objects.filter(especificacion_de_mueble=
                                                                         mueble.especificacion_de_mueble.id
                                                                         ).exclude(servicio__in=serviciomueble.values('servicio'))
        servicios = Servicio.objects.exclude(id__in=serviciotipicopormueble.values('servicio')
                                             ).exclude(servicio='(TRA) Traslado'
                                                       ).exclude(servicio='(MU) Mudanza')
        data = []
        if serviciomueble:

            for item in serviciomueble:
                data.append({'cotizacion_mueble': mueble.id,
                             'servicio': item.servicio,
                             'descripcion_servicio': item.descripcion_servicio,
                             'ch_servicio': True
                             })
        if serviciotipicopormueble:

            for item in serviciotipicopormueble:
                data.append({'cotizacion_mueble': mueble.id,
                             'servicio': item.servicio,
                             'descripcion_servicio': item.servicio.servicio
                             })
        if servicios:

            for item in servicios:
                data.append({'cotizacion_mueble': mueble.id,
                             'servicio': item.id,
                             'descripcion_servicio': item.servicio
                             })
                servi = item.servicio

            formset = self.form_class_formset(initial=data)
        else:
            formset = self.form_class_formset()

        return render(request, self.template_name, {'formset': formset,
                                                    'mueble': mueble})

    def post(self, request, *args, **kwargs):
        formset = self.form_class_formset(request.POST)
        if formset.is_valid():
            mueble = CotizacionMueble.objects.get(id=self.request.GET.get('mueble'))

            contenedoremueble = ContenedorMueble.objects.filter(cotizacion_mueble=mueble.id)
            qcontenedorn = 0
            qcontenedorf = 0
            for cont in contenedoremueble:
                if (cont.tipo_de_contenido.nombre == 'objetos frágiles' or cont.tipo_de_contenido.nombre == 'textiles'):
                    qcontenedorf = qcontenedorf + cont.cantidad
                else:
                    qcontenedorn = qcontenedorn + cont.cantidad

            existeservicio = ServicioMueble.objects.filter(cotizacion_mueble=
                                                           mueble.id)
            if existeservicio:
                ServicioMueble.objects.filter(cotizacion_mueble=
                                              mueble.id).delete()
            for form in formset.forms:
                if form.cleaned_data.get('ch_servicio'):

                    cantidadservicio = servicio_cantidad(form.cleaned_data['descripcion_servicio'],
                                                         mueble.id, qcontenedorn, qcontenedorf,
                                                         mueble.volumen,
                                                         mueble.cotizacion_ambiente.direccion_origen.cantidad_pisos)

                    add_serviciomueble(str(form.cleaned_data['cotizacion_mueble'].id),
                                       str(form.cleaned_data['servicio'].id),
                                       form.cleaned_data['descripcion_servicio'],
                                       cantidadservicio['cantidadservicio'],
                                       cantidadservicio['descripcioncantidad'])
                #form.save()

            # <process form cleaned data>
            messages.success(self.request, "Registro guardado.")
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('ucotizacionesweb:edit_cotizacionmueble',
                                            args=(mueble,)))

        return render(request, self.template_name, {'formset': formset})


class ServicioMuebleDelete(DeleteView):
    model = ServicioMueble
    form_class = ServicioMuebleForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            messages.success(self.request, "servicio '" + str(self.obj) + "'  eliminado con éxito.")
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app tipo de dirección
class TipoDireccionListView(ListView):
    model = TipoDireccion
    paginate_by = 10
    context_object_name = 'tiposdireccion'
    template_name = 'tipodireccion_lista.html'

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
        context = super(TipoDireccionListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['tipodireccion',
                                             'descripcion', ])
            lista_tipodireccion = TipoDireccion.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipodireccion',
                                             'descripcion', ])
            lista_tipodireccion = TipoDireccion.objects.filter(entry_query)
        elif order_by:
            lista_tipodireccion = TipoDireccion.objects.all().order_by(order_by)
        else:
            lista_tipodireccion = TipoDireccion.objects.all()

        paginator = Paginator(lista_tipodireccion, 10)
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
            entry_query = get_query(search, ['tipodireccion',
                                             'descripcion', ])
            queryset = TipoDireccion.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['tipodireccion',
                                             'descripcion', ])
            queryset = TipoDireccion.objects.filter(entry_query)
        elif order_by:
            queryset = TipoDireccion.objects.all().order_by(order_by)
        else:
            queryset = TipoDireccion.objects.all()

        return queryset


class TipoDireccionView(View):
    form_class = TipoDireccionForm
    template_name = 'tipodireccion_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Tipo dirección '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('ucotizacionesweb:edit_tipodireccion',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Tipo direccion '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('ucotizacionesweb:list_tipodireccion'))

        return render(request, self.template_name, {'form': form})


class TipoDireccionUpdate(UpdateView):
    template_name = 'tipodireccion_edit.html'
    form_class = TipoDireccionForm
    model = TipoDireccion

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TipoDireccionUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        tipodireccion = TipoDireccion.objects.get(pk=self.object.pk)
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
            lista_tipodireccion = TipoDireccion.objects.all().order_by(order_by)
        else:
            lista_tipodireccion = TipoDireccion.objects.all()

        paginator = Paginator(lista_tipodireccion, nropag)
        # Show 25 contacts per page

        if page == '0':
            tiposdireccion = lista_tipodireccion
        else:
            try:
                tiposdireccion = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                tiposdireccion = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                tiposdireccion = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(tiposdireccion.object_list[i].id == tipodireccion.id):
                    if tiposdireccion.has_previous:
                        try:
                            previousitem = tiposdireccion.object_list[i-1].id
                        except:
                            previousitem = None

                    if tiposdireccion.has_next:
                        try:
                            nextitem = tiposdireccion.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(tiposdireccion)
            for i in range(0, countitem):
                if(tiposdireccion[i].id == tipodireccion.id):
                    try:
                        previousitem = tiposdireccion[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = tiposdireccion[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            tipodireccion_previous = TipoDireccion.objects.get(pk=previousitem)
        except:
            tipodireccion_previous = None
        try:
            tipodireccion_next = TipoDireccion.objects.get(pk=nextitem)
        except:
            tipodireccion_next = None

        context['tipodireccion_previous'] = tipodireccion_previous
        context['tipodireccion_next'] = tipodireccion_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Tipo dirección " + str(self.object) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Tipo dirección '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                messages.success(self.request, "Tipo dirección '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(reverse('ucotizacionesweb:list_tipodireccion'))
                #return render_to_response(self.template_name, self.get_context_data())


class TipoDireccionDelete(DeleteView):
    model = TipoDireccion
    form_class = TipoDireccionForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            messages.success(self.request, "Tipo dirección '" + str(self.obj) + "'  eliminado con éxito.")
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app concepto de cotización
class ConceptoDeCotizacionListView(ListView):
    model = ConceptoDeCotizacion
    paginate_by = 10
    context_object_name = 'conceptosdecotizacion'
    template_name = 'conceptodecotizacion_lista.html'

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
        context = super(ConceptoDeCotizacionListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['concepto',
                                             'descripcion', ])
            lista_conceptodecotizacion = ConceptoDeCotizacion.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['concepto',
                                             'descripcion', ])
            lista_conceptodecotizacion = ConceptoDeCotizacion.objects.filter(entry_query)
        elif order_by:
            lista_conceptodecotizacion = ConceptoDeCotizacion.objects.all().order_by(order_by)
        else:
            lista_conceptodecotizacion = ConceptoDeCotizacion.objects.all()

        paginator = Paginator(lista_conceptodecotizacion, 10)
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
            entry_query = get_query(search, ['concepto',
                                             'descripcion', ])
            queryset = ConceptoDeCotizacion.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['concepto',
                                             'descripcion', ])
            queryset = ConceptoDeCotizacion.objects.filter(entry_query)
        elif order_by:
            queryset = ConceptoDeCotizacion.objects.all().order_by(order_by)
        else:
            queryset = ConceptoDeCotizacion.objects.all()

        return queryset


class ConceptoDeCotizacionView(View):
    form_class = ConceptoDeCotizacionForm
    template_name = 'conceptodecotizacion_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Concepto '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('ucotizacionesweb:edit_conceptodecotizacion',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Concepto '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('ucotizacionesweb:list_conceptodecotizacion'))

        return render(request, self.template_name, {'form': form})


class ConceptoDeCotizacionUpdate(UpdateView):
    template_name = 'conceptodecotizacion_edit.html'
    form_class = ConceptoDeCotizacionForm
    model = ConceptoDeCotizacion

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ConceptoDeCotizacionUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        conceptodecotizacion = ConceptoDeCotizacion.objects.get(pk=self.object.pk)
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
            lista_conceptodecotizacion = ConceptoDeCotizacion.objects.all().order_by(order_by)
        else:
            lista_conceptodecotizacion = ConceptoDeCotizacion.objects.all()

        paginator = Paginator(lista_conceptodecotizacion, nropag)
        # Show 25 contacts per page

        if page == '0':
            conceptosdecotizacion = lista_conceptodecotizacion
        else:
            try:
                conceptosdecotizacion = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                conceptosdecotizacion = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                conceptosdecotizacion = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(conceptosdecotizacion.object_list[i].id == conceptodecotizacion.id):
                    if conceptosdecotizacion.has_previous:
                        try:
                            previousitem = conceptosdecotizacion.object_list[i-1].id
                        except:
                            previousitem = None

                    if conceptosdecotizacion.has_next:
                        try:
                            nextitem = conceptosdecotizacion.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(conceptosdecotizacion)
            for i in range(0, countitem):
                if(conceptosdecotizacion[i].id == conceptodecotizacion.id):
                    try:
                        previousitem = conceptosdecotizacion[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = conceptosdecotizacion[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            conceptodecotizacion_previous = ConceptoDeCotizacion.objects.get(pk=previousitem)
        except:
            conceptodecotizacion_previous = None
        try:
            conceptodecotizacion_next = ConceptoDeCotizacion.objects.get(pk=nextitem)
        except:
            conceptodecotizacion_next = None

        context['conceptodecotizacion_previous'] = conceptodecotizacion_previous
        context['conceptodecotizacion_next'] = conceptodecotizacion_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Concepto " + str(self.object) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Concepto '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                messages.success(self.request, "Concepto '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(reverse('ucotizacionesweb:list_conceptodecotizacion'))
                #return render_to_response(self.template_name, self.get_context_data())


class ConceptoDeCotizacionDelete(DeleteView):
    model = ConceptoDeCotizacion
    form_class = ConceptoDeCotizacionForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            messages.success(self.request, "Concepto '" + str(self.obj) + "'  eliminado con éxito.")
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


# app fecha de cotización
class FechaDeCotizacionListView(ListView):
    model = FechaDeCotizacion
    paginate_by = 10
    context_object_name = 'fechasdecotizacion'
    template_name = 'fechadecotizacion_lista.html'

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
        context = super(FechaDeCotizacionListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['nombre_fecha', ])
            lista_fechadecotizacion = FechaDeCotizacion.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['nombre_fecha', ])
            lista_fechadecotizacion = FechaDeCotizacion.objects.filter(entry_query)
        elif order_by:
            lista_fechadecotizacion = FechaDeCotizacion.objects.all().order_by(order_by)
        else:
            lista_fechadecotizacion = FechaDeCotizacion.objects.all()

        paginator = Paginator(lista_fechadecotizacion, 10)
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
            entry_query = get_query(search, ['nombre_fecha', ])
            queryset = FechaDeCotizacion.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['nombre_fecha', ])
            queryset = FechaDeCotizacion.objects.filter(entry_query)
        elif order_by:
            queryset = FechaDeCotizacion.objects.all().order_by(order_by)
        else:
            queryset = FechaDeCotizacion.objects.all()

        return queryset


class FechaDeCotizacionView(View):
    form_class = FechaDeCotizacionForm
    template_name = 'fechadecotizacion_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Fecha '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('ucotizacionesweb:edit_fechadecotizacion',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Fecha '" + str(id_reg) + "'  registrado con éxito.")
                return HttpResponseRedirect(reverse('ucotizacionesweb:list_fechadecotizacion'))

        return render(request, self.template_name, {'form': form})


class FechaDeCotizacionUpdate(UpdateView):
    template_name = 'fechadecotizacion_edit.html'
    form_class = FechaDeCotizacionForm
    model = FechaDeCotizacion

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FechaDeCotizacionUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        fechadecotizacion = FechaDeCotizacion.objects.get(pk=self.object.pk)
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
            lista_fechadecotizacion = FechaDeCotizacion.objects.all().order_by(order_by)
        else:
            lista_fechadecotizacion = FechaDeCotizacion.objects.all()

        paginator = Paginator(lista_fechadecotizacion, nropag)
        # Show 25 contacts per page

        if page == '0':
            fechasdecotizacion = lista_fechadecotizacion
        else:
            try:
                fechasdecotizacion = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                fechasdecotizacion = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                fechasdecotizacion = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(fechasdecotizacion.object_list[i].id == fechadecotizacion.id):
                    if fechasdecotizacion.has_previous:
                        try:
                            previousitem = fechasdecotizacion.object_list[i-1].id
                        except:
                            previousitem = None

                    if fechasdecotizacion.has_next:
                        try:
                            nextitem = fechasdecotizacion.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(fechasdecotizacion)
            for i in range(0, countitem):
                if(fechasdecotizacion[i].id == fechadecotizacion.id):
                    try:
                        previousitem = fechasdecotizacion[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = fechasdecotizacion[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            fechadecotizacion_previous = FechaDeCotizacion.objects.get(pk=previousitem)
        except:
            fechadecotizacion_previous = None
        try:
            fechadecotizacion_next = FechaDeCotizacion.objects.get(pk=nextitem)
        except:
            fechadecotizacion_next = None

        context['fechadecotizacion_previous'] = fechadecotizacion_previous
        context['fechadecotizacion_next'] = fechadecotizacion_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Fecha " + str(self.object) + "  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Fecha '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                messages.success(self.request, "Fecha '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(reverse('ucotizacionesweb:list_fechadecotizacion'))
                #return render_to_response(self.template_name, self.get_context_data())


class FechaDeCotizacionDelete(DeleteView):
    model = FechaDeCotizacion
    form_class = FechaDeCotizacionForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        self.obj.delete()

        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            messages.success(self.request, "Fecha '" + str(self.obj) + "'  eliminado con éxito.")
            return HttpResponseRedirect(redirect_to)
        else:
            return render_to_response(self.template_name, self.get_context_data())


class CotizacionBitacoraView(View):
    form_class = CotizacionBitacoraForm
    template_name = 'bitacoracotizacion_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        cotizacion = self.request.REQUEST.get('cotizacion', '')
        origen = self.request.REQUEST.get('origen', '')
        data = {'origen_de_registro': origen,
                'cotizacion': cotizacion,
                'usuario_registro': 2
                }
        form = self.form_class(initial=data)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            messages.success(self.request, "Bitácora '" + str(id_reg) + "'  registrado con éxito.")
            cotizacion = self.request.REQUEST.get('cotizacion', '')
            redirect_to = self.request.REQUEST.get('next', '')
            if cotizacion:
                return HttpResponseRedirect(reverse('ucotizacionesweb:ficha_cotizacion',
                                                    args=(cotizacion,)))
            else:
                if redirect_to:
                    return HttpResponseRedirect(redirect_to)
                else:
                    return render_to_response(self.template_name, self.get_context_data())

        return render(request, self.template_name, {'form': form})


#funciones de carga de datos internas
def add_cotizacion(cliente):

    cliente = Cliente.objects.get(pk=cliente)

    agregarcotizacion = Cotizacion.objects.create(cliente_id=cliente.id,
                                                  nombre_cliente=cliente.nombre)
    agregarcotizacion.save()

    estadoactual = EstadoDeRegistro.objects.filter(model='cotizacion',
                                                   estado__estado='Activo')

    agregarestadoderegistro = CotizacionEstado.objects.create(cotizacion_id=agregarcotizacion.id,
                                                              estado_de_registro_id=estadoactual[0].id,
                                                              usuario_registro_id=2,
                                                              observacion='Creación de la cotización',
                                                              predefinido=True)
    agregarestadoderegistro.save()

    estadoactual = EstadoDeDocumento.objects.filter(tipo_de_documento__tipo_de_documento='cotizacion',
                                                    orden=1)

    agregarestadodedocumento = CotizacionEstado.objects.create(cotizacion_id=agregarcotizacion.id,
                                                               estado_de_documento_id=estadoactual[0].id,
                                                               usuario_registro_id=2,
                                                               observacion='cargando datos básicos de la cotización',
                                                               predefinido=True)
    agregarestadodedocumento.save()

    return(agregarcotizacion.id)


def add_cotizacion_direccion(cotizacion, clientedireccion, tipo):

    clientedireccion = ClienteDireccion.objects.get(pk=clientedireccion)
    tipodireccion = TipoDireccion.objects.filter(tipo_direccion=tipo)
    orden = CotizacionDireccion.objects.filter(cotizacion=cotizacion,
                                               tipo_direccion=tipodireccion[0].id).count()

    agregarcotizaciondireccion = CotizacionDireccion.objects.create(cotizacion_id=cotizacion,
                                                                    clientedireccion_id=clientedireccion.id,
                                                                    tipo_direccion_id=tipodireccion[0].id,
                                                                    direccion=clientedireccion.detalle_de_direccion,
                                                                    orden=orden+1)
    agregarcotizaciondireccion.save()

    bitacora = CotizacionBitacora.objects.create(cotizacion_id=cotizacion,
                                                 usuario_registro_id=2,
                                                 origen_de_registro='A',
                                                 observacion='Creación de una dirección de la cotización')
    bitacora.save()

    cantOrig = CotizacionDireccion.objects.filter(cotizacion=cotizacion,
                                                  tipo_direccion__tipo_direccion='Origen').count()
    cantDest = CotizacionDireccion.objects.filter(cotizacion=cotizacion,
                                                  tipo_direccion__tipo_direccion='Destino').count()
    estado_documento = CotizacionEstado.objects.filter(cotizacion=cotizacion,
                                                       predefinido=True).exclude(estado_de_documento=None)
    if estado_documento:
        estadodedocumento = estado_documento[0].estado_de_documento.orden

    if cantOrig > 0 and cantDest > 0 and estadodedocumento == 1:
        add_cotizacion_detalle(cotizacion, agregarcotizaciondireccion.id, tipo)
        updateestado = CotizacionEstado.objects.filter(cotizacion=cotizacion,
                                                       predefinido=True).exclude(estado_de_documento=None)
        updateestado.update(predefinido=False)

        estadoactual = EstadoDeDocumento.objects.filter(tipo_de_documento__tipo_de_documento='cotizacion',
                                                        orden=2)

        agregarestadodedocumento = CotizacionEstado.objects.create(cotizacion_id=cotizacion,
                                                                   estado_de_documento_id=estadoactual[0].id,
                                                                   usuario_registro_id=2,
                                                                   observacion='Cotización lista para cotizar',
                                                                   predefinido=True)
        agregarestadodedocumento.save()

    return(agregarcotizaciondireccion.id)


def update_cotizacion_direccion(cotizacion, clientedireccion):

    cotizacion_direccion = CotizacionDireccion.objects.filter(cotizacion=cotizacion,
                                                              clientedireccion=clientedireccion)
    clientedireccion = ClienteDireccion.objects.get(pk=clientedireccion)

    nombre_de_edificio = ''
    tipo_de_edificacion = ''
    rampa = False
    distancia_del_vehiculo = 0
    cantidad_pisos = 0
    escalera_estrecha = False
    escalera_inclinada = False
    escalon_grande = False
    especificacion_de_inmueble = ''
    numero_de_inmueble = ''
    numero_de_pisos = 0
    nombre_piso = ''
    cantidad_de_ambientes = 0
    pisos_por_escalera = 0
    numero_de_plantas = 0
    total_m2 = 0
    baulera = False
    volumen_baulera = 0

    if clientedireccion.edificacion:
        edificacion = Edificacion.objects.filter(pk=clientedireccion.edificacion.id)

        nombre_de_edificio = edificacion[0].nombre_de_edificio
        tipo_de_edificacion = edificacion[0].tipo_de_edificacion.tipo_de_edificacion
        rampa = edificacion[0].rampa
        cantidad_pisos = edificacion[0].cantidad_de_pisos
        distancia_del_vehiculo = edificacion[0].distancia_del_vehiculo
        escalera_estrecha = edificacion[0].escalera_estrecha
        escalera_inclinada = edificacion[0].escalera_inclinada
        escalon_grande = edificacion[0].escalon_grande

    if clientedireccion.inmueble:
        inmueble = Inmueble.objects.filter(pk=clientedireccion.inmueble.id)

        especificacion_de_inmueble = inmueble[0].especificacion_de_inmueble.especificacion_de_inmueble
        numero_de_inmueble = inmueble[0].numero_de_inmueble
        numero_de_pisos = inmueble[0].numero_de_pisos
        nombre_piso = inmueble[0].nombre_del_piso
        cantidad_de_ambientes = inmueble[0].cantidad_de_ambientes
        pisos_por_escalera = inmueble[0].pisos_por_escalera
        numero_de_plantas = inmueble[0].numero_de_plantas
        total_m2 = inmueble[0].total_m2
        baulera = inmueble[0].baulera
        volumen_baulera = inmueble[0].volumen_baulera

    cotizacion_direccion.update(direccion=clientedireccion.detalle_de_direccion,
                                nombre_de_edificio=nombre_de_edificio,
                                tipo_de_edificacion=tipo_de_edificacion,
                                rampa=rampa,
                                distancia_del_vehiculo=distancia_del_vehiculo,
                                cantidad_pisos=cantidad_pisos,
                                escalera_estrecha=escalera_estrecha,
                                escalera_inclinada=escalera_inclinada,
                                escalon_grande=escalon_grande,
                                especificacion_de_inmueble=especificacion_de_inmueble,
                                numero_de_inmueble=numero_de_inmueble,
                                numero_de_pisos=numero_de_pisos,
                                nombre_piso=nombre_piso,
                                cantidad_de_ambientes=cantidad_de_ambientes,
                                pisos_por_escalera=pisos_por_escalera,
                                numero_de_plantas=numero_de_plantas,
                                total_m2=total_m2,
                                baulera=baulera,
                                volumen_baulera=volumen_baulera)

    cantOrig = CotizacionDireccion.objects.filter(cotizacion=cotizacion,
                                                  tipo_direccion__tipo_direccion='Origen').count()
    cantDest = CotizacionDireccion.objects.filter(cotizacion=cotizacion,
                                                  tipo_direccion__tipo_direccion='Destino').count()
    estado_documento = CotizacionEstado.objects.filter(cotizacion=cotizacion,
                                                       predefinido=True).exclude(estado_de_documento=None)
    cantAmbiente = CotizacionAmbiente.objects.filter(direccion_origen__cotizacion=cotizacion).count()

    if estado_documento:
        estadodedocumento = estado_documento[0].estado_de_documento.orden

    if cantOrig > 0 and cantDest > 0 and estadodedocumento == 1 and cantAmbiente == 0:
        direccion_origen = CotizacionDireccion.objects.filter(cotizacion=cotizacion,
                                                              tipo_direccion__tipo_direccion='Origen',
                                                              orden='1')
        add_cotizacion_detalle(cotizacion,
                               direccion_origen[0].id,
                               cotizacion_direccion[0].tipo_direccion.tipo_direccion)

        updateestado = CotizacionEstado.objects.filter(cotizacion=cotizacion,
                                                       predefinido=True).exclude(estado_de_documento=None)
        updateestado.update(predefinido=False)

        estadoactual = EstadoDeDocumento.objects.filter(tipo_de_documento__tipo_de_documento='cotizacion',
                                                        orden=2)

        agregarestadodedocumento = CotizacionEstado.objects.create(cotizacion_id=cotizacion,
                                                                   estado_de_documento_id=estadoactual[0].id,
                                                                   usuario_registro_id=2,
                                                                   observacion='Cotización lista para cotizar',
                                                                   predefinido=True)
        agregarestadodedocumento.save()
    elif cantOrig > 0 and cantDest > 0 and cotizacion_direccion[0].tipo_direccion.tipo_direccion == 'Origen':
        cotizacionambiente = CotizacionAmbiente.objects.filter(direccion_origen=cotizacion_direccion[0].id).count()
        if cotizacionambiente <= 0:
            add_cotizacion_detalle(cotizacion,
                                   cotizacion_direccion[0].id,
                                   cotizacion_direccion[0].tipo_direccion.tipo_direccion)

    return(cotizacion_direccion[0].id)


def add_cotizacion_detalle(cotizacion, direccionorigen, tipo):

    if tipo == 'Origen':
        direccion_origen = CotizacionDireccion.objects.filter(id=direccionorigen)
    else:
        direccion_origen = CotizacionDireccion.objects.filter(cotizacion=cotizacion,
                                                              tipo_direccion__tipo_direccion='Origen',
                                                              orden='1')

    direccion_destino = CotizacionDireccion.objects.filter(cotizacion=cotizacion,
                                                           tipo_direccion__tipo_direccion='Destino',
                                                           orden='1')

    ambientes = AmbientePorTipoDeInmueble.objects.filter(predeterminado=True,
                                                         especificacion_de_inmueble__especificacion_de_inmueble=direccion_origen[0].especificacion_de_inmueble)
    if ambientes:
        for ambiente in ambientes:
            agregarambiente = add_cotizacionambiente(direccion_origen[0].id,
                                                     ambiente.ambiente.id,
                                                     ambiente.ambiente.ambiente,
                                                     'Creado por inteligencia de negocio')

            muebles = MueblePorAmbiente.objects.filter(predefinido=True,
                                                       ambiente_por_tipo_de_inmueble=ambiente.id)
            if muebles:
                for mueble in muebles:
                    agregarmueble = add_cotizacionmueble(agregarambiente,
                                                         mueble.especificacion_de_mueble.id,
                                                         direccion_destino[0].id,
                                                         mueble.especificacion_de_mueble.especificacion_de_mueble,
                                                         mueble.especificacion_de_mueble.ancho,
                                                         mueble.especificacion_de_mueble.alto,
                                                         mueble.especificacion_de_mueble.largo, 1,
                                                         mueble.especificacion_de_mueble.volumen_en_camion,
                                                         mueble.especificacion_de_mueble.mueble.trasladable,
                                                         'Creado por inteligencia de negocio')

                    contenedores = ContenedorTipicoPorMueble.objects.filter(especificacion_de_mueble=mueble.especificacion_de_mueble.id)
                    for contenedor in contenedores:
                        add_contenedormueble(agregarmueble,
                                             contenedor.contenedor.id,
                                             contenedor.tipo_de_contenido.id,
                                             contenedor.contenedor.contenedor,
                                             contenedor.cantidad)

                    contenedoremueble = ContenedorMueble.objects.filter(cotizacion_mueble=agregarmueble)
                    qcontenedorn = 0
                    qcontenedorf = 0
                    for cont in contenedoremueble:
                        if (cont.tipo_de_contenido.nombre == 'objetos frágiles' or cont.tipo_de_contenido.nombre == 'textiles'):
                            qcontenedorf = qcontenedorf + cont.cantidad
                        else:
                            qcontenedorn = qcontenedorn + cont.cantidad

                    servicios = ServicioTipicoPorMueble.objects.filter(predefinido=True,
                                                                       especificacion_de_mueble=mueble.especificacion_de_mueble.id)
                    for servicio in servicios:
                        cantidadservicio = servicio_cantidad(servicio.servicio.servicio,
                                                             1, qcontenedorn, qcontenedorf,
                                                             mueble.especificacion_de_mueble.volumen_de_mueble,
                                                             direccion_origen[0].cantidad_pisos)

                        add_serviciomueble(agregarmueble, servicio.servicio.id,
                                           servicio.servicio.servicio,
                                           cantidadservicio['cantidadservicio'],
                                           cantidadservicio['descripcioncantidad'])

        bitacora = CotizacionBitacora.objects.create(cotizacion_id=cotizacion,
                                                     usuario_registro_id=2,
                                                     origen_de_registro='A',
                                                     observacion='Creación de ambientes y muebles propuestos')
        bitacora.save()

    return(cotizacion)


def add_cotizacionambiente(direccionorigen, ambiente, nombreambiente, observaciones):
    agregarambiente = CotizacionAmbiente.objects.create(direccion_origen_id=direccionorigen,
                                                        ambiente_id=ambiente,
                                                        nombre=nombreambiente,
                                                        observaciones=observaciones)
    agregarambiente.save()
    return(agregarambiente.id)


def add_cotizacionmueble(cotizacionambiente, especificaciondemueble,
                         direcciondestino, nombreespecificaciondemueble,
                         ancho, alto, largo, cantidad, volumenencamion,
                         trasladable, observaciones):
    agregarmueble = CotizacionMueble.objects.create(cotizacion_ambiente_id=cotizacionambiente,
                                                    especificacion_de_mueble_id=especificaciondemueble,
                                                    direccion_destino_id=direcciondestino,
                                                    nombre_especificacion_de_mueble=nombreespecificaciondemueble,
                                                    ancho=ancho,
                                                    alto=alto,
                                                    largo=largo,
                                                    cantidad=cantidad,
                                                    volumen_en_camion=volumenencamion,
                                                    trasladable=trasladable,
                                                    observaciones=observaciones)
    agregarmueble.save()
    return(agregarmueble.id)


def add_contenedormueble(cotizacionmueble, contenedor, tipodecontenido,
                         nombrecontenedor, cantidad):

    agregarcontenedor = ContenedorMueble.objects.create(cotizacion_mueble_id=cotizacionmueble,
                                                        contenedor_id=contenedor,
                                                        tipo_de_contenido_id=tipodecontenido,
                                                        nombre_contenedor=nombrecontenedor,
                                                        cantidad=cantidad)
    agregarcontenedor.save()
    return(agregarcontenedor)


def add_serviciomueble(cotizacionmueble, servicio, descripcionservicio,
                       cantidad, descripcioncantidad):
    agregarservicio = ServicioMueble.objects.create(cotizacion_mueble_id=cotizacionmueble,
                                                    servicio_id=servicio,
                                                    descripcion_servicio=descripcionservicio,
                                                    cantidad=cantidad,
                                                    descripcion_cantidad=descripcioncantidad)
    agregarservicio.save()
    return(agregarservicio)


def edit_contenedormueble(idcontenedormueble, tipodecontenido, cantidad):

    updatecontenedor = ContenedorMueble.objects.filter(id=idcontenedormueble)
    updatecontenedor.update(tipo_de_contenido_id=tipodecontenido,
                            cantidad=cantidad)
    return(updatecontenedor)


def edit_serviciomueble(idserviciomueble, cantidad, descripcioncantidad):
    updateservicio = ServicioMueble.objects.filter(id=idserviciomueble)
    updateservicio.update(descripcion_cantidad=descripcioncantidad,
                          cantidad=cantidad)
    return(updateservicio)


#cambiar estado de documento de la cotización
def CotizacionEstadoDeDocumento(request, pk):
    estadoorden = request.GET['estado_orden']

    updateestado = CotizacionEstado.objects.filter(cotizacion=pk,
                                                   predefinido=True).exclude(estado_de_documento=None)
    updateestado.update(predefinido=False)

    estadoactual = EstadoDeDocumento.objects.filter(tipo_de_documento__tipo_de_documento='cotizacion',
                                                    orden=estadoorden)
    agregarestado = CotizacionEstado.objects.create(cotizacion_id=pk,
                                                    estado_de_documento_id=estadoactual[0].id,
                                                    usuario_registro_id=2,
                                                    observacion='Cotización iniciada',
                                                    predefinido=True)
    agregarestado.save()

    messages.success(request, "Registro guardado.")
    return HttpResponseRedirect(reverse('ucotizacionesweb:ficha_cotizacion',
                                args=(pk,)))


# funciones de cálculo
#cantidad de servicios aplicados a muebles
def servicio_armar(cantidadmueble):
    cantidad = cantidadmueble/2
    cantidadservicio = redondeo(cantidad, 1)
    return(cantidadservicio)


def servicio_desarmar(cantidadmueble):
    cantidad = cantidadmueble/4
    cantidadservicio = redondeo(cantidad, 1)
    return(cantidadservicio)


def servicio_embalajecontenido(qcontenedorn, qcontenedorf):
    cantidadservicio = redondeo((qcontenedorn/10), 1) + redondeo((qcontenedorf/5), 1)
    return(cantidadservicio)


def servicio_embalajepremiumdemuebles(volmueble):
    cantidad = volmueble/5
    cantidadservicio = redondeo(cantidad, 1)
    return(cantidadservicio)


def servicio_piano(volmueble):
    cantidadservicio = redondeo(volmueble, 0.10)
    return(cantidadservicio)


def servicio_soga(cantidad):
    cantidadservicio = cantidad
    return(cantidadservicio)


def servicio_cantidad(servicio, cantidadmueble,
                      qcontenedorn, qcontenedorf,
                      volumenmueble, cantidaddepiso):
    cantidadservicio = 0
    descripcioncantidad = ''
    if servicio == '(AR) Armar':
        cantidadservicio = servicio_armar(cantidadmueble)
        descripcioncantidad = str(cantidadmueble) + ' muebles / 2 muebles por hora'
    elif servicio == '(DE) Desarmar':
        cantidadservicio = servicio_desarmar(cantidadmueble)
        descripcioncantidad = str(cantidadmueble) + ' muebles / 4 muebles x hora'
    elif servicio == '(DC) Desembalaje de contenidos':
        cantidadservicio = servicio_embalajecontenido(qcontenedorn,
                                                      qcontenedorf)
        descripcioncantidad = str(qcontenedorn) + \
                              ' contenedores con contenido normal' + \
                              ' / 10 contenedores por hora + ' + \
                              str(qcontenedorf) + \
                              ' contenedores con contenido frágil o textil / ' + \
                              '5 contenedores por hora'
    elif servicio == '(EC) Embalaje de contenidos':
        cantidadservicio = servicio_embalajecontenido(qcontenedorn,
                                                      qcontenedorf)
        descripcioncantidad = str(qcontenedorn) + \
                              ' contenedores con contenido normal' + \
                              ' / 10 contenedores por hora + ' + \
                              str(qcontenedorf) + \
                              ' contenedores con contenido frágil o textil / ' + \
                              '5 contenedores por hora'
    elif servicio == '(EP) Embalaje premium de muebles':
        cantidadservicio = servicio_embalajepremiumdemuebles(volumenmueble)
        descripcioncantidad = str(volumenmueble) + ' m3 de mueble / 5 m3 por hora'
    elif servicio == '(DP) Desembalaje premium de mueble':
        cantidadservicio = servicio_embalajepremiumdemuebles(volumenmueble)
        descripcioncantidad = str(volumenmueble) + ' m3 de mueble / 5 m3 por hora'
    elif servicio == '(PI) Piano':
        cantidadservicio = servicio_piano(volumenmueble)
        descripcioncantidad = str(volumenmueble) + ' Toneladas'
    elif servicio == '(CF) Caja fuerte':
        cantidadservicio = servicio_piano(volumenmueble)
        descripcioncantidad = str(volumenmueble) + ' Toneladas'
    elif servicio == '(SO) Trabajo de soga':
        cantmueble = cantidadmueble + cantidaddepiso
        cantidadservicio = servicio_soga(cantmueble)
        descripcioncantidad = str(cantmueble) + ' muebles/pisos'

    data = {'cantidadservicio': cantidadservicio,
            'descripcioncantidad': descripcioncantidad
            }

    return(data)


#cantidad de servicios aplicados a la cotización
def mudanza(cotizacion):

    muebles = CotizacionMueble.objects.filter(cotizacion_ambiente__direccion_origen__cotizacion=
                                              cotizacion)
    contenedores = ContenedorMueble.objects.filter(cotizacion_mueble__cotizacion_ambiente__direccion_origen__cotizacion=
                                                   cotizacion)
    vm = 0
    vc = 0
    for mueble in muebles:
        vm = vm + (mueble.volumen_en_camion*mueble.cantidad)

    for contenedor in contenedores:
        vc = vc + contenedor.volumen_total_en_camion

    cantidad = vm + vc
    cantidadservicio = redondeo(cantidad, 1)
    descripcioncantidad = vm + ' m3 de muebles + ' + vc + 'm3 de contenedores'

    data = {'cantidadservicio': cantidadservicio,
            'descripcioncantidad': descripcioncantidad
            }

    return(data)


def traslado(recorridokm, cantidaddegracia):
    if (recorridokm - cantidaddegracia) >= 0:
        cantidadservicio = recorridokm
    else:
        cantidadservicio = 0

    descripcioncantidad = cantidadservicio + ' total recorrido en km'
    data = {'cantidadservicio': cantidadservicio,
            'descripcioncantidad': descripcioncantidad
            }

    return(data)


def servivio_cotizacion(totalcantidadservicio, cantidaddegracia, Cotizacion, servicio):
    cantidad = ServicioMueble.objects.filter(cotizacion_mueble__cotizacion_ambiente__direccion_origen__cotizacion=
                                             Cotizacion, servicio=servicio
                                             ).values('servicio'
                                                      ).annotate(cantservicio=Sum('cantidad')
                                                                 ).order_by('servicio')
    if (totalcantidadservicio - cantidaddegracia) >= 0:
        cantidadservicio = totalcantidadservicio
    else:
        cantidadservicio = 0
    return (cantidadservicio)


#Monto de servicio aplicado a la cotización
def monto_servicio(preciobase, preciomarginal,
                   intervalo1, porcentaje1,
                   intervalo2, porcentaje2,
                   intervalo3, porcentaje3,
                   cantidadservicio):
    if (cantidadservicio - 1) >= 0:
        montomarginal = (cantidadservicio - 1) * preciomarginal
    else:
        montomarginal = 0
    montoint1 = (int(cantidadservicio/intervalo1)) * porcentaje1 * preciobase
    montoint2 = (int(cantidadservicio/intervalo2)) * porcentaje2 * preciobase
    montoint3 = (int(cantidadservicio/intervalo3)) * porcentaje3 * preciobase
    montoservicio = preciobase + montomarginal + montoint1 + montoint2 + montoint3
    return (montoservicio)


def monto_serviciosoga(preciobase, preciomarginal,
                       intervalo1, porcentaje1,
                       intervalo2, porcentaje2,
                       intervalo3, porcentaje3,
                       cantidad, piso):
    cantidadservicio = cantidad + piso
    if (cantidadservicio - 1) >= 0:
        montomarginal = (cantidadservicio - 1) * preciomarginal
    else:
        montomarginal = 0
    montoint1 = (int(cantidadservicio/intervalo1)) * porcentaje1 * preciobase
    montoint2 = (int(cantidadservicio/intervalo2)) * porcentaje2 * preciobase
    montoint3 = (int(cantidadservicio/intervalo3)) * porcentaje3 * preciobase
    montoservicio = preciobase + montomarginal + montoint1 + montoint2 + montoint3
    return (montoservicio)


def monto_serviciotraslado(preciobase, preciomarginal,
                           intervalo1, porcentaje1,
                           intervalo2, porcentaje2,
                           intervalo3, porcentaje3,
                           cantidadservicio):

    if (cantidadservicio - 25) >= 0:
        if (cantidadservicio - 1) >= 0:
            montomarginal = (cantidadservicio - 1) * preciomarginal
        else:
            montomarginal = 0
    else:
            montomarginal = 0

    montoint1 = (int(cantidadservicio/intervalo1)) * porcentaje1 * preciobase
    montoint2 = (int(cantidadservicio/intervalo2)) * porcentaje2 * preciobase
    montoint3 = (int(cantidadservicio/intervalo3)) * porcentaje3 * preciobase
    montoservicio = preciobase + montomarginal + montoint1 + montoint2 + montoint3
    return (montoservicio)


def redondeo(cantidad, redondear):
    """docstring"""
    #Parte entera con o sin signo
    entero = int(cantidad)
    #Parte decimal
    residuo = abs(cantidad) - abs(int(cantidad))
    if residuo == 0:
        residuof = 0
    else:
        if (residuo/redondear) > 1:
            cant1 = Decimal(round((residuo / redondear), 2))
            cant2 = cant1 % 1
            if cant2 > 0:
                resto = 1
            else:
                resto = 0
            cant3 = int(residuo/redondear)
            residuof = (cant3 + resto) * redondear
        else:
            residuof = redondear
    cantidad = entero + residuof
    return Decimal(round(cantidad, 2))
