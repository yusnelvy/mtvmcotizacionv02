# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosPrecargado',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre_app', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('dato', models.CharField(max_length=100)),
                ('tipo_de_dato', models.CharField(max_length=100)),
                ('valor', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Dato precargado',
                'verbose_name_plural': 'Datos precargados',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('codigo', models.CharField(max_length=10)),
                ('empresa', models.CharField(max_length=250)),
                ('telefonos', models.CharField(max_length=250)),
                ('direccion', models.CharField(max_length=250)),
                ('sitio_web', models.URLField()),
                ('correo', models.EmailField(max_length=254)),
                ('responsable', models.CharField(null=True, max_length=250, blank=True)),
                ('cuit', models.CharField(null=True, max_length=100, blank=True)),
                ('logo', models.ImageField(upload_to='static/img/')),
                ('telefono_call_center', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('moneda', models.CharField(max_length=5, unique=True)),
            ],
            options={
                'verbose_name': 'Moneda',
                'verbose_name_plural': 'Monedas',
            },
        ),
        migrations.CreateModel(
            name='PersonalizacionVisual',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('tipo', models.CharField(max_length=250)),
                ('valor', models.CharField(max_length=100)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Personalización Visual',
                'verbose_name_plural': 'Personalizaciones Visuales',
            },
        ),
        migrations.CreateModel(
            name='VarianteVisual',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('model', models.CharField(max_length=100)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Variente Visual',
                'verbose_name_plural': 'Variantes Visuales',
            },
        ),
        migrations.CreateModel(
            name='VarianteVisualDetalle',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('campo', models.CharField(max_length=100)),
                ('visibilidad', models.IntegerField()),
                ('variante_visual', models.ForeignKey(to='premisas.VarianteVisual')),
            ],
            options={
                'verbose_name': 'Detalle de la variente visual',
                'verbose_name_plural': 'Detalle de las variantes visuales',
            },
        ),
        migrations.AlterUniqueTogether(
            name='personalizacionvisual',
            unique_together=set([('usuario', 'tipo')]),
        ),
    ]
