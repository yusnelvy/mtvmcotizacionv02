# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalledevehiculo',
            name='tara_vehiculo',
            field=models.DecimalField(max_digits=7, decimal_places=7),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='peso_total_carga',
            field=models.DecimalField(max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='volumen_total_carga',
            field=models.DecimalField(max_digits=7, decimal_places=2),
        ),
    ]
