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
            name='Menu',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('menu', models.CharField(max_length=250, unique=True)),
                ('transaccion', models.CharField(max_length=20)),
                ('namespace', models.CharField(max_length=100, blank=True)),
                ('name', models.CharField(max_length=100, blank=True)),
                ('nivel', models.IntegerField()),
                ('padre', models.BooleanField(default=False)),
                ('menu_padre', models.ForeignKey(blank=True, to='menu.Menu', related_name='nenuchild_set')),
            ],
            options={
                'verbose_name': 'menu',
                'ordering': ['menu'],
                'verbose_name_plural': 'Menus',
            },
        ),
        migrations.CreateModel(
            name='MenuFavorito',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('grupo', models.CharField(max_length=100)),
                ('orden', models.IntegerField()),
                ('menu', models.ForeignKey(to='menu.Menu')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Menu favorito',
                'ordering': ['usuario', 'menu', 'grupo'],
                'verbose_name_plural': 'Menus favoritos',
            },
        ),
    ]
