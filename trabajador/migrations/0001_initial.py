# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CargoTrabajador',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('cargo_trabajador', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField()),
                ('cargo_padre', models.ForeignKey(blank=True, to='trabajador.CargoTrabajador', related_name='cargochild_set')),
            ],
            options={
                'verbose_name': 'Cargo de trabajador',
                'ordering': ['cargo_trabajador'],
                'verbose_name_plural': 'Cargos de trabajadores',
            },
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('dni', models.CharField(max_length=15, blank=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('volumen_en_camion', models.IntegerField()),
                ('cargo_trabajador', models.ForeignKey(to='trabajador.CargoTrabajador')),
            ],
            options={
                'verbose_name': 'Trabajador',
                'ordering': ['nombre', 'apellido'],
                'verbose_name_plural': 'Trabajadores',
            },
        ),
    ]
