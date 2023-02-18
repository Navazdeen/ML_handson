from django.shortcuts import render, redirect
from .models import CheckList, UserModel, User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('signin')
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
        print(user)
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
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        try:
            user = UserModel.objects.create_user(
                username=username, password=password, email=email, phone=phone)
            user.save()
            login(request, user=user)
            return redirect('index')
        except:
            context

    return render(request, "signup.html", context)


def signout(request):
    context = {}
    if request.user.is_authenticated:
        logout(request)

    return redirect("signin")


def checklist_create(request):
    user = UserModel.objects.filter(username=request.user.username)[0]
    context = {}
    if request.method == "POST":
        title = request.POST.get('title')
        completed = request.POST.get('completed')
        completed = True if completed else False
        checklist = CheckList.objects.create(
            title=title, completed=completed, User=user)
        checklist.save()
        return redirect('index')
    return render(request, 'checklist.html', context)

def checklist_delete(request, id):
    checklist = CheckList.objects.filter(id=id).first()
    if checklist:
        checklist.delete()
    return redirect('index')

