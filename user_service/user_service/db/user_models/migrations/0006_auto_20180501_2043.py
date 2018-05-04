# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-01 20:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_models', '0005_auto_20180501_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginentry',
            name='auth_token',
            field=models.CharField(default=b'8da47b1b-cd0e-4362-9d2c-c304adde4573', max_length=512),
        ),
        migrations.AlterField(
            model_name='loginentry',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 1, 20, 43, 32, 866797)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 1, 20, 43, 32, 864569)),
        ),
    ]