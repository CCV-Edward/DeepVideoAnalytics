# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 15:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0011_auto_20170806_0224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='region',
            old_name='metadata_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='tube',
            old_name='metadata_text',
            new_name='text',
        ),
    ]
