# -*- coding:utf-8 -*-
from rest_framework.serializers import ModelSerializer
from order_system.models import Orders


class OrderSimpleSerializer(ModelSerializer):

    class Meta:
        model = Orders
        fields = ("buyer", "server", "count", "pay", "status", "expired_time")
