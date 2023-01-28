from rest_framework import viewsets
from animals.models import Animal
from animals.serializers import AnimalSerializer
from animals.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.prefetch_related('photos').all()
    serializer_class = AnimalSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FoundViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Animal.objects.prefetch_related('photos').filter(status='found')
    serializer_class = AnimalSerializer
    permission_classes = (AllowAny,)
