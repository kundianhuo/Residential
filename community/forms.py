#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/9/29 16:08 
# @Author : Administrator 
# @Version：V 0.1
# @File : forms.py
# @desc :
from django.forms import ModelForm

from community.models import Community


class CommunityModelForm(ModelForm):
    class Meta:
        model = Community

        fields = "__all__"
