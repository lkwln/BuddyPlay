# -*- coding:utf-8 -*-
from django.db import models


class AbstractModel(models.Model):
    '''
    base class for all model
    '''
    is_active = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True