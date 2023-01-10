from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Animal(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='animals')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='offspring', null=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=1000, blank=True, null=True)
    color = models.CharField(max_length=32, blank=True, null=True)
    
