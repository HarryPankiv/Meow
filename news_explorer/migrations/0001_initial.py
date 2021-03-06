# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-02 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('url_to_image', models.URLField()),
                ('publish_date', models.DateTimeField()),
            ],
        ),
    ]
