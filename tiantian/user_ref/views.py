# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponseRedirect
from models import UserInfo
from hashlib import sha1

# Create your views here.
def register(request):
    content={'title':'注册'}
    return render(request,'user_ref/register.html',content)
def login(request):
    uname=request.COOKIES.get("uname")
    context = {"title": "登录", "error_name": 0, "error_pwd": 0, "uname":uname}
    return render(request,'user_ref/login.html',context)
'''注册验证'''
def zhuce_yanzheng(request):


    uname=request.GET.get('uname')
    count=UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count': count})
'''注册信息保存'''
def register_saveInfo(request):
    post=request.POST
    uname=post.get('user_name')
    upwd=post.get('pwd')
    cpwd=post.get('cpwd')
    uemail=post.get('email')
    count = UserInfo.objects.filter(uname=uname).count()
    if upwd!=cpwd :
       return redirect('/user/register/')
    # elif count==1:
    #     return redirect('/user/register/?erroinfo=exist')
    else:
        s=sha1()
        s.update(upwd)
        upwd1=s.hexdigest()
        user=UserInfo()
        user.uname=uname
        user.upwd=upwd1
        user.uemail=uemail
        user.save()

        return redirect('/user/login/')
'''登录验证'''
def login_yanzheng(request):
    post=request.POST
    uname=post.get('username')
    upwd=post.get('pwd')
    jizhu=post.get('jizhu',0)
    user=UserInfo.objects.filter(uname=uname)
    if len(user)==1:
        s=sha1()
        s.update(upwd)
        upwd1=s.hexdigest()
        if upwd1==user[0].upwd:
            red=HttpResponseRedirect('/user/info/')
            if jizhu!=0:
                red.set_cookie("uname",uname)
            else:
                red.set_cookie("uname","",max_age=-1)
            request.session['user_id']=user[0].id
            request.session['uname']=uname
            return red
        else:
            context={"title":"登录","error_name":0,"error_pwd":1,"uname":uname,"upwd":upwd}
            return render(request,"user_ref/login.html",context)
    else:
        context={"title":"登录","error_name":1,"error_pwd":0,"uname":uname,"upwd":upwd}
        return render(request, "user_ref/login.html", context)

def info(requset):
    uname=requset.session["uname"]
    uadress=requset.session
    context={}
    return render(requset,'user_ref/user_center_info.html')
def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        user.ushou = post.get('ushou')
        user.uaddress = post.get('uaddress')
        user.uphone = post.get('uphone')
        user.uyoubian = post.get('uyoubian')
        user.save()
    context = {'title': '用户中心', 'user': user,'page_name':1,'site':1}
    return render(request, 'user_ref/user_center_site.html', context)
def order(request):
    context = {'title': '用户中心', 'page_name': 1, 'order': 1}
    return render(request, 'user_ref/user_center_order.html', context)