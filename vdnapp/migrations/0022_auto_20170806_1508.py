# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 15:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vdnapp', '0021_auto_20170610_0655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annotation',
            old_name='metadata_text',
            new_name='text',
        ),
    ]
