# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-02 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_explorer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish_date',
            field=models.DateTimeField(null=True),
        ),
    ]
