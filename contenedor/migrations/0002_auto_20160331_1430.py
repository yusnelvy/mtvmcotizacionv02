# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenedor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenedor',
            name='capacidad_de_peso',
            field=models.DecimalField(max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='contenedor',
            name='capacidad_de_volumen',
            field=models.DecimalField(max_digits=7, decimal_places=2),
        ),
    ]
