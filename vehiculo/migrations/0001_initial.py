# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('trabajador', '0001_initial'),
        ('estadoderegistro', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoferAsignado',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('fecha_desde', models.DateField()),
                ('fecha_hasta', models.DateField()),
            ],
            options={
                'verbose_name': 'Chofer asignado',
                'ordering': ['detalle_de_vehiculo', 'trabajador'],
                'verbose_name_plural': 'Choferes asignadoa',
            },
        ),
        migrations.CreateModel(
            name='DetalleDeVehiculo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('numero_de_camion', models.IntegerField()),
                ('ancho', models.DecimalField(decimal_places=2, max_digits=7)),
                ('largo', models.DecimalField(decimal_places=2, max_digits=7)),
                ('alto', models.DecimalField(decimal_places=2, max_digits=7)),
                ('ancho_aux', models.DecimalField(decimal_places=2, blank=True, max_digits=7)),
                ('largo_aux', models.DecimalField(decimal_places=2, blank=True, max_digits=7)),
                ('alto_aux', models.DecimalField(decimal_places=2, blank=True, max_digits=7)),
                ('tara_vehiculo', models.DecimalField(decimal_places=3, max_digits=9)),
                ('observacion', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Vehículo',
                'verbose_name_plural': 'Vehículos',
            },
        ),
        migrations.CreateModel(
            name='EstadoDeVehiculo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('observacion', models.TextField(blank=True)),
                ('predefinido', models.BooleanField(default=None)),
                ('detalle_especifico', models.ForeignKey(to='vehiculo.DetalleDeVehiculo')),
                ('estado_de_registro', models.ForeignKey(to='estadoderegistro.EstadoDeRegistro')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Estado de registro de vehículo',
                'ordering': ['detalle_especifico', 'estado_de_registro'],
                'verbose_name_plural': 'Estados de registro de vehículo',
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('transmision', models.CharField(max_length=100)),
                ('motor', models.CharField(max_length=100)),
                ('volumen_total_carga', models.DecimalField(decimal_places=3, max_digits=9)),
                ('peso_total_carga', models.DecimalField(decimal_places=3, max_digits=9)),
            ],
            options={
                'verbose_name': 'Vehículo',
                'verbose_name_plural': 'Vehículos',
            },
        ),
        migrations.AddField(
            model_name='detalledevehiculo',
            name='vehiculo',
            field=models.ForeignKey(to='vehiculo.Vehiculo'),
        ),
        migrations.AddField(
            model_name='choferasignado',
            name='detalle_de_vehiculo',
            field=models.ForeignKey(to='vehiculo.DetalleDeVehiculo'),
        ),
        migrations.AddField(
            model_name='choferasignado',
            name='trabajador',
            field=models.ForeignKey(to='trabajador.Trabajador'),
        ),
    ]
