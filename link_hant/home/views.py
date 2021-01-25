from django.shortcuts import render, HttpResponse


def home_page(request):
    return HttpResponse("<div>text</div>")