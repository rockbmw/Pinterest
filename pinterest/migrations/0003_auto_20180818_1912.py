# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-08-18 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinterest', '0002_auto_20180818_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
