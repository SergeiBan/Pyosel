from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Animal(models.Model):
    city = models.CharField(max_length=128)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='animals')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='offspring', null=True)
    SPECIES_OPTIONS = (
        ('dogs', 'Собаки'),
        ('cats', 'Кошки')
    )
    species = models.CharField(max_length=32, choices=SPECIES_OPTIONS)
    name = models.CharField(max_length=32)
    breed = models.CharField(max_length=64)
    description = models.CharField(max_length=2000, blank=True, null=True)
    color = models.CharField(max_length=32, blank=True, null=True)

    on_sale = models.BooleanField(default=False)
    price = models.IntegerField()
    free_to_take = models.BooleanField(default=False)


class AnimalPhoto(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='animals')