from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "Home/index.html")


def about(request):
    context = {
        'number': range(1, 20),
        'number2': 4
    }
    return render(request, "Home/about.html", context)
