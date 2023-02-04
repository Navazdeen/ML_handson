from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CheckList(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField()
    created = models.DateField(auto_created=True)

    def __str__(self) -> str:
        return self.title


class UserModel(User, models.Model):
    checklist = models.ForeignKey(to=CheckList, on_delete=models.DO_NOTHING)
    phone = models.CharField(max_length=10)
