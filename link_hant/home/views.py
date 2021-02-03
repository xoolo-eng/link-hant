from django.shortcuts import render


def home_page(request):
    context = {}
    return render(request, "home.html", context)


def about_page(request):
    context = {}
    return render(request, "about.html", context)


def contact_page(request):
    context = {}
    return render(request, "contact.html", context)