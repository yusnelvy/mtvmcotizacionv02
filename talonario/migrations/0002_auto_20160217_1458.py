# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talonario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trazabilidadtalonario',
            name='fecha_modificacion',
            field=models.DateField(blank=True),
        ),
    ]
