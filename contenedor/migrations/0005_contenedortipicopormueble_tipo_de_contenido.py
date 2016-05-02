# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenedor', '0004_tipodecontenido'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenedortipicopormueble',
            name='tipo_de_contenido',
            field=models.ForeignKey(default=1, to='contenedor.TipoDeContenido', on_delete=django.db.models.deletion.PROTECT),
            preserve_default=False,
        ),
    ]
