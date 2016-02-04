# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoDeDocumento',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('estado_de_documento', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('orden', models.IntegerField()),
                ('observacion', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Estado de documento',
                'ordering': ['tipo_de_documento', 'estado_de_documento'],
                'verbose_name_plural': 'Estados de documentos',
            },
        ),
        migrations.CreateModel(
            name='TipoDeDocumento',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('tipo_de_documento', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Tipo de documento',
                'ordering': ['tipo_de_documento'],
                'verbose_name_plural': 'Tipos de documento',
            },
        ),
        migrations.AddField(
            model_name='estadodedocumento',
            name='tipo_de_documento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestiondedocumento.TipoDeDocumento'),
        ),
    ]
