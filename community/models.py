from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):

    state = models.BooleanField(verbose_name="状态", default=True)

    create_time = models.DateTimeField(verbose_name="新增时间", auto_now_add=True)

    update_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)

    del_time = models.DateTimeField(verbose_name="删除时间", blank=True, null=True)

    class Meta:
        abstract = True


class Community(BaseModel):
    name = models.CharField(verbose_name="小区名称", max_length=100)

    address = models.CharField(verbose_name="坐落地址", max_length=200)

    area = models.FloatField(verbose_name="占地面积")

    build_name = models.CharField(verbose_name="开发商名称", max_length=100)

    company = models.CharField(verbose_name="物业公司名称", max_length=100)

    greening_rate = models.FloatField(verbose_name="绿化率")

    # 该小区总共的楼栋数量
    building_num = models.IntegerField(verbose_name="总栋数")

    # 小区可以容纳的总户数
    houses_num = models.IntegerField(verbose_name="总户数")

    # 小区状态、显示 还是隐藏
    status = models.BooleanField(verbose_name="小区状态(1显示、0隐藏)", default=True)

    # 小区缩略图
    thumbnail = models.CharField(verbose_name="缩略图", max_length=200)

    descp = models.TextField(verbose_name="小区介绍")

    code = models.CharField(verbose_name="小区编码", max_length=16, null=True, blank=True)

    # 小区管理员、提取 User中的数据
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, blank=True, null=True,
                             related_name="communitys")

    class Meta:
        db_table = "t_community"
