# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0003_auto_20160303_1401'),
        ('cliente', '0003_auto_20160301_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientedireccion',
            name='edificacion',
            field=models.ForeignKey(blank=True, to='direccion.Edificacion', null=True),
        ),
        migrations.AddField(
            model_name='clientedireccion',
            name='inmueble',
            field=models.ForeignKey(blank=True, to='direccion.Inmueble', null=True),
        ),
    ]
