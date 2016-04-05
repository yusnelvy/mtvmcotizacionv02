# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabajador', '0003_trabajadorestadoderegistro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizador',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('id_trabajador', models.ForeignKey(to='trabajador.Trabajador')),
            ],
            options={
                'verbose_name': 'Cotizador',
                'verbose_name_plural': 'Cotizadores',
                'ordering': ['id_trabajador'],
            },
        ),
    ]
