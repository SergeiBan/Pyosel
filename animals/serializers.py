from rest_framework import serializers
from animals.models import Animal, AnimalPhoto


class AnimalPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnimalPhoto
        fields = ('photo',)


class AnimalSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())
    # photos = AnimalPhotoSerializer(many=True)
    # photos = serializers.ImageField(max_length=None)

    class Meta:
        model = Animal
        fields = (
            'pk', 'city', 'owner', 'parent', 'species', 'name', 'breed',
            'description', 'color', 'on_sale', 'price', 'free_to_take',
            'avatar'
        )

    def create(self, validated_data):
        print(validated_data)
        photos = validated_data.pop('photos', None)
        animal = Animal.objects.create(**validated_data)

        photo_data = []
        # if photos:
        #     for photo in photos:
        #         photo_data.append(AnimalPhoto(animal=animal, photo=photo))

        # AnimalPhoto.objects.bulk_create(photo_data)

        # if avatar:
        #     AnimalPhoto.objects.create(animal=animal, photo=photos)
        return animal

    def update(self, instance, validated_data):
        photos = validated_data.pop('photos', None)
        instance.update(**validated_data)
        # animal = instance(**validated_data)

        if photos:
            AnimalPhoto.objects.all().delete()
            photo_data = []
            for photo in photos:
                photo_data.append(AnimalPhoto(animal=instance, photo=photo))
            AnimalPhoto.objects.bulk_create(photo_data)
        
        instance.save()
        return instance
        
