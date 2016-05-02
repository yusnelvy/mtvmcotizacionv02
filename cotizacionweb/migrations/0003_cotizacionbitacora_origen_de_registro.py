# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacionweb', '0002_cotizacionpresupuesto_unidad_de_medida'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacionbitacora',
            name='origen_de_registro',
            field=models.CharField(max_length=20, default='A'),
            preserve_default=False,
        ),
    ]
