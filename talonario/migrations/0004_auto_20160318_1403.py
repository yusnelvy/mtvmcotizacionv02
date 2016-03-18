# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talonario', '0003_auto_20160302_1335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documentodeltalonario',
            old_name='informacion_de_beneficiari',
            new_name='informacion_de_beneficiario',
        ),
    ]
