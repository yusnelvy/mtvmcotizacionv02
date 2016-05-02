# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0001_initial'),
        ('cotizacionweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacionpresupuesto',
            name='unidad_de_medida',
            field=models.ForeignKey(default=1, to='almacen.Unidad'),
            preserve_default=False,
        ),
    ]
