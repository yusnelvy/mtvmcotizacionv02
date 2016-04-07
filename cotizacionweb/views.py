from django.shortcuts import render, render_to_response
from django.views.generic import DetailView
from cotizacionweb.models import Cotizacion, CotizacionEstado,\
    CotizacionDireccion, TipoDireccion, CotizacionBitacora, \
    CotizacionAmbiente, CotizacionMueble, FechaDeCotizacion, \
    CotizacionHistoricoFecha
from cotizacionweb.forms import CotizacionForm
from cliente.models import Cliente, InformacionDeContacto, ClienteDireccion
from estadoderegistro.models import EstadoDeRegistro
from gestiondedocumento.models import EstadoDeDocumento
from direccion.models import Edificacion, Inmueble
from django.views.generic.edit import FormMixin
from django.core.urlresolvers import reverse
from ambiente.models import AmbientePorTipoDeInmueble
from mueble.models import MueblePorAmbiente


# Create your views here.
# app cotización
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

        if form.cleaned_data['fecha_mudanza'] and form.cleaned_data['hora_mudanza']:
            mudanza = FechaDeCotizacion.objects.filter(nombre_fecha='Mudanza')
            if mudanza:
                agregarfecha = CotizacionHistoricoFecha.objects.create(cotizacion_id=self.object.pk,
                                                                       usuario_registro_id=2,
                                                                       tipo_fecha_id=mudanza[0].id,
                                                                       nombre_tipo_fecha=mudanza[0].nombre_fecha,
                                                                       fecha_actual=form.cleaned_data['fecha_mudanza'],
                                                                       hora_actual=form.cleaned_data['hora_mudanza'],
                                                                       observacion='Fecha de la mudanza',
                                                                       aplicar=True)
                agregarfecha.save()

        if form.cleaned_data['fecha_visita'] and form.cleaned_data['hora_visita']:
            visita = FechaDeCotizacion.objects.filter(nombre_fecha='Visita del cotizador')
            if visita:
                agregarfecha = CotizacionHistoricoFecha.objects.create(cotizacion_id=self.object.pk,
                                                                       usuario_registro_id=2,
                                                                       tipo_fecha_id=visita[0].id,
                                                                       nombre_tipo_fecha=visita[0].nombre_fecha,
                                                                       fecha_actual=form.cleaned_data['fecha_visita'],
                                                                       hora_actual=form.cleaned_data['hora_visita'],
                                                                       observacion='Fecha de la visita',
                                                                       aplicar=True)
                agregarfecha.save()

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
                                                    estado_de_documento='cargando')

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
                                                 observacion='Creación de una dirección de la cotización')
    bitacora.save()

    cantOrig = CotizacionDireccion.objects.filter(cotizacion=cotizacion,
                                                  tipo_direccion__tipo_direccion='Origen').count()
    cantDest = CotizacionDireccion.objects.filter(cotizacion=cotizacion,
                                                  tipo_direccion__tipo_direccion='Destino').count()
    estado_documento = CotizacionEstado.objects.filter(cotizacion=cotizacion,
                                                       predefinido=True).exclude(estado_de_documento=None)
    if estado_documento:
        estadodedocumento = estado_documento[0].estado_de_documento.estado_de_documento

    if cantOrig > 0 and cantDest > 0 and estadodedocumento == 'cargando':
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
            agregarambiente = CotizacionAmbiente.objects.create(direccion_origen_id=direccion_origen[0].id,
                                                                ambiente_id=ambiente.ambiente.id,
                                                                observaciones='Creado por inteligencia de negocio')
            agregarambiente.save()

            muebles = MueblePorAmbiente.objects.filter(predefinido=True,
                                                       ambiente_por_tipo_de_inmueble=ambiente.id)
            if muebles:
                for mueble in muebles:
                    agregarmueble = CotizacionMueble.objects.create(cotizacion_ambiente_id=agregarambiente.id,
                                                                    especificacion_de_mueble_id=mueble.especificacion_de_mueble.id,
                                                                    direccion_destino_id=direccion_destino[0].id,
                                                                    nombre_especificacion_de_mueble=mueble.especificacion_de_mueble.especificacion_de_mueble,
                                                                    ancho=mueble.especificacion_de_mueble.ancho,
                                                                    alto=mueble.especificacion_de_mueble.alto,
                                                                    largo=mueble.especificacion_de_mueble.largo,
                                                                    cantidad=1,
                                                                    volumen_en_camion=mueble.especificacion_de_mueble.volumen_en_camion,
                                                                    trasladable=mueble.especificacion_de_mueble.mueble.trasladable,
                                                                    observaciones='Creado por inteligencia de negocio')
                    agregarmueble.save()

    bitacora = CotizacionBitacora.objects.create(cotizacion_id=cotizacion,
                                                 usuario_registro_id=2,
                                                 observacion='Creación de ambientes y muebles propuestos')
    bitacora.save()

    updateestado = CotizacionEstado.objects.filter(cotizacion=cotizacion,
                                                   predefinido=True).exclude(estado_de_documento=None)
    updateestado.update(predefinido=False)

    estadoactual = EstadoDeDocumento.objects.filter(tipo_de_documento__tipo_de_documento='cotizacion',
                                                    estado_de_documento='por cotizar')

    agregarestadodedocumento = CotizacionEstado.objects.create(cotizacion_id=cotizacion,
                                                               estado_de_documento_id=estadoactual[0].id,
                                                               usuario_registro_id=2,
                                                               observacion='Cotización lista para cotizar',
                                                               predefinido=True)
    agregarestadodedocumento.save()

    return(cotizacion)
