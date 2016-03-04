# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0002_auto_20160301_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ascensor',
            name='cantidad',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='ascensor',
            name='velocidad_por_piso',
            field=models.DecimalField(default=6, max_digits=7, decimal_places=2),
        ),
    ]
