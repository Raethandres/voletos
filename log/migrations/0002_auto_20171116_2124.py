# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='cedula',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermodel',
            name='direccion',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermodel',
            name='email',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermodel',
            name='genero',
            field=models.CharField(default=None, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermodel',
            name='telefono',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
