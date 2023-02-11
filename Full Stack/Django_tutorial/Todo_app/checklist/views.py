from django.shortcuts import render, redirect
from .models import CheckList, UserModel, User
from django.contrib.auth import authenticate, login

# Create your views here.


def index(request):
    user = request.user
    context = {
        'checklists': CheckList.objects.all().filter(User=user)
    }
    return render(request, 'index.html', context)


def signin(request):
    context = {
        "Error": False,
        "Status": ''
    }
    user = request.user
    if user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            return redirect("index")
        else:
            context["Error"] = True
            context["Error_msg"] = "Username or Password is Incorrect"
            context['Status'] = "is-invalid"

    return render(request, 'signin.html', context)


def signup(request):
    context = {

    }
    user = request.user
    if user.is_authenticated:
        redirect('index')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')
        email = request.Post.get('email')
        phone = request.Post.get('phone')
        try:
            user = UserModel.objects.create(
                username=username, password=password, email=email, phone=phone)
            user.save()
            login(request, user=user)
            return redirect('index')
        except:
            context

    return render(request, "signup.html", context)


