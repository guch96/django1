"""tiantian URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
import views
urlpatterns = [
url(r'^register/$',views.register,name='register'),
url(r'^register_saveInfo/$',views.register_saveInfo,name='saveInfo'),
url(r'^login/$',views.login,name='login'),
url(r'^zhuce_yanzheng/$',views.zhuce_yanzheng,name='Zhuceyanzheng'),
url(r'^login_yanzheng/$',views.login_yanzheng,name='Loginyanzheng'),
url(r'^info/$',views.info,name='info'),
url(r'^order/', views.order,name='order'),
url(r'^site/$', views.site,name='site'),
]
