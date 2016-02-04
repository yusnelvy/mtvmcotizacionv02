# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='menu_padre',
            field=models.ForeignKey(related_name='nenuchild_set', blank=True, to='menu.Menu', null=True),
        ),
    ]
