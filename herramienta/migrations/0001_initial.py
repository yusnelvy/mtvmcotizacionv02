# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premisas', '0002_unidad'),
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DotacionBasicaDeCamion',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('cantidad', models.IntegerField()),
                ('detalle_de_vehiculo', models.ForeignKey(to='vehiculo.DetalleDeVehiculo')),
            ],
            options={
                'verbose_name_plural': 'Dotaciones básicas de camiones',
                'verbose_name': 'Dotación básica de camión',
            },
        ),
        migrations.CreateModel(
            name='Herramienta',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('herramienta', models.CharField(unique=True, max_length=100)),
                ('descripcion', models.TextField()),
                ('volumen_en_camion', models.IntegerField()),
                ('peso_kg', models.DecimalField(max_digits=9, decimal_places=2)),
                ('unidad', models.ForeignKey(to='premisas.Unidad')),
            ],
            options={
                'verbose_name_plural': 'Herramientas',
                'verbose_name': 'Herramienta',
            },
        ),
        migrations.AddField(
            model_name='dotacionbasicadecamion',
            name='herramienta',
            field=models.ForeignKey(to='herramienta.Herramienta'),
        ),
    ]
