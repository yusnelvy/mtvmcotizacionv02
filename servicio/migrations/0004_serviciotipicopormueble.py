# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mueble', '0001_initial'),
        ('servicio', '0003_auto_20160331_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicioTipicoPorMueble',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('especificacion_de_mueble', models.ForeignKey(to='mueble.EspecificacionDeMueble', on_delete=django.db.models.deletion.PROTECT)),
                ('servicio', models.ForeignKey(to='servicio.Servicio', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'verbose_name_plural': 'Servicios tipicos por Muebles',
                'ordering': ['servicio'],
                'verbose_name': 'Servicio tipico por mueble',
            },
        ),
    ]
