# -*- coding:utf-8 -*-
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from utils.errors import get_code_detail
from utils.serializers import GeneralResponse, GeneralResponseSerializer


def generalResponseData(code, detail=None):
    if detail is None:
        detail = get_code_detail(code)
    serializer = GeneralResponseSerializer(GeneralResponse(code, detail))
    return serializer.data


def generalJsonResponse(status, code, detail=None):
    return HttpResponse(JSONRenderer().render(generalResponseData(code, detail)),
                        content_type="application/json", status=status)
