# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('estadoderegistro', '0001_initial'),
        ('trabajador', '0002_auto_20160204_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrabajadorEstadoDeRegistro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('observacion', models.TextField(blank=True)),
                ('predefinido', models.BooleanField(default=None)),
                ('estado_de_registro', models.ForeignKey(to='estadoderegistro.EstadoDeRegistro')),
                ('trabajador', models.ForeignKey(to='trabajador.Trabajador')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Estado de registro de trabajador',
                'verbose_name_plural': 'Estados de registro de trabajador',
                'ordering': ['trabajador', 'estado_de_registro'],
            },
        ),
    ]
