# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premisas', '0003_auto_20160301_0825'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Unidad',
        ),
    ]
