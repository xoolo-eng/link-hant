from django.urls import path
from django.shortcuts import redirect
from blog import views as blog


urlpatterns = [
    path("all/<int:page_id>/", blog.records, name="blog_records"),
    path("single/<int:blog_id>/", blog.record, name="blog_record"),
    path("", lambda x: redirect("/blog/all/1/"))
]
