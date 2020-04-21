from .models import Fridge
from rest_framework import viewsets, permissions
from .serializers import FridgeSerializer

# Fridge Viewset


class FridgeViewSet(viewsets.ModelViewSet):
    queryset = Fridge.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FridgeSerializer

