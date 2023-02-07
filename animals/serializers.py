from rest_framework import serializers
from animals.models import Animal, LostProfile
from rest_framework.validators import UniqueTogetherValidator





class AnimalSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())
    avatar = serializers.ImageField(required=False)
    avatar_thumbnail = serializers.ImageField(read_only=True)
    aux_photo = serializers.ImageField(required=False)
    breed = serializers.CharField(max_length=32, required=False)
    features = serializers.CharField(max_length=3000, required=False)
    hue = serializers.CharField(max_length=32, required=False)
    size = serializers.CharField(max_length=32, required=False)

    class Meta:
        model = Animal
        fields = (
            'pk', 'city', 'owner', 'species', 'breed',
            'features', 'hue', 'size', 'avatar', 'avatar_thumbnail',
            'aux_photo',
        )

    def create(self, validated_data):
        new_animal = Animal.objects.create(
            avatar_thumbnail=validated_data['avatar'], **validated_data)
        return new_animal


class LostProfileSerializer(serializers.ModelSerializer):
    animal = serializers.PrimaryKeyRelatedField(queryset=Animal.objects.all())
    loss_city_part = serializers.CharField(max_length=128, required=False, allow_null=True)
    loss_street = serializers.CharField(max_length=128, required=False, allow_null=True)
    loss_date = serializers.DateField(required=False, allow_null=True)
    bounty = serializers.CharField(required=False, allow_null=True)

    class Meta:
        model = LostProfile
        fields = (
            'animal', 'loss_city_part', 'loss_street', 'loss_date', 'bounty'
        )


class OutputLostProfileSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer()
    loss_city_part = serializers.CharField(max_length=128, required=False, allow_null=True)
    loss_street = serializers.CharField(max_length=128, required=False, allow_null=True)
    loss_date = serializers.DateField(required=False, allow_null=True)
    bounty = serializers.CharField(required=False, allow_null=True)

    class Meta:
        model = LostProfile
        fields = (
            'animal', 'loss_city_part', 'loss_street', 'loss_date', 'bounty'
        )


class FoundProfileSerializer(serializers.ModelSerializer):
    animal = serializers.PrimaryKeyRelatedField(queryset=Animal.objects.all())
    found_city_part = serializers.CharField(max_length=128, required=False, allow_null=True)
    found_street = serializers.CharField(max_length=128, required=False, allow_null=True)
    found_date = serializers.DateField(required=False, allow_null=True)

    class Meta:
        model = LostProfile
        fields = (
            'animal', 'loss_city_part', 'loss_street', 'loss_date', 'bounty'
        )


class OutputFoundProfileSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer()
    loss_city_part = serializers.CharField(max_length=128, required=False, allow_null=True)
    loss_street = serializers.CharField(max_length=128, required=False, allow_null=True)
    loss_date = serializers.DateField(required=False, allow_null=True)
    bounty = serializers.CharField(required=False, allow_null=True)

    class Meta:
        model = LostProfile
        fields = (
            'animal', 'loss_city_part', 'loss_street', 'loss_date', 'bounty'
        )
