# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_auto_20160303_1401'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='clientedireccion',
            unique_together=set([('cliente', 'direccion')]),
        ),
    ]
