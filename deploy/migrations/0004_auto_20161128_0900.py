# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-28 01:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0003_auto_20161128_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deploy',
            name='hostip',
            field=models.CharField(max_length=100, verbose_name='ip'),
        ),
    ]
