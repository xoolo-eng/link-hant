from django.urls import path
from blog import views as blog


urlpatterns = [
    path("", blog.records, name="blog_records"),
]
