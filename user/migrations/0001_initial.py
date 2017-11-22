# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Voleto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField()),
                ('fecha', models.DateField()),
                ('ubicacion', models.CharField(max_length=40)),
                ('posi', models.CharField(choices=[(b'V', b'VIP'), (b'A', b'alto'), (b'M', b'medio'), (b'P', b'platino')], max_length=1)),
                ('use', models.ManyToManyField(null=True, to='log.UserModel')),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='voleto',
            field=models.ManyToManyField(null=True, to='user.Voleto'),
        ),
    ]
