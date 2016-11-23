# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-23 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deploy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=100, verbose_name='项目名')),
                ('curentversion', models.CharField(max_length=100, verbose_name='当前版本')),
                ('deployhost', models.CharField(max_length=50, verbose_name='部署机器')),
                ('hostip', models.IntegerField(verbose_name='ip')),
                ('action', models.CharField(max_length=100, verbose_name='动作')),
            ],
        ),
    ]
