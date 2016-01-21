# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(unique=True, max_length=100)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Estados',
                'ordering': ['estado'],
                'verbose_name': 'Estado',
            },
        ),
        migrations.CreateModel(
            name='EstadoDeRegistro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('observacion', models.TextField(blank=True)),
                ('estado', models.ForeignKey(to='estadoderegistro.Estado')),
            ],
            options={
                'verbose_name_plural': 'Estados de registros',
                'ordering': ['tipo_de_registro', 'estado'],
                'verbose_name': 'Estado de registro',
            },
        ),
        migrations.CreateModel(
            name='TipoDeRegistro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_registro', models.CharField(unique=True, max_length=100)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Tipos de registro',
                'ordering': ['tipo_de_registro'],
                'verbose_name': 'Tipo de Registro',
            },
        ),
        migrations.AddField(
            model_name='estadoderegistro',
            name='tipo_de_registro',
            field=models.ForeignKey(to='estadoderegistro.TipoDeRegistro'),
        ),
    ]
