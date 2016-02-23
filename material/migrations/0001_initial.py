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
            name='Material',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('material', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('relacion_consumo_venta', models.DecimalField(max_digits=9, decimal_places=2)),
                ('ancho', models.DecimalField(max_digits=7, decimal_places=2)),
                ('largo', models.DecimalField(max_digits=7, decimal_places=2)),
                ('alto', models.DecimalField(max_digits=7, decimal_places=2)),
                ('peso_unidad_consumo_kg', models.DecimalField(max_digits=9, decimal_places=3)),
                ('cotizable', models.BooleanField(default=None)),
            ],
            options={
                'verbose_name_plural': 'Materiales',
                'verbose_name': 'Material ',
                'ordering': ['material'],
            },
        ),
        migrations.CreateModel(
            name='MaterialesPorServicio',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('cantidad', models.DecimalField(max_digits=9, decimal_places=2)),
                ('calculo', models.CharField(max_length=200)),
                ('material', models.ForeignKey(to='material.Material')),
            ],
            options={
                'verbose_name_plural': 'Materiales por servicio',
                'verbose_name': 'Material por servicio',
                'ordering': ['servicio', 'material'],
            },
        ),
        migrations.CreateModel(
            name='PrecioDeMaterial',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('precio', models.DecimalField(max_digits=9, decimal_places=2)),
                ('fecha_desde', models.DateField()),
                ('fecha_hasta', models.DateField()),
                ('infinito', models.BooleanField(default=None)),
                ('fecha_preparacion', models.DateField(auto_now_add=True)),
                ('fecha_aprobacion', models.DateField(blank=True)),
                ('aprobado', models.BooleanField(default=None)),
                ('material', models.ForeignKey(to='material.Material')),
                ('user_aprobador', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='user_aprobador_material', null=True, blank=True)),
                ('user_preparador', models.ForeignKey(related_name='user_preparador_material', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Precios del material',
                'verbose_name': 'Precio del material',
            },
        ),
        migrations.CreateModel(
            name='TipoDeMaterial',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('tipo_de_material', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Tipos de materiales',
                'verbose_name': 'Tipo de material ',
                'ordering': ['tipo_de_material'],
            },
        ),
    ]
