from .models import Fridge
from rest_framework import viewsets, permissions
from .serializers import FridgeSerializer, Fridge2Serializer

# Fridge Viewset


class FridgeViewSet(viewsets.ModelViewSet):
    queryset = Fridge.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FridgeSerializer


class Fridge2ViewSet(viewsets.ModelViewSet):
    queryset = Fridge.objects.all().filter(id=1)
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Fridge2Serializer
