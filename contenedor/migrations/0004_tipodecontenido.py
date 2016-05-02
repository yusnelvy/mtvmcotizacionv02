# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenedor', '0003_contenedortipicopormueble_predefinido'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDeContenido',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(unique=True, max_length=100)),
                ('descripcion', models.TextField()),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name': 'Tipo de contenido',
                'verbose_name_plural': 'Tipos de contenido',
            },
        ),
    ]
