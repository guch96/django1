# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-07 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods_ref', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='gclick',
            field=models.IntegerField(default=0),
        ),
    ]