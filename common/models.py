from django.db import models


# Create your models here.
class Signin(models.Model):
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=15)
    password1 = models.CharField(max_length=15)

