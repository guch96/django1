# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=100)),
                ('uemail', models.CharField(max_length=40)),
                ('uaddress', models.CharField(default='', max_length=100)),
                ('uyoubian', models.CharField(default='', max_length=6)),
                ('uphone', models.CharField(default='', max_length=11)),
            ],
        ),
    ]
