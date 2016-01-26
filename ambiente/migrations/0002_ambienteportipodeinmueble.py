# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0001_initial'),
        ('ambiente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmbientePorTipoDeInmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('predeterminado', models.BooleanField(default=False)),
                ('ambiente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ambiente.Ambiente')),
                ('especificacion_de_inmueble', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccion.EspecificacionDeInmueble')),
            ],
            options={
                'verbose_name_plural': 'Ambientes por tipos de inmueble',
                'verbose_name': 'Ambiente por tipo inmueble',
                'ordering': ['especificacion_de_inmueble', 'ambiente'],
            },
        ),
    ]
