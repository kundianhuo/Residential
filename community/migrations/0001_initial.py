# Generated by Django 3.1.1 on 2020-09-29 07:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='新增时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('del_time', models.DateTimeField(blank=True, null=True, verbose_name='删除时间')),
                ('name', models.CharField(max_length=100, verbose_name='小区名称')),
                ('address', models.CharField(max_length=200, verbose_name='坐落地址')),
                ('area', models.FloatField(verbose_name='占地面积')),
                ('build_name', models.CharField(max_length=100, verbose_name='开发商名称')),
                ('company', models.CharField(max_length=100, verbose_name='物业公司名称')),
                ('greening_rate', models.FloatField(verbose_name='绿化率')),
                ('building_num', models.IntegerField(verbose_name='总栋数')),
                ('houses_num', models.IntegerField(verbose_name='总户数')),
                ('status', models.BooleanField(default=True, verbose_name='小区状态(1显示、0隐藏)')),
                ('thumbnail', models.CharField(max_length=200, verbose_name='缩略图')),
                ('descp', models.TextField(verbose_name='小区介绍')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='communitys', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 't_community',
            },
        ),
    ]
