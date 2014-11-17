# -*- coding:utf-8 -*-
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from bp_user.serializers import UserEx, User, UserExSimpleSerializer
from bp_user.account_util import create_user
from bp_user.authenticate_utils import login_success_process, login_helper
from utils import generalJsonResponse
from utils.errors import *
from rest_framework import status


class RegisterAccount(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        register_dict = request.DATA
        code, userex = create_user(register_dict)
        if userex is None:
            return generalJsonResponse(status=status.HTTP_400_BAD_REQUEST, code=code)
        return generalJsonResponse(status=status.HTTP_201_CREATED, code=SUCCESS)


class UserLogin(APIView):
    perm_exempt = True

    def post(self, request, *args, **kwargs):
        login_dict = request.DATA
        code, user = login_helper(login_dict)
        if code != SUCCESS:
            return generalJsonResponse(status=status.HTTP_400_BAD_REQUEST, code=code)
        else:
            rsp = login_success_process(user)
        return generalJsonResponse(status=status.HTTP_200_OK, code=SUCCESS, detail=rsp)