# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-02 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_explorer', '0002_auto_20171002_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
