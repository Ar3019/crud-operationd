from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class department(models.Model):
    title = models.CharField(max_length = 50)

    def __str__(self):
        return self.title

class Details(models.Model):
    name = models.CharField(max_length = 50)
    mobile_num = models.CharField(max_length = 10)
    age = models.CharField(max_length = 2)
    address = models.CharField(max_length = 255)
    department = models.ForeignKey(department, on_delete = models.CASCADE)
    email = models.EmailField(max_length = 255, unique = True)
    password = models.CharField(max_length = 50)
    # confirm_password = models.CharField(max_length = 50)

    USERNAME_FIELD = 'email'