# -*- coding:utf-8 -*-
from rest_framework import serializers

class GeneralResponse(object):
    def __init__(self, code, detail):
        self.code = code
        self.detail = detail


class GeneralResponseSerializer(serializers.Serializer):
    code = serializers.IntegerField()
    detail = serializers.CharField(max_length=200)