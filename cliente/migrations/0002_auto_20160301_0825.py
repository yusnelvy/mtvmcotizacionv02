# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='cuit',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='observaciones',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='clientedireccion',
            name='detalle_de_direccion',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientedireccion',
            name='titulo_de_direccion',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
