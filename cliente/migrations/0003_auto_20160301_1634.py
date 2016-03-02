# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20160301_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
