# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ascensor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('cantidad', models.IntegerField()),
                ('piso_ascensor', models.IntegerField()),
                ('velocidad_por_piso', models.DecimalField(decimal_places=2, max_digits=7)),
                ('ancho', models.DecimalField(decimal_places=2, max_digits=7)),
                ('largo', models.DecimalField(decimal_places=2, max_digits=7)),
                ('alto', models.DecimalField(decimal_places=2, max_digits=7)),
                ('capacidad_carga', models.DecimalField(decimal_places=3, max_digits=8)),
            ],
            options={
                'verbose_name': 'Ascensor',
                'verbose_name_plural': 'Ascensores',
            },
        ),
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('barrio', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Barrio',
                'ordering': ['ciudad', 'barrio'],
                'verbose_name_plural': 'Barrios',
            },
        ),
        migrations.CreateModel(
            name='Calle',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('calle', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Calle',
                'ordering': ['ciudad', 'calle'],
                'verbose_name_plural': 'Calles',
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('ciudad', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Ciudad',
                'ordering': ['provincia', 'ciudad'],
                'verbose_name_plural': 'Ciudades',
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('calle', models.CharField(max_length=100)),
                ('altura', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=100)),
                ('punto_referencia', models.TextField(blank=True)),
                ('observacion', models.TextField(blank=True)),
                ('barrio', smart_selects.db_fields.ChainedForeignKey(chained_model_field='ciudad', to='direccion.Barrio', chained_field='ciudad')),
                ('ciudad', smart_selects.db_fields.ChainedForeignKey(chained_model_field='provincia', to='direccion.Ciudad', chained_field='provincia')),
            ],
            options={
                'verbose_name': 'Dirección',
                'verbose_name_plural': 'Direcciones',
            },
        ),
        migrations.CreateModel(
            name='Edificacion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre_de_edificio', models.CharField(max_length=250)),
                ('cantidad_de_pisos', models.IntegerField()),
                ('cantidad_de_inmuebles_por_piso', models.IntegerField()),
                ('total_inmuebles', models.IntegerField()),
                ('rampa', models.BooleanField(default=False)),
                ('distancia_del_vehiculo', models.IntegerField()),
                ('escalera_estrecha', models.BooleanField(default=False)),
                ('escalera_inclinada', models.BooleanField(default=False)),
                ('escalon_grande', models.BooleanField(default=False)),
                ('direccion', models.ForeignKey(to='direccion.Direccion')),
            ],
            options={
                'verbose_name': 'Edificación',
                'verbose_name_plural': 'Edificaciones',
            },
        ),
        migrations.CreateModel(
            name='EspecificacionDeInmueble',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('especificacion_de_inmueble', models.CharField(max_length=250)),
                ('descripcion', models.TextField()),
                ('predeterminado', models.BooleanField(default=None)),
            ],
            options={
                'verbose_name': 'Especificación de inmueble',
                'ordering': ['especificacion_de_inmueble'],
                'verbose_name_plural': 'Especificaciones de inmueble',
            },
        ),
        migrations.CreateModel(
            name='HorarioDisponible',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('lunes', models.BooleanField(default=None)),
                ('martes', models.BooleanField(default=None)),
                ('miercoles', models.BooleanField(default=None)),
                ('jueves', models.BooleanField(default=None)),
                ('viernes', models.BooleanField(default=None)),
                ('sabado', models.BooleanField(default=None)),
                ('domingo', models.BooleanField(default=None)),
                ('hora_desde', models.TimeField()),
                ('hora_hasta', models.TimeField()),
                ('edificio', models.BooleanField(default=None)),
                ('ascensor', models.BooleanField(default=None)),
                ('observacion', models.TextField(blank=True)),
                ('edificacion', models.ForeignKey(to='direccion.Edificacion')),
            ],
            options={
                'verbose_name': 'Horario disponible',
                'verbose_name_plural': 'Horarios disponibles',
            },
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('numero_de_inmueble', models.CharField(max_length=100)),
                ('numero_de_pisos', models.IntegerField()),
                ('nombre_del_piso', models.CharField(max_length=100)),
                ('cantidad_de_ambientes', models.IntegerField()),
                ('pisos_por_escalera', models.IntegerField()),
                ('numero_de_plantas', models.IntegerField()),
                ('total_m2', models.DecimalField(decimal_places=2, max_digits=7)),
                ('baulera', models.BooleanField(default=False)),
                ('volumen_baulera', models.DecimalField(decimal_places=3, max_digits=8)),
                ('edificacion', models.ForeignKey(to='direccion.Edificacion')),
                ('especificacion_de_inmueble', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.EspecificacionDeInmueble')),
            ],
            options={
                'verbose_name': 'Inmueble',
                'ordering': ['numero_de_inmueble'],
                'verbose_name_plural': 'Inmuebles',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('pais', models.CharField(max_length=100, unique=True)),
                ('codigo_telefonico', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Pais',
                'ordering': ['pais'],
                'verbose_name_plural': 'Paises',
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('provincia', models.CharField(max_length=100)),
                ('codigo_telefonico', models.CharField(max_length=10, blank=True)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.Pais')),
            ],
            options={
                'verbose_name': 'Provincia',
                'ordering': ['pais', 'provincia'],
                'verbose_name_plural': 'Provincias',
            },
        ),
        migrations.CreateModel(
            name='TipoDeAscensor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('tipo_de_ascensor', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Tipo de ascensor',
                'verbose_name_plural': 'Tipos de ascensor',
            },
        ),
        migrations.CreateModel(
            name='TipoDeEdificacion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('tipo_de_edificacion', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Tipo de edificación',
                'verbose_name_plural': 'Tipos de edificación',
            },
        ),
        migrations.CreateModel(
            name='TipoDeInmueble',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('tipo_de_inmueble', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Tipo de inmueble',
                'ordering': ['tipo_de_inmueble'],
                'verbose_name_plural': 'Tipos de inmueble',
            },
        ),
        migrations.AddField(
            model_name='especificaciondeinmueble',
            name='tipo_de_inmueble',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.TipoDeInmueble'),
        ),
        migrations.AddField(
            model_name='edificacion',
            name='tipo_de_edificacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.TipoDeEdificacion'),
        ),
        migrations.AddField(
            model_name='direccion',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.Pais'),
        ),
        migrations.AddField(
            model_name='direccion',
            name='provincia',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='pais', to='direccion.Provincia', chained_field='pais'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.Pais'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='provincia',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='pais', to='direccion.Provincia', chained_field='pais'),
        ),
        migrations.AddField(
            model_name='calle',
            name='ciudad',
            field=models.ForeignKey(to='direccion.Ciudad'),
        ),
        migrations.AddField(
            model_name='barrio',
            name='ciudad',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='provincia', to='direccion.Ciudad', chained_field='provincia'),
        ),
        migrations.AddField(
            model_name='barrio',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.Pais'),
        ),
        migrations.AddField(
            model_name='barrio',
            name='provincia',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='pais', to='direccion.Provincia', chained_field='pais'),
        ),
        migrations.AddField(
            model_name='ascensor',
            name='edificacion',
            field=models.ForeignKey(to='direccion.Edificacion'),
        ),
        migrations.AddField(
            model_name='ascensor',
            name='tipo_de_ascensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.TipoDeAscensor'),
        ),
        migrations.AlterUniqueTogether(
            name='provincia',
            unique_together=set([('provincia', 'pais')]),
        ),
        migrations.AlterUniqueTogether(
            name='ciudad',
            unique_together=set([('ciudad', 'provincia')]),
        ),
        migrations.AlterUniqueTogether(
            name='calle',
            unique_together=set([('calle', 'ciudad')]),
        ),
        migrations.AlterUniqueTogether(
            name='barrio',
            unique_together=set([('barrio', 'ciudad')]),
        ),
    ]
