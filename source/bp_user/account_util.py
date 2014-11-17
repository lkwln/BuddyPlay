# -*- coding:utf-8 -*-
from bp_user.models import UserEx, User
from utils.errors import *


def validate(user_dict):
    account_name = user_dict.get("account_name", None)
    phone = user_dict.get("phone", None)
    if account_name is not None:
        if UserEx.objects.filter(account_name=account_name).exists():
            return CREATE_USER_ACCOUNT_NAME_EXISTS
    if phone is not None:
        if UserEx.objects.filter(phone=phone, bind_status=UserEx.BIND_ALREADY).exists():
            return CREATE_USER_ACCOUNT_PHONE_BIND_ALREADY
    return SUCCESS


def create_user(user_dict):
    code = validate(user_dict)
    if code != SUCCESS:
        return code, None
    real_name = user_dict.get("real_name", None)
    account_name = user_dict.get("account_name", None)
    nick_name = user_dict.get("nick_name", None)
    gender = user_dict.get("gender", None)
    phone = user_dict.get("phone", None)
    pwd = user_dict.get("password", None)

    username = None
    try:
        if account_name is not None:
            username = account_name
        elif phone is not None:
            username = phone
        if username is not None and pwd is not None:
            user = User.objects.create(username=username)
            user.set_password(pwd)
            user.save()
        else:
            return EMPTY_ACCOUNT_NAME_OR_PHONE, None

        userex = UserEx.objects.create(account_name=account_name, real_name=real_name,
                                       nick_name=nick_name, phone=phone)
        if gender is not None:
            userex.gender = gender
        userex.user = user
        if account_name is not None and phone is not None and account_name == phone:
            userex.bind_status = UserEx.BIND_ALREADY
        code = SUCCESS
        userex.save()
    except Exception, e:
        code = CREATE_USER_ERROR
        userex = None

    return code, userex