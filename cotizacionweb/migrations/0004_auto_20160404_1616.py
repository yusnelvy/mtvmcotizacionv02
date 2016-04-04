# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacionweb', '0003_auto_20160401_1206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cotizaciondireccion',
            name='pisos_escalera',
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='numero_cotizacion',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='cotizaciondireccion',
            name='baulera',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cotizaciondireccion',
            name='escalera_estrecha',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cotizaciondireccion',
            name='escalera_inclinada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cotizaciondireccion',
            name='escalon_grande',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cotizaciondireccion',
            name='rampa',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cotizacionestado',
            name='fecha_registro',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cotizacionestado',
            name='observacion',
            field=models.TextField(blank=True),
        ),
    ]
