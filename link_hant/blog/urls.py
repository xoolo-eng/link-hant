from django.urls import path
from django.shortcuts import redirect
from blog import views as blog


urlpatterns = [
    path("<int:pk>/", blog.OneBlog.as_view(), name="blog_record"),
    path("", blog.AllBlogs.as_view(), name="blog_records")
]
