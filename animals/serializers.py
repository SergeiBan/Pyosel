from rest_framework import serializers
from animals.models import Animal, AnimalPhoto
from rest_framework.validators import UniqueTogetherValidator


class AnimalPhotoSerializer(serializers.ModelSerializer):
    animal = serializers.PrimaryKeyRelatedField(queryset=Animal.objects.all())

    class Meta:
        model = AnimalPhoto
        fields = ('animal', 'photo', 'is_avatar')


class AnimalSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())
    avatar = serializers.ImageField(required=False)
    aux_photo = serializers.ImageField(required=False)

    class Meta:
        model = Animal
        fields = (
            'pk', 'city', 'owner', 'parent', 'species', 'name', 'breed',
            'description', 'color', 'price', 'status', 'avatar', 'aux_photo'
        )
        validators = [
            UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('owner', 'name', 'species'),
                message='У вас уже есть подобное животное с такой же кличкой'
            )
        ]
