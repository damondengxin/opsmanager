# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-28 00:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0002_deploy_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='deploy',
            name='status',
            field=models.IntegerField(choices=[(0, '禁用'), (1, '启用')],verbose_name='状态'),
            preserve_default=False,
        ),
    ]
