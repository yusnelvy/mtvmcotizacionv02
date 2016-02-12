# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20160204_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relacion',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Relación',
                'verbose_name_plural': 'Relaciones',
            },
        ),
        migrations.AlterField(
            model_name='menu',
            name='menu',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='menu',
            name='transaccion',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='relacion',
            name='item_origen',
            field=models.ForeignKey(related_name='item_origen', to='menu.Menu'),
        ),
        migrations.AddField(
            model_name='relacion',
            name='item_relacion',
            field=models.ForeignKey(related_name='item_relacion', to='menu.Menu'),
        ),
    ]
