# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mueble', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mueble',
            name='contenido_fragil',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='mueble',
            name='contenido_textil',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='mueble',
            name='fragil',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='mueble',
            name='pesado',
            field=models.BooleanField(default=None),
        ),
    ]
