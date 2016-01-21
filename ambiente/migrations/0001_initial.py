# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ambiente', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('conteo_de_ambientes', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Ambientes',
                'ordering': ['ambiente'],
                'verbose_name': 'Ambiente',
            },
        ),
    ]
