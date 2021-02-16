from django.urls import path
from django.shortcuts import redirect
from user.views import login_page, logout_page


urlpatterns = [
    path("login/", login_page, name="user_login"),
    path("logout/", logout_page, name="user_logout"),
]
