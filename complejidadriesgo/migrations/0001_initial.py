# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComplejidadRiesgo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('situacion', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField()),
                ('factor_complejidad', models.IntegerField()),
                ('factor_riesgo', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Complejidad y riesgo',
                'ordering': ['situacion'],
                'verbose_name_plural': 'Complejidades y riesgos',
            },
        ),
        migrations.CreateModel(
            name='NivelComplejidadRiesgo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nivel_complejidad_riesgo', models.CharField(max_length=25, unique=True)),
                ('factor_inicial', models.IntegerField()),
                ('factor_final', models.IntegerField()),
                ('porcentaje', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'verbose_name': 'Nivel de complejidad y riesgo',
                'ordering': ['nivel_complejidad_riesgo'],
                'verbose_name_plural': 'niveles de complejidades y riesgos',
            },
        ),
    ]
