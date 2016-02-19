# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premisas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('unidad', models.CharField(max_length=20, unique=True)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Unidad',
                'verbose_name_plural': 'Unidades',
            },
        ),
    ]
