# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mueble', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contenedor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('contenedor', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField()),
                ('capacidad_de_volumen', models.DecimalField(decimal_places=3, max_digits=7)),
                ('capacidad_de_peso', models.DecimalField(decimal_places=3, max_digits=7)),
                ('ancho', models.IntegerField()),
                ('largo', models.IntegerField()),
                ('alto', models.IntegerField()),
                ('volumen_en_camion', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Contenedor',
                'ordering': ['contenedor'],
                'verbose_name_plural': 'Contenedores',
            },
        ),
        migrations.CreateModel(
            name='ContenedorTipicoPorMueble',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('cantidad', models.IntegerField()),
                ('contenedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenedor.Contenedor')),
                ('especificacion_de_mueble', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mueble.EspecificacionDeMueble')),
            ],
            options={
                'verbose_name': 'Contenedor tipico por mueble',
                'ordering': ['contenedor'],
                'verbose_name_plural': 'Contenedores tipicos por Muebles',
            },
        ),
    ]
