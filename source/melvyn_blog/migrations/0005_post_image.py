# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('melvyn_blog', '0004_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='null', upload_to=b'META_DATA'),
            preserve_default=False,
        ),
    ]
