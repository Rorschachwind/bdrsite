# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-31 03:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_auto_20171031_0303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agar',
            old_name='name',
            new_name='media',
        ),
    ]
