# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0001_initial'),
        ('estadoderegistro', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('ambiente', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField()),
                ('conteo_de_ambientes', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'ambiente',
                'ordering': ['ambiente'],
                'verbose_name_plural': 'Ambientes',
            },
        ),
        migrations.CreateModel(
            name='AmbienteEstadoDeRegistro',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('observacion', models.TextField(blank=True)),
                ('predefinido', models.BooleanField(default=None)),
                ('ambiente', models.ForeignKey(to='ambiente.Ambiente')),
                ('estado_de_registro', models.ForeignKey(to='estadoderegistro.EstadoDeRegistro')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Estado de registro de ambiente',
                'ordering': ['ambiente', 'estado_de_registro'],
                'verbose_name_plural': 'Estados de registro de ambiente',
            },
        ),
        migrations.CreateModel(
            name='AmbientePorTipoDeInmueble',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('predeterminado', models.BooleanField(default=False)),
                ('ambiente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ambiente.Ambiente')),
                ('especificacion_de_inmueble', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.EspecificacionDeInmueble')),
            ],
            options={
                'verbose_name': 'Ambiente por tipo inmueble',
                'ordering': ['especificacion_de_inmueble', 'ambiente'],
                'verbose_name_plural': 'Ambientes por tipos de inmueble',
            },
        ),
    ]
