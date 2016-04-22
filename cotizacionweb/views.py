"""
Docstring documentación pendiente

"""

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, View, UpdateView, \
    DeleteView, DetailView
from cotizacionweb.models import Cotizacion, CotizacionEstado,\
    CotizacionDireccion, TipoDireccion, CotizacionBitacora, \
    CotizacionAmbiente, CotizacionMueble, FechaDeCotizacion, \
    CotizacionHistoricoFecha, ServicioMueble, ContenedorMueble, \
    ConceptoDeCotizacion
from cotizacionweb.forms import CotizacionForm, TipoDireccionForm, \
    ConceptoDeCotizacionForm, FechaDeCotizacionForm, CotizacionBitacoraForm
from cliente.models import Cliente, InformacionDeContacto, ClienteDireccion
from estadoderegistro.models import EstadoDeRegistro
from gestiondedocumento.models import EstadoDeDocumento
from direccion.models import Edificacion, Inmueble
from django.views.generic.edit import FormMixin
from django.core.urlresolvers import reverse
from ambiente.models import AmbientePorTipoDeInmueble
from mueble.models import MueblePorAmbiente
from contenedor.models import ContenedorTipicoPorMueble
from servicio.models import ServicioTipicoPorMueble, ComplejidadServicio
from mtvmcotizacionv02.views import valor_Personalizacionvisual, get_query
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from decimal import Decimal
from django.db.models import Sum


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
        context['form'] = self.get_form()

        context['mudanza'] = mudanza(self.object.pk)
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
        add_cotizacion_detalle(cotizacion)

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
        add_cotizacion_detalle(cotizacion)

    return(cotizacion_direccion[0].id)


def add_cotizacion_detalle(cotizacion):

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

                    contenedores = ContenedorTipicoPorMueble.objects.filter(predefinido=True,
                                                                            especificacion_de_mueble=mueble.especificacion_de_mueble.id)
                    for contenedor in contenedores:
                        add_contenedormueble(agregarmueble,
                                             contenedor.contenedor.id,
                                             contenedor.tipo_de_contenido.id,
                                             contenedor.contenedor.contenedor,
                                             contenedor.cantidad)

                    servicios = ServicioTipicoPorMueble.objects.filter(predefinido=True,
                                                                       especificacion_de_mueble=mueble.especificacion_de_mueble.id)
                    for servicio in servicios:
                        complejidadservicio = ComplejidadServicio.objects.filter(servicio=servicio.servicio.id,
                                                                                 predefinido=True)
                        add_serviciomueble(agregarmueble, servicio.servicio.id,
                                           servicio.servicio.servicio,
                                           0, 'descripcion de cantidad')

        bitacora = CotizacionBitacora.objects.create(cotizacion_id=cotizacion,
                                                     usuario_registro_id=2,
                                                     origen_de_registro='A',
                                                     observacion='Creación de ambientes y muebles propuestos')
        bitacora.save()

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

    return(cotizacion)


def add_cotizacionambiente(direccionorigen, ambiente, observaciones):
    agregarambiente = CotizacionAmbiente.objects.create(direccion_origen_id=direccionorigen,
                                                        ambiente_id=ambiente,
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
        data = {
                'origen_de_registro': origen,
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
    return(cantidadservicio)


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
