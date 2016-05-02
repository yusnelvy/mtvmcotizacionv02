# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacionweb', '0003_cotizacionbitacora_origen_de_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacionbitacora',
            name='origen_de_registro',
            field=models.CharField(choices=[('A', 'Automatico'), ('C', 'Call center'), ('M', 'Manual')], max_length=20),
        ),
    ]
