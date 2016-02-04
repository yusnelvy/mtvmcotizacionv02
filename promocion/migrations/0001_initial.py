# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        ('direccion', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('estadoderegistro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alianza',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('alianza', models.CharField(max_length=100)),
                ('porcentaje_comision', models.DecimalField(decimal_places=2, max_digits=5)),
                ('observacion', models.TextField()),
                ('fecha_vigencia', models.DateField()),
            ],
            options={
                'verbose_name': 'Alianza',
                'verbose_name_plural': 'Alianzas',
            },
        ),
        migrations.CreateModel(
            name='AlianzaEstado',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('observacion', models.TextField(blank=True)),
                ('predefinido', models.BooleanField(default=None)),
                ('alianza', models.ForeignKey(to='promocion.Alianza')),
                ('estado_de_registro', models.ForeignKey(to='estadoderegistro.EstadoDeRegistro')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Estado de registro de alianza',
                'ordering': ['alianza', 'estado_de_registro'],
                'verbose_name_plural': 'Estados de registro de alianza',
            },
        ),
        migrations.CreateModel(
            name='FuenteDePromocion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre_referido', models.CharField(max_length=250, blank=True)),
                ('telefono_referido', models.CharField(max_length=100, blank=True)),
                ('institucion_aliado', models.TextField()),
                ('alianza', models.TextField()),
                ('condiciones_de_calculo_alianza', models.TextField()),
                ('barrio', models.ForeignKey(to='direccion.Barrio')),
                ('cliente', models.ForeignKey(to='cliente.Cliente')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=250)),
                ('cuit', models.CharField(max_length=25)),
                ('pagina_web', models.CharField(max_length=250, blank=True)),
                ('persona_contacto', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=25)),
                ('telefono_movil', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=250)),
                ('alianza', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='promocion.Alianza')),
            ],
            options={
                'verbose_name': 'Institución',
                'verbose_name_plural': 'Instituciones',
            },
        ),
        migrations.CreateModel(
            name='Medio',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('medio', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Medio',
                'verbose_name_plural': 'Medios',
            },
        ),
        migrations.CreateModel(
            name='MedioEspecifico',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('medio_especifico', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('medio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='promocion.Medio')),
            ],
            options={
                'verbose_name': 'Medio especifico',
                'verbose_name_plural': 'Medios especificos',
            },
        ),
        migrations.CreateModel(
            name='PersonaAliado',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('dni', models.CharField(max_length=15, blank=True)),
                ('nombre', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=100)),
                ('telefono_movil_1', models.CharField(max_length=25, blank=True)),
                ('telefono_movil_2', models.CharField(max_length=25, blank=True)),
                ('email_principal', models.CharField(max_length=250, blank=True)),
                ('email_secundario', models.CharField(max_length=250, blank=True)),
                ('observacion', models.TextField()),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='promocion.Institucion')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
        migrations.CreateModel(
            name='TipoDeReferido',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('tipo_de_referido', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('medio_especifico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='promocion.MedioEspecifico')),
            ],
            options={
                'verbose_name': 'Tipo de referido',
                'verbose_name_plural': 'Tipos de referidos',
            },
        ),
        migrations.AddField(
            model_name='fuentedepromocion',
            name='medio_especifico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='promocion.MedioEspecifico'),
        ),
        migrations.AddField(
            model_name='fuentedepromocion',
            name='persona_aliado',
            field=models.ForeignKey(to='promocion.PersonaAliado'),
        ),
        migrations.AddField(
            model_name='fuentedepromocion',
            name='tipo_de_referido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='promocion.TipoDeReferido'),
        ),
        migrations.AddField(
            model_name='alianza',
            name='medio_especifico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='promocion.MedioEspecifico'),
        ),
    ]
