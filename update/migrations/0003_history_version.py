# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-03-24 10:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('update', '0002_auto_20200324_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='history_version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(default='', max_length=128)),
                ('local_project_version_ship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='update.local_project_ship')),
            ],
            options={
                'verbose_name': '历史版本',
                'verbose_name_plural': '历史版本',
                'ordering': ['id'],
            },
        ),
    ]
