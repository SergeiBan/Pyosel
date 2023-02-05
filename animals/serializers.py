from rest_framework import serializers
from animals.models import Animal
from rest_framework.validators import UniqueTogetherValidator


class AnimalSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())
    avatar = serializers.ImageField(required=False)
    avatar_thumbnail = serializers.ImageField(read_only=True)
    aux_photo = serializers.ImageField(required=False)

    class Meta:
        model = Animal
        fields = (
            'pk', 'city', 'owner', 'parent', 'species', 'name', 'breed',
            'description', 'color', 'price', 'status', 'avatar',
            'avatar_thumbnail', 'aux_photo'
        )
        validators = [
            UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('owner', 'name', 'species'),
                message='У вас уже есть подобное животное с такой же кличкой'
            )
        ]

    def create(self, validated_data):
        new_animal = Animal.objects.create(
            avatar_thumbnail=validated_data['avatar'], **validated_data)
        print(new_animal.avatar_thumbnail)
        return new_animal
