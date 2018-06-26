# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *
# Create your views here.
# Create your views here.
# 查询每类商品最新的4个和点击率最高的4个
def index(request):
    """
      index函数负责查询页面中需要展示的商品内容，
      主要是每类最新的4种商品和4中点击率最高的商品，
      每类商品需要查询2次
      """
    fruit = GoodsInfo.objects.filter(gtype__id=1).order_by("-id")[:4]
    fruit2 = GoodsInfo.objects.filter(gtype__id=1).order_by("-gclick")[:3]
    fish = GoodsInfo.objects.filter(gtype__id=2).order_by("-id")[:4]
    fish2 = GoodsInfo.objects.filter(gtype__id=2).order_by("-gclick")[:3]
    meat = GoodsInfo.objects.filter(gtype__id=3).order_by("-id")[:4]
    meat2 = GoodsInfo.objects.filter(gtype__id=3).order_by("-gclick")[:4]
    egg = GoodsInfo.objects.filter(gtype__id=4).order_by("-id")[:4]
    egg2 = GoodsInfo.objects.filter(gtype__id=4).order_by("-gclick")[:4]
    vegetables = GoodsInfo.objects.filter(gtype__id=5).order_by("-id")[:4]
    vegetables2 = GoodsInfo.objects.filter(gtype__id=5).order_by("-gclick")[:4]
    frozen = GoodsInfo.objects.filter(gtype__id=6).order_by("-id")[:4]
    frozen2 = GoodsInfo.objects.filter(gtype__id=6).order_by("-gclick")[:4]
    context = {'title': '首页', 'fruit': fruit,
               'fish': fish, 'meat': meat, 'egg': egg,
               'vegetables': vegetables, 'frozen': frozen,
               'fruit2': fruit2, 'fish2': fish2, 'meat2': meat2,
               'egg2': egg2, 'vegetables2': vegetables2, 'frozen2': frozen2,
               'guest_cart': 1, 'page_name': 0, }
    return render(request,'goods_ref/index.html',context)
