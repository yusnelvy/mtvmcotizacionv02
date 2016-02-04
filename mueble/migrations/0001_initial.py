# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ambiente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EspecificacionDeMueble',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('especificacion_de_mueble', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('ancho', models.DecimalField(decimal_places=2, max_digits=7)),
                ('largo', models.DecimalField(decimal_places=2, max_digits=7)),
                ('alto', models.DecimalField(decimal_places=2, max_digits=7)),
                ('volumen_en_camion', models.IntegerField()),
                ('predefinido', models.BooleanField(default=None)),
            ],
            options={
                'verbose_name': 'Especificación del mueble',
                'ordering': ['especificacion_de_mueble'],
                'verbose_name_plural': 'Especificaciones del mueble',
            },
        ),
        migrations.CreateModel(
            name='Mueble',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('mueble', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(blank=True)),
                ('trasladable', models.BooleanField(default=None)),
            ],
            options={
                'verbose_name': 'Mueble',
                'ordering': ['mueble'],
                'verbose_name_plural': 'Muebles',
            },
        ),
        migrations.CreateModel(
            name='MueblePorAmbiente',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('predefinido', models.BooleanField(default=None)),
                ('ambiente_por_tipo_de_inmueble', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ambiente.AmbientePorTipoDeInmueble')),
                ('especificacion_de_mueble', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mueble.EspecificacionDeMueble')),
            ],
            options={
                'verbose_name': 'Mueble por ambiente',
                'ordering': ['especificacion_de_mueble', 'ambiente_por_tipo_de_inmueble'],
                'verbose_name_plural': 'Muebles por ambientes',
            },
        ),
        migrations.CreateModel(
            name='TipoDeMueble',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('tipo_de_mueble', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Tipo de mueble',
                'ordering': ['tipo_de_mueble'],
                'verbose_name_plural': 'Tipos de mueble',
            },
        ),
        migrations.AddField(
            model_name='mueble',
            name='tipo_de_mueble',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mueble.TipoDeMueble'),
        ),
        migrations.AddField(
            model_name='especificaciondemueble',
            name='mueble',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mueble.Mueble'),
        ),
    ]
