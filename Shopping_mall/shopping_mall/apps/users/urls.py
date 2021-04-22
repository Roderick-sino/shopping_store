# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   : urls.py
@Contact: xxx
@Usage  : xxxxxx
@Modify Time        @Author        @Version        @Desciption
------------        -------        --------        -----------
2021/4/7 21:25     xxxxxxxxx      1.0             None
@TODO   :
"""
from . import views
from django.urls import re_path
from .views import RegisterView

urlpatterns = [
    # 用户注册: reverse(user:register)=='/register/'
    re_path(r'^register/$', views.RegisterView.as_view(), name='register'),
    
]
