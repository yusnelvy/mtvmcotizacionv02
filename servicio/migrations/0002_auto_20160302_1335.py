# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preciodeservicio',
            old_name='intevalo_2',
            new_name='intervalo_2',
        ),
    ]
