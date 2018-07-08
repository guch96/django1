# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CartInfo(models.Model):
    user=models.ForeignKey('user_ref.UserInfo')
    goods=models.ForeignKey('goods_ref.GoodsInfo')
    count=models.IntegerField(default=0)