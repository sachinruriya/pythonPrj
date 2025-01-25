from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class Member(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True,blank=False)
    # username = models.CharField(max_length=100, unique=True)
    password  = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.username



