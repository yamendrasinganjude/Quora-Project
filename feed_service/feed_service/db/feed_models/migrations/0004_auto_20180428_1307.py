# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-28 13:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed_models', '0003_auto_20180421_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 28, 13, 7, 49, 627788)),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 28, 13, 7, 49, 627260)),
        ),
    ]