# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('gestiondedocumento', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('origen', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=250)),
                ('texto', models.TextField()),
                ('estado', models.CharField(max_length=100)),
                ('fecha_entrega', models.DateTimeField()),
                ('fecha_alerta', models.DateTimeField()),
                ('log', models.TextField(blank=True)),
                ('url', models.CharField(max_length=500)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='user')),
                ('user_origen', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='user_origen')),
            ],
            options={
                'verbose_name_plural': 'Notificaciones',
                'ordering': ['titulo'],
                'verbose_name': 'Notificación',
            },
        ),
        migrations.CreateModel(
            name='NotificacionEstado',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('observacion', models.TextField(blank=True)),
                ('predefinido', models.BooleanField(default=None)),
                ('estado_de_documento', models.ForeignKey(to='gestiondedocumento.EstadoDeDocumento')),
                ('notificacion', models.ForeignKey(to='notificacion.Notificacion')),
                ('usuario_registro', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Estados de la notificación',
                'ordering': ['notificacion', 'usuario_registro'],
                'verbose_name': 'Estado de la notificación',
            },
        ),
    ]
