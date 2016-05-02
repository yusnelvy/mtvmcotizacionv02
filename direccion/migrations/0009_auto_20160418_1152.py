# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0008_auto_20160404_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ascensor',
            name='capacidad_carga',
            field=models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=2),
        ),
    ]
