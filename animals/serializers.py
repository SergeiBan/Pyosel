from rest_framework import serializers
from animals.models import Animal, AnimalPhoto


class AnimalPhotoSerializer(serializers.ModelSerializer):
    # animal = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = AnimalPhoto
        fields = ('photo')


class AnimalSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())
    images = serializers.ListField(
        child=serializers.FileField(max_length=10000000, allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = Animal
        fields = (
            'pk', 'city', 'owner', 'parent', 'species', 'name', 'breed',
            'description', 'color', 'on_sale', 'price', 'free_to_take',
            'images'
        )

    def create(self, validated_data):
        # uploaded = self.context['request'].data['photos']
        uploaded = validated_data.pop('images')
        print(uploaded)
        animal = Animal.objects.create(**validated_data)

        photo_data = []
        if uploaded:
            for photo in photos:
                photo_data.append(AnimalPhoto(animal=animal, photo=photo))

        AnimalPhoto.objects.bulk_create(photo_data)

        if avatar:
            AnimalPhoto.objects.create(animal=animal, photo=photos)
        if photos:
            AnimalPhoto.objects.create(animal=animal, photo=photos)
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
