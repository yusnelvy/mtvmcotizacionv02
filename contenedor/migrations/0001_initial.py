# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contenedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenedor', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('capacidad_de_volumen', models.DecimalField(max_digits=7, decimal_places=3)),
                ('capacidad_de_peso', models.DecimalField(max_digits=7, decimal_places=3)),
                ('ancho', models.IntegerField()),
                ('largo', models.IntegerField()),
                ('alto', models.IntegerField()),
                ('volumen_en_camion', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Contenedores',
                'ordering': ['contenedor'],
                'verbose_name': 'Contenedor',
            },
        ),
    ]
