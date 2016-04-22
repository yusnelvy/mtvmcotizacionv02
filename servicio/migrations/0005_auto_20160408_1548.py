# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0004_serviciotipicopormueble'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='unidad_de_venta',
            field=models.ForeignKey(to='almacen.Unidad'),
        ),
    ]
