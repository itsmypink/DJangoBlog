# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-08-08 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20180808_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
