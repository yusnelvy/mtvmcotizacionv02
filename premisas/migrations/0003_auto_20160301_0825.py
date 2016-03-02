# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premisas', '0002_unidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variantevisualdetalle',
            name='visibilidad',
            field=models.IntegerField(default=1, choices=[(1, 'Visible'), (2, 'No visible'), (3, 'Nunca visible')]),
        ),
    ]
