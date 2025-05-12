from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)

    REQUIRED_FIELDS = ['email', 'phone_number', 'age']
    USERNAME_FIELD = 'username'  # unaweza kubadilisha kuwa 'email' kama unataka email iwe login key

    def __str__(self):
        return self.username
