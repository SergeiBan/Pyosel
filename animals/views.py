from rest_framework import viewsets, response, status
from rest_framework.decorators import action
from animals.models import Animal, LostProfile, FoundProfile
from animals.serializers import (
    AnimalSerializer, LostProfileSerializer, OutputLostProfileSerializer,
    FoundProfileSerializer, OutputFoundProfileSerializer)
from animals.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters import rest_framework as filters


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    filterset_fields = ['city']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(details=False, permission_classes=[IsAuthenticated])
    def owned_animals(self, request):
        queryset = Animal.objects.filter(owner=request.user)
        serializer = self.serializer_class(data=queryset, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class LostProfileFilter(filters.FilterSet):
    city = filters.CharFilter(field_name='animal__city', lookup_expr='iexact')
    date = filters.DateFilter(field_name='loss_date', lookup_expr='lte')
    species = filters.CharFilter(
        field_name='animal__species', lookup_expr='exact')
    gender = filters.CharFilter(
        field_name='animal__gender', lookup_expr='exact')


class FoundProfileFilter(filters.FilterSet):
    city = filters.CharFilter(field_name='animal__city', lookup_expr='iexact')
    date = filters.DateFilter(field_name='found_date', lookup_expr='gte')
    species = filters.CharFilter(
        field_name='animal__species', lookup_expr='exact')
    gender = filters.CharFilter(
        field_name='animal__gender', lookup_expr='exact')


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
    filterset_class = FoundProfileFilter

    def get_serializer_class(self):
        if self.request.method in ('GET', 'LIST'):
            return OutputFoundProfileSerializer
        else:
            return FoundProfileSerializer
