#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/9/29 14:17 
# @Author : Administrator 
# @Version：V 0.1
# @File : urls.py
# @desc :
from django.urls import path
from . import views

app_name = "community"

urlpatterns = [

    path('list', views.list, name="list"),

    path('add', views.add, name="add"),

    path('upload', views.upload, name="upload"),

    path('data', views.list_data, name="data"),

    path('batch_del', views.batch_del, name="batch_del"),

    path('<int:pk>/status/<int:status>', views.status_update, name='status'),

    path('update', views.update, name="update"),

]
