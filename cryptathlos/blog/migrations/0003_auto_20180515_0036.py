# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-15 00:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180515_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 15, 0, 36, 7, 396419, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 15, 0, 36, 7, 389740, tzinfo=utc)),
        ),
    ]
