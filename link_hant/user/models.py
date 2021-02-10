from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(
        null=True,
        max_length=20,
        verbose_name="User phone number."
    )
    sex = models.CharField(
        null=True,
        max_length=1,
        verbose_name="Sex."
    )
