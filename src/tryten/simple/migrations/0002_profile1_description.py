# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-10 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile1',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
