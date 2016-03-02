# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talonario', '0002_auto_20160217_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trazabilidadtalonario',
            name='fecha_modificacion',
            field=models.DateField(null=True, blank=True),
        ),
    ]
