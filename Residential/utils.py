#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/9/29 15:17 
# @Author : Administrator 
# @Version：V 0.1
# @File : utils.py
# @desc :
import random, string
from django.conf import settings
import os

from django.core.files.uploadedfile import InMemoryUploadedFile


def write_upload_img(path, file: InMemoryUploadedFile):
    """
    将文件存储到磁盘
    :param path:  文件的存储路径、相对于 media
    :param file:  文件对象
    :return: 返回文件相对路径
    """
    # 获取文件的名称
    file_name = file.name

    # 获取文件的名 和 后缀
    index = file_name.rfind(".")
    _n = file_name if index == -1 else file_name[:index]
    _e = "" if index == -1 else file_name[index:]

    # 随机产生文件的后缀、防止重复
    _random_text = "".join(random.choices(string.ascii_letters, k=6))

    # 获取文件名
    file_name = _n + _random_text if index == -1 else _n + _random_text + _e

    # 判断跟目录是否存在
    if not os.path.exists(os.path.join(settings.MEDIA_ROOT, path)):
        os.makedirs(os.path.join(settings.MEDIA_ROOT, path))

    # 进行存储
    with open(os.path.join(settings.MEDIA_ROOT, path, file_name), "wb") as f:

        for chunk in file.chunks():
            f.write(chunk)

    return os.path.join(path, file_name)


def community_code():
    prefix = "".join(random.choices(string.ascii_uppercase, k=3))
    middle = "".join(random.choices(string.ascii_uppercase, k=2))
    suffix = "".join(random.choices(string.digits, k=5))

    return "{}-{}-{}".format(prefix, middle, suffix)
