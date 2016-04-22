# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenedor', '0002_auto_20160331_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenedortipicopormueble',
            name='predefinido',
            field=models.BooleanField(default=None),
        ),
    ]
