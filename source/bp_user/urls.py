# -*- coding:utf-8 -*-
from django.conf.urls import url, patterns
from bp_user.views import RegisterAccount, UserLogin

urlpatterns = patterns("bp_user.views",
    url(r"^register/$", RegisterAccount.as_view(), name="register-account"),
    url(r"^login/$", UserLogin.as_view(), name="user-login"),
)