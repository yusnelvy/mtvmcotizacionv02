# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0005_auto_20160304_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ascensor',
            name='capacidad_carga',
            field=models.DecimalField(max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='volumen_baulera',
            field=models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True),
        ),
    ]
