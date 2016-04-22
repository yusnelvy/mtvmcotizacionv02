# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0005_auto_20160408_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviciotipicopormueble',
            name='predefinido',
            field=models.BooleanField(default=None),
        ),
    ]
