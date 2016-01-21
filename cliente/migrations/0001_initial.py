# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoCivil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_civil', models.CharField(unique=True, max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Estados civil',
                'ordering': ['estado_civil'],
                'verbose_name': 'Estado civil',
            },
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(unique=True, max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Sexos',
                'ordering': ['sexo'],
                'verbose_name': 'Sexo',
            },
        ),
        migrations.CreateModel(
            name='TipoDeCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_cliente', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Tipos de cliente',
                'ordering': ['tipo_de_cliente'],
                'verbose_name': 'Tipo de cliente',
            },
        ),
        migrations.CreateModel(
            name='TipoDeContacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_contacto', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Tipos de contacto',
                'ordering': ['tipo_de_contacto'],
                'verbose_name': 'Tipo de contacto',
            },
        ),
        migrations.CreateModel(
            name='TipoDeInformacionDeContacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_informacion_de_contacto', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Tipos de información de contacto',
                'ordering': ['tipo_de_informacion_de_contacto'],
                'verbose_name': 'Tipo de información de contacto',
            },
        ),
    ]
