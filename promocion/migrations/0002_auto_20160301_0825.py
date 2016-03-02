# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promocion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fuentedepromocion',
            options={'verbose_name': 'Fuente de promoción', 'verbose_name_plural': 'Fuentes de promociones'},
        ),
    ]
