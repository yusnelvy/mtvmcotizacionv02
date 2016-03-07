# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0004_auto_20160303_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='numero_de_pisos',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='total_m2',
            field=models.DecimalField(max_digits=7, null=True, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='volumen_baulera',
            field=models.DecimalField(max_digits=8, null=True, decimal_places=3, blank=True),
        ),
    ]
