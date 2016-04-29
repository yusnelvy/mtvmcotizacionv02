# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0002_auto_20160331_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalledevehiculo',
            name='tara_vehiculo',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
