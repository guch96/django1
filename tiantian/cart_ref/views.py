# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import *
from django.http import JsonResponse

from .models import CartInfo
from islogin import islogin
# Create your views here.
@islogin
def cart(request):
    userid=request.session['user_id']
    carts=CartInfo.objects.filter(user_id=userid)
    context={
        'title':'购物车',
        'page_name':1,
        'carts':carts


    }
    return render(request,'cart_ref/cart.html',context)
@islogin
def add(request,gid,gcount):
    #用户uid购买了gid商品，数量为count
    uid=request.session['user_id']
    gid = int(gid)
    count = int(gcount)
    carts_goods=CartInfo.objects.filter(user_id=uid)
    count1=1
    for cars in carts_goods:
        count1+=cars.count
    # print(count1)
    #查询购物车是否已经有此商品，有则增加
    carts = CartInfo.objects.filter(user_id=uid, goods_id=gid)
    if len(carts)>=1:
        cart=carts[0]
        cart.count=cart.count+count
    else:#不存在则直接加
        cart=CartInfo()
        cart.user_id=uid
        cart.goods_id=gid
        cart.count=count
    cart.save()
    #如果是ajax请求则返回json,否则转向购物车
    if request.is_ajax():
        count=CartInfo.objects.filter(user_id=request.session['user_id'])
        return JsonResponse({'count':count1})
    else:
        return redirect('/cart/')
@islogin
def count(request):
    uid= uid=request.session['user_id']
    carts_goods = CartInfo.objects.filter(user_id=uid)
    count1 = 0
    for car in carts_goods:
        count1 += car.count
    return JsonResponse({'count1': count1})
@islogin
def delete(request,cart_id):
    try:
        cart = CartInfo.objects.get(pk=int(cart_id))
        cart.delete()
        data = {'ok': 1}
    except Exception as e:
        data = {'ok': 0}
    return JsonResponse(data)
@islogin
def edit(request,cart_id,count):
    try:
        cart=CartInfo.objects.get(pk=int(cart_id))
        count1=cart.count=int(count)
        cart.save()
        data={'ok':0}
    except Exception as e:
        data={'ok':count1}
    return JsonResponse(data)