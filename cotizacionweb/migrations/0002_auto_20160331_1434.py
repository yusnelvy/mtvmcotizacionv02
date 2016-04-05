# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenedor', '0002_auto_20160331_1430'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cotizador', '0001_initial'),
        ('cotizacionweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='cotizador',
            field=models.ForeignKey(to='cotizador.Cotizador'),
        ),
        migrations.AddField(
            model_name='contenedormueble',
            name='contenedor',
            field=models.ForeignKey(to='contenedor.Contenedor'),
        ),
        migrations.AddField(
            model_name='contenedormueble',
            name='cotizacion_mueble',
            field=models.ForeignKey(to='cotizacionweb.CotizacionMueble'),
        ),
        migrations.AddField(
            model_name='argumentodeventa',
            name='cotizacion',
            field=models.ForeignKey(to='cotizacionweb.Cotizacion'),
        ),
        migrations.AddField(
            model_name='abono',
            name='cotizacion',
            field=models.ForeignKey(to='cotizacionweb.Cotizacion'),
        ),
        migrations.AddField(
            model_name='abono',
            name='tipo_abono',
            field=models.ForeignKey(to='cotizacionweb.TipoAbono'),
        ),
        migrations.AddField(
            model_name='abono',
            name='usuario_registro',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
