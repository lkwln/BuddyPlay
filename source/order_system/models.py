# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from utils.models import AbstractModel
from bp_merchant.models import Room


class Orders(AbstractModel):
    STATUS_INITIAL = 1
    STATUS_PAYED = 2
    STATUS_EXPIRED = 3
    buyer = models.ForeignKey(User, blank=True, null=True)  # 玩家
    server = models.ForeignKey(Room, blank=True, null=True)  # 商户
    count = models.IntegerField(blank=True, null=True)
    pay = models.IntegerField(blank=True, null=True)
    STATUS_CHOICES = (
        (STATUS_INITIAL, u'未支付'),
        (STATUS_PAYED, u'已支付'),
        (STATUS_EXPIRED, u'过期未支付')
    )

    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=STATUS_INITIAL)
    expired_time = models.DateTimeField(blank=True, null=True)
