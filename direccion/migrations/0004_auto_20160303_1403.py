# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0003_auto_20160303_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edificacion',
            name='cantidad_de_inmuebles_por_piso',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='cantidad_de_pisos',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='distancia_del_vehiculo',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='total_inmuebles',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
