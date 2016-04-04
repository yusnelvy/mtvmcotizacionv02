# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0002_auto_20160302_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complejidadservicio',
            name='porcentaje',
            field=models.DecimalField(max_digits=7, decimal_places=2),
        ),
    ]
