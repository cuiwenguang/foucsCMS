# encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    '''会员扩展信息'''
    user = models.OneToOneField(User)
    pya_pwd = models.CharField(max_length=50)  # 支付提现密码
    location = models.CharField(max_length=50, null=True, blank=True) # 所在地
    avatar = models.CharField(max_length=255) # 头像
    job = models.CharField(max_length=50, null=True, blank=True) # 工作
    mobile = models.CharField(max_length=20, null=True, blank=True) # 电话
    integral = models.IntegerField(default=0) # 资产（积分）
    paypal = models.CharField(max_length=50) # 网银账号


class Favorite(models.Model):
    '''收藏'''
    user_id = models.IntegerField(null=True, blank=True)
    user_name = models.CharField(max_length=50, null=True, blank=True)
    article_id = models.IntegerField()
    collect_date = models.DateTimeField(default=timezone.now)


class Subscribe(models.Model):
    '''我订阅的频道'''
    user_id = models.IntegerField(null=True, blank=True)
    user_name = models.CharField(max_length=50, null=True, blank=True)
    channel_id = models.IntegerField()
    channel_name = models.CharField(max_length=50)