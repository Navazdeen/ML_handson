from django.shortcuts import render
from .models import CheckList

# Create your views here.


def index(request):
    context = {
        'checklists': CheckList.objects.all()
    }
    return render(request, 'index.html', context)
