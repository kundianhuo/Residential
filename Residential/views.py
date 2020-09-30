#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/9/29 14:06 
# @Author : Administrator 
# @Version：V 0.1
# @File : views.py
# @desc :
from django.shortcuts import render


def index(request):
    return render(request, "index.html")
