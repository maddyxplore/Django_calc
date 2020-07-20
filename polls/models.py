from django.db import models
from django.contrib.auth.models import User

class Login(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phno = models.CharField(max_length=100)
    user = models.OneToOneField(User , on_delete=models.CASCADE)
