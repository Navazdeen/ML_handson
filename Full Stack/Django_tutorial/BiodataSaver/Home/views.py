from django.shortcuts import render
from .models import StudentBio

# Create your views here.
def index(request):
    if request.method == "POST":
        Email = request.POST.get("Email")
        Name = request.POST.get("Name")
        Age = request.POST.get("Age")
        Gender = request.POST.get("Gender")
        print(Email, Name, Age, Gender)

        student = StudentBio(Name=Name, Email=Email, Age=Age, Gender=Gender)
        student.save()
    return render(request, 'Home/index.html')