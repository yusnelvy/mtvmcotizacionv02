# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0001_initial'),
        ('servicio', '0007_preciodeservicio_precio_marginal'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='unidad_de_consumo',
            field=models.ForeignKey(default=1, to='almacen.Unidad', related_name='unidad_de_consumo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servicio',
            name='unidad_de_venta',
            field=models.ForeignKey(to='almacen.Unidad', related_name='unidad_de_venta'),
        ),
    ]
