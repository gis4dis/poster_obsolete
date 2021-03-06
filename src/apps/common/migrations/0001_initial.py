# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-24 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_id', models.CharField(editable=False, help_text="Unique and computer-friendly name of the process. eg. ('measure' or 'avg_hour')", max_length=30, unique=True)),
                ('name', models.CharField(help_text='Human-readable name of the process.', max_length=50)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'processes',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_id', models.CharField(editable=False, help_text="Unique and computer-friendly name of the property. eg. ('precipitation' or 'air_temperature')", max_length=30, unique=True)),
                ('name', models.CharField(help_text='Human-readable name of the property.', max_length=30)),
                ('unit', models.CharField(help_text='Unit of observations (physical unit). Same for all observations of the property.', max_length=30)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'properties',
            },
        ),
    ]
