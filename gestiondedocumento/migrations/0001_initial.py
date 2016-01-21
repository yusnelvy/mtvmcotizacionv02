# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoDeDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.IntegerField()),
                ('estado_de_documento', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('observacion', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Estados de documentos',
                'ordering': ['tipo_de_documento', 'estado_de_documento'],
                'verbose_name': 'Estado de documento',
            },
        ),
        migrations.CreateModel(
            name='TipoDeDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_documento', models.CharField(unique=True, max_length=100)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Tipos de documento',
                'ordering': ['tipo_de_documento'],
                'verbose_name': 'Tipo de documento',
            },
        ),
        migrations.AddField(
            model_name='estadodedocumento',
            name='tipo_de_documento',
            field=models.ForeignKey(to='gestiondedocumento.TipoDeDocumento'),
        ),
    ]
