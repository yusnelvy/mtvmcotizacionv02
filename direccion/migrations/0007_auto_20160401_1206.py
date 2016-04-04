# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0006_auto_20160331_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='zip',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='nombre_del_piso',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
