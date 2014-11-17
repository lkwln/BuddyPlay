# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from utils.models import AbstractModel


class Room(AbstractModel):
    owner = models.ForeignKey(User, db_index=True, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    limits = models.SmallIntegerField(blank=True, null=True)
    price = models.SmallIntegerField(blank=True, null=True)
    LEVEL_CHOICES = (
        (0, u'普通桌'),
        (1, u'包房')
    )
    level = models.SmallIntegerField(choices=LEVEL_CHOICES, default=0)
    description = models.TextField(blank=True, null=True)

