from django.db import models
from django.contrib.auth import get_user_model
from django_resized import ResizedImageField


User = get_user_model()


class Animal(models.Model):
    city = models.CharField(max_length=128)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='animals')

    SPECIES_OPTIONS = (
        ('dogs', 'Собаки'),
        ('cats', 'Кошки')
    )
    species = models.CharField(max_length=16, choices=SPECIES_OPTIONS)
    GENDER_OPTIONS = (
        ('M', 'М'),
        ('F', 'Ж')
    )

    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS)
    breed = models.CharField(max_length=64, blank=True, null=True)
    features = models.TextField(max_length=2000, blank=True, null=True)
    hue = models.CharField(max_length=32, blank=True, null=True)
    size = models.CharField(max_length=32)
    accessories = models.TextField(max_length=1000, blank=True, null=True)

    avatar = ResizedImageField(
        size=[1920, 1080], upload_to='animals', quality=50, blank=True, null=True)
    avatar_thumbnail = ResizedImageField(
        size=[360, 360], upload_to='animals', quality=50, blank=True, null=True)
    aux_photo = models.ImageField(upload_to='animals', blank=True, null=True)


class LostProfile(models.Model):
    animal = models.OneToOneField(
        Animal, on_delete=models.CASCADE, related_name='lost_profile')
    nickname = models.CharField(max_length=64)
    loss_city_part = models.CharField(max_length=128, blank=True, null=True)
    loss_street = models.CharField(max_length=128, blank=True, null=True)
    loss_date = models.DateField(blank=True, null=True)
    bounty = models.CharField(max_length=128, blank=True, null=True)


class FoundProfile(models.Model):
    animal = models.OneToOneField(
        Animal, on_delete=models.CASCADE, related_name='found_profile')
    found_city_part = models.CharField(max_length=128, blank=True, null=True)
    found_street = models.CharField(max_length=128, blank=True, null=True)
    found_date = models.DateField(blank=True, null=True)
