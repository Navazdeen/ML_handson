from django.shortcuts import render, redirect
from .models import StudentBio

# Create your views here.


def index(request):
    context = {
        'Students': StudentBio.objects.all()
    }
    if request.method == "POST":
        Email = request.POST.get("Email")
        Name = request.POST.get("Name")
        Age = request.POST.get("Age")
        Gender = request.POST.get("Gender")

        student = StudentBio(Name=Name, Email=Email, Age=Age, Gender=Gender)
        student.save()
    return render(request, 'Home/index.html', context)


def delete(request, id):
    to_del = StudentBio.objects.filter(id=id)
    if to_del:
        to_del.delete()

    return redirect('index')


def modify(request, id):
    to_modify = StudentBio.objects.filter(id=id)[0]
    Male, Female = ["", 'selected'] if to_modify.Gender == 'F' else [
        'selected', ""]
    context = {
        'student': to_modify,
        'Male': Male,
        'Female': Female,
    }
    if request.method == "POST":
        Email = request.POST.get("Email")
        Name = request.POST.get("Name")
        Age = request.POST.get("Age")
        Gender = request.POST.get("Gender")
        to_modify.Email = Email
        to_modify.Name = Name
        to_modify.Age = Age
        to_modify.Gender = Gender
        to_modify.save()
        return redirect('index')

    return render(request, 'Home/modify.html', context)
