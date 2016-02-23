# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('estadoderegistro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentoDelTalonario',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('numero', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=10)),
                ('informacion_de_proceso', models.TextField()),
                ('informacion_de_beneficiari', models.TextField()),
                ('numero_final', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Documentos del talonario',
                'verbose_name': 'Documento del talonario',
                'ordering': ['talonario', 'numero'],
            },
        ),
        migrations.CreateModel(
            name='DocumentoDelTalonarioEstado',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('observacion', models.TextField(blank=True)),
                ('predefinido', models.BooleanField(default=None)),
                ('documento_del_talonario', models.ForeignKey(to='talonario.DocumentoDelTalonario')),
                ('estado_de_documento', models.ForeignKey(to='estadoderegistro.EstadoDeRegistro')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Estados de los documentos de los talonarios',
                'verbose_name': 'Estado del documento del talonario',
                'ordering': ['documento_del_talonario', 'estado_de_documento'],
            },
        ),
        migrations.CreateModel(
            name='Talonario',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('talonario', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('prefijo', models.CharField(blank=True, max_length=10)),
                ('separador', models.CharField(blank=True, max_length=10)),
                ('numero_desde', models.CharField(max_length=50)),
                ('numero_hasta', models.CharField(max_length=50)),
                ('separado_sufijo', models.CharField(blank=True, max_length=10)),
                ('sufijo', models.CharField(blank=True, max_length=10)),
                ('numeracion_correlativa', models.BooleanField(default=None)),
                ('numero_de_documento', models.IntegerField()),
                ('cantidad_fija', models.BooleanField(default=None)),
            ],
            options={
                'verbose_name_plural': 'Talonarios',
                'verbose_name': 'Talonario',
                'ordering': ['talonario'],
            },
        ),
        migrations.CreateModel(
            name='TalonarioEstado',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('observacion', models.TextField(blank=True)),
                ('predefinido', models.BooleanField(default=None)),
                ('estado_de_documento', models.ForeignKey(to='estadoderegistro.EstadoDeRegistro')),
                ('talonario', models.ForeignKey(to='talonario.Talonario')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Estados de los talonarios',
                'verbose_name': 'Estado del talonario',
                'ordering': ['talonario', 'estado_de_documento'],
            },
        ),
        migrations.CreateModel(
            name='TipoDeDocumentoImpreso',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('tipo_de_documento_impreso', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Tipos de documento impreso',
                'verbose_name': 'Tipo de documento impreso',
                'ordering': ['tipo_de_documento_impreso'],
            },
        ),
        migrations.CreateModel(
            name='TrazabilidadTalonario',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField()),
                ('descripcion', models.TextField(blank=True)),
                ('talonario', models.ForeignKey(to='talonario.Talonario')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Trazabilidad de los talonarios',
                'verbose_name': 'Trazabilidad del talonario',
            },
        ),
        migrations.AddField(
            model_name='talonario',
            name='tipo_de_documento_impreso',
            field=models.ForeignKey(to='talonario.TipoDeDocumentoImpreso'),
        ),
        migrations.AddField(
            model_name='documentodeltalonario',
            name='talonario',
            field=models.ForeignKey(to='talonario.Talonario'),
        ),
    ]
