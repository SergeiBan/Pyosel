from rest_framework import viewsets
from animals.models import Animal, LostProfile
from animals.serializers import AnimalSerializer, LostProfileSerializer
from animals.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    filterset_fields = ['city']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FoundViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LostProfile.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = (AllowAny,)


class LostProfileViewSet(viewsets.ModelViewSet):
    queryset = LostProfile.objects.all()
    serializer_class = LostProfileSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)