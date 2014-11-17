# -*- coding:utf-8 -*-
from rest_framework.authtoken.models import Token
from utils.errors import *
from bp_user.models import UserEx, User
from django.contrib.auth import authenticate


def login_helper(login_dict):
    login_name = login_dict.get("login_name", None)
    password = login_dict.get("password", None)
    if login_name is None:
        return LOGIN_ERROR_EMPTY_USERNAME, None
    if password is None:
        return LOGIN_ERROR_EMPTY_PASSWORD, None
    user = None
    userex = UserEx.objects.filter(account_name=login_name, is_active=True)
    if userex.exists():
        user = userex[0].user
    else:
        userex = UserEx.objects.filter(phone=login_name, bind_status=UserEx.BIND_ALREADY, is_active=True)
        if userex.exists():
            user = userex[0].user
    if user is None:
        return LOGIN_ERROR_INVALID_USERNAME, None
    else:
        user = authenticate(username=user.username, password=password)
        if user is None:
            return LOGIN_ERROR_WRONG_PASSWORD, None

    return SUCCESS, user


def disable_user_token(user):
    Token.objects.filter(user=user).delete()


def login_success_process(user):
    # 单点登录, 挤掉其他正在登录中的相同账号
    disable_user_token(user)
    userex = user.userex
    rsp = dict({
        "account_name": userex.account_name,
        "real_name": userex.real_name,
        "nick_name": userex.nick_name,
        "gender": userex.gender,
        "bind_status": userex.bind_status,
        "u_id": user.id,
        "ue_id": userex.id,
        "phone": userex.phone,
    })
    rsp['token'] = Token.objects.get_or_create(user=user)[0].key

    return rsp