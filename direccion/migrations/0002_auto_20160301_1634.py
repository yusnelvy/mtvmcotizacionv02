# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipodeedificacion',
            name='nombre',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='cantidad_de_inmuebles_por_piso',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='cantidad_de_pisos',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='distancia_del_vehiculo',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='escalera_estrecha',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='escalera_inclinada',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='escalon_grande',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='nombre_de_edificio',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='rampa',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='total_inmuebles',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='numero_de_pisos',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='numero_de_plantas',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='pisos_por_escalera',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='total_m2',
            field=models.DecimalField(blank=True, max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='volumen_baulera',
            field=models.DecimalField(blank=True, max_digits=8, decimal_places=3),
        ),
    ]
