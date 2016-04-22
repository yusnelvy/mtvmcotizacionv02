# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenedor', '0005_contenedortipicopormueble_tipo_de_contenido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contenedortipicopormueble',
            name='predefinido',
        ),
    ]
