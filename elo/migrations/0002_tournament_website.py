# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='website',
            field=models.CharField(default='www.irb.com', max_length=400),
            preserve_default=False,
        ),
    ]
