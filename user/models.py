from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.IntegerField()
    age = models.IntegerField()
    location = models.CharField(max_length=200, default=True)