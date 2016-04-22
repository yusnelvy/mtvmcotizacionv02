# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenedor', '0005_contenedortipicopormueble_tipo_de_contenido'),
        ('cotizacionweb', '0004_auto_20160414_1529'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serviciomueble',
            old_name='porcentaje_complejidad',
            new_name='cantidad',
        ),
        migrations.RenameField(
            model_name='serviciomueble',
            old_name='descripcion_monto_servicio',
            new_name='descripcion_cantidad',
        ),
        migrations.RemoveField(
            model_name='cotizacionhistoricofecha',
            name='fecha_actual',
        ),
        migrations.RemoveField(
            model_name='cotizacionhistoricofecha',
            name='hora_actual',
        ),
        migrations.RemoveField(
            model_name='serviciomueble',
            name='complejidad_servicio',
        ),
        migrations.RemoveField(
            model_name='serviciomueble',
            name='incluido',
        ),
        migrations.RemoveField(
            model_name='serviciomueble',
            name='monto_servicio',
        ),
        migrations.RemoveField(
            model_name='serviciomueble',
            name='monto_servicio_asignado',
        ),
        migrations.AddField(
            model_name='contenedormueble',
            name='tipo_de_contenido',
            field=models.ForeignKey(to='contenedor.TipoDeContenido', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cotizacionhistoricofecha',
            name='fecha',
            field=models.DateTimeField(default='2016-04-01 00:00:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cotizacionservicio',
            name='cantidad_servicio',
            field=models.DecimalField(max_digits=7, decimal_places=2, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fechadecotizacion',
            name='obligatoria',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='cotizacionestado',
            name='fecha_registro',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
