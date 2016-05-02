# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promocion', '0003_auto_20160331_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuentedepromocion',
            name='alianza',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='fuentedepromocion',
            name='condiciones_de_calculo_alianza',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='fuentedepromocion',
            name='institucion_aliado',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='personaaliado',
            name='observacion',
            field=models.TextField(blank=True),
        ),
    ]
