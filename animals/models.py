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
    breed = models.CharField(max_length=64, blank=True, null=True)
    features = models.TextField(max_length=2000, blank=True, null=True)
    hue = models.CharField(max_length=32, blank=True, null=True)
    size = models.CharField(max_length=32)

    # price = models.IntegerField(blank=True, null=True)

    avatar = ResizedImageField(
        size=[1920, 1080], upload_to='animals', quality=50, blank=True, null=True)
    avatar_thumbnail = ResizedImageField(
        size=[360, 360], upload_to='animals', quality=50, blank=True, null=True)
    aux_photo = models.ImageField(upload_to='animals', blank=True, null=True)


class LostProfile(models.Model):
    animal = models.OneToOneField(
        Animal, on_delete=models.CASCADE, related_name='lost_profile')
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


class PersonalProfile(models.Model):
    nickname = models.CharField(max_length=32)
    age = models.CharField(max_length=32)
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, related_name='offspring',
        blank=True, null=True)

