from django.db import models
from django.contrib.auth.models import User, UserManager
# Create your models here.


class UserModel(User, models.Model):
    phone = models.CharField(max_length=10)

    objects = UserManager()

    def __str__(self) -> str:
        return self.username


class CheckList(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField()
    created = models.DateField(auto_now_add=True)
    User = models.ForeignKey(to=UserModel, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.title
