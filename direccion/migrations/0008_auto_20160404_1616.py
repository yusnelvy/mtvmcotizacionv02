# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0007_auto_20160401_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='numero_de_plantas',
            field=models.IntegerField(default=1, blank=True),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='pisos_por_escalera',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
