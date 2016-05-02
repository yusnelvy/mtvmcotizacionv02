from django.shortcuts import render
from cliente.models import Cliente, TipoDeCliente
from django.contrib.auth.models import User
from rest_framework import viewsets
from direccion.models import Pais, Provincia, Ciudad, \
    Barrio, Calle, Direccion
from api.serializers import TipoDeClienteSerializer, \
    ClienteSerializer, PaisSerializer, ProvinciaSerializer, \
    CiudadSerializer, BarrioSerializer, CalleSerializer, \
    DireccionSerializer


# ViewSets define the view behavior.
class TipoDeClienteViewSet(viewsets.ModelViewSet):
    queryset = TipoDeCliente.objects.all()
    serializer_class = TipoDeClienteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer


class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer
    lookup_field = 'id'

    def get_queryset(self):
        query = self.request.query_params
        queryset = self.queryset
        if 'pais' in query.keys():
            queryset = queryset.filter(pais=Pais.objects.get(id=query.get('pais')))

        return queryset


class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer
    lookup_field = 'id'

    def get_queryset(self):
        query = self.request.query_params
        queryset = self.queryset
        if 'pais' in query.keys():
            queryset = queryset.filter(pais=Pais.objects.get(id=query.get('pais')))
        if 'provincia' in query.keys():
            queryset = queryset.filter(provincia=Provincia.objects.get(id=query.get('provincia')))

        return queryset


class BarrioViewSet(viewsets.ModelViewSet):
    queryset = Barrio.objects.all()
    serializer_class = BarrioSerializer
    lookup_field = 'id'

    def get_queryset(self):
        query = self.request.query_params
        queryset = self.queryset
        if 'pais' in query.keys():
            queryset = queryset.filter(pais=Pais.objects.get(id=query.get('pais')))
        if 'provincia' in query.keys():
            queryset = queryset.filter(provincia=Provincia.objects.get(id=query.get('provincia')))
        if 'ciudad' in query.keys():
            queryset = queryset.filter(ciudad=Ciudad.objects.get(id=query.get('ciudad')))

        return queryset


class CalleViewSet(viewsets.ModelViewSet):
    queryset = Calle.objects.all()
    serializer_class = CalleSerializer
    lookup_field = 'id'

    def get_queryset(self):
        query = self.request.query_params
        queryset = self.queryset
        if 'ciudad' in query.keys():
            queryset = queryset.filter(ciudad=Ciudad.objects.get(id=query.get('ciudad')))

        return queryset


class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    lookup_field = 'id'

    def get_queryset(self):
        query = self.request.query_params
        queryset = self.queryset
        if 'pais' in query.keys():
            queryset = queryset.filter(pais=Pais.objects.get(id=query.get('pais')))
        if 'provincia' in query.keys():
            queryset = queryset.filter(provincia=Provincia.objects.get(id=query.get('provincia')))
        if 'ciudad' in query.keys():
            queryset = queryset.filter(ciudad=Ciudad.objects.get(id=query.get('ciudad')))
        if 'barrio' in query.keys():
            queryset = queryset.filter(barrio=Barrio.objects.get(id=query.get('barrio')))

        return queryset
