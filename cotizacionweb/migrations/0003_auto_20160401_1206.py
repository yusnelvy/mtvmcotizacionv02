# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacionweb', '0002_auto_20160331_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='como_abona',
            field=models.ForeignKey(null=True, to='cotizacionweb.TipoAbono', blank=True),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='cotizador',
            field=models.ForeignKey(null=True, to='cotizador.Cotizador', blank=True),
        ),
        migrations.AlterField(
            model_name='cotizaciondireccion',
            name='cantidad_de_ambientes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cotizaciondireccion',
            name='cantidad_pisos',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cotizaciondireccion',
            name='distancia_del_vehiculo',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cotizaciondireccion',
            name='especificacion_de_inmueble',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='cotizaciondireccion',
            name='nombre_de_edificio',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='cotizaciondireccion',
            name='nombre_piso',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='cotizaciondireccion',
            name='numero_de_inmueble',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='cotizaciondireccion',
            name='numero_de_pisos',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cotizaciondireccion',
            name='numero_de_plantas',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cotizaciondireccion',
            name='pisos_escalera',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cotizaciondireccion',
            name='pisos_por_escalera',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cotizaciondireccion',
            name='tipo_de_edificacion',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='cotizaciondireccion',
            name='total_m2',
            field=models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cotizaciondireccion',
            name='volumen_baulera',
            field=models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True),
        ),
    ]
