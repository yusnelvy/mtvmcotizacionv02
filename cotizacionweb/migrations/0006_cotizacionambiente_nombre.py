# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacionweb', '0005_auto_20160420_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacionambiente',
            name='nombre',
            field=models.CharField(max_length=100, default=1),
            preserve_default=False,
        ),
    ]
