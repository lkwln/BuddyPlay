# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User, Permission
from utils.models import AbstractModel
from activity.models import Activity

import os


def get_user_upload_path(path):
    def upload_callback(instance, filename):
        userex = UserEx.objects.get(user=instance.user)
        return os.path.join("user", userex.uuid, path, filename)
    return upload_callback


class MerchantEx(AbstractModel):
    user = models.OneToOneField(User, blank=True, null=True)
    parent = models.ForeignKey('MerchantEx', blank=True, null=True)   # 用于连锁店
    account_name = models.CharField(max_length=128, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    phone = models.CharField(max_length=14, blank=True, null=True)
    PROVINCES_CHOICES = (
        (1, u'北京'), (1, u'上海'), (1, u'天津'), (1, u'重庆'),
        # TODO: 待完善
    )
    province = models.SmallIntegerField(choices=PROVINCES_CHOICES, default=1)
    CITIES_CHOICES = (
        (1, u'北京'), (1, u'上海'), (1, u'天津'), (1, u'重庆'),
        # TODO: 待完善
    )
    city = models.SmallIntegerField(choices=CITIES_CHOICES, default=1)
    address = models.CharField(max_length=500, blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = [("longitude", "latitude", "user", "is_active")]

    def __unicode__(self):
        return u'Information for merchant %s<%s>' % (self.account_name, self.name)


class UserEx(AbstractModel):
    user = models.OneToOneField(User, blank=True, null=True)
    real_name = models.CharField(max_length=128, blank=True, null=True)
    account_name = models.CharField(max_length=128, blank=True, null=True)
    nick_name = models.CharField(max_length=128, blank=True, null=True)
    collections = models.ManyToManyField(MerchantEx, blank=True, null=True)  # 收藏商户
    collections_activity = models.ManyToManyField(Activity, blank=True, null=True, related_name="interesting_users")  # 收藏活动
    participate_activity = models.ManyToManyField(Activity, blank=True, null=True, related_name='participates')  # 参与活动
    USER_GENDER_CHOICE = (
        (0, u'male'),
        (1, u'female'),
    )
    gender = models.SmallIntegerField(choices=USER_GENDER_CHOICE, default=0)
    icon = models.ImageField(upload_to=get_user_upload_path, blank=True, null=True)
    phone = models.CharField(max_length=14, blank=True, null=True)
    NOT_BIND = 0
    BIND_ALREADY = 1
    BIND_STATUS = (
        (NOT_BIND, u'未绑定'),
        (BIND_ALREADY, u'已绑定')
    )
    bind_status = models.SmallIntegerField(choices=BIND_STATUS, default=NOT_BIND)

    def __unicode__(self):
        return u'extra information for user %s' % self.account_name