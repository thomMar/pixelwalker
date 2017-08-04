# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-04 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0002_result_encoding_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='average_score',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='progress',
            field=models.IntegerField(null=True),
        ),
    ]
