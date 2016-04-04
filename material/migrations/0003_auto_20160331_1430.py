# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0002_auto_20160215_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='peso_unidad_consumo_kg',
            field=models.DecimalField(max_digits=7, decimal_places=2),
        ),
    ]
