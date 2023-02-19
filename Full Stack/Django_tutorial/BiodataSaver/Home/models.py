from django.db import models
# Create your models here.


class StudentBio(models.Model):
    Email = models.EmailField()
    Name = models.CharField(max_length=255)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=1)

    @classmethod
    def search(cls, text):
        return cls.objects.filter(Name__contains=text)

    @classmethod
    def sort(cls):
        return cls.objects.all().order_by('Name', 'Email')

    def __str__(self):
        return self.Name
