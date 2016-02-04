# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('codigo', models.CharField(max_length=15)),
                ('mensaje', models.CharField(max_length=250)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Mensaje',
                'verbose_name_plural': 'Mensajes',
            },
        ),
        migrations.CreateModel(
            name='TipoDeMensaje',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('tipo_de_mensaje', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Tipo de mensaje',
                'verbose_name_plural': 'Tipos de mensajes',
            },
        ),
        migrations.AddField(
            model_name='mensaje',
            name='tipo_de_mensaje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mensaje.TipoDeMensaje'),
        ),
    ]
