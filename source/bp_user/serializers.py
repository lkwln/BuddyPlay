# -*- coding:utf-8 -*-
from rest_framework.serializers import ModelSerializer
from bp_user.models import User, UserEx


class UserExSimpleSerializer(ModelSerializer):

    class Meta:
        model = UserEx
        fields = ("user", "real_name", "account_name", "nick_name", "gender", "icon", "phone")