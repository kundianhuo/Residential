#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/9/30 10:35 
# @Author : Administrator 
# @Version：V 0.1
# @File : middlewares.py.py
# @desc :
from django.http import HttpResponse, HttpResponseNotAllowed
from django.utils.deprecation import MiddlewareMixin
import json


class JsonRequestMiddleware(MiddlewareMixin):
    """
        自定义JsonRequestMiddleware处理 application/json的数据
    """
    http_methods_name = ["PUT", "DELETE", "POST"]

    def process_view(self, request, view, args, kwargs):
        # 获取请求的类型
        if request.content_type.startswith("application/json") and request.method in self.http_methods_name:
            json_text = request.body.decode()

            # 转成 对象 或者 列表
            request.JSON = json.loads(json_text)

        elif request.content_type.startswith("application/json") and not request.method in self.http_methods_name:

            return HttpResponseNotAllowed(permitted_methods=self.http_methods_name)
