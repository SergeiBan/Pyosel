from rest_framework import serializers
from animals.models import Animal, LostProfile
from rest_framework.validators import UniqueTogetherValidator


class LostProfileSerializer(serializers.Serializer):
    loss_city_part = serializers.CharField(max_length=128, required=False)
    loss_street = serializers.CharField(max_length=128, required=False)
    loss_date = serializers.DateField(required=False)
    bounty = serializers.IntegerField(required=False)

    class Meta:
        model = LostProfile
        fields = (
            'animal', 'loss_city_part', 'loss_street', 'loss_date', 'bounty'
        )

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

    lost_profile = LostProfileSerializer(required=False)

    class Meta:
        model = Animal
        fields = (
            'pk', 'city', 'owner', 'species', 'breed',
            'features', 'hue', 'size', 'avatar', 'avatar_thumbnail',
            'aux_photo',
            'lost_profile'
        )
    
    def create(self, validated_data):
        lost_profile = validated_data.pop('lost_profile', None)
        new_animal = Animal.objects.create(
            avatar_thumbnail=validated_data['avatar'], **validated_data)
        
        if lost_profile:
            LostProfile.objects.create(animal=new_animal.pk, **lost_profile)
        return new_animal


class OwnershipProfileSerializer(serializers.Serializer):
    parent = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = (
            'nickname', 'age', 'parent'
        )

