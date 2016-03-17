# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('visible', models.BooleanField(default=None)),
                ('desplegable', models.IntegerField()),
                ('numero_de_columna', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('orden', models.IntegerField()),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Widget',
                'ordering': ['nombre'],
                'verbose_name_plural': 'Widgetes',
            },
        ),
        migrations.AlterUniqueTogether(
            name='widget',
            unique_together=set([('usuario', 'nombre')]),
        ),
    ]
