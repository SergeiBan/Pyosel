from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import gettext_lazy as _
# from .managers import CustomUserManager


class CustomUser(AbstractUser):
    pass


class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    city = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=16)
