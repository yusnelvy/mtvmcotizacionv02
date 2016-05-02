# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0003_auto_20160331_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='unidad_de_consumo',
            field=models.ForeignKey(to='almacen.Unidad', related_name='und_consumo'),
        ),
        migrations.AlterField(
            model_name='material',
            name='unidad_de_venta',
            field=models.ForeignKey(to='almacen.Unidad', related_name='und_venta'),
        ),
    ]
