# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('almacen', models.CharField(max_length=100, unique=True)),
                ('ventas', models.BooleanField(default=False)),
                ('compras', models.BooleanField(default=False)),
                ('consumo', models.BooleanField(default=False)),
                ('produccion', models.BooleanField(default=False)),
                ('descripcion', models.TextField()),
            ],
            options={
                'ordering': ['almacen'],
                'verbose_name_plural': 'Almacenes',
                'verbose_name': 'Almacen',
            },
        ),
        migrations.CreateModel(
            name='TipoDeMovimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_movimiento', models.CharField(max_length=100, unique=True)),
                ('sentido', models.BooleanField(default=False)),
                ('descripcion', models.TextField()),
            ],
            options={
                'ordering': ['tipo_de_movimiento'],
                'verbose_name_plural': 'Tipos de movimientos',
                'verbose_name': 'Tipo de movimiento',
            },
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidad', models.CharField(max_length=20, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Unidades',
                'verbose_name': 'Unidad',
            },
        ),
    ]
