from rest_framework import viewsets
from animals.models import Animal, LostProfile, FoundProfile
from animals.serializers import (
    AnimalSerializer, LostProfileSerializer, OutputLostProfileSerializer,
    FoundProfileSerializer, OutputFoundProfileSerializer)
from animals.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny
from django_filters import rest_framework as filters


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    filterset_fields = ['city']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LostProfileFilter(filters.FilterSet):
    city = filters.CharFilter(field_name='animal__city', lookup_expr='iexact')
    date = filters.DateFilter(field_name='loss_date', lookup_expr='lte')
    species = filters.CharFilter(field_name='animal__species', lookup_expr='exact')


class LostProfileViewSet(viewsets.ModelViewSet):
    queryset = LostProfile.objects.select_related('animal').all()
    serializer_class = LostProfileSerializer
    permission_classes = (AllowAny,)
    filterset_class = LostProfileFilter

    def get_serializer_class(self):
        if self.request.method in ('GET', 'LIST'):
            return OutputLostProfileSerializer
        else:
            return LostProfileSerializer


class FoundProfileViewSet(viewsets.ModelViewSet):
    queryset = FoundProfile.objects.select_related('animal').all()
    serializer_class = FoundProfileSerializer
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.request.method in ('GET', 'LIST'):
            return OutputFoundProfileSerializer
        else:
            return FoundProfileSerializer