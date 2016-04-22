from rest_framework import serializers
from direccion.models import Pais, Provincia, Ciudad, \
    Barrio, Calle, Direccion

from cliente.models import Cliente, TipoDeCliente


# Serializers define the API representation.
class TipoDeClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoDeCliente
        fields = ('id', 'tipo_de_cliente', 'descripcion')


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    tipo_de_cliente = TipoDeClienteSerializer(many=False, read_only=True)

    class Meta:
        model = Cliente
        fields = ('id', 'tipo_de_cliente', 'cuit', 'nombre')


class PaisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pais
        fields = ('id', 'pais', 'codigo_telefonico')


class ProvinciaSerializer(serializers.HyperlinkedModelSerializer):
    pais = PaisSerializer(many=False, read_only=True)

    class Meta:
        model = Provincia
        fields = ('id', 'provincia', 'pais', 'codigo_telefonico')


class CiudadSerializer(serializers.HyperlinkedModelSerializer):
    provincia = ProvinciaSerializer(many=False, read_only=True)
    pais = PaisSerializer(many=False, read_only=True)

    class Meta:
        model = Ciudad
        fields = ('id', 'ciudad', 'provincia', 'pais')


class BarrioSerializer(serializers.HyperlinkedModelSerializer):
    ciudad = CiudadSerializer(many=False, read_only=True)
    provincia = ProvinciaSerializer(many=False, read_only=True)
    pais = PaisSerializer(many=False, read_only=True)

    class Meta:
        model = Barrio
        fields = ('id', 'barrio', 'ciudad', 'provincia', 'pais')


class CalleSerializer(serializers.HyperlinkedModelSerializer):
    ciudad = CiudadSerializer(many=False, read_only=True)

    class Meta:
        model = Calle
        fields = ('id', 'calle', 'ciudad')


class DireccionSerializer(serializers.HyperlinkedModelSerializer):
    barrio = BarrioSerializer(many=False, read_only=True)
    ciudad = CiudadSerializer(many=False, read_only=True)
    provincia = ProvinciaSerializer(many=False, read_only=True)
    pais = PaisSerializer(many=False, read_only=True)

    class Meta:
        model = Direccion
        fields = ('id',
                  'calle',
                  'altura',
                  'barrio',
                  'ciudad',
                  'provincia',
                  'pais',
                  'zip',
                  'punto_referencia',
                  'observacion')
