from django.db import models
from django.contrib.auth import get_user_model
from django_resized import ResizedImageField


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
    breed = models.CharField(max_length=64, blank=True, null=True)
    features = models.TextField(max_length=2000, blank=True, null=True)
    hue = models.CharField(max_length=32, blank=True, null=True)
    size = models.CharField(max_length=32)

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

    # avatar = models.ImageField(upload_to='animals', blank=True, null=True)
    avatar = ResizedImageField(
        size=[1920, 1080], upload_to='animals', quality=50, blank=True, null=True)
    avatar_thumbnail = ResizedImageField(
        size=[360, 360], upload_to='animals', quality=50, blank=True, null=True)
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


class OwnedAnimal(models.Model):
    nickname = models.CharField(max_length=32)
    age = models.CharField(max_length=32)

    class Meta:
        abstract = True


class LostProfile(OwnedAnimal):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    loss_city_part = models.CharField(max_length=128, blank=True, null=True)
    loss_street = models.CharField(max_length=128, blank=True, null=True)
    loss_date = models.DateField()
    bounty = models.IntegerField(blank=True, null=True)
