# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from utils.models import AbstractModel
from bp_merchant.models import Room


class Activity(AbstractModel):
    creator = models.ForeignKey(User, blank=True, null=True)
    title = models.CharField(max_length=128, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    limits = models.SmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    server = models.ForeignKey(Room, blank=True, null=True)

    STATUS_INITIAL = 1
    STATUS_UNDERWAY = 2
    STATUS_CLOSED = 3
    STATUS_CHOICES = (
        (STATUS_INITIAL, u'征集玩家中'),
        (STATUS_UNDERWAY, u'已开始'),
        (STATUS_CLOSED, u'已结束')
    )
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=STATUS_INITIAL)

    def __unicode__(self):
        return u'activity object for <%s>' % self.title


class ActivityComment(AbstractModel):
    parent = models.ForeignKey('ActivityComment', blank=True, null=True)
    activity = models.ForeignKey(Activity, blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)
    text = models.TextField(blank=True, null=True)