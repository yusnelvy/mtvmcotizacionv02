# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('premisas', '0002_unidad'),
        ('herramienta', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplejidadServicio',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('porcentaje', models.DecimalField(max_digits=5, decimal_places=2)),
                ('predefinido', models.BooleanField(default=None)),
            ],
            options={
                'verbose_name_plural': 'Complejidades del servicio',
                'verbose_name': 'Complejidad del servicio',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='HerramientasPorServicio',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('cantidad', models.DecimalField(max_digits=9, decimal_places=2)),
                ('calculo', models.CharField(max_length=200)),
                ('herramienta', models.ForeignKey(to='herramienta.Herramienta')),
            ],
            options={
                'verbose_name_plural': 'Herramientas por servicio',
                'verbose_name': 'Herramienta por servicio',
                'ordering': ['servicio', 'herramienta'],
            },
        ),
        migrations.CreateModel(
            name='PrecioDeServicio',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('precio_base', models.DecimalField(max_digits=9, decimal_places=2)),
                ('cantidad_de_gracia', models.DecimalField(max_digits=9, decimal_places=2)),
                ('intervalo_1', models.DecimalField(max_digits=9, decimal_places=2)),
                ('porcentaje_1', models.DecimalField(max_digits=9, decimal_places=2)),
                ('intevalo_2', models.DecimalField(max_digits=9, decimal_places=2)),
                ('porcentaje_2', models.DecimalField(max_digits=9, decimal_places=2)),
                ('intervalo_3', models.DecimalField(max_digits=9, decimal_places=2)),
                ('porcentaje_3', models.DecimalField(max_digits=9, decimal_places=2)),
                ('redondeo', models.DecimalField(max_digits=9, decimal_places=2)),
                ('fecha_desde', models.DateField()),
                ('fecha_hasta', models.DateField()),
                ('infinito', models.BooleanField(default=None)),
                ('fecha_preparacion', models.DateField(auto_now_add=True)),
                ('fecha_aprobacion', models.DateField(blank=True)),
                ('aprobado', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Precios del servicio',
                'verbose_name': 'Precio del servicio',
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('servicio', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('unidad_de_venta', models.ForeignKey(to='premisas.Unidad')),
            ],
            options={
                'verbose_name_plural': 'Servicios',
                'verbose_name': 'Servicio',
                'ordering': ['servicio'],
            },
        ),
        migrations.AddField(
            model_name='preciodeservicio',
            name='servicio',
            field=models.ForeignKey(to='servicio.Servicio'),
        ),
        migrations.AddField(
            model_name='preciodeservicio',
            name='user_aprobador',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='user_aprobador', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='preciodeservicio',
            name='user_preparador',
            field=models.ForeignKey(related_name='user_preparador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='herramientasporservicio',
            name='servicio',
            field=models.ForeignKey(to='servicio.Servicio'),
        ),
        migrations.AddField(
            model_name='complejidadservicio',
            name='servicio',
            field=models.ForeignKey(to='servicio.Servicio'),
        ),
    ]
