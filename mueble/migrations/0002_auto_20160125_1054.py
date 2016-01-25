# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambiente', '0002_ambienteportipodeinmueble'),
        ('mueble', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EspecificacionDeMueble',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('especificacion_de_mueble', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('ancho', models.DecimalField(decimal_places=2, max_digits=7)),
                ('largo', models.DecimalField(decimal_places=2, max_digits=7)),
                ('alto', models.DecimalField(decimal_places=2, max_digits=7)),
                ('volumen_en_camion', models.IntegerField()),
                ('predefinido', models.BooleanField(default=None)),
            ],
            options={
                'verbose_name_plural': 'Especificaciones del mueble',
                'verbose_name': 'Especificación del mueble',
                'ordering': ['especificacion_de_mueble'],
            },
        ),
        migrations.CreateModel(
            name='Mueble',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('mueble', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(blank=True)),
                ('trasladable', models.BooleanField(default=None)),
                ('tipo_de_mueble', models.ForeignKey(to='mueble.TipoDeMueble')),
            ],
            options={
                'verbose_name_plural': 'Muebles',
                'verbose_name': 'Mueble',
                'ordering': ['mueble'],
            },
        ),
        migrations.CreateModel(
            name='MueblePorAmbiente',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('predefinido', models.BooleanField(default=None)),
                ('ambiente_por_tipo_de_inmueble', models.ForeignKey(to='ambiente.AmbientePorTipoDeInmueble')),
                ('especificacion_de_mueble', models.ForeignKey(to='mueble.EspecificacionDeMueble')),
            ],
            options={
                'verbose_name_plural': 'Muebles por ambiente ',
                'verbose_name': 'Mueble por ambiente',
                'ordering': ['especificacion_de_mueble', 'ambiente_por_tipo_de_inmueble'],
            },
        ),
        migrations.AddField(
            model_name='especificaciondemueble',
            name='mueble',
            field=models.ForeignKey(to='mueble.Mueble'),
        ),
    ]
