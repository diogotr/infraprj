from django.db import models
from django.contrib.auth.models import AbstractUser

class Contact(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=20)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class User(AbstractUser):
    email = models.EmailField(unique=True)