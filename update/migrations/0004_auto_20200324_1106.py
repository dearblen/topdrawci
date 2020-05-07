# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-03-24 11:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('update', '0003_history_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='history_version',
            name='c_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='history_version',
            name='u_time',
            field=models.DateTimeField(auto_now_add=True, default=123),
            preserve_default=False,
        ),
    ]
