# -*- coding:utf-8 -*-
from django.conf.urls import url, patterns
from order_system.views import OrderListCreateView

urlpatterns = patterns("order_system.views",
    url(r"^$", OrderListCreateView.as_view(), name="order-list-create"),
)