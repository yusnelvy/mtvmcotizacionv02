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
            name='Cliente',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='ClienteDireccion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('cliente', models.ForeignKey(to='cliente.Cliente')),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.Direccion')),
            ],
            options={
                'verbose_name': 'Dirección del cliente',
                'ordering': ['cliente', 'direccion'],
                'verbose_name_plural': 'Direcciones del cliente',
            },
        ),
        migrations.CreateModel(
            name='ClienteEstadoDeRegistro',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('observacion', models.TextField(blank=True)),
                ('predefinido', models.BooleanField(default=None)),
                ('cliente', models.ForeignKey(to='cliente.Cliente')),
                ('estado_de_registro', models.ForeignKey(to='estadoderegistro.EstadoDeRegistro')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Estado de registro de cliente',
                'ordering': ['cliente', 'estado_de_registro'],
                'verbose_name_plural': 'Estados de registro de cliente',
            },
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('dni', models.CharField(max_length=15, blank=True)),
                ('nombre', models.CharField(max_length=300)),
                ('fecha_nacimiento', models.DateField(blank=True)),
                ('observaciones', models.TextField(blank=True)),
                ('cliente', models.ForeignKey(to='cliente.Cliente')),
            ],
            options={
                'verbose_name': 'Contacto',
                'ordering': ['nombre'],
                'verbose_name_plural': 'Contactos',
            },
        ),
        migrations.CreateModel(
            name='EstadoCivil',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('estado_civil', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'verbose_name': 'Estado civil',
                'ordering': ['estado_civil'],
                'verbose_name_plural': 'Estados civil',
            },
        ),
        migrations.CreateModel(
            name='InformacionDeContacto',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('informacion_de_contacto', models.CharField(max_length=250)),
                ('contacto', models.ForeignKey(to='cliente.Contacto')),
            ],
            options={
                'verbose_name': 'Información de contacto',
                'ordering': ['contacto', 'tipo_de_informacion_de_contacto'],
                'verbose_name_plural': 'Informaciones de contactos',
            },
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('sexo', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'verbose_name': 'Sexo',
                'ordering': ['sexo'],
                'verbose_name_plural': 'Sexos',
            },
        ),
        migrations.CreateModel(
            name='TipoDeCliente',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('tipo_de_cliente', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Tipo de cliente',
                'ordering': ['tipo_de_cliente'],
                'verbose_name_plural': 'Tipos de cliente',
            },
        ),
        migrations.CreateModel(
            name='TipoDeInformacionDeContacto',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('tipo_de_informacion_de_contacto', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Tipo de información de contacto',
                'ordering': ['tipo_de_informacion_de_contacto'],
                'verbose_name_plural': 'Tipos de información de contacto',
            },
        ),
        migrations.CreateModel(
            name='TipoDeRelacion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('tipo_de_relacion', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Tipo de relacion',
                'ordering': ['tipo_de_relacion'],
                'verbose_name_plural': 'Tipos de relaciones',
            },
        ),
        migrations.AddField(
            model_name='informaciondecontacto',
            name='tipo_de_informacion_de_contacto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cliente.TipoDeInformacionDeContacto'),
        ),
        migrations.AddField(
            model_name='contacto',
            name='estado_civil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cliente.EstadoCivil'),
        ),
        migrations.AddField(
            model_name='contacto',
            name='sexo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cliente.Sexo'),
        ),
        migrations.AddField(
            model_name='contacto',
            name='tipo_de_relacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cliente.TipoDeRelacion'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipo_de_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cliente.TipoDeCliente'),
        ),
    ]
