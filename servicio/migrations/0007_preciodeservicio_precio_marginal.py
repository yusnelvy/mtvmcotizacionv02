# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0006_serviciotipicopormueble_predefinido'),
    ]

    operations = [
        migrations.AddField(
            model_name='preciodeservicio',
            name='precio_marginal',
            field=models.DecimalField(max_digits=9, decimal_places=2, default=0),
            preserve_default=False,
        ),
    ]
