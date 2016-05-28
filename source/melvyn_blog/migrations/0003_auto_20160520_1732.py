# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('melvyn_blog', '0002_post_co_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='co_author',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='null', upload_to=b''),
            preserve_default=False,
        ),
    ]