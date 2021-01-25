from django.urls import path
from home import views as home

urlpatterns = [
    path("", home.home_page, name="home_page"),
]