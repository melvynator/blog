# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 23:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('melvyn_blog', '0003_auto_20160520_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
