# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promocion', '0002_auto_20160301_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alianza',
            name='porcentaje_comision',
            field=models.DecimalField(max_digits=7, decimal_places=2),
        ),
    ]
