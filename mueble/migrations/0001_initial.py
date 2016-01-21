# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDeMueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_mueble', models.CharField(unique=True, max_length=100)),
                ('descripcion', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Tipos de mueble',
                'ordering': ['tipo_de_mueble'],
                'verbose_name': 'Tipo de mueble',
            },
        ),
    ]
