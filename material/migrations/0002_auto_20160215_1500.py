# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premisas', '0002_unidad'),
        ('servicio', '0001_initial'),
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialesporservicio',
            name='servicio',
            field=models.ForeignKey(to='servicio.Servicio'),
        ),
        migrations.AddField(
            model_name='material',
            name='tipo_de_material',
            field=models.ForeignKey(to='material.TipoDeMaterial'),
        ),
        migrations.AddField(
            model_name='material',
            name='unidad_de_consumo',
            field=models.ForeignKey(related_name='und_consumo', to='premisas.Unidad'),
        ),
        migrations.AddField(
            model_name='material',
            name='unidad_de_venta',
            field=models.ForeignKey(related_name='und_venta', to='premisas.Unidad'),
        ),
    ]
