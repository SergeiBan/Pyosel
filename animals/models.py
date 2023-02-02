from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Animal(models.Model):
    city = models.CharField(max_length=128)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='animals')
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, related_name='offspring',
        blank=True, null=True)
    SPECIES_OPTIONS = (
        ('dogs', 'Собаки'),
        ('cats', 'Кошки')
    )
    species = models.CharField(max_length=16, choices=SPECIES_OPTIONS)
    name = models.CharField(max_length=32)
    breed = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(max_length=2000, blank=True, null=True)
    color = models.CharField(max_length=32, blank=True, null=True)

    price = models.IntegerField(blank=True, null=True)

    STATUS_OPTIONS = (
        ('boasting', 'Просто хвастаюсь'),
        ('free_to_take', 'Отдается'),
        ('on_sale', 'Продается'),
        ('lost', 'Потеряшка'),
        ('found', 'Найденыш')
    )
    status = models.CharField(
        max_length=16, choices=STATUS_OPTIONS, default='boasting')

    avatar = models.ImageField(upload_to='animals', blank=True, null=True)
    aux_photo = models.ImageField(upload_to='animals', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['owner', 'name', 'species'],
                name='unique_owner_name_species'
            )
        ]


class AnimalPhoto(models.Model):
    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='animals')
    is_avatar = models.BooleanField(default=False)
