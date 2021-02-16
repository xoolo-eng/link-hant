from django.shortcuts import render
from blog.models import Blog


def records(request, page_id):
    count = 3
    start = count * page_id - count
    context = {"records": Blog.objects.all()[start:start+count]}
    return render(request, "blogs.html", context)


def record(request, blog_id):
    pass