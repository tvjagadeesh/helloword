# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-10 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple', '0003_profile1_loction'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile1',
            name='job',
            field=models.CharField(default='IT', max_length=128),
        ),
    ]
