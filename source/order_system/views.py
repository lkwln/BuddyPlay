# -*- coding:utf-8 -*-
from order_system.serializers import Orders, OrderSimpleSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class OrderListCreateView(ListCreateAPIView):
    model = Orders
    serializer_class = OrderSimpleSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )