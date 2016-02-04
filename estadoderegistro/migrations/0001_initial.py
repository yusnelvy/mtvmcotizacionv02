# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('estado', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Estado',
                'ordering': ['estado'],
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='EstadoDeRegistro',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('model', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('observacion', models.TextField(blank=True)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='estadoderegistro.Estado')),
            ],
            options={
                'verbose_name': 'Estado de registro',
                'ordering': ['model', 'estado'],
                'verbose_name_plural': 'Estados de registros',
            },
        ),
    ]
