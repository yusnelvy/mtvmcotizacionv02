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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('piso_ascensor', models.IntegerField()),
                ('velocidad_por_piso', models.DecimalField(max_digits=7, decimal_places=2)),
            ],
            options={
                'verbose_name_plural': 'Ascensores',
                'verbose_name': 'Ascensor',
            },
        ),
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barrio', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Barrios',
                'ordering': ['ciudad', 'barrio'],
                'verbose_name': 'Barrio',
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Ciudades',
                'ordering': ['provincia', 'ciudad'],
                'verbose_name': 'Ciudad',
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=100)),
                ('altura', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=100)),
                ('punto_referencia', models.CharField(max_length=250)),
                ('adicional', models.CharField(blank=True, max_length=250)),
                ('barrio', smart_selects.db_fields.ChainedForeignKey(chained_model_field='ciudad', chained_field='ciudad', to='direccion.Barrio')),
                ('ciudad', smart_selects.db_fields.ChainedForeignKey(chained_model_field='provincia', chained_field='provincia', to='direccion.Ciudad')),
            ],
            options={
                'verbose_name_plural': 'Direcciones',
                'verbose_name': 'Direccion',
            },
        ),
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_de_edificio', models.CharField(max_length=100)),
                ('cantidad_de_pisos', models.IntegerField()),
                ('cantidad_de_inmuebles_por_piso', models.IntegerField()),
                ('total_inmuebles', models.IntegerField()),
                ('rampa', models.BooleanField(default=False)),
                ('distancia_del_vehiculo', models.IntegerField()),
                ('escalera_estrecha', models.BooleanField(default=False)),
                ('escalera_inclinada', models.BooleanField(default=False)),
                ('escalon_grande', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Tipos de edificación',
                'verbose_name': 'Tipo de edificación',
            },
        ),
        migrations.CreateModel(
            name='EspecificacionDeInmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especificacion_de_inmueble', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Especificaciones de inmueble',
                'ordering': ['especificacion_de_inmueble'],
                'verbose_name': 'Especificación de inmueble',
            },
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_de_inmueble', models.IntegerField()),
                ('numero_de_pisos', models.IntegerField()),
                ('nombre_del_piso', models.CharField(max_length=100)),
                ('cantidad_de_ambientes', models.IntegerField()),
                ('pisos_por_escalera', models.IntegerField()),
                ('numero_de_plantas', models.IntegerField()),
                ('total_m2', models.DecimalField(max_digits=7, decimal_places=2)),
                ('baulera', models.BooleanField(default=False)),
                ('volumen_baulera', models.DecimalField(max_digits=8, decimal_places=3)),
                ('edificio', models.ForeignKey(to='direccion.Edificio')),
                ('especificacion_de_inmueble', models.ForeignKey(to='direccion.EspecificacionDeInmueble', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'verbose_name_plural': 'Inmuebles',
                'ordering': ['numero_de_inmueble'],
                'verbose_name': 'Inmueble',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(unique=True, max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Paises',
                'ordering': ['pais'],
                'verbose_name': 'Pais',
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provincia', models.CharField(max_length=100)),
                ('pais', models.ForeignKey(to='direccion.Pais', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'verbose_name_plural': 'Provincias',
                'ordering': ['pais', 'provincia'],
                'verbose_name': 'Provincia',
            },
        ),
        migrations.CreateModel(
            name='TipoDeAscensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_ascensor', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Tipos de ascensor',
                'verbose_name': 'Tipo de ascensor',
            },
        ),
        migrations.CreateModel(
            name='TipoDeEdificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_edificacion', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Tipos de edificación',
                'verbose_name': 'Tipo de edificación',
            },
        ),
        migrations.CreateModel(
            name='TipoDeInmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_inmueble', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Tipos de inmueble',
                'ordering': ['tipo_de_inmueble'],
                'verbose_name': 'Tipo de inmueble',
            },
        ),
        migrations.AddField(
            model_name='especificaciondeinmueble',
            name='tipo_de_inmueble',
            field=models.ForeignKey(to='direccion.TipoDeInmueble', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='edificio',
            name='tipo_de_edificacion',
            field=models.ForeignKey(to='direccion.TipoDeEdificacion', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='direccion',
            name='pais',
            field=models.ForeignKey(to='direccion.Pais', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='direccion',
            name='provincia',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='pais', chained_field='pais', to='direccion.Provincia'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='pais',
            field=models.ForeignKey(to='direccion.Pais', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='provincia',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='pais', chained_field='pais', to='direccion.Provincia'),
        ),
        migrations.AddField(
            model_name='barrio',
            name='ciudad',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='provincia', chained_field='provincia', to='direccion.Ciudad'),
        ),
        migrations.AddField(
            model_name='barrio',
            name='pais',
            field=models.ForeignKey(to='direccion.Pais', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='barrio',
            name='provincia',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='pais', chained_field='pais', to='direccion.Provincia'),
        ),
        migrations.AddField(
            model_name='ascensor',
            name='edificio',
            field=models.ForeignKey(to='direccion.Edificio'),
        ),
        migrations.AddField(
            model_name='ascensor',
            name='tipo_de_ascensor',
            field=models.ForeignKey(to='direccion.TipoDeAscensor'),
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
            name='barrio',
            unique_together=set([('barrio', 'ciudad')]),
        ),
    ]
